"""WO-001 / C1 REDO driver — runs the frozen V3-R2 dynamics at reference resolution
and reports N_B*gamma1 and sqrt(N_B)*gamma1 side by side, from the evolved ensemble.

The V3-R2 machinery (v3_r2_authoritative.py, byte-identical to the BRI1 record) already
inserts eps = N_B**(-1/2) into the *dynamics* (integrate_tensor carries eps), measures
kappa3(X) from the evolved ensemble on the Gauss-Legendre tensor grid, and applies only
the exact iid identity kappa3(F) = kappa3(X)/sqrt(N_B) with pipeline assertions. Nothing
about the N_B scaling is inserted analytically. The scaling FIT (log-log slope) is
computed from the data and can fail.

This driver:
  1. runs run() at the reference resolution (nx=240, dt=5e-4) plus a cross-check row;
  2. reports N_B*gamma1 and sqrt(N_B)*gamma1 side by side at t* and the diagnostics;
  3. computes the log-log scaling exponent p from the data (expect p ~= 1; the
     RETRACTED run's exponent was 0.5);
  4. keeps the RETRACTED run labelled in the report (pointer to c1_witness.json @ b5e7dde).
"""
import json
import numpy as np
import v3_r2_authoritative as V

OUT = "../PROGRAM/RESULTS/WO-001/"
LADDER = V.NB_GRID


def gamma1_column(r, T):
    row = r["p1"][str(T)]
    nb = np.array(LADDER, dtype=float)
    g = np.array([row[str(n)]["gamma1_F"] for n in LADDER])
    k3F = np.array([row[str(n)]["kappa3_F"] for n in LADDER])
    eps = np.array([row[str(n)]["epsilon"] for n in LADDER])
    return nb, g, k3F, eps


def scaling_exponent(nb, g):
    p_global, a_global = np.polyfit(np.log(nb), np.log(np.abs(g)), 1)
    local = [float(-np.log(abs(g[i+1])/abs(g[i]))/np.log(nb[i+1]/nb[i]))
             for i in range(len(nb)-1)]
    return float(-p_global), local


def main():
    import time
    t0 = time.time()
    out = {"protocol": ("C1 redo from dynamics; eps=N_B^(-1/2) inserted in the dynamics; "
                        "kappa3(F)=kappa3(X)/sqrt(N_B) is the exact iid identity (asserted "
                        "in code); no scaling inserted analytically"),
           "retracted_run": {"label": "RETRACTED",
                             "file": "c1_witness.json @ b5e7dde",
                             "reason": "scaling 1/sqrt(N_B) was inserted analytically; "
                                       "contradicts BRI1's O(1/N_B)"}}
    # reference resolution (the frozen authoritative setting) + one cross-check
    r_ref = V.run(V.NX_REF, V.DT_REF)
    out["reference"] = {"nx": V.NX_REF, "dt": V.DT_REF}
    r_cross = V.run(120, 1e-3)
    out["crosscheck"] = {"nx": 120, "dt": 1e-3}

    for label, r in (("reference", r_ref), ("crosscheck", r_cross)):
        for T in [V.T_STAR] + V.T_DIAG:
            nb, g, k3F, eps = gamma1_column(r, T)
            p_glob, local = scaling_exponent(nb, g)
            nbg = np.array([n * x for n, x in zip(nb, g)])
            out.setdefault(label, {})[f"T={T}"] = {
                "N_B": [int(n) for n in nb],
                "gamma1_F": [float(x) for x in g],
                "NB_gamma1": [float(x) for x in nbg],
                "sqrtNB_gamma1": [float(np.sqrt(n) * x) for n, x in zip(nb, g)],
                "NB_gamma1_rel_spread": float((np.abs(nbg).max() - np.abs(nbg).min())
                                              / np.abs(nbg).mean()),
                "kappa3_F": [float(x) for x in k3F],
                "epsilon": [float(x) for x in eps],
                "scaling_exponent_global_p": p_glob,
                "scaling_exponent_local": local,
            }
    out["reference"]["odd_epsilon"] = r_ref["odd_epsilon"]
    out["reference"]["gibbs_identity_residual"] = r_ref["gibbs_identity_residual"]
    out["runtime_seconds"] = time.time() - t0
    json.dump(out, open(OUT + "c1_redo_results.json", "w"), indent=1, default=str)

    print("== C1 REDO: gamma1 from finite-N_B dynamics, eps=N_B^(-1/2) in the dynamics ==")
    print("(retracted run: c1_witness.json @ b5e7dde — scaling was inserted analytically)\n")
    for T in [V.T_STAR] + V.T_DIAG:
        d = out["reference"][f"T={T}"]
        print(f"T={T}  (nx={V.NX_REF}, dt={V.DT_REF})")
        print("  N_B      gamma1_F        N_B*gamma1      sqrt(N_B)*gamma1")
        for i, n in enumerate(d["N_B"]):
            print(f"  {n:5d}  {d['gamma1_F'][i]:+.6e}  {d['NB_gamma1'][i]:+.6e}  {d['sqrtNB_gamma1'][i]:+.6e}")
        print(f"  scaling exponent p (global) = {d['scaling_exponent_global_p']:.6f}"
              f"   local = {[round(x, 4) for x in d['scaling_exponent_local']]}")
        print(f"  N_B*gamma1 rel spread = {d['NB_gamma1_rel_spread']:.3e}\n")
    print(f"odd-epsilon control (kappa3 odd in eps): {out['reference']['odd_epsilon']}")
    print(f"Gibbs identity residual: {out['reference']['gibbs_identity_residual']:.3e}")
    print(f"runtime: {out['runtime_seconds']:.0f}s")
    json.dump(out, open(OUT + "c1_redo_results.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
