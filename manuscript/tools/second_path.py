#!/usr/bin/env python3
"""Supplement S6: second numerical code path for the finite-N_B illustration.

Role: manuscript-stage numerical cross-check of the frozen result (reproducibility artifact). It is
not a new verification lane, not external replication, and does not upgrade the evidence grade.
It cannot change the frozen result: gen_values.py stops the build if it disagrees materially.

Written for this build; it shares only the model definition with the record's
computation. Differences in every numerical ingredient:
  record: tensor Gauss-Legendre on [-L, L]^2 (same nodes in x and p), fixed-step RK4;
  here:   Gauss-Legendre in x (different node count) x probabilists' Gauss-Hermite
          in p (Gaussian factor in the weights), adaptive DOP853 (scipy) with tight
          tolerances, both times from one integration.
Quantities: the ramp-protocol standardised skewness gamma_1[F(t)] and N_B gamma_1
at t = 0.5 and t = 1.0 for the bath-size grid, and the reference-protocol variance.

Output: data/second_path.json
"""
import os

import numpy as np
from scipy.integrate import solve_ivp

from common import AUTH_JSON, AUTH_JSON_REL, DATA, dump_json, load_json, tool_ref

NX, NP, L = 200, 100, 6.0
RTOL = ATOL = 1e-12


def q_ramp(t):
    if t <= np.pi:
        u = t / np.pi
        return 10 * u ** 3 - 15 * u ** 4 + 6 * u ** 5      # protocol definition
    return 1.0


def nodes():
    xg, wx = np.polynomial.legendre.leggauss(NX)
    x, wx = L * xg, L * wx
    p, wp = np.polynomial.hermite_e.hermegauss(NP)          # weight exp(-p^2/2)
    X, P = np.meshgrid(x, p, indexing="ij")
    W = np.outer(wx * np.exp(-x ** 2 / 2 - x ** 4 / 4), wp)
    return X.ravel(), P.ravel(), (W / W.sum()).ravel()


def evolve(x0, p0, eps, times):
    n = x0.size

    def rhs(t, z):
        x, p = z[:n], z[n:]
        return np.concatenate([p, -x - x ** 3 + eps * q_ramp(t)])

    sol = solve_ivp(rhs, (0.0, max(times)), np.concatenate([x0, p0]), method="DOP853",
                    t_eval=list(times), rtol=RTOL, atol=ATOL)
    assert sol.success, sol.message
    return {T: sol.y[:n, i] for i, T in enumerate(times)}


def cumulants(x, w):
    m1 = np.sum(w * x)
    c = x - m1
    var = np.sum(w * c * c)
    k3 = np.sum(w * c ** 3)
    return m1, var, k3


def main():
    auth = load_json(AUTH_JSON)
    times = (0.5, 1.0)
    nbs = list(auth["p1"]["0.5"].keys())
    x0, p0, w = nodes()
    out = {"role": "manuscript-stage numerical cross-check of the frozen result; not a new verification lane, not external replication, no upgrade of the evidence grade; it cannot change the frozen result (a material contradiction stops the build)",
           "method": tool_ref("second_path.py", f"GL({NX}) in x on [-{L:g},{L:g}] x Gauss-Hermite({NP}) in p; "
                                                f"DOP853 rtol=atol={RTOL:g}"),
           "compared_with": AUTH_JSON_REL, "reference": {}, "ramp": {}}
    ref = evolve(x0, p0, 0.0, times)
    for T in times:
        _, var, k3 = cumulants(ref[T], w)
        a = auth["p0"][f"{T}"]["var"]
        out["reference"][f"{T}"] = {"var": float(var), "kappa3": float(k3), "rel_diff_var_vs_record": float(abs(var - a) / a)}
    worst = 0.0
    for nb in nbs:
        eps = 1.0 / np.sqrt(int(nb))
        st = evolve(x0, p0, eps, times)
        row = {}
        for T in times:
            _, var, k3 = cumulants(st[T], w)
            k3F = k3 / np.sqrt(int(nb))
            g1 = k3F / var ** 1.5
            a = auth["p1"][f"{T}"][nb]["gamma1_F"]
            rel = abs(g1 - a) / abs(a)
            worst = max(worst, rel)
            row[f"{T}"] = {"var_X": float(var), "kappa3_X": float(k3), "gamma1_F": float(g1),
                           "NB_gamma1": float(int(nb) * g1), "record_gamma1_F": a, "rel_diff_vs_record": float(rel)}
        out["ramp"][nb] = row
        print(f"N_B={nb:>4}: rel diff gamma1 vs record  t=0.5: {row['0.5']['rel_diff_vs_record']:.2e}"
              f"   t=1.0: {row['1.0']['rel_diff_vs_record']:.2e}", flush=True)
    for T in ("0.5", "1.0"):
        g = [out["ramp"][nb][T]["NB_gamma1"] for nb in nbs]
        out[f"NB_gamma1_drift_t{T}"] = float(abs(g[0] - g[-1]) / abs(g[-1]))
        out[f"NB_gamma1_relspread_t{T}"] = float((max(g) - min(g)) / abs(np.mean(g)))
    out["max_rel_diff_gamma1_vs_record"] = worst
    dump_json(out, os.path.join(DATA, "second_path.json"))
    print("max rel diff vs record:", worst, " drift t=1.0:", out["NB_gamma1_drift_t1.0"])


if __name__ == "__main__":
    main()
