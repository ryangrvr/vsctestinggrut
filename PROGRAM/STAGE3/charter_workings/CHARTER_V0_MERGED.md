# GRUT 2: Stage-3 Charter v0 (rules for judging 𝒦 cards)

**Date:** 2026-10-07 · **Branch:** `grut2-stage3`, equal to `main` after the G2-11 merge `86bf5a0` · **R1 terminal boundary:** `dbfd64b` · **Governing ruling:** G2-11 (the ruling block, additions 1–4 and the reconciliation note on 𝒜_ε).

> **Status: CHARTER v0, a draft for owner review. Not frozen.**
> - This draft merges three independent drafts. Where they differ, it keeps the most precise and most conservative rule. Appendix D records every choice.
> - It is written to be frozen **alone** (G2-11).
> - It contains **no candidate law**. No 𝒦 is proposed, sketched, named, exemplified or optimized, either in the body or in any appendix.
> - Every construction in §24 is an abstract gaming pattern labelled **CHARTER TEST**. None of them is a physical proposal.
> - After the freeze: **STOP for owner review before Card 1.**
> - Nothing in this charter is banked. The freeze commit gets a `pending` line in CHECKS.

---

## 0. Status, sources, naming and conventions

### 0.1 Governing documents
- `PROGRAM/OWNER_RULINGS.md`: G2-11. Also G2-08 and G2-10 where they are cited.
- `PROGRAM/STATE.md`: the Stage 3–6 definitions.
- `PROGRAM/RULES.md`.
- `PROGRAM/NORTH_STAR.md`: the architecture and the environmental-identity requirement.
- `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md` §§1–3, 7, 11 and 12.
- `R1_T_LADDER.md`: §0 (frozen definition), §1 (the lattice) and §10.
- `D5_COMPARATOR_AUDIT.md` §§2.3, 3 and 6, and `D5_IDENTIFICATION.md`.
- `PROGRAM/SCOREBOARD.md` and `PROGRAM/GRAVEYARD.md`.
- `F0_REQUIREMENTS_CONSOLIDATION_01.md` at `0a9a941`, as cited by the SD0 charter.

### 0.2 Precedents adopted
- **`F0_SD0_CHARTER.md`:**
  - the charter is frozen alone;
  - candidates are preregistered;
  - modifying a candidate after the fact makes a new candidate;
  - repairs are numbered.
- **`F0_SD0_COMPACTNESS_ACCOUNTING_01.md`:**
  - free choices are weighed against distinctions;
  - a symbol that encodes a table counts as the table;
  - a constant that matters for one control only is fitted to that control;
  - lookup structure is classed RELOCATED.
- **`F0_SD0_HOLDOUT_PROTOCOL_01.md`:** an independent selector picks holdouts after the freeze. **`F0_SD0_GENERALIZATION_CHECKS_01.md`** is also adopted.
- **`F0_SD0_RECON_01.md` and `F0_SD0_RESULT.md`:**
  - the exact counts of the selectivity landscape;
  - the PR-forcing lemma;
  - T1 and T2;
  - ASP's over-allowance of the theta parity system;
  - the decidability caveat, which was flagged but never audited;
  - the comparator audit, which stopped at 1 of 5.

### 0.3 Naming
- **FR1–FR15** are requirements R1–R15 of the consolidation map, renamed so they are not confused with the Stage-2 observable.
- **R1** is the Stage-2 observable and its terminal record.
- **ℛ** is a card's target relation. **ℛ★** is its primary lock.
- **GY-n** is a GRAVEYARD entry (§21.2).
- **Card** is one frozen 𝒦 candidate with every field of §17.
- **Roles** (§23): Author, Intake auditor, Evaluator, Recomputer, Selector, Comparator panel, Owner.
- **Harness** is the charter's own code (§19.3).
- **[P]** marks a constant the owner fixes at freeze (Appendix A).

### 0.4 Conventions (binding throughout)
- **CV-1 Hostile default.** Ambiguities, unresolved disputes and unresolved regime hypotheses are resolved against the card until the owner rules. A dispute goes to the owner together with both computations.
- **CV-2 Burden asymmetry.**
  - The card bears the burden of every certificate.
  - The evaluator adds nothing that helps a card, in particular no standard witnesses.
  - The evaluator may add anything that reduces credit: derivations into 𝒮, comparators, chart coordinates, larger hostile families, decoders.
- **CV-3 Honesty (RULES 5).** No theorem is claimed without a proof. NOT FOUND ≠ IMPOSSIBLE. Literature is verified against primary sources; a citation that is not verified cannot carry a verdict on its own.
- **CV-4 Numerics (RULES 6).** The pipeline runs computed → machine-readable output → generated tables, with at least one exact-identity control (§15.3).
- **CV-5 Neutrality.**
  - The charter preregisters no target relation, sign, monotonicity or functional form, and favours no outcome category.
  - If ℛ★ is signed or monotone, the sign and the form must come from 𝒦 (G2-11).

---

## 1. Definitions and objects

### 1.1 Law and ontology
- **Ξ** is the relational process object. Its kinematic type 𝒳 and its relata carrier V_Ξ are declared and priced by the card.
- **𝒞** is the card's declared commitment data. Its meaning is declared and priced (FR11). Any possibility language means *declared* possibility.
- **𝒦[𝒞, Ξ] = 0** is the law, and **Sol_𝒦(𝒞)** := {Ξ ∈ 𝒳 : 𝒦[𝒞, Ξ] = 0}.
- **Nonvacuity:** ∅ ≠ Sol_𝒦(𝒞) ⊊ 𝒳 on every instance in the declared domain, at both r★ and r★★.

### 1.2 The pipeline and its components

The chain is:

  𝒦 → Sol →[X_Π] Π →[X_Z] Z_Π →[X_h] [h]_{T_Π} →[X_T] T_Π →[Obs] Γ_Π →[ε, charter code] ε_R → ℛ

**Components the card supplies:**
- X_Π, the partition extractor;
- X_Z, the carrier extractor;
- X_h, the readout-class construction;
- X_T, the interface-class construction;
- Obs, the record map;
- Emb, the rule that embeds a battery scenario into Ξ;
- s_T, a canonical reduction, needed only when T_Π lies outside the frozen tiers (§1.4).

**Components the charter supplies:**
- the ε_R implementation (the R1 code);
- the batteries;
- the 𝒮-checker;
- the harness: ablation, representation, decoders and pricing.

**Rules for card components:**
- **PC-1 Uniform.** Each component has one L₀ definition for every instance. It has no branch on scenario name, size, party count, setting count, dimension, resolution or item identity (SD0 firewall 3).
- **PC-2 Priced** exactly like law clauses (§4). Calling something "extraction, not law" earns no discount.
- **PC-3 Covariant** under the representation moves of §1.6.
- **PC-4 Decidable** within the declared resources (§16).
- **PC-5 Ablatable.** It runs unchanged when 𝒦 is replaced by a null law (NR-4).

### 1.3 Generated structures

**Π(Ξ), the partition.**
- It partitions V into one designated environment block E and a system block S. Multipartite embeddings use blocks S₁…S_m (§15.1).
- An approximate Π is an assignment V → Δ(blocks). It may leave a boundary ∂ of unassigned relata, with |∂|/|V| ≤ δ_∂ [P].

**Persistence and A-stability.** Let VI_norm(Π, Π′) := VI(Π, Π′)/log₂|V|, Meilă's variation of information under the uniform measure on V. Π is persistent and A-stable if both:
- VI_norm ≤ δ_Π [P], either against Π_ref (from the reference protocol a₀) for every a ∈ A and every t ≤ H when Π is time-indexed, or pairwise across protocols when Π is global;
- the fraction of reassigned relata is ≤ η [P], where elements of ∂ count as reassigned.

H ≥ max(the full protocol and record window of every a ∈ A, 10·τ_int), where τ_int is the card's declared shortest internal timescale, which is priced.

**Nontrivial Π:**
- S ≠ ∅ ≠ E and Π ≠ ⊥;
- Π is not the partition into components that are disconnected in the inputs;
- Γ_Π is not constant across A.

**Z_Π, the environment state variable (the carrier).**
- Its dimension is arbitrary.
- *Which* variable it is (instantaneous, initial or other) is a derived output and never a definition (R1 §12 item 5; D5 Remark D3).

**[h]_{T_Π}, the readout class.**
- h maps states of Z_Π to the record space 𝒴. It is fixed only up to T_Π: h ~ t∘h.
- The class must be derived as the readout redundancy of the card's own observation map.
- No unique coordinate formula for h is credited (G2-11).

**T_Π, the interface class.** A group of record maps acting per protocol, generated from (Ξ, Π) and placed in 𝕃_T (§1.4).

**Repertoire.**
- A is a finite set of interventions on the S-block(s) of Π_ref, with a reference protocol a₀ ∈ A.
- The card declares a repertoire class 𝔄 and a grid class 𝔗. 𝔄 must contain the frozen repertoires A_{r★} and A_{r★★} (Appendix A), and it must be closed under sub-repertoires that have |A| ≥ 2 and contain a₀.

**Γ_Π := Obs_Π(Ξ) = (P_a)_{a∈A}.**
- P_a is the law of the record Y_a ∈ 𝒴^τ under protocol a.
- **Only per-protocol laws are data.** Joint laws across protocols are inaccessible-context data (FR3).
- A Γ given as an empirical model is supplied, not generated (FR13).

**Carrier status.**
- **PASS** if and only if the card proves from 𝒦 that Y_a = t_a(h(Z_Π)), with one h, t_a ∈ T_Π and Z_Π derived, for every a in every A ∈ 𝔄.
- **FAIL** if the derivation produces protocol-dependent readouts h_a.
- **UNRESOLVED** otherwise.
- R1's verdict table applies unchanged: R1-PASS, R1-NULL, NO RECIPROCITY VERDICT, MODE SELECTION.

### 1.4 ε_R and the interface lattice
- **Definition (frozen R1).** ε_R := ε[Γ_Π, T_Π] := inf over P★ of max over a ∈ A of d_op^{T_Π}(P_a, T_Π·P★).
- It is computed **only by charter code**, never by card code.
- **Catalogue 𝕃_T.**
  - E₂± ⊂ T_caus ⊂ T_lin, where T_lin = T_R1 = GL(k) with translations;
  - T_mono ⊇ E₂±, and T_lin ∩ T_mono = E₂±;
  - the join J := ⟨T_lin, T_mono⟩;
  - T_univ, the GY-11 classes (§21.2).
- **Admissible set 𝕃_T^adm** = {E₂±, T_caus, T_lin, T_mono} ∪ {generated T_Π with a proved canonical reduction}.
  - An ε value taken at J, at T_univ, or at a class without a proved reduction is **void**.
- **Frozen d_op.** For T_lin it is d_q^BL (center, whiten, then O(k)); for T_mono it is the normal-score form modulo reflections ℛ; d_BL has its frozen normalization (R1 §1).
- **A generated T_Π outside the frozen tiers.** The card supplies a canonical reduction s_{T_Π} with residual compact group K, and proves that d_op^{T_Π}(P, T_Π·Q) := min_{k∈K} d_BL(s(P), k#s(Q)) is invariant under T_Π acting on both arguments.
  - The reduction is priced as a component and run inside charter code.
  - Without it, ε_R is undefined for that card, and every relation that uses ε_R fails Q8.
- **The R1 ladder stays closed** (G2-10). A card's T_Π is a card output, not a new R1 tier. This is a use of R1, not a modification of it (OD-6).

### 1.5 Scenarios, audit instances, fibers and charts

**Scenario σ** (observable level, independent of any card): a finite port set (intervention and record ports), a repertoire A_σ, a grid τ_σ and a record space Y_σ.
- Freedom counts, witnesses and gate tests are computed at this level.
- In B-SEL support scenarios only the Γ axis is scored. Π and T are reported there.

**Audit instances** ι = (𝒞_ι, V_ι, A_ι ∈ 𝔄, τ_ι ∈ 𝔗, 𝒴_ι):

| Family | Content | Generated by |
|---|---|---|
| AI-1 | The smallest nontrivial instance, computed exactly | The card declares it; the evaluator may add more |
| AI-2 | Symmetric-input instances, with Aut transitive on V or on the candidate partitions | The evaluator |
| AI-3 | A generic-input ensemble drawn from the charter reference measure (uniform on the declared finite truncation of 𝒞's type), with seeds committed after the batch closes | The evaluator |
| AI-4 | Battery embeddings via Emb | The harness |
| AI-5 | Sealed holdouts (§15.9) | The Selector |

**Lock fibers.**
- A lock fiber is a pair (ι, H): an instance and a regime class (§13.2).
- The **hostile fiber** at ι uses H_host: every hypothesis that is not proved to fail at x by more than the lock resolution (BP-4).
- I_𝒦 is the instance set on which credit is summed. It has at most 3 structurally distinct instances with mutually independent data, declared at freeze.

**Chart φ_ι.**
- It is a finite chart of 𝒜_Γ, built from T-invariant witness coordinates for scope Q and from response functionals for scope G. It has box windows (Appendix A) and resolution 2^(−p).
- The card declares it and the auditor may add coordinates. **Credit is computed on whichever admissible chart minimizes the credited bits.**

**Chart rules.**
- **Ch-1** Resolutions r★ and r★★ are fixed by the charter (Appendix A). Every claim must hold at both.
- **Ch-2** Scoring uses frozen protocol templates. The card does not choose battery items or scoring repertoires.
- **Ch-3** Finer grids, higher precision, copies of instances or a larger carrier earn nothing (caps in §2.4).
- **Ch-4** A truncation artifact earns zero: a relation that holds at r★ but fails at r★★, or fails at the next truncation level.
- **Ch-5** Credit is summed only across structurally distinct instances with mutually independent data.

### 1.6 Representation moves (FR1)
- **RM1** Relabel the elements of finite sets.
- **RM2** Relabel outcomes, interventions and ports.
- **RM3** Reparametrize continuous parameters by declared bijections.
- **RM4** Use an equivalent presentation of a conditional-response kernel (one that induces the same laws).
- **RM5** Re-bracket compositions.

The card's declared moves must include RM1–RM5. Any further move is priced. Invariance is claimed only under the declared moves.

---

## 2. Owner item 1: baseline freedom spaces

### 2.1 Principles
- **BP-1 What the baseline is.** Everything established physics permits for operational data of the same type, in the same regime, from the same inputs, with Π, Z, [h] and T **supplied by hand**. It is computed after 𝒮 (§13).
- **BP-2 Where standard theory leaves freedom.** Standard theory leaves Π, Z, [h] and T to the modeller and constrains Γ through 𝒮. Every R1 claim was conditional on a carrier supplied from outside.
- **BP-3 Regime matching.** Claims about a realization x are compared only with the baseline under H(x), the set of regime hypotheses true at x. A witness drawn from another regime is invalid.
- **BP-4 Hostile default.** A hypothesis whose status at x is unresolved is taken to hold, unless the card proves it fails by more than the lock resolution.
- **BP-5 Same inputs.** The baseline receives exactly the data that the card's prediction consumes.

### 2.2 Standard models
𝔐_std(ι | H) is the set of models of the Standard Framework Panel (§8.4). These are classical Hamiltonian or stochastic models, or quantum open-system models, in which the system, environment, coupling, initial state, readout, partition and calibration class are each chosen independently. A model belongs to the set if it:
- (i) produces data of the declared operational type on ι;
- (ii) satisfies every STD constraint (§13.3) whose hypotheses lie in H;
- (iii) uses the card's inputs at the level being compared;
- (iv) takes Π, Z, [h] and T as supplied.

### 2.3 The spaces

**𝒜_Π(ι | H): partitions.**
- Defined as {⊥} ∪ {Π persistent and A-stable under some m ∈ 𝔐_std(ι | H)}, modulo the scenario's declared relabelling group.
- If 𝒞 fixes no dynamics, every partition with S ≠ ∅ ≠ E is admitted.
  - With one S and a designated E: 2^|V| − 2 partitions, plus ⊥.
  - Multi-block embeddings: all ordered set partitions with a designated E.
- If 𝒞 fixes dynamics, the space is the set of partitions certified as persistent by standard criteria (STD-6, STD-10, and the SPS decoders of §5.4).
- Under CV-2 the smaller construction is used.

**𝒜_T(ι, Π | H): interface structures ([h], T).**
- T ∈ 𝒯 ∪ {⊥}, where 𝒯 = {E₂±, T_caus, T_lin, T_mono} is frozen.
- h is any readout of a declared E-state variable, common across A by hand.
- T must be causally implementable (STD-1) and CP-implementable (STD-2), and must contain the platform's calibrated maps.
- 𝒯 excludes the GY-11 and GY-12 classes, J and T_univ.
- A generated T_Π is added to 𝒯 for placement and ε computation only. The T-credit cap does not change.

**𝒜_Γ(ι, Π, [h], T | H): record families.**
- Defined as {Obs(m) : m ∈ 𝔐_std with this (Π, Z, [h], T)}.
- With H = ∅ this is the set of non-anticipating, positive families on 𝒴^τ indexed by A (the grid-level E_univ). Each hypothesis in H intersects that set with its constraints.

**𝒜_ε := {ε[Γ, T] : (Γ, ([h], T)) jointly admissible}.**
- This is an **image, not an axis** (Addition 2). It carries no freedom count (§12).

**Joint baseline 𝒜(ι | H).**
- It is the fibered set of triples (Π, ([h], T), Γ), each component admissible given the earlier ones.
- The standard couplings (STD-5, STD-7, STD-10) already live inside the fibers. Only coupling beyond them can be credited.

**Definitional space 𝒟(ι).** All well-typed tuples (Π, [h], T, Γ), with ε substituted, **before** 𝒮 is imposed.

**The null hypothesis Stage 3 must break.** Standard physics treats Π, T and the generators of Γ as independent modelling choices, coupled only through 𝒮. That near-product structure is what Stage 3 must break.

### 2.4 Values fixed now
- **(2,2,2), possibilistic object:** 2961 pNS tables.
  - 1721 are local.
  - 1232 are logically contextual. Of these, 992 have an exact-support realization and 240 do not.
  - 8 are strongly contextual, and these are exactly the 8 PR boxes.
- **(2,2,2), record-law object:** 2721 exact-support-realizable supports.
- **Interface catalogue:** |𝒜_T| = 5 at freeze, giving a T-term cap of log₂ 5 ≈ 2.32 bits per instance.
- **Partitions of n relata with one S:** |Part*| = 2ⁿ − 2. For n = 8 that is 254, about 7.99 bits. The Π-term cap is 16 bits per instance.
- **Everything else** is computed by the evaluator with the frozen procedures of §2.5, never by the card.

### 2.5 Measuring freedom reduction
Write Im_σ(Sol) ⊆ 𝒜_Π × 𝒜_T × 𝒜_Γ and 𝓡_𝒦 := Im* := Im ∩ 𝒜^base.

**Non-standard realizations.** A triple in Im \ 𝒜^base is a non-standard realization.
- Each one is a declared prediction and needs its own kill condition.
- If it contradicts an established relation inside that relation's tested domain, KU-4 applies.

**Discrete axes.** ΔF_disc = log₂|𝒜/~| − log₂|Im*/~| on the Π, T and support axes, subject to the caps.

**Continuous axes: codimension only.**
- c(ι) := dim_lb 𝒜^base(ι | H) − dim_ub Im*(ι).
- dim_lb is certified by standard models (B-HB) that realize a full-dimensional box of chart coordinates around the instance.
- dim_ub is certified by a proof, or by an exact rank computation at an explicit point.
- Continuous credit is p·c(ι).
- Reductions that only shrink a log-volume through inequalities are reported and never credited.

**Per-instance total.** ΔF(ι) = p·c(ι) + min(16, ΔF_Π) + min(log₂5, ΔF_T) + ΔF_supp.

**When a reduction counts as nontrivial.** Only if all four hold:
- (i) ΔF > 0 on joint coordinates (Q5);
- (ii) the §3 witnesses exist;
- (iii) the anchors are retained (§15.8);
- (iv) Im satisfies 𝒮, apart from declared violations outside 𝒮's established domain, each of which has its own kill condition.

---

## 3. Owner item 2: success criterion

### 3.1 Qualifying relation: certificates Q1–Q12
A relation has the form ℛ(Π, [h]_{T_Π}, T_Π, Γ_Π) = 0, with ε_R entering only as ε[Γ_Π, T_Π], and zero set Z(ℛ). ℛ★ must hold **every** certificate, at both r★ and r★★.

- **Q1 Forced.**
  - 𝓡_𝒦(ι) ⊆ Z(ℛ) on every in-domain instance (AI-1 to AI-4 and the holdouts), for every A ∈ 𝔄 and every grid in 𝔗.
  - It holds on **all of Sol**, not on a selected subset (FR8).
  - It must be at DERIVED grade: a theorem, or exact computation on every finite battery instance plus a proof for the declared scope.
  - Forcing at evidence grade only gives CARD-UNFORCED.
- **Q2 Non-definitional.**
  - After the substitution ε_R := ε[Γ, T], some tuple in 𝒟(ι) violates ℛ.
  - ℛ is none of DEF-1 to DEF-11 (§12).
  - ℛ restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R.
- **Q3 Non-standard.**
  - For each regime class H on which ℛ is claimed, and each Standard Framework Panel framework F applicable under H, a witness m*_F ∈ 𝔐_F(ι | H) must violate ℛ by more than the lock resolution.
  - The witness comes from B-HB, or is added by the card and verified independently. It must be regime-matched and judged under the hostile default.
  - B-SRB must give |I_SRB|/|I_K| ≥ Q_min.
  - ℛ must be none of the D5 reverse-direction relations (§13.8), and not implied by them in its lock fibers.
  - A framework with no witness: ℛ is RESTATED by it. A derivation from 𝒮: ℛ is STANDARD-IMPLIED.
- **Q4 Law-dependent (W-pipe).**
  - Some Ξ of the declared type with Ξ ∉ Sol has a pipeline image that violates ℛ.
  - The responsibility map (NR-4) must show that ℛ depends on 𝒦's clauses, not on the type, the extractors, the representation or a prior.
- **Q5 Joint.**
  - Z(ℛ) ∩ 𝒜(ι | H) is **not** of the form (Z_I × Z_Γ) ∩ 𝒜(ι | H), where Z_I lies on the interface side (Π, [h], T) and Z_Γ on the response side (Γ, ε_R).
  - **Rectangle witness:** (u₁, Γ₁) and (u₂, Γ₂) lie in Z(ℛ); (u₁, Γ₂) and (u₂, Γ₁) lie in 𝒜(ι | H); and at least one of the last two lies outside Z(ℛ).
  - A restriction on a single axis, or a coupling of Π and T that does not involve Γ, is not a qualifying ℛ.
- **Q6 Informative.**
  - c ≥ 1 at every lock fiber (continuous case), or ΔF_disc ≥ log₂ Q_min (discrete case).
  - b_meas(ℛ) ≥ log₂ Q_min ≈ 3.32 bits.
  - A relation that fixes only a sign or a zero carries at most 1 bit and fails.
- **Q7 Representation-invariant.**
  - ℛ is invariant under h ↦ t∘h for t ∈ T_Π, under the declared moves of Ξ and 𝒞, and under relabellings of V.
  - It depends on Γ only through the per-protocol laws (FR3).
- **Q8 Admissible interface.** Every ε value in ℛ is taken at T_Π ∈ 𝕃_T^adm (§1.4).
- **Q9 Non-vacuous.**
  - Scope Q: every lock fiber contains certified realized points with ε_R > 0 beyond the resolution, and ℛ is not satisfied merely because ε_R ≡ 0.
  - Any scope: Z(ℛ) ∩ 𝓡_𝒦 ≠ ∅.
- **Q10 Scoped.** Exactly one response scope is declared, and ℛ is consistent with it (§14).
- **Q11 Neutral.**
  - Any sign, monotonicity, tradeoff or functional form in ℛ is an output of the derivation from 𝒦.
  - W-pipe must show that the pipeline alone would also admit the opposite sign.
  - A sign that is supplied is a supplied target relation (§5.6).
- **Q12 Named.** ℛ★ is entered in the **lock register** at freeze, together with its LT-1 instantiation (§3.3).

**Number of relations.** A card has at most 2 relations, exactly one of them primary. A secondary relation is scored separately, never replaces ℛ★ once scoring has started, and is never credited to ℛ★ (no cross-subsidy).

### 3.2 Success thresholds
A card succeeds only through all three of the following, and only while it remains admissible (S0–S9, §18):
- **SC1 Nontrivial freedom reduction.** Q1–Q12 hold at r★ and r★★, and c ≥ 1 (or the discrete equivalent) at every lock-fiber instance, after 𝒮.
- **SC2 Positive compression.** §4.5.
- **SC3 Measurable consequence.** An admissible and **feasible** LT-1 instantiation (§3.3). There is no "in-principle" grade.
- **SC4 Never credited toward SC1–SC3:** the items in §22.

### 3.3 Named lock target LT-1: the Interface–Response Residual (IRR)

ℛ★ is evaluated on a physically realized environment with a certified carrier. It predicts a lock observable O, in one of two ways:
- from interface-side quantities measured independently: the persistence and A-stability statistic of Π, the T_Π tier verdicts, and the carrier certification;
- or from response-side data on a protocol subset disjoint from the one used to evaluate O.

No parameter is fitted on lock data. **The quantity locked is the SRB residual: the part of the prediction that B-SRB, given the same inputs, leaves free.**

**Measurement rules.**
- **MC-1 Observable type matches scope.** Scope Q uses a T-invariant observable, measured with the frozen d_op at a frozen tier or through a witness with a frozen constant. Scope G uses a response functional.
- **MC-2 Independence and identification.**
  - At least one input to the prediction is an interface-side measurement made independently of the record laws used for O.
  - Π and T_Π are certified for the test system independently of the records used to test ℛ★.
  - A certification that presupposes ℛ★ is circular.
  - The carrier cannot be certified from records (R1 §3).
  - A lock that predicts ε_R from the same Γ it is computed on is definitional.
- **MC-3 Prediction.** The interval I_K is stated at freeze, with every uncertainty propagated, including truncation error.
- **MC-4 Discrimination.**
  - The auditor computes I_SRB before unsealing.
  - |I_SRB|/|I_K| ≥ Q_min.
  - The effect size against the nearest certified standard witness is reported.
  - A lock that tests only a sign is inadmissible.
- **MC-5 Thresholds.**
  - **LOCK-FALSIFIED** if dist(O_meas, I_K) > 3σ_tot.
  - **LOCK-CONFIRMED** if dist ≤ 2σ_tot, σ_tot ≤ |I_K|/4, and MC-4 holds.
  - **LOCK-INCONCLUSIVE** otherwise.
  - σ_tot includes the preregistered systematics, among them the residuals of the carrier certificate.
  - If any threshold, observable, tier, protocol set, grid, estimator or exclusion rule changes after unsealing, the result is **LOCK-VOID, which counts as LOCK-FALSIFIED**.
- **MC-6 Carrier certification.**
  - The platform must pass R1's 10-item certificate checklist, adopted here as a Stage-3 rule and not as an edit to R1 (OD-9).
  - Failure gives NO RECIPROCITY VERDICT, which counts as LOCK-INCONCLUSIVE.
  - One preregistered alternate platform is allowed. There is no third.
- **MC-7 Feasibility.**
  - N_req ≤ N_max = 10⁹ independent records in total per lock observable, at α = 0.0027 and power ≥ 0.9 against the nearest point of I_SRB at distance ≥ |I_K|.
  - At most 30 days of platform time.
  - Otherwise CARD-UNMEASURABLE. For reference, BRI1's single-time witness (about 10¹¹ records) would fail this test.
  - Estimation uses per-witness forms; no plug-in d_BL for k ≥ 3. R1's D4 is not a prerequisite.
- **MC-8 Sealing.**
  - **LOCK-H:** existing datasets chosen after freeze by the Selector, under the SD0 holdout protocol adapted to datasets.
  - **LOCK-E:** a prospective experiment, with its protocol committed before any data exist.
  - In-silico evaluation (≤ 10¹⁰ effective samples) is evidence grade only and **never confers PREDICTIVE**.
- **MC-9 Multiplicity.** At most 2 relations. Thresholds are Bonferroni-adjusted across lock observables.
- **MC-10 Status.** LOCK-CONFIRMED on sealed real data, plus an external check, gives PREDICTIVE. LOCK-FALSIFIED fires KU-12.

**Platform classes.** The card declares one at freeze.
- P-1: classical mechanical or stochastic environments with independently calibrated readouts.
- P-2: mesoscopic electronic environments with calibrated detection of counting statistics.
- P-3: engineered quantum environments with calibrated input–output readout.
- P-4: archived datasets that meet MC-6 (LOCK-H only).

Listing a class does not claim that any relation can be tested there.

---

## 4. Owner item 3: compression accounting and information price

### 4.1 Base language and code
- **L₀ (RULES 2):** finite sets, maps, interventions, conditional response, composition and logic.
- **Code:** the frozen 64-token alphabet in Polish notation (Appendix B.1).
- **Statement length:** L_stmt(X) := 6·#tokens(X) + Σ over variable occurrences of ⌈log₂(v_X + 1)⌉ + Σ over literals of ℓ(lit).
  - v_X is the number of distinct variables in X.
  - ℓ(n) is the Elias-δ length of n + 1.
  - ℓ(n/d) := ℓ(n) + ℓ(d) + 1.
  - A real literal costs p + ℓ(|exponent|) + 1 at precision p.
  - A defined symbol costs its definition once, then ⌈log₂(#definitions + 1)⌉ bits per use.

### 4.2 Price components
Price(𝒦) is the sum of IP-1 to IP-13.

- **IP-1 Statement.** L_stmt of 𝒦 in clause normal form, plus the declaration of 𝒳 (sorts, arities, labels).
- **IP-2 Inputs.** Every supplied datum, encoded with the same code:
  - 𝒞 itself; carrier size; initial data; couplings; constants; scales; the time unit;
  - Emb and the selectivity-interface map;
  - X_Π, X_Z, X_h, X_T, Obs and s_T;
  - priors and measures;
  - truncation levels, tolerances and thresholds;
  - representation moves beyond RM1–RM5;
  - restrictions of the declared domain.
- **IP-3 Tables.**
  - A symbol that encodes a table costs the whole table.
  - Hand-listed configurations are tables.
  - Uniform quantification is not a table.
- **IP-4 Selection.**
  - Choosing an invariant, clause shape, component or framework from a family costs log₂ m.
  - m is the largest natural family an auditor exhibits. The card may argue for a smaller family by citing the published family it actually chose from.
  - The item's price is max(L_stmt, selection price).
- **IP-5 Constants.**
  - Price = max(literal code length at p, tuning price log₂(declared range / passing window)).
  - The range is declared at freeze. The default for a dimensionless positive constant is [10⁻³, 10³] on a log scale.
  - The passing window is the coarsest window inside which no credited verdict or prediction changes.
  - A value forced by other priced items costs 0.
  - Constants are repriced at p = 6, 10 and 16.
- **IP-6 Priced vocabulary.**
  - Each item VB-1 to VB-21 (Appendix B.2) costs P_v := max(L_stmt(def_v), ΔF_tgt(v)).
  - ΔF_tgt(v) is the reduction that v alone imposes on 𝒟, plus the SEL distinctions that v alone settles. "Alone" means the card with every non-vocabulary clause removed.
  - Import subtraction (FC-2) also applies.
  - **Supplying a quantum set, the Born rule or a GPT cone makes every selectivity result RELOCATED** (SD0 firewall).
  - Every use is flagged on the ledger.
- **IP-7 Supplied protected structures** (declared; §5.6).
  - P_X := max(L_stmt(X), ΔF_tgt(X)), computed against 𝒟(ι) and never against 𝒜^base.
  - So no compression can ever come from a structure the card supplies.
- **IP-8 Imported standard components.**
  - Priced at log₂|SFP menu| plus their constants.
  - Their consequences are baseline and earn nothing.
- **IP-9 Case splits.**
  - Each branch costs 1 bit plus the price of its condition.
  - Branches keyed to scenario names, party or setting counts, dimensions, capacities, sizes, resolution or item identity are **prohibited**. Such a branch is LOOKUP and the card is RELOCATED.
- **IP-10 Per-instance structure.** A constant or clause whose effect is confined to one battery item or one instance is a table row priced in that instance. The distinction it produces is removed from D_sel.
- **IP-11 Lock-side fits.**
  - Cost: log₂(range / posterior width).
  - The prediction becomes a fit and cannot serve as a lock.
- **IP-12 Selection tax.**
  - τ_sel := log₂(1 + n_drafts). n_drafts counts every 𝒦 draft in any form (any agent, panel or workflow) logged between the charter freeze and this card's freeze. The count is cumulative.
  - A further log₂(N_frozen) is charged at the owner's pick.
  - Undisclosed search voids the card (KU-10).
- **IP-13 Domain restriction.** Excluding instances from the declared domain is priced as a selection from the family of domains.

### 4.3 Credited content
- **FC-1 Lock bits** for each qualifying relation:
  - b_struct(ℛ) = Σ over ι ∈ I_𝒦 of ΔF(ι).
  - b_meas(ℛ) = Σ over independent lock observables o of log₂(|I_SRB(o)| / max(|I_K(o)|, 2σ_tot(o) at N_max)).
  - An observable implied by the others under 𝒮 together with ℛ contributes 0.
  - **Credited b(ℛ) = min(b_struct, b_meas).**
- **FC-2 D_sel.**
  - 1 bit for each verified B-SEL verdict class that is mandatory or graded and that the card reproduces, up to 10 bits.
  - Removed:
    - distinctions implied by other counted ones, or by structural facts of the SD0 record. Example: T1, under which every table that is not strongly contextual survives arc consistency. Each such implication must be argued explicitly;
    - import subtraction: distinctions a vocabulary item or an import still reproduces with 𝒦's clauses deleted;
    - IP-10 structure;
    - consistency collapse (§15.2);
    - automatic items (SEL-0, SEL-4, SEL-12).
- **FC-3 D_diff = 0.** Persistence and differentiation are gates, not credits.
- **FC-4 Never counted:**
  - bits on 𝒜_ε;
  - restrictions implied by 𝒮 (RECOVERY);
  - definitional relations;
  - consequences of the priced inputs alone (the restriction holds for every Ξ ∈ 𝒳 consistent with 𝒞);
  - holdout successes, which are tallied separately.

Credited(𝒦) := Σ_ℛ b(ℛ) + D_sel. ΔL := Credited(𝒦) − Price(𝒦). ρ := Credited/Price.

### 4.4 Two-part code against the null
On AI-1 and AI-3, Price(𝒦) plus the residual bits needed to describe the card's realized data must be less than Price(NULL-ΠT) plus the residual bits for the same data (§15.6).

### 4.5 Compression verdict

| Condition | Verdict |
|---|---|
| ΔL ≤ 0 at p = 10 | **LOOKUP**: CARD-RELOCATED, whatever the gates say (SD0 rule) |
| ρ ≥ 2, ΔL ≥ p★ at p★ = 10, ΔL > 0 at p = 16, and §4.4 holds | **COMPRESSIVE** (SC2 met). The value at p = 6 is reported |
| Otherwise | **NON-COMPRESSIVE** |

### 4.6 Mandatory ledger
- One row per item, with these columns: item · class (statement / input / vocabulary / supplied protected / selection / domain) · L₀ encoding · bits · hostile family size · ΔF_tgt · rule applied.
- Then:
  - ΔF(ι) per instance, with the dim_lb, dim_ub, Π, T and support terms;
  - b_struct and b_meas;
  - D_sel, with its removals argued;
  - Price, ΔL and ρ at p = 6, 10 and 16;
  - the two-part code comparison.

### 4.7 Disputes
- An ambiguity goes against the card.
- Any higher price an auditor raises governs until the owner rules.
- Thresholds are never reopened.

---

## 5. Owner item 4: nonrelocation

### 5.1 Protected structures
- **PS-1 The partition Π**, including the party structure of embedded scenarios.
- **PS-2 The carrier, i.e. the environmental identity.** Which E state variable counts as "the environment" (instantaneous versus initial; D5 Remark D3), and the protocol invariance of the readout.
- **PS-3 The readout class [h].** This includes a common-readout axiom, a designated list of observables, and any readout clause indexed by protocol.
- **PS-4 The interface class T**, including its calibration and any group action on record space.
- **PS-5 Gibbs/KMS/FDT structure:**
  - invariant or thermal measures; temperature; energy-weighted measures;
  - detailed balance; KMS; FDT kernels;
  - fluctuation-theorem premises; Onsager symmetry used as a premise.
- **PS-6 The target relation ℛ★.** Also any relation that implies it, any monotone of it, any penalty, objective or selection criterion that contains it, and any presumed sign or identity–response tradeoff.

**Prohibited inputs** (STATE):
- memory kernels, viscoelastic constitutive laws and crystalline order;
- R1 calibration data: the BRI1 grid, protocols, calibrated maps and constants.

**"Hidden"** means present in 𝒦, 𝒞, 𝒳, the components, priors, Emb, truncation choices, the representation, or the choice of battery or repertoire, without being declared.

### 5.2 Input inventory
The card lists every input item I_j by class:
- clauses;
- 𝒞 constants;
- the type and representation of Ξ;
- components;
- priors and measures;
- Emb;
- truncation levels;
- scope declarations.

### 5.3 Tests (executed by the auditor; each is a finite procedure)

- **NR-0 Inventory closure.**
  - The evaluator reproduces every verdict from the listed inputs alone.
  - The reference implementation reads nothing else: no files, no embedded data, no literals beyond those declared.
  - An undeclared input makes it RELOCATED.
- **NR-1 Vocabulary firewall** (syntactic; all definitions unfolded).
  - The harness lists every symbol and flags any that names or encodes a protected structure. Examples:
    - Π or S/E labels, and typed sorts that pre-split the relata;
    - h, [h] or readout maps;
    - T or record-space group actions;
    - Γ, Obs, ε, P★, d_op or "carrier";
    - measures, weights or temperatures, Gibbs, KMS, FDT, Onsager;
    - target-level coordinates, or ℛ.
  - A flagged symbol that is declared → SUPPLIED. A flagged symbol that is not declared → RELOCATED.
- **NR-2 Target-level firewall.**
  - Put 𝒦 in clause normal form.
  - A clause is target-level if it mentions records, chart coordinates, ε, interface maps, partition labels or readouts.
  - RELOCATED if, up to RM moves and definitional unfolding, either:
    - the target-level clauses together with 𝒮 imply ℛ★ on 𝒟; or
    - ℛ★ is a clause, a conjunct, or a consequence of the clauses that mention only observable-level or pipeline terms.
  - ℛ★ is fixed in the lock register at freeze.
- **NR-3 Two-witness.**
  - For each generated X ∈ {Π, Z_Π, [h], T_Π, Gibbs/FDT if claimed, ℛ★}, a W-pipe is required: some Ξ ∉ Sol of the declared type whose pipeline output lacks X or yields a different X.
  - No W-pipe → X RELOCATED, into the type, the pipeline or the representation.
- **NR-4 Law ablation and responsibility map.**
  - Run the pipeline with 𝒦 replaced by 𝒦_∅ (type only), then by 𝒦_𝒮 (type plus 𝒮), then with single clauses deleted.
  - X appears under 𝒦_∅ → RELOCATED. X appears under 𝒦_𝒮 but not under 𝒦_∅ → STANDARD-IMPLIED.
  - The resulting map of which clauses each X and each credited claim depend on is recorded. It is used by Q4, Q11, FC-2 and the GY return test.
- **NR-5 Symmetric-input probe** (mandatory). On AI-2, with Aut(𝒞_sym) transitive on V or on the candidate partitions:
  - every solution must carry a persistent, nontrivial, A-stable Π;
  - {Π(Ξ)} must be Aut-invariant, reported as an orbit, not as a labelled choice;
  - if 𝒞 contains a symmetry-breaking parameter λ, differentiation must persist as λ → 0. Only which side carries which label may follow the sign of λ.

  If the type of 𝒞 cannot be symmetric, its asymmetry is priced, NR-6 and NR-7 apply at full strength, and Π cannot be GENERATED-STRONG. **Fail → CARD-NONGENERATIVE.**
- **NR-6 Decoder probe.**
  - Decoders read the inputs only, with no access to 𝒦. They are the RB and SPS templates (§5.4) and any uniform L₀ decoder of price ≤ ℓ_dec = ½·F_X, where F_X = log₂|𝒜_X(ι)|.
  - A decoder **fires** if it recovers X within tolerance on at least p_dec = 0.5 of the AI-3 instances, or on every lock-fiber instance. Tolerance means VI_norm ≤ δ_Π for Π, the same class for T and [h], and the same variable for the carrier.
  - Fires → X RELOCATED in that input.
- **NR-7 Scramble.** Replace each priced input component by an independent draw of its type. If X tracks the scrambled component, that component carries X: RELOCATED.
- **NR-8 Representation.**
  - Apply RM1–RM5 and the declared moves, with seeds committed after the batch closes.
  - A non-covariant X is INVALID: it is not generated.
  - An X moved by a declared gauge move is RELOCATED in the representation.
- **NR-9 Prior ablation.**
  - (a) Remove the law and keep μ: if X appears, it is RELOCATED in the prior.
  - (b) Replace μ by the charter reference measure and keep the law: if X disappears, it is RELOCATED in the prior.
- **NR-10 Carrier, readout and interface.** All of the following must hold:
  - (a) no clause of 𝒦, Emb or Obs is indexed by protocol identity, apart from the protocol's action on S;
  - (b) the common-carrier form is proved for every A ∈ 𝔄 and every protocol in A_{r★★};
  - (c) Z_Π is derived from 𝒦, not from records and not by definition;
  - (d) for every family read as reciprocity, 𝒦 excludes, or classifies as a non-solution, both the exact product-latent mode-selection representation (D5 Theorem D1) and its causal prefix-tree version (D2);
  - (e) **E2 test:** on any instance that can express the two-mode configuration, the carrier derivation returns FAIL. The configuration is: a symmetric mode read by a₀; the symmetric mode plus a skewed mode read by the driven protocol; an environment law that does not depend on the protocol;
  - (f) no input names a record-space group action or a readout class; T_Π ≠ Aut(R) for any record structure R that the inputs supply; [h] is derived as the readout redundancy of the card's own observation map; the harness verifies T_Π's generators on the chart;
  - (g) T_Π and [h] are computed without R1 calibration data.
- **NR-11 Mode selection.**
  - Readouts h_a ∉ [h]_{T_Π} give the verdict MODE SELECTION for every ε-relation, and the lock is void.
  - Harness control: HB-9 must return MODE SELECTION.
- **NR-12 Gibbs/FDT premises.**
  - (a) PS-5 items are syntactically absent from the inputs.
  - (b) Every premise of each credited derivation is listed. A Gibbs, KMS, FDT, detailed-balance or Onsager premise that 𝒦 does not generate (with a W-pipe) makes the claim STANDARD-IMPLIED. If the premise is hidden in the inputs, it is RELOCATED.
  - (c) On an instance whose reference state is not KMS: if ℛ's credited content vanishes there, it lived in FDT and earns nothing.
  - Gibbs or KMS properties of the solutions are outputs. They count as RECOVERY, a Stage-6 consistency item with zero credit.
- **NR-13 Neutrality.** No objective, penalty or selection criterion is monotone in ℛ, and no sign is presumed.
- **NR-14 Exclusion audit.** Checks for the STATE exclusions, for IP-9 branches, and for R1 calibration data.
- **NR-15 No promissory structure.**
  - Every structure claimed as generated is computed by the card's frozen algorithms at r★ and r★★.
  - "To be derived later" means SUPPLIED. No follow-up may supply it (§20).
- **NR-16 Battery independence.** A systematic pattern of passing the public items but failing the holdouts is labelled BATTERY-TUNED and reported as RELOCATED.

### 5.4 Decoder templates
**RB, the reader battery.** A reader's cost is the template index plus its parameters, in L₀ bits.
- RB1: read any input label or sort.
- RB2: a threshold or top-n read of any input weight.
- RB3: connected components of any input relation or its complement, k-cores, or degree thresholds.
- RB4: blocks of the finest module decomposition of any input matrix or relation.
- RB5: unions of orbits of Aut(inputs).
- RB6: balls of any radius around an input-designated element, in any input distance.

**SPS, the Standard Partition Selector panel:**
- min-cut, max-cut, spectral bisection and modularity, on any graph or weight structure in 𝒞;
- conserved-charge and symmetry-sector partitions;
- explicit labelling;
- slow/fast splits by input timescales;
- heterogeneity thresholds;
- support co-occurrence;
- for [h]: "most-coupled-variable" readouts and declared observable lists.

### 5.5 Generation grades
- **Π GENERATED-STRONG:**
  - NR-5 passes on a transitive instance on which every solution has a persistent, nontrivial Π;
  - at least one lock fiber is drawn from such instances;
  - every other NR test is clean.
- **Π GENERATED-WEAK:** NR-5 passes (or 𝒞's asymmetry is priced), no decoder fires, and every other test is clean.
- **Carrier, [h] and T_Π GENERATED** if and only if NR-3, NR-4 and NR-10(a)–(g) are clean and T_Π ∈ 𝕃_T^adm.

### 5.6 Labels and consequences

| Finding | Consequence |
|---|---|
| Any protected structure RELOCATED (hidden) | **CARD-RELOCATED**. The card is dead. After external check, a GRAVEYARD line reads "RELOCATED in ⟨input⟩" |
| Π, the carrier, [h] or T_Π SUPPLIED, even when declared | **CARD-NONGENERATIVE** (FR5 strengthened; it fails differentiation by definition) |
| Gibbs/FDT SUPPLIED and declared | COMMITMENT, priced under IP-7. Every claim whose responsibility map touches it earns 0. If the derivation of ℛ★ uses it → **CARD-RELOCATED** |
| ℛ★, or content implying ℛ★, supplied in any form | **CARD-RELOCATED** |
| A STATE-excluded input, or R1 calibration data | **CARD-RELOCATED** |
| STANDARD-IMPLIED (a single claim) | That claim is not credited |
| INVALID (non-covariant) | The structure is not generated: **CARD-NONGENERATIVE** |

---

## 6. Owner item 5: budget and genuine distinctness

- **BU-1** At most **three frozen cards** for the whole generative route, Stages 3–6 included.
- **BU-2** A slot is consumed at commit, i.e. when the card has a freeze SHA, whatever happens to it afterwards. Withdrawn, INCOMPLETE, VARIANT and intake-rejected cards all consume slots (OD-3).
- **BU-3 Modification.**
  - Any change after freeze creates a new card: to the statement, constants, type, components, truncation, tolerances, scope, response-scope declaration, kill conditions, ℛ★, battery predictions, declared domain or lock design.
  - A modification made after any score was visible is labelled REPAIR.
  - The only exception is a tooling repair that realigns code to the frozen statement. It is logged, its diff is reviewed, and it changes no statement.
- **BU-4 Genuinely distinct.** K_j is distinct from every earlier K_i only if all of the following hold:
  - (a) their clause normal forms differ by more than numeric literals, thresholds, renaming or equivalent rewriting;
  - (b) a certified point lies in the symmetric difference of their realized sets, on an AI-1, AI-2 or AI-4 instance or a lock fiber, or their SEL verdict vectors differ;
  - (c) a certified point lies in Z(ℛ★_i) Δ Z(ℛ★_j) on 𝒜^base;
  - (d) K_j is no variant of K_i, under any of:
    - **VAR-1** a translation of price ≤ ℓ_tr = 32 bits, built from RM moves, renaming and reparametrization of constants, maps Sol(K_i) onto Sol(K_j) on the whole battery universe;
    - **VAR-2** the same normalized skeleton with different constants;
    - **VAR-3 patch**, any one of:
      - one clause added or deleted;
      - one conjunct or disjunct added to or removed from one clause;
      - one clause changed by a VAR-1 or VAR-2 move;
      - K_j = K_i ∧ Q, where Q changes battery verdicts only on items where K_i failed;
      - clause changes worth ≤ b_patch = 4 bits in total;
    - **VAR-4** a changed scope, battery exclusion, extractor, tolerance, truncation or response scope;
    - **VAR-5** a conjunction or disjunction of earlier cards or of their clause sets;
    - **VAR-6** any composition of VAR-1 to VAR-5.

  Failure → **CARD-VARIANT**, and the slot is consumed. The author names the nearest earlier card and argues distinctness (C1). The intake auditor rules. Disputes go to the owner, and until the owner rules the card counts as a VARIANT.
- **BU-5 Draft ledger.**
  - Every draft, in any form, is logged with a hash and a time before it is discarded or developed.
  - A draft found unlogged later → the card is repriced with the corrected n_drafts and flagged.
  - Deliberate non-disclosure → KU-10.
- **BU-6 Sequencing: the batch-freeze rule** (§19.4). No card is scored on any battery, holdout or lock until every card is frozen, or until the route declares its final count.
- **BU-7 Owner's pick.**
  - Only among CARD-ADMISSIBLE cards. The pick costs log₂(N_frozen) bits.
  - If the picked card fails Stage 4 or 5, the owner may take another frozen ADMISSIBLE card, unmodified.
  - **There is no fourth card.**
- **BU-8 No budget laundering.** Any artifact that states a law in L₀ for evaluation is a card. "Proto-laws", "lemma cards" and "pre-cards" are prohibited (SM-4).

---

## 7. Owner item 6: required card contents and kill conditions

### 7.1 Required contents

| Owner-required content | Template fields (§17) |
|---|---|
| Exact law | C2, C3, C4 |
| Information price | C5, C6 |
| Generated structures | C7 |
| Measurable target | C8, C13 |
| Hostile baseline comparison | C12 |
| Kill condition | C14 |
| Declared response scope (STATE) | C9 |

A missing or empty field → **CARD-INCOMPLETE**. The slot is consumed.

### 7.2 Universal kill conditions
These apply automatically to every card.

| ID | Kill condition |
|---|---|
| KU-1 | Sol is empty on an in-domain instance at r★ or r★★, or Sol = 𝒳 |
| KU-2 | Causality violation: signalling from later protocol segments into earlier records; superluminal signalling between blocks in a spatial embedding; violation of pNS in a Bell embedding |
| KU-3 | Positivity violation: negative probabilities; record maps that are not CP; negative spectral densities; negative entropy production under RH-TH |
| KU-4 | Contradiction of an experimentally established standard relation inside its tested domain (FDT/KMS in equilibrium, Onsager–Casimir near equilibrium, energy–momentum conservation, the second law), or of a standard consequence of a regime whose hypotheses the card's own construction meets. The only exception is a contradiction that is the declared ℛ★ and is consistent with existing bounds cited at freeze |
| KU-5 | A mandatory ALLOW anchor is forbidden (§15.8) |
| KU-6 | B-REC is contradicted while those environments are claimed as realizable |
| KU-7 | ℛ★ fails any of Q1–Q12 |
| KU-8 | Any protected structure is RELOCATED |
| KU-9 | A GRAVEYARD idea returns at card level (§21.2) |
| KU-10 | Undisclosed search, or modification after freeze. The card is void |
| KU-11 | ΔL < p★ at p★, or ΔL ≤ 0 at p = 16 |
| KU-12 | LOCK-FALSIFIED (LOCK-VOID included), or a Stage-5 holdout violates ℛ★ beyond the declared error inside the declared scope |
| KU-13 | A card-specific kill condition fires |

### 7.3 Card-specific kill conditions
Each card states its own kill conditions, and together they must meet KP-1 to KP-4:
- **KP-1** Each is finite and decidable on the frozen battery, or is a named experimental outcome.
- **KP-2** Each is reachable: some 𝒮-admissible outcome triggers it. A vacuous kill condition makes the card CARD-INCOMPLETE.
- **KP-3** Each is automatic; there is no reinterpretation after the fact.
- **KP-4** Coverage:
  - at least one observable kill condition on ℛ★, with a threshold;
  - at least one structural kill condition that is decidable at Stage 4 without new theory;
  - at least one on B-SEL or B-DIF.

**No rescue.** Once a kill fires, the card is not repaired.

---

## 8. Owner item 7: originality

- **OR-1** Familiar component theories are allowed and expected. Familiarity is neither a defect nor a credit.
- **OR-2** Novelty is judged **only for the assembled law**: 𝒦 with its generated chain, its qualifying relations and its realized joint set.
- **OR-3 Conjunction test** (mandatory comparator).
  - The conjunction C₁ ∧ … ∧ C_m, with each component stated in its standard form, together with 𝒮, is a comparator.
  - If ℛ follows from it without the card's coupling clauses (located by NR-4), ℛ is not novel.
- **OR-4 Comparator floor.** The auditor may add comparators, and none may be removed. Each must be verified against primary sources at audit time.
  - **SFP-1** Linear and nonlinear response: Kubo; higher-order FDRs (Stratonovich–Efremov; Bochkov–Kuzovlev); Kramers–Kronig; sum rules.
  - **SFP-2** Equilibrium and non-equilibrium statistical mechanics: KMS and FDT; fluctuation theorems (Jarzynski, Crooks, Bochkov–Kuzovlev, Evans–Searles, Gallavotti–Cohen); NESS response (Agarwal, Harada–Sasa, Baiesi–Maes–Wynants); stochastic thermodynamics; typicality and ETH.
  - **SFP-3** Onsager–Casimir, and nonlinear reciprocity (Andrieux–Gaspard).
  - **SFP-4** Projection and GLE: Mori–Zwanzig; Ford–Kac–Mazur; Caldeira–Leggett; Feynman–Vernon.
  - **SFP-5** Open systems and measurement: GKSL; Davies; Redfield; process tensors; input–output theory; quantum regression; imprecision–back-action and the SQL (Clerk et al.); einselection and quantum Darwinism.
  - **SFP-6** Dissipative field theory: Schwinger–Keldysh EFT with dynamical KMS symmetry; MSR / Janssen–De Dominicis; GENERIC.
  - **SFP-7** Mechanisms for differentiation and subsystems:
    - SSB, Landau theory, Goldstone, Mermin–Wagner–Hohenberg;
    - critical phenomena and renormalization;
    - Turing patterns and pattern formation; Cahn–Hilliard;
    - timescale separation and slow manifolds; near-decomposability (Simon–Ando); lumpability (Kemeny–Snell);
    - observable-induced tensor-product structures (Zanardi; Zanardi–Lidar–Lloyd); quantum mereology (Carroll–Singh);
    - Markov blankets (Pearl; Friston); coarse-graining and causal emergence;
    - conserved-charge sectors; graph decompositions; planted-partition and community-detection baselines.
  - **SFP-8** The ten D5 comparators, applied to ℛ and not to ε_R.
  - **SFP-9** Readout classes: measurement invariance; Stevens scale types; IRT linking and equating; interventional-CRL identifiability classes (R1 §12 item 1).
  - **SFP-10** The correlation sector:
    - Abramsky–Brandenburger and AvN; KS sets; Local Orthogonality;
    - reconstructions (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller); JGBB polygons and boxworld;
    - bounded-width CSP and operator assignment (Atserias–Kolaitis–Severini; Bulatov–Živný; Ciardo; Ó Conghaile); Slofstra.
  - **SFP-11** Constructor theory (GY-1).
- **OR-5 Categories** (preregistered; mathematics (M) and physical relation (P) classified separately; none favoured in advance):

| Category | Meaning |
|---|---|
| RESTATED | Up to representation, the image of Sol equals an existing framework's image, and there is no new relation |
| KNOWN ASSEMBLY | The combination already exists in the literature |
| STANDARD COMPONENTS, NEW ASSEMBLY, NO NEW RELATION | Every credited relation follows from the conjunction test or from a comparator |
| DISTINCTIVE | ℛ★ passes Q1–Q12, and neither any comparator nor the conjunction imposes it |

  - **Only DISTINCTIVE (P) for ℛ★ makes a card ADMISSIBLE**, and it is re-confirmed at G5-LOCK.
  - The middle categories may be banked as a COMPRESSIVE known or assembled sector, if S6 passes. They are never banked as a law.
- **OR-6 Procedure.**
  - Each comparator family gets an analyst and a skeptic, and the skeptic is instructed to argue RESTATED. The more conservative verdict governs.
  - **The audit must be complete, with every floor comparator returned, before the owner's pick.** No partial audit is accepted (SD0 stopped at 1/5).
- **OR-7 Timing.**
  - The cheap screens run inside S5: Q3 witnesses, B-SRB, the reverse-direction relations, and B-CF.
  - The full audit is S9.
  - No novelty claim is made before then (RULES 7).

---

## 9. Owner item 8: cross-sector gold standard (parameter transfer)

- **XS-1 Sector.** A sector is σ = (platform class, regime hypotheses H_σ, standard description F_σ ∈ SFP, observable set O_σ, dataset D_σ). The frozen coordinate blocks are:
  - Q: correlation and contextuality (the B-SEL type);
  - Θ: response and reciprocity;
  - 𝔊: gravitational (Stage 6);
  - any further block the owner declares.
- **XS-2 Independence.** Sectors A and B are independent only if all five hold:
  - **SI-1 Data.** The datasets are disjoint and frozen by hash, and no B datum fixes anything in A.
  - **SI-2 Physics.** No degree of freedom, sample or apparatus is shared, apart from generic calibration standards. F_A and F_B share no free parameter that standard physics would fit jointly.
  - **SI-3 No standard bridge.** The Standard Bridge Panel, applied to A's data together with B's standard parameters, must give an interval for the B observable at least Q_min × wider than the transfer prediction. The panel:
    - FDT/KMS; Onsager;
    - Kramers–Kronig and sum rules;
    - dimensional analysis with universality and scaling;
    - symmetry and Ward identities; conservation; ensemble equivalence;
    - Mori–Zwanzig; EFT matching; CLT and large-N.
  - **SI-4 Not a replication.** B is not A at another value of a control parameter within the same H and the same F_σ.
  - **SI-5 Zero-transfer certificate.** Two standard models agree on every A observable but differ on the B target, and standard model pairs realize every combination in a product box of positive dimension around the instance.
- **XS-3 North-Star lock.** In addition, A and B must lie in different regimes among quantum, thermodynamic and gravitational.
- **XS-4 Parameter ledger.**
  - θ_K: constants of the law.
  - θ_dict: dictionary constants.
  - θ_std,σ: standard parameters of sector σ, calibrated without using the target observable.
  - θ_cal: calibration of the ε machinery.
  - The GRUT-specific parameters are θ_K, θ_dict and every discrete choice.
- **XS-5 Protocol.**
  1. Fix θ_K and θ_dict on D_A alone, by a frozen procedure, and freeze them by hash.
  2. Measure θ_std,B independently, and freeze it by hash before B's target data are unsealed.
  3. Preregister a numeric prediction y_B = f_B(θ̂_A), with its band, before B's data are opened.
  4. Refit nothing.
- **XS-6 Prohibited (a GRUT-specific fit in B):**
  - adjusting θ_K or θ_dict on any B data;
  - introducing any new constant;
  - making any discrete choice after B's data are accessible: T tier; which Π (unless 𝒦 selects it); scope; protocol subset; grid or window; coarse-graining; carrier variable or readout representative; estimator or exclusions;
  - a B-side nuisance fit that absorbs the prediction.

  B's standard nuisance parameters may be fixed only from declared B calibration data independent of the predicted quantity, and are priced per instance.
- **XS-7 Gold standard.**
  - **d_B = 0** (no GRUT-specific degree of freedom adjusted in B) and n_B ≥ 1.
  - Transfer gain TG := F_p(𝒜_B^base) − F_p(𝓡_{𝒦,B}(θ̂_A)) ≥ p★.
  - The band is ≤ ¼ of the target's range over 𝒜_B^base.
  - The SI-3 ratio is ≥ Q_min.
- **XS-8 Not credited:**
  - analogy, shared vocabulary or formalism, dimensional analysis, unit conventions;
  - the same functional form with a refitted constant;
  - links inside one sector: FDT linking fluctuation and response is **not** cross-sector;
  - same-regime replications;
  - local back-reaction used as the predicted quantity in the gravitational export.
- **XS-9 Status.**
  - CROSS-SECTOR is awarded only after LOCK-CONFIRMED in B on sealed real data under §3.3, plus an external check (RULES 8).
  - Stage 3 claims none. Cards only declare a transfer plan.
- **XS-10 Stage-6 export.**
  - The same 𝒦, unmodified.
  - ε_R is exported with the same quotient and the same distance used at the lock.
  - Local back-reaction sets θ_cal only. It counts toward θ_K only if it qualifies as sector-A data under SI-1 to SI-5.
  - Any change makes a new card (§6).

---

## 10. Owner item 9: stopping rule and terminals

**T-1 Card terminals.** Each frozen card gets exactly one terminal.
- S0 to S8 are always run and reported. S9 runs on cards that clear S0 to S8.
- The first failing screen in §18.2 names the terminal. Otherwise the card is **CARD-ADMISSIBLE**.
- UNSCORABLE and UNRESOLVED count as failures and are final within the route (DC-7).

**T-2 Route terminals:**
- **STAGE3-PICK:** the owner picks an ADMISSIBLE card, and the route goes to Stage 4.
- **STAGE3-ROUTE-TERMINATED.**
- **STAGE3-OWNER-HALT.**

**T-3 Termination.** The route terminates when any of these holds:
- (a) the budget is spent, or the final count is declared, with no ADMISSIBLE card;
- (b) every frozen ADMISSIBLE card has failed a Stage-4 or Stage-5 gate;
- (c) Stage 6 requires modifying 𝒦 and no unused slot remains.

Termination is recorded in GRAVEYARD, after the external check (RULES 8), and in STATE. The stage stops (RULES 4).

**T-4 Prohibited.** See §20.

**T-5 Allowed after termination:**
- banking DERIVED sub-results as a library, after external check (SD0 precedent);
- banking a COMPRESSIVE known or assembled sector;
- GRAVEYARD lines and the terminal report;
- continuing R1's non-blocking upgrades;
- a new program, but only by a new explicit owner ruling that names it as a new route, with its own charter and no inherited budget, and not as a continuation of or prerequisite for this one.

---

## 11. Addition A1: merge = provenance, not endorsement

- **PV-1** The merge `86bf5a0` and the boundary `dbfd64b` are provenance markers. They change no status. Merging this charter, a card or a result changes no status either.
- **PV-2 Pending items keep their status, and their CHECKS lines stay pending:** A-BL, F, M1–M3, Prop. G, and the D5 analyses (C1–C6, D1–D3).
- **PV-3 Dependency labels.**
  - A score or verdict that depends on a pending or evidence-grade item carries the label "conditional on ⟨item⟩", and banking is blocked.
  - If an external check finds an issue, the affected scores are recomputed under unchanged thresholds.
- **PV-4 Banking.** Nothing is banked until its CHECKS line shows an external check with no open issue (RULES 8). This includes the charter's freeze commit.
- **PV-5 Items used by this charter:**

| Item | Role here | Status |
|---|---|---|
| ε_R definition, T_R1, d_op, verdict table, common-carrier commitment, Prop. E/E1/E2, G2-08 certificate (`82d311e`) | ε code, carrier semantics, NR-11 | Frozen pre-result; checked: Claude |
| Theorems A and C | DEF-2, B-REC, HB-2 calibration | DERIVED; checked |
| A-BL, F, M1–M3, Prop. G | DEF-2, DEF-5, witness enclosures, Tier-2 zero set, B-REC rate | DERIVED; external check pending |
| BRI1 Tier 2 (`cb81a3b`) | B-REC | DERIVED, evidence grade; checked: Claude |
| D5 C1–C6, D1–D3, regime restatement, reverse-direction relations, M-A/M-A′/M-B, C2-F′ | Hostile baseline, B-REC, DEF-9, DEF-10 | D5 ANALYSIS; evidence grade; not externally checked |
| 10-item checklist, instantaneous-state form, Z_A, [h]_T, MI framing | MC-6 (adopted as a Stage-3 rule); not-credited seeds | POST-RESULT SEED |
| SD0 counts 2961 / 1721 / 1232 / 8, the 240 gap, 2721, the PR-forcing lemma | B-SEL, harness validation | DERIVED, exact |
| SD0 T1 | FC-2 structural discount | SD0 record (structural) |
| SD0 T2 (2-SAT equivalence) | B-CF behaviour | UNRESOLVED, pending review |
| ASP (`aacbc52`) | B-CF member | COMPRESSIVE, known sector (#6) |

- **PV-6 Scoreboard mapping** (each after external check):

| Outcome | Status |
|---|---|
| Card frozen and ADMISSIBLE | COMMITMENT (priced) |
| 𝒦 ⇒ ℛ★ proved | DERIVED |
| SC2 met | COMPRESSIVE |
| LOCK-CONFIRMED on sealed real data | PREDICTIVE |
| §9 passed | CROSS-SECTOR |
| An NR violation, or LOOKUP | RELOCATED |
| B-SRB, an SFP comparator or the audit restates it | RESTATED |
| A kill | GRAVEYARD entry |

---

## 12. Addition A2: ε_R is derived

- ε_R = ε[Γ_Π, T_Π] by definition. It is computed only by charter code, from the card's Γ_Π and T_Π (and s_T where needed).
- 𝒜_ε is the image of 𝒜_Γ × 𝒜_T. It is never an independent axis, and no bits are ever counted on it.
- A qualifying relation restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition (Q2), and it couples interface with response (Q5).
- The claim "ε_R > 0 somewhere" is not credited; R1 already has BRI1.

**Definitional relations: never credited.**
- **DEF-1** ε_R = ε[Γ_Π, T_Π], and any algebraic rewriting of it.
- **DEF-2** ε_R ≥ 0; ε_R = 0 if and only if the family is T-separable (Theorems A, A-BL and M1); ε_R ≤ 2.
- **DEF-3** ε_R ≡ 0 when |A| = 1.
- **DEF-4** Monotonicity in T: T ⊆ T′ ⇒ ε^{T′} ≤ ε^{T}. Zero sets are monotone along the ladder.
- **DEF-5** Witness bounds with frozen constants, and their consequences for any family:
  - Theorem F: ε = ½·d_q for two protocols with a symmetric P0; ε ≥ ½·|E f_odd|/‖f‖_BL;
  - M2, Prop. B, and the rate in Prop. G.
- **DEF-6** Invariance under h ↦ t∘h for t ∈ T.
- **DEF-7** Data-processing and garbling identities, and invariance-reduction identities (Blackwell plus Lehmann; D5 §3 B).
- **DEF-8** The logic of the R1 verdict table.
- **DEF-9** Triviality and representation statements:
  - Prop. E and E1; D5 Theorems D1 and D2;
  - ε^{T_univ} ≡ 0;
  - the time-marginalization facts of the ladder.
- **DEF-10** D5's four-cell independence of (Markov or not) × (ε zero or positive), and its one-way links:
  - Markovianity that differs across protocols ⇒ ε^mono > 0;
  - ε^mono > 0 ⇒ restricted process-tensor non-Markovianity.
- **DEF-11 Tautology test.** Any statement true for every well-typed tuple of 𝒟(ι).

---

## 13. Addition A3: baseline after standard theory

### 13.1 The rule
The standard constraint set 𝒮 is imposed before any freedom is counted. Relations implied by 𝒮 earn nothing.

### 13.2 Regime hypotheses
Each hypothesis holds at a realization x when its condition is true at x.

| RH | Holds when |
|---|---|
| RH-HAM | S+E evolve under a closed generator at record resolution |
| RH-KMS | The reference state of E (or of S+E) is KMS or Gibbs for the realized generator, within lock resolution |
| RH-MR | The dynamics is microreversible, with parities and field reversal |
| RH-MK | The records or the reduced dynamics are Markov at record resolution |
| RH-GAU | E is Gaussian or harmonic, with coupling linear in E's variables |
| RH-SYM(G) | The reference law and the dynamics are invariant under a group G |
| RH-CQ | The dynamics has conserved quantities |
| RH-WC | Weak coupling or timescale separation holds |
| RH-LIN | The readout is a linear detector of a weakly coupled E observable |
| RH-MF | E is N weakly coupled units with a normalized collective readout |
| RH-NESS | The dynamics is stationary non-equilibrium Markov |
| RH-ORD | An ordered phase, a critical point or a pattern-forming instability is present |
| RH-TH | Macroscopic thermodynamic regime |

### 13.3 Standard constraints STD-1 to STD-12
For each constraint: the hypotheses under which it applies, what it imposes, and what therefore earns no credit.

- **STD-1 Causality.** Applies always.
  - Non-anticipation: protocols that agree on [0, t] give the same record laws on τ ∩ [0, t].
  - Response functions are retarded, and Kramers–Kronig holds.
  - No-signalling holds, i.e. pNS for multi-block supports; relativistic causality holds in spatial embeddings.
  - T_caus ⊂ T_lin.
- **STD-2 Positivity.** Applies always; the quantum part applies once Hilbert-space structure is supplied or generated.
  - Probability laws are valid; covariances and spectral densities are positive semidefinite (Bochner).
  - Processes are CP (positive combs; GKSL form for Markov semigroups).
  - Uncertainty and Tsirelson-type bounds hold once quantum structure is present.
  - Interface maps preserve validity. If quantum structure is supplied, these bounds are also RELOCATED (IP-6).
- **STD-3 KMS / FDT / fluctuation relations.** Applies under RH-KMS with RH-HAM; the NESS forms need RH-NESS and RH-MK.
  - KMS holds for every multi-time correlator.
  - Linear FDT: classically χ_AB(t) = −β·θ(t)·(d/dt)⟨A(t)B(0)⟩; in the quantum case through the KMS factor.
  - Higher-order response is fixed by equilibrium correlators (Kubo, Stratonovich–Efremov, Bochkov–Kuzovlev, quantum nonlinear FDRs).
  - The fluctuation theorems hold for every protocol.
  - A Gaussian E is fixed entirely by (J(ω), β), including its exact exogenous decomposition (Feynman–Vernon, Caldeira–Leggett, Ford–Kac–Mazur).
  - The NESS forms are Agarwal, Harada–Sasa and Baiesi–Maes–Wynants.
  - Under RH-KMS, RH-GAU and linear coupling, 𝒜_ε = {0}. Under the BRI1 class, the leading Tier-1 value is fixed by the reference 4-point function: ε_R = (V*/12)·|γ₁|·(1 + 0.235/N_B + …), with sharpness at D5 evidence grade.
  - **No credit for:** any ε value or Γ restriction fixed by equilibrium correlators among the same inputs; any fluctuation-theorem identity; "harmonic baths are R1-NULL".
- **STD-4 Onsager–Casimir.** Applies under RH-MR with RH-KMS; nonlinear forms follow from current fluctuation theorems.
  - L_ij(B) = ε_i·ε_j·L_ji(−B), and χ_AB(t; B) = ε_A·ε_B·χ_BA(t; −B).
  - Nonlinear reciprocity identities.
  - R1's operational "reciprocity" is a different thing. A relation that reduces to Onsager–Casimir symmetry earns nothing under either name.
- **STD-5 Conservation and symmetry.** Applies under RH-CQ and RH-SYM(G).
  - Continuity equations, f-sum and moment sum rules, Ward identities.
  - Curie and selection rules: a symmetric reference read through a covariant interface has no odd statistics. This is Theorem C's mechanism.
  - Energy and momentum balance, i.e. action–reaction.
  - Charge and superselection partitions are standard selectors.
- **STD-6 Mori–Zwanzig / GLE.** Applies under RH-HAM with Π supplied.
  - There is an exact GLE: a memory kernel plus projected noise. A Gibbs E gives the second FDT.
  - RH-WC gives the Markov limit.
  - A harmonic E gives exogenous noise plus linear memory exactly.
  - **No credit for:** memory, non-Markovianity, viscoelastic response, or "E carries S's history".
- **STD-7 Open-system and measurement response:**
  - GKSL (RH-MK); Davies (RH-WC with RH-KMS); Redfield; quantum regression (RH-MK);
  - process tensors (always available); influence functionals (RH-GAU);
  - input–output theory, b_out = b_in + √γ·a;
  - the imprecision–back-action bound S̄_xx·S̄_FF − |S̄_xF|² ≥ (ħ/2)², and the SQL (RH-LIN);
  - measurement rate ≤ dephasing rate.
  - **No credit for:** any interface–response tradeoff of these kinds.
- **STD-8 Stability and the second law.** Applies under RH-TH or RH-KMS.
  - Entropy production ≥ 0; passivity; Clausius; Landauer; positive-definite static susceptibilities; Le Chatelier–Braun.
- **STD-9 Large-N, CLT and Edgeworth.** Applies under RH-MF.
  - The r-th cumulants of a normalized collective readout scale as O(N^(−(r−2)/2)), and reservoir limits are Gaussian.
  - **No credit for:** N-scaling laws of ε_R or of its witnesses.
- **STD-10 Standard relations between differentiation and response.** Applies under RH-ORD.
  - Goldstone; Mermin–Wagner–Hohenberg.
  - Scaling relations (Rushbrooke, Widom, Fisher, Josephson); susceptibility versus correlation length; Landau mean-field relations.
  - Interface tension and stiffness; Turing wavelength selection; slow-manifold selection of persistent variables.
- **STD-11 Representation freedom.** Applies always.
  - Only T-invariants are observable.
  - Readout classes, maximal invariants, copulas modulo reflections and measurement invariance are known mathematics.
  - **No credit for** the existence or form of [h]_T as such.
- **STD-12 Universal exogenous representation.** Applies always; this is mathematics.
  - Every non-anticipating family has an exact exogenous representation with protocol-dependent readouts, even causal linear ones (Prop. E/E1; D1; D2).
  - **No credit for** any back-reaction claim made from records alone, or any relation that does not involve the derived carrier.

### 13.4 Closure
- 𝒮 includes every relation derivable from STD-1 to STD-12 by published standard theorems, the fluctuation theorems included (OD-7).
- An auditor who cites such a derivation moves the relation into 𝒮.
- The stricter reading governs until the owner rules.

### 13.5 Precedent fixed in advance
- BRI1's Tier-1 ε_R value lies in 𝒮: it is a Kubo/FDT third-cumulant response fixed by P0's connected 4-point function (D5).
- So does any relation that expresses ε_R through the same environment's equilibrium correlations.

### 13.6 RECOVERY
- Generating KMS or Gibbs states, thermalization or memory from dynamics is standard (typicality, ETH, Davies, ergodic theory).
- It earns RECOVERY, a Stage-6 consistency item, and zero Stage-3 credit.

### 13.7 Regimes where FDT is silent
- There the baseline is larger. Credit is computed per regime class.
- Regime shopping is defeated by BP-3 and BP-4.

### 13.8 D5 reverse-direction relations
These are baseline relations that comparators give and R1 does not:
- (i) for a Gibbs environment driven through the recorded variable, the FDT predicts the leading Tier-1 ε from undriven 4-point correlations;
- (ii) the GLE / linear-response route detects linear back-reaction;
- (iii) process-tensor signalling detects the harmonic bath's response.

ℛ★ must be none of these and must not be implied by them in its lock fibers.

---

## 14. Addition A4: response scope

At freeze, every relation declares exactly one scope.

- **SCOPE-Q: quotient-irreducible back-reaction.**
  - The relation constrains Γ only through T_Π-invariant content: ε_R, its zero set, its witnesses, or the maximal invariant.
  - It is measured under R1's verdict table.
  - It is silent on mean response of every order, on linear back-reaction, and on affine or Gaussian latent change.
  - Linear-response data can neither confirm nor refute it.
- **SCOPE-G: response in general.**
  - Its observables are response functionals: susceptibilities, response functions, noise spectra, transport coefficients. **It is never stated through ε_R alone**, because ε_R is blind to linear response.
  - B-SRB applies at full strength, starting with STD-3 (linear FDT), STD-4, STD-7 and STD-1.
  - D5's comparators 2 and 3 in the reverse direction are mandatory baselines.
- **SCOPE-MIX.** Two relations, each declared and scored separately. This uses the card's two-relation maximum.

**Rules.**
- **RS-1 R1-NULL does not mean "no response."** A claim of the form "ε_R = 0 ⇒ no back-reaction", or "ε_R > 0 ⇒ the environment is nonlinear", is void. A relation whose derivation uses such a claim fails Q10. The harmonic bath responds yet is R1-NULL; the parametric harmonic control escapes both tiers with linear bath dynamics.
- **RS-2 No cross-subsidy** between scopes.
- **RS-3 Battery emphasis.**
  - SCOPE-Q faces B-REC first: it must predict ε_R = 0 wherever RH-GAU with linear coupling holds. Then B-HB.
  - SCOPE-G faces B-SRB first: STD-3 and STD-7.
- **RS-4** A mismatch between scope and lock observable voids the lock. A SCOPE-G relation stated only through ε_R is reclassified as SCOPE-Q, and its credit is limited to its quotient-irreducible part.
- **RS-5** No scope declared → CARD-INCOMPLETE. A change of scope after freeze is a new card.
- **RS-6** The card states which carrier verdict it expects at measurement, and how that verdict will be certified.

---

## 15. Frozen battery and gates

**General rules.**
- The batteries are frozen with the charter. Cards may not add, remove or reweight items.
- The public items are development data: they earn credit only under FC-2. Sealed holdouts and post-batch seeds exist for that reason.

### 15.1 B-SEL: the selectivity battery (exact SD0 record and code)

**Operational embedding.**
- Emb is uniform and priced. It maps a scenario Σ into Ξ-instances:
  - measurements → interventions;
  - contexts → jointly performed protocol sets, under the card's declared compatibility notion (FR6);
  - outcomes → records;
  - **parties and sites → generated blocks of Π.**
- The admitted family is 𝔖_𝒦(Σ) := {supp Γ_Π : Ξ ∈ Sol_𝒦(Emb(Σ))}. **The object is the set of supports of record laws.**
- **ALLOW** means the card exhibits, or proves the existence of, a realization with exactly that support. **FORBID** means it proves no realization exists.
- If neither is decided, the item is UNSCORABLE (§16). A card that cannot embed Bell scenarios fails G-SEL.

| ID | Instance | Requirement | Class |
|---|---|---|---|
| SEL-0 | Every embedded instance | ∅ ≠ Sol ⊊ 𝒳 | Mandatory (structural; earns 0) |
| SEL-1 | The 1721 possibilistically local (2,2,2) tables | ALLOW all | Mandatory anchor |
| SEL-2 | The Hardy support (SD-K2) and its orbit under the 128-element relabelling group | ALLOW | Mandatory anchor |
| SEL-3 | The 8 PR boxes | FORBID all | Mandatory |
| SEL-4 | The 240 pNS (2,2,2) tables with no exact-support realization | FORBID all, as record-law supports | Mandatory (automatic for no-signalling record laws; earns 0) |
| SEL-5 | GHZ (3,2,2) | ALLOW | Mandatory anchor |
| SEL-6 | Peres–Mermin square | ALLOW | Mandatory anchor |
| SEL-7 | The CHTW 3×3 KS game over the certified core of 94 rays and 67 triads (`f0_sd0_k6_core.json`) | ALLOW | Mandatory anchor |
| SEL-8 | Mermin pentagram (H2); bipartite magic square; CEG-18 bipartite; GHZ (4,2,2) (G1) | ALLOW all | Mandatory anchors |
| SEL-9 | The SD-K7(i) frozen family (`f0_sd0_evaluate.py`): PR ×8; the 480 strong XOR-(2,3,2) tables; embedded PR (2,3,2); fine-grained PR | FORBID all | Mandatory |
| SEL-10 | The theta parity system: {p,q,r} even, {p,q,s} even, {r,s} odd (no operator model; J = e) | FORBID | Mandatory (OD-2) |
| SEL-11 | SD-K8: qubit versus boxworld gbit, both of capacity 2 | Exclude the gbit's PR realization. The responsibility map contains no clause on capacity, dimension, party count or setting count | Mandatory audit |
| SEL-12 | SD-K9 closure: mixing-union over whole admitted families; independent products (Hardy ⊗ GHZ admitted; PR ⊗ PR forbidden) | Respected | Mandatory (structural; earns 0) |
| SEL-13 | Specker triangle; chained-PR 6-cycle; C7 odd-cycle box (H1) | FORBID | Graded |
| SEL-14 | Padded-PR (2,2,3) | Reported (quantum status unknown); no credit either way | Report |
| SEL-15 | G2, G3, H3, H4 | Reported against their literature status | Report |
| SEL-16 | K7(ii): audit against the POVM-inclusive BMT boundary | Recorded. UNRESOLVED is allowed for a card that is blind to dimension | Audit |
| SEL-H | At least 3 blind holdouts (§15.9) | Literature status; tallied separately | Holdout |

**Grades.**
- **EXACT-ON-BATTERY:** every mandatory and every graded item passes.
- **OUTER:** every mandatory item passes, and some graded FORBID is over-allowed. It is labelled an outer approximation and is never upgraded (FR9).
- **NON-SELECTIVE:** any mandatory failure.
- Forbidding an anchor also fires KU-5.

**G-SEL PASS** requires at least OUTER, SEL-11 passed, and the consistency-collapse check of §15.2.

### 15.2 B-CF: the consistency family
- **Members:** k-consistency for k = 1, 2, 3; Singleton Linear Arc-Consistency; ASP (SCOREBOARD #6).
- Their SEL verdict vectors are computed by the harness before Card 1.
- **Consistency collapse.** If a card's SEL vector equals that of a B-CF member, or its FORBID set equals the set that k-consistency refutes for some k ≤ 3, then:
  - its selectivity is KNOWN SECTOR and D_sel = 0;
  - the CSP comparators (SFP-10) become mandatory in its audit.

### 15.3 B-REC: R1 calibration controls (exact-identity controls; no credit)
Each record is fed through the card's Γ_Π interface into the charter's ε code. The output must reproduce the recorded value.

| Control | Required value | Grade |
|---|---|---|
| BRI1 X1, Duffing bath, Gibbs; protocols P0, P1, P2; grid (π, 3π/2, 2π) | Theorem C sign structure; ε_R = ½·d_q for two protocols | DERIVED (C checked; F pending) |
| BRI1 rate | liminf N_B·ε_R ≥ \|K\|·V*/(12·m₂^(3/2)), V* = 0.943578 | Prop. G pending |
| BRI1 Tier 2 | R1-PASS (odd 7/7, even 3/3, scaling as 1/N_B) | Evidence grade |
| Harmonic twin | ε_R = 0 at both tiers (≈ 1.27×10⁻¹⁴); the bath responds through friction | DERIVED (numerical control) |
| Parametric harmonic control | ε_R > 0 at both tiers, with linear bath dynamics | D5 analysis |
| C2-G, C2-NG | 0 | R1 record |
| C2-F (colored AR(1)) | > 0 under E₂±; 0 under T_lin with calibrated filters | R1 record |
| C2-F′ (genuinely non-Markov exogenous) | 0 | D5 analysis (exact predictor weights only) |
| M-A (Markov); M-A′ (non-Markov) | ε_R^{T_R1} ≥ 1.915×10⁻² | D5 analysis |
| M-B | ε_R^mono ≥ 7.98×10⁻³ | Evidence grade |
| E2 | ε_R > 0 with no response. The pipeline never returns R1-PASS | Frozen pre-result |
| Prop. E product latent (HB-9) | MODE SELECTION | Frozen pre-result |

- For each control the card also reports whether it lies in Im(Sol), and its ℛ value.
- Any relation linking ε_R to Markovianity must respect DEF-10.

### 15.4 B-HB: the hostile standard-model library (frozen)

| ID | Family | Regime | Role |
|---|---|---|---|
| HB-1 | Harmonic bath, bilinear coupling, Gibbs | G-cl | R1-NULL while responding |
| HB-2 | Duffing / BRI1-class bath, Gibbs; quartic λ ∈ [0, 2] | G-cl | Tier-1 PASS; Kubo third-cumulant response |
| HB-3 | Exogenous Gaussian (C2-G) | X | Exact zero |
| HB-4 | Exogenous affine-entry non-Gaussian (C2-NG) | X | Exact zero |
| HB-5 | Exogenous filtered non-Gaussian with calibrated filters (C2-F, C2-F′) | X | T-dependence of the zero set; non-Markov null |
| HB-6 | Markov responding environment (M-A) and its non-Markov variant (M-A′) | N | ε > 0 with and without memory |
| HB-7 | Parametric coupling to a harmonic bath | G-cl | Escapes both tiers with linear bath dynamics |
| HB-8 | Gaussian latent configural change (the E2 class) | X / 0 | ε > 0 with no response |
| HB-9 | Product latent with selection readouts (Prop. E / D1) | — | MODE SELECTION control |
| HB-10 | Quantum systems of ≤ 4 qubits or qutrits; local Hamiltonians from an ensemble frozen by the harness; KMS reference; Hamiltonian coupling; fixed measurement model | G-q | Quantum standard witnesses |
| HB-11 | Two-temperature or driven steady-state baths | N | Non-equilibrium witnesses |
| HB-12 | Finite Markov jump processes with local detailed balance; discrete records | N / G | Discrete-record chart |

- **Ranges:** β ∈ [0.25, 4]; frequencies ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8.
- Members may be composed by juxtaposition or by Hamiltonian coupling.
- Cards may add witnesses, and each added witness is verified independently for 𝒮-admissibility and for realization by a standard model. **The evaluator adds no witnesses.**
- **Containment report:** which HB members 𝓡_𝒦 contains. Q3 implies that some standard member is excluded in every lock fiber.

### 15.5 B-SRB: standard response theory with the same inputs
- **Input:** exactly what the card's prediction consumes:
  - (Π, Z, [h], T) as generated, treated as supplied;
  - the reference laws and correlators used;
  - the platform parameters;
  - H(x).
- **Procedure:** the auditor computes I_SRB(o) from STD-1 to STD-12 under BP-3 and BP-4, using SFP-1 to SFP-6, before anything is unsealed.

| Outcome | Verdict |
|---|---|
| I_K ⊇ I_SRB, or \|I_SRB\|/\|I_K\| < Q_min | RESTATED. Precedent: BRI1's Tier-1 value is a Kubo/FDT quantity |
| I_K ∩ I_SRB = ∅ under experimentally established hypotheses | KU-4, unless this contradiction is the declared ℛ★ and is consistent with existing bounds |
| Otherwise | PASS; b_meas is computed |

### 15.6 B-NULL: the nulls
- **NULL-ΠT.**
  - Ξ is any SFP model of the declared type; Π, Z, [h] and T are chosen by hand; Γ = Obs. Its realized set is 𝒜(ι | H).
  - Price(NULL-ΠT) = log₂|𝒜_Π| + log₂|𝒜_T| + log₂(the number of φ-cells for Γ) + its framework choice.
  - Required: 𝓡_𝒦 ⊊ 𝒜(ι | H); some qualifying ℛ holds on 𝓡_𝒦 and fails on 𝒜; and §4.4.
- **E-B twin.**
  - For every realized Γ, the auditor builds the product latent μ = ⊗_a P_a with h_a = π_a, and its causal prefix-tree version.
  - Reciprocity statements must rest on a derived carrier; otherwise the verdict is NO RECIPROCITY VERDICT.
  - ℛ★ or the derived carrier must exclude the twin. A relation satisfied by the E-B twin of every family is record-only and earns no reciprocity credit.
- **Information nulls:**

| Null | What happens |
|---|---|
| Lookup law ("Ξ is one of the listed realizations") | Its price equals the table; the card must beat it |
| Definitional law (R1 definitions plus the verdict table) | Credited 0 |
| Maximal-interface null (T ⊇ J or T_univ) | ε ≡ 0; ε-relations are void |
| Single-protocol or hand-picked repertoire | The relation is a table |
| Sign-only null | At most 1 bit; fails Q6 |

### 15.7 B-DIF: the differentiation battery
The evaluator generates these instances from the declared type, with seeds committed after the batch closes:
- (i) a null-witness search, which feeds NR-3;
- (ii) symmetric instances (AI-2), which feed NR-5;
- (iii) a planted, decoupled instance, as an extractor sanity check with no credit;
- (iv) horizon doubling: at (2η, 2H) the same Π must be found;
- (v) random solution instances at the declared truncation;
- (vi) the AI-3 generic ensemble;
- (vii) perturbation instances for DIF-6;
- (viii) an SFP-7 comparison on AI-2 and AI-3. If Π is extensionally a standard mechanism (same Π from the same data), the result is STANDARD-MECHANISM: allowed, but with no differentiation novelty. If ℛ is an STD-10 relation, it is RESTATED.

### 15.8 Anchors
- **Mandatory ALLOW anchors:** SEL-1, SEL-2, SEL-5, SEL-6, SEL-7 and SEL-8.
- **Standard-regime anchor.** For every B-REC scenario inside the declared scope, Im(Sol) contains at least one triple realized by an experimentally established standard regime (equilibrium FDT and Onsager behaviour).
- Forbidding an anchor is a FAIL and fires KU-5. Freedom reduction obtained by forbidding anchors, or by emptying Sol, earns nothing.

### 15.9 Sealed holdouts
- **Protocol.** `F0_SD0_HOLDOUT_PROTOCOL_01.md`, adapted.
  - The Selector is invoked only after the batch closes, i.e. once every card SHA exists.
  - It receives the protocol, the exclusion lists, the scenario conventions and each card's bare input/output signature, and nothing else.
  - The selection is committed by hash before any evaluation on the selected cases.
- **Pools:**
  - (a) Selectivity: support-level cases with an established classification (eligibility E1–E4), excluding everything in §15.1, G1–G3, H1–H4, and the whole (2,2,2) scenario. At least 3.
  - (b) Reciprocity: standard-model environments with computable ε_R, outside the frozen HB members and parameter points. At least 3.
  - (c) AI-5 instances.
  - (d) LOCK-H datasets, chosen at Stage 5 (MC-8).
- Holdout results are tallied separately and never enter ΔL. A failure on an item of mandatory type fails the gate (NR-16).

### 15.10 Stage-4 gates (picked card only)
Each is recomputed by an agent that did not build the card, checked externally before banking, and followed by checkpoint (e).

**G4-SEL.** §15.1 and §15.2, recomputed, including SEL-H.

**G4-DIF.**
- **DIF-1** Π is computed by the frozen algorithm on every in-domain solution.
- **DIF-2** Persistence holds (δ_Π, η, δ_∂, H) across A_{r★★} and the whole horizon, and horizon doubling passes.
- **DIF-3** Π is nontrivial (§1.3).
- **DIF-4** Π is GENERATED-STRONG or GENERATED-WEAK.
- **DIF-5** The carrier, [h] and T_Π are GENERATED:
  - T_Π ∈ 𝕃_T^adm;
  - T_Π is nontrivial: some B-REC or B-DIF family has ε^{T_Π} > 0 and some has ε^{T_Π} = 0;
  - T_Π is placed relative to T_R1, T_mono and J;
  - T_Π is not a GY-11 or GY-12 class.
- **DIF-6** Π is unchanged within δ_Π under relative perturbations of 2^(−p★) applied to every numeric input while preserving Aut(inputs), and under the card's declared ε_C ≥ 2^(−p★).
- **DIF-7** Universality: on all of Sol, on every in-domain instance. The domain contains AI-1, AI-2 and at least θ_gen = 0.9 of AI-3.
- **DIF-8** Covariance (NR-8).
- **DIF-9** The environmental identity across interventions, and the environment's state variable, are outputs.
- **DIF-10** The B-DIF (viii) classification is recorded.

**G4-NR.** NR-0 to NR-16 are re-run computationally on AI-1 to AI-5. The reader and decoder batteries are run by an agent that has not seen the card's derivation of Π.

### 15.11 Stage-5 gates
- **G5-LOCK.**
  - Q1–Q12 and the scope are re-verified independently at r★ and r★★.
  - DISTINCTIVE (P) is re-confirmed.
  - The LT-1 design is preregistered.
- **G5-HOLD.**
  - After G5-LOCK, a hostile auditor selects at least max(2, number of lock observables) holdouts. Each is a physically realized system class inside the declared scope that the card does not reference.
  - Their hashes are committed before the prediction is evaluated.
  - **PASS:** ℛ★ holds within the declared error on every holdout. A certified violation inside the scope fires KU-12.
  - A preregistered prospective experiment may replace a holdout.
  - Only sealed real data can confer PREDICTIVE.

### 15.12 Stage 6 (pointer only)
- The same 𝒦, unmodified, must yield the quantum, thermodynamic and gravitational regimes.
- ε_R is exported as in XS-10.
- Memory, viscoelasticity and crystalline order are checked as effective regimes after Stage 4.
- B-SEL OUTER cards carry a flag on the quantum regime.

---

## 16. Decidability and scorability

- **DC-1 Total procedures.** Every gate predicate, Sol membership, and every chain map at r★ and r★★ needs a frozen decision procedure and a termination argument: a proof, or a finite bound on an enumeration.
- **DC-2 Resources.** The card declares time and memory per item. The evaluator allows κ = 10 times that. An item that exceeds the allowance is UNSCORABLE.
- **DC-3 Exactness.**
  - Zero tests, equalities and memberships are decided in exact arithmetic (ℚ or algebraic numbers), or by certified intervals separated from the decision boundary by at least 2^(−p★).
  - A tolerance-based "≈ 0" is UNSCORABLE, unless the tolerance is part of the frozen law, in which case it is priced and its robustness is checked.
- **DC-4 Unbounded quantifiers** (over all dimensions, all n, all extensions) need a frozen finite truncation level. That level is part of the law, is priced, and is what gets scored. Claims about the limit earn nothing.
- **DC-5 Possibly undecidable targets.**
  - Items that are only semi-decidable and do not terminate are UNSCORABLE.
  - Exact quantum correlation and support families may be undecidable (Slofstra; flagged but not audited in SD0). A card claims only a declared outer or inner approximation of such a target.
  - Claiming an exact characterization requires a proof. Without one the card is CARD-UNDECIDABLE, or labelled OUTER.
  - No exactness is claimed beyond the battery (FR9).
- **DC-6 Gate semantics.**
  - A gate is PASS only if every mandatory item is scored and passes.
  - A mandatory item that is UNSCORABLE makes the gate UNSCORABLE, which means not passed. Such a card cannot advance and counts as a budget failure.
  - Its GRAVEYARD line reads "UNSCORABLE AT FROZEN BATTERY", not "refuted".
- **DC-7 No pending status.** An UNSCORABLE verdict is never reopened within the route, whether by later tooling, a larger κ or another truncation level. A different truncation level would in any case be a new card.
- **DC-8 Cards built only from consistency conditions** are flagged at intake.
  - To earn D_sel, they must survive §15.2.
  - To claim differentiation they must satisfy FR8: their C7 algorithm must compute Π as an output. A veto does not generate Π.
  - To have ε_R values they need a weight rule within supports (FR15(b)). That weight rule is then the actual law, priced and judged as such. Without it, the card is CARD-UNMEASURABLE.
  - Their quantum claims are capped at OUTER.
- **DC-9 Reference implementation.** It is frozen with the card and run unchanged. Changing it is a modification (BU-3), except for a tooling repair.

---

## 17. Required card template (fields)

Each card is one committed file plus its reference implementation. The SHA is recorded before any scoring. Every field is mandatory.

| Field | Content |
|---|---|
| C1 Identity | Card number; slot; freeze SHA; charter SHA; n_drafts and τ_sel; the nearest earlier card and the non-variant argument (BU-4); designer provenance: how the card was produced, the alternatives considered, and the evaluations the designer had seen |
| C2 Exact law | 𝒳 and V_Ξ; the type of 𝒞 and its declared meaning (FR11); 𝒦 in L₀ plus priced vocabulary, with every quantifier explicit; clause normal form and normalized skeleton; the notion of solution; truncation levels; uniform instantiations at r★ and r★★, with no case splits; the reference implementation |
| C3 Ontology declarations | Gluing and composition as an explicit act (FR2); the source of temporal order and of the time unit (FR7); compatibility scope and Emb (FR6); subsidiary possibility dependencies (FR14); the G0-trichotomy landing, which must address (b) weights within supports (FR15) |
| C4 Decidability | Procedures, termination arguments and resources per item; approximation status for targets that may be undecidable (§16) |
| C5 Price ledger | §4.6 in full, with hostile family sizes and search disclosure |
| C6 Input inventory | §5.2; the expected outcome of every NR test; any declared supplied structures |
| C7 Generated structures | Π (δ_Π, η, δ_∂, H); the derivation of Z_Π and the carrier; [h]_{T_Π}; T_Π, with its placement and s_T if needed; Γ_Π = Obs_Π(Ξ). For each: algorithm or proof, responsibility map, grade (DERIVED, evidence or conjectured), and expected NR label |
| C8 Lock register | ℛ★: formula, normalization, coordinates, rectangle witness, lock fibers, I_𝒦, claimed codimension, the derivation 𝒦 ⇒ ℛ★ with its grade, W-std per framework and regime, W-pipe, and the DEF-test argument. An optional second relation is given in the same format |
| C9 Response scope | Per relation (§14); evidence of non-vacuity; the expected carrier verdict at measurement and how it will be certified |
| C10 Certificates | Q1–Q12, as code plus machine-readable output |
| C11 Freedom and compression | ΔF(ι) with its terms; b_struct; b_meas; claimed D_sel; Price; ΔL and ρ at p = 6, 10 and 16; the two-part comparison with NULL-ΠT |
| C12 Hostile baseline | (a) The regime map H(x) for every realization class, and the hostile fibers. (b) The attempted derivation of ℛ★ from 𝒮 and why it fails, with the predicted I_SRB. (c) The B-HB witnesses, the closest HB family, and why ℛ★ does not follow from it. (d) The D5 reverse-direction relations. (e) B-CF. (f) The conjunction test. (g) The predicted outcome of every battery item |
| C13 Measurable target | The LT-1 instantiation: the operational definition of each coordinate (which S channel is intervened, which E readout is recorded, what calibration fixes T_Π); the identification plan; platform class; A; tier; estimator; I_K with its uncertainty, truncation included; effect size against the nearest certified standard witness; σ budget; N_req; power; platform time; sealing route; the declared scope domain |
| C14 Kill conditions | Acknowledgement of KU-1 to KU-13; the card-specific kill conditions, meeting KP-1 to KP-4 |
| C15 Selectivity interface | Emb; the support object (record-law supports); every SEL verdict, with its decision procedure |
| C16 Audit instances | AI-1; the input type for the AI-3 reference measure; the chart φ with windows and resolution; the declared domain and its price |
| C17 Representation | The declared moves (including RM1–RM5) and the covariance argument. No unique formula for h |
| C18 Tradeoff declaration | Whether any monotone identity–response relation appears. If so, its derivation from 𝒦 and the W-pipe for the opposite sign |
| C19 FR and GY standings | The tables of §21 |
| C20 Dependencies, transfer, non-claims | Labels on pending R1 items; the transfer plan, declared only (the θ ledger, the sector pair, the transfer observable, the planned SI witnesses); explicit non-claims |

---

## 18. Scoring procedure, step by step

### 18.1 Sequence
0. **Preconditions.** The charter is frozen; the harness work order is validated (§19.3); the B-CF vectors and the Appendix-B coder are tested.
1. **Draft ledger.** Every draft is logged (BU-5).
2. **Card freeze.** Each card is one commit with its SHA, the reference implementation and C1–C20, battery predictions included, before any evaluation. τ_sel is computed.
3. **Intake** (static, per card, by the Intake auditor):
   - S0;
   - S1: the variant check and the GY declarations;
   - S2: the decidability declaration;
   - the static NR tests: NR-0, NR-1, NR-2 and NR-14.

   The results are recorded. They are not gate scores.
4. **Batch close.** Every card is frozen, or the final count is declared (§19.4).
5. **Selection.** The Selector fixes and commits by hash: the AI-3 seeds, the AI-2 constructions, the B-DIF and NR-8 seeds, SEL-H, the reciprocity holdouts and AI-5.
6. **Evaluation.** The Evaluator runs screens S0–S8 on every card. S9 runs on every card that clears S0–S8.
7. **Recomputation.** A second agent recomputes every screen result before anything is reported.
8. **Checkpoint (d).** At most 5 lines per card. The owner picks among the ADMISSIBLE cards, or the route terminates.
9. **Stage 4** on the picked card (§15.10), with checkpoint (e) after each gate.
10. **Stage 5** (§15.11): G5-LOCK, G5-HOLD and the LT-1 unsealing, with checkpoint (e).
11. **Banking** under §11.

### 18.2 Screens (in order)

| Screen | Tests | Terminal if this is the first failing screen |
|---|---|---|
| S0 Completeness and intake | C1–C20 present and non-empty; KP-1 to KP-4; FR2, FR3, FR6, FR7, FR11, FR14 and FR15 declarations valid | CARD-INCOMPLETE |
| S1 Distinctness and graveyard | BU-4 and VAR-1 to VAR-6; the GY return test at card level | CARD-VARIANT; CARD-GRAVEYARD |
| S2 Decidability | DC-1 to DC-9; every mandatory predicate scorable | CARD-UNDECIDABLE (UNSCORABLE included) |
| S3 Nonrelocation | NR-0 to NR-16; §5.6 | CARD-RELOCATED; CARD-NONGENERATIVE |
| S4 Chain and consistency | KU-1; every chain map computed at r★ and r★★; persistence and nontriviality on the lock fibers; 𝒮 (KU-2 to KU-4); B-REC (KU-6); anchors (KU-5) | CARD-EMPTY; CARD-UNDIFFERENTIATED; CARD-INCONSISTENT |
| S5 Lock certificates | Q1 to Q12 on ℛ★ at r★ and r★★, including B-SRB, B-NULL and the reverse-direction screens | CARD-UNFORCED (Q1); CARD-DEFINITIONAL (Q2); CARD-STANDARD (Q3); CARD-PIPELINE (Q4, Q11); CARD-NONJOINT (Q5); CARD-UNINFORMATIVE (Q6); CARD-NONINVARIANT (Q7, Q8); CARD-VACUOUS (Q9); CARD-UNSCOPED (Q10); CARD-INCOMPLETE (Q12) |
| S6 Freedom and compression | SC1 and §4.5 | CARD-RELOCATED (LOOKUP); CARD-NONCOMPRESSIVE |
| S7 Measurability | §3.3 | CARD-UNMEASURABLE |
| S8 Selectivity | §15.1 and §15.2, computed by the harness after the batch closes | CARD-UNSELECTIVE |
| S9 Originality | The complete assembled-law audit (§8) | CARD-RESTATED; CARD-ASSEMBLY (bankable as a COMPRESSIVE sector if S6 passed) |
| — | Otherwise | **CARD-ADMISSIBLE** |

---

## 19. Freezing and preregistration

### 19.1 Charter freeze
- **FZ-1 Preconditions:**
  - the owner fixes the Appendix-A constants and decides the points in Appendix C;
  - the self-tests ST-1 to ST-5 (§24.2) return their stated verdicts on paper;
  - an auditor confirms that the cited rules catch every CHARTER TEST. A pattern that no rule catches is a charter defect, and it is fixed before the freeze.
- **FZ-2** The charter is committed **alone**, with a `pending` CHECKS line. Every card cites its SHA.
- **FZ-3** STOP for owner review.

### 19.2 Repairs
- **Before Card 1 is frozen:** numbered repairs CR-n, by owner ruling only.
- **After Card 1 is frozen:**
  - the charter text is immutable for Stages 3–6;
  - a tooling repair realigns code to the frozen text, is logged with its diff, and changes no threshold, battery, chart, baseline, price or verdict criterion;
  - an error repair ruled by the owner may only **tighten** a rule. It applies to every card, and rescoring may move verdicts only toward failure;
  - a repair never loosens anything, and never changes a computed verdict in a card's favour.

### 19.3 The harness work order
After owner authorization, and while no card exists, one bounded work order implements §§1–5 and §15 and the price coder. It is validated against:
- the SEL counts 2961 / 1721 / 1232 / 8, the 240 gap and 2721;
- the PR-forcing lemma;
- ε ≡ 0 on single-protocol families;
- the exact zeros on HB-1, HB-3, HB-4, and HB-5 under T_lin with its calibrated filters;
- HB-9 returning MODE SELECTION;
- the sign of BRI1's Tier-1 PASS on HB-2;
- STD-1 holding exactly on every HB family;
- the B-CF vectors;
- the price coder on Appendix B;
- the CT-21, CT-22 and CT-18 patterns, built only from HB models plus supplied structure. Each must be rejected with its predicted terminal.

A harness defect is fixed in the harness and never in the charter. This work order is not Card 1 and not a prerequisite campaign: it implements frozen text and nothing else.

### 19.4 Card preregistration and the batch-freeze rule
- Every field, every battery prediction and the lock register are frozen before that card's evaluation.
- **Batch freeze** (OD-1). No card is scored on any battery, holdout or lock until every card the route will submit is frozen, or until the route declares its final count (≤ 3). Static intake audits may run card by card.
- **Information hygiene.** Authors never see sealed holdouts, seeds, or another card's gate scores before freezing.
- **Lock preregistration** follows MC-5 and MC-8.

---

## 20. Staircase prohibition

**The staircase test.** A proposed work item is a **forbidden staircase move** if both hold:
- (i) it is motivated by a card failure, a gate failure or a missing input; **and**
- (ii) what it delivers is an ingredient for a future card, rather than a card, a gate result or a terminal record.

**Forbidden at any time, before or after termination:**
- **SM-1** A "missing ingredient", "deeper prerequisite" or "foundations" campaign. Examples: a theory of the carrier, of weights, of temporality, of the partition, of the interface class, of Gibbs structure, of the representation of Ξ, or of decidability.
- **SM-2** Any change to a gate, battery, baseline, chart, pricing rule or constant that would let a failed card pass, or that rescores under modified rules (§19.2).
- **SM-3** Describing a failed card as "partial progress" or "future work", or opening an extension stage for it.
- **SM-4** Budget laundering (BU-8), or a fourth card.
- **SM-5** Reopening R1: new interface classes, a change to d_op or to the verdict table, or reinterpreting WO-002.
- **SM-6** Treating UNSCORABLE or UNRESOLVED as "pending better tools".
- **SM-7** Mining GRAVEYARD entries for "repaired" candidates (§21.2).
- **SM-8** Opening a new generative route by any means other than an explicit new owner ruling (T-5).

**Non-blocking items.** M5, D4, Tier-2 carrier necessity, triviality of the join, WO-001 C3/C4 and the pending external checks continue as housekeeping.
- They are **never prerequisites** of any Stage-3, 4 or 5 step.
- A verdict that depends on one of them is labelled "conditional on ⟨item⟩" and proceeds.
- Their results cannot reopen this route.

---

## 21. Relation to FR1–FR15 and the GRAVEYARD

### 21.1 FR1–FR15
Each FR receives a standing of SATISFIED (with its argument), SCOPED-OUT (declared and priced), N/A (with a reason the auditor may contest), or VIOLATED. No FR is claimed discharged without an external check.

| FR | Stage-3 form | Where | Consequence of violation |
|---|---|---|---|
| FR1 Representation invariance | Covariance under the declared moves only | §1.6, Q7, NR-8 | INVALID → CARD-NONGENERATIVE, or the relation is NONINVARIANT |
| FR2 Gluing is an explicit act | Composition of Ξ-instances is declared | C3, SEL-12 | CARD-INCOMPLETE |
| FR3 No inaccessible-context data | Per-protocol laws only; inputs checked against declared access | §1.3, Q7, NR-0 | CARD-INCOMPLETE (inputs) or NONINVARIANT (relation) |
| FR4 Observer independence | Π and [h] come from Ξ; counterfactual framing does not count | DIF-9 | CARD-NONGENERATIVE |
| FR5 No unpriced split | Strengthened: even a declared split fails | §5.6 | NONGENERATIVE (declared); RELOCATED (hidden) |
| FR6 Compatibility scope | Declared in Emb | C3, §15.1 | CARD-INCOMPLETE |
| FR7 Earned temporality | Time is primitive and priced (VB-9) or earned; the instantaneous-state designation is derived | C3, NR-10(c) | CARD-INCOMPLETE; RELOCATED if hidden |
| FR8 Constraint ≠ selection | Q1 holds on all of Sol; DIF-7; DC-8 | §3, §15.10 | CARD-UNFORCED or NONGENERATIVE |
| FR9 No outer→exact upgrade | B-SEL grades; DC-5 | §15.1, §16 | Correction before scoring; the claim is not credited |
| FR10 Information price | §4 | §4 | An unpriced input → RELOCATED |
| FR11 Declared meaning of 𝒞 (gate F0-PHYS-OPEN-02) | C2 | C2 | CARD-INCOMPLETE |
| FR12 Convention fixes | Adopted for the B-SEL encodings | §15.1 | Correction required |
| FR13 A deeper Γ object | Γ_Π = Obs_Π(Ξ) is built; Γ as an empirical model counts as SUPPLIED | §1.3, C7 | CARD-NONGENERATIVE |
| FR14 Subsidiary possibility facts | Dependency declared | C3 | CARD-INCOMPLETE if hidden |
| FR15 G0 trichotomy | Landing declared; weights within supports (b) are addressed | C3, DC-8 | CARD-INCOMPLETE; no weight rule → CARD-UNMEASURABLE |

### 21.2 GRAVEYARD

| GY | Killed idea |
|---|---|
| GY-1 | Restatement as constructor theory (CT-parallel embedding) |
| GY-2 | "Forbid strong contextuality" as the support law |
| GY-3 | "Bipartite ≥ 3 settings" as the resource |
| GY-4 | Counting capacity or dimension |
| GY-5 | Counting parties |
| GY-6 | ASP as a new generative support law |
| GY-7 | Pairwise or sub-cover locality, single-context-deletion solvability, cohomology/AvN classes as support laws |
| GY-8 | Support determination as a standalone line |
| GY-9 | A distinctive payoff from the bridge or the scouts at their premise envelopes |
| GY-10 | The selector campaign at the current screen |
| GY-11 | The "maximal" T read literally |
| GY-12 | "Latent dimension ≤ k" as the T commitment |

- **Declarations.** For each entry the card declares one of: NOT USED; COMPARATOR ONLY; COMPONENT (priced, with every distinction it alone produces removed from D); RESEMBLES (with an argument that distinguishes the card from it).
- **Return test.** A claim's responsibility map contains a component equivalent to a GY entry (under VAR-1 or VAR-2, or with the same verdict vector and the same responsibility on the batteries), and the claim vanishes when that component is ablated.
  - **Claim level:** the claim is not credited.
  - **Card level, CARD-GRAVEYARD (KU-9):** the returning component carries the selectivity discriminator, the mechanism that generates Π, or ℛ★; or every credited claim fails the test.
- **GY-10** reopens only with a new named candidate. A card that is a selector must say so, and it is audited against GY-10's screen.

---

## 22. Not credited (consolidated)

- **Definitional relations**, DEF-1 to DEF-11, and any bits on 𝒜_ε.
- **Standard-theory consequences** under regime matching (STD-1 to STD-12):
  - causality, Kramers–Kronig, positivity, CP and uncertainty bounds;
  - KMS, the FDRs, the fluctuation theorems, Gaussian-bath completeness;
  - Onsager–Casimir; conservation, sum rules, selection rules, action–reaction;
  - GLE memory; GKSL, input–output theory, imprecision–back-action and the SQL;
  - the second law; large-N scaling; SSB, critical and pattern relations;
  - representation freedom; E_univ.
- **D5's reverse-direction relations.**
- **RECOVERY** of Gibbs states, thermalization or memory derived from 𝒦. This is Stage-6 bookkeeping only.
- **Calibration-only results:** the BRI1 Tier-1 value and its 1/N_B rate, the harmonic R1-NULL, and the C2 and M controls.
- **Consequences of the priced inputs alone, and consequences of supplied structures.**
- **Relations without a W-pipe**, i.e. produced by the pipeline alone.
- **Freedom reductions inside Ξ that never reach the chart; reductions of log-volume by inequalities.**
- **Persistence and differentiation**: these are gates.
- **Restrictions on a single axis, and couplings of Π and T only**, presented as ℛ.
- **Scope-Q relations in the ε ≡ 0 blind spot; ε values at a non-admissible T; truncation artifacts; redundant or copied instances.**
- **Relations that only fix a sign; relations that hold on a single protocol or a hand-picked repertoire; relations that depend on a representative or on joint laws across protocols.**
- **Record-only relations** (satisfied by the E-B twin), and any back-reaction claim made without a derived carrier.
- **Readings of R1-NULL as "no response."**
- **Selectivity reached through bounded-width consistency** (KNOWN SECTOR); SD0-implied and structural ALLOWs; over-allowances reported as exact.
- **Holdout successes** as compression.
- **In-silico locks** as PREDICTIVE.
- **Analogy, shared vocabulary or formalism, and same-regime replications** as CROSS-SECTOR.
- **Novelty of a component, a representation or a name; STANDARD COMPONENTS, NEW ASSEMBLY; KNOWN ASSEMBLY.**
- **Re-presentation of the post-result seeds:** Z_A, the measurement-invariance framing, and [h]_T in its known nearby forms.
- **Existence claims** of the form "ε_R > 0 somewhere".
- **A presumed monotone identity–response tradeoff.**

---

## 23. Governance and roles

- **Roles.** No agent context both authors and audits the same card.
  - **Author:** the builder, Claude Code.
  - **Intake auditor:** independent and hostile.
  - **Evaluator:** independent. Runs the reference implementations and the harness, writes machine-readable output and generated tables.
  - **Recomputer:** independent of the Evaluator.
  - **Selector:** sees the card's signature only.
  - **Comparator panel:** analysts and skeptics.
  - **External checkers:** via `CHECKS.md`.
  - **Owner:** issues rulings and makes the pick.
- **Hostile default** (CV-1) governs every dispute until the owner rules.
- **Records.**
  - Each card, intake audit and gate result gets a CHECKS line once it is verified on the remote.
  - Checkpoint reports are five lines or fewer: stage · result · scoreboard change · next action · blockers.

---

## 24. CHARTER TESTS and charter self-tests

### 24.1 CHARTER TESTS
**Every row is an abstract gaming pattern labelled CHARTER TEST. None is a physical proposal.** If a card instantiates a pattern, it is presumed to receive that pattern's classification, and the card carries the burden of rebuttal.

| ID | CHARTER TEST pattern (abstract) | Caught by | Outcome |
|---|---|---|---|
| CT-01 | An input asymmetry (labels, weights, a distinguished substructure) from which Π can be read cheaply, e.g. a weighted structure whose cut or community equals Π | NR-6, NR-7 | RELOCATED |
| CT-02 | Sorts or labels of Ξ's type whose classes coincide with S/E | NR-1, NR-6 | RELOCATED, or NONGENERATIVE if declared |
| CT-03 | A clause that asserts a bipartition with a persistence or decoupling property | NR-1 | SUPPLIED → NONGENERATIVE |
| CT-04 | A table of constants whose block or zero pattern is Π | NR-6, IP-3 | RELOCATED |
| CT-05 | A vanishing explicit seed in 𝒞 selects Π; differentiation is absent at zero seed | NR-5 | NONGENERATIVE |
| CT-06 | An extractor threshold tuned so that Π appears only on Sol | NR-3, DIF-2, IP-5 | RELOCATED (pipeline) |
| CT-07 | Π depends on a chosen basis or coordinate system | NR-8 | INVALID → NONGENERATIVE |
| CT-08 | Persistence obtained by pushing relata into the boundary ∂ | §1.3 (∂ counted as reassigned; δ_∂ cap) | Not persistent |
| CT-09 | The carrier stated as an axiom, or Obs defined with one shared readout by construction | NR-1, NR-3, NR-10 | RELOCATED; NO RECIPROCITY VERDICT |
| CT-10 | The carrier variable declared to be the instantaneous E state by definition | NR-10(c) | RELOCATED |
| CT-11 | Protocol-dependent readouts in disguise (clauses keyed to protocol identity; an Emb or repertoire under which protocols change the readout) used to obtain ε_R > 0 | NR-10(a), NR-11, B-NULL E-B | MODE SELECTION; lock void |
| CT-12 | T_Π equal to the automorphism group of a supplied record structure | NR-10(f) | NONGENERATIVE |
| CT-13 | T_Π picked from 𝒯 by a selector clause rather than constructed | NR-1, NR-10(f), IP-4 | SUPPLIED → NONGENERATIVE |
| CT-14 | A generated T_Π ⊇ J or T_univ, so ε ≡ 0 | Q8, DIF-5, B-NULL | Relations void; DIF-5 fails |
| CT-15 | R1 calibration data (grid, protocols, calibrated maps) used as law inputs | NR-10(g), NR-14 | RELOCATED |
| CT-16 | Admissible states restricted to Gibbs, KMS or detailed-balanced states, or a temperature among the inputs | NR-1, NR-12 | SUPPLIED with dependent claims at 0; RELOCATED if hidden or if ℛ★ uses it |
| CT-17 | Thermal structure entering through a weighting measure or a prior of Gibbs or maximum-entropy form | NR-9, NR-12 | RELOCATED (prior) |
| CT-18 | A known standard model, with its cut, readout and Gibbs ensemble, repackaged as a law | NR-1, NR-12, IP-7, OR-3 | NONGENERATIVE / RESTATED |
| CT-19 | The lock smuggled in as a clause, or as the objective or penalty of an extremum principle | NR-2, NR-13 | RELOCATED |
| CT-20 | A tradeoff or sign imposed by an input clause, or a monotone identity–response tradeoff postulated | Q11, NR-13 | RELOCATED |
| CT-21 | A lock that is an identity of ε's definition or of R1's theorems (a rewriting of ε, monotonicity in T, ε = 0 on one protocol, a Theorem-F bound) | Q2 | DEFINITIONAL |
| CT-22 | A lock that follows from KMS, FDT, a fluctuation theorem or Onsager, rewritten in (Π, T, ε) variables | Q3, STD-3, STD-4, B-SRB | STANDARD |
| CT-23 | A lock equal to a D5 reverse-direction relation | Q3, §13.8 | STANDARD |
| CT-24 | A lock that is an N-scaling law of ε_R in a mean-field architecture | STD-9 | STANDARD |
| CT-25 | A lock of the form "an odd channel vanishes under a symmetric reference" | STD-5 with Theorem C | STANDARD |
| CT-26 | Regime shopping: witnesses from another regime, or avoiding Gibbs structure so that the baseline is weaker | BP-3, BP-4 | Witness invalid; scored on the hostile fiber |
| CT-27 | Separate interface and response constraints presented as one relation | Q5 | NONJOINT |
| CT-28 | A scope-Q relation on a realized set with ε_R ≡ 0 | Q9 | VACUOUS |
| CT-29 | Scope switching: scope Q supported by linear-response evidence; scope G tested on ε_R alone; R1-NULL read as "no response" | §14 | Lock void / UNSCOPED |
| CT-30 | ε evaluated at a non-admissible, joined or universal T | Q8 | Void |
| CT-31 | A relation that holds for one representative h but not for the class | Q7 | NONINVARIANT |
| CT-32 | A relation that uses joint laws across protocols | Q7, FR3 | NONINVARIANT |
| CT-33 | A relation that holds only because \|A\| = 1, or only for a listed repertoire | Q1, B-NULL | UNFORCED |
| CT-34 | A lock that predicts ε_R from the same Γ it is computed on | MC-2 | DEFINITIONAL |
| CT-35 | An identification plan that certifies Π or T_Π by using ℛ★ | MC-2 | UNMEASURABLE |
| CT-36 | A lock that needs more than N_max samples | MC-7 | UNMEASURABLE |
| CT-37 | Forcing claimed from numerics with a tolerance | Q1, DC-3 | UNFORCED |
| CT-38 | A truncation artifact | Ch-4 | Zero |
| CT-39 | Inflation through grid, precision, instance copies or carrier size | Ch-1, Ch-3, Ch-5, caps | No gain |
| CT-40 | Freedom reduction obtained by forbidding anchors or emptying Sol | §15.8, §2.5(iii) | No credit; KU-5 |
| CT-41 | A real constant tuned to make the lock hold or to flip one battery item | IP-5, IP-10 | Priced; distinction not credited |
| CT-42 | One symbol encoding a table, or target vocabulary encoded as an isomorphic L₀ table to avoid its price | IP-3, IP-6, NR-6 | Priced in full; RELOCATED if Π is decodable from it |
| CT-43 | Selectivity by lookup: scenario name, party or setting count, dimension or capacity | IP-9, SEL-11, §21.2 | RELOCATED or GRAVEYARD |
| CT-44 | A law built only from consistency conditions, whose battery behaviour equals a B-CF member's, with no weights | §15.2, DC-8 | D_sel = 0; UNMEASURABLE |
| CT-45 | An exact characterization claimed for a target that may be undecidable; membership quantified over all extensions with no truncation | DC-4, DC-5 | UNDECIDABLE or OUTER |
| CT-46 | Many drafts produced, the best frozen, the search undisclosed | IP-12, BU-5, KU-10 | Tax charged; void if undisclosed |
| CT-47 | A repair variant (renamed symbols, rescaled constants, a clause excluding the failed items, a conjunction of failed cards) | VAR-1 to VAR-6 | VARIANT; slot consumed |
| CT-48 | Items, domain or response scope declared OUT after results are seen | BU-3 | New card or VARIANT |
| CT-49 | Deferral: "ℛ follows once X is derived", "T_Π derived in a follow-up", a structure to be supplied later | NR-15, §20 | SUPPLIED; no X campaign |
| CT-50 | A baseline, battery or chart edited after a card is seen | §19.2 | Forbidden |
| CT-51 | A pending item cited as checked | §11 | Labelled conditional; banking blocked |
| CT-52 | Protocols chosen so that the relation happens to hold | Ch-2, Q1 | No effect |
| CT-53 | Memory, viscoelastic or crystalline-order input | NR-14 | RELOCATED |
| CT-54 | A record-only statement offered as evidence of back-reaction | STD-12, B-NULL | No reciprocity credit |
| CT-55 | Holdouts selected before the batch closes, or by an agent that has seen the mechanism | §15.9 | Evaluation void; holdouts reselected |
| CT-56 | A weak set of comparators | OR-4 floor | Audit incomplete; no DISTINCTIVE |
| CT-57 | A "transfer" in which a B-side nuisance fit absorbs the prediction, B data enter the fit, a standard bridge links A and B, or B replicates A in the same regime | XS-2, XS-6 | Not CROSS-SECTOR |
| CT-58 | Threshold, platform, tier, repertoire or estimator chosen after data access | MC-5, MC-8 | LOCK-VOID = LOCK-FALSIFIED |
| CT-59 | A discriminator that reduces to capacity or dimension, party count, a blanket ban on strong contextuality, maximal T, or a latent-dimension bound | §21.2 | CARD-GRAVEYARD |

### 24.2 Charter self-tests
These must hold at freeze (FZ-1). They are run on known objects only; none of them is a candidate.

| ID | Known object treated as if it were a card | Required verdict |
|---|---|---|
| ST-1 | BRI1's Tier-1 ε_R relation | S3: CARD-NONGENERATIVE (the partition, readout, bath and Gibbs state are all supplied). Independently, B-SRB: STANDARD (STD-3 nonlinear FDR plus STD-9) |
| ST-2 | The harmonic R1-NULL | STANDARD (STD-3, STD-6, Ford–Kac–Mazur). RS-1 applies: R1-NULL ≠ no response |
| ST-3 | ASP | S1: CARD-GRAVEYARD (GY-6). Also: SEL-10 (theta) and SEL-4 (the 240 tables) admitted, so NON-SELECTIVE; B-CF collapse; no weights, so UNMEASURABLE |
| ST-4 | NULL-ΠT | Credited = 0, so ΔL ≤ 0: LOOKUP → RELOCATED. It is also NONGENERATIVE |
| ST-5 | The product-latent E-B model | NR-11: MODE SELECTION. STD-12: no credit |

---

## 25. Hard stop

- This charter is committed **alone**, with a `pending` CHECKS line.
- No 𝒦 card is generated, frozen, scored or optimized until the owner has reviewed the frozen charter and authorized the harness work order and Card 1.
- After the freeze, the charter changes only under §19.2.

---

## Appendix A: Frozen numbers [P]
The owner may change any value before the freeze. None may change after Card 1 is frozen.

| Symbol | Value |
|---|---|
| p★ | 10 bits; sensitivity reported at 6 and 16 |
| r★ | k = 3 grid times; maximal witness order m = 4; A = {a₀, a₊, a₋}; d_rec = 1 |
| r★★ | k = 4; m = 5; A ∪ {a₊₊}; d_rec = 2 |
| Protocol templates | a₀ is null; a± are linear ramps of amplitude ±α starting after t₁; a₊₊ is a ramp of amplitude 2α; α = 1 null-protocol standard deviation |
| Windows | [−4, 4] for whitened cumulant coordinates; [0, 2] for ε |
| q (finite record alphabet) | 3 |
| Certification tolerance | 2^(−p★) |
| δ_Π / η / δ_∂ | 0.05 / 0.05 / 0.10 |
| H | ≥ max(the full protocol and record window, 10·τ_int) |
| Horizon robustness | (2η, 2H) |
| θ_gen | 0.9 of the AI-3 ensemble |
| Caps | Π term 16 bits per instance; T term log₂5 |
| Credit instances | ≤ 3, structurally distinct, with independent data |
| Σ_L₀ | 64 tokens (6 bits each) |
| τ_sel | log₂(1 + n_drafts), cumulative; log₂ N_frozen at the pick |
| Compression | ρ ≥ 2; ΔL ≥ p★ at p = 10; ΔL > 0 at p = 16; ΔL ≤ 0 → LOOKUP |
| Codimension | ≥ 1 |
| Q_min | 10 (3.32 bits) |
| N_max | 10⁹ independent records per lock observable; ≤ 30 days of platform time |
| α, power | 0.0027; 0.9 |
| Lock thresholds | Falsified above 3σ_tot; confirmed within 2σ_tot with σ_tot ≤ \|I_K\|/4 |
| In-silico budget | ≤ 10¹⁰ effective samples (evidence grade only) |
| ℓ_dec, p_dec | ½·F_X; 0.5 |
| ℓ_tr, b_patch | 32 bits; 4 bits |
| κ | 10 |
| DIF-6 perturbation | 2^(−p★), relative |
| Default constant range | [10⁻³, 10³], log scale |
| SEL credit | 1 bit per verified distinction; at most 10 |
| Consistency collapse | k ≤ 3 |
| Holdouts | ≥ 3 per sector; Stage 5 ≥ max(2, number of lock observables) |
| Budget | 3 cards, Stages 3–6 |
| Relations per card | ≤ 2, one of them primary |
| Transfer | d_B = 0; TG ≥ p★; band ≤ ¼ of range; bridge ≥ Q_min× wider |
| HB ranges | β ∈ [0.25, 4]; ω ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8; quantum ≤ 4 sites; quartic λ ∈ [0, 2] |
| Alternate lock platforms | 1 |

## Appendix B: L₀ code and vocabulary schedule

**B.1 The alphabet (64 tokens, Polish notation).**

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
- **Price:** P_v = max(L_stmt(def_v), ΔF_tgt(v)), with import subtraction.
- **Canonical definitions** are encoded in L₀ by the harness before Card 1.
- **Items:**
  - VB-1 metric
  - VB-2 inner product / orthogonality
  - VB-3 finite-dimensional Hilbert space and tensor product
  - VB-4 tensor-product or subsystem factorization (beyond VB-3)
  - VB-5 quantum correlation set
  - VB-6 GPT cone with order unit
  - VB-7 Born rule
  - VB-8 continuum analysis (ℝ, limits, exp/log), and continuous time or space beyond the declared resolution
  - VB-9 temporal order and time unit, unless earned
  - VB-10 dimension, capacity or any dimension-like parameter (SD0 CR3)
  - VB-11 energy function / Hamiltonian
  - VB-12 locality graph of a Hamiltonian or generator
  - VB-13 probability measures, weights or priors on Ξ, unless generated
  - VB-14 a symmetry group and its action, when not generated by 𝒦
  - VB-15 conserved-quantity declarations
  - VB-16 time-reversal parity / microscopic reversibility
- **Protected items** (cannot be bought; §5.6):
  - VB-17 invariant measure, temperature, Gibbs weight, detailed balance or KMS (PS-5)
  - VB-18 group action on record space (PS-4)
  - VB-19 readout map or class (PS-3)
  - VB-20 partition sorts (PS-1)
  - VB-21 target-level coordinates in clauses (PS-6)
- Supplying VB-5, VB-6 or VB-7 makes every selectivity result RELOCATED.

## Appendix C: Owner decision points before freeze
- **OD-1** The batch-freeze rule. Adopted; the alternative, sequential evaluation, invites patch-tuning.
- **OD-2** The theta parity system as a mandatory FORBID. Adopted; otherwise ASP's known over-allowance would be free.
- **OD-3** Cards rejected at intake (VARIANT, INCOMPLETE) consume their slot. Adopted.
- **OD-4** The Appendix-A constants, in particular r★★'s d_rec = 2 and a₊₊ = 2α, which no draft fixed.
- **OD-5** The reading of 𝒞 is kept neutral.
- **OD-6** The d_op rule for a generated T_Π: a canonical reduction supplied by the card, run by charter code, counted as a use of R1 and not a modification.
- **OD-7** The closure of 𝒮 includes the fluctuation theorems. Adopted.
- **OD-8** UNSCORABLE is final within the route. Adopted.
- **OD-9** R1's post-result 10-item checklist is adopted as the Stage-3 lock-platform certification standard.
- **OD-10** A complete assembled-law audit before the pick, with DISTINCTIVE (P) required for ADMISSIBLE.
- **OD-11** No "in-principle" measurability grade.
- **OD-12** Authorization of the §19.3 harness work order.

## Appendix D: Resolved conflicts
D1, D2 and D3 below refer to the three source drafts.

1. **Audit timing.** D1 audits after the pick and D3 picks on intake alone. Chosen: D2, a full audit before the pick, with DISTINCTIVE (P) required for ADMISSIBLE (most conservative; this is the SD0 lesson).
2. **Compression.** The tests are conjoined: ρ ≥ 2 (D2; the same as D3's I(F) ≤ ½I(D)), ΔL ≥ p★ at p = 10 and > 0 at p = 16 (D1), and the two-part code against NULL-ΠT (D2). D3's MARGINAL owner-discretion band is removed: such a card is NON-COMPRESSIVE.
3. **Lock credit.** min(b_struct, b_meas). D2 took the max of the two; D3 took c·b_res. The min caps credit at both what is structurally reduced and what is measurable.
4. **Real constants.** Price = max(literal length at p (D1), tuning price (D2, D3)).
5. **Vocabulary.** Both pricing at max(def, ΔF_tgt) (D1) and import subtraction (D3) apply, deliberately: vocabulary cannot earn anything.
6. **Selection tax.** Cumulative n_drafts (D1), plus log₂ N_frozen at the pick (D2).
7. **B-SEL classes.**
   - Mandatory: the D1 minimal-gate anchors, plus G1; D2's core FORBIDs (SEL-9) and PR⊗PR; theta (D3 recommendation); the 240 tables.
   - Graded: Specker triangle, chained-PR 6-cycle, C7.
   - Padded-PR is reported only, because the SD0 candidate record gives its quantum status as unknown. D2's mandatory treatment of it was rejected.
8. **The 240 tables.** The selectivity object is fixed to record-law supports, because Γ_Π consists of laws (FR13). FORBID is mandatory and earns 0. D1 let the card choose its object.
9. **Selectivity timing.** Computed at Stage 3 for every card after the batch closes (D1), not merely predicted (D2) or run after the pick (D3). Stage 4 recomputes it.
10. **Sequencing.** Batch freeze (D3) over adaptive design (D1). This matches RULES checkpoint (d), "the three 𝒦 cards".
11. **Variants.** The union of D1 BD2, D2 GD-1 to GD-4 and D3 V1 to V6. The slot is consumed (D1, D3), against D2's "no slot".
12. **Gibbs/FDT supplied and declared.** Priced commitment, dependent claims at 0, CARD-RELOCATED if ℛ★ uses it (D2). D1 priced it; D3 failed only the gate.
13. **Target relation supplied in any form → CARD-RELOCATED** (D2, D3), over D1's pricing. Inputs excluded by STATE → CARD-RELOCATED (D2), over D1's SUPPLIED.
14. **Symmetric-input probe.** Mandatory (D2), keeping D1's STRONG/WEAK grades. Universality over all of Sol (D3), on a domain that includes 0.9 of AI-3 (D1's 0.9 value, over D2's 1/2).
15. **Decoders.** Budget ½·F_X (D1, the most generous non-trivial value: a budget ≥ F_X decodes anything). It fires on 0.5 of AI-3 (D2) or on every lock fiber (D1). D3's min(32, ¼) was rejected as less conservative.
16. **Persistence.** VI_norm 0.05 (D2); reassigned fraction 0.05 (stricter than D3's 0.1); ∂ counted as reassigned, with cap 0.10 (D1); H ≥ max(window, 10τ_int); horizon doubling (D3).
17. **Measurability.** N_max of 10⁹ records in total (D3), not per protocol (D1); α = 0.0027 (D2); power 0.9 (D1, D3); 30 days (D2). D1's IN-PRINCIPLE grade is removed.
18. **Forcing.** DERIVED grade is required (D3). Evidence grade gives CARD-UNFORCED, not a PROVISIONAL admission.
19. **Joint test.** The interface-versus-response rectangle (D2). D3's "any two axes" would credit a coupling of Π and T alone.
20. **The join.** ε at J is void (D1), over D3's "allowed with a proof".
21. **d_op for a generated T_Π.** A canonical reduction supplied by the card (D2), computed in charter code (D3). D3's plain inf_t d_BL(P, t#Q) was rejected because it is not T-invariant in its first argument, which would break DEF-6 and Q7.
22. **𝒜_T.** D3's frozen 𝒯 (4 classes + ⊥) with cap log₂5, the smaller cap. D1 used log₂6 and D2 a 7-element set.
23. **Cross-sector.** d_B = 0 is required (owner text), over D2's n_B − d_B ≥ 1. TG ≥ p★ (D1), the ¼ band (D3) and the bridge ratio ≥ Q_min (D2) are conjoined. The independence certificates of all three drafts are combined into SI-5.
24. **Stage-5 holdouts.** ≥ max(2, number of observables) (D1 and D2), with PREDICTIVE only on sealed real data (D2).
25. **Repairs after Card 1.** Tighten only, apply to all cards, and rescoring may move verdicts only toward failure (D3 SM-2 combined with D1).
26. **The budget spans Stages 3–6** (D3). D_diff = 0 always (D1), over D3's exception. At most 2 relations per card (D2).
27. **Witnesses.** The card carries the burden; the evaluator adds no witnesses (D3 B-STD) but may add anything that reduces credit (D2, D3).
28. **Audit instances.** The evaluator generates AI-2 and AI-3 with post-batch seeds (D3); the card declares only AI-1 and the input type. D2 had the card instantiate them.
29. **Embedding.** Parties are generated blocks of Π (D2). An Emb that supplies the split would be a supplied partition (FR5).
30. **D1's truncated sections.** D1's §§0–5 were truncated at Q9. Its certificate letters, chart rules, O-items and B6 are reconstructed here as Q1–Q12, Ch-1 to Ch-5, §1.3 and BP-3/BP-4. No rule is cited by a lost label.
31. **Label collisions.** Renamed to: STD-n (standard constraints), FC-n (credit components), DEF-n (definitional relations), VB-n (vocabulary), VAR-n (variants), KU-n and KP-n (kills), SEL-n (selectivity items). The terminal for an empty law is CARD-EMPTY, to avoid a clash with Q9's VACUOUS.

## Appendix E: Traceability

| Requirement | Section |
|---|---|
| Item 1: baseline spaces 𝒜_Π, 𝒜_T, 𝒜_Γ, with 𝒜_ε as an image | §2, §12 |
| Item 2: success criterion | §3 |
| Item 3: compression and information price | §4, Appendix B |
| Item 4: nonrelocation | §5 |
| Item 5: at most 3 genuinely distinct cards | §6 |
| Item 6: card contents | §7, §17 |
| Item 7: originality at the assembled-law level | §8 |
| Item 8: parameter transfer | §9 |
| Item 9: stopping rule; no staircase | §10, §20 |
| A1 merge = provenance | §11 |
| A2 ε_R derived; definitional relations; joint restriction | §12, Q2, Q5 |
| A3 baseline after standard theory | §13, Q3, NR-12 |
| A4 response scope | §14 |
| Carrier and readout derived modulo representation; no unique h | §1.3, NR-10, C17 |
| No presumed monotone tradeoff | Q11, NR-13, C18 |
| R1's identifying assumption becomes a Stage-3 target | NR-10, DIF-5, DIF-9 |
| Environmental identity (NORTH_STAR) | PS-2, DIF-9 |
| Stage 4–6 gates made