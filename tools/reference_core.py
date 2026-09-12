"""Deterministic, dependency-free Markdown integration engine.

The source repositories are never modified.  A manifest describes their
reading order, while this module performs the format conversion required for
one self-contained, portable Markdown document.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from fnmatch import fnmatchcase
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping
from urllib.parse import quote, unquote, urlsplit

from adapters import get_adapter


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPOSITORY_ROOT / "manifests"
LOCK_PATH = REPOSITORY_ROOT / "sources.lock.json"
LOCK_VERSION = 1
# Bump this whenever a generic rendering rule changes.  Source pins alone are
# insufficient because a renderer upgrade can legitimately change output even
# when upstream content remains at the same commit.
ENGINE_VERSION = "9"


class ReferenceError(RuntimeError):
    """An input or generated-document contract was not satisfied."""


@dataclass(frozen=True)
class PartSpec:
    """One source Markdown file in its reader-facing order."""

    path: str
    title: str
    empty_note: str | None = None


@dataclass(frozen=True)
class SectionSpec:
    title: str
    parts: tuple[PartSpec, ...]
    include_globs: tuple[str, ...] = ()
    exclude_paths: tuple[str, ...] = ()


@dataclass(frozen=True)
class Manifest:
    """Validated source and output configuration for one integrated book."""

    identifier: str
    title: str
    repository: str
    ref: str
    language: str
    adapter: str
    output: str
    authors: tuple[str, ...]
    tags: tuple[str, ...]
    sections: tuple[SectionSpec, ...]
    required_globs: tuple[str, ...]
    source_format: str
    article_class: str | None
    raw: dict[str, Any]

    def iter_parts(self) -> Iterable[PartSpec]:
        for section in self.sections:
            yield from section.parts


@dataclass(frozen=True)
class SourceSnapshot:
    """An immutable source checkout selected by an exact commit SHA."""

    manifest: Manifest
    root: Path
    commit: str
    commit_date: str
    published_at: str
    updated_at: str
    # A Git-tree index for the pinned commit.  Cache checkouts deliberately
    # materialize source Markdown only, so linked images and evidence files
    # usually do not exist in the sparse working tree.  Their immutable tree
    # entries are sufficient to validate and rewrite portable source URLs.
    repository_entries: Mapping[str, str] | None = None


MARKDOWN_IMAGE_TARGET = re.compile(
    r"(?P<prefix>!\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)(?P<rest>[^)]*\))"
)
MARKDOWN_IMAGE_LINE = re.compile(
    r"^(?P<prefix>\s*!\[)(?P<alt>(?:\\.|[^\]])*)(?P<suffix>\]\(.+\))\s*$"
)
# A caption must include a figure/table number.  Merely beginning with “图” is
# not enough: ordinary prose such as “图形可以……” is not a figure caption.
FIGURE_CAPTION = re.compile(
    r"^(?:(?:图|表)\s*\d+(?:[.．-]\d+)*|(?:fig(?:ure)?|table)\.?\s*\d+(?:[.．-]\d+)*).+",
    re.IGNORECASE,
)
GENERIC_IMAGE_ALT_TEXTS = frozenset(
    {
        "图片描述",
        "图像描述",
        "图片",
        "image description",
        "image placeholder",
    }
)
MARKDOWN_LINK_TARGET = re.compile(
    r"(?<!\!)\[(?P<label>[^\]]*)\]\((?P<target><[^>]+>|[^)\s]+)(?P<rest>[^)]*\))"
)
PANDOC_IMAGE_ATTRIBUTES = re.compile(
    r"(?P<image>!\[[^\]]*\]\((?:<[^>]+>|[^)\s]+)(?:[^)]*)\))\{[^{}\n]*\}"
)
HTML_IMAGE_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HTML_STRONG_TAG = re.compile(r"</?(?:strong|b)\b[^>]*>", re.IGNORECASE)
HTML_EMPHASIS_TAG = re.compile(r"</?(?:em|i)\b[^>]*>", re.IGNORECASE)
HTML_PARAGRAPH_TAG = re.compile(r"</?p\b[^>]*>", re.IGNORECASE)
HTML_ATTRIBUTE = re.compile(
    r"\b(?P<name>[a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*"
    r"(?:\"(?P<double>[^\"]*)\"|'(?P<single>[^']*)'|(?P<bare>[^\s>]+))",
    re.IGNORECASE,
)
ALIGN_DIV_TAG = re.compile(r"</?div\s+align\s*=\s*[\"']?center[\"']?\s*/?>", re.IGNORECASE)
BARE_DIV_CLOSE_TAG = re.compile(r"</div\s*>", re.IGNORECASE)
FIGURE_TAG = re.compile(r"</?figure(?:\s+[^>]*)?>", re.IGNORECASE)
FIGCAPTION_TAG = re.compile(r"</?figcaption(?:\s+[^>]*)?>", re.IGNORECASE)
FENCE_MARKER = re.compile(r"^\s*(?P<fence>`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})(\s+)(.*?)(\s*)$")
PANDOC_HEADING_ATTRIBUTES = re.compile(r"\s*\{[^{}\n]*\}\s*$")


def _require_string(value: object, name: str, origin: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ReferenceError(f"{origin}: {name} must be a non-empty string")
    return value.strip()


def _safe_relative(path: str, name: str, origin: str) -> str:
    value = _require_string(path, name, origin)
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ReferenceError(f"{origin}: {name} must remain inside its repository: {value}")
    return candidate.as_posix()


def manifest_from_data(data: object, origin: str = "manifest") -> Manifest:
    """Validate JSON manifest data and turn it into immutable configuration."""

    if not isinstance(data, dict):
        raise ReferenceError(f"{origin}: top-level JSON value must be an object")
    identifier = _require_string(data.get("id"), "id", origin)
    title = _require_string(data.get("title"), "title", origin)
    source = data.get("source")
    if not isinstance(source, dict):
        raise ReferenceError(f"{origin}: source must be an object")
    repository = _require_string(source.get("repository"), "source.repository", origin)
    ref = _require_string(source.get("ref"), "source.ref", origin)
    language = _require_string(data.get("language"), "language", origin)
    adapter = _require_string(data.get("adapter", "generic"), "adapter", origin)
    try:
        get_adapter(adapter)
    except ValueError as exc:
        raise ReferenceError(f"{origin}: {exc}") from exc
    output = _safe_relative(data.get("output"), "output", origin)
    if not output.endswith(".md"):
        raise ReferenceError(f"{origin}: output must end in .md")

    front_matter = data.get("front_matter", {})
    if not isinstance(front_matter, dict):
        raise ReferenceError(f"{origin}: front_matter must be an object")

    def string_array(value: object, name: str) -> tuple[str, ...]:
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise ReferenceError(f"{origin}: front_matter.{name} must be a non-empty string array")
        return tuple(item.strip() for item in value)

    authors = string_array(front_matter.get("authors"), "authors")
    tags = string_array(front_matter.get("tags"), "tags")

    sections_data = data.get("sections")
    if not isinstance(sections_data, list) or not sections_data:
        raise ReferenceError(f"{origin}: sections must be a non-empty array")
    sections: list[SectionSpec] = []
    for section_index, section_data in enumerate(sections_data, start=1):
        section_origin = f"{origin}: sections[{section_index}]"
        if not isinstance(section_data, dict):
            raise ReferenceError(f"{section_origin} must be an object")
        section_title = _require_string(section_data.get("title"), "title", section_origin)
        parts_data = section_data.get("parts")
        selection_data = section_data.get("selection")
        if (parts_data is None) == (selection_data is None):
            raise ReferenceError(f"{section_origin}: define exactly one of parts or selection")
        parts: list[PartSpec] = []
        include_globs: tuple[str, ...] = ()
        exclude_paths: tuple[str, ...] = ()
        if parts_data is not None:
            if not isinstance(parts_data, list) or not parts_data:
                raise ReferenceError(f"{section_origin}: parts must be a non-empty array")
            for part_index, part_data in enumerate(parts_data, start=1):
                part_origin = f"{section_origin}: parts[{part_index}]"
                if not isinstance(part_data, dict):
                    raise ReferenceError(f"{part_origin} must be an object")
                empty_note = part_data.get("empty_note")
                if empty_note is not None and not isinstance(empty_note, str):
                    raise ReferenceError(f"{part_origin}: empty_note must be a string")
                parts.append(
                    PartSpec(
                        path=_safe_relative(part_data.get("path"), "path", part_origin),
                        title=_require_string(part_data.get("title"), "title", part_origin),
                        empty_note=empty_note.strip() if empty_note else None,
                    )
                )
        else:
            if not isinstance(selection_data, dict):
                raise ReferenceError(f"{section_origin}: selection must be an object")
            include_data = selection_data.get("include_globs")
            if not isinstance(include_data, list) or not include_data:
                raise ReferenceError(f"{section_origin}: selection.include_globs must be a non-empty array")
            if not all(isinstance(item, str) for item in include_data):
                raise ReferenceError(f"{section_origin}: selection.include_globs must contain strings")
            exclude_data = selection_data.get("exclude_paths", [])
            if not isinstance(exclude_data, list) or not all(isinstance(item, str) for item in exclude_data):
                raise ReferenceError(f"{section_origin}: selection.exclude_paths must be a string array")
            include_globs = tuple(
                _safe_relative(item, "selection.include_globs entry", section_origin)
                for item in include_data
            )
            exclude_paths = tuple(
                _safe_relative(item, "selection.exclude_paths entry", section_origin)
                for item in exclude_data
            )
        sections.append(SectionSpec(section_title, tuple(parts), include_globs, exclude_paths))

    completeness = data.get("completeness", {})
    if not isinstance(completeness, dict):
        raise ReferenceError(f"{origin}: completeness must be an object")
    globs_data = completeness.get("required_globs", [])
    if not isinstance(globs_data, list) or not all(isinstance(item, str) for item in globs_data):
        raise ReferenceError(f"{origin}: completeness.required_globs must be a string array")
    required_globs = tuple(_safe_relative(item, "required_globs entry", origin) for item in globs_data)

    render = data.get("render", {})
    if not isinstance(render, dict):
        raise ReferenceError(f"{origin}: render must be an object")
    source_format = _require_string(render.get("source_format", "markdown"), "render.source_format", origin)
    if source_format not in {"markdown", "html_article"}:
        raise ReferenceError(f"{origin}: unsupported render.source_format: {source_format}")
    article_class = render.get("article_class")
    if source_format == "html_article":
        article_class = _require_string(article_class, "render.article_class", origin)
    elif article_class is not None:
        raise ReferenceError(f"{origin}: render.article_class is only valid for html_article")

    return Manifest(
        identifier=identifier,
        title=title,
        repository=repository,
        ref=ref,
        language=language,
        adapter=adapter,
        output=output,
        authors=authors,
        tags=tags,
        sections=tuple(sections),
        required_globs=required_globs,
        source_format=source_format,
        article_class=article_class,
        raw=data,
    )


def load_manifests() -> list[Manifest]:
    """Load every manifest in deterministic filename order."""

    paths = sorted(MANIFESTS_DIR.glob("*.json"))
    if not paths:
        raise ReferenceError(f"no manifests found under {MANIFESTS_DIR}")
    manifests = [manifest_from_data(json.loads(path.read_text(encoding="utf-8")), str(path)) for path in paths]
    identifiers = [manifest.identifier for manifest in manifests]
    duplicates = sorted({identifier for identifier in identifiers if identifiers.count(identifier) > 1})
    if duplicates:
        raise ReferenceError(f"duplicate manifest id(s): {', '.join(duplicates)}")
    return manifests


def select_manifests(targets: Iterable[str] | None) -> list[Manifest]:
    """Select requested manifests, failing on an unknown identifier."""

    manifests = load_manifests()
    wanted = set(targets or [])
    if not wanted:
        return manifests
    selected = [manifest for manifest in manifests if manifest.identifier in wanted]
    missing = wanted - {manifest.identifier for manifest in selected}
    if missing:
        raise ReferenceError(f"unknown manifest id(s): {', '.join(sorted(missing))}")
    return selected


def manifest_digest(manifest: Manifest) -> str:
    """Return a reproducible digest for the manifest contract."""

    canonical = json.dumps(manifest.raw, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def generator_version(manifest: Manifest) -> str:
    """Return the version of both the source adapter and generic renderer."""

    adapter = get_adapter(manifest.adapter)
    return f"{adapter.identifier}@{adapter.version};engine@{ENGINE_VERSION}"


def load_lock() -> dict[str, Any]:
    """Load the checked-in source pin file, or return an empty lock."""

    if not LOCK_PATH.exists():
        return {"version": LOCK_VERSION, "sources": {}}
    try:
        data = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ReferenceError(f"invalid JSON in {LOCK_PATH}: {exc}") from exc
    if not isinstance(data, dict) or data.get("version") != LOCK_VERSION:
        raise ReferenceError(f"{LOCK_PATH}: expected lock version {LOCK_VERSION}")
    if not isinstance(data.get("sources"), dict):
        raise ReferenceError(f"{LOCK_PATH}: sources must be an object")
    return data


def output_path(manifest: Manifest) -> Path:
    """Resolve a checked-in output path without allowing traversal."""

    path = (REPOSITORY_ROOT / manifest.output).resolve()
    try:
        path.relative_to(REPOSITORY_ROOT.resolve())
    except ValueError as exc:
        raise ReferenceError(f"output escapes this repository: {manifest.output}") from exc
    return path


def _source_path(snapshot: SourceSnapshot, relative: str) -> Path:
    path = (snapshot.root / relative).resolve()
    try:
        path.relative_to(snapshot.root.resolve())
    except ValueError as exc:
        raise ReferenceError(f"source path escapes checkout: {relative}") from exc
    return path


def _matches_repository_glob(path: str, pattern: str) -> bool:
    """Match a repository path against a slash-aware, anchored glob."""

    path_parts = PurePosixPath(path).parts
    pattern_parts = PurePosixPath(pattern).parts

    def match_at(path_index: int, pattern_index: int) -> bool:
        if pattern_index == len(pattern_parts):
            return path_index == len(path_parts)
        pattern_part = pattern_parts[pattern_index]
        if pattern_part == "**":
            return any(
                match_at(candidate, pattern_index + 1)
                for candidate in range(path_index, len(path_parts) + 1)
            )
        return (
            path_index < len(path_parts)
            and fnmatchcase(path_parts[path_index], pattern_part)
            and match_at(path_index + 1, pattern_index + 1)
        )

    return match_at(0, 0)


def _natural_path_key(path: str) -> tuple[tuple[int, object], ...]:
    """Sort source filenames numerically while retaining deterministic Unicode order."""

    return tuple(
        (0, int(piece)) if piece.isdecimal() else (1, piece.casefold())
        for piece in re.split(r"(\d+)", path)
    )


def _title_from_path(path: str) -> str:
    """Derive a concise reader heading for declaratively selected source files."""

    title = Path(path).stem.strip()
    return re.sub(r"^\d+\s+", "", title).strip() or title


def resolve_section_parts(section: SectionSpec, repository_entries: Mapping[str, str] | None) -> tuple[PartSpec, ...]:
    """Resolve explicit or declarative section sources from a pinned Git tree."""

    if section.parts:
        return section.parts
    if repository_entries is None:
        raise ReferenceError(f"{section.title}: declarative selection requires a Git tree index")
    candidates = [
        path
        for path, kind in repository_entries.items()
        if kind == "blob"
        and any(_matches_repository_glob(path, pattern) for pattern in section.include_globs)
        and path not in section.exclude_paths
    ]
    if not candidates:
        raise ReferenceError(f"{section.title}: selection matched no source files")
    return tuple(PartSpec(path=path, title=_title_from_path(path)) for path in sorted(candidates, key=_natural_path_key))


def resolved_sections(snapshot: SourceSnapshot) -> tuple[tuple[SectionSpec, tuple[PartSpec, ...]], ...]:
    """Return every section with source paths fixed by the snapshot's Git tree."""

    return tuple(
        (section, resolve_section_parts(section, snapshot.repository_entries))
        for section in snapshot.manifest.sections
    )


def selected_source_paths(manifest: Manifest, repository_entries: Mapping[str, str]) -> tuple[str, ...]:
    """Resolve all source paths before sparse checkout materializes their blobs."""

    paths: list[str] = []
    for section in manifest.sections:
        paths.extend(part.path for part in resolve_section_parts(section, repository_entries))
    if len(paths) != len(set(paths)):
        raise ReferenceError(f"{manifest.identifier}: source selected more than once")
    return tuple(paths)


def validate_manifest_sources(snapshot: SourceSnapshot) -> None:
    """Ensure all listed source files exist exactly once and globs are complete."""

    listed: set[str] = set()
    for _, parts in resolved_sections(snapshot):
        for part in parts:
            if part.path in listed:
                raise ReferenceError(f"{snapshot.manifest.identifier}: source listed more than once: {part.path}")
            listed.add(part.path)
            if not _source_path(snapshot, part.path).is_file():
                raise ReferenceError(f"{snapshot.manifest.identifier}: missing source: {part.path}")

    discovered: set[str] = set()
    if snapshot.repository_entries is None:
        for pattern in snapshot.manifest.required_globs:
            for path in snapshot.root.glob(pattern):
                if path.is_file():
                    discovered.add(path.relative_to(snapshot.root).as_posix())
    else:
        source_files = {
            path
            for path, kind in snapshot.repository_entries.items()
            if kind == "blob"
        }
        for pattern in snapshot.manifest.required_globs:
            discovered.update(
                path for path in source_files if _matches_repository_glob(path, pattern)
            )
    excluded = {
        path
        for section in snapshot.manifest.sections
        for path in section.exclude_paths
    }
    omitted = discovered - listed - excluded
    if omitted:
        names = ", ".join(sorted(omitted))
        raise ReferenceError(f"{snapshot.manifest.identifier}: source omitted from manifest: {names}")


def github_slug(repository: str) -> tuple[str, str]:
    """Extract owner/repository from an official GitHub repository URL."""

    value = repository.strip().rstrip("/")
    if value.endswith(".git"):
        value = value[:-4]
    if value.startswith("git@github.com:"):
        path = value.split(":", 1)[1]
    else:
        parsed = urlsplit(value)
        if parsed.hostname != "github.com":
            raise ReferenceError(f"only github.com repositories are currently supported: {repository}")
        path = parsed.path.strip("/")
    pieces = path.split("/")
    if len(pieces) != 2 or not all(pieces):
        raise ReferenceError(f"not a GitHub owner/repository URL: {repository}")
    return pieces[0], pieces[1]


def slugify(title: str) -> str:
    """Make stable anchors for the intentionally simple generated headings."""

    value = title.strip().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^\w\u3400-\u9fff\- ]+", "", value)
    value = re.sub(r"\s+", "-", value)
    return value.strip("-")


def split_target(target: str) -> tuple[str, str]:
    """Separate a local Markdown target from query or fragment suffixes."""

    match = re.match(r"([^?#]*)(.*)$", target)
    assert match is not None
    return match.group(1), match.group(2)


def is_external_target(target: str) -> bool:
    """Return whether a target should be preserved as-is."""

    return target.startswith(("#", "/", "data:")) or bool(re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target))


def _repository_entry_kind(snapshot: SourceSnapshot, relative: Path) -> str | None:
    """Return the pinned Git-tree kind for a repository-relative target."""

    if relative == Path("."):
        return "tree"
    if snapshot.repository_entries is not None:
        return snapshot.repository_entries.get(relative.as_posix())
    path = _source_path(snapshot, relative.as_posix())
    if not path.exists():
        return None
    return "tree" if path.is_dir() else "blob"


def _repository_relative_target(target: str, source: Path, snapshot: SourceSnapshot) -> tuple[Path, str] | None:
    path_text, suffix = split_target(target)
    if not path_text or is_external_target(path_text):
        return None

    def resolve_relative(value: str) -> Path | None:
        resolved = (source.parent / Path(unquote(value))).resolve()
        try:
            return resolved.relative_to(snapshot.root.resolve())
        except ValueError:
            return None

    relative = resolve_relative(path_text)
    if relative is not None and _repository_entry_kind(snapshot, relative) is not None:
        return relative, suffix
    # Some static-site exports keep a CDN resize suffix in the actual filename
    # (for example ``diagram.png?wh=1740*733``).  Prefer a normal URL query,
    # but fall back to that exact Git-tree path when no ordinary file exists.
    if suffix.startswith("?"):
        literal = resolve_relative(path_text + suffix)
        if literal is not None and _repository_entry_kind(snapshot, literal) is not None:
            return literal, ""
    return None


def _unique_repository_asset_target(target: str, snapshot: SourceSnapshot) -> tuple[Path, str] | None:
    """Recover a moved local image when its immutable basename is unique.

    Some static-site exports retain a relative path to a previous copy of the
    same course.  The path no longer resolves, but the image blob remains in
    the pinned repository under the course's current ``assets/`` directory.
    A basename fallback is safe only when exactly one blob in the Git tree has
    that name; ambiguous assets deliberately remain unresolved for review.
    """

    path_text, suffix = split_target(target)
    if not path_text or is_external_target(path_text):
        return None
    basename = Path(unquote(path_text)).name
    if not basename:
        return None
    if snapshot.repository_entries is not None:
        matches = [
            Path(path)
            for path, kind in snapshot.repository_entries.items()
            if kind == "blob" and Path(path).name == basename
        ]
    else:
        matches = [
            path.relative_to(snapshot.root)
            for path in snapshot.root.rglob(basename)
            if path.is_file()
        ]
    if len(matches) == 1:
        return matches[0], suffix
    return None


def _github_url(base: str, relative: Path, suffix: str = "") -> str:
    encoded = quote(relative.as_posix(), safe="/-._~!$&'()*+,;=:@")
    return f"{base}/{encoded}{suffix}"


def _is_snapshot_repository(owner: str, repository: str, snapshot: SourceSnapshot) -> bool:
    snapshot_owner, snapshot_repository = github_slug(snapshot.manifest.repository)
    return owner.lower() == snapshot_owner.lower() and repository.lower() == snapshot_repository.lower()


def _rewrite_pinned_raw_target(target: str, snapshot: SourceSnapshot) -> str | None:
    """Pin an absolute Raw URL when it already points at this source repository."""

    path_text, suffix = split_target(target)
    try:
        parsed = urlsplit(path_text)
    except ValueError:
        # Keep malformed third-party URLs untouched.  The integration must not
        # reject an otherwise valid source document merely because a reference
        # embeds unescaped brackets in its path.
        return None
    if parsed.scheme not in {"http", "https"} or parsed.hostname != "raw.githubusercontent.com":
        return None
    pieces = parsed.path.lstrip("/").split("/", 3)
    if len(pieces) != 4 or not _is_snapshot_repository(pieces[0], pieces[1], snapshot):
        return None
    owner, repository = github_slug(snapshot.manifest.repository)
    relative = Path(unquote(pieces[3]))
    return _github_url(
        f"https://raw.githubusercontent.com/{owner}/{repository}/{snapshot.commit}", relative, suffix
    )


def _rewrite_pinned_source_link(target: str, snapshot: SourceSnapshot) -> str | None:
    """Pin absolute GitHub blob/tree links that already point at this source."""

    path_text, suffix = split_target(target)
    try:
        parsed = urlsplit(path_text)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or parsed.hostname != "github.com":
        return None
    pieces = parsed.path.strip("/").split("/", 4)
    if len(pieces) != 5 or pieces[2] not in {"blob", "tree"}:
        return None
    if not _is_snapshot_repository(pieces[0], pieces[1], snapshot):
        return None
    owner, repository = github_slug(snapshot.manifest.repository)
    relative = Path(unquote(pieces[4]))
    return _github_url(
        f"https://github.com/{owner}/{repository}/{pieces[2]}/{snapshot.commit}", relative, suffix
    )


def rewrite_image_target(target: str, source: Path, snapshot: SourceSnapshot) -> str:
    """Turn an existing local asset into a SHA-pinned GitHub Raw URL."""

    pinned = _rewrite_pinned_raw_target(target, snapshot)
    if pinned is not None:
        return pinned
    resolved = _repository_relative_target(target, source, snapshot)
    if resolved is None:
        resolved = _unique_repository_asset_target(target, snapshot)
    if resolved is None:
        return target
    relative, suffix = resolved
    owner, repository = github_slug(snapshot.manifest.repository)
    return _github_url(
        f"https://raw.githubusercontent.com/{owner}/{repository}/{snapshot.commit}",
        relative,
        suffix,
    )


def rewrite_link_target(target: str, source: Path, snapshot: SourceSnapshot) -> str:
    """Turn an existing local document/directory link into a SHA-pinned source URL."""

    pinned = _rewrite_pinned_source_link(target, snapshot)
    if pinned is not None:
        return pinned
    resolved = _repository_relative_target(target, source, snapshot)
    if resolved is None:
        return target
    relative, suffix = resolved
    owner, repository = github_slug(snapshot.manifest.repository)
    kind = _repository_entry_kind(snapshot, relative)
    if kind is None:
        return target
    return _github_url(
        f"https://github.com/{owner}/{repository}/{kind}/{snapshot.commit}",
        relative,
        suffix,
    )


def html_attribute(tag: str, name: str) -> str | None:
    """Read a single HTML attribute from an image tag."""

    for match in HTML_ATTRIBUTE.finditer(tag):
        if match.group("name").lower() == name.lower():
            return next(
                value
                for value in (match.group("double"), match.group("single"), match.group("bare"))
                if value is not None
            )
    return None


def image_alt_text(raw_target: str) -> str:
    """Supply useful alt text when a source HTML image has none."""

    path_text, _ = split_target(raw_target)
    if path_text.startswith(("http://", "https://")):
        try:
            path_text = urlsplit(path_text).path
        except ValueError:
            pass
    stem = Path(unquote(path_text)).stem
    return stem or "image"


def markdown_image_alt_text(value: str) -> str:
    """Escape HTML alt text before placing it between Markdown brackets."""

    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def promote_caption_to_generic_image_alt(lines: list[str]) -> None:
    """Use an adjacent numbered figure caption to improve a placeholder alt.

    A number of sources write an image and its visible caption as neighbouring
    HTML blocks, but supply only a literal placeholder such as “图片描述” for
    the image alt attribute.  The visible caption remains intact; this adds
    the same useful description to Markdown's non-visual image text.
    """

    for index, line in enumerate(lines):
        image = MARKDOWN_IMAGE_LINE.match(line)
        if image is None or image.group("alt").strip().casefold() not in GENERIC_IMAGE_ALT_TEXTS:
            continue
        next_index = index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1
        if next_index == len(lines):
            continue
        caption = lines[next_index].strip()
        if not FIGURE_CAPTION.match(caption):
            continue
        lines[index] = f"{image.group('prefix')}{markdown_image_alt_text(caption)}{image.group('suffix')}"


def _html_image_to_markdown(tag: str, source: Path, snapshot: SourceSnapshot) -> str:
    raw_target = html_attribute(tag, "src")
    if raw_target is None:
        return tag
    target = rewrite_image_target(raw_target, source, snapshot)
    alt = markdown_image_alt_text(html_attribute(tag, "alt") or image_alt_text(raw_target))
    return f"![{alt}]({target})"


def rewrite_semantic_html(line: str) -> str:
    """Replace presentational HTML with standard Markdown inline syntax.

    Source chapters use these tags for formatting, not for semantic data or
    custom rendering.  Standard Markdown is more portable in a standalone
    file and avoids leaving a mixed HTML/Markdown document for readers.
    """

    def strong_replacer(match: re.Match[str]) -> str:
        return "**"

    def emphasis_replacer(match: re.Match[str]) -> str:
        return "*"

    line = HTML_STRONG_TAG.sub(strong_replacer, line)
    line = HTML_EMPHASIS_TAG.sub(emphasis_replacer, line)
    return HTML_PARAGRAPH_TAG.sub("", line)


def rewrite_assets(line: str, source: Path, snapshot: SourceSnapshot, align_div_closes: int = 0) -> str:
    """Rewrite Markdown/HTML images and local links while retaining captions."""

    converted_html_image = bool(HTML_IMAGE_TAG.search(line))
    converted_paragraph = bool(HTML_PARAGRAPH_TAG.search(line))

    def image_replacer(match: re.Match[str]) -> str:
        target = match.group("target")
        if target.startswith("<") and target.endswith(">"):
            target = f"<{rewrite_image_target(target[1:-1], source, snapshot)}>"
        else:
            target = rewrite_image_target(target, source, snapshot)
        return f"{match.group('prefix')}{target}{match.group('rest')}"

    def link_replacer(match: re.Match[str]) -> str:
        target = match.group("target")
        if target.startswith("<") and target.endswith(">"):
            target = f"<{rewrite_link_target(target[1:-1], source, snapshot)}>"
        else:
            target = rewrite_link_target(target, source, snapshot)
        return f"[{match.group('label')}]({target}{match.group('rest')}"

    line = MARKDOWN_IMAGE_TARGET.sub(image_replacer, line)
    line = PANDOC_IMAGE_ATTRIBUTES.sub(lambda match: match.group("image"), line)
    line = MARKDOWN_LINK_TARGET.sub(link_replacer, line)
    line = HTML_IMAGE_TAG.sub(lambda match: _html_image_to_markdown(match.group(0), source, snapshot), line)
    line = ALIGN_DIV_TAG.sub("", line)
    line = FIGURE_TAG.sub("", line)
    if align_div_closes:
        line = BARE_DIV_CLOSE_TAG.sub("", line, count=align_div_closes)
    line = FIGCAPTION_TAG.sub("", line)
    line = rewrite_semantic_html(line)
    return line.strip() if converted_html_image or converted_paragraph else line.rstrip()


@dataclass
class _HtmlNode:
    """A minimal HTML tree used only for configured article extraction."""

    tag: str
    attrs: dict[str, str]
    children: list[object]


class _ArticleHtmlParser(HTMLParser):
    """Parse a static HTML export without adding a third-party dependency."""

    _VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = _HtmlNode("root", {}, [])
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized = tag.lower()
        node = _HtmlNode(normalized, {name.lower(): value or "" for name, value in attrs}, [])
        self.stack[-1].children.append(node)
        if normalized not in self._VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        normalized = tag.lower()
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == normalized:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        self.stack[-1].children.append(data)


def _walk_html(nodes: Iterable[object]) -> Iterable[_HtmlNode]:
    for node in nodes:
        if isinstance(node, _HtmlNode):
            yield node
            yield from _walk_html(node.children)


def _html_plain_text(nodes: Iterable[object]) -> str:
    fragments: list[str] = []
    for node in nodes:
        if isinstance(node, str):
            fragments.append(node)
        elif isinstance(node, _HtmlNode):
            fragments.append(_html_plain_text(node.children))
    return "".join(fragments)


def _collapse_html_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _html_inline(nodes: Iterable[object], source: Path, snapshot: SourceSnapshot) -> str:
    fragments: list[str] = []
    for node in nodes:
        if isinstance(node, str):
            fragments.append(node)
            continue
        if not isinstance(node, _HtmlNode):
            continue
        tag = node.tag
        if tag in {"script", "style", "noscript"}:
            continue
        if tag == "br":
            fragments.append("  \n")
            continue
        if tag == "img":
            raw_target = node.attrs.get("src")
            if raw_target is None:
                continue
            target = rewrite_image_target(raw_target, source, snapshot)
            alt = markdown_image_alt_text(node.attrs.get("alt") or image_alt_text(raw_target))
            fragments.append(f"![{alt}]({target})")
            continue
        content = _html_inline(node.children, source, snapshot)
        if tag in {"strong", "b"}:
            fragments.append(f"**{content.strip()}**")
        elif tag in {"em", "i"}:
            fragments.append(f"*{content.strip()}*")
        elif tag == "code":
            fragments.append(f"`{content.strip()}`")
        elif tag == "a":
            target = node.attrs.get("href")
            label = _collapse_html_whitespace(content)
            if target and label:
                fragments.append(f"[{label}]({rewrite_link_target(target, source, snapshot)})")
            else:
                fragments.append(content)
        else:
            fragments.append(content)
    return "".join(fragments)


def _html_list(node: _HtmlNode, source: Path, snapshot: SourceSnapshot, depth: int = 0) -> str:
    """Render nested HTML lists into portable Markdown list items."""

    lines: list[str] = []
    items = [child for child in node.children if isinstance(child, _HtmlNode) and child.tag == "li"]
    for index, item in enumerate(items, start=1):
        nested = [child for child in item.children if isinstance(child, _HtmlNode) and child.tag in {"ul", "ol"}]
        text = _collapse_html_whitespace(
            _html_inline(
                (child for child in item.children if child not in nested),
                source,
                snapshot,
            )
        )
        marker = f"{index}." if node.tag == "ol" else "-"
        if text:
            lines.append(f"{'  ' * depth}{marker} {text}")
        for child in nested:
            lines.extend(_html_list(child, source, snapshot, depth + 1).splitlines())
    return "\n".join(lines)


def _html_blocks(nodes: Iterable[object], source: Path, snapshot: SourceSnapshot) -> list[str]:
    blocks: list[str] = []
    for node in nodes:
        if isinstance(node, str):
            text = _collapse_html_whitespace(node)
            if text:
                blocks.append(text)
            continue
        if not isinstance(node, _HtmlNode) or node.tag in {"script", "style", "noscript"}:
            continue
        tag = node.tag
        if tag in {"div", "section", "article", "main", "body"}:
            blocks.extend(_html_blocks(node.children, source, snapshot))
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            content = _collapse_html_whitespace(_html_inline(node.children, source, snapshot))
            if content:
                blocks.append(f"{'#' * int(tag[1])} {content}")
        elif tag == "p":
            content = _collapse_html_whitespace(_html_inline(node.children, source, snapshot))
            if content:
                blocks.append(content)
        elif tag in {"ul", "ol"}:
            content = _html_list(node, source, snapshot)
            if content:
                blocks.append(content)
        elif tag == "blockquote":
            content = "\n\n".join(_html_blocks(node.children, source, snapshot))
            if content:
                blocks.append("\n".join(f"> {line}" if line else ">" for line in content.splitlines()))
        elif tag == "pre":
            code = _html_plain_text(node.children).strip("\n")
            language = ""
            code_nodes = [child for child in node.children if isinstance(child, _HtmlNode) and child.tag == "code"]
            if code_nodes:
                for class_name in code_nodes[0].attrs.get("class", "").split():
                    if class_name.startswith("language-"):
                        language = class_name.removeprefix("language-")
                        break
            if code:
                blocks.append(f"```{language}\n{code}\n```")
        elif tag == "img":
            content = _collapse_html_whitespace(_html_inline([node], source, snapshot))
            if content:
                blocks.append(content)
        elif tag == "hr":
            blocks.append("---")
        else:
            content = _collapse_html_whitespace(_html_inline([node], source, snapshot))
            if content:
                blocks.append(content)
    return blocks


def html_article_to_markdown(document: str, article_class: str, source: Path, snapshot: SourceSnapshot) -> str:
    """Extract a configured static-site article container as portable Markdown."""

    parser = _ArticleHtmlParser()
    parser.feed(document)
    parser.close()
    article = next(
        (
            node
            for node in _walk_html(parser.root.children)
            if node.tag == "div" and article_class in node.attrs.get("class", "").split()
        ),
        None,
    )
    if article is None:
        raise ReferenceError(f"{snapshot.manifest.identifier}: missing HTML article container .{article_class}")
    blocks = _html_blocks(article.children, source, snapshot)
    if not blocks:
        raise ReferenceError(f"{snapshot.manifest.identifier}: HTML article container .{article_class} is empty")
    return "\n\n".join(blocks) + "\n"


def transform_part(part: PartSpec, snapshot: SourceSnapshot) -> str:
    """Lift a source chapter under a level-three generated part heading."""

    source = _source_path(snapshot, part.path)
    source_text = source.read_text(encoding="utf-8")
    if snapshot.manifest.source_format == "html_article":
        assert snapshot.manifest.article_class is not None
        source_text = html_article_to_markdown(source_text, snapshot.manifest.article_class, source, snapshot)
    lines = source_text.splitlines()
    result: list[str] = []
    in_fence = False
    align_div_depth = 0
    title_written = False
    previous_heading_level = 3

    for line in lines:
        if FENCE_MARKER.match(line):
            in_fence = not in_fence
            result.append(line.rstrip())
            continue
        if in_fence:
            # Line-ending whitespace has no meaning in a fenced block, while
            # leaving it intact makes generated output fail Git whitespace
            # checks and creates needless future diffs.
            result.append(line.rstrip())
            continue

        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            heading_text = PANDOC_HEADING_ATTRIBUTES.sub("", heading.group(3)).strip()
            if not title_written and level == 1:
                result.append(f"### {part.title}")
                title_written = True
                previous_heading_level = 3
            else:
                # Static-site HTML sometimes skips heading levels for visual
                # styling.  Preserve depth where possible, but fill a gap so
                # the portable document always has a valid outline.
                rendered_level = min(level + 2, 6, previous_heading_level + 1)
                result.append(f"{'#' * rendered_level} {heading_text}")
                previous_heading_level = rendered_level
            continue

        align_opens = len(ALIGN_DIV_TAG.findall(line))
        align_closes = len(BARE_DIV_CLOSE_TAG.findall(line))
        closings_to_remove = min(align_div_depth + align_opens, align_closes)
        align_div_depth += align_opens - closings_to_remove
        result.append(rewrite_assets(line, source, snapshot, closings_to_remove))

    promote_caption_to_generic_image_alt(result)
    if not title_written:
        result.insert(0, f"### {part.title}")
        if not lines and part.empty_note:
            result.append("")
            result.append(part.empty_note)
    return "\n".join(result).strip() + "\n"


def _yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _front_matter(snapshot: SourceSnapshot) -> list[str]:
    manifest = snapshot.manifest
    owner, repository = github_slug(manifest.repository)
    commit_url = f"https://github.com/{owner}/{repository}/commit/{snapshot.commit}"
    return [
        "---",
        f"title: {_yaml_string(manifest.title)}",
        "authors:",
        *[f"  - {_yaml_string(author)}" for author in manifest.authors],
        f"language: {_yaml_string(manifest.language)}",
        "tags:",
        *[f"  - {_yaml_string(tag)}" for tag in manifest.tags],
        f"published_at: {_yaml_string(snapshot.published_at)}",
        f"updated_at: {_yaml_string(snapshot.updated_at)}",
        "---",
        "",
        f"# {manifest.title}",
        "",
        "## 文档信息",
        "",
        "| 项目 | 内容 |",
        "| --- | --- |",
        f"| 文档标题 | {manifest.title} |",
        f"| 文档类型 | {manifest.language} 整合 Markdown |",
        f"| 上游仓库 | [{owner}/{repository}]({manifest.repository.removesuffix('.git')}) |",
        f"| 锁定提交 | [{snapshot.commit[:12]}]({commit_url}) |",
        f"| 提交时间 | {snapshot.commit_date} |",
        f"| 生成器版本 | `{generator_version(manifest)}` |",
        "",
        "> 本文件由 reference 仓库自动生成。请修改上游源文件或本仓库的清单/适配器后重新生成，不要直接编辑此文件。",
        "",
        "## 阅读说明",
        "",
        "本文档按清单中的阅读顺序合并上游 Markdown。图片被改写为锁定提交的 GitHub Raw 链接，章节内有效的本地文档链接被改写为同一提交的 GitHub 源文件链接。",
        "",
        "## 目录",
        "",
    ]


def build_document(snapshot: SourceSnapshot) -> str:
    """Build a portable single Markdown document from an exact source snapshot."""

    validate_manifest_sources(snapshot)
    sections = resolved_sections(snapshot)
    lines = _front_matter(snapshot)
    for section, parts in sections:
        lines.append(f"- [{section.title}](#{slugify(section.title)})")
        for part in parts:
            lines.append(f"  - [{part.title}](#{slugify(part.title)})")
    lines.extend(["", "---", ""])
    for section, parts in sections:
        lines.extend([f"## {section.title}", ""])
        for part in parts:
            lines.append(transform_part(part, snapshot).rstrip())
            lines.append("")
    document = "\n".join(lines).rstrip() + "\n"
    assert_document_contract(document)
    return document


def _clean_markdown_target(target: str) -> str:
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1]
    return target


def assert_document_contract(document: str) -> None:
    """Reject output that is stale, malformed, or not portable enough to publish."""

    in_fence = False
    h1_count = 0
    previous_level = 0
    for number, line in enumerate(document.splitlines(), start=1):
        if FENCE_MARKER.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.rstrip() != line:
            raise ReferenceError(f"generated document has trailing whitespace at line {number}")
        if HTML_IMAGE_TAG.search(line) or ALIGN_DIV_TAG.search(line) or FIGURE_TAG.search(line):
            raise ReferenceError(f"generated document keeps unsupported HTML image wrapper at line {number}")
        if HTML_STRONG_TAG.search(line) or HTML_EMPHASIS_TAG.search(line) or HTML_PARAGRAPH_TAG.search(line):
            raise ReferenceError(f"generated document keeps presentational HTML at line {number}")
        if PANDOC_IMAGE_ATTRIBUTES.search(line):
            raise ReferenceError(f"generated document keeps Pandoc image attributes at line {number}")
        for match in MARKDOWN_IMAGE_TARGET.finditer(line):
            target = _clean_markdown_target(match.group("target"))
            if not is_external_target(target):
                raise ReferenceError(f"generated document keeps local image target at line {number}: {target}")
        heading = HEADING.match(line)
        if not heading:
            continue
        level = len(heading.group(1))
        if level == 1:
            h1_count += 1
        if previous_level and level > previous_level + 1:
            raise ReferenceError(f"generated document has heading-level jump at line {number}")
        previous_level = level
    if in_fence:
        raise ReferenceError("generated document has an unclosed fenced code block")
    if h1_count != 1:
        raise ReferenceError(f"generated document must contain exactly one level-one heading, found {h1_count}")


def atomic_write_text(path: Path, content: str) -> None:
    """Write a file atomically so a failed update cannot leave a partial document."""

    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        temporary.replace(path)
    finally:
        if temporary.exists():
            temporary.unlink()


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    """Serialize lock data consistently and atomically."""

    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
