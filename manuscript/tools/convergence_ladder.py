#!/usr/bin/env python3
"""MANUSCRIPT REPRODUCIBILITY CHECK — NOT PART OF FROZEN SCIENTIFIC EVIDENCE.

Archived only. Its output (data/reproducibility/convergence_ladder.json) is not used by any theorem,
disposition, fitted result, table, figure or publication claim, and it is not run by the build.
The manuscript's convergence statement is extracted from the record's archived logs
(tools/extract_frozen_convergence.py). Do not rerun this ladder to improve the manuscript.

Original purpose (superseded by the scope rule above): resolution ladder for the finite-N_B computation.

The record describes a resolution ladder (quadrature nodes nx x RK4 step dt) for
its deterministic quadrature, but only the reference-resolution output is
machine-readable. This tool regenerates the ladder at the two times the
manuscript reports, t_star = 0.5 and t = 1.0, using the record's own numerical
definitions imported read-only from
  backreaction_identifiability_0/publication_verification/v3_r2/v3_r2_authoritative.py
(protocol q_p1, moments, the RK4 right-hand side, the quadrature domain and the
nx/dt ladder). The only change is operational: one integration per (nx, dt, eps)
is snapshotted at both times instead of being restarted from t = 0. The driver
is verified bit-for-bit against the record's integrate_tensor before use.

Output: data/reproducibility/convergence_ladder.json (archived only)
"""
import importlib.util
import os
import sys
from multiprocessing import Pool

import numpy as np

from common import AUTH_JSON, DATA, ROOT, RECORD_DIR, dump_json, load_json

REC = os.path.join(ROOT, RECORD_DIR, "publication_verification/v3_r2/v3_r2_authoritative.py")
TIMES = (0.5, 1.0)


def load_record():
    sys.dont_write_bytecode = True        # never write into the imported record directory
    spec = importlib.util.spec_from_file_location("v3r2_record", REC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # defines functions/constants only; main() is guarded
    return mod


R = load_record()


def grid(nx):
    xg, wg = np.polynomial.legendre.leggauss(nx)
    xs, wx = R.L * xg, R.L * wg
    X0 = np.broadcast_to(xs[:, None], (nx, nx)).copy()
    P0 = np.broadcast_to(xs[None, :], (nx, nx)).copy()
    rho = np.exp(-0.5 * P0 ** 2 - 0.5 * X0 ** 2 - 0.25 * X0 ** 4)
    W = wx[:, None] * wx[None, :] * rho
    return X0, P0, W / W.sum()


def rk4_snapshots(X0, P0, eps, qfun, dt, times):
    """Same arithmetic, in the same order, as the record's integrate_tensor; snapshots at each time."""
    steps_at = {int(round(T / dt)): T for T in times}
    h = dt
    x = X0.copy(); v = P0.copy()
    out = {}
    for k in range(max(steps_at)):
        t0 = k * h
        q0 = qfun(t0)
        k1v = -x - x**3 + eps*q0; k1x = v
        x2 = x + 0.5*h*k1x; v2 = v + 0.5*h*k1v
        qm = qfun(t0 + 0.5*h)
        k2v = -x2 - x2**3 + eps*qm; k2x = v2
        x3 = x + 0.5*h*k2x; v3 = v + 0.5*h*k2v
        k3v = -x3 - x3**3 + eps*qm; k3x = v3
        x4 = x + h*k3x; v4 = v + h*k3v
        q1 = qfun(t0 + h)
        k4v = -x4 - x4**3 + eps*q1; k4x = v4
        x = x + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        v = v + (h/6)*(k1v + 2*k2v + 2*k3v + k4v)
        if k + 1 in steps_at:
            out[steps_at[k + 1]] = x.copy()
    return out


def job(arg):
    nx, dt, nb = arg
    X0, P0, Wn = grid(nx)
    if nb == 0:
        snaps = rk4_snapshots(X0, P0, 0.0, lambda t: 0.0, dt, TIMES)
    else:
        snaps = rk4_snapshots(X0, P0, 1.0 / np.sqrt(nb), R.q_p1, dt, TIMES)
    res = {}
    for T, xT in snaps.items():
        m1, m2, var, k3, m4 = R.moments(xT, Wn)
        d = {"mean": float(m1), "var": float(var), "kappa3_X": float(k3)}
        if nb:
            k3F = k3 / np.sqrt(nb)
            d.update(kappa3_F=float(k3F), gamma1_F=float(k3F / var ** 1.5), NB_gamma1=float(nb * k3F / var ** 1.5))
        res[str(T)] = d
    return (nx, dt, nb, res)


def equivalence_check():
    nx, dt, eps = 60, 1e-3, 0.5
    X0, P0, _ = grid(nx)
    mine = rk4_snapshots(X0, P0, eps, R.q_p1, dt, TIMES)
    ref = {T: R.integrate_tensor(X0, P0, T, eps, R.q_p1, dt) for T in TIMES}
    return {str(T): float(np.max(np.abs(mine[T] - ref[T]))) for T in TIMES}


def main():
    eq = equivalence_check()
    assert all(v == 0.0 for v in eq.values()), f"driver differs from record integrate_tensor: {eq}"
    jobs = [(nx, dt, nb) for nx in R.NX_LIST for dt in R.DT_LIST for nb in [0] + list(R.NB_GRID)]
    jobs.sort(key=lambda j: -(j[0] ** 2 / j[1]))           # longest first
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    with Pool(workers) as pool:
        results = pool.map(job, jobs, chunksize=1)
    ladder = {}
    for nx, dt, nb, res in results:
        cell = ladder.setdefault(f"nx{nx}_dt{dt:g}", {"nx": nx, "dt": dt, "reference": None, "ramp": {}})
        if nb == 0:
            cell["reference"] = res
        else:
            cell["ramp"][str(nb)] = res
    for cell in ladder.values():
        nbs = np.array(sorted(int(k) for k in cell["ramp"]), float)
        g = np.array([cell["ramp"][str(int(n))]["0.5"]["gamma1_F"] for n in nbs])
        p, a = np.polyfit(np.log(nbs), np.log(np.abs(g)), 1)
        cell["fit_t0.5"] = {"p": float(-p), "intercept": float(a)}
    # consistency of the reference cell with the authoritative JSON
    auth = load_json(AUTH_JSON)
    ref = ladder[f"nx{240}_dt{5e-4:g}"]
    dev = max(abs(ref["ramp"][nb][t]["gamma1_F"] - auth["p1"][t][nb]["gamma1_F"]) / abs(auth["p1"][t][nb]["gamma1_F"])
              for nb in ref["ramp"] for t in ("0.5", "1.0"))
    dump_json({"label": "MANUSCRIPT REPRODUCIBILITY CHECK — NOT PART OF FROZEN SCIENTIFIC EVIDENCE",
               "use_rule": "Not used by any theorem, disposition, fitted result, table, figure or publication claim. "
                           "Archived only. The manuscript's convergence statement is extracted from the record's "
                           "archived logs (data/frozen_convergence.json).",
               "source_functions": RECORD_DIR + "/publication_verification/v3_r2/v3_r2_authoritative.py",
               "times": list(TIMES), "nx_list": list(R.NX_LIST), "dt_list": list(R.DT_LIST),
               "nb_grid": list(R.NB_GRID), "driver_equivalence_max_abs_diff": eq,
               "reference_cell_vs_authoritative_json_max_rel_diff_gamma1": dev,
               "cells": ladder}, os.path.join(DATA, "reproducibility", "convergence_ladder.json"))
    print("ladder written; reference cell vs authoritative JSON max rel diff:", dev)


if __name__ == "__main__":
    main()
