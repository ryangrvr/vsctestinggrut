#!/usr/bin/env python3
"""Reproducibility of the authoritative numerical output (Supplement S6).

Copies the record script whose output schema matches the authoritative JSON,
  backreaction_identifiability_0/publication_verification/v3_r2/extract_data.py,
into a temporary directory (the record itself is never written to), runs it
unchanged, and compares its output with the committed authoritative JSON.

Output: data/repro_record.json. Runtime: about twenty minutes on one core.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

from common import AUTH_JSON, AUTH_JSON_REL, DATA, RECORD_DIR, ROOT, dump_json

SCRIPT_REL = RECORD_DIR + "/publication_verification/v3_r2/extract_data.py"


def flatten(o, p="", out=None):
    out = {} if out is None else out
    if isinstance(o, dict):
        for k, v in o.items():
            flatten(v, f"{p}.{k}", out)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            flatten(v, f"{p}[{i}]", out)
    elif isinstance(o, (int, float)):
        out[p] = float(o)
    return out


def main():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(os.path.join(ROOT, SCRIPT_REL), tmp)
        r = subprocess.run([sys.executable, "extract_data.py"], cwd=tmp, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr)
        with open(os.path.join(tmp, "v3_r2_results.json")) as f:
            new = json.load(f)
    with open(AUTH_JSON) as f:
        old = json.load(f)
    a, b = flatten(new), flatten(old)
    sig = {k: abs(a[k] - b[k]) / abs(b[k]) for k in b if abs(b[k]) > 1e-12}
    small = {k: abs(a[k] - b[k]) for k in b if abs(b[k]) <= 1e-12}
    import numpy, platform
    dump_json({
        "role": "reproducibility of the frozen authoritative output by re-running the record script unchanged",
        "script": SCRIPT_REL, "compared_with": AUTH_JSON_REL,
        "same_keys": set(a) == set(b),
        "n_values": len(b), "n_significant": len(sig), "n_roundoff_level": len(small),
        "bitwise_identical_values": sum(a[k] == b[k] for k in b),
        "max_rel_diff_significant": max(sig.values()),
        "max_abs_diff_roundoff_level": max(small.values()) if small else 0.0,
        "environment": {"python": platform.python_version(), "numpy": numpy.__version__},
    }, os.path.join(DATA, "repro_record.json"))
    print("max rel diff (significant values):", max(sig.values()))


if __name__ == "__main__":
    main()
