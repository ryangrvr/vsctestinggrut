# R1 — THE INTERFACE LADDER (Claude Code) · v2 addendum to R1_DEFINITION · 2026-10-06

**Question (Review 2, open).** E₂± is not closed under independently calibrated linear
interface maps; C2-F showed this. Does BRI1's escape survive once T is enlarged?

**Answer.**
- **Against every linear interface class: yes, BRI1 still escapes.** This holds causal
  or not, calibrated or not, at the grid level and at the path level. The reason is
  structural: P0 is exactly sign-symmetric, and no linear map can create an odd
  cumulant (Theorem C).
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
√β₁(P) := ‖E W^⊗3‖_F (Mardia's multivariate skewness). Let μ_P := (E|W|³)^(1/3),
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

**Remarks on (C1).**
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
  of atomless laws lies in one T-orbit, mod null sets. So ε_R ≡ 0 for every d_op that
  vanishes on equal laws.
- **Source.** The isomorphism theorem for measures on standard Borel spaces (Kechris,
  *Classical Descriptive Set Theory*, Thm 17.41; cited from memory — primary-text check
  pending).
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

**Owner decision needed: freeze T for R1.** T is not derivable; it is a COMMITMENT
priced in L₀ plus vocabulary.

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
| D3 — invariance and coarse-graining | As in v1, plus: zero sets are monotone along the ladder. |
| D4 — finite-data identifiability | **OPEN.** Review 2 flag: BRI1's witness at these parameters needs about 10¹¹ samples. |
| D5 — comparator audit | Not started. Kill-condition flag above. |
