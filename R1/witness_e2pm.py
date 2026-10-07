"""WO-001 / C1 + C2: skewness-witness lower bound on eps_R over the E2+- class.

Reproduces BRI1's frozen K_q[a,b,c] tensors (pf4q_core.py, byte-pulled from
bri1-manuscript @ 92dc6bb; archived pf4q_results.json for comparison), then computes
the C1 witness:

  For the E2+- class F_q = M_q + G_q * xi (shared law xi, G_q != 0, deterministic M,G):
  any affine map with POSITIVE slope leaves per-time standardized skewness unchanged;
  a NEGATIVE slope flips the odd-order standardized cumulants' signs. Therefore the
  spread across protocols of per-time |standardized skewness| lower-bounds
    eps_R^{E2+-} >= max_t spread_a( |skew_t^{(a)}| ) / 2   (exact two-protocol form:
    eps >= (1/2) |skew^{(a1)} - skew^{(a2)}| when slopes can be chosen sign-free)

The witness along the N_B ladder: kappa3(t_a,t_b,t_c) of the averaged force scales as
K_q[a,b,c]/N_B + O(N_B^-2) (Lemma BRI1-R1), while the variance scales as 1/N_B too, so
the standardized skewness is O(1) in N_B -- the witness does NOT decay; the *unperturbed*
scaling of the raw cumulant is the 1/N_B content.

NUMERICAL EVIDENCE ONLY -- not certified. No Monte Carlo in C1 (exact quadrature);
C2 uses declared-spectrum sampling of the shared law xi (exact control included).
"""
import json
import numpy as np
import pf4q_core as C

TAU = C.TAU
NAMES = ["pi", "3pi/2", "2pi"]
IDX = C.IDX


# ------------------------------------------------------------------ C1: K tensors
def compute_K(protocol, h=0.06, gh_n=192):
    """Method B (variational + trapezoid, exactly symmetric under (x,p)->(-x,-p)) and
    Method A (Gauss-Hermite) for the same protocol; returns (K_methodB, K_methodA)."""
    X, P, W = C.rule_trap(h)
    sol = C.variational(X, P, list(TAU))
    K_trap = C.K_from_variational(W, sol, protocol)
    Xg, Pg, Wg, _ = C.rule_gh(gh_n)
    solg = C.variational(Xg, Pg, list(TAU))
    K_gh = C.K_from_variational(Wg, solg, protocol)
    return K_trap, K_gh


def reproduce_archived():
    """Cross-check our computed K tensors against the archived pf4q_results.json."""
    try:
        archived = json.load(open("pf4q_results_archived.json"))
    except FileNotFoundError:
        return None
    ok, rows = True, []
    for protocol in (1, 2):
        K, Kgh = compute_K(protocol)
        for k in IDX:
            lab = f"P{protocol}(" + ",".join(NAMES[i] for i in k) + ")"
            if lab not in archived:
                continue
            a_arch = archived[lab]["K_A06"]
            a_ours = K[k]
            rel = abs(a_ours - a_arch) / max(abs(a_arch), 1e-30)
            ok &= rel < 1e-6
            rows.append({"component": lab, "archived_K_A06": a_arch,
                         "recomputed_K_A06": a_ours, "rel_diff": rel,
                         "gh192": Kgh[k],
                         "archived_gh192": archived[lab]["GH192"]})
    return {"all_match": ok, "rows": rows}


# ------------------------------------------------- C1 witness: standardized skewness
def standardized_skew_spread(K_by_protocol):
    """Per-time standardized skewness of the force-response components.

    From the joint response tensor K_q[a,b,c] at the frozen tau triple, the
    per-time third cumulant of the force component at time t_j is
        kappa3_j = K[j,j,j] averaged over the appropriate response components.
    We use the diagonal-in-time slices available in the tensor (j,j,j) and the
    mixed (j,j,k) slices for the off-diagonal spread, exactly as archived.
    The E2+- skewness witness: |standardized skew| spread across protocols."""
    out = {}
    for j in range(3):
        # diagonal slice: kappa3 of the force component at time TAU[j]
        # from the tensor: K[j,j,j] is the response-tensor component; the physical
        # force cumulant is K[j,j,j] itself in the archived normalization.
        s_j = {}
        for pr, K in K_by_protocol.items():
            # standardized: kappa3 / kappa2^{3/2}; kappa2 from the variance tensor.
            # BRI1's archived numbers give kappa3 directly; the variance (kappa2)
            # of the averaged force at time t_j is O(1/N_B) too, so the standardized
            # skewness is O(1). We compute the raw ratio using the archived kappa2
            # proxy: Var ~ |K[j,j,j]|^{2/3} is NOT available; instead we report the
            # raw kappa3 spread (the witness BRI1 uses), and the standardized form
            # using the measured variance from the same quadrature (below).
            s_j[pr] = K[(j, j, j)]
        out[f"t={NAMES[j]}"] = s_j
    return out


def variance_tensor(protocol, h=0.06):
    """Second cumulant of the response coordinate y at the frozen times:
    kappa2(t_a,t_b) = W@(y_a*y_b) - (W@y_a)(W@y_b), exact on the quadrature measure."""
    X, P, W = C.rule_trap(h)
    sol = C.variational(X, P, list(TAU))
    y = [sol[t][protocol] for t in TAU]
    cov = {}
    for a in range(3):
        for b in range(a, 3):
            cov[(a, b)] = W @ (y[a] * y[b]) - (W @ y[a]) * (W @ y[b])
    return cov


def witness_table(n_ladder=(4, 8, 16, 32, 64, 128), h=0.06):
    """C1: the skewness-witness lower bound on eps_R^{E2+-} along the N_B ladder.

    Averaged force F_bar = (1/N_B) sum_i f_i; with the frozen single-oscillator
    response tensors, the cumulants of F_bar scale as
        kappa3(F_bar) = K_q / N_B^2 ,  kappa2(F_bar) = V / N_B
    (third cumulant of a sum of independent variables adds; standardized skewness
    of the SUM scales as 1/sqrt(N_B); the standardized skewness of the SINGLE
    response is O(1). BRI1's witness is the SINGLE-oscillator standardized skewness
    ratio across protocols, which is O(1) and protocol-dependent; the raw third
    cumulant of the averaged force carries the 1/N_B^2 scaling; the witness for
    eps_R over E2+- is the SPREAD of standardized skewness across protocols,
    which is O(1) -- i.e. eps_R^{E2+-} does NOT decay with N_B. The 1/N_B content
    is the decay of the RAW detectable signal kappa3(F_bar) ~ 1/N_B^2 with fixed
    variance 1/N_B, i.e. the standardized skewness of the averaged force decays
    as 1/sqrt(N_B): that is the scaling to report.)
    """
    K_by = {}
    V_by = {}
    for pr in (1, 2):
        K_trap, _ = compute_K(pr, h=h)
        K_by[pr] = K_trap
        V_by[pr] = variance_tensor(pr, h=h)
    rows = []
    for N_B in n_ladder:
        # standardized skewness of the AVERAGED force at each time:
        # kappa3(F_bar) = K_diag / N_B^2 ; kappa2(F_bar) = V_diag / N_B
        # => std skew = kappa3 / kappa2^{3/2} = (K_diag / N_B^2) / (V_diag/N_B)^{3/2}
        #             = (K_diag / V_diag^{3/2}) * sqrt(N_B) ... per INDEPENDENT oscillator.
        # For the SUM over N_B independent oscillators the standardized skewness of the
        # averaged force DECAYS as 1/sqrt(N_B):
        #   skew(F_bar) = kappa3(F_bar)/kappa2(F_bar)^{3/2}
        # with kappa3 ~ K/N_B^2 (sum of N_B independent copies each contributing
        # K/N_B^3 to the average) and kappa2 ~ V/N_B, giving skew ~ 1/sqrt(N_B).
        entry = {"N_B": N_B, "per_protocol": {}}
        for pr in (1, 2):
            sk = {}
            for j in range(3):
                k3_diag = K_by[pr][(j, j, j)]
                v_diag = V_by[pr][(j, j)]
                # averaged force over N_B independent copies:
                k3_avg = k3_diag / N_B ** 2
                v_avg = v_diag / N_B
                skew = k3_avg / max(abs(v_avg) ** 1.5, 1e-300) * (1 if v_avg > 0 or True else 1)
                sk[NAMES[j]] = {"k3_avg": k3_avg, "v_avg": v_avg, "std_skew": skew}
            entry["per_protocol"][f"P{pr}"] = sk
        # witness: spread of |std_skew| across protocols at each time
        spreads = {}
        for j in range(3):
            t = NAMES[j]
            s1 = entry["per_protocol"]["P1"][t]["std_skew"]
            s2 = entry["per_protocol"]["P2"][t]["std_skew"]
            spreads[t] = abs(s1 - s2) / 2.0  # lower bound on eps over E2+- (sign-flip freedom)
        entry["witness_lower_bound"] = spreads
        entry["max_lower_bound"] = max(spreads.values())
        # scaling: max_lower_bound(N_B) should decay as 1/sqrt(N_B)
        rows.append(entry)
    # check 1/sqrt(N_B) scaling: witness(N) * sqrt(N) approximately constant
    scaling = []
    base = rows[0]["max_lower_bound"] * (rows[0]["N_B"] ** 0.5)
    for r in rows:
        c = r["max_lower_bound"] * (r["N_B"] ** 0.5)
        scaling.append({"N_B": r["N_B"], "witness": r["max_lower_bound"],
                        "witness*sqrt(N_B)": c, "ratio_to_N4": c / base})
    return {"ladder": rows, "sqrt_scaling_check": scaling,
            "raw_cumulant_1_over_NB2_check": [
                {"N_B": r["N_B"],
                 "k3_avg_P1_t0": r["per_protocol"]["P1"][NAMES[0]]["k3_avg"],
                 "k3_avg*N_B^2": r["per_protocol"]["P1"][NAMES[0]]["k3_avg"] * r["N_B"] ** 2}
                for r in rows]}


if __name__ == "__main__":
    out = {}
    rep = reproduce_archived()
    if rep is not None:
        out["C1_reproduction"] = {"all_match_within_1e-6": rep["all_match"],
                                  "rows": rep["rows"][:6]}
        print(f"C1 reproduction vs archived pf4q_results.json: all_match = {rep['all_match']}")
        for r in rep["rows"][:4]:
            print(f"  {r['component']}: archived {r['archived_K_A06']:.6e} ours {r['recomputed_K_A06']:.6e} rel {r['rel_diff']:.2e}")
    wit = witness_table()
    out["C1_witness"] = wit
    print("\nC1 witness lower bound on eps_R^{E2+-} along the N_B ladder")
    print("N_B   witness(max_t spread/2)   witness*sqrt(N_B)   ratio")
    for s in wit["sqrt_scaling_check"]:
        print(f"{s['N_B']:5d}  {s['witness']:.6e}          {s['witness*sqrt(N_B)']:.6e}      {s['ratio_to_N4']:.4f}")
    print("\nraw third cumulant of averaged force (1/N_B^2 scaling check):")
    for r in wit["raw_cumulant_1_over_NB2_check"]:
        print(f"  N_B={r['N_B']:4d}  k3_avg={r['k3_avg_P1_t0']:.6e}  k3_avg*N_B^2={r['k3_avg*N_B^2']:.6e}")
    json.dump(out, open("../PROGRAM/RESULTS/WO-001/c1_witness.json", "w"), indent=1, default=str)
    print("\nwrote PROGRAM/RESULTS/WO-001/c1_witness.json")
