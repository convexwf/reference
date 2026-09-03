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
    """Keep only the source trees needed by a manifest in the local cache.

    The cache must see sibling assets in order to turn local image references
    into raw URLs, but it must not materialize unrelated large PDFs, notebooks
    or build artefacts from the upstream repository.
    """

    prefixes: set[str] = set()
    for pattern in manifest.required_globs:
        wildcard = min(
            (index for index, character in enumerate(pattern) if character in "*?["),
            default=len(pattern),
        )
        prefix = pattern[:wildcard].rsplit("/", 1)[0].strip("/")
        if prefix:
            prefixes.add(prefix)
    patterns = [f"/{prefix}/**" for prefix in sorted(prefixes)]
    patterns.extend(f"/{part.path}" for part in manifest.iter_parts())
    return sorted(set(patterns))


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
    _git(["fetch", "--depth=1", "origin", commit], target)
    _git(["checkout", "--detach", "--force", commit], target)
    actual = _git(["rev-parse", "HEAD"], target)
    if actual != commit:
        raise ReferenceError(f"{manifest.identifier}: cache checkout mismatch: expected {commit}, got {actual}")
    return SourceSnapshot(manifest, target, actual, _commit_date(target, actual))


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
    return SourceSnapshot(manifest, target, commit, _commit_date(target, commit))
