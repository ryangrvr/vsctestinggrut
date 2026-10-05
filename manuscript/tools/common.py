"""Shared paths and source identifiers for the manuscript build.

Every scientific value in the manuscript is traced to one of two kinds of source:
  (a) a file of the imported proof/verification record (byte-exact copy of
      ryangrvr/TestingGRUT @ SOURCE_COMMIT, path prefix RECORD_DIR), or
  (b) a computation performed by a script in manuscript/tools/.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.dirname(HERE)                      # manuscript/
ROOT = os.path.dirname(MS)                      # repository root
SRC = os.path.join(MS, "src")
DATA = os.path.join(MS, "data")
FIG = os.path.join(MS, "figures")
BUILD = os.path.join(MS, "build")

SOURCE_REPO = "ryangrvr/TestingGRUT"
SOURCE_BRANCH = "grut-backreaction-identifiability-0"
SOURCE_COMMIT = "27829f1fa8fd52353f596921da9630a9bf70397e"
RECORD_DIR = "backreaction_identifiability_0"   # same path in source repo and here

AUTH_JSON_REL = RECORD_DIR + "/publication_verification/v3_r2/v3_r2_results.json"
AUTH_JSON = os.path.join(ROOT, AUTH_JSON_REL)


def record_path(rel):
    """Absolute path of a record file given its path relative to RECORD_DIR."""
    return os.path.join(ROOT, RECORD_DIR, rel)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def src_ref(rel, section, json_path=None):
    """Provenance record pointing into the imported record."""
    d = {"repo": SOURCE_REPO, "commit": SOURCE_COMMIT,
         "path": RECORD_DIR + "/" + rel, "section": section}
    if json_path is not None:
        d["json_path"] = json_path
    return d


def tool_ref(script, method):
    """Provenance record for a value computed by a build script."""
    return {"computed_by": "manuscript/tools/" + script, "method": method}
