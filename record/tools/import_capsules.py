#!/usr/bin/env python3
"""Byte-exact import of frozen TestingGRUT campaign records into record/testinggrut/.

Reads the import plan (import_plan.json: capsule -> {branch, pin, files, ...}), extracts each
file's blob from the frozen source clone at the pinned commit, writes it byte-exact under
record/testinggrut/<capsule>/<original path>, and builds record/RECORD_IMPORT_MANIFEST.json with,
per file: the source path, the git blob id at the pin, and sha256 over the blob bytes.

Never edits an imported file. Verification mode re-hashes every imported file against the
manifest and re-reads the source blob ids at the pins.

  python3 import_capsules.py import   # one-time extraction + manifest
  python3 import_capsules.py verify   # IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.dirname(HERE)                      # record/
ROOT = os.path.dirname(REC)                      # repo root
SRC_CLONE = "/home/user/ryangrvr/testinggrut"    # frozen source (read-only; not needed once imported)
SOURCE_REPO = "ryangrvr/TestingGRUT"
MANIFEST = os.path.join(REC, "RECORD_IMPORT_MANIFEST.json")
PLAN = os.path.join(HERE, "import_plan.json")


def git(*args):
    return subprocess.run(["git", "-C", SRC_CLONE, *args], capture_output=True)


def blob_bytes(pin, path):
    r = git("cat-file", "blob", f"{pin}:{path}")
    if r.returncode:
        raise SystemExit(f"cannot read {pin}:{path}: {r.stderr.decode()[:200]}")
    return r.stdout


def blob_id(pin, path):
    r = git("rev-parse", f"{pin}:{path}")
    if r.returncode:
        raise SystemExit(f"no blob id for {pin}:{path}")
    return r.stdout.decode().strip()


def dest_path(capsule, path, dest_root):
    return os.path.join(ROOT, dest_root if dest_root else f"record/testinggrut/{capsule}", path)


def do_import():
    plan = json.load(open(PLAN))
    manifest = {
        "record": "RECORD_IMPORT_MANIFEST",
        "note": ("Byte-exact imports from the frozen historical record. Never edit an imported file. "
                 "sha256 is computed over the exact git blob bytes at the pinned commit; git_blob is the "
                 "blob id there. Follows the pattern of manuscript/RECORD_IMPORT.json on bri1-manuscript."),
        "source_repo": SOURCE_REPO,
        "inventory_source": {"path": "TESTINGGRUT_ARCHIVE_INDEX_01.md", "branch": "archive-index",
                             "commit": plan["_index_pin"]},
        "capsules": {},
    }
    for name, cap in plan.items():
        if name.startswith("_"):
            continue
        entry = {k: cap[k] for k in ("branch", "pin", "proposed_tag_label", "terminal_verbatim",
                                     "terminal_is_recorded_state", "parent_capsule") if k in cap}
        entry["source_repo"] = SOURCE_REPO
        entry["files"] = {}
        for path in cap.get("files", []):
            data = blob_bytes(cap["pin"], path)
            dst = dest_path(name, path, cap.get("dest_root"))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "wb") as f:
                f.write(data)
            entry["files"][path] = {"git_blob": blob_id(cap["pin"], path),
                                    "sha256": hashlib.sha256(data).hexdigest()}
        if cap.get("reference_only"):
            entry["reference_only"] = cap["reference_only"]
        if cap.get("dest_root"):
            entry["dest_root"] = cap["dest_root"]
        manifest["capsules"][name] = entry
        print(f"{name:28s} {len(entry['files']):4d} files")
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("manifest written")


def verify():
    """IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS."""
    man = json.load(open(MANIFEST))
    plan = json.load(open(PLAN)) if os.path.exists(PLAN) else {}
    bad, n = [], 0
    have_src = os.path.isdir(SRC_CLONE)
    for name, cap in man["capsules"].items():
        for path, rec in cap["files"].items():
            n += 1
            dst = dest_path(name, path, cap.get("dest_root"))
            if not os.path.exists(dst):
                bad.append(f"missing: {name}/{path}")
                continue
            h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
            if h != rec["sha256"]:
                bad.append(f"sha256 mismatch: {name}/{path}")
            if have_src and blob_id(cap["pin"], path) != rec["git_blob"]:
                bad.append(f"source blob moved: {name}/{path}")
    if bad:
        print("\n".join(bad))
        sys.exit(1)
    print(f"import verified: {n} files byte-exact against the manifest"
          + ("" if have_src else " (source clone absent; destination hashes only)"))


if __name__ == "__main__":
    do_import() if (len(sys.argv) > 1 and sys.argv[1] == "import") else verify()
