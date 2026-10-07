# R1 — DEFINITION OF ε_R (Claude Code) · v1 · 2026-10-06

**Scope.** This fixes ε_R for the class T = E₂±, BRI1's own competitor class. That is
the instance Stage 2 and WO-001 need. The general "maximal independently calibrated,
environment-preserving" class from `STATE.md` is not specified here.
**Update (v2):** the enlarged classes are treated in `R1_T_LADDER.md`. Its §7
supersedes §3 below where the two differ.

**Status of the pieces.**
- Propositions 1–3 and Corollary 4: DERIVED (proofs below). Sanity checks:
  `r1_witness_bound_check.py` and its output JSON.
- The choice of d_op is a definition decision, open to owner veto.

**Erratum (owned).** WO-001's provisional spec said the skewness spread
"lower-bounds the distance to E₂±". That was written before any d_op was fixed, and
it is false for total variation (Prop. 3). Proposition 2 below replaces it.

## 1. Definition

- **Data.**
  - A finite protocol set A and a time grid t₁ < … < t_k.
  - P_a is the law of the force path Y_a = (F_a(t₁), …, F_a(t_k)) ∈ ℝ^k under
    protocol a. It is the multi-time joint law, never a single-time marginal.
  - Each P_a has finite third moments and nonzero variance at every time.
- **Interface class T = E₂±** (`BRI0_CHARTER.md` §5, with G ≠ 0):
  - T = { y ↦ M + G⊙y : M ∈ ℝ^k, G ∈ (ℝ∖{0})^k }, where ⊙ is the per-time product.
  - T is a group under composition.
- **Standardization.** std(P) is the law of Z, where Z_i = (Y_i − E Y_i)/sd(Y_i).
- **Distance.** **d_op(P, Q) := W₃(std P, std Q)**, the Wasserstein-3 distance with
  Euclidean cost on ℝ^k. W_p for any p ≥ 3 also works, because W₃ ≤ W_p.
- **The object.**

  **ε_R^(T)(P_A) := inf over P★ of max over a ∈ A of inf over t_a ∈ T of d_op(P_a, (t_a)#P★)**

## 2. Results

**Proposition 1 (quotient form).** Define

d_q(P, Q) := min over s ∈ {±1}^k of W₃(std P, s·std Q).

Then:
- inf over t ∈ T of d_op(P, t#Q) = d_q(P, Q);
- d_q is a pseudometric;
- d_q(P, Q) = 0 if and only if Q ∈ T#P.

Consequently ε_R = inf over P★ of max_a d_q(P_a, P★), which is the radius of the
family in the quotient by T. Moreover:
- **(i)** ε_R = 0 if and only if all the P_a lie in one T-orbit, that is, if and only
  if the protocol dependence factors through T.
- **(ii)** ½·max_{a,b} d_q(P_a, P_b) ≤ ε_R ≤ max_{a,b} d_q(P_a, P_b).

*Proof.*
- **Standardization absorbs T.** If Y′ = M + G⊙Y, then Y′_i − E Y′_i =
  G_i(Y_i − E Y_i) and sd(Y′_i) = |G_i|·sd(Y_i). So std(t#Q) = sign(G)·std(Q), and
  every sign vector arises for some G. This gives the first equality.
- **d_q is a pseudometric.** y ↦ s⊙y is a Euclidean isometry and s² = 1.
  - Symmetry: W₃(Z, sW) = W₃(sZ, W).
  - Triangle inequality: W₃(Z, ss′X) ≤ W₃(Z, sW) + W₃(W, s′X).
  - Zero set: d_q = 0 if and only if the standardized laws agree up to sign, that is,
    if and only if Q ∈ T#P.
- **(i), "if".** Take P★ in the common orbit.
- **(i), "only if".** If the radius is 0, then for every δ > 0 some P★ has
  d_q(P_a, P★) < δ for all a. So d_q(P_a, P_b) < 2δ for every δ, which forces
  d_q(P_a, P_b) = 0. No attainment is needed.
- **(ii), lower bound.** By the triangle inequality,
  d_q(P_a, P_b) ≤ 2·max_c d_q(P_c, P★) for any P★.
- **(ii), upper bound.** Take P★ = P_b. ∎

**Proposition 2 (moment witnesses for ε_R). Proved; the constants are computed from
the data.**

For protocols a, b and time index i, write:
- γ_a(i) = E[Z_{a,i}³] (the standardized skewness);
- m_a(i) = ‖Z_{a,i}‖₃;
- ρ_a(i, j) = E[Z_{a,i} Z_{a,j}].

Then:
- **(2a)** | |γ_a(i)| − |γ_b(i)| | ≤ d_q(P_a, P_b)·L_ab(i), where
  L_ab(i) = m_a(i)² + m_a(i)m_b(i) + m_b(i)².
  **Hence ε_R ≥ max_{a,b,i} | |γ_a(i)| − |γ_b(i)| | / (2·L_ab(i)).**
- **(2b)** | |ρ_a(i,j)| − |ρ_b(i,j)| | ≤ 2·d_q(P_a, P_b).
  **Hence ε_R ≥ max | Δ|ρ| | / 4.** This is a multi-time witness: E₂± preserves
  cross-time correlations up to sign.

*Proof.*
- **Setup.** Fix s and an optimal W₃ coupling of (std P_a, s·std P_b). In coordinate
  i, put U = Z_{a,i} and V = s_i Z_{b,i}. Then ‖U − V‖₃ ≤ W₃.
- **(2a).** E U³ − E V³ = E[(U − V)(U² + UV + V²)].
  - Hölder with exponents (3, 3/2) bounds this by ‖U − V‖₃·‖U² + UV + V²‖_{3/2}.
  - Minkowski in L^{3/2}, together with ‖U²‖_{3/2} = ‖U‖₃² and
    ‖UV‖_{3/2} ≤ ‖U‖₃‖V‖₃, gives
    ‖U² + UV + V²‖_{3/2} ≤ ‖U‖₃² + ‖U‖₃‖V‖₃ + ‖V‖₃² = L_ab(i).
  - E V³ = s_i·γ_b(i) and ‖V‖₃ = m_b(i). Since
    | |γ_a| − |γ_b| | ≤ |γ_a − s_i γ_b| for either sign, minimizing over s gives (2a).
  - The bound on ε_R follows from Prop. 1(ii).
- **(2b).** E[U_iU_j − V_iV_j] = E[(U_i − V_i)U_j + V_i(U_j − V_j)]
  ≤ ‖U_i − V_i‖₂ + ‖U_j − V_j‖₂ ≤ 2W₂ ≤ 2W₃. Here we used ‖U‖₂ = ‖V‖₂ = 1. ∎
  - *Correction (2026-10-07, workflow verification).* Under the fixed W₃-optimal
    coupling, the step "≤ 2W₂" is not justified, because ‖U − V‖₂ for that coupling is
    ≥ W₂. The conclusion is still correct: ‖U − V‖₂ ≤ ‖U − V‖₃ = W₃, so the bound is
    ≤ 2W₃. Alternatively, choose a W₂-optimal coupling to get 2W₂.

**Proposition 3 (total variation, W₁ and W₂ cannot support a skewness bound).**
Take P_η = (1−η)·N(0,1) + η·δ_c with c = η^(−1/3). As η → 0:
- TV(P_η, N(0,1)) = η → 0, and the same holds after standardization;
- W₂ ≲ η^(1/6) → 0, and W₁ → 0;
- but γ(P_η) → 1, while γ(N(0,1)) = 0. The computed values are in the C3 table.

So no d_op from {TV, W₁, W₂} admits a skewness lower bound on ε_R. W₃ is the weakest
W_p that does, and it stays O(1) on this family.

**Corollary 4 (the lower-bound half of deliverable 2: BRI1 ⇒ ε_R > 0).**
- BRI1's witness is a standardized single-time third-cumulant/skewness difference
  across protocols (synthesis, line 39). Escaping the *signed* class E₂± requires
  |γ| to differ.
- So for each fixed small t and every N_B ≥ N₀(t), with BRI1's quantifiers verbatim:
  ε_R^(E₂±) ≥ | |γ_{a}(t)| − |γ_{b}(t)| | / (2L) > 0.
- As N_B → ∞, L tends to 3·(E|N(0,1)|³)^(2/3) ≈ 4.10. So the lower bound inherits
  BRI1's witness size, O(1/N_B).
- **Not shown:** an upper bound on ε_R with the same rate, and the reservoir limit
  ε_R → 0. Those remain OPEN.

## 3. Deliverable status

| Deliverable | Status |
|---|---|
| D1 — ε_R = 0 on exogenous processes whose protocol dependence factors through T | **DERIVED** for E₂± (Prop. 1(i)). Holds for colored and non-Markovian noise, since no Markov property is used. The converse also holds. |
| D2 — BRI1 as a special case | **Lower-bound half DERIVED** (Cor. 4). The rate and the reservoir-limit upper bound are OPEN. |
| D3 — invariance and coarse-graining | **DERIVED in part:** ε_R is invariant under per-protocol T-maps and protocol relabelling (Prop. 1). It is non-increasing under time-marginalization, because coordinate projection is 1-Lipschitz for W₃ and standardization commutes with it. Nonlinear coarse-grainings are OPEN. |
| D4 — identifiability from finite data | **OPEN.** Route: plug-in estimation of the Prop. 2 witnesses (consistent under finite 6th moments), plus empirical W₃ convergence rates (literature to verify). |
| D5 — comparator audit | **Not started.** |
