# D5 — identification agent: questions C and D (appendix to D5_COMPARATOR_AUDIT.md)

> Agent-written, evidence grade, not externally checked. Scratch paths map to `D5_evidence/`.

# D5 audit: questions C and D (common carrier and product-latent non-identifiability)

**Scope.** This was a read-only audit; nothing in `/tmp/claude-0/f0chain` was edited.

**What I read.**
- `D5_PREREGISTRATION.md`.
- `R1_T_LADDER.md`: §0, §4, §5(E), §8, §8.1, §9, §10, §11.1.
- `R1_DEFINITION.md`, `R1_SYNTHESIS.md`, `WO-002/REPORT.md`, `WO-001/C2_REPORT.md`.
- `OWNER_RULINGS.md` (G2-01, G2-08, G2-09, G2-10), `OWNER_RULING_R1_BOUNDARY.md`, `CHECKS.md`.
- From the BRI record at `92dc6bb`: `BRI0_CHARTER.md` (§5, §6, BRI-O7, BRI-O8), `BRI0_FINAL_SYNTHESIS.md`, `BRI1_ANALYTIC_ESCAPE_THEOREM.md` (T3), and both BRI1 novelty audits.

**Scratch sanity checks.** These use exact rational arithmetic and are evidence, not results.
- Script: `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/d5_cd_checks.py`
- Output: `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/d5_cd_checks_output.json`
- Checks K1 to K5 all return the expected values.

**Provenance (G2-10).**
- **Pre-result**, frozen at `82d311e`: the product-latent construction E1, Prop. E, E2, and the h ↦ h_a exclusion.
- **Added at `cb81a3b`**, after the WO-002 numbers were opened: the causal prefix-tree version of E1, the remark "ker K₀ ⊆ ker K_a suffices", and the excess-dimension dichotomy. These are mathematical strengthenings, not definition changes. I re-derive them independently below (D2, C4, C5).
- **POST-RESULT SYNTHESIS / STAGE-3 SEED** (per G2-10): the measurement-invariance framing and the instantaneous-state precision of the carrier. I use them below only to compare against comparator 9. They are not used to change any criterion.

**Notation.**
- A is the protocol set and P_a is the law of the record Y_a ∈ 𝒴 (ℝ^k, or path space).
- A **null model** is a protocol-independent latent law μ on a space 𝒵, together with readouts h_a: 𝒵 → 𝒴.
- T is a group of record maps. A family is **T-separable** if there are P★ and t_a ∈ T with P_a = t_a#P★. Under the standing nonsingular-covariance assumption this is exactly ε_R = 0 (Theorems A-BL(i) and M1).
- The three explanations, as model classes:
  - **E-A:** P_a = t_a#h#μ, with one h.
  - **E-B:** P_a = h_a#μ.
  - **E-C:** P_a = h#μ_a, with one h and Law(Z) depending on a.
- Ω is the map from a model to its family (P_a)_a.
- Identifiability follows Pearl (2009, Def. 2): Q(M) is identifiable under assumptions 𝒜 if P(M₁) = P(M₂) implies Q(M₁) = Q(M₂) for all M₁, M₂ satisfying 𝒜.

---

## Question D: product-latent non-identifiability

### Theorem D1 (product-latent universality; exact)

**Statement.**
- Let A be any index set and P_a any probability measures on measurable spaces 𝒴_a.
- Put 𝒵 := Π_a 𝒴_a with the product σ-algebra, μ := ⊗_a P_a, and h_a := π_a, the coordinate projection.
- Then h_a#μ = P_a for every a.
- If 𝒴_a = ℝ^k (or a vector space of paths), each h_a is linear and surjective.
- Hence, for any interface class T containing id and any d_op with d_op(P, P) = 0:

  inf over μ of max_a inf over (t_a ∈ T, h_a linear) of d_op(P_a, t_a#h_a#μ) = 0.

**Proof.**
- μ exists. For finite A it is the finite product measure. For arbitrary A it is the Łomnicki–Ulam product (Kallenberg 2002, Cor. 6.18).
- The marginal of a product measure on factor a is P_a.
- Take t_a = id. Then d_op(P_a, P_a) = 0 for every a. ∎

**Remarks.**
- No moment, shift, independence, atomlessness or causality assumption is used.
- **One-dimensional nonlinear variant.** Take Z ~ U(0,1) and h_a = f(a, ·), where f randomizes the kernel a ↦ P_a. Kallenberg's randomization lemma (2002, Lemma 3.22) supplies f, so a single uniform latent suffices once readouts may be nonlinear.

### Corollary D1′ (E-B and E-C are observationally equivalent everywhere)

**Statement.** Let 𝔉 be the set of all families.
- (i) Ω(E-B) = 𝔉.
- (ii) Ω(E-C) = 𝔉.
- (iii) Ω(E-A) = {T-separable families}.
- So the query Q = "Law(Z) depends on the protocol" is not identifiable at **any** family when readouts are unrestricted.
- **Test version.** Data are independent samples per protocol, so any test's rejection probability is a function of (P_a)_a alone. A level-α test of "exogenous with unrestricted readouts" therefore has power ≤ α at every E-C alternative.

**Proof.**
- (i) is D1.
- (ii): take a latent μ_a := P_a ⊗ ν_a with ν_a varying in a, and h := the first-coordinate projection.
- (iii) is the definition.
- For the test statement: the null is all of 𝔉, so the test has rejection probability ≤ α at every family. ∎

**Further remarks.**
- D1′ holds even if the counterfactual joint law of (Y_a)_a were observable, for example by replaying one initial microstate in simulation. Take μ := that joint law and h_a = π_a.
- Holland's (1986) "Fundamental Problem of Causal Inference" explains why ordinary data constrain only the marginals.
- **R1-NULL is not "no response".** E-C families exist inside every T-orbit. Examples are a response that is a T-map of W, or a response in modes that are not read. The harmonic bath is the program's own instance: back-reaction there is a deterministic shift, which lies in E₂±.

### Theorem D2 (causal version: prefix-tree latent; BRI0 non-anticipating domain)

**Setting.**
- Take a grid t₁ < … < t_k. Protocols are paths q_a.
- Define a ~_j b if q_a = q_b on [0, t_j]. These partitions are nested.
- The family is **non-anticipating** if Law(Y_a(t₁), …, Y_a(t_j)) depends on a only through the class [a]_j, for each j.
- A readout tuple is **causal** if rows 1..j of h_a depend on a only through [a]_j.

**Statement.**
- (i) Every non-anticipating family has an exact representation with a protocol-independent latent Z = (Z_c), indexed by the nodes c of the prefix tree, and with 0/1 selection readouts, where row j of h_a selects node [a]_j. These readouts are linear and causal.
- (ii) Conversely, any family with a causal-readout representation is non-anticipating.
- (iii) Hence, on any finite A: {families with a causal linear-latent representation} = {non-anticipating families} = grid-level E_univ.

**Proof.**
- **(i), level 1.** Draw Z_c from the law of Y_a(t₁) for any a ∈ c. This is well defined by non-anticipation.
- **(i), level j.** For a node c with ancestors c₁, …, c_{j−1}, the ancestor vector has the law of Y_a(t_{<j}) for any a ∈ c (induction hypothesis). The transfer theorem (Kallenberg 2002, Thm 6.10) gives a measurable f_c with Z_c := f_c(Z_{c₁..c_{j−1}}, V_c) and (ancestors, Z_c) =d Y_a(t_{≤j}). The V_c are i.i.d. U(0,1). This is well defined because Law(Y_a(t_{≤j})) is the same for all a ∈ c.
- **(i), conclusion.** By induction, (Z_{[a]₁}, …, Z_{[a]_k}) =d Y_a.
- **(ii).** Rows 1..j of h_a are determined by [a]₁, …, [a]_j, all of which are determined by [a]_j. So Law(rows 1..j of h_a·Z) depends on a only through [a]_j.
- **(iii).** The second equality is BRI0 §6's "Remark (KNOWN technique)": in discrete time, sequential randomization writes every non-anticipating family as a causal functional of q and one shared U. The first is (i)+(ii). ∎

**Remarks.**
- The plain product projections are causal only if [a]₁ ≠ [b]₁ for all a ≠ b.
- That fails for X1. P1 and P2 share the prefix [0, π], and π ∈ τ. The tree for (P0, P1, P2) on τ has 2 + 3 + 3 = 8 nodes, against 9 latent coordinates in the product.
- **Precision note for R1_SYNTHESIS §2.** "The zero set is exactly grid-level E_univ" holds for **causal** linear readouts. With unrestricted linear readouts the zero set is all of 𝔉 (D1).
- Exact sanity checks:
  - K1: a three-protocol, two-time non-anticipating family is reproduced exactly by tree selections, and row 1 is shared within the prefix class.
  - K2: the product projections are exact but not causal.

### Remark D3 (BRI1 itself has an exact E-B representation)

BRI-UPPER (BRI0 §6, BRI-O7) gives F_q(t) = C(𝒴_t[q, U], q(t)), where U ~ Gibbs is the initial bath state.
- **Latent Z := U (initial state).** Law(U) is protocol-independent, and the readout h_a = 𝔉_t[q_a, ·] is protocol-dependent. That is **E-B**.
- **Latent Z(t) := the instantaneous bath state.** The readout h = N_B^(−1/2)·Σ_j x_j(t) is common, and Law(Z(t)) depends on the protocol. That is **E-C**.

Both representations are exact for the same records. So for BRI1 the B/C label is relative to which state variable is declared to be the environment.
- The pre-result G2-08 certificate fixes this implicitly ("readout F = N_B^(−1/2)·Σ_j x_j(t)… so h is common").
- The explicit "why instantaneous" argument is post-result synthesis.
- This is exactly R1's North-star sentence: environmental identity must be declared.

### Closest established results and what R1 adds

| R1 statement | Established result it instantiates | Relation |
|---|---|---|
| D1, product latent with h_a = π_a | Balke and Pearl 1994 response-function variables: r ranges over all functions from A to the outcome domain, and Y = f(a, r) = r(a) is evaluation at a, which is a coordinate projection. Rubin/Neyman potential-outcome vector (Y(a))_a with consistency (Pearl 2009, Def. 4). | D1 is the response-function / potential-outcome representation with the product prior. Any coupling of the marginals works, because joint counterfactuals are unobservable (Holland 1986 FPCI; Pearl 2009, p. 121). |
| D1, one-dimensional nonlinear variant | Kallenberg 2002, Lemma 3.22 (randomization of a probability kernel) | Exact instance, with S = A. |
| D2, causal tree | Kallenberg 2002, Thm 6.10 (transfer), iterated. BRI0 §6 remark: E_univ equals the non-anticipating families (discrete time). Robins 1986: counterfactuals indexed by treatment history. | Instance. The only specialization is that the readouts are 0/1 selections, i.e. linear. |
| D1′, non-identifiability | Pearl 2009 Def. 2 (identifiability); Bongers et al. 2021 Def. 4.3 (interventional equivalence) | E-B and E-C models are interventionally equivalent with respect to the record. |
| Remark D3 | BRI-UPPER (internal, `92dc6bb`) | R1's carrier exclusion is BRI0's "back-reaction itself is never the discriminator" restated in readout language. |
| Prop. E, injective nonlinear readouts | Kechris 1995, Thm 17.41 | Already cited in R1 §5. |

**What R1 adds beyond specialization.**
- **No new mathematics.** Its two additions are:
  1. The readouts can be taken **linear** (coordinate or 0/1 selections). So the linearity of the frozen Tier-1 class gives no protection by itself.
  2. It locates the protection in a cross-protocol condition (C1 below).
- Both are elementary.
- **Category input for D.**
  - (M): STANDARD MATHEMATICS. On its own, the statement is an instance of known representation theorems.
  - (P): the statement is frozen pre-result, and R1_SYNTHESIS §2 already says it "is not claimed as new". That is correct.

---

## Question C: is the common-carrier certificate an unavoidable identifying assumption?

**Framing.** An identifying assumption is a restriction 𝒩 on null models (μ, (h_a)).
- It is **sound for ε_R^T** if every family in Ω(𝒩) is T-separable. Then ε_R^T > 0 certifies that the model is not in 𝒩.
- **Readout-only** means 𝒩 restricts the tuple (h_a) and leaves μ free. That is R1's own frame, since ε_R takes the infimum over all P★.

### C(i): without restrictions, no record statistic separates E-B from E-C

This is Corollary D1′.

### Theorem C1 (the carrier is necessary and sufficient for soundness under readout-only assumptions; T = T_R1)

**(a) Linear readouts, inside the standing assumption.**
- Let h_a: ℝ^m → ℝ^k be affine, with linear parts H_a of rank k.
- The following are equivalent:
  - (i) (h_a#μ)_a is T_R1-separable for every μ with a density. Equivalently, ε_R = 0 for every exogenous family.
  - (ii) ker H_a = ker H_b for all a, b.
  - (iii) h_a = t_a∘H for one linear H and t_a ∈ T_R1 (the common carrier).
- *Proof.*
  - (iii) ⇒ (i): set P★ = H#μ.
  - (ii) ⇒ (iii): equal kernels and equal rank give H_a = L_a·H_{a₀} with L_a ∈ GL(k).
  - (i) ⇒ (ii): suppose v ∈ ker H_b but v ∉ ker H_a. Let μ = Law(G + ξv), with G ~ N(0, I_m) and ξ independent, with a density, mean 0 and E ξ³ ≠ 0. Then h_b#μ is a nondegenerate Gaussian. h_a#μ has third cumulant (u·H_a v)³·κ₃(ξ) ≠ 0 along u = H_a v. T_R1 maps Gaussians to Gaussians, so the two laws are not in one orbit. ∎
  - The obstruction is exactly §10 E2, so E2's mechanism is the generic one.

**(b) Measurable readouts, finitely supported environment laws.**
- Let h_a: 𝒵 → ℝ^k be measurable.
- Then (h_a#μ)_a is T_R1-separable for every finitely supported μ if and only if h_a = t_a∘h with t_a ∈ T_R1. In that case it is separable for every μ.
- *Proof.*
  - **Step 1: equal level sets.** Suppose h_b z = h_b z′ but h_a z ≠ h_a z′. With μ = ½δ_z + ½δ_z′, the two images have different numbers of atoms, and bijections preserve atom count. So h_a = φ∘h_b for a bijection φ: h_b(𝒵) → h_a(𝒵).
  - **Step 2: φ is locally affine.** For distinct points h_b z₁..h_b z_n, put distinct weights w_i on the z_i. Separability gives s ∈ T_R1 with h_a#μ = s#h_b#μ. Matching atoms by weight forces s = φ on that finite set.
  - **Step 3: φ is globally affine.** Fix an affine basis x₀..x_m of aff(h_b𝒵). For any further point x, the map s_x is fixed on aff(h_b𝒵) by the basis values, so φ is one injective affine map on the hull. It extends to an element of T_R1.
  - **Step 4.** Put h := h_{a₀}. ∎
- Exact check K4 confirms the atom count.

**Consequence.**
- Among readout-only assumptions, the common carrier modulo T_R1 is the **unique weakest** one under which "ε_R^T_R1 > 0 ⇒ not exogenous" holds for unknown environment laws.
- Any strictly weaker readout-only assumption admits a false positive.
- Tier 2 (T_mono): sufficiency holds trivially. **Necessity is OPEN**, because the atom argument is unavailable for continuous margins.

### Weaker assumptions (C(ii)), each stated exactly

**Prop. C2 (per-map conditions).**
- If each admissible class contains the coordinate projections of some product latent, then Ω(𝒩) = 𝔉 and nothing is identified. This covers linear, full-rank, surjective, Lipschitz, smooth and nondegenerate-output classes.
- Per-map **linear injectivity** does identify. But it does so only by implying the carrier: rank k plus injectivity gives m = k and h_a ∈ GL(k), so W := Z is the carrier.
- Per-map **Borel** injectivity absorbs every atomless family (Prop. E; Kechris 17.41).

**Prop. C3 (known finite readout family, unknown assignment).**
- Readouts are drawn from {g₁, …, g_m}, which are jointly free: any m-tuple of laws is realizable.
- Then Ω(𝒩) = {families with at most m distinct T-orbits}, and identification is pure counting.
- *Proof.* Protocols that share a g lie in one orbit. Conversely, pick one representative per orbit and use freeness. ∎
- For two-protocol witnesses (P0 vs P1: Theorem C, Prop. G), m ≥ 2 identifies nothing.
- Whether BRI1's three protocols occupy three distinct orbits was not preregistered or tested, and is **not claimed**.
- **Analog.** This mirrors ICP's relaxation that "interventions on Y happened in at most V environments" (Peters et al. 2016, eq. (32)).

**Prop. C4 (bounded mode-selection excess; two protocols; T_R1).**
- Define the excess e as the dimension of ker H_a after quotienting ker H₀ ∩ ker H₁, on the fluctuation span.
- An exogenous linear representation with excess ≤ e exists **if and only if** there are affine surjections ℓ₀, ℓ₁: ℝ^k → ℝ^(k−e) with ℓ₀#P0 = ℓ₁#P1.
- *Proof.*
  - (⇒): set K = ker H₀ ⊕ ker H₁. The quotient map q onto ℝ^m/K, of dimension ≥ k − e, factors through both readouts.
  - (⇐): glue P0 and P1 along the common marginal using the transfer theorem. The glued law lives on {ℓ₀y₀ = ℓ₁y₁} ⊂ ℝ^2k, of dimension k + e. The readouts are the two coordinate projections. ∎
- Exact check K3 (k = 2, e = 1): a centrally symmetric P0 and a skewed P1 with a common one-dimensional marginal are reproduced exactly from a three-dimensional latent.
- **Endpoints.**
  - e = 0 gives one T_R1-orbit, i.e. the carrier and ε_R = 0.
  - e = k makes everything absorbable.
  - At k = 1, any e ≥ 1 absorbs every pair. So single-time witnesses (Prop. G at one time) give nothing under any mode-selection excess.
- This makes §10's "excess dichotomy" exact and graded.
- The test is a common-marginal test, not ε_R.

**Prop. C5 (reference-only injectivity, ker K₀ ⊆ ker K_a).**
- Under R1's standing assumption (every P_a on ℝ^k with nonsingular covariance), every K_a has rank k on the fluctuation span. So the kernels have equal dimension, inclusion becomes equality, and K_a = L_a K₀ with L_a ∈ GL(k).
- So it **collapses to the carrier**.
- It is genuinely weaker only with lower-dimensional or singular records. There it gives the one-sided null P_a = L_a#P0, a deterministic-garbling order.

**Partial calibration on a subset of channels J (anchor channels).**
- ε_R on the J-marginal records is sound.
- This is still carrier-type, applied to fewer channels. It is the analog of partial measurement invariance (Byrne et al. 1989).

**Prop. C6 (environment-side alternative, incomparable with the carrier).**
- **Null:** μ is centrally symmetric (all modes, read or not), and the h_a are affine and protocol-dependent, of any rank.
- **Tier 1.** Every P_a is then centrally symmetric. Any odd witness (Theorem F1) rejects this null, with no common carrier needed.
- **Tier 2.** If h_a = (φ_{a,i}∘ℓ_{a,i})_i, with each ℓ_{a,i} affine and each φ_{a,i} monotone, then every copula is radially symmetric. So the M2 / F4 odd channel rejects this null.
- **The even channel is not covered.** Counterexample: μ = N(0, I₃), h₀ = (z₁, z₂), h₁ = (z₁, (z₁ + z₂)/√2). The normal-score correlation goes from 0 to 1/√2 with no back-reaction. This changes T_mono orbits, while both laws are in one T_R1 orbit.
- **BRI1 satisfies this premise.** The whole bath state path law is symmetric under (x, p) ↦ (−x, −p) (BRI1 T3), and F is linear.
- So the disjunctive assumption "carrier OR (global symmetry + affine readouts)" is **strictly weaker** than the carrier, and it still certifies BRI1's Tier 1 and Tier-2 odd channel.
- **Only the Tier-2 even channel (Δρ, which escapes under T_mono only) needs the carrier itself.**
- Exact check K5: a symmetric latent read through mode-selecting maps gives symmetric records; E2's asymmetric latent does not.

### Necessity: no assumption-free identification

- Every sufficient assumption must exclude, for the family at hand, all the representations above: the product latent (D1), the tree latent (D2), the single-uniform randomization, and the initial-state representation (BRI-UPPER).
- None of these assumptions can be refuted by records, because E-C with h = id and μ_a = P_a satisfies all of them. So any certificate must come from outside the records.
- Moreover (Remark D3), the certificate includes a declaration of what the environment's state variable is.

### Comparison with established identifying assumptions

| Assumption | Primary statement | Relation to the carrier certificate |
|---|---|---|
| Measurement invariance (Meredith 1993; Merkle and Zeileis 2011, eq. 7) | f(X given T, V) = f(X given T): the measurement does not depend on group V given the latent T. Without it, valid comparisons of latent means are impossible (Van de Schoot et al. 2015). | The carrier is deterministic measurement invariance with respect to the protocol, relaxed modulo T. Mode selection is measurement non-invariance. The same type of assumption, restated. |
| Partial invariance; DIF identification (Byrne et al. 1989; Bechger and Maris 2015) | Some parameters invariant. "The difficulty of an item is not identified … relative difficulties are." | Analog of anchor channels and of identifying only quotient invariants. |
| Exclusion restriction (Angrist, Imbens and Rubin, Assumption 2) | Y(Z, D) = Y(Z′, D) | The carrier means Y_a(z) = Y_a′(z) modulo T. The protocol is excluded from the measurement equation given the environment state. In IV the mediator D is observed; here it is latent. |
| Nondifferential outcome measurement (Hernán and Cole 2009) | f(U_Y given A) = f(U_Y); differential error means an arrow from A to U_Y | Mode selection is differential outcome measurement. Restated. |
| Invariant prediction (Peters et al. 2016, Assumption 1 and Prop. 1) | The conditional law of the target given its causal parents is invariant; no interventions on Y | Analogous structure (assume one mechanism invariant, test another), but ICP's invariant object is observable and testable. Not a restatement. |
| Latent-law restrictions (Comon 1994, ICA Thm 11; symmetry) | Independence plus non-Gaussianity identifies the mixing up to scale and permutation | Prop. C6's route: restrict μ instead of h. An alternative, not a restatement. |

**Verdict input for C.**
- (M): STANDARD MATHEMATICS. C1–C6 are elementary: atom counting, gluing by transfer, rank arguments.
- (P): the certificate's **type** is restated: measurement invariance, exclusion restriction, nondifferential measurement. Its **form** is not stated in this form by any comparator. That form is: invariance modulo a declared, calibrated, protocol-dependent T on the record; the target is the whole latent law modulo T; and the latent is the declared instantaneous state.
- So (P) belongs in the middle category, not RESTATED. Standard MI compares latent means and variances; it does not compare latent laws modulo per-group affine maps.
- **Kill trigger.** C and D do not trigger "unidentifiable within declared scope", because the certificate is part of the frozen pre-result scope. The identification is still conditional and untestable from records. That is a portability limit, and it should be stated as one.

---

## Citations and verification status

| Source | Item relied on | Status |
|---|---|---|
| Balke and Pearl, UAI 1994, arXiv:1302.6784 | §2: the response-function variable "takes on as many values as there are functions between A and B", linked to Rubin's potential responses. §3: bounds by optimizing over functional models. | VERIFIED (primary text) |
| Pearl, Statistics Surveys 3 (2009) 96–146, DOI 10.1214/09-SS057 (author's tech report R-350) | Def. 2 (identifiability; Pearl 2000a p. 77; the source has a typo, P(M1) = P(M1)). Def. 4 (counterfactual Y_x(u); 2000a p. 98). Joint counterfactuals unobservable (p. 121). | VERIFIED (primary text) |
| Pearl, Causality, 2nd ed. 2009: ch. 7 §7.1; §8.2.2 "Canonical Partitions" | Section titles | Table of contents VERIFIED (bayes.cs.ucla.edu/BOOK-2K/book-toc.html). §8.2.2 title from a search snippet only. Book text UNVERIFIED. |
| Holland, JASA 81(396) 945–960 (1986), DOI 10.1080/01621459.1986.10478354, JSTOR 2289064 | Fundamental Problem of Causal Inference, p. 947 | VERIFIED (primary scan) |
| Kallenberg, Foundations of Modern Probability, 2nd ed. 2002: Lemma 3.22; Thm 6.10; Cor. 6.18 | Randomization; transfer; Łomnicki–Ulam product measure | VERIFIED-SECONDARY: verbatim or applied statements in Janson arXiv:1711.09830 (Lemma 2.7), Janson arXiv:0902.0306 (§5), Shalizi 36-754 solutions (Ex. 3.1). Book not inspected. |
| Kechris, CDST, GTM 156 (1995), Thm 17.41 | Isomorphism theorem for continuous measures | VERIFIED by the prior R1 workflow check plus a search confirmation. Not re-inspected. |
| Robins, Math. Modelling 7 (1986) 1393–1512 | Counterfactuals indexed by treatment history | Bibliographic VERIFIED. Content UNVERIFIED (secondary summaries only). |
| Bongers, Forré, Peters, Mooij, Ann. Statist. 49(5) 2885–2915 (2021), DOI 10.1214/21-AOS2064 | Def. 4.3 (interventional equivalence) | VERIFIED (arXiv:1611.06221 text) |
| Meredith, Psychometrika 58(4) 525–543 (1993), DOI 10.1007/BF02294825 | Measurement-invariance taxonomy | Bibliographic VERIFIED. Definition VERIFIED-SECONDARY via Merkle and Zeileis, Innsbruck WP 2011-09, eq. (7). |
| Van de Schoot et al., Front. Psychol. 6:1064 (2015), DOI 10.3389/fpsyg.2015.01064 | MI definition; latent mean comparison impossible without MI | VERIFIED (PMC4516821) |
| Byrne, Shavelson, Muthén, Psychol. Bull. 105(3) 456–466 (1989) | Partial invariance | Bibliographic VERIFIED. Content via Van de Schoot (secondary). DOI UNVERIFIED. |
| Bechger and Maris, Psychometrika 80(2) 317–340 (2015), DOI 10.1007/s11336-014-9408-y | Item difficulty not identified; relative difficulties are | VERIFIED (abstract) |
| Angrist, Imbens, Rubin, NBER TWP 136 (1993); published JASA 91 (1996) 444–455, DOI 10.2307/2291629 | Assumption 2, exclusion restriction: Y(Z, D) = Y(Z′, D) | VERIFIED in the working-paper scan, pp. 10–12. The published-version numbering was not inspected. |
| Hernán and Cole, Am. J. Epidemiol. 170(8) 959–962 (2009), DOI 10.1093/aje/kwp293 | f(U_Y given A) = f(U_Y) | VERIFIED (PMC2765368) |
| Peters, Bühlmann, Meinshausen, JRSS-B 78(5) 947–1012 (2016), arXiv:1501.01332 | Assumption 1; Prop. 1; eq. (32) | VERIFIED (arXiv text) |
| Comon, Signal Processing 36(3) 287–314 (1994), DOI 10.1016/0165-1684(94)90029-9 | Thm 11 (ICA identifiability) | VERIFIED-SECONDARY |
| BRI0 §6 remark, BRI-UPPER, BRI-O7; BRI1 T3 (`92dc6bb`) | E_univ = non-anticipating families (discrete time); X1 ∈ E_univ; parity symmetry | Internal record, read |

The prior BRI1 novelty audits are consistent with this report and are not contradicted. In particular, the supplement grades the invariance logic as KNOWN-IN-NEARBY-FORM.

---

## Final answers

**C.** The common carrier is unavoidable in a qualified sense, not an absolute one.
- **What is unavoidable.** Some identifying assumption from outside the records is needed. By D1′, no record statistic separates E-B from E-C. Every sufficient assumption is unrefutable by records, and it must also declare what the environment's state variable is: for BRI1 itself, BRI-UPPER gives an exact mode-selection representation with the initial-state latent.
- **Where the carrier is minimal.** Within R1's own frame, where only the readouts are restricted and the environment law is left free, the carrier modulo T_R1 is necessary and sufficient for ε_R > 0 to be a sound reciprocity certificate. That is Theorem C1, for linear readouts with densities and for measurable readouts with finitely supported laws. So it is the unique weakest assumption of that kind.
- **Weaker readout-only assumptions** give only graded partial identification, with their own statistics:
  - m possible readouts: identification only when there are more than m orbits (C3);
  - mode-selection excess e: an exact common-marginal criterion that degrades to nothing at e = k, and at e ≥ 1 for single-time witnesses (C4);
  - reference-only kernel inclusion collapses to the carrier under R1's standing assumption (C5);
  - anchor-channel calibration is still carrier-type.
- **Where it is not the only route.** An environment-side premise — global symmetry of the whole environment plus affine (or monotone∘affine) readouts — is incomparable with the carrier. The disjunction of the two is strictly weaker than the carrier and still certifies BRI1's Tier 1 and Tier-2 odd channel. Only the Tier-2 even channel needs the carrier itself (C6).
- **Relation to established assumptions.** The certificate is the same type of assumption as measurement invariance, exclusion of the protocol from the measurement equation, or nondifferential outcome measurement. Its R1 form (modulo a declared calibrated T, applied to the whole latent law, on a declared instantaneous state) is not stated in this form by any comparator.
- **Category input:** (M) STANDARD MATHEMATICS; (P) STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION, not DISTINCTIVE.

**D.** Yes. The product-latent construction proves exact, total non-identifiability when protocol-dependent readouts are unrestricted.
- **The theorem (D1).** For every family, with any index set and at path level, μ = ⊗P_a with linear projections h_a = π_a reproduces every P_a exactly. So ε vanishes for every d_op with d_op(P, P) = 0, E-B and E-C have identical observational images, and every level-α test of E-B has power ≤ α.
- **Causal version (D2).** On BRI0's non-anticipating domain, a prefix-tree latent with 0/1 selection readouts gives an exact causal linear representation. The causal-linear zero set equals the non-anticipating families, which is grid-level E_univ.
- **Not new mathematics.** D is an instance of:
  - the response-function / potential-outcome representation (Balke–Pearl 1994; Pearl 2009 Def. 4), with only marginals constrained (Holland 1986);
  - Kallenberg's randomization lemma (one-latent nonlinear version) and transfer theorem (causal version);
  - BRI0's own E_univ remark and BRI-UPPER.
- **What R1 adds** is specialization only: the readouts may be taken linear, so the protection comes from commonality of the readout, not linearity. Theorem C1 makes that location exact.
- **Category input:** STANDARD MATHEMATICS. Correctly frozen pre-result and not claimed as new. One wording fix: in R1_SYNTHESIS §2, "zero set = E_univ" should say "causal linear readouts".