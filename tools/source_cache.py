"""Read-only source snapshot acquisition for reference updates and checks."""

from __future__ import annotations

import io
import subprocess
import tarfile
from pathlib import Path

from tools.reference_core import (
    REPOSITORY_ROOT,
    Manifest,
    ReferenceError,
    SourceSnapshot,
    github_slug,
    selected_source_paths,
)


CACHE_ROOT = REPOSITORY_ROOT / ".cache" / "sources"


def _git(arguments: list[str], cwd: Path | None = None) -> str:
    command = ["git"]
    if cwd is not None:
        command.extend(["-C", str(cwd)])
    command.extend(arguments)
    try:
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError as exc:
        raise ReferenceError("git is required to acquire source snapshots") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or exc.stdout.strip() or "unknown git error"
        raise ReferenceError(f"git command failed: {' '.join(command)}\n{detail}") from exc
    return completed.stdout.strip()


def _git_bytes(
    arguments: list[str], cwd: Path | None = None, *, input_bytes: bytes | None = None
) -> bytes:
    """Run Git while preserving binary object and tree data."""

    command = ["git"]
    if cwd is not None:
        command.extend(["-C", str(cwd)])
    command.extend(arguments)
    try:
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            input=input_bytes,
        )
    except OSError as exc:
        raise ReferenceError("git is required to acquire source snapshots") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", errors="replace").strip() or "unknown git error"
        raise ReferenceError(f"git command failed: {' '.join(command)}\n{detail}") from exc
    return completed.stdout


def _commit_date(root: Path, commit: str) -> str:
    return _git(["show", "-s", "--format=%cI", commit], root)


def _document_dates(
    identifier: str, paths: tuple[str, ...], root: Path, commit: str
) -> tuple[str, str]:
    """Return the first and latest commit date for the included source files."""

    latest = _git(["log", "-1", "--format=%cI", commit, "--", *paths], root)
    history = _git(["log", "--reverse", "--format=%cI", commit, "--", *paths], root)
    if not latest or not history:
        raise ReferenceError(f"{identifier}: included sources have no Git history")
    return history.splitlines()[0][:10], latest[:10]


def resolve_remote_commit(manifest: Manifest) -> str:
    """Resolve a source ref once, before fetching its exact immutable SHA."""

    output = _git(["ls-remote", manifest.repository, manifest.ref])
    candidates = [line.split("\t", 1)[0] for line in output.splitlines() if line.strip()]
    if not candidates:
        raise ReferenceError(
            f"{manifest.identifier}: unable to resolve ref {manifest.ref!r} in {manifest.repository}"
        )
    commit = candidates[0]
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit.lower()):
        raise ReferenceError(f"{manifest.identifier}: remote returned invalid commit SHA: {commit}")
    return commit


def _materialize_source_files(
    repository: Path,
    snapshot_root: Path,
    commit: str,
    paths: tuple[str, ...],
) -> None:
    """Write only selected source blobs without checking out the source tree.

    Some upstream repositories contain paths that Windows cannot represent.
    Reading selected blobs directly from Git keeps those unrelated paths from
    preventing a valid source snapshot from being built.
    """

    wanted = set(paths)
    materialized: set[str] = set()
    snapshot_root.mkdir(parents=True, exist_ok=True)
    root_resolved = snapshot_root.resolve()
    # Keep each command short enough for Windows' process command-line limit.
    for start in range(0, len(paths), 64):
        chunk = paths[start : start + 64]
        archive_bytes = _git_bytes(
            ["-c", "core.protectNTFS=false", "archive", "--format=tar", commit, "--", *chunk],
            repository,
        )
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            for member in archive:
                relative = member.name.rstrip("/")
                if relative not in wanted or not member.isfile():
                    continue
                destination = snapshot_root.joinpath(*Path(relative).parts)
                try:
                    destination.resolve().relative_to(root_resolved)
                except ValueError as exc:
                    raise ReferenceError(f"source path escapes snapshot directory: {relative}") from exc
                content = archive.extractfile(member)
                if content is None:
                    raise ReferenceError(f"Git archive omitted source content: {relative}")
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(content.read())
                materialized.add(relative)

    missing = wanted - materialized
    if missing:
        raise ReferenceError("Git archive omitted source files: " + ", ".join(sorted(missing)))


def _cache_path(manifest: Manifest) -> Path:
    """Reuse one blob-filtered Git cache for every document from a repository."""

    owner, repository = github_slug(manifest.repository)
    return CACHE_ROOT / f"{owner.lower()}--{repository.lower()}"


def _repository_entries(root: Path, commit: str) -> dict[str, str]:
    """Index blob/tree paths of *commit* without materializing their blobs."""

    output = _git(["ls-tree", "-r", "-t", "-z", commit], root)
    entries: dict[str, str] = {}
    for record in output.split("\0"):
        if not record:
            continue
        header, separator, path = record.partition("\t")
        fields = header.split()
        if not separator or len(fields) != 3 or fields[1] not in {"blob", "tree"}:
            raise ReferenceError(f"unable to parse Git tree entry: {record!r}")
        entries[path] = fields[1]
    if not entries:
        raise ReferenceError(f"source commit has no tree entries: {commit}")
    return entries


def snapshot_from_cache(manifest: Manifest, commit: str) -> SourceSnapshot:
    """Return selected files from a pinned cache snapshot, never a contributor checkout."""

    target = _cache_path(manifest)
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "--no-checkout", "--filter=blob:none", manifest.repository, str(target)])
    if not (target / ".git").exists():
        raise ReferenceError(f"source cache path is not a git repository: {target}")
    current_remote = _git(["remote", "get-url", "origin"], target)
    if current_remote != manifest.repository:
        _git(["remote", "set-url", "origin", manifest.repository], target)
    # Frontmatter records the first/latest included-source commit dates. Keep
    # history metadata complete while retaining blob filtering for unrelated
    # files and assets.
    if _git(["rev-parse", "--is-shallow-repository"], target) == "true":
        _git(["fetch", "--unshallow", "--filter=blob:none", "origin"], target)
    _git(["fetch", "--filter=blob:none", "origin", commit], target)
    entries = _repository_entries(target, commit)
    paths = selected_source_paths(manifest, entries)
    snapshot_root = target.parent / f"{target.name}-snapshots" / commit
    _materialize_source_files(target, snapshot_root, commit, paths)
    published_at, updated_at = _document_dates(manifest.identifier, paths, target, commit)
    return SourceSnapshot(
        manifest,
        snapshot_root,
        commit,
        _commit_date(target, commit),
        published_at,
        updated_at,
        entries,
    )


def snapshot_from_local(manifest: Manifest, source_root: Path) -> SourceSnapshot:
    """Use an explicitly supplied sibling checkout after verifying it is clean.

    This exists for offline development only.  It is intentionally opt-in and
    never used by CI, so normal operations cannot mutate or depend on sibling
    working trees.
    """

    _, repository = github_slug(manifest.repository)
    target = (source_root / repository).resolve()
    if not (target / ".git").exists():
        raise ReferenceError(f"{manifest.identifier}: expected local git checkout at {target}")
    if _git(["status", "--porcelain"], target):
        raise ReferenceError(f"{manifest.identifier}: local source checkout is dirty: {target}")
    commit = _git(["rev-parse", "HEAD"], target)
    entries = _repository_entries(target, commit)
    paths = selected_source_paths(manifest, entries)
    published_at, updated_at = _document_dates(manifest.identifier, paths, target, commit)
    return SourceSnapshot(
        manifest,
        target,
        commit,
        _commit_date(target, commit),
        published_at,
        updated_at,
        entries,
    )
