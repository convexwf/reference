"""Verify that committed Markdown exactly matches every locked source commit."""

from __future__ import annotations

import argparse
import sys

from adapters import get_adapter
from tools.reference_core import (
    ReferenceError,
    assert_document_contract,
    build_document,
    load_lock,
    manifest_digest,
    output_path,
    select_manifests,
)
from tools.source_cache import snapshot_from_cache


REQUIRED_LOCK_FIELDS = {
    "repository",
    "ref",
    "commit",
    "commit_date",
    "manifest_sha256",
    "generator_version",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--all", action="store_true", help="check every manifest (the default)")
    scope.add_argument("--target", action="append", metavar="ID", help="check one manifest; repeatable")
    return parser.parse_args()


def validate_lock_entry(manifest, entry: object) -> dict[str, str]:
    if not isinstance(entry, dict) or set(entry) != REQUIRED_LOCK_FIELDS:
        raise ReferenceError(f"{manifest.identifier}: lock entry must contain exactly {sorted(REQUIRED_LOCK_FIELDS)}")
    if any(not isinstance(value, str) or not value for value in entry.values()):
        raise ReferenceError(f"{manifest.identifier}: lock entry values must be non-empty strings")
    if entry["repository"] != manifest.repository or entry["ref"] != manifest.ref:
        raise ReferenceError(f"{manifest.identifier}: lock source does not match manifest")
    if entry["manifest_sha256"] != manifest_digest(manifest):
        raise ReferenceError(f"{manifest.identifier}: manifest changed; run tools.update")
    if entry["generator_version"] != get_adapter(manifest.adapter).version:
        raise ReferenceError(f"{manifest.identifier}: adapter changed; run tools.update")
    return entry


def main() -> int:
    args = parse_args()
    try:
        lock = load_lock()
        for manifest in select_manifests(args.target):
            entry = validate_lock_entry(manifest, lock["sources"].get(manifest.identifier))
            snapshot = snapshot_from_cache(manifest, entry["commit"])
            if snapshot.commit_date != entry["commit_date"]:
                raise ReferenceError(f"{manifest.identifier}: locked commit date does not match source")
            expected = build_document(snapshot)
            destination = output_path(manifest)
            if not destination.is_file():
                raise ReferenceError(f"{manifest.identifier}: missing generated Markdown: {destination}")
            actual = destination.read_text(encoding="utf-8")
            assert_document_contract(actual)
            if actual != expected:
                raise ReferenceError(f"{manifest.identifier}: generated Markdown is stale; run tools.update")
            print(f"valid: {manifest.identifier} ({snapshot.commit[:12]})")
        return 0
    except ReferenceError as exc:
        print(f"check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
