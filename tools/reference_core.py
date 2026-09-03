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
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote, unquote, urlsplit

from adapters import get_adapter


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPOSITORY_ROOT / "manifests"
LOCK_PATH = REPOSITORY_ROOT / "sources.lock.json"
LOCK_VERSION = 1


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
    sections: tuple[SectionSpec, ...]
    required_globs: tuple[str, ...]
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


MARKDOWN_IMAGE_TARGET = re.compile(
    r"(?P<prefix>!\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)(?P<rest>[^)]*\))"
)
MARKDOWN_LINK_TARGET = re.compile(
    r"(?<!\!)\[(?P<label>[^\]]*)\]\((?P<target><[^>]+>|[^)\s]+)(?P<rest>[^)]*\))"
)
PANDOC_IMAGE_ATTRIBUTES = re.compile(
    r"(?P<image>!\[[^\]]*\]\((?:<[^>]+>|[^)\s]+)(?:[^)]*)\))\{[^{}\n]*\}"
)
HTML_IMAGE_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
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
    adapter = _require_string(data.get("adapter"), "adapter", origin)
    try:
        get_adapter(adapter)
    except ValueError as exc:
        raise ReferenceError(f"{origin}: {exc}") from exc
    output = _safe_relative(data.get("output"), "output", origin)
    if not output.endswith(".md"):
        raise ReferenceError(f"{origin}: output must end in .md")

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
        if not isinstance(parts_data, list) or not parts_data:
            raise ReferenceError(f"{section_origin}: parts must be a non-empty array")
        parts: list[PartSpec] = []
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
        sections.append(SectionSpec(section_title, tuple(parts)))

    completeness = data.get("completeness", {})
    if not isinstance(completeness, dict):
        raise ReferenceError(f"{origin}: completeness must be an object")
    globs_data = completeness.get("required_globs", [])
    if not isinstance(globs_data, list) or not all(isinstance(item, str) for item in globs_data):
        raise ReferenceError(f"{origin}: completeness.required_globs must be a string array")
    required_globs = tuple(_safe_relative(item, "required_globs entry", origin) for item in globs_data)

    return Manifest(
        identifier=identifier,
        title=title,
        repository=repository,
        ref=ref,
        language=language,
        adapter=adapter,
        output=output,
        sections=tuple(sections),
        required_globs=required_globs,
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


def validate_manifest_sources(snapshot: SourceSnapshot) -> None:
    """Ensure all listed source files exist exactly once and globs are complete."""

    listed: set[str] = set()
    for part in snapshot.manifest.iter_parts():
        if part.path in listed:
            raise ReferenceError(f"{snapshot.manifest.identifier}: source listed more than once: {part.path}")
        listed.add(part.path)
        if not _source_path(snapshot, part.path).is_file():
            raise ReferenceError(f"{snapshot.manifest.identifier}: missing source: {part.path}")

    discovered: set[str] = set()
    for pattern in snapshot.manifest.required_globs:
        for path in snapshot.root.glob(pattern):
            if path.is_file():
                discovered.add(path.relative_to(snapshot.root).as_posix())
    omitted = discovered - listed
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

    return target.startswith(("#", "/", "data:")) or bool(urlsplit(target).scheme)


def _repository_relative_target(target: str, source: Path, snapshot: SourceSnapshot) -> tuple[Path, str] | None:
    path_text, suffix = split_target(target)
    if not path_text or is_external_target(path_text):
        return None
    resolved = (source.parent / Path(unquote(path_text))).resolve()
    try:
        relative = resolved.relative_to(snapshot.root.resolve())
    except ValueError:
        return None
    if not resolved.exists():
        return None
    return relative, suffix


def _github_url(base: str, relative: Path, suffix: str = "") -> str:
    encoded = quote(relative.as_posix(), safe="/-._~!$&'()*+,;=:@")
    return f"{base}/{encoded}{suffix}"


def rewrite_image_target(target: str, source: Path, snapshot: SourceSnapshot) -> str:
    """Turn an existing local asset into a SHA-pinned GitHub Raw URL."""

    resolved = _repository_relative_target(target, source, snapshot)
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

    resolved = _repository_relative_target(target, source, snapshot)
    if resolved is None:
        return target
    relative, suffix = resolved
    owner, repository = github_slug(snapshot.manifest.repository)
    kind = "tree" if _source_path(snapshot, relative.as_posix()).is_dir() else "blob"
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
        path_text = urlsplit(path_text).path
    stem = Path(unquote(path_text)).stem
    return stem or "image"


def _html_image_to_markdown(tag: str, source: Path, snapshot: SourceSnapshot) -> str:
    raw_target = html_attribute(tag, "src")
    if raw_target is None:
        return tag
    target = rewrite_image_target(raw_target, source, snapshot)
    alt = html_attribute(tag, "alt") or image_alt_text(raw_target)
    return f"![{alt}]({target})"


def rewrite_assets(line: str, source: Path, snapshot: SourceSnapshot, align_div_closes: int = 0) -> str:
    """Rewrite Markdown/HTML images and local links while retaining captions."""

    converted_html_image = bool(HTML_IMAGE_TAG.search(line))

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
    return line.strip() if converted_html_image else line.rstrip()


def transform_part(part: PartSpec, snapshot: SourceSnapshot) -> str:
    """Lift a source chapter under a level-three generated part heading."""

    source = _source_path(snapshot, part.path)
    lines = source.read_text(encoding="utf-8").splitlines()
    result: list[str] = []
    in_fence = False
    align_div_depth = 0
    title_written = False

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
            else:
                result.append(f"{'#' * min(level + 2, 6)} {heading_text}")
            continue

        align_opens = len(ALIGN_DIV_TAG.findall(line))
        align_closes = len(BARE_DIV_CLOSE_TAG.findall(line))
        closings_to_remove = min(align_div_depth + align_opens, align_closes)
        align_div_depth += align_opens - closings_to_remove
        result.append(rewrite_assets(line, source, snapshot, closings_to_remove))

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
    adapter = get_adapter(manifest.adapter)
    owner, repository = github_slug(manifest.repository)
    commit_url = f"https://github.com/{owner}/{repository}/commit/{snapshot.commit}"
    return [
        "---",
        f"title: {_yaml_string(manifest.title)}",
        f"language: {_yaml_string(manifest.language)}",
        f"source_repository: {_yaml_string(manifest.repository)}",
        f"source_ref: {_yaml_string(manifest.ref)}",
        f"source_commit: {_yaml_string(snapshot.commit)}",
        f"source_commit_date: {_yaml_string(snapshot.commit_date)}",
        f"generator_version: {_yaml_string(adapter.version)}",
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
        f"| 适配器版本 | `{manifest.adapter}@{adapter.version}` |",
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
    lines = _front_matter(snapshot)
    for section in snapshot.manifest.sections:
        lines.append(f"- [{section.title}](#{slugify(section.title)})")
        for part in section.parts:
            lines.append(f"  - [{part.title}](#{slugify(part.title)})")
    lines.extend(["", "---", ""])
    for section in snapshot.manifest.sections:
        lines.extend([f"## {section.title}", ""])
        for part in section.parts:
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
