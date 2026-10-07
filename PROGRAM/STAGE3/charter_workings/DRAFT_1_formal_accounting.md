# Stage-3 charter: null space, scoring and gates for the 𝒦 cards (draft for freeze) · 2026-10-07

**Status: DRAFT FOR FREEZE.**
- The charter is written alone, before any 𝒦 candidate exists, as G2-11 requires.
- It contains no candidate law and no example law. It preregisters no target relation, sign or functional form.
- After the freeze, stop for owner review before Card 1 (G2-11; RULES checkpoint (d)).

**Authority.**
- G2-11: items 1–9, the central task, and the owner additions. The additions are numbered here as:
  - A1: merge = provenance, not endorsement.
  - A2: ε_R is derived.
  - A3: the baseline is computed after standard theory.
  - A4: response scope.
- The G2-11 reconciliation note applies: 𝒜_ε is the image of 𝒜_Γ × 𝒜_T, not a free axis.

**Builds on.**
- `PROGRAM/STATE.md`, `RULES.md`, `NORTH_STAR.md`, `SCOREBOARD.md`, `GRAVEYARD.md`.
- `RESULTS/R1/R1_SYNTHESIS.md` (§§1–3, 7, 11, 12) and `D5_COMPARATOR_AUDIT.md` (§§2.3, 3, 6).
- `R1_T_LADDER.md` §§0–2.
- `F0_REQUIREMENTS_CONSOLIDATION_01.md`.
- The SD0 charter, compactness accounting, result and reconnaissance.

**Naming.**
- **FR1–FR15** are the F0 requirements (R1–R15 in the consolidation). "R1" means Stage 2 only.
- A **CHARTER TEST** is an abstract gaming pattern used to test this charter's rules. It is never a candidate.

**Coverage**

| G2-11 element | Where |
|---|---|
| Item 1: baseline freedom spaces 𝒜_Π, 𝒜_T, 𝒜_Γ (𝒜_ε as image) | §2, §3 |
| Item 2: success criterion | §4, §5, §7 |
| Item 3: compression accounting and information price | §6 |
| Item 4: nonrelocation | §8 |
| Item 5: budget of three distinct cards | §10 |
| Item 6: required card contents | §9 |
| Item 7: originality at the assembled-law level | §11 |
| Item 8: cross-sector parameter transfer | §12 |
| Item 9: stopping rule | §14 |
| A1: merge = provenance | §15 |
| A2: ε_R derived; definitional relations earn nothing | §3 B2; §5 Q2, Q5 |
| A3: baseline after causality, positivity, KMS/FDT, Onsager, conservation | §3 B3–B7; §5 Q3 |
| A4: response scope | §5 Q7–Q8; §9 C8 |
| Carrier/readout derived; no unique formula for h; no presumed tradeoff | §1 O3, O6; §8 NR3; §5 Q10 |
| Stage 4–6 definitions made concrete | §13 |

**Known trajectory risks, and the rule that blocks each**

| Risk | Blocking rule |
|---|---|
| R1 grows into a prerequisite staircase | §1 O8 (ladder closed); §14 T4 (R1 upgrades never block Stage 3) |
| A card built only from consistency conditions hits the SD0 arc-consistency / undecidability boundary | §13.2 CO1–CO4; SB1.7 (theta) |
| No named lock target | §5 Q11; §9 C7; missing → CARD-INCOMPLETE |
| Selectivity checked without a concrete battery | §13.1 SB-1 and §13.3 HB, frozen here |

---

## 0. Principles

- **0.1 Null space before candidates.** This charter fixes everything a card is judged against: the baselines, the chart, the standard package, the hostile batteries, the price code and every threshold. No card can redefine what counts as an impressive freedom reduction.
- **0.2 Hostility rule.**
  - Where a rule has two readings, the one less favorable to the card applies.
  - Where a quantity can only be bounded, the bound less favorable to the card is scored.
- **0.3 Finite and certified.**
  - Every scored quantity is computed on the frozen finite representation (§2), in exact rational or rigorous interval arithmetic.
  - Sampling results are evidence grade and never score.
- **0.4 Zero sets, not formulas.**
  - A relation is scored only through its zero set. Scores do not change under rescaling, sign change or invertible reparametrization of the relation.
  - No sign, monotonicity or functional form is presumed (G2-11: no presumed identity–response tradeoff).
- **0.5 Modulo representation.** Partition, readout and interface are scored modulo representation (FR1; G2-11):
  - Π modulo Aut(Ξ);
  - readouts as classes [h]_{T_Π};
  - records through T-invariants wherever the declared scope requires it.

## 1. Objects (frozen notation)

**O1. Ξ.** The relational process object a card constrains.
- The card declares Ξ's type in L₀ (§6) plus priced vocabulary.
- It also declares a finite carrier set V_Ξ: its relata at the frozen resolution.
- If V_Ξ is derived (for example, collective degrees of freedom), its construction is part of the generated chain and falls under §8.

**O2. The law.** 𝒦[𝒞, Ξ] = 0.
- 𝒞 is the card's context/compatibility data. Its meaning is declared and priced (FR11).
- Sol(𝒦, 𝒞) := {Ξ : 𝒦[𝒞, Ξ] = 0}, at a stated resolution.

**O3. Generated chain.** The card supplies algorithms, not data, for each of these:
- Π = π_𝒦(Ξ);
- the **carrier**: which state variable of E counts as "the environment" (R1_SYNTHESIS §12 item 1; D5 Remark D3);
- the readout class [h]_{T_Π};
- the interface class T_Π;
- Γ_Π = Obs_Π(Ξ);
- ε_R = ε[Γ_Π, T_Π].

Write G_𝒦 : Sol → (Π, T_Π, Γ_Π).

**O4. Partition.** Π is a labeled map μ: V_Ξ → {S, E, ∂}.
- S and E are nonempty.
- ∂ is the approximate boundary, with |μ⁻¹(∂)| ≤ δ_∂·|V_Ξ|.
- Soft memberships are mapped by the threshold θ_μ: membership ≥ θ_μ goes to S or E, otherwise to ∂.
- **Persistent** means one μ for every protocol in the repertoire and over the whole record horizon, up to a normalized Hamming drift ≤ δ_drift.
- Π is counted modulo Aut(Ξ).

**O5. Protocols and records.**
- Protocols act only on S, through one S-side intervention channel.
- Records are read on E through the common carrier.
- Γ_Π := (P_a) over a ∈ A, where P_a is the joint law of Y_a ∈ ℝⁿ, n = k·d_rec, on the frozen grid.

**O6. Readout class and interface class.**
- [h]_{T_Π} is the class of latent-to-record maps that the card proves physically equivalent.
- T_Π is the group of record-space maps t with t∘h ∈ [h].
- **Carrier condition:** h_a ∈ [h]_{T_Π} for every protocol a. There is no mode selection (R1_SYNTHESIS §§2–3).
- The card derives the class. No unique coordinate formula for h is assumed or required.

**O7. ε.** The frozen R1 definition (R1_SYNTHESIS §1) is used unmodified.
- ε⁽¹⁾ := ε^{T_R1}: the bounded-Lipschitz quotient after centering and whitening, with O(k) residual group.
- ε⁽²⁾ := ε^{T_mono}: the bounded-Lipschitz quotient on normal-score laws, with the reflections as residual group. It is defined only for atomless margins with interval supports; otherwise it is ⊥.
- ε_R := ε⁽ⁱ⁾ when T_Π equals tier i. **No other ε value exists in Stage 3.**
- For every T in the lattice O8, the distance-free predicate sep_T(Γ) := [all P_a lie in one T-orbit] is available. Where ε^T is defined, sep_T is its zero set (Theorem A).
- Zero sets are monotone in T; values are not (R1_T_LADDER §2).

**O8. Interface lattice 𝕃_T.**
- **The chain:** T_0 = {id} ⊂ T_tr (translations) ⊂ E₂± (coordinatewise affine) ⊂ T_caus (lower-triangular affine) ⊂ T_lin = T_R1 (affine).
- **T_mono:** E₂± ⊂ T_mono, and T_lin ∩ T_mono = E₂±.
- **Admissible:** 𝕃_T^adm = {T_0, T_tr, E₂±, T_caus, T_lin, T_mono}.
- **Excluded:**
  - T_join = ⟨T_lin ∪ T_mono⟩: no claim; expected to trivialize ε.
  - T_univ: in GRAVEYARD, because it trivializes ε.
- **The R1 ladder stays closed.** No Stage-3 step adds a tier, a distance, or an ε value for any class outside {T_lin, T_mono}.

## 2. Frozen finite representation

**Ch1. Resolutions.**

| | r★ (scoring) | r★★ (refinement) |
|---|---|---|
| Record grid size k | 3 | 4 |
| Record channels d_rec | 1, or 2 if the card declares a two-channel carrier | as at r★ |
| Cumulant order m | 4 | 5 |
| Protocols A | {a₀, a₊, a₋} | {a₀, a₊, a₋, a₊₊} |
| Coordinates per protocol, D(n, m) with n = k·d_rec | C(n+m, m) − 1 | C(n+m, m) − 1 |
| Chart dimension d_r = (size of A)·D − 2n | 3·34 − 6 = 96 (d_rec = 1) | 4·125 − 8 = 492 (d_rec = 1) |

**Ch2. Protocol templates.**
- **Grid:** t_i = t₁ + (i−1)Δ.
- **Pulse shape φ:** φ(t) = 0 for t ≤ t₁, and φ(t) = (t − t₁)/(t_k − t₁) on (t₁, t_k].
- **Protocols:**
  - a₀: no intervention (reference clamp);
  - a_±: the path ±αφ;
  - a₊₊: the path 2αφ.
- **Scales:**
  - α = 1, in units of the null-protocol standard deviation of the S-channel.
  - Δ and the S-channel scale come from Ξ (temporality earned, FR7), or else are priced constants.
- **Uniformity:** one template-realization map serves every solution. It is a priced input.
- **Built-in control:** t₁ is a pre-intervention time by construction. This is the exact causality control (S1).

**Ch3. Γ-chart c_r(Γ).**
- Coordinates: the joint cumulants κ_a^{(j)} of Y_a, for j = 1, …, m.
- They are standardized coordinatewise by the null protocol's means and standard deviations. The 2n null-protocol normalization coordinates are therefore fixed and removed.
- Response tensors (finite differences across α) are linear functions of these coordinates. They are not extra freedom.

**Ch4. Finite-alphabet variant.**
- If records are finite-valued, the chart is ∏_a Δ(𝒴), with 𝒴 = [q]ⁿ and q = 3.
- ε⁽¹⁾ is defined only after a declared embedding into ℝⁿ, which is priced as metric vocabulary.
- ε⁽²⁾ = ⊥.

**Ch5. ε augmentation.**
- e(Γ) := (ε⁽¹⁾(Γ), ε⁽²⁾(Γ)) ∈ [0, 2]², computed from the full laws, not from c_r. The truncated coordinates do not determine ε.
- The augmented chart is χ̃_r(Π, T, Γ) := (Π, T, c_r(Γ), e(Γ)).

**Ch6. Window and mesh.**
- Continuous coordinates live in B_r = [−4, 4]^{d_r} × [0, 2]². Points outside are clipped to the boundary.
- The mesh is dyadic, with spacing 2^(−p).
- **p★ = 10.** Sensitivity is reported at p = 6 and p = 16.

**Ch7. Certification.**
- All computations use exact rational or rigorous interval arithmetic.
- ε is enclosed in an interval [ε_lo, ε_hi]:
  - ε_lo is the larger of the witness bounds (Theorem F, per-witness forms) and ½·max pairwise d_q;
  - ε_hi = max pairwise d_q (Theorem A(ii));
  - d_q itself is enclosed by rigorous optimization over the compact residual group.
- "Certified nonzero" means the enclosure excludes [−2^(−p★), 2^(−p★)] in normalized units.
- Monte Carlo and plug-in estimates are evidence grade only.

**Ch8. Truncation robustness.** Every score is computed at both r★ and r★★. A relation counts only if all three hold:
- its r★★ form restricts to its r★ form;
- every certificate holds at both resolutions;
- its certified codimension at r★★ is at least its codimension at r★.

A relation present at r★ and absent at r★★ is a **truncation artifact** and scores zero.

## 3. Baseline freedom spaces (item 1; A2, A3)

**B1. The three axes.**
- **𝒜_Π(Ξ)** := {persistent μ as in O4} / Aut(Ξ), computed on the carrier V_Ξ of each realized solution.
  - The modeler-supplied cut of standard physics is persistent, so persistence is built into the baseline.
  - Persistence is therefore a gate (§13.4), never a credit.
- **𝒜_T** := 𝕃_T^adm, which has 6 points.
- **𝒜_Γ(r)** := the c_r-image of all families (P_a), a ∈ A_r, of probability laws on ℝⁿ with finite moments of order m. ε⁽²⁾ = ⊥ wherever a margin has atoms.

**B2. ε is derived (A2).**
- The baseline is the graph 𝒢_r := {χ̃_r(Π, T, Γ) : Π ∈ 𝒜_Π, T ∈ 𝒜_T, Γ ∈ 𝒜_Γ}.
- 𝒜_ε := {ε[Γ, T] : Γ ∈ 𝒜_Γ, T ∈ {T_lin, T_mono}} ⊆ [0, 2] is the image of 𝒜_Γ × 𝒜_T. It is never a free axis.
- Freedom is always counted on 𝒢_r. So e contributes only the directions that c_r(Γ) does not already determine.
- Consequence: every relation that holds on all of 𝒢_r — every consequence of ε's definition — has zero freedom reduction by construction.

**B3. The standard package (A3).**

| | Content | How it is imposed |
|---|---|---|
| S1 Causality | Non-anticipation. On the chart: the law of Y(t₁) is equal across protocols, giving D(d_rec, m) equalities per non-null protocol | Explicit equalities, and through the model class |
| S2 Positivity | Each P_a is a probability law: moment matrices are PSD up to order ⌊m/2⌋; ε ∈ [0, 2] | Explicit inequalities, and through the model class |
| S3 KMS/FDT | Gibbs/KMS reference with Hamiltonian coupling. Includes the whole fluctuation–response hierarchy (linear FDT, nonlinear FDRs, higher-order Kubo response), plus fluctuation theorems when a Gibbs initial ensemble is present | Model class only: grid-level FDR equalities are not exact on a coarse grid |
| S4 Onsager–Casimir | Reciprocity of cross-responses; time-reversal symmetry, with parities, of the equilibrium reference | Model class; also explicit cross-symmetry equalities when d_rec = 2 and swapped protocols are present |
| S5 Conservation | Conserved quantities and sum rules of the standard model | Model class |

**B4. Standard model class 𝔐_std(ρ), by regime class ρ.**
- **G-cl.** Finite classical Hamiltonian systems S+E with a Gibbs reference, clamped-path intervention through a Hamiltonian coupling term, and records through a fixed readout of the E state.
- **G-q.** Finite-dimensional quantum systems with a KMS reference, Hamiltonian coupling, and records through a declared fixed measurement model: projective at grid times, or a fixed weak continuous measurement.
- **N.** Either of:
  - finite Markov jump or diffusion processes with local detailed balance;
  - Hamiltonian systems with a non-Gibbs reference (for example, several temperatures).

  The same intervention and record conventions apply.
- **X.** Exogenous environments: the law of E does not depend on the protocol, and only T-maps depend on the protocol. This is the R1 null class.
- **0.** The union of all the above.

Each class is closed under independent juxtaposition and Hamiltonian coupling of its members. Its members satisfy S1–S5 by construction, so every implied relation (FDT, nonlinear FDRs, reciprocity, sum rules) holds on their images.

**B5. The baseline after standard theory.**
- 𝒜^std(ρ) := closure of χ̃_r(𝔐_std(ρ)), intersected with the explicit S1 and S2 constraints.
- 𝒜^std(ρ) ⊆ 𝒢_r.

**B6. Admissible and hostile regimes.**
- A regime ρ is **admissible** for a realized point x if either:
  - **(a)** the card's own construction satisfies ρ's hypotheses at x; or
  - **(b)** the card or the hostile auditor exhibits some M ∈ 𝔐_std(ρ) with χ̃_r(M) within one mesh cell of x.
- Model classes are ordered by inclusion: G-cl, G-q ⊂ N ⊂ 0, and X ⊂ 0.
- The **hostile fiber** for x is the admissible ρ that minimizes the scored reduction of §4. The auditor may refine ρ by any parameter of the exhibiting model that the chart can identify.

**B7. Computing dim 𝒜^std(ρ) (two-sided; the hostile side is scored).**
- **Upper bound:** dim_ub := d_r − rank(S1 equalities) − rank(explicit S4 equalities, if present) + the number of components of e that are defined.
- **Lower bound:** dim_lb := the maximum, over exhibited standard families M_θ ⊆ 𝔐_std(ρ), of the certified rank of D_θ χ̃_r(M_θ).
  - Exhibited families are the hostile battery HB (§13.3), plus any family that the card or the auditor proves standard.
- **Scored:** dim_lb. **Reported:** the gap dim_ub − dim_lb.
- Exhibiting more standard families can only raise dim_lb.

**B8. Not in the baseline:**
- structure specific to any card;
- unobservable structure internal to Ξ;
- persistence credit;
- anything outside the chart.

## 4. Freedom reduction (the measurable quantity)

**F1. Freedom functional.** For S ⊆ 𝒢_r:
- F_p(S) := log₂ N_p(S);
- N_p(S) is the number of (discrete value, mesh cell) pairs within B_r that S meets.

**F2. Leading order.** Suppose S is a finite union of bounded semialgebraic or subanalytic pieces of top dimension d, with M discrete labels.
- Then F_p(S) = d·p + log₂ M + O(1) as p → ∞.
- So freedom reduction = codimension × p, plus discrete bits, plus a log-volume term.

**F3. Scored reduction of S ⊆ S₀.**

ΔF★(S | S₀) := p★·(dim_lb S₀ − dim_ub S) + min(16, log₂ M_Π(S₀) − log₂ M_Π(S)) + (log₂ M_T(S₀) − log₂ M_T(S))

- The Π term is computed per realized Ξ, modulo Aut(Ξ), and capped at 16 bits per instance.
- The T term is at most log₂ 6 ≈ 2.585 bits. It is 0 if T_Π ∉ 𝕃_T^adm.
- Log-volume reductions (restrictions of codimension 0) are reported, not scored.

**F4. Realized set.**
- 𝓡_𝒦 := χ̃_r(G_𝒦(Sol(𝒦))).
- The fiber is 𝓡_𝒦(ρ) := {x ∈ 𝓡_𝒦 : ρ is admissible for x}.
- Required: 𝓡_𝒦 satisfies S1 and S2 explicitly.
- Required: wherever a card's solution meets a standard class's hypotheses, the harness confirms the class's implemented exact consequences.
- A violation means CARD-INCONSISTENT.

**F5. dim_ub(𝓡_𝒦(ρ)).**
- This is the certified upper bound obtained from the card's count of the moduli of Sol at ρ, through the chart map.
- Without a certified bound, dim_ub := dim_ub(𝒜^std(ρ)), so no continuous credit is earned.

**F6. Instance score.**
- ΔF_i := the minimum, over hostile admissible ρ in the instance's lock fiber, of ΔF★(𝓡_𝒦(ρ) | 𝒜^std(ρ)), computed at r★.
- The r★★ value is also reported, and it must be at least the r★ value.

**F7. Instances.**
- Before scoring, the card declares a set I_𝒦 of at most 3 **structurally distinct** instances.
- Distinct instances differ in regime class or in the class of carrier structure. They are not related by isomorphism, relabeling, scaling, or a change of resolution.
- Copies score once.

## 5. Qualifying relations: the lock target (A2, A4)

**Q1. Form.**
- A relation is a map ℛ: 𝒢_r → ℝ^c with c ≥ 1, in normalized chart units, stated at both r★ and r★★. Its zero set is Z_ℛ := ℛ⁻¹(0).
- ℛ must be defined on all of 𝒢_r.
- Where ℛ uses ε_R and T ∉ {T_lin, T_mono}:
  - ℛ must be stated through sep_T, or declared undefined there;
  - such points are never counted as satisfying ℛ.
- Only equality relations qualify as locks. Inequalities count only through §4, and only as reported quantities.
- Scoring depends only on Z_ℛ.

**Q2. Certificate D (non-definitional).**
- Required: a point x ∈ 𝒢_r with ℛ(x) certified nonzero. Equivalently, ℛ fails somewhere in the baseline product space once ε is substituted by its definition.
- A relation that holds on all of 𝒢_r is **DEFINITIONAL** and earns nothing. Examples:
  - ε ≡ 0 on single-protocol families;
  - T-invariance of ε;
  - ½·diam ≤ ε ≤ diam;
  - the Theorem F bounds;
  - chart conventions.

**Q3. Certificate S (not imposed by standard theory).**
- Required, in every minimal admissible regime class of every lock fiber: an exhibited model M ∈ 𝔐_std(ρ) with ℛ(χ̃_r(M)) certified nonzero.
- If no standard model in the hostile fiber violates ℛ, then ℛ is **STANDARD-IMPLIED** and earns nothing (A3).
  - The canonical case is D5's Kubo/FDT regime restatement: BRI1's Tier-1 value is predicted from undriven 4-point correlations.
- S implies D. Both are reported.

**Q4. Certificate C (codimension).**
- Required: a standard family M_θ ⊆ 𝔐_std(ρ) with χ̃_r(M_θ₀) ∈ Z_ℛ and certified rank D_θ(ℛ ∘ χ̃_r ∘ M)(θ₀) ≥ c_ℛ.
- Then Z_ℛ ∩ 𝒜^std(ρ) has codimension ≥ c_ℛ near that point.
- For components that involve ε (which is not smooth), a certified sign change along a path inside the family replaces the rank condition. Each such component counts 1.
- Required: c_ℛ ≥ 1.

**Q5. Certificate J (jointness: interface and response structure are not independent).**
- Write x = (I, R), with I = (Π, T) and R = (c_r(Γ), e(Γ)).
- Required, all certified:
  - two points x = (I, R) and x′ = (I′, R′) in Z_ℛ ∩ 𝒜^std(ρ);
  - their cross point (I, R′) lies in 𝒜^std(ρ) ∖ Z_ℛ.
- This proves that Z_ℛ ∩ 𝒜^std(ρ) is not the product of an interface-side constraint and a response-side constraint.
- In other words, ℛ restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R (A2).
- A product relation is **NONJOINT**. It is not a lock, although it may still count in §4.

**Q6. Certificate F (forcing).**
- Required: 𝓡_𝒦(ρ) ⊆ Z_ℛ in every lock fiber, at r★ and r★★. Acceptable forms:
  - a proof (DERIVED);
  - an exhaustive certified computation over the card's solution moduli (COMPUTED).
- Sampling does not suffice.

**Q7. Response scope (A4).** Every relation declares one scope.
- **Scope Q: quotient-irreducible back-reaction, detected by ε_R.**
  - Test: ℛ is invariant under the protocolwise action of T_Π^A on Γ. This is certified symbolically, or by exact invariance of the chart coordinates ℛ uses.
  - Measurement: only through ε_R or T_Π-invariants.
- **Scope G: response in general.**
  - ℛ depends on structure that T_Π can explain: mean, linear, Gaussian or affine response.
  - Its hostile baseline adds D5's reverse-direction relations to 𝒜^std: Kubo/FDT (comparator 1) and the GLE (comparator 2).
  - ε_R may not be its only measured quantity, because ε_R annihilates every T-explainable response.
- **Mixed relations** are split, and each component is scored under its own scope.
- **In every scope:**
  - R1-NULL is never evidence of "no response" (R1_SYNTHESIS §7.3).
  - A scope-Q relation can be neither confirmed nor refuted by linear-response data.

**Q8. Non-vacuity (scope Q).**
- Required: in each lock fiber, some x ∈ 𝓡_𝒦(ρ) has ε_R certified > 0.
- A scope-Q relation on a realized set where ε_R ≡ 0 (the linear/Gaussian blind spot) is **VACUOUS**.

**Q9. ε values.**
- A relation that uses an ε value requires T_Π ∈ {T_lin, T_mono}.
- For any other T_Π
in 𝕃_T^adm, only sep_T predicates may appear.
- A relation evaluated at T_join or T_univ is void.

**Q10. Neutrality.**
- The charter preregisters no target relation, sign, monotonicity or functional form.
- If a card's ℛ★ is signed or monotone, the sign and form must come from 𝒦 (G2-11).
- A tradeoff or sign supplied as input is a supplied target relation (§8 NR5).

**Q11. Named lock.**
- Each card names exactly one primary lock ℛ★ at freeze, with its lock fibers, scope and claimed codimension.
- The card may name further relations. They are scored separately and can never replace ℛ★ after scoring starts.

## 6. Compression accounting and information price (item 3)

**P1. Base language.**
- L₀ (RULES rule 2): finite sets, maps, interventions, conditional response, composition, logic.
- Frozen token alphabet Σ_L₀ with 64 tokens (Appendix B.1).
- Prefix (Polish) notation: arity is implicit, so no brackets are needed.

**P2. Statement length.** For an expression X:

L_stmt(X) := 6·#tokens(X) + Σ over variable occurrences of ⌈log₂(v_X + 1)⌉ + Σ over literals of ℓ(lit)

- v_X is the number of distinct variables in X.
- ℓ(n) is the Elias-δ length of n+1, for a natural number n.
- ℓ(n/d) := ℓ(n) + ℓ(d) + 1, for a rational.
- A real constant costs p + ℓ(|exponent|) + 1 bits (mantissa at the precision p under evaluation, exponent, sign).
- A defined symbol costs its definition once, then ⌈log₂(#definitions + 1)⌉ bits per use.

**P3. Inputs (L_in).** Every supplied datum is encoded with the same code. This covers:
- 𝒞 itself;
- carrier size, initial data, couplings, constants, scales, time unit;
- the template-realization map and the selectivity-interface map.

A symbol that encodes a table costs the whole table (SD0 compactness §1).

**P4. Priced vocabulary.** Each vocabulary item v used costs P_v := max(L_stmt(def_v), ΔF_tgt(v)).
- The items are the RULES list (Hilbert space, orthogonality/inner product, quantum set, GPT cone, Born rule, metric) plus the Stage-3 items in Appendix B.2.
- def_v is the canonical definition in Appendix B.2.
- ΔF_tgt(v) is the sum of:
  - the scored reduction (§4) that v alone imposes on 𝒢_r;
  - the SB-1 distinctions (§13.1) that v alone settles.
- "Alone" means the card with every non-vocabulary clause removed.

**P5. Supplied protected structures (§8 NR0), declared.** Each costs P_X := max(L_stmt(X), ΔF_tgt(X)).
- Here ΔF_tgt is computed against 𝒢_r, the pre-standard product, not against 𝒜^std.
- Rationale: R1_SYNTHESIS §12 requires these structures to be derived, so a card can never earn compression from a structure it supplies.

**P6. Selection tax.**
- τ_sel := log₂(1 + n_drafts).
- n_drafts counts the 𝒦 drafts in any form (any agent, any panel) logged between the charter freeze and this card's freeze.

**P7. Per-control constants (SD0 §4, hazard 3).**
- A constant whose value matters for only one battery item or one instance is a per-instance parameter.
- It is priced in that instance, and that item's distinction is not credited.

**P8. Price.** Price(𝒦) := L_stmt(𝒦) + L_in + Σ_v P_v + Σ_X P_X + τ_sel.

**P9. Two-part code (comparison against the baseline description of the same structures).** For instance i with hostile fiber ρ_i:
- **Baseline description:** L_base(i) := F_p(𝒜^std(ρ_i)). This is what standard physics must specify, with Π and T supplied by the modeler.
- **Card description:** L_𝒦(i) := F_p(𝓡_𝒦(ρ_i)). This is what remains to specify once 𝒦 holds.
- Regime data appear in both descriptions and cancel.
- **ΔL := Σ_{i∈I_𝒦} [L_base(i) − L_𝒦(i)] + D_sel − Price(𝒦) = Σ_i ΔF_i + D_sel − Price(𝒦).** The ΔF_i are scored with the hostile dimension bounds of §4.

**P10. D_sel.**
- One bit for each SB-1 anchor verdict reproduced, under SD0's rule.
- A distinction is not counted if it is implied by other counted distinctions, or by a structural fact in the SD0 record. Example: SD0 T1, every table that is not strongly contextual survives arc consistency.
- Holdout successes are tallied separately and never enter ΔL.

**P11. Mandatory ledger.**
- One row per item, with columns: item; class (statement / input / vocabulary / supplied protected / selection); L₀ encoding; bits; ΔF_tgt where applicable; rule applied.
- Then:
  - ΔF_i per instance (the dim_lb, dim_ub, Π and T terms);
  - D_sel;
  - Price;
  - ΔL at p = 6, 10 and 16, with real constants repriced at each p.

**P12. Disputes.**
- An ambiguity is resolved against the card (0.2).
- An unresolved dispute goes to the owner with both computations.

## 7. Success criterion (item 2)

A card meets the criterion only if all of the following hold.

- **SC1. Nontrivial freedom reduction.**
  - For every instance, dim_lb 𝒜^std − dim_ub 𝓡_𝒦 ≥ 1 on the response side, after standard theory.
  - ℛ★ holds Certificates D, S, C (with c ≥ 1), J and F, has a declared scope, and (for scope Q) is non-vacuous (V), at both r★ and r★★.
- **SC2. Positive compression.**
  - ΔL ≥ p★ bits at p★ = 10 (the margin is the price of one real coordinate).
  - ΔL > 0 at p = 16.
  - The value at p = 6 is reported.
- **SC3. Measurable consequence.** ℛ★'s coordinates are operationally defined (C12), with:
  - an estimator;
  - the predicted relation and its uncertainty;
  - the effect size against the nearest certified standard witness;
  - n_req, the sample size needed.

  Grades:
  - **FEASIBLE:** n_req ≤ 10⁹ per protocol at α = 0.01 and power 0.9.
  - **IN-PRINCIPLE:** passes Stage 3, but Stage 5 then needs either a feasible holdout path or a sealed holdout on established system data.
- **SC4. Never credited toward SC1–SC3:**
  - definitional relations;
  - standard-implied relations;
  - D5's reverse-direction relations;
  - consequences of supplied structures;
  - everything listed in §18.

## 8. Nonrelocation (item 4)

**NR0. Protected structures.**
- (1) The partition Π.
- (2) The carrier: which E state variable counts as the environment (including the instantaneous-versus-initial choice, D5 Remark D3), and the protocol invariance of the readout.
- (3) The readout class [h].
- (4) The interface class T.
- (5) Gibbs/KMS/FDT structure: invariant or thermal measures, temperature, energy-weighted measures, detailed balance, KMS, FDT kernels.
- (6) The target relation ℛ★, or any relation that implies it.
- Never inputs (STATE.md): memory, viscoelasticity, crystalline order.
- "Hidden" means present in 𝒦, 𝒞 or any input without being declared.

**NR1. Vocabulary screen.**
- The harness lists every symbol of 𝒦, 𝒞 and the inputs.
- It flags any symbol that names or encodes a protected structure. Examples:
  - typed sorts that pre-split the relata;
  - group actions on record space;
  - readout maps;
  - measures, weights or temperatures;
  - target-level coordinates.
- Flagged and declared → **SUPPLIED** (priced under P5). Flagged and undeclared → **RELOCATED**.

**NR2. Generation grade for Π and the carrier.**
- **GENERATED-STRONG.** There is an input instance whose automorphism group acts transitively on V_Ξ, such that:
  - every solution has a persistent nontrivial Π;
  - so Π is necessarily not invariant under the input's symmetries;
  - and at least one lock fiber is drawn from such instances.

  Then Π is provably not a function of the inputs.
- **GENERATED-WEAK.** Otherwise, no reader in the battery RB (NR9) recovers Π from the inputs at cost ≤ ½·F_Π, within drift δ_drift. Here F_Π := log₂ size(𝒜_Π(Ξ)).
- **Otherwise** RELOCATED, or SUPPLIED if declared.

**NR3. T and [h].** These are GENERATED if and only if all of:
- **(a)** no input names a group action on records or a readout class;
- **(b)** the card derives [h]_{T_Π} as the readout redundancy of its own observation map, and the harness verifies T_Π's generators on the chart;
- **(c)** T_Π ≠ Aut(R) for any record-space structure R that the inputs supply;
- **(d)** the carrier condition h_a ∈ [h]_{T_Π} holds for every protocol in A_{r★★}, and the environment-state designation is derived from 𝒦, not from the records.
  - Records cannot certify the carrier (R1_SYNTHESIS §3; D5 D1′).

**NR4. Gibbs/FDT.**
- GENERATED only if no input contains any NR0(5) item.
- Any Gibbs/KMS property of the solutions is an output. It is recorded as a Stage-6 consistency item and credited zero freedom, because it is already in 𝒜^std.

**NR5. Target relation.**
- Put 𝒦 in clause normal form.
- A clause is **target-level** if it mentions records, chart coordinates, ε, interface maps, partition labels or readouts.
- If the target-level clauses together with the standard package imply ℛ★ on 𝒢_r, the lock is RELOCATED.
- A card with no target-level clauses passes NR5 by construction.

**NR6. Mode selection.**
- A card whose observation map uses protocol-dependent readouts h_a ∉ [h]_{T_Π} receives R1's verdict MODE SELECTION for every relation that involves ε_R.
- The product-latent construction (Prop. E / D1) is a harness control, and it must return MODE SELECTION.

**NR7. No promissory structure.**
- Every structure claimed as generated must be computed by the card's frozen algorithms at r★ and r★★.
- "To be derived later" means SUPPLIED. No follow-up campaign may supply it (§14).

**NR8. Labels and consequences.** Each protected item is labeled GENERATED-STRONG, GENERATED-WEAK, SUPPLIED or RELOCATED.
- RELOCATED anywhere → CARD-RELOCATED.
- Π, carrier, [h] or T_Π SUPPLIED → CARD-NONGENERATIVE, which fails Stage-4 differentiation by definition.
- Gibbs/FDT SUPPLIED, or ℛ★-implying clauses SUPPLIED → priced under P5, and the relations they imply score zero.

**NR9. Reader battery RB.** A reader's cost is the template index plus its parameters, in L₀ bits. The templates are:
- **RB1:** read any input label or sort.
- **RB2:** threshold or top-n read of any input weight.
- **RB3:** connected components of any input relation or of its complement, k-cores, or degree thresholds.
- **RB4:** blocks of the finest block (module) decomposition of any input matrix or relation.
- **RB5:** a union of orbits of Aut(inputs).
- **RB6:** a ball of any radius around any input-designated element, in any input distance.

A reader succeeds if it reproduces Π within δ_drift on every solution instance of the lock fibers.

## 9. Required card contents (item 6, A4)

Each card is one file, committed with its SHA recorded before any scoring.

- **C1. Identity.** Card number, freeze SHA, n_drafts, and the distinctness statement (§10).
- **C2. Exact law.**
  - The general statement, in L₀ plus priced vocabulary, and its clause normal form.
  - Its instantiations at r★ and r★★, which must be uniform. No case splits on scenario names, party or setting counts, dimensions, sizes or resolution (SD0 firewall 3).
- **C3. Ontology declarations.**
  - Ξ's type and the carrier V_Ξ.
  - The meaning of 𝒞 (FR11).
  - Composition or gluing as an explicit act (FR2).
  - The source of temporal order and of the time unit (FR7).
  - The compatibility scope (FR6).
  - Dependencies on subsidiary theories (FR14).
- **C4. Decidability.**
  - A decision procedure, with a resource bound, for Sol membership and for every chain map, at r★ and r★★.
  - The approximation status (exact, outer or inner) of any target whose exact form may be undecidable (§13.2).
- **C5. Information-price ledger** (P11).
- **C6. Generated structures.** Π, carrier, [h]_{T_Π}, T_Π (with its placement in 𝕃_T), Γ_Π and ε_R, each with its algorithm or proof and its NR8 label.
- **C7. Primary lock ℛ★.** Its formula, normalization, coordinates, lock fibers, the instance set I_𝒦, and the claimed codimension.
- **C8. Response scope** of every relation (Q7), with non-vacuity (Q8).
- **C9. Certificates** D, S, C, J, F and V, as code plus machine-readable output.
- **C10. Freedom and compression.** ΔF_i; dim_lb and dim_ub with their gap; D_sel; Price; ΔL at p = 6, 10 and 16.
- **C11. Hostile baseline comparison.**
  - (a) The hostile fibers, with the standard models that exhibit them.
  - (b) The HB witnesses; the HB family closest to 𝓡_𝒦; and why ℛ★ is not a consequence of that family.
  - (c) D5's reverse-direction relations: the FDT prediction of the leading Tier-1 ε from undriven 4-point correlations; GLE detection of linear back-reaction; process-tensor signalling. ℛ★ must be none of these, and must not be implied by them in its lock fibers.
  - (d) The consistency family (§13.2), where it applies.
- **C12. Measurable target.**
  - The operational definition of each coordinate: which S channel is intervened, which E readout is recorded, and what calibration fixes T_Π.
  - The estimator. For ε, use per-witness forms; no plug-in d_BL at n ≥ 3 (D4).
  - The predicted relation with its uncertainty.
  - The effect size against the nearest certified standard witness.
  - n_req, and the SC3 grade.
  - The holdout class, and the declared scope domain where ℛ★ must hold.
- **C13. Kill conditions.**
  - The universal list K-U1 to K-U8 below.
  - At least two card-specific kill conditions: one decidable at Stage 4 without new theory, and one empirical.
- **C14. Selectivity interface.**
  - A uniform map from Sol to empirical models on the SB-1 scenarios.
  - The declared target object: either possibilistic no-signalling (pNS) support tables, or exact-support-realizable supports (SD0 reconnaissance, finding 3).
  - The declared G0-trichotomy branch (FR15).
  - The harness computes the verdicts after the freeze.
- **C15. FR1–FR15 table** (§16). Each requirement is marked satisfied, SUPPLIED, or not applicable with a reason. No FR is claimed discharged without an external check.
- **C16. Non-claims.**
- **Optional C17.** A cross-sector transfer target (§12).

A missing or empty field → **CARD-INCOMPLETE**. The card still counts against the budget.

**Universal kill conditions**
- **K-U1:** Sol is empty at r★ or r★★.
- **K-U2:** 𝓡_𝒦 violates S1 or S2, or violates the standard consequences of a regime whose hypotheses the card's own construction meets.
- **K-U3:** ℛ★ fails D, S, C, J or F.
- **K-U4:** a scope-Q ℛ★ is vacuous, or is evaluated at a void T (Q9).
- **K-U5:** any protected structure is RELOCATED.
- **K-U6:** the SB-1 minimal gate fails.
- **K-U7:** ΔL < p★ at p★, or ΔL ≤ 0 at p = 16.
- **K-U8:** a holdout violates ℛ★ beyond the declared error, inside the declared scope (Stage 5).

## 10. Budget and distinctness (item 5)

- **BD1. Budget.** At most three cards are frozen in Stage 3. Every frozen card counts: INCOMPLETE, VARIANT and withdrawn cards included.
- **BD2. Genuinely distinct.** Card K_j is distinct from an earlier card K_i only if all three hold:
  - **(a)** their clause normal forms differ by more than numeric literals, thresholds, renaming, or rewriting into an equivalent form;
  - **(b)** either a certified point lies in the symmetric difference of their realized sets in some lock fiber, or their SB-1 verdict vectors differ;
  - **(c)** their primary locks have different zero sets on 𝒜^std, shown by a certified point in Z_ℛ★i Δ Z_ℛ★j.

  Otherwise it is **CARD-VARIANT**.
- **BD3. Modifications.**
  - Any modification of a frozen card is a new card (SD0 §3.6).
  - A modification made after any score of the earlier card was visible is labeled REPAIR.
- **BD4. Draft ledger.**
  - Every draft, in any form, is logged with a hash and a time before it is discarded or developed.
  - If a draft is found unlogged later, the affected card is repriced with the corrected n_drafts and flagged.
- **BD5. Adaptive design.**
  - A card may be designed after earlier cards were scored.
  - Each card is frozen before its own scoring.
  - No card changes the charter.
- **BD6. Owner's pick.**
  - The owner picks only among CARD-ADMISSIBLE cards.
  - If the picked card fails Stage 4 or 5, the owner may take another frozen admissible card, unmodified.
  - There is no fourth card.

## 11. Originality (item 7)

- **OR1. Components.** Familiar component theories are allowed and expected. A component's familiarity is never a defect and never a credit.
- **OR2. Assembled law.** Novelty is judged only for the assembled law: 𝒦, with its generated chain and ℛ★.
- **OR3. Preregistered verdict categories** (D5 pattern):
  - **RESTATED:** an existing framework under new names, with the same realized structures on the batteries and the same ℛ★.
  - **KNOWN COMPONENTS, NEW ASSEMBLY:** the assembly is new, but some existing framework imposes ℛ★. Bankable as COMPRESSIVE if ΔL > 0, but not a lock.
  - **DISTINCTIVE:** ℛ★ survives every comparator. Required for the Stage-5 lock.

  Procedure:
  - Each comparator gets an analyst and a skeptic, and the skeptic is instructed to argue RESTATED.
  - The more conservative of the two verdicts governs.
  - Mathematics and physical interpretation are classified separately.
- **OR4. Comparator corpus.** These are comparator candidates only. Each is verified against primary sources at audit time, and none is load-bearing before then.
  - (i) D5's ten comparators.
  - (ii) Response theory: Kubo; nonlinear FDRs (Bochkov–Kuzovlev); Jarzynski, Crooks, Gallavotti–Cohen; GLE / Mori–Zwanzig; Ford–Kac–Mazur / Caldeira–Leggett.
  - (iii) Open systems: GKSL and Redfield equations; process tensors; einselection / quantum Darwinism.
  - (iv) Frameworks that derive subsystem partitions or boundaries:
    - observable-induced tensor-product structures (Zanardi; Zanardi–Lidar–Lloyd);
    - quantum mereology (Carroll–Singh);
    - Markov-blanket formalisms (Pearl; Friston);
    - near-decomposability (Simon–Ando);
    - lumpability (Kemeny–Snell).
  - (v) Readout classes: IRT linking; Stevens scale types; interventional-CRL identifiability classes; measurement invariance (R1_SYNTHESIS §12 item 1).
  - (vi) The correlation sector:
    - Abramsky–Brandenburger;
    - bounded-width CSP and operator assignments (Atserias–Kolaitis–Severini; Bulatov–Živný; Ciardo; Ó Conghaile);
    - Slofstra;
    - Local Orthogonality;
    - reconstructions (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller);
    - JGBB polygon theories.
- **OR5. Timing.**
  - At Stage 3: the cheap screens (Certificate S, HB, reverse-direction relations, consistency family).
  - The full assembled-law audit runs on the owner-picked card and finishes before the Stage-5 verdict.
  - No novelty claim is made before then (RULES rule 7).
- **OR6. Graveyard.**
  - A card whose selectivity or partition mechanism reduces, on the batteries, to a GRAVEYARD entry is **CARD-GRAVEYARD**.
  - The entries include:
    - forbidding strong contextuality;
    - counting settings, parties, capacity or dimension;
    - ASP as a new law;
    - pairwise or sub-cover locality, single-context-deletion solvability, cohomology or AvN classes;
    - maximal T read literally;
    - latent dimension ≤ k;
    - the constructor-theory (CT)-parallel embedding;
    - support determination as a standalone line.

## 12. Cross-sector gold standard (item 8)

- **XS1. Sectors** are frozen coordinate blocks:
  - Q: correlation and contextuality data, of the SB-1 type;
  - Θ: response and reciprocity, the chart 𝒢_r;
  - 𝔊: gravitational (Stage 6);
  - any further sector the owner declares.
- **XS2. Independence.**
  - Sectors A and B are otherwise independent if the standard baseline is a product on their coordinates.
  - This is certified by standard model pairs that realize every combination in a product box of positive dimension around the instance.
- **XS3. Parameter transfer.**
  - θ, the vector of 𝒦's parameters (priced), is fixed from sector-A data only, by a fitting procedure frozen in the card.
  - The sector-B prediction is y_B = f_B(θ̂_A), with uncertainty propagated from the fit.
  - No 𝒦 parameter is refit in B.
  - Nuisance parameters standard to B may be fit only if they are declared and priced per instance.
- **XS4. Transfer gain.**
  - TG := F_p(𝒜^std_B) − F_p(𝓡_{𝒦,B}(θ̂_A)) ≥ p★.
  - It must come with a certificate that standard theory gives zero transfer: a standard pair (M_A, M_B) consistent with the A data that violates the B prediction.
- **XS5. Status.**
  - CROSS-SECTOR is awarded only after a sealed test of the B prediction under the Stage-5 rules.
  - Analogy, shared vocabulary or shared formalism never counts (RULES rule 3).
  - Stage 3 claims no CROSS-SECTOR status.
- **XS6. Stage-6 export.**
  - ε_R is exported to a gravitational ensemble with the same quotient and distance (the frozen tiers).
  - Local back-reaction serves as the sector-A calibration only.

## 13. Batteries and gates (Stages 4–6 made concrete)

### 13.1 SB-1: selectivity battery (frozen, from the exact SD0 record)

| Item | Content | Requirement |
|---|---|---|
| SB1.1 | The 1721 possibilistically local (2,2,2) tables | ALLOW all (minimal gate) |
| SB1.2 | Hardy support (SD-K2) | ALLOW (minimal gate) |
| SB1.3 | The 8 PR boxes | FORBID all (minimal gate) |
| SB1.4 | The 240 pNS tables with no exact-support realization | Report; must agree with the declared target object |
| SB1.5 | GHZ (3,2,2); Peres–Mermin; Mermin pentagram; bipartite magic square; CEG-18; the CHTW 3×3 KS core (94 rays / 67 triads) | ALLOW all (minimal gate) |
| SB1.6 | The qubit-on-either-side hostile family (SD-K7(i)) | Graded FORBID |
| SB1.7 | The theta parity system | Graded FORBID; ALLOW makes the card OUTER |
| SB1.8 | Strong XOR-(2,3,2) (480); Specker triangle; chained-PR 6-cycle; C7 odd cycle; embedded and fine-grained PR; PR⊗PR | Graded FORBID |
| SB1.9 | The qubit vs gbit capacity pair (SD-K8) | Audit: the discriminator must not be capacity or dimension |

- **Minimal pass:**
  - SB1.1, SB1.2 and SB1.5 are all ALLOW;
  - SB1.3 is FORBID;
  - the admitted set is strictly smaller than the 2961 pNS tables;
  - the SB1.9 audit passes.
- **Grade:**
  - EXACT-ON-BATTERY if every graded item is forbidden; otherwise OUTER.
  - Under FR9, OUTER never upgrades to exact.

### 13.2 Consistency-only and decidability boundary (SD0 lessons)

- **CO1. Consistency family CF.**
  - Members: k-consistency for k = 1, 2, 3; Singleton Linear Arc-Consistency; ASP (SCOREBOARD #6).
  - Their SB-1 verdict vectors are computed before Card 1.
- **CO2. RESTATED selectivity.** If a card's SB-1 vector equals that of a CF member, or its forbid mechanism is a local-consistency refutation:
  - its selectivity is RESTATED: D_sel = 0;
  - the CSP comparators become mandatory in its audit;
  - if it also allows theta, it is OUTER.
- **CO3. Decidability.**
  - Decision procedures are required at r★ and r★★ (C4).
  - For targets whose exact form may be undecidable (quantum correlation and support families; Slofstra), the card claims only a declared outer or inner approximation.
  - A claim to characterize such a target exactly requires a proof.
- **CO4. Constraint ≠ selection (FR8).**
  - Π must be computed as an output, not merely left unforbidden.
  - A law made only of vetoes must show, through its C6 algorithm, which output its allowed set forces.

### 13.3 HB: hostile model battery (frozen) and SB-2

| ID | Family | Regime | Role |
|---|---|---|---|
| HB-1 | Harmonic bath, bilinear coupling, Gibbs; N_B ≤ 8 | G-cl | R1-NULL while responding (friction) |
| HB-2 | Duffing / BRI1-class bath, Gibbs; quartic λ ∈ [0, 2] | G-cl | Tier-1 PASS; Kubo third-cumulant response |
| HB-3 | Exogenous Gaussian (C2-G) | X | Exact zero |
| HB-4 | Exogenous affine-entry non-Gaussian (C2-NG) | X | Exact zero |
| HB-5 | Exogenous filtered non-Gaussian with calibrated filters (C2-F, C2-F′) | X | T-dependence of the zero set; non-Markov null |
| HB-6 | Markov responding environment (M-A) and its non-Markov variant (M-A′) | N | ε > 0 with and without memory |
| HB-7 | Parametric coupling to a harmonic bath | G-cl | Escapes both tiers with linear bath dynamics |
| HB-8 | Gaussian latent configural change (E2 class) | X / 0 | ε > 0 with no response |
| HB-9 | Product latent with selection readouts (Prop. E / D1) | — | MODE SELECTION control |
| HB-10 | Quantum systems of ≤ 4 qubits or qutrits; local Hamiltonians from a frozen ensemble; KMS reference; Hamiltonian coupling; fixed measurement model | G-q | Quantum standard witnesses |
| HB-11 | Two-temperature or driven steady-state baths | N | Nonequilibrium standard witnesses |
| HB-12 | Finite Markov jump processes with local detailed balance; discrete records | N / G | Discrete-record chart |

- **Frozen ranges:** β ∈ [0.25, 4]; frequencies in [0.5, 2]; couplings in [0, 1]; N_B ≤ 8.
- Members may be composed by juxtaposition or Hamiltonian coupling.
- **SB-2** records which HB members 𝓡_𝒦 contains. Its minimal requirement — some standard member forbidden in every lock fiber — is implied by Certificate S.

### 13.4 Stage-4 gates

These run on the owner-picked card. Every gate is recomputed independently by an agent that did not build the card, and checked externally before banking. Each gate result is reported to the owner (RULES checkpoint (e)).

- **G4-SEL.** The SB-1 minimal pass and its grade; CO1–CO4.
- **G4-DIF (differentiation).**
  - **D1:** Π is computed by the frozen algorithm on every lock-fiber solution.
  - **D2:** persistence (δ_drift, δ_∂) holds across A_{r★★} and the whole horizon.
  - **D3:** S and E are nonempty, and Π is not the partition into input-disconnected components.
  - **D4:** Π is GENERATED-STRONG or GENERATED-WEAK.
  - **D5:** carrier, [h] and T_Π are GENERATED, and T_Π lies in 𝕃_T^adm.
  - **D6:** Π is unchanged, within δ_drift, under relative perturbations of size 2^(−p★) applied to every numeric input, provided they preserve the input's automorphism group.
- **G4-NR.** NR1–NR9 are re-run. The reader battery is run by an agent that has not seen the card's derivation of Π.

### 13.5 Stage-5 lock

- **G5-LOCK.**
  - Certificates D, S, C, J, F and V and the declared scope are re-verified independently, at r★ and r★★.
  - The assembled-law audit returns DISTINCTIVE for ℛ★.
- **G5-HOLD.**
  - After G5-LOCK, the hostile auditor selects at least 2 holdouts. Each is:
    - a physically realized system class inside the declared scope;
    - not referenced in the card;
    - backed by established record data, or by an established model of that physical system.
  - Their hashes are committed before 𝒦's prediction is evaluated.
  - **PASS:** ℛ★ holds within the declared error on every holdout.
  - Any certified violation inside the scope triggers K-U8.
  - A preregistered prospective experiment may replace a holdout.

### 13.6 Stage 6 (pointer only)

- The same 𝒦, unmodified, must yield the quantum, thermodynamic and gravitational regimes.
- ε_R is exported with the same quotient and distance; local back-reaction is used as calibration only.
- Memory, viscoelasticity and crystalline order are checked as effective regimes after Stage 4.

## 14. Stopping rule and terminals (item 9)

**T1. Card terminals.** Each card gets exactly one terminal.
- **Screen order:**
  1. S0 completeness;
  2. S1 distinctness and graveyard;
  3. S2 decidability;
  4. S3 nonrelocation;
  5. S4 chain computation and standard consistency;
  6. S5 lock certificates;
  7. S6 freedom and compression;
  8. S7 measurability;
  9. S8 selectivity.
- All screens are run and reported. The first failing screen names the terminal.
- **Terminals:**
  - CARD-INCOMPLETE (S0);
  - CARD-VARIANT, CARD-GRAVEYARD (S1);
  - CARD-UNDECIDABLE (S2);
  - CARD-RELOCATED, CARD-NONGENERATIVE (S3);
  - CARD-INCONSISTENT (S4);
  - CARD-DEFINITIONAL, CARD-STANDARD, CARD-NONJOINT, CARD-VACUOUS, CARD-UNFORCED (S5);
  - CARD-NONCOMPRESSIVE (S6);
  - CARD-UNMEASURABLE (S7);
  - CARD-UNSELECTIVE (S8);
  - otherwise **CARD-ADMISSIBLE**.

**T2. Route terminals.**
- STAGE3-PICK: the owner picks an ADMISSIBLE card.
- STAGE3-ROUTE-TERMINATED.

**T3. Termination.** The generative route terminates when either:
- (a) the budget is spent with no ADMISSIBLE card; or
- (b) every frozen ADMISSIBLE card has failed a Stage-4 or Stage-5 gate.

Termination is recorded in GRAVEYARD, after the external check (RULES rule 8), and in STATE.

**T4. Prohibited, during Stage 3 and after termination.**
- A fourth card.
- Any "missing ingredient", "deeper prerequisite" or "foundations" campaign.
- Reopening R1 to add tiers or distances.
- Changing any frozen number, battery, chart or baseline.
- Rescoring under modified rules.
- Describing a failed card as partial progress toward a prerequisite.
- R1's open upgrades (M5, D4, Tier-2 carrier necessity, the pending external checks) are never prerequisites of any Stage-3 step.

**T5. Allowed after termination.**
- Banking DERIVED sub-results as a library, after external check (the SD0 precedent).
- A new program, but only by a new, explicit owner direction — never as a continuation of this route.

## 15. Provenance (A1: merge = provenance, not endorsement)

| Item used here | Role in this charter | Status |
|---|---|---|
| Frozen ε_R definition, T_R1, d_q^BL, verdict table, Prop. E (`82d311e`) | ε computation; carrier semantics; NR6 | Frozen pre-result; checked: Claude |
| Theorems A and C | sep_T; HB-2 calibration | DERIVED; checked |
| A-BL, F, M1–M3, Prop. G | ε enclosures (F); the Tier-2 zero set (M1) | DERIVED; external check pending |
| BRI1 Tier 2 | HB-2 Tier-2 behavior | Evidence grade (`cb81a3b` checked: Claude) |
| D5 C1–C6 and D1–D3; regime restatement; reverse-direction relations | Hostile baseline content | D5 ANALYSIS: evidence grade, not externally checked |
| SD0 counts 2961 / 1721 / 1232 / 8 and the 240 gap | SB-1 | DERIVED, exact |
| SD0 T2 (2-SAT equivalence) | Consistency-family behavior | UNRESOLVED, pending review |
| ASP (`aacbc52`) | CF member | COMPRESSIVE, known sector (#6) |

- A score that depends on a pending item is labeled "conditional on <item>".
- If an external check finds an issue, the affected scores are recomputed. Thresholds never change.
- The merge `86bf5a0` and the R1 boundary `dbfd64b` are provenance markers. They change no status.
- This charter's own freeze commit gets a CHECKS line marked pending. Nothing in the charter is banked.

## 16. FR1–FR15 map

| FR | Where the charter applies it |
|---|---|
| FR1 representation invariance | O4, O6, 0.5, Q1, NR3 |
| FR2 gluing as an explicit act | C3 |
| FR3 no inaccessible-context data | NR1: input fields are checked against the declared access |
| FR4 observer independence | O3: Π and [h] come from Ξ; counterfactual framing does not count as generation |
| FR5 no unpriced split | NR0–NR2, P5 |
| FR6 compatibility scope | C3 |
| FR7 earned temporality | Ch2, C3; the instantaneous-state designation is derived (NR3(d)) |
| FR8 constraint ≠ selection | CO4 |
| FR9 no outer→exact upgrade | §13.1 grades |
| FR10 information price | §6 |
| FR11 declared meaning of 𝒞 | O2, C3, P3 |
| FR12 convention fixes | Adopted for the SB-1 encodings |
| FR13 a deeper Γ object | Γ_Π = Obs_Π(Ξ) must be built (C6); Γ given as an empirical model counts as SUPPLIED |
| FR14 subsidiary possibility facts | C3, C15 |
| FR15 G0 trichotomy | C14 |

## 17. CHARTER TESTS

Every row is an **abstract gaming pattern** labeled CHARTER TEST. None is a physical proposal.

| ID | CHARTER TEST pattern | Caught by | Outcome |
|---|---|---|---|
| CT-01 | Input asymmetry (labels, weights, a distinguished substructure) from which Π can be read cheaply | NR2, NR9 | RELOCATED (or NONGENERATIVE) |
| CT-02 | Π supplied as two typed sorts of relata | NR1 | NONGENERATIVE |
| CT-03 | T_Π is the automorphism group of a supplied record structure | NR3(c) | NONGENERATIVE |
| CT-04 | Protocol-dependent readout, to make ε_R > 0 | NR6 | MODE SELECTION; lock void |
| CT-05 | A lock that is an identity of ε's definition or of R1's theorems | Q2 | DEFINITIONAL |
| CT-06 | A lock that follows from KMS/FDT for the reference state | Q3 under the hostile G fiber | STANDARD |
| CT-07 | A lock equal to a D5 reverse-direction relation | C11(c) | STANDARD |
| CT-08 | Regime shopping: avoiding Gibbs structure so the baseline is weaker | B6 hostile fiber | Scored against G |
| CT-09 | Separate interface and response constraints presented as one relation | Q5 | NONJOINT |
| CT-10 | A scope-Q relation on a realized set with ε_R ≡ 0 | Q8 | VACUOUS |
| CT-11 | Scope switching: scope Q declared, linear-response evidence offered; or R1-NULL read as "no response" | Q7 | Relation unscored |
| CT-12 | ε value used at a non-frozen, join or universal T | Q9 | Void |
| CT-13 | Truncation artifact | Ch8 | Zero |
| CT-14 | Inflation by grid, precision, instance copies or carrier size | Ch1, Ch6, F3 cap, F7 | No gain |
| CT-15 | A real constant tuned to make the lock hold or to flip one battery item | P2, P7 | Priced; distinction not credited |
| CT-16 | One symbol that encodes a table | P3 | Priced as the table |
| CT-17 | Many drafts, the best one frozen | P6, BD4 | Selection tax |
| CT-18 | The lock smuggled in as a clause of 𝒦 | NR5, P5 | RELOCATED; ΔL ≤ 0 |
| CT-19 | A known standard model, with its cut, readout and Gibbs ensemble, repackaged as a law | NR1, NR4, P5 | NONGENERATIVE |
| CT-20 | A consistency-only law whose battery behavior equals a CF member's | CO1, CO2, OR6 | Selectivity RESTATED or GRAVEYARD |
| CT-21 | Claimed exact characterization of a target that may be undecidable | CO3, C4 | UNDECIDABLE or OUTER |
| CT-22 | Capacity or dimension counting as the discriminator | SB1.9, OR6 | GRAVEYARD |
| CT-23 | "T_Π derived in a follow-up" | NR7, T4 | SUPPLIED; no follow-up allowed |
| CT-24 | A tradeoff or sign imposed by an input clause | Q10, NR5 | RELOCATED |
| CT-25 | Persistence obtained by pushing relata into ∂ | O4 δ_∂ | Not persistent |
| CT-26 | Baseline or battery edited after a card is seen | §19 | Forbidden |
| CT-27 | A repair variant used to evade the budget | BD1–BD3 | VARIANT; counts against the budget |
| CT-28 | A pending item cited as checked | §15 | Score labeled conditional; banking blocked |
| CT-29 | Gibbs structure smuggled in through the choice of weighting measure | NR4 | SUPPLIED |
| CT-30 | Protocols chosen so that the relation happens to hold | Ch2 frozen templates | No effect |
| CT-31 | Memory, viscoelastic or crystalline-order input | NR0 | SUPPLIED |

## 18. Not credited (consolidated)

- Relations that hold on all of 𝒢_r: consequences of ε's definition, of R1's theorems, or of chart conventions.
- Relations with no violating standard model in the hostile fiber, including KMS/FDT, Onsager, conservation and causality consequences.
- D5's reverse-direction relations.
- Deriving the standard package itself. That is Stage-6 bookkeeping only.
- Consequences of supplied structures.
- Reductions of freedom internal to Ξ that never reach the chart.
- Log-volume (inequality) reductions; they are reported only.
- Persistence. It is a gate, not a credit.
- Scope-Q relations in the ε ≡ 0 blind spot.
- ε values at non-frozen T.
- Truncation artifacts.
- Redundant instances.
- SD0-implied distinctions, structural ALLOWs, and holdout successes as design targets.
- R1-NULL read as "no response".
- Analogy as CROSS-SECTOR.
- Novelty of components.

## 19. Procedure, harness, repairs, hard stop

1. **Freeze.** Commit this charter alone, with a pending CHECKS line. Stop for owner review.
2. **Harness work order.** After owner authorization, one bounded harness work order runs, with no card in existence.
   - It implements §§2–6 and §13.
   - It is validated against the exact controls:
     - the SB-1 counts 2961 / 1721 / 1232 / 8 and the 240 gap;
     - the PR-forcing lemma;
     - ε ≡ 0 on single-protocol families;
     - the exact zeros on HB-1, HB-3, HB-4, and HB-5 under T_lin with its calibrated filters;
     - HB-9 returning MODE SELECTION;
     - the sign of BRI1's Tier-1 PASS on HB-2;
     - S1 holding exactly on every HB family;
     - the CF verdict vectors;
     - the price coder on Appendix B.
   - It also runs the CT-05, CT-06 and CT-19 patterns, built only from HB models plus supplied structure. Each must be rejected with its predicted terminal.
   - A harness defect is fixed in the harness. It never changes the charter.
3. **Cards 1–3.**
   - Log every draft in the ledger.
   - Freeze each card, score it, and have the score recomputed independently.
   - Send a report of five lines or fewer per card.
4. **Checkpoint (d).** The owner picks a card, or the route terminates.
5. **Repairs.**
   - Before Card 1: numbered repairs by owner ruling.
   - After Card 1: only owner-ruled error repairs. A repair may not loosen any threshold, battery, chart, baseline or price. It applies to all cards and triggers rescoring.

**HARD STOP.** This charter is frozen alone. No 𝒦 card is generated, frozen, scored or optimized before the owner has reviewed it.

---

## Appendix A — frozen numbers

These are the drafter's proposals. The owner may change any of them before the freeze; none may change after Card 1 is frozen.

| Symbol | Value |
|---|---|
| p★ | 10 bits; sensitivity at 6 and 16 |
| r★ | k = 3, m = 4, A = {a₀, a₊, a₋}, d_rec = 1 (or 2) |
| r★★ | k = 4, m = 5, A gains a₊₊ |
| φ, α | Linear ramp starting after t₁; α = 1 in null-protocol standard deviations |
| Window | [−4, 4] for cumulant coordinates; [0, 2] for ε |
| q (finite alphabet) | 3 |
| Certification tolerance | 2^(−p★) |
| δ_∂ / δ_drift / θ_μ | 0.10 / 0.05 / 0.9 |
| Caps | Π term 16 bits per instance; T term log₂ 6 |
| Instances | At most 3, structurally distinct |
| Size of Σ_L₀ | 64 (6 bits per token) |
| τ_sel | log₂(1 + n_drafts) |
| ΔL threshold | ≥ p★ at p★; > 0 at p = 16 |
| Codimension threshold | ≥ 1, for the realized set and for ℛ★ |
| Feasible n_req | ≤ 10⁹ per protocol at α = 0.01, power 0.9 |
| Reader cost bound | ≤ ½·F_Π |
| D6 perturbation | 2^(−p★), relative |
| Budget / holdouts | 3 cards / at least 2 holdouts |
| HB ranges | β ∈ [0.25, 4]; ω ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8; quantum ≤ 4 sites |

## Appendix B — L₀ code and vocabulary schedule

**B.1 The L₀ alphabet (64 tokens).**

| Group | Tokens | Count |
|---|---|---|
| Logic | ¬ ∧ ∨ → ↔ ∀ ∃ = ≠ ⊤ ⊥ ite | 12 |
| Sets | ∈ ⊆ ∅ singleton pair × 𝒫 card ∪ ∩ ∖ [n] | 12 |
| Maps | λ apply ∘ id image preimage inverse restrict | 8 |
| ℕ/ℚ arithmetic | 0 1 succ + − × ÷ ≤ < Σ-finite | 10 |
| Conditional response | kernel cond-prob E ⊗ marginal do law support | 8 |
| Process composition | sequential parallel contract wire | 4 |
| Structure | def var nat-literal rat-literal real-literal end | 6 |
| Reserved | — | 4 |

**B.2 Priced vocabulary.**
- **Canonical definitions** are encoded in L₀ by the harness before Card 1.
- **Price:** P_v = max(L_stmt(def_v), ΔF_tgt(v)).
- **Items:**
  - V1 metric
  - V2 inner product / orthogonality
  - V3 finite-dimensional Hilbert space and tensor product
  - V4 quantum correlation set
  - V5 GPT cone with order unit
  - V6 Born rule
  - V7 continuum analysis (ℝ, limits, exp/log)
  - V8 temporal order and time unit
  - V9 dimension or capacity parameter
  - V10 energy function / Hamiltonian
  - V11 invariant measure / temperature / Gibbs weight / detailed balance / KMS (protected)
  - V12 group action on record space (protected)
  - V13 readout map or class (protected)
  - V14 partition sorts (protected)
  - V15 conserved-quantity declaration
  - V16 time-reversal parity
  - V17 target-level coordinates in clauses (protected)
- **Sources** (read-only): `/tmp/claude-0/mainwt/PROGRAM/OWNER_RULINGS.md` (G2-11), `PROGRAM/STATE.md`, `PROGRAM/RULES.md`, `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md`, `PROGRAM/RESULTS/R1/D5_COMPARATOR_AUDIT.md`, `PROGRAM/RESULTS/R1/R1_T_LADDER.md`, `F0_REQUIREMENTS_CONSOLIDATION_01.md`, `F0_SD0_CHARTER.md`, `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`, `F0_SD0_RESULT.md`, `F0_SD0_RECON_01.md`.