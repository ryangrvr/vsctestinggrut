# R1 — THE INTERFACE LADDER (Claude Code) · v3 (frozen definition) · 2026-10-07

*v2 (2026-10-06) is kept below as the derivation record. §0 and §§8–11 were added in v3
and govern where they differ.*

## 0. FROZEN R1 DEFINITION (owner rulings G2-01 … G2-06, `PROGRAM/OWNER_RULINGS.md`)

> **Pre-result vs post-result labeling (ruling G2-10).**
>
> **FROZEN PRE-RESULT** (text at `82d311e`, committed before the WO-002 numbers were
> opened):
> - T_R1, d_op and the verdict table;
> - the common-carrier commitment as "one latent-to-record map h for all protocols; no
>   h_a";
> - Prop. E, §10 E1/E2, and the D5 mode-selection mandate;
> - the G2-08 carrier certificate.
>
> **The non-identifiability is pre-result.** "With unrestricted protocol-dependent
> readouts, any record family has an exogenous explanation; hence every reciprocity
> claim is conditional on a certified common readout" is a consequence of the frozen
> definition and is cited as such.
>
> **POST-RESULT** (`cb81a3b` and later, written after the WO-002 numbers were open). The
> following are labeled **POST-RESULT SYNTHESIS / STAGE-3 SEED**:
> - the "precise form v3.1" of the carrier (instantaneous state);
> - "Why instantaneous";
> - record completeness;
> - the 10-item certificate checklist;
> - and, per G2-10, Z_A (interventionally sufficient predictive carrier state relative
>   to a frozen repertoire A), [h]_T (the protocol-invariant readout equivalence class)
>   and the measurement-invariance framing.
>
> They are **not** modifications of the frozen definition and **not** retroactive
> inputs to WO-002. WO-002's verdict rests only on the pre-result G2-08 carrier
> certificate.
>
> Mathematical errata from adversarial verification (F1/F2 justification, D3, the F4
> example, Prop. 2b) correct proofs, not the definition.

**Interface class.**
- **T_R1 = GL(k) with translations** on the observed path record.
- Independently calibrated nonlinearities and filters are either removed with their
  known maps before the inf (not fitted), or included in T.
- **Canonical reduction:** centering and whitening, P ↦ P̃ = law of Σ^(−1/2)(Y − μ).
  This leaves an O(k) quotient.
- **Standing assumption:** finite, nonsingular covariance of every P_a. If a covariance
  is singular, work on the affine hull of its support. The rank of Σ is a T_R1
  invariant, so laws with different ranks lie in different orbits.

**Common-carrier / mode-stability commitment** (replaces G2-01's "latent dimension").

*Precise form, v3.1 — POST-RESULT SYNTHESIS / STAGE-3 SEED (G2-10). It clarifies,
and does not replace, the frozen pre-result commitment "one latent-to-record map h for
all protocols; no h_a".*
- **Environment state process.** Z = (Z(t))_t is the environment's state process. Its
  state space may have any dimension.
- **Common carrier.** **One** fixed readout channel h is applied to the environment's
  **instantaneous** state, W(t) := h(Z(t)), on **one** fixed time base and sampling
  grid, for every protocol. A calibrated fixed filter of h(Z) also counts. Then
  Y_a = t_a(W), with t_a ∈ T_R1.
- **Exogenous null:** Law(Z) does not depend on the protocol.
- **Back-reaction:** the protocol changes Law(Z) through the system.
- **Mode selection** (excluded by the commitment): the protocol changes the readout
  channel h ↦ h_a. That includes channel weights, time windows or trigger phases,
  sampling grids, and filter memory reaching outside the record.
- **Consequence:** under the null, P★ = Law(W) is shared, and Theorem C applies verbatim
  (§10).

**Why instantaneous.** If h could be any functional of the *initial* environment state,
then every closed system would be "exogenous with mode selection". For example, BRI1's
X1 can be written F_q = 𝔉_t[q, z₀], with z₀ ~ Gibbs independent of q (BRI-UPPER:
X1 ∈ E_univ). The applicability test would then exclude the very model it is meant to
certify. With the instantaneous definition, X1 has carrier PASS (one readout,
N_B^(−1/2)·Σ_j x_j(t)), and its protocol dependence is back-reaction.

**Record completeness (design check).**
- If interfaces are filters of one driver, the record must contain the full support of
  every interface kernel, past **and** future, at driver resolution, with every K_a
  invertible on the record.
- This is **sufficient** for a common read subspace, not equivalent to it.
- Injectivity is required **into the observed record**: a path-level bijective filter
  whose memory falls outside the grid is mode selection at the grid level.

**Distance.**
- d_op is the bounded-Lipschitz quotient distance:

  d_q^BL(P, Q) := min over O ∈ O(k) of d_BL(P̃, O#Q̃),

  d_BL(P, Q) := sup{ |E_P f − E_Q f| : ‖f‖_∞ ≤ 1, Lip(f) ≤ 1 }, with Euclidean
  distance on ℝ^k.
- **Normalization stated:** ‖f‖_BL := max(‖f‖_∞, Lip f). Dudley's β uses
  ‖f‖_∞ + Lip f, and β ≤ d_BL ≤ 2β (sharp).
  - **Coupling form.** d_BL equals W₁ for the truncated cost min(|x − y|, 2).
  - **Citations.** Dudley, *Real Analysis and Probability*, 2nd ed. 2002: Prop. 11.3.2
    for the metric; Thm. 11.3.3 for metrization of weak convergence (stated for
    sequences).
  - **Mixing conventions.** The witness bound ε_R ≥ |E f|/(2‖f‖) holds for (d_BL, max
    norm) and for (β, sum norm). (d_BL, sum norm) is valid but looser. Only (β, max
    norm) can fail, by a factor of up to 2.
- **Caution for estimation (D4).**
  - d_q^BL is **not** weakly continuous in the raw laws, because whitening uses second
    moments. A vanishing contamination can move d_q by O(1).
  - The plug-in d_BL in dimension k ≥ 3 converges only like n^(−1/k).
  - So estimation should use the per-f witness form, not plug-in d_BL.
- ε_R := inf over P★ of max_a d_q^BL(P_a, P★). Its theorems are §8.
- **Skewness (and the W₃ results of v1/v2) stay as the analytic BRI calibration layer.**
  Because d_BL ≤ W₁ ≤ W₃, the W₃ lower bounds do **not** transfer to d_BL. The d_BL
  lower bounds are §8.
- **MMD** may be used only as a computational proxy with a frozen kernel, after its
  connection to d_BL is shown. That has not been done.

**Empirical rule.**
- Every reciprocity claim needs a **mode-stability certificate**: calibration showing
  that (i) the interface nonlinearity is known, and (ii) the protocols do not change
  which environmental modes couple.
- Without a certificate the verdict is **NO RECIPROCITY VERDICT**, not ε_R > 0.
- **What the certificate must cover** — POST-RESULT SYNTHESIS / STAGE-3 SEED (G2-10).
  Each item is tied to a mechanism that a loophole hunt found NOT excluded by the
  earlier wording. Workflow verification is recorded in CHECKS.
  1. **Interface is deterministic, invertible and calibrated.** Residual uncalibrated
     curvature must be below the witness: 3σ·|φ″_res/φ′| < |witness| at every
     operating point. For BRI1 at N_B = 4 that is about 1.8×10⁻⁶/σ.
  2. **Readout noise is protocol-independent and calibrated.** Calibrated nonlinearities
     must be removed on noise-free data or with a noise model. Additive noise is a
     kernel, not a map, so "removed by known maps" does not cover it.
  3. **No random (run-to-run) interface gains or offsets** beyond a calibrated
     stationary model. Mixtures of affine images of a symmetric law can be skewed.
  4. **One fixed time base, sampling grid and trigger phase.** No protocol-dependent
     clock jitter, latency, window or phase of a nonstationary environment.
  5. **One readout channel with fixed weights.** No push-pull reweighting of
     environmental sources.
  6. **Record completeness**, as above.
  7. **No outcome-dependent selection:** no vetoes, cuts or lock-loss rejection.
  8. **Only invertible calibrated nonlinearities.** Saturation, clipping and
     quantization are excluded unless provably inactive.
  9. **The protocol acts on the environment only through the system.** No actuator
     heating, EMI, vibration or other cross-talk.
  10. **Estimation is controlled:** equal or modelled per-protocol sample sizes (D4).

**D5 must discriminate three explanations:**
- (A) an unchanged environment plus a calibrated interface transformation;
- (B) an unchanged environment plus protocol-dependent mode selection;
- (C) a responding environment.

**R1 exit gate (G2-02 item 5; G2-06 item 6).**
- (i) T scope fixed. Done, per this section.
- (ii) WO-002 decides, yes or no: does the BRI1 intervention family change its copula
  class modulo the reflection group ℛ? Or it identifies precisely why T_mono trivializes
  it (§9).
- (iii) d_op frozen with the proved inequality (§8).
- (iv) D5 complete, including mode selection.

Then R1 terminates and Stage 3 opens. C4 continues as laboratory preparation and does
not block Stage 3. **No Stage-3 candidate is frozen, scored or optimized before then.**

**Order:** WO-002 → final T → d_op → D5 → R1 terminal → Stage 3.

**R1 boundary (ruling G2-08, `PROGRAM/OWNER_RULING_R1_BOUNDARY.md`).**

**Verdict logic.** Operational reciprocity needs both a common-carrier certificate and
the failure of T-separability.

| Carrier | Protocol classes under T | Verdict |
|---|---|---|
| PASS | different | **R1-PASS** |
| PASS | same | R1-NULL |
| UNRESOLVED | different | NO RECIPROCITY VERDICT |
| FAIL | different | MODE SELECTION (not reciprocity) |
| FAIL or UNRESOLVED | same | R1-NULL |

**BRI1 carrier:** PASS. It has the same bath degrees of freedom, Hamiltonian class,
equilibrium ensemble and readout; protocols change only the forcing.

**Two-tier T.**
- **Tier 1 — calibrated-readout reciprocity.** T = GL(k) on the record, plus the common
  carrier.
  - BRI1: **R1-PASS**, by Theorem C (under the common carrier, §10) plus the
    certificate.
  - Banked by the ruling regardless of WO-002. Its SCOREBOARD entry waits for the
    external check (rule 8).
- **Tier 2 — readout-robust reciprocity.** T = T_mono, with residual group ℛ = coordinate
  reflections only (no permutations across time coordinates).
  - **This is the declared top of R1: no larger class will be considered.**

**Stopping rule.**
- If BRI1's protocols lie in one copula reflection orbit under T_mono, the reciprocity
  spine ends as a portable observable.
- Tier 1 stays banked as a calibrated-readout result. There is no rescue class.

**Finite-witness asymmetry.**
- Under T_mono, an escape on one finite grid is a process-level escape.
- A null on one grid is a null for that projection only, unless that projection was
  declared the terminal scope in advance.
- No terminal projection has been declared.

---


**Question (Review 2, open).** E₂± is not closed under independently calibrated linear
interface maps; C2-F showed this. Does BRI1's escape survive once T is enlarged?

**Answer.**
- **Against every linear interface acting on a common carrier: yes, BRI1 still
  escapes.**
  - That means interfaces injective on the shared environment record (v3.1 wording).
  - This holds causal or not, calibrated or not, at the grid level and at the path
    level.
  - The reason is structural: P0 is exactly sign-symmetric, and an **injective** linear
    map cannot create an odd cumulant (Theorem C).
  - **Without injectivity (mode selection) the claim is false:** see §10 E2. The v2
    wording "every linear interface class" overclaimed and is corrected here.
- **Against per-time nonlinear interfaces at a single time: no, it is absorbed**
  (Prop. D1).
- **Against per-time nonlinear interfaces across times: OPEN.** The question reduces to
  two computable leading-order channels (Prop. D4 → WO-002).
  - Per-time nonlinear and linear interfaces are incomparable: they share only E₂±.
    So the ladder is a lattice, not a chain.
- **Against unrestricted interfaces:** everything is absorbed and R1 is trivial
  (Prop. E).

So T cannot be derived; it is a priced commitment. §6 states the owner decision this
requires.

**Status.**
- Theorem A, Props. B, C1, C2 and D1–D3: DERIVED (proofs below).
- E: DERIVED given a cited standard theorem; the primary-text check is pending.
- D4: formal leading-order criteria only (two channels); NOT proved.
- Sanity checks are in `r1_t_ladder_check.py` and `_output.json`. They are checks, not
  results.
- The choice of d_op per class (below) is a definition decision, open to owner veto.

## 1. The ladder

Grid-level data are as in v1 §1: laws P_a on ℝ^k with finite third moments. For
T_caus and T_lin, assume in addition that **Cov P_a is nonsingular**.

| Class | Maps y ↦ M + K y with … | Canonical form s_T(P) = law of … | Residual group H_T |
|---|---|---|---|
| E₂± (v1) | K diagonal, invertible | D⁻¹(Y − μ), with D = diag(sd) | signs {±1}^k |
| T_caus | K lower-triangular, invertible: causal linear interfaces with memory | L⁻¹(Y − μ), where L is the Cholesky factor of Cov (positive diagonal): the standardized innovations | signs {±1}^k |
| T_lin | K ∈ GL(k): any linear interface, including non-causal smoothing | Σ^(−1/2)(Y − μ): the whitened law | O(k) |

E₂± ⊂ T_caus ⊂ T_lin. Each is a group. T_mono (§5, per-time nonlinear) also contains
E₂±, but T_lin ∩ T_mono = E₂±. **The ladder is a lattice, not a chain.**

**Definition (v2).**
- d_op^T(P, Q) := W₃(s_T P, s_T Q).
- ε_R^T := inf over P★ of max_a inf over t_a ∈ T of d_op^T(P_a, t_a#P★).
- For T = E₂± this is v1 exactly.

**Equivariance lemma.** For t ∈ T, s_T(t#Q) = h·s_T(Q) for some h ∈ H_T. Every
h ∈ H_T arises in this way.

*Proof.*
- **T_caus.** Let Y′ = M + KY. Then Cov Y′ = (KL)(KL)ᵀ. KL is lower-triangular with
  diagonal K_ii·L_ii ≠ 0, so the Cholesky factor of Y′ is KL·S, with
  S = diag(sign K_ii). Then (KLS)⁻¹(Y′ − EY′) = S·L⁻¹(Y − μ). K = diag(s) gives
  S = diag(s).
- **T_lin.** O := Σ′^(−1/2)·K·Σ^(1/2) satisfies OOᵀ = Σ′^(−1/2)·KΣKᵀ·Σ′^(−1/2) = I, and
  Σ′^(−1/2)(Y′ − EY′) = O·Σ^(−1/2)(Y − μ). Taking K = O gives that O. ∎

## 2. Theorem A (quotient form, whole ladder)

Define

d_q^T(P, Q) := min over h ∈ H_T of W₃(s_T P, h·s_T Q).

The minimum is attained: H_T is compact and h ↦ W₃(·, h·) is continuous.

Then:
- inf over t ∈ T of d_op^T(P, t#Q) = d_q^T(P, Q);
- d_q^T is a pseudometric;
- d_q^T(P, Q) = 0 if and only if P ∈ T#Q;
- ε_R^T = inf over P★ of max_a d_q^T(P_a, P★).

Moreover:
- **(i)** ε_R^T = 0 if and only if all the P_a lie in one T-orbit;
- **(ii)** ½·diam ≤ ε_R^T ≤ diam.

*Proof.*
- The equivariance lemma gives the first equality. H_T acts by Euclidean isometries,
  so the proof of v1 Prop. 1 applies verbatim.
- For the zero set: P = t#(law of s_T P) with t ∈ T, namely y ↦ μ + Ly or
  y ↦ μ + Σ^(1/2)y. ∎

**Not claimed:** that the value ε_R^T is monotone in T, since the distances are
T-adapted. What is monotone is the zero set: if T ⊂ T′, then ε_R^T = 0 implies
ε_R^(T′) = 0.

## 3. Proposition B (witnesses)

**(B1) T_caus.** v1 Prop. 2 (both parts) applies verbatim to the innovation
coordinates U = s_caus(P):

ε_R^caus ≥ max_{a,b,i} | |γ^inn_a(i)| − |γ^inn_b(i)| | / (2·L^inn_ab(i)).

The first innovation is Y₁ standardized, so the first-time skewness is a T_caus witness.
Later times enter only through their innovations.

**(B2) T_lin (Mardia skewness).** Let W = s_lin(P) and
√β₁(P) := ‖E W^⊗3‖_F. This is Mardia's multivariate skewness β₁,k = E[((X−μ)ᵀΣ⁻¹(Y−μ))³]
for independent copies, as quoted in Koizumi–Okamoto–Seo, TR08-14 §2.1. The primary text
(Biometrika 57:519, 1970) was not inspected. The tensor identity is proved directly. Let μ_P := (E|W|³)^(1/3),
with Euclidean |·|. Then:

| √β₁(P) − √β₁(Q) | ≤ d_q^lin(P, Q)·Λ_PQ, where Λ_PQ = μ_P² + μ_Pμ_Q + μ_Q².

**Hence ε_R^lin ≥ max_{a,b} | √β₁(P_a) − √β₁(P_b) | / (2Λ_ab).**

Also, μ ≥ √k, by Lyapunov's inequality and E|W|² = k.

*Proof.*
- **Invariance.** O^⊗3 preserves the Frobenius norm, so √β₁ is O(k)-invariant.
- **Coupling.** Fix h and an optimal W₃ coupling of A = W_P and B = h·W_Q.
- **Telescoping.** A^⊗3 − B^⊗3 = (A−B)⊗A⊗A + B⊗(A−B)⊗A + B⊗B⊗(A−B).
  - With ‖E X‖_F ≤ E‖X‖_F and ‖a⊗b⊗c‖_F = |a||b||c|, this gives
    ‖E A^⊗3 − E B^⊗3‖_F ≤ E[|A−B|·(|A|² + |A||B| + |B|²)].
- **Hölder and Minkowski.** Hölder (3, 3/2) and Minkowski bound this by W₃·Λ_PQ, as in
  v1 Prop. 2a.
- **Conclusion.** Apply the reverse triangle inequality, then Theorem A(ii). ∎

**Entry bound.** Write κ₃(Y) for the third-cumulant tensor and Σ for the covariance.
Since A^⊗3 has smallest singular value σ_min(A)³:

√β₁(P) = ‖(Σ^(−1/2))^⊗3·κ₃(Y)‖_F ≥ |κ₃(Y_i, Y_i, Y_i)| / λ_max(Σ)^(3/2), for every i.

## 4. Theorem C (symmetry obstruction): BRI1 escapes every linear interface class

**Facts used, all from the BRI1 record at `92dc6bb`:**
- **P0 is centrally symmetric as a path law.** F_{P0,N} =d −F_{P0,N} jointly over all
  times. The reason: the Gibbs law and the unforced flow are invariant under
  (x, p) ↦ (−x, −p), and the summands are i.i.d. (`BRI1_ANALYTIC_ESCAPE_THEOREM.md`
  T3). The law has mean 0.
- **P1 is skewed at t*.** For t* ∈ (0, δ) and every N_B ≥ N₀(t*),
  κ₃(F_{P1,N}(t*)) = K_{P1}(t*,t*,t*)/N_B + O(N_B⁻²) ≠ 0 (T1–T2 there).

**(C1) Path level: exact non-factorization (qualitative).**
- **Setting.** Let V be any real vector space of force paths carrying the X1 laws, for
  example C[0, 2π]. Let t_a(y) = M_a + K_a·y, where each K_a : V → V is linear and
  bimeasurable-bijective. This covers every linear interface: time-varying or not,
  causal or not, with any memory, calibrated or not. C2-F's filters are an instance.
- **Claim.** Then there is no law P★ with P0 = t_0#P★ and P1 = t_1#P★, for any
  N_B ≥ N₀(t*).

*Proof.*
- **Step 1.** P1 = (t_1∘t_0⁻¹)#P0 = c + K·F, with F ~ P0 and K linear.
- **Step 2.** Since F =d −F, we get K·F =d −K·F. So the time-t* coordinate
  ℓ(F) := (K·F)(t*) is a symmetric real random variable. ℓ is linear, so no continuity
  is needed.
- **Step 3.** Its law is the law of F_{P1,N}(t*) − c(t*). That law has a finite third
  moment and κ₃ ≠ 0. A symmetric law with a finite third moment has κ₃ = 0.
  Contradiction. ∎

**Remarks on (C1), with v3.1 corrections from workflow verification.**
- **Measurability, not continuity.** Step 2 needs ℓ to be measurable, not continuous.
  For a finite-dimensional record it is automatic, via a left inverse.
- **First-kind Volterra filters are not bijections of C[0, 2π].** For example,
  (Ky)(t) = ∫₀ᵗ τ⁻¹e^(−(t−s)/τ)y(s)ds maps onto {g ∈ C¹ : g(0) = 0}.
  - "C2-F's filters are an instance" holds for the discretized, unit-diagonal
    lower-triangular filters actually run (`R1/c2_controls.py`). Those are bijective on
    ℝ⁶⁴.
  - For continuous-time first-kind filters, replace "bijective" with "injective, with a
    measurable inverse on the range".
- **Strengthening: only the reference interface must be injective.**
  - Suppose t₀ is injective with a measurable inverse on its range. Then for **any**
    measurable affine t₁, every t_a#P★ is centrally symmetric whenever P0 is. In finite
    dimensions the sharp condition is ker K₀ ⊆ ker K_a.
  - This is a strengthening of the theorem, **not** a licence to weaken the commitment:
    ε_R is reference-free, and Theorem A's quotient form needs T to be a group. T_R1
    keeps every K_a invertible.
- **Why C2-F differs.** C2-F is absorbed because its protocols are linear images of one
  *skewed* law. BRI1 is not absorbed because its reference law is exactly *symmetric*,
  and the driven law has acquired an odd cumulant.
- **Where the odd cumulant comes from.** Only the bath nonlinearity creates it. With a
  harmonic bath, F_{P1} = F_{P0} + a deterministic shift, which lies in E₂±.
- **What remains open.** The quantitative path-level version needs a d_op on path space
  and is OPEN. Grid-level witnesses are valid lower bounds only for classes that act on
  the observed grid. That is the C2-F lesson: a filter that mixes in unobserved history
  is not a grid map.

**(C2) Grid level: quantitative.**
- **Setting.** Take any grid containing t* on which Cov F_{P1,N} is nonsingular (always
  true for k = 1). Let N_B ≥ N₀(t*).
- **Claim.** ε_R^T(X1) > 0 for T ∈ {E₂±, T_caus, T_lin}. Quantitatively, since
  β₁(P0) = 0 exactly:

  ε_R^lin(X1) ≥ √β₁(P1) / (2Λ) ≥ |κ₃(F_{P1,N}(t*))| / (2Λ·λ_max(Σ_{P1})^(3/2)) > 0.

  The lower bound inherits BRI1's rate: numerator |K_{P1}(t*,t*,t*)|/N_B + O(N_B⁻²).
  - **T_caus case.** Positivity follows through the zero set, since T_caus ⊂ T_lin. A
    T_caus bound with explicit constants comes from (B1) when t* is the first grid
    time.

*Proof.* Apply (B2) and the entry bound. ∎

**Not shown:**
- that Λ stays bounded as N_B → ∞ on grids with k ≥ 2. For k = 1, Λ → 3(E|N(0,1)|³)^(2/3)
  ≈ 4.10, as in v1;
- the matching upper bound;
- the reservoir limit.

## 5. Per-time nonlinear interfaces, and the trivial top of the ladder

**T_mono.** T_mono := {y ↦ (φ₁(y₁), …, φ_k(y_k))}, where each φ_i is a strictly monotone
continuous bijection of ℝ. It is a group, and E₂± ⊂ T_mono.

- **Standing assumption:** the marginal CDFs F_i are continuous and strictly increasing.
  BRI1's force marginals qualify: they have everywhere-positive densities, because the
  time-t map is a diffeomorphism and ρ > 0.
- **Canonical form:** the normal scores N_i = Φ⁻¹(F_i(Y_i)). The residual group is the
  signs, because a decreasing φ_i flips N_i.
- Theorem A holds verbatim with d_op^mono := W₃ between normal-score laws.

**(D1) A single time is absorbed.**
- At k = 1 every normal-score law is N(0,1), so ε_R^mono ≡ 0.
- In particular X1 at t* is absorbed. The map F_{P1(t*)}⁻¹ ∘ F_{P0(t*)} carries P0(t*) to
  P1(t*).
- **BRI1's single-time witness does not survive per-time nonlinear interfaces.**

**(D2) The multi-time invariant.**
- **Invariance.** Central symmetry of the normal-score law (N =d −N) is T_mono-invariant,
  because sign flips commute with −I.
- **P0 has it.** If Y − μ =d μ − Y with continuous marginals, then
  N_i(μ + v) = −N_i(μ − v).
- **Consequence.** X1 escapes T_mono on a grid **if** P1's normal-score law on that grid
  is not centrally symmetric. Then ε_R^mono > 0, by Theorem A(i) applied to T_mono:
  every element of P0's orbit has a symmetric normal-score law.
- **This is sufficient, not necessary.** In general, escape holds if and only if the two
  normal-score laws differ up to signs. A symmetric difference also counts, for example
  in the normal-score correlations.

**(D3) Normal-score witness inequality.** Let m := ‖N(0,1)‖₃ = (2√(2/π))^(1/3). For any
indices (a, b, c) that are not all equal (for example E N_i²N_j or E N_iN_jN_l):

| |E_P N_aN_bN_c| − |E_Q N_aN_bN_c| | ≤ 3m²·d_q^mono(P, Q), with 3m² ≈ 4.10.

**Hence ε_R^mono(X1) ≥ max | E_{P1} N_aN_bN_c | / (6m²).**

*Proof.*
- Telescope A_aA_bA_c − B_aB_bB_c as in (B2).
- Each coordinate difference satisfies ‖A_i − B_i‖₃ ≤ W₃.
- Every marginal is exactly N(0,1), so every ‖·‖₃ factor is m.
- A sign flip changes only the sign of each co-moment. ∎

**(D4) Leading-order criteria (formal; NOT proved).** Two channels, each O(1/N_B).

**Odd channel (asymmetry; uses the archived K).**
- **Ingredients.** Let K̃ := K_{P1}/m₂^(3/2), since the free variance is m₂ at every time
  by stationarity. Let ρ_ab be the free (P0) autocorrelation E[x₀(t_a)x₀(t_b)]/m₂.
- **Formal expansion.** A first-order Cornish–Fisher normalization,
  N = Y − (γ/6)(Y² − 1) + …, gives

  E_{P1}[N_aN_bN_c] = A_abc/N_B + O(N_B⁻²),

  A_abc = K̃_abc − (1/3)·[K̃_aaa·ρ_ab·ρ_ac + K̃_bbb·ρ_ba·ρ_bc + K̃_ccc·ρ_ca·ρ_cb].
- **Contributions that drop out.**
  - Fourth-cumulant terms are odd-degree Gaussian moments, so they vanish at this
    order.
  - Correlation corrections enter at O(N_B⁻²).
- **Identities.**
  - A_aaa ≡ 0.
  - A ≡ 0 whenever the non-Gaussianity is purely marginal, that is,
    K̃_abc = 2Σ c_m·ρρ with K̃_mmm = 6c_m.
**Even channel (correlation; not in the archive).**
- **Why it is O(1/N_B).** Cov F = Cov X^ε exactly, and the covariance is even in ε,
  because x₀ is odd and y₁ is even in z₀. So

  Cov F_{P1} = Cov x₀ + C2/N_B + O(N_B⁻²), with
  C2_ab = Cov(y₁(t_a), y₁(t_b)) + ½·[Cov(x₀(t_a), y₂(t_b)) + Cov(y₂(t_a), x₀(t_b))],

  where y₂ := ∂²_ε X^ε|₀ solves ÿ₂ + (1 + 3x₀²)y₂ = −6x₀y₁², with y₂(0) = ẏ₂(0) = 0.
- **The witness.** Formally, the normal-score correlations then differ from P0's by

  Δρ_ab/N_B, with Δρ_ab = [C2_ab − ½ρ_ab(C2_aa + C2_bb)]/m₂.

  Marginal γ and κ₄ corrections enter at O(N_B⁻²).
- **What this channel is.** It is also a v1 Prop. 2b witness under E₂±. BRI1 did not use
  it. A harmonic bath has C2 ≡ 0.
- **Under T_lin it is absorbed,** because whitening removes it. That is why it appears
  only on the T_mono side of the lattice.

**Common to both channels.**
- **Missing proof.** Turning either channel into a theorem needs a multi-time Edgeworth
  expansion, with remainder, for the normalized bath sums. BRI1-R1 gives moment bounds,
  not an Edgeworth bound. That proof obligation is Claude Code's.
- **Data.** The archived frozen-τ K tensor (10 components each for P1 and P2, at
  τ = (π, 3π/2, 2π); grade: strong numerical evidence, NOT certified) gives the odd
  channel, except for ρ at τ. The even channel needs C2, a new second-order response
  computation in the PF4Q machinery. Both are computations: **WO-002**.

**The join is expected to trivialize (not proved).** The group generated by T_lin and
T_mono consists of compositions of linear mixing and per-time nonlinearities: the
normalizing-flow / neural-network class. Universal-approximation results suggest its
orbit closures are large enough to make ε_R ≡ 0. So a commitment can take one side of
the lattice, not both.

**(E) Unrestricted interfaces trivialize R1.**
- **Claim.** If T contains every bimeasurable bijection (per protocol), then any family
  of atomless laws lies in one T-orbit, exactly (see the source below). So ε_R ≡ 0 for
  every d_op that vanishes on equal laws.
- **Source.** The isomorphism theorem for measures (Kechris, *Classical Descriptive Set
  Theory*, GTM 156, 1995, Thm 17.41).
  - Every continuous (atomless) Borel probability measure on a standard Borel space is
    carried to Lebesgue measure on [0, 1] by a Borel isomorphism.
  - So the isomorphism is **exact**, not merely "mod null sets". Number and statement
    were confirmed by the workflow literature check.
- **Atomlessness is essential.** Under Borel bijections, the multiset of atom masses is
  an orbit invariant.
- **If non-injective Borel maps are allowed,** every family is absorbed: every Borel
  probability on a standard Borel space is a Borel image of Lebesgue measure.
- **Consequence.** That is R1's kill condition "trivial". "Maximal" in STATE.md cannot
  mean unrestricted, which is consistent with "no unrestricted per-protocol maps".

## 6. Consequences

**BRI1 X1 (P0 vs P1) on the ladder:**

| T | Effect on X1 | Status |
|---|---|---|
| E₂± | escapes; ε_R ≥ O(1/N_B) | DERIVED (BRI1; v1 Cor. 4) |
| T_caus, T_lin (grid) | escapes; ε_R ≥ O(1/N_B) via Mardia | DERIVED (C2) |
| any linear interface on paths (C2-F's filters included) | no exact factorization | DERIVED (C1); quantitative version OPEN |
| T_mono, single time | absorbed; ε_R = 0 | DERIVED (D1) |
| T_mono, k ≥ 2 times | escapes if, at leading order, some A_abc ≠ 0 (odd channel) or some Δρ_ab ≠ 0 (even channel) | OPEN → WO-002 (numbers), plus the D4 proof obligation |
| join of T_lin and T_mono | expected to trivialize | expectation only; not proved |
| unrestricted | everything absorbed; R1 trivial | DERIVED (E) |

**Consistency with the controls.**
- C2-G, C2-NG and C2-F are each one orbit of path-level linear interfaces, so they give 0
  under T_lin when the observed grid contains the filter support. That is how VS Code's
  exact deconvolution ran.
- (L4) in the check script shows the C2-F mechanism directly: the single-time skewness
  differs (2.32 vs 1.35) while √β₁ is identical to about 10⁻¹⁴.

**Kill-condition flag (for D5).** Under T_lin, ε_R > 0 fires on any protocol-dependent
non-Gaussianity that is not a linear image, including an exogenous environment read
through an uncalibrated nonlinear detector (the C3 controls).
- So ε_R's power to discriminate back-reaction rests entirely on the interface being
  *independently calibrated*.
- Whether ε_R^lin reduces to a known non-Gaussianity or nonlinear-response test is
  exactly the "reduces to generic nonlinear response" kill condition. D5 must address
  it.

**[Superseded by §0: T frozen by rulings G2-01 … G2-06; kept as the record of the
recommendation.]** **Owner decision needed: freeze T for R1.** T is not derivable; it
is a COMMITMENT priced in L₀ plus vocabulary.

- **Recommended:**

  **T_R1 := protocol-dependent linear interfaces on force-path space,
  y ↦ M_a + K_a·y.**

  - Evaluate it with T_lin on the observed grid, with the grid containing the
    interface's support.
  - Any interface nonlinearity that is independently calibrated is removed with its
    known map **before** the inf, not fitted inside it.
- **Price.** Linear structure on the readout space (one vocabulary item), plus the
  calibration protocol.
- **Why this class:**
  - it contains every exogenous control built so far;
  - it is the largest linear class, and BRI1 provably still escapes it;
  - the other side of the lattice (T_mono) already trivializes single-time data;
  - the join of the two sides is expected to trivialize everything.
- **The alternative:** T_mono, which bets on D4 coming back nonzero in either channel.
  That decision should wait until WO-002 reports.

## 7. Deliverable status (supersedes v1 §3 where they differ)

| Deliverable | Status |
|---|---|
| D1 — ε_R = 0 on exogenous processes factoring through T | **DERIVED for every grid-level class on the ladder** (Theorem A(i)). Path-level linear filters: zero when the grid contains the filter support; a path-space d_op is OPEN. |
| D2 — BRI1 as a special case | **Lower bounds DERIVED for E₂±, T_caus and T_lin** (v1 Cor. 4; C2). Path-level linear non-factorization DERIVED (C1). Per-time nonlinear interfaces: single time absorbed (D1); multi-time OPEN (D4, two channels, WO-002). Rate, upper bound and reservoir limit OPEN. |
| D3 — invariance and coarse-graining | As in v1 for **E₂±**. Zero sets are monotone along the ladder. **Correction (v3.1):** monotonicity under time-marginalization **fails for T_lin**: a swap counterexample takes ε_R from 0 on {1, 2} to ≥ 0.0518 on {1}. It also fails for T_caus on non-initial subgrids. It holds for E₂±, and for T_caus on initial segments, under both W₃ and BL. |
| D4 — finite-data identifiability | **OPEN.** Review 2 flag: BRI1's witness at these parameters needs about 10¹¹ samples. |
| D5 — comparator audit | Not started. Kill-condition flag above. |

---

## 8. The frozen distance: bounded-Lipschitz quotient (v3)

**Theorem A-BL.** Assume every P_a has a finite, nonsingular covariance. Then:
- the minimum over O(k) in d_q^BL is attained;
- d_q^BL is a pseudometric;
- d_q^BL(P, Q) = 0 if and only if P ∈ T_R1#Q;
- inf over t ∈ T_R1 of d_BL(P̃, (t#Q)~) = d_q^BL(P, Q).

Moreover:
- **(i)** ε_R = 0 if and only if all the P_a lie in one T_R1-orbit;
- **(ii)** ½·diam ≤ ε_R ≤ diam.

*Proof.*
- **Isometries.** Rotations and the negation R: y ↦ −y are Euclidean isometries. Since
  f∘O has the same sup-norm and Lipschitz constant as f, we get
  d_BL(O#P, O#Q) = d_BL(P, Q).
- **Metric.** d_BL is a metric on Borel probability measures on ℝ^k (Dudley, *Real
  Analysis and Probability*, ch. 11; primary-text check in CHECKS).
- **Continuity.** |d_BL(P̃, O#Q̃) − d_BL(P̃, O′#Q̃)| ≤ d_BL(O#Q̃, O′#Q̃)
  ≤ E|(O − O′)W| ≤ ‖O − O′‖·E|W|, using d_BL ≤ W₁. With O(k) compact, the minimum is
  attained.
- **The rest.** The equivariance lemma (§1, T_lin row) and the proof of Theorem A
  apply verbatim. ∎

**Theorem F (symmetric-orbit witness bound; constants derived, not hard-coded).**
Let 𝒮 be the set of laws on ℝ^k that are centrally symmetric about 0, and R = −id.

- **(F1) Distance to the symmetric laws: constant 1, and sharp.** For every law P on
  ℝ^k:

  dist_BL(P, 𝒮) = ½·d_BL(P, R#P) = sup over odd f with ‖f‖_BL ≤ 1 of |E_P f|.

  Hence |E_P f| / ‖f‖_BL ≤ dist_BL(P, 𝒮) for every odd bounded-Lipschitz f.

  *Proof.*
  - **(≥)** For S ∈ 𝒮: d_BL(P, R#P) ≤ d_BL(P, S) + d_BL(S, R#P)
    = d_BL(P, S) + d_BL(R#S, R#P) = 2·d_BL(P, S).
  - **(≤)** S₀ := ½P + ½R#P lies in 𝒮. Since d_BL(μ, ν) is a **seminorm of the signed
    measure** μ − ν, and P − S₀ = ½(P − R#P), we get d_BL(P, S₀) = ½·d_BL(P, R#P).
    *(v3.1 correction: the earlier justification "d_BL is affine in each argument" is
    false. Counterexample: P = ½δ₁ + ½δ₋₁ with Q₁ = δ₁, Q₂ = δ₋₁.)*
  - **The sup over odd f.** For any admissible f, E_P f − E_{R#P} f = 2·E_P f_odd, with
    f_odd(y) = (f(y) − f(−y))/2. Moreover ‖f_odd‖_∞ ≤ ‖f‖_∞ and
    Lip(f_odd) ≤ Lip(f). So d_BL(P, R#P) = 2·sup over odd admissible f of |E_P f|. ∎

- **(F2) Two protocols: ε_R is exactly half the quotient distance.** For {P0, P1}:

  ε_R = ½·d_q^BL(P0, P1).

  *Proof.*
  - **(≥)** Theorem A-BL (ii).
  - **(≤)** Let O be optimal and Q := ½·Law(P̃1) + ½·Law(O·W̃0). Both components have
    mean 0 and covariance I, so Q has mean 0 and covariance I, and Q̃ = Q.
  - Then P̃1 − Q = ½(P̃1 − O#P̃0) and O#P̃0 − Q = −½(P̃1 − O#P̃0). By the seminorm
    property, both distances equal ½·d_BL(P̃1, O#P̃0).
  - The lower bound needs only central symmetry of P0. The exactness of (F2) needs both
    covariances nonsingular. ∎

- **(F3) The witness-to-bound theorem.** Let P0 be centrally symmetric about its mean,
  and take any P1.
  - Every member of P0's T_R1-orbit, after centering and whitening, lies in 𝒮. Centering,
    whitening and rotation all commute with R.
  - So d_q^BL(P0, P1) ≥ dist_BL(P̃1, 𝒮). By (F1) and (F2):

  **ε_R^(T_R1)({P0, P1}) ≥ ½·dist_BL(P̃1, 𝒮) = ¼·d_BL(P̃1, R#P̃1)
  ≥ ½·|E_{P1} f(P̃1)| / ‖f‖_BL, for every odd bounded-Lipschitz f.**

  - **The two constants.** The constant is **1** for the distance from the driven law to
    the symmetric null orbit (G2-03). It is **½** for ε_R (G2-04), and that ½ is exact
    for two protocols by (F2).
  - **For more protocols.** With any protocol set containing a symmetric P0, the same
    bound holds through Theorem A-BL (ii).
  - **Why no invariance is needed.** The witness f need not be rotation-invariant: the
    bound uses the symmetry of the whole null orbit.

- **(F4) Why the route fails under T_mono in raw coordinates, and where it survives.**
  - **It fails in raw coordinates.** Coordinatewise monotone maps do not commute with
    R.
    - Example: k = 1, Y ~ N(0,1), and φ(y) = y for y ≤ 0, φ(y) = 2y for y > 0. This φ
      is valid under both T_mono definitions: §5's bijections of ℝ, and §9's bijections
      between support intervals. **§9 governs.** e^Y is excluded under §5 but
      admissible under §9.
    - φ#N(0,1) has exact skewness 0.7595. So P0's T_mono-orbit is not contained in 𝒮.
    - The **conclusion** fails as well as the proof route, by D1.
  - **It survives in normal-score (copula) coordinates.** There the T_mono-orbit acts by
    coordinate sign flips, which commute with R. A centrally symmetric P0 has a
    radially symmetric copula (§9), so (F1)–(F3) apply verbatim with the normal-score
    vector N in place of P̃:

    ε_R^(mono,BL) ≥ ½·sup over odd g of |E g(N₁)| / ‖g‖_BL.

  - **At a single time,** N₁ ~ N(0,1) exactly, so this is 0. That is D1 again.
  - **Hypotheses.** Only "C₀ radially symmetric" is needed. (F2) holds verbatim for
    T_mono, because a mixture of laws with N(0,1) margins has N(0,1) margins.
  - **This is a sufficient condition only.** Exactly, it is positive if and only if C₁
    is radially asymmetric. A nonzero E[N_aN_bN_c] is sufficient for that but not
    necessary.
  - **Choose bounded-Lipschitz odd witnesses for k ≥ 2.**
    - tanh(c·n_a·n_b·n_c) is **not** globally Lipschitz.
    - Use products of bounded odd Lipschitz functions instead, e.g.
      g = tanh(n_a)·tanh(n_b)·tanh(n_c), with ‖g‖_∞ ≤ 1 and Lip ≤ √3.
    - In 1-D, tanh(c·H₃) is fine.
  - **"Rotations" means all of O(k), reflections included.** Under SO(k) at k = 1 the
    quotient would not absorb y ↦ −y, which is in T_lin.

**Prop. G (BRI1: rate of a bounded odd surrogate)** — see §8.1 below.

### 8.1 Prop. G — BRI1 rate of a bounded odd surrogate (G2-02 item 4, second part) — DERIVED

**Setting.**
- Fix t* ∈ (0, δ), with δ from BRI1 T1. Take any observed grid containing t* on which
  Cov F_{P1} is nonsingular (always true for k = 1).
- Let f be odd and bounded with f″ Lipschitz. For example f_c = tanh(c·H₃) for any
  c > 0, with H₃(z) = z³ − 3z, or a C^{2,1} mollification of any bounded-Lipschitz odd
  function.

**Claims.**
- **(G1)** E_{P1} f(W₁(t*)) = (γ₁(P1)/6)·E_φ[f H₃] + O(N_B^(−3/2)), where:
  - W₁(t*) is the standardized force at t*;
  - γ₁(P1) = K/(N_B m₂^(3/2)) + O(N_B⁻²);
  - K = K_{P1}(t*, t*, t*) < 0, by BRI1 T1.
- **(G2)** Hence there is N₁(t*, f) such that for every N_B ≥ N₁:

  **ε_R^(T_R1)({P0, P1}) ≥ |K|·E_φ[f H₃] / (24·m₂^(3/2)·‖f‖_BL·N_B).**

  N₁ is a new threshold, distinct from BRI1's N₀.
  - Equivalently, liminf N_B·ε_R ≥ |K|·E_φ[f H₃] / (12·m₂^(3/2)·‖f‖_BL).
  - Taking the sup over smooth odd f: **liminf N_B·ε_R ≥ |K|·V*/(12·m₂^(3/2)),
    with V* = 0.943578.**
  - V* is the LP optimum of sup{E_φ[f H₃] : f odd, ‖f‖_∞ ≤ 1, Lip f ≤ 1}. Its
    closed-form optimizer is piecewise linear with kink a = 1.0653381390. Mollifying by
    an even kernel keeps f odd and both norms, so the sup over smooth f equals V*.
  - For the tanh family, the best c is c* ≈ 0.1442, with
    E_φ[f H₃]/‖f‖_BL = 0.4185.
- **(G3)** The bound transfers to **any** grid containing t*, with no loss of constant.
  Take f(w) = g(v·w), with v = Σ^(1/2)e_{t*}/√Σ_{t*t*} and |v| = 1. Then v·W₁ is exactly
  the standardized F(t*), and Lip f = Lip g.

**Quantifiers.** ∃δ (BRI1), ∀t* ∈ (0, δ), ∃N₁(t*, f), ∀N_B ≥ N₁. No numerical value of
δ, N₀ or N₁ is claimed. The sign of C = K·E_φ[f H₃]/(6m₂^(3/2)) is negative in BRI1's
convention, F = +ε·Σ_j X_j.

*Proof.*
- **(i) Smooth-function expansion without Cramér's condition.**
  - **Source.** Barbour, *Asymptotic expansions based on smooth functions in the central
    limit theorem*, PTRF 72 (1986) 289–303: the Theorem, eq. (8), p. 294, case (i) with
    k = 4, α = 1, p = 0. The primary text was read from page images during workflow
    verification.
  - **Statement.** For independent mean-zero summands with Σ E X_i² = 1 and h ∈ C²
    with h″ Lipschitz:

    E h(W) = E h(N) + (κ₃/6)·E[H₃h] + (κ₄/24)·E[H₄h] + (κ₃²/72)·E[H₆h] + η,
    with |η| ≤ C·L(h″)·Σ E|X_i|⁵,

    where C is universal but not explicit.
  - **For odd h,** E h(N) = E[H₄h] = E[H₆h] = 0.
  - **A self-contained alternative** with explicit constants is the Lindeberg "Lemma A"
    (f ∈ C⁷ or C⁹) in the workflow record (CHECKS). Barbour is the load-bearing citation.
- **(ii) Uniformity over BRI1's triangular array.**
  - Set X_j = (X_j^ε − μ_ε)/(σ_ε √N_B), so Σ E|X_j|⁵ = N_B^(−3/2)·β₅(ε). Here β₅(ε) is
    the fifth absolute moment of X^ε(t*) − μ_ε divided by σ_ε⁵, and it is bounded
    uniformly in ε ∈ [0, 1]:
  - **Numerator.** |X^ε(t*)|⁵ ≤ 2^(5/2)(√E₀ + √2·Q·π)^(5/2), by BRI1-R1(i)'s energy
    estimate, and this is Gibbs-integrable.
  - **Denominator.** σ_ε² > 0 for every ε ∈ [0, 1] by T3's density argument (the
    time-t* map is a C¹ diffeomorphism), and ε ↦ σ_ε² is continuous. So
    σ_min² := min over [0, 1] of σ_ε² > 0.
- **(iii) The skewness.**
  - κ₃(F) = N_B^(−1/2)·κ₃(X^ε) = K/N_B + O(N_B⁻²), by BRI1-R1(iv).
  - Var F = Var X^ε = m₂ + O(ε²): σ²(ε) is even in ε by parity, C² by BRI1-R1(iii), and
    σ²(0) = m₂ by stationarity.
  - So γ₁ = κ₃(W₁) = K/(N_B m₂^(3/2)) + O(N_B⁻²).
- **(iv) Positivity.** E_φ[f_c H₃] > 0, because x·tanh(cx) ≥ 0, with strict inequality
  on a set of positive measure.
- **(v) Combine.** Apply Theorem F (F3): ε_R ≥ |E f|/(2‖f‖_BL). For N_B ≥ N₁ the
  remainder is at most half the main term. ∎

**Checks (evidence only).**
- An exact lattice triangular array, where Cramér's condition fails, confirms
  N·E f(W) → (N·γ₁/6)·E_φ[f H₃] with remainder × N^(3/2) bounded.
- WO-001 C1's N_B·γ₁ matches BRI1's symbolic series to its truncation error.

**Not covered.**
- **k ≥ 2 copula coordinates (M5).** Normal scores are law-dependent nonlinear
  transforms, so neither Barbour nor Lemma A applies. M5 stays OPEN.
- **An O(N_B⁻²) refinement.** It would need Barbour's k = 5 case and a 5-factor
  extension of BRI1-R1(iii). Not claimed.

## 9. Coordinatewise monotone interfaces: the copula theorem (WO-002 freeze, ruling G2-07)

**Scope.**
- **Interface class.** T_mono consists of coordinatewise, strictly monotone (increasing
  or decreasing) continuous bijections of the margins' support intervals, on the finite
  observed time grid.
- **Laws.** Margins are continuous and atomless, each supported on an interval with a
  CDF strictly increasing there. P★ ranges over the same class.
- **Reflections.** ℛ := {R_S : S ⊆ {1, …, k}}, where R_S reflects u_i ↦ 1 − u_i for
  i ∈ S. In normal-score coordinates N = Φ⁻¹(U), R_S is the sign flip of the
  coordinates in S.
- **Distance.** d_op^mono := d_BL between normal-score laws, minimized over ℛ.

**The hierarchy (stated so the layers are not confused).**
- **Exact:** M1, the quotient, and M2, the symmetry certificate.
- **Perturbative diagnostic:** M3, the Gaussian tangent structure.
- The count C(k+2, 3) − k belongs **only** to M3.

**M1 — Exact quotient (the whole intervention family).**
- **Claim.** ε_R^(T_mono) = 0 if and only if all the protocols' copulas lie in one
  ℛ-orbit.
- **Corollary.** The ℛ-orbit class of the copula is the exact maximal invariant of
  T_mono on the grid.

*Proof.*
- **Copula uniqueness (Sklar).** With continuous margins the copula C_P is unique, and
  N_P := Φ⁻¹(F(Y)) has law Φ⁻¹#C_P.
- **Forward: maps move copulas by reflections.**
  - If φ_i is increasing, F′_i ∘ φ_i = F_i. If it is decreasing, F′_i ∘ φ_i = 1 − F_i.
  - So for t ∈ T_mono, C_{t#Q} = R_S#C_Q, where S is the set of decreasing coordinates.
- **Converse: quantile maps.** If C_P = R_S#C_Q, define φ_i := F_{P,i}⁻¹ ∘ F_{Q,i}
  (i ∉ S) or F_{P,i}⁻¹ ∘ (1 − F_{Q,i}) (i ∈ S).
  - Each is a strictly monotone continuous bijection between the support intervals,
    because the CDFs are continuous and strictly increasing there.
  - t#Q has the margins of P and copula R_S#C_Q = C_P, so t#Q = P (Sklar).
- **Attainment versus closure.** ε_R is an infimum, so "= 0" has to be pinned down.
  - Suppose ε_R = 0. For every δ > 0 there is a P★ with d_op^mono(P_a, P★) < δ for all
    a. By the triangle inequality, d_op^mono(P_a, P_b) < 2δ for all a, b.
  - So d_op^mono(P_a, P_b) = 0. The minimum over the **finite** group ℛ is attained, and
    d_BL is a metric. Hence N_{P_a} =d R_S·N_{P_b} for some S, and C_{P_a} = R_S#C_{P_b}.
  - ℛ-orbits are closed: they are finite sets. So the closure reading ("C_a lies in the
    closure of Orb_ℛ(C_b)") and the exact reading coincide.
  - "One orbit" is transitive because ℛ is a group. So all copulas lie in one orbit.
  - Conversely, if they do, take P★ := P_{a₀}. By the quantile construction every
    d_op^mono(P_a, P★) = 0. ∎

**M2 — Symmetry certificate.**
- **Claim.** If C₀ is radially symmetric (U =d 1 − U) and C₁ is radially asymmetric,
  then ε_R^(T_mono) > 0. Quantitatively, ε_R^(mono,BL) ≥ ½·sup over odd g of
  |E g(N₁)| / ‖g‖_BL (F4).
- **When C₀ is radially symmetric.** Whenever P0 is centrally symmetric with continuous
  margins: F_i(μ_i + v) = 1 − F_i(μ_i − v), so U(Y) = 1 − U(2μ − Y), and
  2μ − Y =d Y.

*Proof.*
- Radial symmetry is ℛ-invariant: 1 − R_S U = R_S(1 − U) =d R_S U.
- So every member of Orb_ℛ(C₀) is radially symmetric, C₁ ∉ Orb_ℛ(C₀), and M1 applies. ∎

**M3 — Gaussian tangent structure (leading-order diagnostic; subordinate to M1).**
- **Setting.** Let X ~ N(0, C) and perturb one coordinate:
  Y_i = X_i + a·δ_im·g(X_m).
- **Regularity.** g ∈ C² with sup|g′| < ∞, so that x + a·g(x) is strictly monotone for
  |a| < 1/sup|g′|. Also g, g′, g″ of polynomial growth, which is the integrability the
  Gaussian identity needs.
- **The identity.** By Gaussian integration by parts (Stein/Price),
  E[g(X_m)X_jX_ℓ] = C_jℓ·E g + C_jm·C_ℓm·E g″. Hence

  ∂_a κ(Y_i, Y_j, Y_ℓ)|₀ = E[g″(X_m)]·[δ_im C_jm C_ℓm + δ_jm C_im C_ℓm + δ_ℓm C_im C_jm]
  =: α_m·T^(m)_ijℓ.

- **Consequences.**
  - Each coordinate contributes one scalar, α_m = E g″(X_m). Odd g give α_m = 0.
  - T^(m)_mmm = 3C_mm², and T^(n)_mmm = 0 for n ≠ m.
  - So if C_mm > 0 for every retained coordinate, the diagonal block of J is
    diag(3C_mm²): **rank J = k**.
  - The surviving leading-order third-order directions number **C(k+2, 3) − k**: zero at
    k = 1 (D1) and two at k = 2.
- **Realizability.** Every direction is realized inside the regularity class. A smoothly
  truncated quadratic, equal to x² − 1 on [−L, L] with bounded g′, has α_m → 2 as
  L → ∞.
- **Correction to the wording "x → x + a(x² − 1)".** That wording appears in G2-04
  and in Claude Code's reply of the same day. The untruncated x + a(x² − 1) is **not**
  globally monotone for any a ≠ 0: its derivative vanishes at x = −1/(2a). It is a
  formal tangent direction only.
- **In copula coordinates.**
  - E N_m³ = 0 identically, and the C(k+2, 3) − k off-diagonal moments E[N_aN_bN_c]
    remain.
  - At formal Edgeworth order these equal A_abc/N_B (D4). A_abc is the third-cumulant
    tensor projected off span{T^(m)}.

**Witnesses modulo reflections.**
- **Odd sector.** Radial asymmetry (M2). The null orbit's odd normal-score moments are
  identically 0, so any nonzero one is reflection-safe.
- **Even sector.**
  - Use only ℛ-invariant copula functionals: |ρ^N_ab| and the triple products
    ρ^N_ab·ρ^N_bc·ρ^N_ca, where ρ^N is the correlation of the **normal scores**.
  - Not Pearson correlation of the raw force, which monotone maps change. Not signed
    Δρ, which a partial reflection flips.
  - At formal order 1/N_B, the change in normal-score correlation equals the Pearson
    change Δρ_ab/N_B computed from C2. Marginal corrections enter at O(N_B⁻²).
  - |ρ^N_ab| then changes by sign(ρ⁰_ab)·Δρ_ab/N_B when ρ⁰_ab ≠ 0.
- **Bounded even witness (v3.1).** ρ^N is an unbounded moment, so it does not directly
  lower-bound d_BL; the reflection route of F4 sees only odd asymmetry.
  - Take g_ab(n) := tanh(n_a)·tanh(n_b). Then ‖g_ab‖_∞ ≤ 1 and Lip ≤ √2.
  - Every R_S ∈ ℛ multiplies g_ab by ±1, so |E g_ab| is ℛ-invariant.
  - Hence | |E_P g| − |E_Q g| | ≤ |E_P g − E_{R_S Q} g| ≤ ‖g‖_BL·d_BL(N_P, R_S N_Q) for
    every S. Minimizing over S, and using Theorem A-BL (ii):

    **ε_R^(mono) ≥ max_ab | |E_{P1} g_ab(N)| − |E_{P0} g_ab(N)| | / (2‖g_ab‖_BL).**

  - At formal leading order, E g_ab(N) moves by (∂/∂ρ)E_ρ[tanh(Z_a)tanh(Z_b)]·Δρ_ab/N_B.
    That derivative is nonzero for |ρ| < 1.

**M4 — BRI1 computation and preregistered outcomes (fixed before the numbers are read).**
- **The question.** Does BRI1's intervention family move to a different copula
  reflection-orbit? What is the N_B scaling of the first detectable invariant?
- **What is computed** (`PROGRAM/RESULTS/WO-002/`):
  - the odd coordinates A_abc;
  - the even coordinates Δρ_ab;
  - each at formal leading order, with N_B·(cumulant-level coordinate) at
    N_B ∈ {4, …, 128}.

**Preregistered outcomes.**
1. **Some leading-order surviving component is nonzero** beyond 10² × its quadrature
   spread → **escape at leading order**, via M2 for the odd sector or M1 for the even
   sector. Grade: numerical evidence, not certified (PF4Q grade).
2. **All leading-order components are zero** → compute the **exact** copula radial
   asymmetry from finite-N_B dynamics (normal scores) **before any verdict**. A zero
   perturbative witness is **not** a kill.
3. **The copulas lie exactly in one reflection orbit** → this reciprocity branch is
   **KILLED**.

**M5 — Theorem grade for BRI1: OPEN** (a proof obligation for Claude Code).
- **What it needs.** An expansion E g(N₁) = (linear functional of A)/N_B + o(1/N_B), for
  a bounded odd g in normal-score coordinates, in BRI1's triangular array.
- **The route.** A Cramér-condition Edgeworth expansion: X^ε has a density, and the
  Cramér bound must be shown uniform in ε.
- **Until then.** Outcome 1 is evidence-grade only.

**Caveats (G2-03).**
- Discrete variables need generalized copulas, which are not unique.
- Non-strict maps destroy information.
- Path-dependent nonlinear filters are outside T_mono and outside this argument.

## 10. Common carrier, mode selection, and the top of the ladder

**(Carrier) Theorem C under the common carrier.**
- **Setting.** If Y_a = t_a(h(Z)) with one h, set W := h(Z). Then Y_a = t_a(W) with
  t_a ∈ T_R1.
- **Theorem C** (C1 path level, C2 grid level) then applies verbatim with P★ = Law(W).
  The latent space of Z may have any dimension.

**(E1) Linear interfaces from a latent space of unrestricted dimension (necessarily
non-injective) make R1 trivial** (G2-01 item 3a).
- **Construction.** Let Z = (Z_a)_{a∈A} have independent coordinates with Z_a ~ P_a, on
  (ℝ^k)^A. Let h_a := π_a, the projection onto copy a, which is linear. Then
  h_a#Law(Z) = P_a exactly, for every family.
  - No shifts, moments, independence or atomlessness are needed. The path-level and
    uncountable-A versions hold too.
- **Relation to E_univ.** On BRI0 §4's admissible domain (environment causality, i.e.
  non-anticipating families), the zero set of unrestricted linear-latent T coincides
  with grid-level E_univ.
  - Every such family even has a causal linear representation: 0/1 selections from a
    latent indexed by the protocols' prefix tree.
  - So "the E_univ ceiling reached linearly" holds in this strong form.
  - The plain product projections are causal only for prefix-separated protocols. That
    does not cover X1's P1 and P2, which agree on [0, π].
- **What blocks absorption.** Per-map conditions do **not** block it (full rank,
  surjectivity, nondegenerate output). A **cross-protocol** kernel condition does:
  equal kernels on the latent fluctuation span. Equivalently, the interfaces are
  injective after quotienting the common kernel. For Theorem C alone,
  ker K₀ ⊆ ker K_a suffices (§4 remarks).
- **The excess-dimension dichotomy.**
  - Theorem C is protected at excess 0, where excess := dim ker K₀ on the direction
    space of aff supp P★.
  - It breaks at excess 1, for every k with nondegenerate laws.
  - The excess needed to *absorb* a given family can be larger: k(|A| − 1) always
    suffices.

**(E2) The physical counterexample outside the commitment** (G2-01 item 3b; check L6).
- **Construction.** Take S symmetric with nonsingular Cov S, and U skewed, independent;
  the environment's law is protocol-independent. Protocol 0 reads S; protocol 1 reads
  S + U.
- **What "exogenous" requires physically.** U's law must not depend on the protocol.
  That needs a one-way (skew-product) or non-reciprocal readout of U, or the limit in
  which U's response vanishes. A reciprocal Hamiltonian coupling A(q)·U would drive U,
  and that is back-reaction.
- **Result.** The reference is exactly symmetric and the driven law is skewed (exact
  γ = 4/3^(3/2) ≈ 0.770 in L6), and there is no back-reaction.
- **What it shows.** The maps (1, 0) and (1, 1) from ℝ² to ℝ are linear but select
  modes. So E2 lies outside Theorem C's hypothesis; it does not contradict Theorem C. It
  is why the mode-stability certificate is mandatory.

**(E) The unrestricted ceiling** — as in §5 (Kechris Thm 17.41; exact Borel
isomorphism; atomless laws).

**North-star consequence (G2-02 item 6).** "Environment responds" is meaningful only
relative to a specified environmental identity across interventions. Operationally,
that identity is the common carrier; at the fundamental level, 𝒦 must generate it.

## 11. Deliverables and the exit gate (v3; supersedes §7 where they differ)

| Item | Status |
|---|---|
| T scope (exit i) | **FROZEN** (§0). The commitment is priced: linear readout structure + common carrier + calibration protocol. |
| d_op (exit iii) | **FROZEN**: BL quotient. Theorems A-BL and F are DERIVED (checked in `82d311e`; v3.1 justification fixes pending check). **Prop. G is DERIVED** (§8.1): liminf N_B·ε_R ≥ abs(K)·V*/(12 m₂^(3/2)), via Barbour 1986 with triangular-array uniformity proved. External check pending. |
| T_mono survival (exit ii) | Exact theorem (M1, M2) DERIVED. **WO-002 answer: YES**, outcome 1, escape at leading order, for P1 and P2 in both sectors (§11.1). Grade: numerical evidence at formal leading order. Theorem grade: OPEN (M5). |
| D5 (exit iv) | Not started. It must discriminate A / B / C, including mode selection. |
| D4 / C4 | OPEN; laboratory preparation; does not block Stage 3. |

### 11.1 WO-002 result (read after the boundary ruling G2-08 was on the remote)

`PROGRAM/RESULTS/WO-002/REPORT.md` is generated from `wo002_results.json` and
cross-checked by an independent implementation in `xcheck/`.

**Controls.** Every exact control passes on both primary trapezoid rules:
- A_aaa: 9×10⁻¹⁶ and 3×10⁻¹³;
- stationarity: 3×10⁻¹⁶ and 1×10⁻¹³;
- m₂ + m₄ − 1: −2×10⁻¹⁶ and 0;
- marginal-only control: 2×10⁻¹⁵;
- parity: 4×10⁻¹⁶;
- harmonic bath: 1×10⁻¹⁴;
- K against the archive: 3×10⁻¹⁶.

The archive's GH192 rule is weak, with a stationarity error of 1.2×10⁻⁶. It is
reported per rule and excluded from the spreads.

**Odd sector (radial asymmetry, M2).** All 7 off-diagonal A_abc are nonzero for P1
and for P2, at 2×10⁶ to 3×10⁸ times the quadrature spread. Examples:
- P1(π, 3π/2, 2π) = +0.37602;
- P2(π, 3π/2, 2π) = +0.56381.

**Even sector (M3 witnesses, read modulo ℛ).** All 3 Δρ_ab are nonzero, at 3×10⁶ to
3×10⁹ times the spread. Example: P2(π, 2π) = +0.96390.
- **Base correlations** on τ: ρ = −0.609, −0.154, −0.609. None is near 0, as the G2-08
  item 7 check requires. So reflections cannot absorb the change.

**N_B scaling.** The finite-N_B cumulant-level coordinates, times N_B, converge to the
leading-order values with O(1/N_B) corrections. For example, P1 A(π,π,3π/2):
−0.175, −0.202, −0.217, −0.225, −0.230, −0.232 → −0.2338. So the first detectable
copula invariants scale as **1/N_B**.

**Cross-check.** The independent implementation agrees to ≤ 2×10⁻¹⁴ on every A and Δρ.

**Preregistered reading, applied mechanically.**
- **P1:** ESCAPE-ODD and ESCAPE-EVEN.
- **P2:** ESCAPE-ODD and ESCAPE-EVEN.
- That is **outcome 1: escape at leading order**.

**Verdict under G2-08.**
- The carrier is PASS, and the protocol classes under Tier 2 (T_mono) are different at
  leading order.
- So: **Tier 2, readout-robust reciprocity: R1-PASS at evidence grade (formal leading
  order).** The theorem grade remains OPEN (M5).
- Finite-witness asymmetry: an escape on this finite grid is a process-level escape.

**Remaining to the R1 terminal.**
- (iii) The external check of the v3/v3.1 theorems (A-BL, F, M1–M3) and of Prop. G.
- (iv) D5, the comparator audit, including mode selection.
- M5 is the remaining proof obligation of rigour; Prop. G is now DERIVED (§8.1). M5 is
  not an exit-gate item unless the owner rules otherwise.
