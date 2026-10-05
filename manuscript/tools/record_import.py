#!/usr/bin/env python3
"""Record-import ledger for the proof/verification record.

The record lives in ryangrvr/TestingGRUT at commit 27829f1 (branch
grut-backreaction-identifiability-0). That commit is not part of this
repository's history, so the record directory is imported byte-exact and every
file is pinned by its git blob id in manuscript/RECORD_IMPORT.json.

  python3 record_import.py create <path-to-TestingGRUT-clone>
      writes the ledger from the source tree (one-time).
  python3 record_import.py verify
      re-hashes every imported file with `git hash-object` and fails on any
      mismatch, missing file, or unledgered extra file.
"""
import os
import subprocess
import sys

from common import ROOT, MS, RECORD_DIR, SOURCE_REPO, SOURCE_BRANCH, SOURCE_COMMIT, dump_json, load_json

LEDGER = os.path.join(MS, "RECORD_IMPORT.json")


def blob_id(path):
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def create(src_repo):
    out = subprocess.check_output(
        ["git", "-C", src_repo, "ls-tree", "-r", SOURCE_COMMIT, RECORD_DIR], text=True)
    files = {}
    for line in out.splitlines():
        meta, path = line.split("\t", 1)
        _, kind, sha = meta.split()
        if kind != "blob":
            continue
        local = os.path.join(ROOT, path)
        got = blob_id(local)
        if got != sha:
            sys.exit(f"MISMATCH on import: {path} local {got} != source {sha}")
        files[path] = sha
    dump_json({"source_repo": SOURCE_REPO, "source_branch": SOURCE_BRANCH,
               "source_commit": SOURCE_COMMIT, "imported_dir": RECORD_DIR,
               "note": "Byte-exact import; verified by git blob id. Do not edit these files.",
               "files": files}, LEDGER)
    print(f"ledger written: {len(files)} files")


def verify():
    led = load_json(LEDGER)
    bad = []
    for path, sha in led["files"].items():
        local = os.path.join(ROOT, path)
        if not os.path.exists(local):
            bad.append(f"missing: {path}")
        elif blob_id(local) != sha:
            bad.append(f"modified: {path}")
    present = set()
    for dp, _, fns in os.walk(os.path.join(ROOT, RECORD_DIR)):
        for fn in fns:
            present.add(os.path.relpath(os.path.join(dp, fn), ROOT))
    for extra in sorted(present - set(led["files"])):
        bad.append(f"unledgered extra file: {extra}")
    return bad, len(led["files"])


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "create":
        create(sys.argv[2])
    else:
        bad, n = verify()
        if bad:
            print("\n".join(bad))
            sys.exit(1)
        print(f"record import verified: {n} files byte-exact at {SOURCE_COMMIT[:7]}")
