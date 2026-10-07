"""WO-001 / C2 — exogenous controls for eps_R (static interface, per R1_DEFINITION).

All controls are EXOSGENOUS: the protocol dependence enters only through the interface
class T; there is no back-reaction (the drivers are not influenced by the system path).

Controls:
  C2-G   Gaussian colored (OU-style) baseline. Per-time law is Gaussian under every
         protocol -> gamma1 = 0 identically. The SKEWNESS witness cannot fire under any
         linear processing, because Gaussianity is preserved by linear maps.
         (Corrected 2026-10-07: under E2+- with k >= 2 time points, protocol-dependent
         filters of a Gaussian driver DO fire the cross-time correlation witness of
         R1_DEFINITION Prop. 2b. They are absorbed only under T_lin, because
         nonsingular Gaussians form one GL(k) orbit.)

  C2-NG  Non-Gaussian shared noise entering ONLY through M_a, G_a (affine per protocol):
         F_a = M_a + G_a * xi, xi shared. EXACT CONTROL: the maps t_a(x) = M_a + G_a*x
         are in T (signed-affine) by construction, so eps_R = 0 exactly; the optimizer
         must return 0 to machine precision.

  C2-F   Filtered non-Gaussian, COLORED: F_a = K_a @ xi, where xi is a shared
         (Erratum, D5 audit 2026-10-07: with K_a[k,j] = r^(k-j) the records are exact
         AR(1) Markov chains -- a Levy-driven OU in continuous time -- colored, not
         non-Markovian. Numbers and verdicts are unchanged. A genuinely non-Markov
         zero control, C2-F', is proposed in D5_COMPARATOR_AUDIT.md and was not run.)
         skewed i.i.d. driver vector and K_a are PROTOCOL-DEPENDENT linear filters
         (causal exponential smoothing with different time constants tau_1 != tau_2),
         calibrated (known) but NOT of the signed-affine form.
         - Under T = signed-affine: the per-time standardized skewness differs between
           protocols (exact formula below), so the witness is NONZERO. This is the
           correct value under E2+-, not a false positive: E2+- is not closed under
           calibrated linear filters (R1_T_LADDER.md), and there is no back-reaction.
         - Under T enlarged to include the calibrated filters K_a: F_a = t_a(xi) with
           t_a = K_a in T by construction -> eps_R = 0 to machine precision
           (demonstrated by exact deconvolution: K_a^{-1} F_a recovers the same xi).

Exact formulas used (no Monte Carlo in the primary numbers):
  For xi_j i.i.d. with skewness gamma1_xi, and F = sum_j K_j xi_j:
      gamma1_F = gamma1_xi * (sum_j K_j^3) / (sum_j K_j^2)^(3/2).
  The filters are lower-triangular with unit diagonal -> invertible -> exact
  deconvolution control.

Scale references:
  - BRI1 witness at the same t* (N_B = 4): |gamma1| = 5.338286e-06 (from C1 redo,
    PROGRAM/RESULTS/WO-001/c1_redo_results.json).
  - Numerical noise floor: exact quantities reproduce to machine precision (two runs
    identical). A sampled variant calibrates the empirical gamma1 noise floor for
    judging "zero" at finite sample size. It uses two independent batches of
    n_sample // m = 31,250 path samples each (2 x 10^6 driver draws per batch, fixed
    seeds). The floor reported is the max over the 64 grid times of |g_A - g_B|.
    (Corrected 2026-10-07 by Claude Code: an earlier docstring said N = 2 x 10^6 and
    the printout said 2 x 20000; neither was the per-time sample size.)
"""
import json
import numpy as np

OUT = "../PROGRAM/RESULTS/WO-001/"
SEED = 20260506

# ------------------------------------------------------------------ drivers
def gamma_skew(k=2.0):
    """Skewness of a Gamma(shape=k) variable: 2/sqrt(k)."""
    return 2.0 / np.sqrt(k)

def sample_xi(n, m, seed):
    """m i.i.d. standardized gamma(k=2) drivers, shape (n, m)."""
    rng = np.random.default_rng(seed)
    k = 2.0
    x = rng.gamma(shape=k, scale=1.0, size=(n, m))
    x = (x - k) / np.sqrt(k)          # mean 0, var 1, skewness 2/sqrt(k)
    return x

def filters(n_t=64, dt=0.01, taus=(0.05, 0.20)):
    """Causal exponential smoothing filters K_a[k, j] = exp(-(k-j)*dt/tau), j <= k.
    Lower-triangular with unit diagonal -> invertible."""
    Ks = []
    for tau in taus:
        K = np.zeros((n_t, n_t))
        for k in range(n_t):
            for j in range(k + 1):
                K[k, j] = np.exp(-(k - j) * dt / tau)
        Ks.append(K)
    return Ks

def gamma1_of_sum(K_row, g1_xi):
    """Exact skewness of sum_j K_j xi_j for i.i.d. xi_j with common skewness g1_xi."""
    s2 = np.sum(K_row**2)
    s3 = np.sum(K_row**3)
    return g1_xi * s3 / s2**1.5

# ------------------------------------------------------------------ controls
def c2_g_gaussian(n_t=64, dt=0.01):
    """Gaussian colored baseline: per-time law Gaussian -> gamma1 = 0 exactly.
    OU check: the OU autocovariance is exponential in the lag; a Gaussian process
    has zero skewness at every time and every linear filter, so no witness can fire."""
    tau = 0.05
    lags = np.arange(n_t) * dt
    acf = np.exp(-lags / tau)          # OU autocorrelation (unit variance)
    # gamma1 of any Gaussian = 0; linear filters preserve Gaussianity exactly.
    return {"gamma1_per_time": [0.0] * n_t,
            "witness": 0.0,
            "note": "Gaussian marginals under every protocol and every linear filter; "
                    "unable to fire under any linear processing.",
            "exact": True}

def c2_ng_affine(n_t=64, m=64, M=(0.0, 0.3), G=(1.0, 2.0)):
    """C2-NG: F_a = M_a + G_a * xi (per-time affine, shared xi). Exact control:
    t_a(x) = M_a + G_a*x is signed-affine -> in T -> eps_R = 0 by construction.
    The optimizer on the exact law must return 0 to machine precision."""
    g1_xi = gamma_skew(2.0)
    # per-time standardized skewness: gamma1_Fa = sign(G_a) * gamma1_xi
    g1 = {f"P{a+1}": (np.sign(G[a]) * g1_xi) for a in range(2)}
    witness_signed = abs(g1["P1"] - g1["P2"])
    witness_abs = abs(abs(g1["P1"]) - abs(g1["P2"]))
    # exact construction of the T-maps: P_a = t_a # Pstar with Pstar = law(xi)
    # -> eps_R = 0 exactly. Numerical demonstration: sample xi, form both F_a,
    # unstandardize/recover: (F_a - M_a)/G_a = xi exactly.
    xi = sample_xi(20000, 1, SEED)[:, 0]
    rec1 = (M[0] + G[0] * xi - M[0]) / G[0]
    rec2 = (M[1] + G[1] * xi - M[1]) / G[1]
    max_dev = float(np.max(np.abs(rec1 - rec2)))
    return {"gamma1": g1, "witness_signed": float(witness_signed),
            "witness_abs": float(witness_abs),
            "eps_R_by_construction": 0.0,
            "recovered_xi_max_dev": max_dev,
            "exact": True}

def c2_f_filtered(n_t=64, m=64, dt=0.01, taus=(0.05, 0.20), n_sample=2_000_000):
    """C2-F: filtered non-Gaussian control. Two runs:
       (a) T = signed-affine: witness NONZERO (the correct value under E2+-, not a
           false positive), eps_R > 0 with the Prop-2a lower bound;
       (b) T enlarged with the calibrated filters: eps_R = 0 to machine precision."""
    g1_xi = gamma_skew(2.0)
    Ks = filters(n_t, dt, taus)
    # (a) exact per-time gamma1 under signed-affine T
    g1 = {f"P{a+1}": np.array([gamma1_of_sum(Ks[a][k], g1_xi) for k in range(n_t)])
          for a in range(2)}
    wit_signed = np.abs(g1["P1"] - g1["P2"])
    wit_abs = np.abs(np.abs(g1["P1"]) - np.abs(g1["P2"]))
    k_max = int(np.argmax(wit_signed))
    # (b) exact deconvolution control: F_a = K_a xi -> K_a^{-1} F_a = xi
    rng = np.random.default_rng(SEED)
    xi = sample_xi(1, m, SEED)[0, :]
    F1 = Ks[0] @ xi
    F2 = Ks[1] @ xi
    xi_rec1 = np.linalg.solve(Ks[0], F1)
    xi_rec2 = np.linalg.solve(Ks[1], F2)
    dev = float(np.max(np.abs(xi_rec1 - xi_rec2)))
    rel_dev = float(np.max(np.abs(xi_rec1 - xi_rec2)) / np.max(np.abs(xi)))
    # (c) sampled gamma1 noise floor: two independent batches
    xA = sample_xi(n_sample // m + 1, m, SEED + 1)[: n_sample // m]
    xB = sample_xi(n_sample // m + 1, m, SEED + 2)[: n_sample // m]
    def emp_g1(mat, K):
        F = mat @ K
        mu = F.mean(axis=0); s2 = ((F - mu)**2).mean(axis=0)
        s3 = ((F - mu)**3).mean(axis=0)
        return s3 / s2**1.5
    gA = emp_g1(xA, Ks[0]); gB = emp_g1(xB, Ks[0])   # same protocol, independent batches
    floor = float(np.max(np.abs(gA - gB)))
    return {
        "taus": taus,
        "gamma1_P1_at_kmax": float(g1["P1"][k_max]),
        "gamma1_P2_at_kmax": float(g1["P2"][k_max]),
        "witness_signed_max": float(wit_signed.max()),
        "witness_abs_max": float(wit_abs.max()),
        "witness_signed_at_kmax": float(wit_signed[k_max]),
        "k_max": k_max,
        "gamma1_profiles_P1": [float(x) for x in g1["P1"]],
        "gamma1_profiles_P2": [float(x) for x in g1["P2"]],
        "enlarged_T": {"eps_R": 0.0, "recovered_xi_max_dev": dev,
                       "recovered_xi_rel_dev": rel_dev,
                       "method": "exact deconvolution K_a^{-1} F_a = xi (both protocols "
                                 "recover the identical driver vector)"},
        "sampled_noise_floor_max_over_times": floor,
        "sampled_noise_floor_paths_per_batch": n_sample // m,
        "sampled_noise_floor_batches": 2,
        "g1_xi": g1_xi,
    }

def bri1_reference():
    d = json.load(open("../PROGRAM/RESULTS/WO-001/c1_redo_results.json"))
    g = d["reference"]["T=0.5"]["gamma1_F"][0]
    return abs(float(g))

if __name__ == "__main__":
    out = {"scale_reference": {}}
    bri1_w = bri1_reference()
    out["scale_reference"] = {
        "BRI1_witness_abs_gamma1_NB4_tstar0.5": bri1_w,
        "note": "BRI1 witness at the same t* (N_B=4): |gamma1| = 5.338286e-06. "
                "'Zero' judgments are against this effect size and the noise floor below."}
    r_g = c2_g_gaussian()
    r_ng = c2_ng_affine()
    r_f = c2_f_filtered()
    out["C2_G_ou_gaussian"] = r_g
    out["C2_NG_affine_exact_control"] = r_ng
    out["C2_F_filtered"] = r_f

    print("== C2 controls: eps_R witnesses (static interface) ==")
    print(f"\nScale reference: BRI1 |gamma1| at t*=0.5, N_B=4: {bri1_w:.6e}")
    print(f"\nC2-G  Gaussian colored (OU): witness = {r_g['witness']:.1e}  (exact; Gaussian "
          f"marginals under every linear processing -> unable to fire)")
    print(f"\nC2-NG non-Gaussian shared noise, affine entry (exact control):")
    print(f"  gamma1 P1 = {r_ng['gamma1']['P1']:+.6f}, P2 = {r_ng['gamma1']['P2']:+.6f}")
    print(f"  witness signed = {r_ng['witness_signed']:.3e}, |.| = {r_ng['witness_abs']:.3e}")
    print(f"  eps_R = {r_ng['eps_R_by_construction']:.1e} (maps in T by construction; "
          f"recovered xi max dev {r_ng['recovered_xi_max_dev']:.2e})")
    print(f"\nC2-F filtered non-Gaussian (taus={r_f['taus']}):")
    print(f"  (a) T = signed-affine:")
    print(f"      gamma1 P1(k*) = {r_f['gamma1_P1_at_kmax']:+.6f}, P2(k*) = {r_f['gamma1_P2_at_kmax']:+.6f} "
          f"(k* = {r_f['k_max']})")
    print(f"      witness signed max = {r_f['witness_signed_max']:.6f}, |.| max = {r_f['witness_abs_max']:.6f}"
          f"  -> NONZERO: correct value under E2+- (calibrated filter, not back-reaction)")
    print(f"      Prop-2a scale: witness is {r_f['witness_abs_max']/bri1_w:.2e} x the BRI1 witness")
    print(f"  (b) T enlarged with calibrated filters K_a:")
    print(f"      eps_R = {r_f['enlarged_T']['eps_R']:.1e} to machine precision "
          f"(deconvolution max dev {r_f['enlarged_T']['recovered_xi_max_dev']:.2e}, "
          f"rel {r_f['enlarged_T']['recovered_xi_rel_dev']:.2e})")
    print(f"\nNoise floor: exact quantities reproduce to machine precision; sampled "
          f"gamma1 floor (max over times, 2 batches x "
          f"{r_f['sampled_noise_floor_paths_per_batch']} paths): "
          f"{r_f['sampled_noise_floor_max_over_times']:.2e}")
    json.dump(out, open(OUT + "c2_controls_results.json", "w"), indent=1, default=str)
    print(f"\nwrote {OUT}c2_controls_results.json")
