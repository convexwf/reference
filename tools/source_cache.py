"""Read-only source checkout acquisition for reference updates and checks."""

from __future__ import annotations

import subprocess
from pathlib import Path

from tools.reference_core import REPOSITORY_ROOT, Manifest, ReferenceError, SourceSnapshot


CACHE_ROOT = REPOSITORY_ROOT / ".cache" / "sources"


def _git(arguments: list[str], cwd: Path | None = None) -> str:
    command = ["git"]
    if cwd is not None:
        command.extend(["-C", str(cwd)])
    command.extend(arguments)
    try:
        completed = subprocess.run(command, check=True, capture_output=True, text=True)
    except OSError as exc:
        raise ReferenceError("git is required to acquire source snapshots") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or exc.stdout.strip() or "unknown git error"
        raise ReferenceError(f"git command failed: {' '.join(command)}\n{detail}") from exc
    return completed.stdout.strip()


def _commit_date(root: Path, commit: str) -> str:
    return _git(["show", "-s", "--format=%cI", commit], root)


def _document_dates(manifest: Manifest, root: Path) -> tuple[str, str]:
    """Return the first and latest commit date for the included source files."""

    paths = [part.path for part in manifest.iter_parts()]
    latest = _git(["log", "-1", "--format=%cI", "--", *paths], root)
    history = _git(["log", "--reverse", "--format=%cI", "--", *paths], root)
    if not latest or not history:
        raise ReferenceError(f"{manifest.identifier}: included sources have no Git history")
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


def _sparse_patterns(manifest: Manifest) -> list[str]:
    """Materialize only Markdown parts explicitly listed by a manifest.

    Linked assets are resolved against the pinned Git tree, not the sparse
    working tree.  This avoids downloading sibling PDFs, vendored libraries,
    notebooks, and large image collections just to construct immutable URLs.
    """

    return sorted({f"/{part.path}" for part in manifest.iter_parts()})


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
    """Return a detached cache checkout at *commit*, never a contributor checkout."""

    target = CACHE_ROOT / manifest.identifier
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "--no-checkout", "--filter=blob:none", manifest.repository, str(target)])
    if not (target / ".git").exists():
        raise ReferenceError(f"source cache path is not a git repository: {target}")
    current_remote = _git(["remote", "get-url", "origin"], target)
    if current_remote != manifest.repository:
        _git(["remote", "set-url", "origin", manifest.repository], target)
    _git(["sparse-checkout", "init", "--no-cone"], target)
    _git(["sparse-checkout", "set", "--no-cone", *_sparse_patterns(manifest)], target)
    # Frontmatter follows the original per-repository builders and records
    # the first/latest included-source commit dates.  Keep history metadata
    # complete while retaining blob filtering and sparse checkout for assets.
    if _git(["rev-parse", "--is-shallow-repository"], target) == "true":
        _git(["fetch", "--unshallow", "--filter=blob:none", "origin"], target)
    _git(["fetch", "--filter=blob:none", "origin", commit], target)
    _git(["checkout", "--detach", "--force", commit], target)
    actual = _git(["rev-parse", "HEAD"], target)
    if actual != commit:
        raise ReferenceError(f"{manifest.identifier}: cache checkout mismatch: expected {commit}, got {actual}")
    published_at, updated_at = _document_dates(manifest, target)
    return SourceSnapshot(
        manifest,
        target,
        actual,
        _commit_date(target, actual),
        published_at,
        updated_at,
        _repository_entries(target, actual),
    )


def snapshot_from_local(manifest: Manifest, source_root: Path) -> SourceSnapshot:
    """Use an explicitly supplied sibling checkout after verifying it is clean.

    This exists for offline development only.  It is intentionally opt-in and
    never used by CI, so normal operations cannot mutate or depend on sibling
    working trees.
    """

    target = (source_root / manifest.identifier).resolve()
    if not (target / ".git").exists():
        raise ReferenceError(f"{manifest.identifier}: expected local git checkout at {target}")
    if _git(["status", "--porcelain"], target):
        raise ReferenceError(f"{manifest.identifier}: local source checkout is dirty: {target}")
    commit = _git(["rev-parse", "HEAD"], target)
    published_at, updated_at = _document_dates(manifest, target)
    return SourceSnapshot(
        manifest,
        target,
        commit,
        _commit_date(target, commit),
        published_at,
        updated_at,
        _repository_entries(target, commit),
    )
