#!/usr/bin/env python3
"""Supplement S5: extract the frozen resolution-ladder results from the record's archived logs.

No computation is performed. The record ran the 3 x 3 ladder (quadrature nodes x RK4 step) and
archived its console output in two committed logs:
  publication_verification/v3_r2/authoritative.log   gamma_1 at t_star to 7 significant figures
  publication_verification/v3_r2/v3_r2.log           gamma_1 at t_star to 5 significant figures, plus
                                                     reference-protocol drift and Gibbs residual
Every extracted number carries its log file and line number. Cells whose header appears without
data (the run did not complete them) are recorded as missing, not filled in.

Output: data/frozen_convergence.json
"""
import os
import re

from common import DATA, RECORD_DIR, SOURCE_COMMIT, SOURCE_REPO, dump_json, record_path

LOGS = {"authoritative": "publication_verification/v3_r2/authoritative.log",
        "v3_r2": "publication_verification/v3_r2/v3_r2.log"}


def parse(rel):
    cells, cur = {}, None
    with open(record_path(rel), encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            mo = re.match(r"--- nx(\d+)_dt([0-9.e-]+) ---", line.strip())
            if mo:
                cur = f"nx{mo.group(1)}_dt{float(mo.group(2)):g}"
                cells[cur] = {"nx": int(mo.group(1)), "dt": float(mo.group(2)), "header_line": ln}
                continue
            if cur is None:
                continue
            g = re.search(r"gamma1(?: at t\*=0\.5)?:\s*(.*)$", line) if "t*=0.5" in line else None
            if g:
                pairs = re.findall(r"(\d+):([-0-9.e+]+)", g.group(1))
                cells[cur]["gamma1_tstar"] = {k: float(v) for k, v in pairs}
                cells[cur]["gamma1_line"] = ln
                mant = pairs[0][1].lstrip("-").split("e")[0]
                cells[cur]["printed_sigfigs"] = sum(c.isdigit() for c in mant)
            mo = re.search(r"P0 var drift:\s*([0-9.e+-]+)", line)
            if mo:
                cells[cur]["ref_var_drift"] = float(mo.group(1)); cells[cur]["ref_var_drift_line"] = ln
            mo = re.search(r"(?:Gibbs identity res|gibbs_res)[:=]\s*([0-9.e+-]+)", line)
            if mo:
                cells[cur]["gibbs_residual"] = float(mo.group(1)); cells[cur]["gibbs_residual_line"] = ln
    for c in cells.values():
        c["complete"] = "gamma1_tstar" in c
    return cells


def main():
    out = {"role": "frozen record evidence, extracted without recomputation",
           "source": {"repo": SOURCE_REPO, "commit": SOURCE_COMMIT,
                      "logs": {k: RECORD_DIR + "/" + v for k, v in LOGS.items()}},
           "logs": {}}
    for key, rel in LOGS.items():
        cells = parse(rel)
        done = [c for c in cells.values() if c["complete"]]
        nbs = sorted(done[0]["gamma1_tstar"], key=int)
        spread = max((max(c["gamma1_tstar"][nb] for c in done) - min(c["gamma1_tstar"][nb] for c in done))
                     / abs(done[0]["gamma1_tstar"][nb]) for nb in nbs)
        out["logs"][key] = {"cells": cells, "printed_sigfigs": done[0]["printed_sigfigs"], "n_cells_complete": len(done), "n_cells_listed": len(cells),
                            "missing": [k for k, c in cells.items() if not c["complete"]],
                            "max_rel_spread_gamma1_tstar_at_printed_precision": spread}
    dump_json(out, os.path.join(DATA, "frozen_convergence.json"))
    for k, v in out["logs"].items():
        print(f"{k}: {v['n_cells_complete']} complete cells, missing {v['missing']}, "
              f"max rel spread of printed gamma1 = {v['max_rel_spread_gamma1_tstar_at_printed_precision']}")


if __name__ == "__main__":
    main()
