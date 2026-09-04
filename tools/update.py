"""Update one or more integrated Markdown documents from their upstream refs.

Run ``python -m tools.update --all`` from the reference repository.  The
command reads source repositories through detached cache checkouts and writes
only this repository's ``markdown/`` files and ``sources.lock.json``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools.reference_core import (
    LOCK_VERSION,
    ReferenceError,
    atomic_write_json,
    atomic_write_text,
    build_document,
    generator_version,
    load_lock,
    manifest_digest,
    output_path,
    select_manifests,
)
from tools.source_cache import resolve_remote_commit, snapshot_from_cache, snapshot_from_local


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--all", action="store_true", help="update every manifest (the default)")
    scope.add_argument("--target", action="append", metavar="ID", help="update one manifest; repeatable")
    parser.add_argument(
        "--source-root",
        type=Path,
        help="offline development only: read clean sibling source checkouts from this directory",
    )
    parser.add_argument("--dry-run", action="store_true", help="build and validate without changing tracked files")
    parser.add_argument("--force", action="store_true", help="regenerate even when lock and output are current")
    return parser.parse_args()


def lock_entry(snapshot) -> dict[str, str]:
    return {
        "repository": snapshot.manifest.repository,
        "ref": snapshot.manifest.ref,
        "commit": snapshot.commit,
        "commit_date": snapshot.commit_date,
        "manifest_sha256": manifest_digest(snapshot.manifest),
        "generator_version": generator_version(snapshot.manifest),
    }


def main() -> int:
    args = parse_args()
    try:
        manifests = select_manifests(args.target)
        current_lock = load_lock()
        next_lock = {"version": LOCK_VERSION, "sources": dict(current_lock["sources"])}
        planned: list[tuple[object, str, dict[str, str]]] = []

        for manifest in manifests:
            locked = current_lock["sources"].get(manifest.identifier)
            if args.source_root is not None:
                snapshot = snapshot_from_local(manifest, args.source_root)
            else:
                commit = resolve_remote_commit(manifest)
                snapshot = snapshot_from_cache(manifest, commit)
            entry = lock_entry(snapshot)
            destination = output_path(manifest)
            is_current = locked == entry and destination.is_file()
            if is_current and not args.force:
                print(f"up to date: {manifest.identifier} ({snapshot.commit[:12]})")
                continue
            content = build_document(snapshot)
            planned.append((manifest, content, entry))
            print(f"prepared: {manifest.identifier} ({snapshot.commit[:12]})")

        if not planned:
            print("no source updates")
            return 0
        if args.dry_run:
            print("dry run: no tracked files changed")
            return 0

        for manifest, content, entry in planned:
            atomic_write_text(output_path(manifest), content)
            next_lock["sources"][manifest.identifier] = entry
        atomic_write_json(Path(__file__).resolve().parent.parent / "sources.lock.json", next_lock)
        print(f"updated {len(planned)} integrated document(s)")
        return 0
    except ReferenceError as exc:
        print(f"update failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
