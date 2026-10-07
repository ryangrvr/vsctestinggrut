# GRUT 2: Stage-3 Charter v1 (rules for judging 𝒦 cards)

**Date:** 2026-10-07 · **Branch:** `grut2-stage3` = `main` after the G2-11 merge `86bf5a0` · **R1 terminal boundary:** `dbfd64b` · **Governing ruling:** G2-11 (ruling block, additions 1–4, reconciliation note on 𝒜_ε). · **Supersedes:** charter v0 (same date). · **Working copy:** `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/rt_def/charter_v1.md` (uncommitted).

> **Status: CHARTER v1, a draft for owner review. Not frozen.**
> - v1 is v0 plus the fixes from five red-team reports (lenses: definitional **D**, relocation **L**, standard physics **S**, accounting **C**, measurability and stopping **M**). The **Red-team ledger** at the end answers every attack and every ambiguity they raised: the fix was applied, or it was declined with a reason.
> - Report D reached the reviser only from its CT-D10 ablation clause onward. Its fixes for CT-D01–CT-D10 are reconstructed from that report's cross-references (priority list, harness table, ambiguity fixes). The content of CT-D02 and CT-D05 is unknown. FZ-1(d) therefore requires the D lens to be re-run on v1 before the freeze.
> - The charter contains **no candidate law**. No 𝒦 is proposed, sketched, named, exemplified or optimized anywhere. Every construction in §24 and in the ledger is an abstract gaming pattern labelled **CHARTER TEST**, not a physical proposal. The self-tests use only known textbook objects.
> - It is written to be frozen **alone** (G2-11). After the freeze: **STOP for owner review before Card 1.** Nothing here is banked. The freeze commit gets a `pending` CHECKS line.

---

## 0. Status, sources, naming and conventions

### 0.1 Governing documents
- `PROGRAM/OWNER_RULINGS.md`: G2-11, plus G2-08 and G2-10 where cited.
- `PROGRAM/STATE.md`: the Stage 3–6 definitions.
- `PROGRAM/RULES.md`.
- `PROGRAM/NORTH_STAR.md`: the architecture and the environmental-identity requirement.
- `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md` §§1–3, 7, 11 and 12.
- `R1_T_LADDER.md` §0, §1 and §10.
- `D5_COMPARATOR_AUDIT.md` §§2.3, 3 and 6, and `D5_IDENTIFICATION.md`.
- `PROGRAM/SCOREBOARD.md` and `PROGRAM/GRAVEYARD.md`.
- `F0_REQUIREMENTS_CONSOLIDATION_01.md` at `0a9a941`.

### 0.2 Precedents adopted
- **`F0_SD0_CHARTER.md`:** the charter is frozen alone; candidates are preregistered; any later modification makes a new candidate; repairs are numbered.
- **`F0_SD0_COMPACTNESS_ACCOUNTING_01.md`:** free choices are weighed against distinctions; a symbol that encodes a table costs the table; a constant that matters for one control only is fitted to that control; lookup structure is RELOCATED.
- **`F0_SD0_HOLDOUT_PROTOCOL_01.md`** (an independent selector picks holdouts after the freeze) and **`F0_SD0_GENERALIZATION_CHECKS_01.md`**.
- **`F0_SD0_RECON_01.md` and `F0_SD0_RESULT.md`:**
  - the exact (2,2,2) counts;
  - the PR-forcing lemma;
  - T1 and T2;
  - ASP's over-allowance of the theta parity system;
  - the decidability caveat, which was flagged but never audited;
  - the comparator audit, which stopped at 1 of 5.

### 0.3 Naming
- **FR1–FR15** are requirements R1–R15 of the consolidation map, renamed so they are not confused with the Stage-2 observable.
- **R1** is the Stage-2 observable and its terminal record.
- **ℛ** is a card's target relation. **ℛ★** is its primary lock relation.
- **GY-n** is a GRAVEYARD entry (§21.2).
- **Card** is one frozen 𝒦 candidate with every field of §17.
- **Roles** (§23): Author, Harness builder, Intake auditor, Evaluator, Recomputer, Selector, Comparator panel, Owner.
- **Harness** is the charter's own code (§19.3).
- **[P]** marks a constant the owner fixes at freeze (Appendix A).
- **Ledger IDs:** the prefixes `D:`, `L:`, `S:`, `C:` and `M:` mark the item numbers of the five red-team reports.

### 0.4 Conventions (binding throughout)
- **CV-1 Hostile default.** Ambiguities, unresolved disputes and unresolved regime hypotheses are resolved against the card until the owner rules. A dispute goes to the owner together with both computations.
- **CV-2 Burden asymmetry.** The card bears the burden of every certificate. The evaluator adds nothing that helps a card. It may add anything that reduces credit, within BP-7.
- **CV-3 Honesty (RULES 5).** No theorem is claimed without a proof. NOT FOUND ≠ IMPOSSIBLE. Literature is verified against primary sources. A citation that has not been verified cannot carry a verdict on its own.
- **CV-4 Numerics (RULES 6).** The pipeline runs computed → machine-readable output → generated tables, with at least one exact-identity control (§15.3).
- **CV-5 Neutrality.** The charter preregisters and favours no target relation, sign, monotonicity or functional form. Any sign or form in ℛ★ must come from 𝒦 (G2-11).
- **CV-6 Constants.** Every threshold, constant and catalogue is fixed at freeze. No card, including the first, sets or moves one.
- **CV-7 Interpretations.** After Card 1, an owner ruling on a dispute chooses between the two submitted computations. The ruling is recorded as interpretation **CI-n** and applies uniformly to every card, null and self-test. It is void if it changes any self-test verdict (§24.2).

---

## 1. Definitions and objects

### 1.1 Law, ontology and the pre-law domain
- **Ξ** is the relational process object. The card declares and prices its kinematic type 𝒳 and its relata carrier V_Ξ (IP-1, IP-14).
- **𝒞** is the card's declared commitment data. Its meaning is an L₀ statement, declared and priced (FR11, IP-2). Any possibility language means *declared* possibility.
- **𝒦[𝒞, Ξ] = 0** is the law, and **Sol_𝒦(𝒞)** := {Ξ ∈ 𝒳 : 𝒦[𝒞, Ξ] = 0}.
- **Nonvacuity:** ∅ ≠ Sol ⊊ 𝒳 on every in-domain instance, at both r★ and r★★.
- **Dom_pre(ι), the pre-law domain:** every Ξ ∈ 𝒳 consistent with 𝒞_ι and Emb at the declared truncation, with no law clause imposed.
- **Dom_pre^chain(ι):** the subset on which X_Π returns a nontrivial persistent Π (§1.3) and the remaining chain maps are defined.
- **Dom_pre^carrier(ι):** the subset on which X_Π is defined.
- All ablations, W-pipes and pipeline-tautology tests run on these sets.

### 1.2 The pipeline and its components
The chain is:

  𝒦 → Sol →[X_Π] Π →[X_Z] Z_Π →[X_h] [h]_{T_Π} →[X_T] T_Π →[Obs] Γ_Π →[ε, charter code] ε_R → ℛ

**Components the card supplies:**
- X_Π, the partition extractor;
- X_Z, the carrier extractor;
- X_h, the readout-class construction;
- X_T, the interface-class construction;
- Obs, the record map;
- Emb, the embedding of scenarios and repertoires into Ξ;
- s_T, a canonical reduction, needed only when T_Π lies outside the frozen tiers.

**Components the charter supplies:** the ε_R implementation (the R1 code), the batteries, the 𝒮-checker, the chart, and the harness (ablation, representation, decoders and pricing).

**Rules for card components:**
- **PC-1 Uniform.** Each component has one L₀ definition for every instance. It has no branch on scenario name, size, party count, setting count, dimension, resolution or item identity (SD0 firewall 3).
- **PC-2 Priced** exactly like law clauses (§4). Calling something "extraction, not law" earns no discount.
- **PC-3 Covariant** under the moves of §1.6.
- **PC-4 Decidable** within the declared resources (§16).
- **PC-5 Ablatable.** The component runs unchanged when 𝒦 is replaced by a null law (NR-4), and it is total on Dom_pre. It may return ⊥ explicitly.
- **PC-6 Upstream-only reads.**
  - X_Π reads (Ξ, 𝒞) only.
  - X_Z reads (Ξ, Π).
  - X_h reads (Ξ, Π, Z_Π) and Obs's declared static structure.
  - X_T reads (Ξ, Π, Z_Π, [h]).
  - Obs reads (Ξ, Π, [h]) and each protocol's action on S.
  - **No component reads** Γ, any P_a, records, any functional of record laws, ε, chart coordinates, battery verdicts, or protocol identity beyond the protocol's action on S.
  - Persistence and identity measures used anywhere in the chain are functionals of Ξ-level structure only.
  - A violation makes every relation whose coupling passes through the illicit read **CARD-DEFINITIONAL**.
- **PC-7 Components carry no target content.**
  - NR-2's target-level test, the decoders (NR-6, NR-7), JN (NR-17) and the responsibility map apply to components exactly as to clauses.
  - If the components alone, together with the type and 𝒮, imply ℛ★ on Dom_pre^chain, then ℛ★ is DEF-12.
- **PC-8 Statement and implementation.**
  - The L₀ statement is normative. The Recomputer derives Sol and every credited quantity from it independently.
  - Where the statement is ambiguous, the frozen reference implementation fixes the reading, and that disambiguating behaviour is priced as a clause (IP-2).
  - Implementation behaviour that selects within Sol and is not fixed by L₀ (tie-breaking, ordering, initialization, tolerance) makes the affected claims CARD-UNFORCED.
  - Any call from card code into charter code (B-HB, the ε code, the 𝒮-checker) → RELOCATED.

### 1.3 Generated structures

**Π(Ξ), the partition.**
- Its blocks are one designated environment block E and one or more system blocks S. Multipartite embeddings use blocks S₁…S_m (§15.1).
- An approximate Π is an assignment V → Δ(blocks). It may leave a boundary ∂ of unassigned relata, with |∂|/|V| ≤ δ_∂ [P].
- The **persistent core** (S_core, E_core) is the set of relata that are never reassigned across A and t ≤ H. Records are read from the core only.

**Persistence and A-stability.** Let VI_norm(Π, Π′) := VI(Π, Π′)/log₂|V|, Meilă's variation of information under the uniform measure on V. Π is persistent and A-stable if and only if **both** tests pass and the reassignment bound holds:
- (a) **against the reference:** VI_norm(Π_a(t), Π_ref) ≤ δ_Π for every a ∈ A and every t ≤ H, where Π_ref comes from the reference protocol a₀;
- (b) **pairwise:** VI_norm(Π_a, Π_b) ≤ δ_Π across protocols;
- the reassigned fraction is ≤ η [P], with elements of ∂ counted as reassigned.

**Horizon.**
- H ≥ max(the full protocol and record window, 10·τ_int, 3·τ_slow).
- The **Evaluator** computes τ_int (the fastest internal timescale) and τ_slow (the slowest relaxation time, for example the inverse spectral gap) from the law at the truncation.
- If τ_slow is not computable, Π must be shown invariant under the realized stationary dynamics. Otherwise DIF-2 fails.

**Scale window.** If the card uses any coarse-graining scale or threshold (priced, IP-5), Π must stay within δ_Π when each such scale is multiplied or divided by w [P].

**Nontrivial Π.**
- S ≠ ∅ ≠ E and Π ≠ ⊥.
- Π is not the partition into components that are disconnected in the inputs.
- Γ_Π is not constant across A.
- **Size:** log₂|𝒜_Π(ι)| ≥ b_Π [P] on the lock fibers, and the law's selection removes at least b_Π bits beyond the IP-14 price of the ontology choice.

**Z_Π, the carrier.**
- Its dimension is arbitrary.
- *Which* variable it is (instantaneous, initial or other) is a derived output and never a definition (R1 §12 item 5; D5 Remark D3; NR-10).

**[h]_{T_Π}, the readout class.**
- h maps states of Z_Π to the record space 𝒴. It is fixed only up to T_Π: h ~ t∘h.
- The class must be derived as the readout redundancy of the card's own observation map.
- The record space, its coordinates and its σ-algebra are outputs of this derivation.
- No unique coordinate formula for h is credited (G2-11).

**T_Π, the interface class.**
- A group of record maps generated from (Ξ, Π) under PC-6.
- Elements may differ per protocol (the R1 form Y_a = t_a(W)). The class itself may not be generated from protocols or records.
- It is placed in 𝕃_T (§1.4).

**Γ_Π := Obs_Π(Ξ) = (P_a)_{a∈A}.**
- P_a is the law of the record Y_a ∈ 𝒴^τ under protocol a.
- **Only per-protocol laws are data.** Joint laws across protocols are inaccessible-context data (FR3).
- A Γ given as an empirical model is supplied, not generated (FR13).
- Under an approximate Π, Γ is read on the core, and every credited quantity must survive boundary ablation (NR-11(b)).

**Carrier status.**
- **PASS** if and only if the card proves from 𝒦 that Y_a = t_a(h(Z_Π)), with one h, t_a ∈ T_Π and Z_Π derived, for every a in every A ∈ 𝔄.
- **FAIL** if the derivation produces protocol-dependent readouts h_a.
- **UNRESOLVED** otherwise. This counts as a failure (DC-6).
- R1's verdict table applies unchanged: R1-PASS, R1-NULL, NO RECIPROCITY VERDICT, MODE SELECTION.

### 1.4 ε_R and the interface lattice
- **Definition (frozen R1).** ε_R := ε[Γ_Π, T_Π] := inf over P★ of max over a ∈ A of d_op^{T_Π}(P_a, T_Π·P★).
  - It is computed **only by charter code**, on **continuous** records. The finite alphabet of Appendix A is used only for support-level objects, never for ε.
  - No per-card normalization or alternative distance is allowed.
- **Catalogue 𝕃_T.**
  - E₂± ⊂ T_caus ⊂ T_lin, where T_lin = T_R1 = GL(k) with translations;
  - T_mono ⊇ E₂±, and T_lin ∩ T_mono = E₂±;
  - the join J;
  - T_univ and the GY-11/GY-12 classes.
- **Admissible set 𝕃_T^adm** = {E₂±, T_caus, T_lin, T_mono} ∪ {generated T_Π with a valid s_T}. An ε value taken at J, at T_univ, or at a class without a valid s_T is **void**.
- **Frozen d_op.** For T_lin it is d_q^BL (center, whiten, then O(k)). For T_mono it is the normal-score form modulo reflections. d_BL keeps its frozen normalization (R1 §1).
- **A generated T_Π outside the frozen tiers.** The card supplies s_{T_Π} with residual compact group K and proves:
  - (i) **invariance:** d_op^{T_Π}(P, T_Π·Q) := min over k ∈ K of d_BL(s(P), k#s(Q)) is invariant under T_Π acting on both arguments;
  - (ii) **maximality and faithfulness:** d_op^{T_Π}(P, T_Π·Q) = 0 ⇔ P ∈ cl(T_Π·Q). The Recomputer checks (ii) on the frozen chart.
  - s_T is priced as a component and run inside charter code.
  - Without (i) and (ii), ε_R is undefined for that card, and every relation that uses ε_R fails Q8.
- **Witnesses.** Witness families and their constants are frozen with the card (C8).
- **Decision semantics for ε.** ε is not exactly computable in general. An ε-equality or ε-inequality is decided in one of two ways:
  - by a theorem; or
  - against the frozen enclosure [frozen witness lower bound, frozen-optimizer upper bound]. The claim holds if and only if the enclosure lies inside the claim's priced band and is separated from the band's boundary by at least 2^(−p★).
- **The R1 ladder stays closed** (G2-10). A generated T_Π is a card output, never a new R1 tier. If T_Π equals T_R1 or T_mono, that equality is a result to be proved, and it imports no R1 theorem (NR-10(k)).

### 1.5 Scenarios, instances, fibers and charts

**Scenario σ** (observable level, independent of any card): a finite port set (intervention and record ports), a repertoire A_σ, a grid τ_σ and a record space 𝒴_σ.
- 𝒜_Γ and 𝒜_T are counted at this level.
- 𝒜_Π is counted on the instance's relata set V; the ontology choice is priced (IP-14).
- In B-SEL support scenarios only the Γ axis is scored.

**Audit instances** ι = (𝒞_ι, V_ι, A_ι, τ_ι, 𝒴_ι):

| Family | Content | Generated by |
|---|---|---|
| AI-1 | The smallest nontrivial instance, computed exactly | The card; the evaluator may add more |
| AI-2 | Symmetric-input instances, with Aut transitive on V or on the candidate partitions | The evaluator |
| AI-3 | A generic ensemble drawn from the charter reference measure, with seeds committed after the batch closes. The measure is fixed per primitive type in its canonical parametrization: uniform on finite sets, log-uniform on default ranges. The truncation contains every configuration of size ≤ n_min [P] | The evaluator |
| AI-4 | Battery embeddings via Emb. Never used for credit | The harness |
| AI-5 | Sealed holdouts (§15.9) | The Selector |

**Credit instances.**
- I_𝒦 := AI-1 ∪ {N_cred − 1 instances that the Selector draws from AI-3, inside the frozen domain predicate (DIF-7), after the batch closes}.
- Instances are **structurally distinct** if and only if their 𝒞 are non-isomorphic and their seeds are disjoint. The auditor decides.
- Credit per instance is the **minimum** over I_𝒦.

**Lock fibers.**
- A lock fiber is a pair (ι, H): an instance together with a regime class (§13.2).
- The card declares at most 3 lock fibers at freeze. **At least one must be regime-matched to the LT-1 platform:** H(fiber) ⊇ H_host(platform), certified under MC-6.
- The **hostile fiber** at ι uses H_host: every hypothesis that is not certified to fail by at least 3·r_lock (BP-4).
- **Robustness:** Q1, Q5, Q6 and Q9 must hold on a neighbourhood of each lock-fiber instance whose relative size is at least max(2^(−p★), the platform's certified parameter uncertainty), checked as in DIF-6. Otherwise the card is CARD-UNMEASURABLE at S7.

**The chart φ_ι (frozen).**
- The harness generates it before Card 1, for each scope and resolution:
  - scope Q: every T-invariant witness coordinate of order ≤ m on the template grid;
  - scope G: the response functionals of Appendix A;
  - the interface side: the observables listed in §3.3 (LT-1).
- It has box windows and resolution 2^(−p), per Appendix A.
- Cards neither add nor remove coordinates.
- The auditor may register up to N_ch [P] further coordinates before evaluation. Credit is the minimum over {the frozen chart, the frozen chart plus the registered coordinates}.

**Chart rules.**
- **Ch-1** Every claim must hold at r★ and at r★★. Credit is the minimum of the two values.
- **Ch-2** Scoring uses frozen templates. The card chooses no battery items and no scoring repertoires.
- **Ch-3** Finer grids, higher precision, copies of instances or a larger carrier earn nothing.
- **Ch-4** A truncation artifact earns zero: a relation that holds at r★ but fails at r★★ or at the next truncation level (DC-4).
- **Ch-5** Credit is summed only across structurally distinct instances with independent data.

### 1.6 Representation moves (FR1)
- **RM1** Relabel the elements of finite sets.
- **RM2** Relabel outcomes, interventions and ports.
- **RM3** Reparametrize continuous parameters by declared bijections.
- **RM4** Use an equivalent presentation of a conditional-response kernel (one that induces the same laws).
- **RM5** Re-bracket compositions.

The declared moves must include RM1–RM5. Any further move is priced. **Every representation move acts identically on every protocol;** a move indexed by protocol is mode selection (R1 §0). Invariance is claimed only under the declared moves, against a declared generating set that the harness verifies.

### 1.7 Repertoire
- The repertoire is a **function of the generated Π**. It is the frozen protocol templates (Appendix A) applied to the generated S through the template-to-Ξ map. That map is part of Emb: uniform, priced and frozen.
- A_{r★} and A_{r★★} are mandatory. 𝔄 is closed under sub-repertoires that have |A| ≥ 2 and contain a₀.
- A restriction to a sub-repertoire is declared at freeze and costs log₂(the number of admissible choices) (IP-4). No repertoire is selected after any score.
- a₀ may appear on both sides of a lock (route (ii), §3.3) only if the two sides use records from independent runs.

---

## 2. Owner item 1: baseline freedom spaces

### 2.1 Principles
- **BP-1 What the baseline is.** Everything established physics permits for operational data of the same type, in the same regime, from the same inputs (via θ_dict, §2.2), with Π, Z, [h] and T **supplied by hand**. It is computed after 𝒮 (§13) and after removing the classes killed in the GRAVEYARD.
- **BP-2 Where standard theory leaves freedom.** Standard theory leaves Π, Z, [h] and T to the modeller and constrains Γ through 𝒮. Every R1 claim was conditional on a carrier supplied from outside.
- **BP-3 Regime matching.** Claims about a realization x are compared only with the baseline under H(x). A witness drawn from another regime is invalid. A generated regime property puts the fiber in that regime (S:A13).
- **BP-4 Hostile regime default.**
  - A hypothesis holds at x unless two conditions are both met: a deviation δ ≥ 3·r_lock (r_lock, Appendix A) is certified on the lock platform, and δ ≥ 2^(−p★) in the frozen regime metric of Appendix F. The deviation is judged at charter resolution, never at the card's resolution.
  - A hypothesis that fails by δ still imposes its **near-regime consequences**, with published perturbative error bounds: linear response about the regime; FDT-violation and Harada–Sasa bounds; ensemble-equivalence corrections; Onsager to O(affinity).
  - A hypothesis that is ill-typed for the declared type is evaluated through its Appendix-F surrogate. If the surrogate is undecidable, the hypothesis holds.
- **BP-5 Same or more inputs.** The baseline receives, at zero price, the union of:
  - (i) every datum the card's prediction consumes;
  - (ii) every datum used to fix a constant that enters the prediction (θ_K, θ_dict, platform calibration);
  - (iii) the **standard reference package**, measured in a calibration run disjoint from the lock records: every statistic of P_{a₀} (connected correlators up to order m★★ on the frozen grid); the independently calibrated linear-response functions of the driven and recorded variables; and every regime parameter a standard modeller calibrates (temperature, spectral densities, conserved-charge values);
  - (iv) all MC-6 certification data;
  - (v) Θ_std: every parameter standard theory would use for O that can be measured without the lock records, declared in C13.

  The card's prediction may use the same union.
- **BP-6 Generation grants no exemption.** Every standard theorem conditioned on a supplied partition, readout or interface applies verbatim to a generated one. A framework is applicable at x unless the card proves that one of its hypotheses fails at x by at least 2^(−p★).
- **BP-7 Asymmetric enlargement.** The evaluator may enlarge standard families for Q3 transplant and genericity draws, for 𝒮 derivations and for narrowing J_SRB. It never enlarges FB, dim_lb or 𝒜^base, because that would help the card.

### 2.2 Standard models
- **𝔐_std(ι | H)** is a frozen generative grammar: the B-HB families (§15.4), their compositions by juxtaposition or by Hamiltonian or generator coupling within the frozen ranges, and card-added models that are independently verified (§15.4).
- SFP frameworks (§8) serve as derivation sources for 𝒮 and as comparators. They are not open model classes.
- A model belongs to the set if it:
  - (i) produces data of the declared operational type on ι;
  - (ii) satisfies every STD constraint whose hypotheses lie in H;
  - (iii) uses the card's inputs through the dictionary **θ_dict**;
  - (iv) takes Π, Z, [h] and T as supplied.
- **θ_dict** maps the card's instance inputs to standard-model parameters.
  - It is declared, priced (IP-2), and used identically for the baseline and the lock.
  - The auditor may narrow it when the declared meaning of 𝒞 (FR11) fixes more standard parameters than θ_dict uses.
- **Single-model realization.**
  - Any interface-side quantity u that is a functional of the dynamics (relaxation of ∂, exchange rates, persistence statistics) is a chart coordinate computed from the **same** model m that produces Γ.
  - A mixed point (u, Γ) belongs to the baseline only if a single m ∈ 𝔐_std(ι|H) realizes it.

### 2.3 The spaces

**𝒜_Π(ι | H): partitions.**
- Defined as {⊥} ∪ {Π persistent and A-stable (§1.3) under some m ∈ 𝔐_std(ι|H)}, modulo Aut(𝒞_ι). The harness computes Aut(𝒞_ι).
- **The "no dynamics" branch** admits every partition with S ≠ ∅ ≠ E: 2^|V| − 2 partitions with one S, and all ordered set partitions with a designated E for multi-block embeddings. It applies only if the Intake auditor confirms that the FR11 meaning admits no standard dynamical reading.
- Otherwise, the SPS panel (§5.4) and the STD-10/SFP-7 criteria are applied to the **realized dynamics of Sol** as well as to 𝒞, and the smaller set governs.
- A STANDARD-MECHANISM verdict (B-DIF (viii)) sets ΔF_Π := 0.

**𝒜_T(ι, Π | H): interface structures ([h], T).**
- T ∈ 𝒯 ∪ {⊥}, where 𝒯 = {E₂±, T_caus, T_lin, T_mono} is frozen.
- h is any readout of a declared E-state variable, common across A by hand.
- T must be causally implementable (STD-1) and CP-implementable (STD-2), and must contain the platform's calibrated maps.
- 𝒯 excludes the GY-11 and GY-12 classes, J and T_univ.
- For membership in 𝒜^base, a generated T_Π counts as a class that can be supplied by hand. The T-term is reported only (FC-3).

**𝒜_Γ(ι, Π, [h], T | H): record families.**
- Defined as {Obs(m) : m ∈ 𝔐_std with this (Π, Z, [h], T)}.
- With H = ∅ this is the set of non-anticipating, positive families on 𝒴^τ indexed by A (the grid-level E_univ). Each hypothesis in H intersects that set with its constraint list (Appendix F).
- Under RH-SYM(G), 𝒜 consists of G-covariant models, with partitions taken up to G.

**𝒜_ε** := {ε[Γ, T] : (Γ, ([h], T)) jointly admissible}. This is an **image, not an axis** (Addition 2). No bits are counted on it.

**FB = 𝒜(ι | H), the fibered joint baseline.**
- It is the set of pairs (u, Γ), where u = (Π, [h], T, interface-side coordinates), with each component admissible given the earlier ones.
- It includes every type-level dependence of Γ_Π = Obs_Π(Ξ) on Π.
- The standard couplings (STD-5, STD-7, STD-10, STD-13) live inside the fibers.
- Freedom reduction is measured inside FB, never against the product 𝒜_Π × 𝒜_T × 𝒜_Γ.

**𝒟(ι), the definitional space.** All well-typed tuples, with ε substituted, **before** 𝒮 is imposed:
- Π is any partition of V;
- [h] is any class;
- T ∈ 𝕃_T^adm ∪ {T_Π};
- Γ is any family of per-protocol laws on 𝒴^τ indexed by A.

**Intractable quantities.** A baseline quantity that no terminating frozen procedure can compute within the work-order budget contributes zero credit on its axis: b_J = 0 wherever it enters.

**The null hypothesis Stage 3 must break.** Standard physics treats Π, T and the generators of Γ as independent modelling choices, coupled only through 𝒮.

### 2.4 Values fixed now
- **(2,2,2), possibilistic object:** 2961 pNS tables.
  - 1721 are local.
  - 1232 are logically contextual. Of these, 992 have an exact-support realization and 240 do not.
  - 8 are strongly contextual, and these are exactly the 8 PR boxes.
- **(2,2,2), record-law object:** 2721 exact-support-realizable supports.
- **Interface catalogue:** |𝒯 ∪ {⊥}| = 5.
- **Partitions of n relata with one S:** 2ⁿ − 2. For n = 8 that is 254, about 7.99 bits.
- **Everything else** is computed by the evaluator with the frozen procedures of §2.5, never by the card.

### 2.5 Measuring freedom reduction
- **The realized image.** Im_σ(Sol), in the coordinates of FB, is the **full** realized image.
  - A point in Im \ 𝒜^base is a non-standard realization. Each one is reported and is a declared prediction with its own kill condition. If it contradicts an established relation inside that relation's tested domain, KU-4 applies.
  - Non-standard realizations are **never removed** to shrink the realized set.
  - Q1, Q5, Q6 and Q9 use Im.
- **Rectangle hull.**
  - For X ⊆ FB: Rect(X) := {(u, Γ) ∈ FB : u ∈ π_I X, Γ ∈ π_Γ X}. Here π_I projects onto the interface coordinates and π_Γ onto Γ, and membership follows the single-model rule (§2.2).
  - Rectangles are formed **within fixed-T fibers**, or with ε evaluated at one frozen class on every point (DEF-14).
  - Z_ℛ := Z(ℛ) ∩ FB.
  - Rect_𝒟 is the same construction with 𝒟 in place of FB.
- **Coupling codimension.** c_J(ℛ, ι) is the minimum of three quantities:
  - (a) dim_lb Rect(Im) − dim_ub(Rect(Im) ∩ Z(ℛ));
  - (b) dim_lb Rect(Z_ℛ) − dim_ub Z_ℛ;
  - (c) for every standard class M ⊇ Im with Price(M) ≤ Price(𝒦), the codimension of Z(ℛ) ∩ Obs(M) in Obs(M).

  c_J never exceeds the number of functionally independent scalar equations in ℛ.
- **Coupling bits (discrete coordinates).** κ_J(ℛ, ι) is the same three-way minimum, taken in log₂ cell counts at resolution 2^(−p★).
- **Coupling credit.**
  - b_J(ℛ) := N_cred · min over ι ∈ I_𝒦 of [p★·c_J^lock(ℛ, ι) + κ_J^lock(ℛ, ι)].
  - It is computed after 𝒮, at both r★ and r★★, and the minimum is taken.
  - The superscript *lock* restricts the count to scalar equations of ℛ that some registered lock observable tests.
  - One codimension is worth exactly p★ bits. Window bits are not credited.
- **Dimension certificates.**
  - dim_ub is the **generic** rank. It is certified in one of three ways:
    - by a proof;
    - by c explicit equations, verified by exact symbolic identity to vanish on Im within the window, whose Jacobian has generic rank c, with the singular locus certified to be of lower dimension;
    - by a proof that the parametrization is analytic on a connected domain, together with the exact rank at points drawn with post-batch seeds (the maximum is taken).
  - A rank at a chosen point certifies only dim ≥ that rank.
  - dim_lb is certified on a regime-matched box around the same generic point, by B-HB witnesses that meet the witness rules of §15.4.
- **Reported, never credited:** marginal reductions (proj Im ⊊ FB on one side), ΔF_Π, ΔF_T, ΔF_supp, and reductions of log-volume through inequalities.
- **Nontrivial reduction** (SC1). All of the following must hold:
  - Q5 and Q6 on every lock fiber;
  - the §3 witnesses exist;
  - the anchors are retained (§15.8);
  - Im satisfies 𝒮, apart from declared violations outside 𝒮's established domain, each with its own kill condition;
  - the excluded set FB \ Z(ℛ) has nonempty relative interior in FB (positive reference measure on discrete parts), meets {ε > r_lock}, and meets the region where the card's Π is realized.

---

## 3. Owner item 2: success criterion

### 3.1 Qualifying relation: certificates Q1–Q12
A relation has the form ℛ(Π, [h]_{T_Π}, T_Π, Γ_Π) = 0, with zero set Z(ℛ). ε_R enters only as ε[Γ_Π, T_Π] and is never a coordinate. ℛ★ must hold **every** certificate, at both r★ and r★★.

- **Q1 Forced.**
  - Im(ι) ⊆ Z(ℛ) on every in-domain instance (AI-1 to AI-4 and the holdouts), for every A ∈ 𝔄 and every grid in 𝔗.
  - It holds on **all of Sol**, not on a selected subset (FR8).
  - It must be at DERIVED grade: a theorem, or exact computation on every finite battery instance plus a proof for the declared scope. ε-claims follow the decision semantics of §1.4.
  - It must hold without relying on any pending or evidence-grade item (§11).
  - Forcing at evidence grade only gives CARD-UNFORCED.
- **Q2 Non-definitional.**
  - Some tuple in Rect_𝒟(Z(ℛ)) \ Z(ℛ) exists, so the coupling part can be violated in 𝒟.
  - ℛ is none of DEF-1 to DEF-17 (§12), and is not implied by them on the realized fibers.
  - ℛ restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R.
- **Q3 Non-standard.** For each regime class H on which ℛ is claimed:
  - (a) **Witnesses.**
    - At least two SFP frameworks must be applicable under H (BP-6). Inapplicable frameworks are listed with reasons. Fewer than two applicable frameworks → Q3 fails.
    - For each applicable framework F, a witness m*_F ∈ 𝔐_F(ι|H) is required, where 𝔐_F means the 𝔐_std models built in F.
    - The witness is regime-matched and comes from B-HB, or is added by the card and verified independently.
    - Obs(m*_F) ∈ Rect(Z_ℛ) \ Z(ℛ), and the witness violates ℛ by at least 3·r_lock. For discrete relations, violation means a certified membership change.
    - A witness that violates only a single-axis consequence of ℛ does not count.
  - (b) **Genericity.**
    - A witness counts only if ℛ fails on an open neighbourhood of it within its standard family. For discrete families, the neighbourhood must have positive reference measure.
    - If ℛ holds on an open dense subset of the image of 𝔐_F(ι|H), it is **STANDARD-GENERIC** and is not credited.
  - (c) **Transplant.**
    - For each lock fiber, the Evaluator draws standard models of the declared type from NULL-ΠT under H. B-HB parameters are generic under the charter reference measure, with post-batch seeds.
    - It runs the card's own components on them, using the card's realized Π wherever X_Π is undefined, and then the charter ε code.
    - If ℛ★ holds within r_lock on a fraction f_std ≥ 1/Q_min of the draws → CARD-STANDARD.
  - (d) **Hand-supplied interfaces.** A witness whose interface is supplied by hand is reported, but it never satisfies Q3 by itself.
  - (e) **Constructive rule.** STANDARD status is decided constructively. Without witnesses that meet (a) and (b), ℛ is STANDARD by default. Any cited standard derivation (§13.4) also makes it STANDARD-IMPLIED.
  - (f) **Excluded forms.**
    - ℛ is none of the D5 reverse-direction relations (§13.8), and is not implied by them on its lock fibers.
    - It is not the saturation of a standard bound, unless it survives the boundary rule of §13.5.
    - A relation of the form "response = X·correlation" is STANDARD unless X is predicted from interface-side data and beats B-SRB by Q_min.
- **Q4 Law-dependent.**
  - A W-pipe exists: some Ξ ∈ Dom_pre^chain \ Sol whose pipeline image violates ℛ.
  - The responsibility map (NR-4) shows that ℛ depends on 𝒦's clauses, not on the type, the components, the representation or a prior.
  - ℛ survives JN (NR-17).
- **Q5 Joint.**
  - On every lock fiber, c_J ≥ 1 or κ_J > 0 (§2.5).
  - One rectangle witness is necessary, not sufficient. A rectangle witness is two realized points of Z(ℛ) in one T-fiber whose single-model cross pairs lie in FB, with at least one cross pair outside Z(ℛ).
  - None of the following is a qualifying ℛ: a restriction on one axis; a coupling of Π and T alone; a disjunction of single-axis restrictions; a coupling carried only by ε's T-argument.
- **Q6 Informative.**
  - c_J ≥ 1 or κ_J ≥ log₂ Q_min on every lock fiber.
  - b_meas ≥ log₂ Q_min (MC-4).
  - A relation that fixes only a sign or a zero carries at most 1 bit and fails.
- **Q7 Representation-invariant.**
  - ℛ is invariant under h ↦ t∘h for t ∈ T_Π, under the declared (protocol-uniform) moves of Ξ and 𝒞 (§1.6), and under relabellings of V.
  - It depends on Γ only through the per-protocol laws (FR3).
- **Q8 Admissible interface.** Every ε value is taken at T_Π ∈ 𝕃_T^adm with a valid s_T (§1.4).
- **Q9 Non-vacuous.**
  - Scope Q: every lock fiber contains certified realized points with ε_R > r_lock, and ℛ is not satisfied merely because ε_R ≡ 0.
  - Any scope: on each lock fiber, FB admits points with ℛ = 0 and points with ℛ ≠ 0, and points with ε = 0 and points with ε > 0. The excluded set also meets the nontrivial-reduction conditions of §2.5.
- **Q10 Scoped.** Exactly one response scope is declared for each relation and frozen with the card, and ℛ is consistent with it (§14).
- **Q11 Neutral.**
  - Any sign, monotonicity, tradeoff or functional form in ℛ is an output of the derivation from 𝒦.
  - The W-pipe must show that the pipeline alone would also admit the opposite sign.
  - A sign that is supplied is a supplied target relation (§5.6).
- **Q12 Named.** ℛ★ is entered in the **lock register** at freeze, together with its LT-1 instantiation (§3.3).

**Number of relations.**
- A card has at most 2 relations, exactly one of them primary (ℛ★).
- The secondary relation costs log₂ 2 = 1 bit of selection (IP-4) and shares the Bonferroni correction (MC-9).
- It never replaces ℛ★, and it earns credit only through the conjoined credit of FC-1.
- A falsified observable of either relation fires KU-12.

### 3.2 Success thresholds
A card succeeds only through all of the following, and only while it remains admissible (S0–S9, §18):
- **SC1 Nontrivial freedom reduction.** Q1–Q12 hold at r★ and r★★, and the nontrivial-reduction conditions of §2.5 hold on every lock fiber, after 𝒮.
- **SC2 Positive compression.** §4.5.
- **SC3 Measurable consequence.** An admissible and feasible LT-1 instantiation (§3.3) on a named existing platform. There is no "in-principle" grade.
- **SC4 Never credited toward SC1–SC3:** the items in §22.

### 3.3 Named lock target LT-1: the Interface–Response Residual (IRR)
ℛ★ is evaluated on a physically realized environment with a certified carrier. It predicts at most 3 lock observables o⃗, each a frozen chart coordinate, in one of two ways:
- (i) from **interface-side quantities** measured independently. These are the chart's interface-side observables: VI_norm and the reassigned and boundary fractions of the platform's Π, the T_Π tier verdicts, and the carrier certification outcome, all obtained as MC-2 requires;
- (ii) from **response-side data** on protocols, record channels and grid times that are all disjoint from O's. a₀ may be shared only with independent runs (§1.7). The map from those inputs to I_K must not be derivable from DEF-1 to DEF-17 ∪ 𝒮 alone.

No parameter is fitted on lock data. **The quantity locked is the SRB residual: the part of the prediction that B-SRB, given the BP-5 inputs, leaves free.**

**Measurement rules.**
- **MC-1 Observable type matches scope.**
  - Scope Q uses a T-invariant observable, taken at a frozen tier or at the generated T_Π, or a frozen witness.
  - A **witness lock** is admissible only if ℛ★ fixes the witness value on the lock fiber: either ℛ★ is stated in terms of the frozen witness, or w = ε is proved at DERIVED grade on that fiber.
  - An I_K with an endpoint at a DEF-2 or DEF-5 bound is a sign test, and is inadmissible.
  - Scope G uses a response functional.
- **MC-2 Independence, sensitivity and identification.**
  - **Sensitivity.** Replacing every independent interface-side input by its full admissible range over 𝒜_Π × 𝒜_T must widen the predicted region J_K by a factor of at least Q_min in cell count. That is, I_int := log₂(N(J_K^{∅I}) / N(J_K)) ≥ log₂ Q_min. Otherwise the lock is a pin: it is DEFINITIONAL (CT-34) and SC3 fails.
  - **Platform interface.** The platform's Π and T_Π are obtained by applying the card's frozen X_Π and X_T to interface-side structural data only: geometry, independently measured couplings, apparatus specifications, and records of declared calibration-only protocols outside A. No functional of the record laws of any protocol in A, or of the route-(ii) inputs, may be used. Selecting the cut by maximizing a record functional is prohibited.
  - Π and T_Π are certified independently of the records used to test ℛ★. A certification that presupposes ℛ★ is circular.
  - The carrier cannot be certified from records (R1 §3).
  - Predicting ε_R from the same Γ it is computed on is definitional.
- **MC-3 Prediction.**
  - I_K (the joint region J_K) is frozen in C13, with every uncertainty propagated, truncation error included.
  - Every error term entering ℛ★ (leakage of an approximate Π, truncation, coarse-graining) must be bounded by 𝒦, and the predicted effect must exceed that bound by a factor of at least Q_min. Otherwise the lock is **UNFALSIFIABLE**, which is a FAIL at S7.
  - σ_pre, the preregistered total uncertainty with systematics included, is frozen in C13, with σ_pre ≤ |I_K|/4.
- **MC-4 Discrimination.**
  - b_meas := log₂(N(J_SRB ∩ W) / N(J_K ⊕ 2σ_tot at N_max)) must be ≥ log₂ Q_min. Here N(·) counts 2^(−p★) cells of the frozen chart coordinates, in frozen units, within the windows W.
  - Reparametrizing o⃗ is prohibited. b_meas is the minimum over {the frozen coordinate, log|·| of it where it has one sign on J_SRB}.
  - **J_SRB** (B-SRB, §15.5) is computed before unsealing and intersected with W.
  - **Live rival.** At least one verified standard witness consistent with every BP-5 input must predict O outside I_K by at least 3σ_pre. MC-7's power is computed against the nearest such rival.
  - For scope Q, additionally: I_K ∩ [0, 3σ_pre] = ∅.
  - A lock that predicts O only from amplitude-scaled or sign-reversed versions of O's protocol must beat the order-(|A|−1) Volterra interpolation by Q_min (STD-14).
  - A lock that tests only a sign is inadmissible.
- **MC-5 Thresholds.** Let σ_eff := max(σ_pre, σ_stat).
  - **LOCK-FALSIFIED** if dist(O_meas, I_K) > 3σ_eff.
  - **LOCK-CONFIRMED** if dist ≤ 2σ_eff, σ_eff ≤ |I_K|/4, and MC-4 holds.
  - **LOCK-VOID** if the realized systematics exceed 1.25·σ_pre.
  - **LOCK-INCONCLUSIVE** otherwise. On the primary platform (and on the alternate, if used) it is a **G5-LOCK FAIL**.
  - Any change to a threshold, observable, tier, protocol set, grid, estimator, platform or exclusion rule **after card freeze** → LOCK-VOID.
  - LOCK-VOID counts as LOCK-FALSIFIED.
- **MC-6 Carrier certification.**
  - The platform must pass the frozen 10-item checklist (Appendix G), adopted here as a Stage-3 rule and not as an edit to R1 (OD-9).
  - Certification is completed and frozen by hash, by an agent blind to O, before O is unsealed. It is never revised using lock data.
  - It must certify **the carrier the card derives**: the same state-variable class and readout class that C9 and RS-6 state.
  - If RS-6 predicted a certifiable carrier on the platform, then a failed certification, MODE SELECTION or NO RECIPROCITY VERDICT counts as LOCK-FALSIFIED. Otherwise it counts as LOCK-INCONCLUSIVE.
  - One preregistered alternate platform is allowed. It is used only if the primary fails MC-6 before any lock datum is unsealed. There is no third.
- **MC-7 Feasibility.**
  - The Evaluator computes N_req by simulating the frozen estimator on two cases: the card's in-silico realization at the lock fiber, and the live rival. Sample sizes are effective sample sizes from a frozen integrated-autocorrelation estimator. The larger of the card's value and the Evaluator's value governs.
  - Required: N_req ≤ N_max (a total per card), at the α and power of Appendix A, and at most 30 days of platform time in total. Otherwise the card is CARD-UNMEASURABLE.
  - Estimation uses per-witness forms; no plug-in d_BL for k ≥ 3. R1's D4 is not a prerequisite.
- **MC-8 Sealing.**
  - **LOCK-H:** requires an eligible pool of at least N_pool [P] archived datasets that pass MC-6. Ineligible datasets: those in the author's C1 "seen" declaration; those the card cites; those whose O value was published before card freeze (that is calibration, not a lock). The Selector draws from the pool with a committed seed.
  - **LOCK-E:** used when LOCK-H is not available. A prospective experiment, with its protocol committed before any data exist. Its data must be unsealed within T_lock [P] of G5-LOCK, or G5-LOCK fails.
  - In-silico evaluation (≤ 10¹⁰ effective samples) is evidence grade only and never confers PREDICTIVE.
- **MC-9 Multiplicity.** At most 3 lock observables per card. Thresholds are Bonferroni-adjusted across observables and across every card locked in the route (BU-7′).
- **MC-10 Status.**
  - LOCK-CONFIRMED requires every observable of ℛ★ to be CONFIRMED, on sealed real data. With an external check, it confers PREDICTIVE, on ℛ★ only.
  - LOCK-FALSIFIED on any observable of any registered relation fires KU-12.
- **MC-11 Platform.**
  - C13 names an existing platform with published operating parameters, in one declared class:
    - P-1: classical mechanical or stochastic environments with independently calibrated readouts;
    - P-2: mesoscopic electronic environments with calibrated detection of counting statistics;
    - P-3: engineered quantum environments with calibrated input–output readout;
    - P-4: archived datasets that meet MC-6 (LOCK-H only).
  - The Intake auditor pre-assesses each Appendix-G item as satisfiable on that platform. Otherwise the card is CARD-UNMEASURABLE.
  - If the platform's H contains RH-KMS, Q3 and B-SRB run with STD-3 in force on the platform-matched fiber.

---

## 4. Owner item 3: compression accounting and information price

### 4.1 Base language and code
- **L₀ (RULES 2):** finite sets, maps, interventions, conditional response, composition and logic.
- **Code:** the frozen 64-token alphabet in Polish notation (Appendix B.1). The 4 Reserved tokens are unavailable to cards.
- **Base-token typing.**
  - `kernel`, `cond-prob`, `E`, `law`, `marginal`, `support`, `⊗`, `parallel`, `pair` and `×` are base tokens only when every argument is an intervention, a record or a record law.
  - Applied to Ξ, 𝒞, V_Ξ or a relatum, they are priced vocabulary: VB-13 for measures, and VB-4 for splitting V_Ξ or 𝒳 into blocks. NR-1 also flags such a split as a PS-1 candidate.
- **Normal form.** Prenex negation normal form, with quantifiers explicit and no Skolem symbols, computed by the harness's frozen normalizer. L_stmt is computed on the card's own form instead, if that form is shorter and proved equivalent.
- **Statement length:** L_stmt(X) := 6·#tokens(X) + Σ over variable occurrences of ⌈log₂(v_X + 1)⌉ + Σ over literals of ℓ(lit).
  - v_X is the number of distinct variables in X.
  - ℓ(n) is the Elias-δ length of n + 1.
  - ℓ(n/d) := ℓ(n) + ℓ(d) + 1.
  - A real literal costs p + ℓ(|exponent|) + 1 at precision p.
  - A defined symbol costs its definition once, then ⌈log₂(#definitions + 1)⌉ bits per use.

### 4.2 Price components
Price(𝒦) is the sum of IP-1 to IP-14.

- **IP-1 Statement.** L_stmt of 𝒦 in normal form, plus the declaration of 𝒳 (sorts, arities, labels).
- **IP-2 Inputs.** Every supplied datum, encoded with the same code:
  - 𝒞 and the statement of its FR11 meaning;
  - carrier size, initial data, couplings, constants, scales and the time unit;
  - Emb (including the template-to-Ξ map) and the selectivity interface;
  - X_Π, X_Z, X_h, X_T, Obs and s_T;
  - θ_dict;
  - truncation levels, tolerances, thresholds and enumeration bounds;
  - representation moves beyond RM1–RM5;
  - domain restrictions;
  - disambiguating implementation behaviour (PC-8).

  **Priors and measures** cost max(L_stmt, D_KL(prior ‖ charter reference measure) in bits).
- **IP-3 Tables.** A symbol that encodes a table costs the whole table. Hand-listed configurations are tables. Quantifying over a list supplied in the inputs is also a table.
- **IP-4 Selection.**
  - Choosing an invariant, clause shape, component, framework or relation from a family costs log₂ m.
  - m is the size of the largest finite family that any auditor exhibits, either by citation or by an L₀ generator of items in the same role. A family the card cites is only a lower bound.
  - The item's price is max(L_stmt, log₂ m).
- **IP-5 Constants.**
  - Price = max(literal length at p, log₂(R / passing window)).
  - R := max(the declared range, the charter default for the constant's type, the largest natural range any auditor exhibits). The default for a dimensionless positive constant is [10⁻³, 10³] on a log scale.
  - The passing window is the largest window inside which I_K moves by less than ¼|I_K| and no verdict changes.
  - A value costs 0 only if a DERIVED theorem from 𝒦's clauses fixes it, with no expression introduced for the purpose. Otherwise it costs max(L_stmt(expression), tuning price), and every expression tried counts toward n_drafts.
  - Constants are repriced at p = 6, 10 and 16.
- **IP-6 Priced vocabulary.**
  - Each item VB-1 to VB-21 (Appendix B.2) costs P_v := max(L_stmt(def_v), ΔF_tgt(v)).
  - ΔF_tgt(v) := max(the credit of 𝒦 with only v, Credited(𝒦) − Credited(𝒦[v ↦ v̄])), where v̄ is an uninterpreted symbol with v's signature and with v's axioms deleted. SEL distinctions that change under this replacement are added.
  - **Closure.** The harness holds a frozen axiom checklist for each VB item. Any defined symbol whose interpretation satisfies a checklist on any audit or battery instance *is* that item, and costs P_v.
  - Every defined symbol carries a VB declaration. An undeclared match found later → RELOCATED.
  - Supplying, or matching, VB-5, VB-6 or VB-7 makes every selectivity result RELOCATED (SD0 firewall).
  - Every use is flagged on the ledger.
- **IP-7 Supplied protected structures** (§5.6). P_X := max(L_stmt(X), ΔF_tgt(X)), computed against 𝒟(ι) and never against 𝒜^base. Pricing never substitutes for generation (§5.1).
- **IP-8 Imports.**
  - An imported standard component is unfolded into L₀ before every firewall and pricing test.
  - Price := max(log₂|SFP menu| + its constants, L_stmt(the unfolding), Σ P_v over the VB items it uses).
  - NR-1, NR-2, NR-12, IP-6 and §5.6 apply to the unfolding.
  - Its consequences are baseline. Import subtraction applies to b(ℛ) as well as to D_sel.
- **IP-9 Case splits.**
  - Each branch costs 1 bit plus the price of its condition.
  - Branches keyed to scenario names, party or setting counts, dimensions, capacities, sizes, resolution or item identity are LOOKUP → RELOCATED.
  - A switch among m sub-laws that is not fixed by a priced condition decidable from the inputs consumes m slots (BU-9).
- **IP-10 Per-instance structure.**
  - A constant or clause is confined if ablating it changes at most 2 credited verdicts or instances. Effects on report, audit and holdout items are ignored in this count.
  - It costs max(L_stmt, the bits it flips), and its distinctions leave D_sel.
- **IP-11 Lock-side fits.**
  - Cost: log₂(range / posterior width). The prediction becomes a fit and cannot serve as a lock.
  - A law constant whose implied value falls within the passing window of a published platform-specific value, for any candidate LOCK-H dataset, is a lock-side fit.
- **IP-12 Selection tax.**
  - τ_sel := log₂(1 + n_drafts).
  - n_drafts counts every distinct 𝒦, or distinct assignment of constants, for which any score, verdict, price or chain output was computed or estimated, by any agent or program, since G2-11 (2026-10-07).
  - A template counts the size of its instance space. Reusing an archived proposal adds log₂(the archive's size).
  - A further log₂ N_frozen is charged at the owner's pick.
  - The search code and its logs are disclosed in C1. Undisclosed search voids the card (KU-10).
- **IP-13 Domain restriction.** Price := max(L_stmt(predicate), log₂ C(N, k)), where N is the size of the AI-3 batch and k is the number of AI-3 instances excluded.
- **IP-14 Ontology.** The choice of Ξ's type, alphabet and arity is a selection from the family of types any auditor exhibits (IP-4). This is charged in addition to IP-1.

### 4.3 Credited content
- **FC-1 Lock credit.**
  - b(ℛ★) := b_J(ℛ★) (§2.5). It is awarded only if SC3's b_meas gate passes (MC-4).
  - With a secondary relation, credit is computed **once**: b := b_J(ℛ★ ∧ ℛ₂), on Z(ℛ★) ∩ Z(ℛ₂). Each relation is still scored separately for Q1–Q12 and for its kill conditions.
  - Import subtraction applies.
- **FC-2 D_sel.**
  - 1 bit for each verified B-SEL verdict class, mandatory or graded, that the card reproduces, up to 10 bits. A class earns its bit only if both hold:
    - the closest B-CF* member (by Hamming distance on the mandatory and graded items) gets it wrong;
    - the reference law that admits every no-signalling support does not give the same verdict.
  - Removed:
    - distinctions implied by counted ones, or by structural facts of the SD0 record (T1; T2 once it is resolved). Each implication must be argued explicitly;
    - distinctions reproduced under 𝒦_∅ or 𝒦_𝒮 on Dom_pre, or by a vocabulary item or an import alone;
    - IP-10 structure;
    - consistency collapse (§15.2);
    - automatic items (SEL-0, SEL-4, SEL-12).
- **FC-3 D_diff = 0.** Persistence and differentiation are gates, not credits. ΔF_Π, ΔF_T and ΔF_supp are reported under SC1 and G4 only.
- **FC-4 Never counted:**
  - bits on 𝒜_ε;
  - restrictions implied by 𝒮 (RECOVERY);
  - definitional relations;
  - consequences of the priced inputs alone;
  - holdout successes;
  - credit obtained by removing realizations.

Credited(𝒦) := b + D_sel. ΔL := Credited − Price. ΔL₀ := b − Price, i.e. ΔL with D_sel = 0. ρ := Credited/Price.

### 4.4 Two-part code against the nulls
- On AI-1 and on the Selector-drawn credit instances:
  - L(𝒦) := Price(𝒦) + log₂ N(Im/~), using a uniform code over the 2^(−p★) chart cells within Im;
  - L(null) := Price(null) + log₂ N(the cells of 𝒜 the null needs to cover the same realized data);
  - L(𝒦) < L(null) must hold for **every** null below. Each cell count is used once.
- **NULL-ΠT.** Price := min(log₂|𝒜_Π/Aut|, the price of the cheapest SPS or RB selector that returns the null's Π) + log₂|𝒯 ∪ {⊥}| + the framework index, on the frozen chart.
- **NULL-M.** For every standard model class M published before the freeze and stated without reference to the card, the price is the sum of:
  - the framework choice (IP-4);
  - the statement of M (IP-1);
  - the constants of M fitted on the instance at precision p (IP-5);
  - (Π, [h], T) chosen by hand.
- Failure → NON-COMPRESSIVE.
- A Stage-5 form on sealed data is G5-MDL (§15.11).

### 4.5 Compression verdict

| Condition | Verdict |
|---|---|
| ΔL ≤ 0 at p = 10 | **LOOKUP**: CARD-RELOCATED (SD0 rule) |
| ρ ≥ 2, ΔL₀ ≥ p★ at p★ = 10, ΔL₀ > 0 at p = 16, and §4.4 holds | **COMPRESSIVE** (SC2 met). The value at p = 6 is reported |
| Otherwise | **NON-COMPRESSIVE** |

### 4.6 Mandatory ledger
- One row per item, with these columns: item · class (statement / input / vocabulary / supplied protected / selection / domain / ontology) · L₀ encoding · bits · hostile family size · ΔF_tgt · rule applied.
- Then:
  - for each credit instance: c_J and κ_J, with the dim_lb and dim_ub certificates;
  - b_J and b_meas;
  - D_sel, with its removals argued;
  - Price, ΔL, ΔL₀ and ρ at p = 6, 10 and 16;
  - the §4.4 comparison against every null;
  - the reported-only ΔF terms.

### 4.7 Disputes
- An ambiguity goes against the card.
- Any higher price an auditor raises governs until the owner rules (CV-7).
- Thresholds are never reopened.

---

## 5. Owner item 4: nonrelocation

### 5.1 Protected structures
- **PS-1 The partition Π**, including the party structure of embedded scenarios.
- **PS-2 The carrier, i.e. the environmental identity:** which E state variable counts as "the environment" (instantaneous versus initial; D5 Remark D3), and the protocol invariance of the readout.
- **PS-3 The readout class [h]:** any common-readout axiom, designated list of observables, or readout clause indexed by protocol.
- **PS-4 The interface class T:** its calibration and any group action on record space.
- **PS-5 Gibbs/KMS/FDT structure, defined operationally.** Any input from which a standard theorem (cited by the author or exhibited by a reviewer) derives one of the following:
  - a KMS state;
  - detailed balance or microscopic reversibility;
  - an exponential-family stationary law;
  - canonical typicality;
  - a fluctuation–response identity of any order.

  Examples of such inputs: invariant or thermal measures; temperatures; energy-weighted measures; a conserved quantity plus maximum-entropy closure; a reversible kernel; ergodicity plus weak coupling; a time-reversal involution plus stationarity; an exponentially weighted reference measure.
- **PS-6 The target relation ℛ★.** Also any relation that implies it, any monotone of it, any penalty, objective or selection criterion that contains it, and any presumed sign or identity–response tradeoff.

**Pricing never substitutes for generation.**
- A card that supplies PS-1 to PS-4, at any price, fails the corresponding generation gate (CARD-NONGENERATIVE).
- PS-5 supplied and declared is a priced commitment whose dependent claims earn 0 (§5.6).
- PS-6 supplied in any form → CARD-RELOCATED.
- FR5 and RULES 1 ("postulates are allowed if priced") govern unprotected inputs only.

**Prohibited inputs** (STATE):
- memory kernels, viscoelastic constitutive laws and crystalline order;
- R1 calibration data: the BRI1 grid, protocols, calibrated maps and constants.

**"Hidden"** means present, without being declared, in any input listed in §5.2.

### 5.2 Input inventory (the full input list for every test)
- clauses;
- Ξ-level data, typings, weights, and boundary and initial conditions;
- 𝒞 constants and parameter values;
- priors and reference measures;
- the type and representation (gauge) of Ξ;
- components;
- Emb, together with the Ξ→battery and template-to-Ξ maps;
- the protocol repertoire;
- coarse-graining scales, thresholds, tolerances and truncation levels;
- θ_dict;
- apparatus calibrations;
- scope declarations;
- imports, unfolded.

### 5.3 Tests (executed by the auditor; each is a finite procedure)
- **NR-0 Inventory closure.** The evaluator reproduces every verdict from the listed inputs alone, and the reference implementation reads nothing else. An undeclared input → RELOCATED.
- **NR-1 Vocabulary firewall** (syntactic; definitions and imports unfolded).
  - Scope: 𝒦, 𝒞, 𝒳, priors and Emb. Components are governed by PC-6 and PC-7.
  - The harness flags any symbol that names or encodes a protected structure. Examples:
    - Π or S/E labels, and typed sorts or blockings of V_Ξ that pre-split the relata;
    - h, [h] or readout maps;
    - T or record-space group actions;
    - Γ, Obs, ε, P★, d_op or "carrier";
    - measures, weights, temperatures, Gibbs, KMS, FDT, Onsager;
    - target-level coordinates, or ℛ.
  - A flagged symbol that is declared → SUPPLIED. A flagged symbol that is not declared → RELOCATED.
- **NR-2 Target-level firewall.**
  - Put 𝒦 in normal form. A clause (or a component, per PC-7) is target-level if it mentions records, chart coordinates, ε, interface maps, partition labels or readouts.
  - RELOCATED if, up to RM moves and unfolding, either:
    - the target-level clauses together with 𝒮 imply ℛ★ on 𝒟; or
    - ℛ★ is a clause, a conjunct, or a consequence of the clauses that mention only observable-level or pipeline terms.
- **NR-3 Two-witness.**
  - For each generated X ∈ {Π, Z_Π, [h], T_Π, Gibbs/FDT if claimed, ℛ★}, a W-pipe is required: some Ξ ∈ Dom_pre^chain \ Sol whose pipeline output lacks X or yields a different X.
  - For the carrier, the W-pipe is taken in Dom_pre^carrier \ Sol, where the carrier derivation returns FAIL.
  - No W-pipe → X RELOCATED (into the type, the pipeline or the representation).
- **NR-4 Law ablation and responsibility map.**
  - Run the pipeline on Dom_pre with 𝒦 replaced by 𝒦_∅ (type only), then by 𝒦_𝒮 (type plus 𝒮), then with single clauses deleted.
  - X appears under 𝒦_∅ on at least p_dec of the reference measure on Dom_pre, or on every lock-fiber instance → RELOCATED.
  - X appears under 𝒦_𝒮 but not under 𝒦_∅ → STANDARD-IMPLIED.
  - The resulting responsibility map is recorded. It feeds Q4, Q11, FC-2, JN and the GY return test.
- **NR-5 Symmetric-input probe** (mandatory) **and symmetrization.**
  - On AI-2, with Aut(𝒞_sym) transitive on V or on the candidate partitions:
    - every solution must carry a persistent, nontrivial, A-stable Π;
    - {Π(Ξ)} must be Aut-invariant, reported as an orbit, not as a labelled choice.
  - A symmetry-breaking parameter λ in 𝒞 is evaluated at λ = 0 (if in the domain), at 2^(−p★) and at 2^(−2p★). Differentiation must persist at all three. Only which side carries which label may follow the sign of λ.
  - **Generalization (NR-S).** Take any protected X with a group G_X of input transformations that preserves the input class and acts transitively on X's admissible alternatives. On a G_X-invariant input, 𝒦 must still output some persistent X, up to 𝒦's own symmetry. If X appears only on non-invariant inputs and moves equivariantly with them, X was supplied.
  - If the type of 𝒞 cannot be symmetric, its asymmetry is priced, NR-6 and NR-7 apply at full strength, and Π cannot be GENERATED-STRONG.
  - Fail → CARD-NONGENERATIVE.
- **NR-6 Decoder test.**
  - A decoder reads only the §5.2 inputs, is uniform (PC-1), and may not invoke 𝒦's selection, fixed-point, solver or evolution step.
  - It **fires** if it recovers X within tolerance on at least p_dec of AI-3 or on every lock-fiber instance. Tolerance means VI_norm ≤ δ_Π for Π, the same class for T and [h], and the same variable for the carrier.
  - Budget: the RB and SPS templates (§5.4) always run, whatever their price. Any other decoder costs at most ℓ_dec := max(½·F_X, c_dec), where F_X = log₂|𝒜_X(ι)|.
  - Decoders may be exhibited by the Intake auditor, the Evaluator or the Comparator panel during the hostile window, which runs from intake to S9 completion.
  - Fires → X RELOCATED in that input.
  - Passing is graded **NOT FOUND within the hostile window**, never "proved unencoded".
- **NR-7 Scramble.** Replace each priced input component by an independent draw of its type from the charter reference measure at the declared truncation (uniform on finite function spaces). If X is recovered within tolerance from the scrambled component's value on at least p_dec of the draws (X tracks the component), that component carries X: RELOCATED.
- **NR-8 Representation.**
  - Apply RM1–RM5 and the declared moves, with post-batch seeds.
  - A non-covariant X is INVALID: it is not generated.
  - An X moved by a declared gauge move is RELOCATED in the representation.
- **NR-9 Prior ablation.**
  - (a) Remove the law and keep μ: if X appears, it is RELOCATED in the prior.
  - (b) Replace μ by the charter reference measure and keep the law: if X disappears, it is RELOCATED in the prior.
- **NR-10 Carrier, readout and interface.** All of the following must hold:
  - (a) no clause of 𝒦, Emb or Obs is indexed by protocol identity, apart from the protocol's action on S;
  - (b) the common-carrier form is proved for every A ∈ 𝔄 and every protocol in A_{r★★};
  - (c) Z_Π is derived from 𝒦 under PC-6, with the NR-3 carrier W-pipe in Dom_pre^carrier;
  - (d) for every family read as reciprocity, 𝒦 excludes, or classifies as a non-solution, both the exact product-latent representation (D5 Theorem D1) and its causal prefix-tree version (D2);
  - (e) **E2 test:** on any instance that can express the two-mode configuration, the carrier derivation returns FAIL. The configuration is: a symmetric mode read by a₀; the symmetric mode plus a skewed mode read by the driven protocol; an environment law that does not depend on the protocol;
  - (f) no input names a record-space group action or a readout class; T_Π ≠ Aut(R) for any record structure R that the inputs supply; the harness verifies T_Π's generators on the chart;
  - (g) T_Π and [h] are computed without R1 calibration data;
  - (h) [h] is invariant under every 𝒦-preserving representation move, verified against a declared generating set;
  - (i) the card names the 𝒦-internal property that excludes the D1/D3 E-B representation for this Ξ. That property must survive NR-6: it may not be L₀-equivalent, within c_dec bits, to "the readout is a function of the instantaneous state";
  - (j) each item of the Appendix-G checklist that the carrier claim uses is either derived from 𝒦 or marked SUPPLIED (→ CARD-NONGENERATIVE);
  - (k) T_Π is SUPPLIED if it equals, or is L₀-definable within c_dec bits from, a symmetry group, an invariance requirement or a calibration map stated in 𝒦 or its inputs. Calibration maps exist only as an apparatus layer outside T_Π, and ℛ★ may not depend on them;
  - (l) wherever the auditor can express the E-B twin (§15.6) in the declared type, X_h and X_T applied to the twin return carrier FAIL or MODE SELECTION.
- **NR-11 Mode selection.**
  - (a) Readouts h_a ∉ [h]_{T_Π} give the verdict MODE SELECTION for every ε-relation, and the lock is void. Harness control: HB-9 must return MODE SELECTION.
  - (b) **Boundary ablation.** Every credited quantity is recomputed with the records of the relata in ∪_a(Π_a Δ Π_ref) ∪ ∂ removed. Each must stay within r_lock. Otherwise the verdict is MODE SELECTION.
- **NR-12 Gibbs/FDT premises.**
  - (a) PS-5 items are absent from the inputs, or declared and priced.
  - (b) Every premise of each credited derivation is listed. If any premise is a PS-5 structure (an invariant, Gibbs or KMS measure; detailed balance; an FDT kernel; a fluctuation-theorem premise; Onsager symmetry), **whether it is supplied, hidden or generated by 𝒦**, then every claim whose derivation passes through it is STANDARD-IMPLIED and earns 0. Generation changes only the label of the premise itself (SUPPLIED → RECOVERY), never the status of its consequences. A hidden premise → RELOCATED.
  - (c) **PS-5 substitution test.** Replace Sol by standard models with the same PS-5 premise and the same H(x) (B-HB, or card-supplied and verified). If ℛ★ holds on all of them → STANDARD-IMPLIED.
  - (d) On an instance whose reference state is not KMS: if ℛ's credited content vanishes there, it lived in FDT and earns 0.
  - (e) KMS, detailed-balance or FDT forms relative to a flow constructed from the state itself are DEF-16.
- **NR-13 Neutrality.** No objective, penalty or selection criterion is monotone in ℛ, and no sign is presumed.
- **NR-14 Exclusion audit.** Checks for the STATE exclusions, for IP-9 branches and for R1 calibration data.
- **NR-15 No promissory structure.**
  - Every structure claimed as generated is computed by the card's frozen algorithms at r★ and r★★.
  - Any premise not proved at card freeze counts as SUPPLIED.
  - "To be derived later" means SUPPLIED, and no follow-up may supply it (§20).
- **NR-16 Battery independence.** A preregistered one-sided binomial test at α (Appendix A) compares the holdout failure rate with the public failure rate. Rejection → BATTERY-TUNED, reported as RELOCATED.
- **NR-17 Joint necessity (JN).**
  - Consider any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂, offered by the author or by a reviewer.
  - If 𝒦₂ alone implies ℛ, with Π, T_Π and Γ_Π treated as free variables, and Price(𝒦₂) ≤ Price(ℛ) + c_dec, then ℛ is **imposed, not forced**: RELOCATED on the target relation.
  - Novelty at the assembled-law level does not override this.

### 5.4 Decoder templates
**RB, the reader battery.** A reader's cost is its template index plus its parameters, in L₀ bits.
- RB1: read any input label or sort.
- RB2: a threshold or top-n read of any input weight.
- RB3: connected components of any input relation or its complement, k-cores, or degree thresholds.
- RB4: blocks of the finest module decomposition of any input matrix or relation.
- RB5: unions of orbits of Aut(inputs).
- RB6: balls of any radius around an input-designated element, in any input distance.

**SPS, the Standard Partition Selector panel:**
- min-cut, max-cut, spectral bisection and modularity, on any graph or weight structure in 𝒞 or in the realized dynamics;
- conserved-charge and symmetry-sector partitions;
- explicit labelling;
- slow/fast splits by timescale;
- heterogeneity thresholds;
- support co-occurrence;
- for [h]: "most-coupled-variable" readouts and declared observable lists.

### 5.5 Generation grades
- **Π GENERATED-STRONG:**
  - NR-5 passes on a transitive instance on which every solution has a persistent, nontrivial Π;
  - at least one lock fiber is drawn from such instances;
  - every other NR test is clean.
- **Π GENERATED-WEAK:** NR-5 passes (or 𝒞's asymmetry is priced), no decoder is found, and every other test is clean.
- **Carrier, [h] and T_Π GENERATED** if and only if NR-3, NR-4 and NR-10(a)–(l) are clean and T_Π ∈ 𝕃_T^adm.
- Every grade reads "no decoder found within the hostile window" (NR-6).

### 5.6 Labels and consequences
**"Supplied"** means present in 𝒞, 𝒳, the components, the priors or Emb, or in a clause that NR-2 flags as target-level. A law that merely implies ℛ★ is what Q1 requires; it does not count as "supplying" ℛ★.

| Finding | Consequence |
|---|---|
| Any protected structure RELOCATED (hidden) | **CARD-RELOCATED**. After external check, a GRAVEYARD line reads "RELOCATED in ⟨input⟩" |
| Π, the carrier, [h] or T_Π SUPPLIED, even when declared | **CARD-NONGENERATIVE** |
| Gibbs/FDT SUPPLIED and declared | COMMITMENT, priced under IP-7. Every dependent claim earns 0. If the derivation of ℛ★ uses it → **CARD-RELOCATED** |
| ℛ★, or content implying ℛ★, supplied (as defined above); or ℛ★ fails JN | **CARD-RELOCATED** |
| A STATE-excluded input, or R1 calibration data | **CARD-RELOCATED** |
| STANDARD-IMPLIED (a single claim) | That claim is not credited |
| INVALID (non-covariant) | **CARD-NONGENERATIVE** |
| An illicit upstream read (PC-6) | **CARD-DEFINITIONAL** for every relation coupled through it |

---

## 6. Owner item 5: budget and genuine distinctness

- **BU-1** At most **three frozen cards** for the whole generative route, Stages 3–6 included.
- **BU-2** A slot is consumed at commit, i.e. when the card has a freeze SHA, whatever happens to it afterwards. Withdrawn, INCOMPLETE, VARIANT and intake-rejected cards all consume slots (OD-3).
- **BU-3 Modification.**
  - Any change after freeze creates a new card. This covers the statement, constants, type, components, truncation, tolerances, scope, response scope, kill conditions, ℛ★, battery predictions, domain predicate, lock design, and the transfer plan (the sector pair, the transfer observable, the split of θ into θ_K, θ_dict, θ_std and θ_cal, and the SI witnesses).
  - A modification made after any score was visible is labelled REPAIR.
  - The only exception is a tooling repair (§19.2).
- **BU-4 Genuinely distinct.** K_j is distinct from every earlier K_i only if all of the following hold:
  - (a) their normal forms differ by more than numeric literals, thresholds, renaming or equivalent rewriting;
  - (b) a certified point lies in the symmetric difference of their realized sets, on an AI-1, AI-2 or AI-4 instance or a lock fiber, or their SEL verdict vectors differ;
  - (c) a certified point lies in Z(ℛ★_i) Δ Z(ℛ★_j) within FB;
  - (d) K_j is no variant of K_i, under any of:
    - **VAR-1** a translation of price ≤ ℓ_tr, built from RM moves, renaming and reparametrization of constants, maps Sol(K_i) onto Sol(K_j) on the battery universe (the battery, AI-1 to AI-3, and the lock fibers). The card bears the burden of proving distinctness. The auditor's search is capped at R_item;
    - **VAR-2** the same normalized skeleton with different constants;
    - **VAR-3 patch**, any one of:
      - one clause added or deleted;
      - one conjunct or disjunct added to or removed from one clause;
      - one clause changed by a VAR-1 or VAR-2 move;
      - K_j = K_i ∧ Q, where Q changes battery verdicts only on items where K_i failed;
      - clause changes worth ≤ b_patch bits in total;
    - **VAR-4** a changed scope, battery exclusion, extractor, tolerance, truncation or response scope;
    - **VAR-5** a conjunction or disjunction of earlier cards or of their clause sets;
    - **VAR-6** a composition of VAR-1 to VAR-5 whose total edit is at most max(3·b_patch, 25% of K_i's clauses), or that preserves the clauses carrying ℛ★ and Π;
  - (e) **mechanism distinctness:** the clause sets that carry ℛ★ and Π in the NR-4 responsibility maps are not equivalent under VAR-1 or VAR-2.

  Failure → **CARD-VARIANT**, and the slot is consumed. The author names the nearest earlier card and argues distinctness (C1). The Intake auditor rules. Disputes go to the owner; until the owner rules, the card counts as a VARIANT.
- **BU-5 Draft ledger.**
  - Every draft, and every evaluated instance (IP-12), is logged with a hash and a time.
  - A draft found unlogged later → the card is repriced with the corrected n_drafts and flagged.
  - Deliberate non-disclosure → KU-10.
- **BU-6 Batch freeze** (§19.4).
  - No card is scored on any battery, holdout or lock until the batch closes.
  - The batch closes when every card is frozen, when the owner declares the final count, or automatically D_batch [P] days after harness validation, whichever comes first.
  - Declaring the final count, or the clock expiring, forfeits the unused slots.
- **BU-7 Owner's pick.**
  - Only among CARD-ADMISSIBLE cards. The pick costs log₂ N_frozen bits.
  - If the picked card fails Stage 4 or 5, the owner may take another frozen ADMISSIBLE card, unmodified.
  - **There is no fourth card.**
- **BU-7′ No lock reuse.**
  - An unsealed lock dataset never serves another card.
  - Cards with a shared lock observable on a shared platform class are a VARIANT pair.
  - Confirmation thresholds are Bonferroni-adjusted across every card locked in the route.
- **BU-8 No budget laundering.** Any artifact that states a law in L₀ for evaluation is a card. "Proto-laws", "lemma cards" and "pre-cards" are prohibited (SM-4).
- **BU-9 Sub-law switches.** A card containing a switch among m sub-laws that is not fixed by a priced, input-decidable condition (IP-9) consumes m slots. If that exceeds the budget, the card is CARD-VARIANT.

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
| KU-4 | Contradiction of an experimentally established standard relation inside its tested domain (FDT/KMS in equilibrium, Onsager–Casimir near equilibrium, energy–momentum conservation, the second law), or of a standard consequence of a regime whose hypotheses the card's own construction meets. For every relation that its non-standard realizations approach, the card cites the tested domain at freeze; the auditor may add domains; when in doubt, a case counts as inside. The only exception is a contradiction that is the declared ℛ★ and is consistent with existing bounds cited at freeze |
| KU-5 | A mandatory ALLOW anchor is forbidden (§15.8) |
| KU-6 | B-REC is contradicted while those environments are claimed as realizable |
| KU-7 | ℛ★ fails any of Q1–Q12 |
| KU-8 | Any protected structure is RELOCATED |
| KU-9 | A GRAVEYARD idea returns at card level (§21.2) |
| KU-10 | Undisclosed search, or modification after freeze. The card is void |
| KU-11 | ΔL₀ < p★ at p★, or ΔL₀ ≤ 0 at p = 16 |
| KU-12 | LOCK-FALSIFIED (LOCK-VOID included) on any observable of any registered relation; or a G5-HOLD holdout violates ℛ★ inside the declared scope |
| KU-13 | A card-specific kill condition fires |

### 7.3 Card-specific kill conditions
Each card states its own kill conditions. Together they must meet:
- **KP-1** Each is finite and decidable on the frozen battery, or is a named experimental outcome.
- **KP-2** Each is reachable: some 𝒮-admissible, realizable outcome triggers it. A vacuous kill condition makes the card CARD-INCOMPLETE.
- **KP-2′ Risk.** Each is decided on post-batch seeds, on sealed holdouts, or by the C13 lock. Kill conditions decided on public items are consistency checks and do not count toward KP-4.
- **KP-3** Each is automatic; there is no reinterpretation after the fact.
- **KP-4 Coverage:**
  - at least one observable kill condition on ℛ★, with a threshold;
  - at least one structural kill condition decidable at Stage 4 using only the frozen harness and the card's reference implementation;
  - at least one on B-SEL or B-DIF.

**No rescue.** Once a kill fires, the card is not repaired.

---

## 8. Owner item 7: originality

- **OR-1** Familiar component theories are allowed and expected. Familiarity is neither a defect nor a credit.
- **OR-2** Novelty is judged **only for the assembled law**: 𝒦 with its generated chain, its qualifying relations and its realized joint set. It is judged only for a card whose ℛ★ survives JN (NR-17).
- **OR-3 Conjunction test** (a mandatory comparator). The conjunction C₁ ∧ … ∧ C_m, with each component stated in its standard form, is taken together with 𝒮. If ℛ follows from it without the card's coupling clauses (located by NR-4), ℛ is not novel.
- **OR-4 Comparator floor.** The auditor may add comparators, and none may be removed. Each is verified against primary sources at audit time.
  - **SFP-1** Linear and nonlinear response: Kubo; higher-order FDRs (Stratonovich–Efremov; Bochkov–Kuzovlev); Kramers–Kronig; sum rules.
  - **SFP-2** Equilibrium and nonequilibrium statistical mechanics:
    - KMS and FDT;
    - fluctuation theorems (Jarzynski, Crooks, Bochkov–Kuzovlev, Evans–Searles, Gallavotti–Cohen);
    - NESS response (Agarwal; Harada–Sasa; Baiesi–Maes–Wynants; Seifert–Speck; Prost–Joanny–Parrondo);
    - effective-temperature FDRs (Cugliandolo–Kurchan–Peliti);
    - frenetic higher-order response (Basu–Krüger–Lazarescu–Maes; Lippiello et al.);
    - TURs; stochastic thermodynamics;
    - typicality, ETH and GGE.
  - **SFP-3** Reciprocity: Onsager–Casimir; dynamical reciprocity; nonlinear reciprocity (Andrieux–Gaspard); Lorentz, Rayleigh–Carson, Betti–Maxwell and Helmholtz reciprocity; S-matrix symmetry.
  - **SFP-4** Projection and GLE: Mori–Zwanzig; Ford–Kac–Mazur; Caldeira–Leggett; Feynman–Vernon.
  - **SFP-5** Open systems and measurement:
    - GKSL; Davies; Redfield; process tensors; input–output theory; quantum regression;
    - imprecision–back-action and the SQL;
    - full counting statistics (Levitov–Lesovik) and cascade/environmental-feedback corrections (Nagaev; Beenakker–Kindermann–Nazarov);
    - einselection, quantum Darwinism, and Brandão–Piani–Horodecki objectivity;
    - information–disturbance relations.
  - **SFP-6** Dissipative field theory: Schwinger–Keldysh EFT with dynamical KMS symmetry; MSR / Janssen–De Dominicis; GENERIC.
  - **SFP-7** Mechanisms for differentiation and subsystems:
    - SSB, Landau theory, Goldstone, Mermin–Wagner–Hohenberg, Halperin–Hohenberg hydrodynamics;
    - critical phenomena and renormalization;
    - Turing patterns; Cahn–Hilliard;
    - timescale separation and slow manifolds; near-decomposability (Simon–Ando); lumpability (Kemeny–Snell);
    - observable-induced tensor-product structures (Zanardi; Zanardi–Lidar–Lloyd); quantum mereology (Carroll–Singh);
    - Markov blankets (Pearl; Friston); coarse-graining and causal emergence;
    - conserved-charge sectors; graph decompositions; planted-partition and community-detection baselines;
    - Lieb–Robinson bounds.
  - **SFP-8** The ten D5 comparators, applied to ℛ and not to ε_R.
  - **SFP-9** Readout classes: measurement invariance; Stevens scale types; IRT linking and equating; interventional-CRL identifiability classes (R1 §12 item 1).
  - **SFP-10** The correlation sector:
    - Abramsky–Brandenburger and AvN; KS sets; Local Orthogonality;
    - reconstructions (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller); JGBB polygons and boxworld;
    - bounded-width CSP and operator assignment (Atserias–Kolaitis–Severini; Bulatov–Živný; Ciardo; Ó Conghaile); Slofstra.
  - **SFP-11** Constructor theory (GY-1).
- **OR-5 Categories** (preregistered; mathematics (M) and physical relation (P) are classified separately; none is favoured in advance):

| Category | Meaning |
|---|---|
| RESTATED | Up to representation, the image of Sol equals an existing framework's image, and there is no new relation |
| KNOWN ASSEMBLY | The combination already exists in the literature |
| STANDARD COMPONENTS, NEW ASSEMBLY, NO NEW RELATION | Every credited relation follows from the conjunction test or from a comparator |
| DISTINCTIVE | ℛ★ passes Q1–Q12, survives JN, and neither any comparator nor the conjunction imposes it |

  - **Only DISTINCTIVE (P) for ℛ★ makes a card ADMISSIBLE**, and it is re-confirmed at G5-LOCK.
  - A middle category may be banked as a COMPRESSIVE known or assembled sector only if S6 still passes when recomputed with NULL-M and c_J. It is never banked as a law.
- **OR-6 Procedure.**
  - Each comparator family gets an analyst and a skeptic, and the skeptic is instructed to argue RESTATED. The more conservative verdict governs.
  - **The audit must be complete, with every floor comparator returned, before the owner's pick and within T_audit [P] of batch close.** Otherwise the card is CARD-RESTATED.
- **OR-7 Timing.**
  - The cheap screens run inside S5: the Q3 witnesses and transplant, B-SRB, the reverse-direction relations, and B-CF*.
  - The full audit is S9.
  - No novelty claim is made before then (RULES 7).

---

## 9. Owner item 8: cross-sector gold standard (parameter transfer)

- **XS-1 Sector.** A sector is σ = (platform class, regime hypotheses H_σ, standard description F_σ ∈ SFP, observable set O_σ, dataset D_σ).
  - **Sector data are empirical measurements on physical systems.** Battery items, classifications and theorems are card design, priced under §4, and are never θ̂_A.
  - The frozen coordinate blocks are: Q (correlation and contextuality); Θ (response and reciprocity); 𝔊 (gravitational, Stage 6); and any further block the owner declares.
- **XS-2 Independence.** Sectors A and B are independent only if FB after §13 admits their joint values as a product, and all five of the following hold:
  - **SI-1 Data.** The datasets are disjoint and frozen by hash. Every A quantity is hashed and committed before any B datum is read. No B datum fixes anything in A.
  - **SI-2 Physics.** No degree of freedom, sample or apparatus is shared, apart from generic calibration standards. F_A and F_B share no parameter that standard physics would fit jointly.
  - **SI-3 No standard bridge.** The Standard Bridge Panel, applied to A's data together with B's standard parameters, must give an interval for the B target at least Q_min × wider than the transfer prediction. The panel:
    - FDT/KMS; Onsager;
    - Kramers–Kronig and sum rules;
    - dimensional analysis with universality and scaling;
    - symmetry and Ward identities; conservation; ensemble equivalence;
    - Mori–Zwanzig; EFT matching; CLT and large-N;
    - every item of the §13 floor.
  - **SI-4 Not a replication.** B is not A at another value of a control parameter within the same H and the same F_σ.
  - **SI-5 Zero-transfer certificate.** Two standard models agree on every A observable but differ on the B target, and standard model pairs realize every combination in a product box of positive dimension.
- **XS-3 North-Star lock.** A and B must lie in different regimes, decided operationally:
  - *quantum* means the target observable changes by at least 3σ between F_σ and its classical limit;
  - *thermodynamic* means an RH-TH observable whose large-N limit is essential;
  - *gravitational* means F_σ contains gravitational coupling.

  F_A and F_B are different SFP entries.
- **XS-4 Parameter ledger.**
  - θ_K: constants of the law, **frozen at card freeze**.
  - θ_dict: dictionary constants. Their count and ranges are declared in C20.
  - θ_std,σ: standard parameters of sector σ, measured without using the target observable.
  - θ_cal: calibration of the ε machinery.
  - The GRUT-specific parameters are θ_K, θ_dict and every discrete choice.
- **XS-5 Protocol.**
  1. Fit only θ_dict, on D_A alone, by a frozen procedure. Each fitted parameter is priced (IP-11) and subtracted from TG. Freeze the result by hash.
  2. Measure θ_std,B independently, and freeze it by hash before B's target data are unsealed.
  3. Preregister a numeric prediction y_B = f_B(θ̂_A), with its band, before B's data are opened.
  4. Refit nothing.
- **XS-6 Prohibited (a GRUT-specific fit in B):**
  - adjusting θ_K or θ_dict on any B data;
  - introducing any new constant;
  - any fitted quantity of any origin beyond apparatus constants measured independently and declared beforehand;
  - any discrete choice made after B's data are accessible: T tier; which Π (unless 𝒦 selects it); carrier, [h] or representative; scope; protocol subset; grid or window; coarse-graining; units; estimator or exclusions;
  - a nuisance fit that absorbs the prediction.
- **XS-7 Gold standard.** Let F_p(X) := log₂ of the number of 2^(−p) frozen-chart cells that meet X.
  - **d_B = 0:** no GRUT-specific degree of freedom is adjusted in B. n_B ≥ 1 B target observables are predicted.
  - Transfer gain: **TG** := F_p(𝒜_B^base) − F_p(Im_{𝒦,B}(θ̂_A)) ≥ p★.
  - Gain from A: **TG_A** := F_p(Im_{𝒦,B}(priors)) − F_p(Im_{𝒦,B}(θ̂_A)) ≥ p★. At least one parameter must be fixed on D_A that, by the responsibility map, sets the B prediction.
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
  - Stage 3 claims none. Cards only declare a transfer plan, which is frozen under BU-3.
- **XS-10 Stage-6 export.**
  - The same 𝒦, unmodified.
  - ε_R is exported with the same quotient and the same distance used at the lock.
  - If 𝒦 generates T_Π per sector, the exported class must be the same up to isomorphism in every sector, or the export uses the class frozen in C20. Otherwise the export fails.
  - Local back-reaction sets θ_cal only, unless it qualifies as sector-A data under SI-1 to SI-5.

---

## 10. Owner item 9: stopping rule and terminals

- **T-1 Card terminals.** Each frozen card gets exactly one terminal.
  - S0 to S8 are always run and reported. S9 runs on cards that clear S0 to S8.
  - The first failing screen (§18.2) names the terminal. Otherwise the card is **CARD-ADMISSIBLE**.
  - UNSCORABLE and UNRESOLVED count as failures and are final within the route (DC-7).
  - **The GRAVEYARD line lists every failed screen from S0 to S8.** Every listed failure counts as a killed idea for the GY return test, in this route and in any later one.
- **T-2 Route terminals.** The list is exhaustive; there is no OPEN terminal.
  - **STAGE3-PICK:** the owner picks an ADMISSIBLE card, and Stage 4 follows.
  - **STAGE3-ROUTE-TERMINATED.**
  - **STAGE3-OWNER-HALT.**
- **T-3 Termination.** The route terminates when any of these holds:
  - (a) the budget is spent, the batch has closed (BU-6), or the final count is declared, with no ADMISSIBLE card;
  - (b) every frozen ADMISSIBLE card has failed a Stage-4 or Stage-5 gate. LOCK-INCONCLUSIVE counts as a failure. A void caused by the author side is a failure; a void caused by the auditor side allows one disclosed reselection;
  - (c) Stage 6 would require modifying 𝒦.

  Termination is recorded in GRAVEYARD after the external check (RULES 8), and in STATE. The stage stops (RULES 4).
- **T-4 Prohibited.** See §20.
- **T-5 Allowed after termination:**
  - banking DERIVED sub-results as a library, after external check. Excluded from the library: interface classes, distances, s_T, carrier constructions, and any result whose stated use is a law ingredient;
  - banking a COMPRESSIVE known or assembled sector (OR-5);
  - GRAVEYARD lines and the terminal report;
  - continuing R1's non-blocking upgrades;
  - a new program, but only by a new explicit owner ruling that names it as a new route, with its own charter and no inherited budget. A new route inherits this route's GRAVEYARD and FR standings, and cannot cite library items as discharging any FR.

---

## 11. Addition A1: merge = provenance, not endorsement

- **PV-1** The merge `86bf5a0` and the boundary `dbfd64b` are provenance markers. They change no status. Merging this charter, a card or a result changes no status either.
- **PV-2 Pending items keep their status, and their CHECKS lines stay pending:** A-BL, F, M1–M3, Prop. G, and the D5 analyses (C1–C6, D1–D3).
- **PV-3 No conditional verdicts.**
  - Every credited claim or gate verdict that depends on a pending or evidence-grade item is scored **now, under the hostile reading** of that item: the item is treated as false or absent wherever that hurts the card.
  - Q1 needs DERIVED grade without the item.
  - A verdict never proceeds "conditionally". If an external check later finds an issue, the affected scores are recomputed under unchanged thresholds, and they may move only toward failure.
- **PV-4 Banking.** Nothing is banked until its CHECKS line shows an external check with no open issue (RULES 8). This includes the charter's freeze commit.
- **PV-5 Items used by this charter:**

| Item | Role here | Status |
|---|---|---|
| ε_R definition, T_R1, d_op, verdict table, common-carrier commitment, Prop. E/E1/E2, G2-08 certificate (`82d311e`) | ε code, carrier semantics, NR-11 | Frozen pre-result; checked: Claude |
| Theorems A and C | DEF-2, B-REC, HB-2 calibration | DERIVED; checked |
| A-BL, F, M1–M3, Prop. G | DEF-2, DEF-5, witness enclosures, Tier-2 zero set, B-REC rate | DERIVED; external check pending (hostile reading, PV-3) |
| BRI1 Tier 2 (`cb81a3b`) | B-REC | DERIVED, evidence grade; checked: Claude |
| D5 C1–C6, D1–D3, regime restatement, reverse-direction relations, M-A/M-A′/M-B, C2-F′ | Baseline, B-REC, DEF-9, DEF-10 | D5 ANALYSIS; evidence grade; not externally checked |
| 10-item checklist (Appendix G), instantaneous-state form, Z_A, [h]_T, MI framing | MC-6 (adopted as a Stage-3 rule); not-credited seeds | POST-RESULT SEED |
| SD0 counts 2961/1721/1232/8, the 240 gap, 2721, the PR-forcing lemma | B-SEL, harness validation | DERIVED, exact |
| SD0 T1 | FC-2 structural discount | SD0 record |
| SD0 T2 (2-SAT equivalence) | B-CF* behaviour; FC-2 discount once resolved | UNRESOLVED, pending review |
| ASP (`aacbc52`) | B-CF* member | COMPRESSIVE, known sector (#6) |

- **PV-6 Scoreboard mapping** (each after external check):

| Outcome | Status |
|---|---|
| Card frozen and ADMISSIBLE | COMMITMENT |
| 𝒦 ⇒ ℛ★ proved | DERIVED |
| SC2 met | COMPRESSIVE |
| LOCK-CONFIRMED on sealed real data | PREDICTIVE |
| §9 passed | CROSS-SECTOR |
| An NR violation, or LOOKUP | RELOCATED |
| B-SRB, a comparator or the audit restates it | RESTATED |
| A kill | GRAVEYARD entry |

---

## 12. Addition A2: ε_R is derived

- ε_R = ε[Γ_Π, T_Π] by definition. It is computed only by charter code, from the card's Γ_Π and T_Π (and s_T where needed).
- 𝒜_ε is the image of 𝒜_Γ × 𝒜_T. It is never an independent axis, and no bits are ever counted on it.
- A qualifying relation restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition (Q2), and it couples interface with response (Q5).
- The claim "ε_R > 0 somewhere" is not credited.

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
- **DEF-9** Triviality and representation statements: Prop. E and E1; D5 Theorems D1 and D2; ε^{T_univ} ≡ 0; the ladder's time-marginalization facts.
- **DEF-10** D5's four-cell independence of (Markov or not) × (ε zero or positive), and its one-way links.
- **DEF-11 Tautology test.** Any statement true for every well-typed tuple of 𝒟(ι).
- **DEF-12 Pipeline tautology.** ℛ holds on the pipeline image of every Ξ ∈ Dom_pre^chain, or follows from the components together with the type and 𝒮 (PC-7).
- **DEF-13 Restriction and marginal bounds.**
  - A′ ⊆ A ⇒ ε_{A′} ≤ ε_A, and the time-marginalization facts.
  - Every prediction of a full-repertoire or full-grid quantity that goes through these bounds, from sub-repertoire, sub-grid, channel-marginal or overlapping-sub-repertoire records of the same protocols.
- **DEF-14 ε-class coupling.** Any coupling between T and Γ carried by the T-argument of ε, i.e. the class at which ε is evaluated varies across the compared points. This includes cross-tier comparisons implied by DEF-4. Hence jointness is tested within fixed-T fibers (§2.5).
- **DEF-15 Definitional given C.**
  - Suppose a single-axis property C (Γ-only, or (Π, [h], T)-only) holds on Im(ι), and C ⇒ ℛ is a theorem of ε's definition, of R1's theorems or of mathematics. Then ℛ is DEFINITIONAL-GIVEN-C: only C remains, and C is not joint.
  - Examples: nonsingular Gaussian families are T_caus- and T_lin-separable in every regime; tier coincidences at record dimension 1; Theorem F under any symmetric P0.
- **DEF-16 Self-referential flows.**
  - KMS, detailed-balance or FDT forms relative to a flow constructed from the state itself (modular or thermal-time constructions; a time unit calibrated on the reference law).
  - KMS-type credit, or RECOVERY, needs a time evolution certified independently, with the FR7 order fixed before the state is considered.
- **DEF-17 The card's own definitions.**
  - (a) The stationarity, fixed-point or extremality conditions of any rule the card uses to define Π, [h], T_Π or the carrier, and all their consequences.
  - (b) Consequences of the card's own definitions of persistence or identity measures.
  - (c) A relation between two functionals of Γ_Π qualifies only if FB admits its violation.

---

## 13. Addition A3: baseline after standard theory

### 13.1 The rule
The standard constraint set 𝒮 is imposed before any freedom is counted. Relations implied by 𝒮 earn nothing.

### 13.2 Regime hypotheses
This table is a floor. Each hypothesis is decided operationally by its Appendix-F surrogate and threshold.

| RH | Holds when |
|---|---|
| RH-HAM | S+E evolve under a closed generator at record resolution |
| RH-KMS | The reference state of E (or of S+E) is KMS or Gibbs for the realized evolution |
| RH-MR | The dynamics is microreversible, with parities and field reversal |
| RH-DB | The realized generator (Hamiltonian, stochastic or GKSL) satisfies classical or quantum detailed balance with respect to its reference state, including detailed balance implied by Kolmogorov's criterion (e.g. on acyclic state graphs) |
| RH-LDB | Local detailed balance |
| RH-MK | The records or the reduced dynamics are Markov at record resolution |
| RH-STAT | The reference process is stationary |
| RH-GAU | E is Gaussian or harmonic, with coupling linear in E's variables |
| RH-SYM(G) | The reference law and the dynamics are invariant under a group G |
| RH-CQ | The dynamics has conserved quantities |
| RH-GGE | Extra conserved charges, with a generalized Gibbs reference |
| RH-WC | Weak coupling or timescale separation |
| RH-LIN | The readout is a linear detector of a weakly coupled E observable |
| RH-MF | E is N weakly coupled units with a normalized collective readout |
| RH-LOC | The generator has finite range, or E is a local or mixing system of n units read by a normalized aggregate |
| RH-ERG | Mixing: finite correlation length or time |
| RH-AN | Record laws depend analytically on the drive amplitude (fading memory). This includes the perturbative radius within which an order-m Volterra truncation matches the records to 2^(−p★) |
| RH-NESS | The dynamics is stationary nonequilibrium Markov |
| RH-NEQ | Small affinities (near equilibrium) |
| RH-MC | Finite bath, microcanonical |
| RH-ORD | An ordered phase, a critical point or a pattern-forming instability is present |
| RH-TH | Macroscopic thermodynamic regime |
| RH-Q | Quantum structure is present (supplied or generated) |

### 13.3 Standard constraints STD-1 to STD-15
For each constraint: the hypotheses under which it applies, what it imposes, and what therefore earns no credit.

- **STD-1 Causality.** Applies always.
  - Non-anticipation: protocols that agree on [0, t] give the same record laws on τ ∩ [0, t].
  - Response functions are retarded; Kramers–Kronig and sum rules hold.
  - No-signalling holds, i.e. pNS for multi-block supports; relativistic causality holds in spatial embeddings.
  - T_caus ⊂ T_lin.
- **STD-2 Positivity.** Applies always.
  - Probability laws are valid; covariances and spectral densities are positive semidefinite (Bochner).
  - Processes are CP (positive combs; GKSL form for Markov semigroups).
  - Interface maps preserve validity.
  - Under RH-Q, every theorem of quantum theory and quantum information enters 𝒮: uncertainty relations, Tsirelson-type bounds, information–disturbance relations, no-cloning, and the rest. Supplied quantum structure is also priced, or RELOCATED, under IP-6.
- **STD-3 KMS / FDT / fluctuation relations.** The equilibrium forms apply under RH-KMS together with any one of RH-HAM, RH-DB or RH-MK. The NESS forms apply under any stationary Markov reference, equilibrium included.
  - KMS holds for every multi-time correlator.
  - Linear FDT: classically χ_AB(t) = −β·θ(t)·(d/dt)⟨A(t)B(0)⟩; in the quantum case through the KMS factor.
  - The n-th order response equals the reference-state correlator of A with n nested commutators (quantum) or Poisson brackets (classical) of B. KMS converts the first order fully and higher orders only partially (Stratonovich–Efremov; Bochkov–Kuzovlev; quantum nonlinear FDRs). Path-space forms have entropic plus frenetic terms.
  - The fluctuation theorems hold for every protocol.
  - A Gaussian E is fixed entirely by (J(ω), β), including its exact exogenous decomposition (Feynman–Vernon, Caldeira–Leggett, Ford–Kac–Mazur).
  - NESS forms: Agarwal; Seifert–Speck; Harada–Sasa; Baiesi–Maes–Wynants; Prost–Joanny–Parrondo.
  - Effective-temperature FDRs and FDT-violation ratios (Cugliandolo–Kurchan–Peliti); frenetic higher-order response (Basu–Krüger–Lazarescu–Maes; Lippiello et al.). Under RH-GGE: generalized FDT.
  - Under RH-KMS, RH-GAU and linear coupling, 𝒜_ε = {0}.
  - Under the BRI1 class, the leading Tier-1 value is fixed by the reference 4-point function: ε_R = (V*/12)·|γ₁|·(1 + 0.235/N_B + …), with sharpness at D5 evidence grade.
  - **No credit for:**
    - any ε value or Γ restriction fixed by reference correlators among the BP-5 inputs;
    - any fluctuation-theorem identity;
    - "harmonic baths are R1-NULL";
    - any "response = X·correlation", with X a constant or a fitted or generated function, unless X is predicted from interface-side data and beats B-SRB by Q_min.
- **STD-4 Reciprocity.**
  - (a) Dynamical reciprocity, S_ij = ε_iε_j S_ji, under RH-MR or RH-DB at any temperature. Also Lorentz, Rayleigh–Carson, Betti–Maxwell and Helmholtz reciprocity, and S-matrix symmetry, for time-reversal-symmetric linear dynamics at any temperature.
  - (b) Onsager–Casimir, L_ij(B) = ε_iε_j L_ji(−B) and χ_AB(t; B) = ε_Aε_B χ_BA(t; −B), under (a) plus RH-KMS.
  - (c) Nonlinear forms (Andrieux–Gaspard), under the fluctuation-theorem hypotheses.
  - R1's operational "reciprocity" is a different thing. A relation that reduces to any of these earns nothing under either name.
- **STD-5 Conservation and symmetry.** Applies under RH-CQ and RH-SYM(G).
  - Continuity equations, f-sum and moment sum rules, Ward identities.
  - Energy and momentum balance, i.e. action–reaction.
  - Charge and superselection partitions are standard selectors.
  - Curie and selection rules: a symmetric reference read through a covariant interface has no odd statistics. This is Theorem C's mechanism.
  - **Selection rules relative to the unbroken subgroup Stab(Π) of a supplied or generated partition or ordered state** (Curie; Wigner–Eckart; Landau; Goldstone counting; Halperin–Hohenberg hydrodynamics).
- **STD-6 Mori–Zwanzig / GLE.** Applies always: to any linear generator and any projection, supplied or generated.
  - There is an exact GLE: a memory kernel plus projected noise.
  - RH-KMS gives the second FDT. RH-WC gives the Markov limit.
  - A harmonic E gives exogenous noise plus linear memory exactly.
  - **No credit for:** memory, non-Markovianity, viscoelastic response, or "E carries S's history".
- **STD-7 Open-system and measurement response:**
  - GKSL (RH-MK); Davies (RH-WC with RH-KMS); Redfield; quantum regression (RH-MK);
  - process tensors (always available); influence functionals (RH-GAU);
  - input–output theory, b_out = b_in + √γ·a;
  - the imprecision–back-action bound S̄_xx·S̄_FF − |S̄_xF|² ≥ (ħ/2)², and the SQL (RH-LIN);
  - measurement rate ≤ dephasing rate;
  - full counting statistics and cascade/environmental-feedback corrections to higher cumulants, under RH-LIN or RH-WC at any temperature;
  - information–disturbance relations (RH-Q).
  - **No credit for:** any interface–response tradeoff of these kinds.
- **STD-8 Stability and the second law.** Applies under RH-TH or RH-KMS.
  - Entropy production ≥ 0; passivity; Clausius; Landauer (including Sagawa–Ueda); positive-definite static susceptibilities; Le Chatelier–Braun.
- **STD-9 Large-N, CLT and Edgeworth.** Applies whenever a recorded quantity is a sum or average over many weakly dependent contributions (RH-MF, RH-LOC, RH-ERG; Bolthausen; Edgeworth expansions for mixing sequences).
  - "N" includes any extensive size of a generated structure: |E_Π|, |∂|, numbers of blocks, numbers of correlation volumes.
  - Cumulants scale with N and with the fraction of units that respond (dilution); reservoir limits are Gaussian.
  - **No credit for:** scaling of ε_R or of its witnesses with N, with block sizes, or with boundary-to-bulk ratios of Π.
- **STD-10 Standard relations between differentiation and response.** Applies under RH-ORD.
  - Goldstone; Mermin–Wagner–Hohenberg.
  - Scaling relations (Rushbrooke, Widom, Fisher, Josephson); susceptibility versus correlation length; Landau mean-field relations.
  - Interface tension and stiffness; capillary-wave statistics; Turing wavelength selection; slow-manifold selection of persistent variables.
- **STD-11 Representation freedom.** Applies always.
  - Only T-invariants are observable.
  - Readout classes, maximal invariants, copulas modulo reflections and measurement invariance are known mathematics.
  - **No credit for** the existence or form of [h]_T as such.
- **STD-12 Universal exogenous representation.** Applies always; this is mathematics.
  - Every non-anticipating family has an exact exogenous representation with protocol-dependent readouts, even causal linear ones (Prop. E/E1; D1; D2).
  - **No credit for** any back-reaction claim made from records alone, or any relation that does not involve the derived carrier.
- **STD-13 Regression and rate–response.**
  - Onsager regression (RH-KMS);
  - golden-rule/Davies rates and susceptibilities that share J(ω) (RH-WC);
  - the second FDT (GLE); Harada–Sasa (NESS);
  - interface statistics plus FDT; Green–Kubo and Einstein relations;
  - Wiener–Khinchin (RH-STAT);
  - graph-theoretic (matrix-tree) response equalities for Markov jump networks;
  - Lieb–Robinson light cones (RH-LOC).
  - **No credit for:** relations between dynamical statistics of the interface (relaxation of ∂, exchange rates, decay of S–E correlation) and response-side content that these results fix.
- **STD-14 Amplitude analyticity.** Applies under RH-AN.
  - Record laws are analytic in the drive amplitude (fading memory; Boyd–Chua).
  - Standard: the leading amplitude power in each T-irreducible channel, and the ratios across a₊, a₋ and a₊₊ that this power and symmetry fix.
  - Standard: every relation among protocols that are scalings or sign-reversals of one template, if it is implied by an order-(|A|−1) Volterra truncation or by parity under RH-SYM.
- **STD-15 Power counting.** Applies under RH-WC or RH-AN.
  - Each witness scales with coupling and drive at the lowest nonvanishing order (cumulant expansion of the influence functional; Volterra).
  - Exponents and leading coefficients expressed through E's undriven cumulants and intrinsic response kernels are standard in any regime.

### 13.4 Closure
- 𝒮(x) is the set of relations implied, by any published theorem verified against primary sources, by **any** standard hypothesis true at x.
- The table in §13.2 is a floor. The auditor may add any published structural or regime hypothesis that comes with an operational test, and BP-3 and BP-4 apply to it. The fluctuation theorems are included (OD-7).
- Membership is **retroactive until banking**: a derivation cited at any time before banking removes the credit. Rescoring moves only toward failure.
- STANDARD status is decided constructively (Q3(e)). Non-standardness requires regime-matched, generic standard witnesses that violate ℛ; without them, ℛ is STANDARD.

### 13.5 Boundary and near-regime rules
- **Boundary rule.**
  - Suppose ℛ★ implies, on a lock fiber, equality in a published standard inequality: imprecision–back-action and the SQL; TUR or KUR; Clausius, Landauer or Sagawa–Ueda; Cramér–Rao; uncertainty relations; Tsirelson.
  - The baseline is then the saturating standard subclass under H(x). Every regime in which saturation is a published consequence is added to H.
  - If a saturating standard subclass realizes Im with matching inputs → STANDARD-IMPLIED. Otherwise the credit is only the codimension that ℛ★ cuts inside that subclass.
- **Near-regime rule** (BP-4).
  - A hypothesis that fails by δ in the frozen Appendix-F metric (relative entropy to the nearest KMS state; entropy-production rate; KMS defect at a fitted β) still imposes its consequences, with published perturbative bounds. J_SRB includes these.
  - Fitting a temperature-like parameter costs the baseline nothing.

### 13.6 Precedents and RECOVERY
- BRI1's Tier-1 ε_R value lies in 𝒮: it is a Kubo/FDT third-cumulant response fixed by P0's connected 4-point function (D5).
- So does any relation that expresses ε_R through the reference correlators of **any** environment with the same reference law, for any driven/recorded pair, at any order.
- Generating KMS or Gibbs states, thermalization or memory from dynamics is standard (typicality, ETH, Davies, ergodic theory). It earns RECOVERY, a Stage-6 consistency item with zero Stage-3 credit.
- A generated regime property puts the fiber in that regime, and the baseline imposes the corresponding STD items. Its consequences follow NR-12(b).

### 13.7 Regimes where FDT is silent
- There the baseline is larger. Credit is computed per regime class, after the near-regime rule.
- Regime shopping is defeated by BP-3, BP-4, §13.5 and the platform-matched lock fiber (§1.5).

### 13.8 D5 reverse-direction relations
These are baseline relations that comparators give and R1 does not:
- (i) for a Gibbs environment driven through any variable, FDT predicts the leading Tier-1 ε from undriven 4-point correlations;
- (ii) the GLE / linear-response route detects linear back-reaction;
- (iii) process-tensor signalling detects the harmonic bath's response.

ℛ★ must be none of these and must not be implied by them in its lock fibers.

---

## 14. Addition A4: response scope

At freeze, every relation declares exactly one scope, and the scope is frozen with the card.

- **SCOPE-Q: quotient-irreducible back-reaction.**
  - The relation constrains Γ only through T_Π-invariant content: ε_R, its zero set, its witnesses, or the maximal invariant. It is measured under R1's verdict table.
  - It is available **only if T_Π ⊇ E₂±** (translations and per-coordinate rescalings), and only if the harness verifies ε^{T_Π} = 0 exactly on HB-1, HB-3, HB-4 and on every Gaussian family under linear coupling.
  - ℛ is invariant when any T_Π-explainable response is added to Γ.
  - ℛ fails when the card's Π is replaced by some Π′ ∈ FB with Γ and T held fixed.
  - It is silent on mean response of every order, on linear back-reaction, and on affine or Gaussian latent change. Linear-response data can neither confirm nor refute it.
- **SCOPE-G: response in general.**
  - Its observables are response functionals: susceptibilities, response functions, noise spectra, transport coefficients. **It is never stated through ε_R alone.**
  - B-SRB applies at full strength, starting with STD-1, STD-3, STD-4, STD-6, STD-7 and STD-13, and with full linear-response theory (Kubo, Onsager–Casimir, Kramers–Kronig, the GLE/Zwanzig decomposition).
  - FB must admit a violation of ℛ when Π or T_Π varies while the linear part of Γ is held fixed.
  - D5's comparators 2 and 3, in the reverse direction, are mandatory baselines.
- **SCOPE-MIX.** Two relations, each declared and scored separately. This uses the card's two-relation maximum.

**Rules.**
- **RS-1 R1-NULL does not mean "no response."** A claim of the form "ε_R = 0 ⇒ no back-reaction", or "ε_R > 0 ⇒ the environment is nonlinear", is void. A relation whose derivation uses such a claim fails Q10. (The harmonic bath responds yet is R1-NULL; the parametric harmonic control escapes both tiers with linear bath dynamics.)
- **RS-2** No cross-subsidy between scopes.
- **RS-3 Battery emphasis.**
  - SCOPE-Q faces B-REC first, at the frozen tiers **and at T_Π**: it must predict ε = 0 wherever RH-GAU with linear coupling holds. Then B-HB.
  - SCOPE-G faces B-SRB first.
- **RS-4 Mismatches.**
  - A mismatch between scope and lock observable voids the lock.
  - A SCOPE-G relation stated only through ε_R is reclassified as SCOPE-Q, and its credit is limited to its quotient-irreducible part.
  - A SCOPE-Q relation that fails the T_Π ⊇ E₂± condition or the harness check is reclassified as SCOPE-G, with full B-SRB.
- **RS-5** No scope declared → CARD-INCOMPLETE. Any change of scope after freeze is a new card.
- **RS-6** The card states which carrier verdict it expects at measurement, and how that verdict will be certified. This feeds MC-6.

---

## 15. Frozen battery and gates

**General rules.**
- The batteries are frozen with the charter. Cards may not add, remove or reweight items.
- The public items are development data: they earn credit only under FC-2. Sealed holdouts and post-batch seeds exist for that reason.

### 15.1 B-SEL: the selectivity battery (exact SD0 record and code)
**Embedding.**
- Emb is uniform, priced and frozen with the card.
- It receives **only the abstract signature** of a scenario: ports, alphabets, the context hypergraph and the support.
  - Labels are scrambled under RM1/RM2 by post-batch seeds.
  - Rays, operator or vector representations, quantum witnesses, literature names and file order are withheld.
  - Verdicts must agree across at least 2 seeds.
- Emb adds no relata, relations or weights beyond a uniform image of the incidence structure. It references no scenario name, party or setting count, dimension or individual item. Any further reading is RELOCATED (NR-0).
- Mapping: measurements → interventions; contexts → jointly performed protocol sets, under the card's declared compatibility notion (FR6); outcomes → records; **parties and sites → generated blocks of Π**.

**Object.**
- The admitted family is 𝔖_𝒦(Σ) := {supp Γ_Π : Ξ ∈ Sol_𝒦(Emb(Σ))}: **the object is the set of supports of record laws.**
- **ALLOW** means the card exhibits, or proves the existence of, a realization with exactly that support. **FORBID** means it proves that no realization exists.
- Verdicts come from the card's single frozen decision procedure (DC-10). An item that is not decided is UNSCORABLE.
- A card that cannot embed Bell scenarios fails G-SEL.

| ID | Instance | Requirement | Class |
|---|---|---|---|
| SEL-0 | Every embedded instance | ∅ ≠ Sol ⊊ 𝒳 | Mandatory (structural; earns 0) |
| SEL-1 | The 1721 possibilistically local (2,2,2) tables | ALLOW all | Mandatory anchor |
| SEL-2 | The Hardy support (SD-K2) and its orbit under the 128-element relabelling group | ALLOW | Mandatory anchor |
| SEL-3 | The 8 PR boxes | FORBID all | Mandatory |
| SEL-4 | The 240 pNS (2,2,2) tables with no exact-support realization | FORBID all, as record-law supports | Mandatory (automatic; earns 0) |
| SEL-5 | GHZ (3,2,2) | ALLOW | Mandatory anchor |
| SEL-6 | Peres–Mermin square | ALLOW | Mandatory anchor |
| SEL-7 | The CHTW 3×3 KS game over the certified core of 94 rays and 67 triads (abstract signature only) | ALLOW | Mandatory anchor |
| SEL-8 | Mermin pentagram (H2); bipartite magic square; CEG-18 bipartite; GHZ (4,2,2) (G1) | ALLOW all | Mandatory anchors |
| SEL-9 | The SD-K7(i) frozen family: PR ×8; the 480 strong XOR-(2,3,2) tables; embedded PR (2,3,2); fine-grained PR | FORBID all | Mandatory |
| SEL-10 | The theta parity system: {p,q,r} even, {p,q,s} even, {r,s} odd (no operator model; J = e) | FORBID | Mandatory (OD-2) |
| SEL-11 | SD-K8: qubit versus boxworld gbit, both of capacity 2 | Exclude the gbit's PR realization. The responsibility map contains no clause on capacity, dimension, party count or setting count | Mandatory audit |
| SEL-12 | SD-K9 closure: mixing-union over whole admitted families; independent products (Hardy ⊗ GHZ admitted; PR ⊗ PR forbidden) | Respected | Mandatory (structural; earns 0) |
| SEL-13 | Specker triangle; chained-PR 6-cycle; C7 odd-cycle box (H1) | FORBID | Graded |
| SEL-14 | Padded-PR (2,2,3) | Reported; no credit either way | Report |
| SEL-15 | G2, G3, H3, H4 | Reported against their literature status | Report |
| SEL-16 | K7(ii): audit against the POVM-inclusive BMT boundary | Recorded. UNRESOLVED is allowed for a card that is blind to dimension | Audit |
| SEL-H | At least 3 blind holdouts (§15.9). Where the pool allows, one of them has a shortest known certificate longer than twice the battery maximum | Literature status | Holdout |

**Grades.**
- **EXACT-ON-BATTERY:** every mandatory and every graded item passes.
- **OUTER:** every mandatory item passes, and some graded FORBID is over-allowed. It is labelled an outer approximation and is never upgraded (FR9).
- **NON-SELECTIVE:** any mandatory failure.
- Forbidding an anchor also fires KU-5.

**G-SEL PASS** requires all of: at least OUTER; SEL-11 passed; the consistency-collapse check of §15.2; and **every SEL-H holdout passed**. An over-allowed holdout fails G-SEL, even for an OUTER card.

### 15.2 B-CF*: the consistency family
- **Members:**
  - (j,k)-consistency for j ≤ k ≤ 6;
  - Singleton Linear Arc-Consistency;
  - BLP; AIP; BLP+AIP;
  - Sherali–Adams levels ≤ 3;
  - ASP (SCOREBOARD #6);
  - every conjunction or disjunction of two members.

  The harness computes their SEL verdict vectors before Card 1.
- **Consistency collapse** holds if either:
  - (a) the card's SEL vector is within Hamming distance 1 of a B-CF* vector on the mandatory and graded items (the differing item is treated as IP-10 structure); or
  - (b) the responsibility map shows that the card's FORBID verdicts are bounded-width refutations of width ≤ 6.

  Then the card's selectivity is KNOWN SECTOR, D_sel = 0, and the SFP-10 comparators become mandatory in its audit.

### 15.3 B-REC: R1 calibration controls (exact-identity controls; no credit)
- Each record is passed through the card's static record maps (the static part of Obs) into the charter's ε code. It is evaluated **at the frozen tiers and at T_Π**.
- The output must reproduce the required value.
- For the exogenous controls (C2-G, C2-NG, C2-F′, and HB-5 with calibrated filters), the required value at T_Π is exactly 0 (DIF-5(e)).

| Control | Required value | Grade |
|---|---|---|
| BRI1 X1, Duffing bath, Gibbs; protocols P0, P1, P2; grid (π, 3π/2, 2π) | Theorem C sign structure; ε_R = ½·d_q for two protocols | DERIVED (C checked; F pending) |
| BRI1 rate | liminf N_B·ε_R ≥ \|K\|·V*/(12·m₂^(3/2)), V* = 0.943578 | Prop. G pending |
| BRI1 Tier 2 | R1-PASS (odd 7/7, even 3/3, scaling as 1/N_B) | Evidence grade |
| Harmonic twin | ε_R = 0 at both tiers (≈ 1.27×10⁻¹⁴); the bath responds through friction | DERIVED (numerical control) |
| Parametric harmonic control | ε_R > 0 at both tiers, with linear bath dynamics | D5 analysis |
| C2-G, C2-NG | 0 | R1 record |
| C2-F (colored AR(1)) | > 0 under E₂±; 0 under T_lin with calibrated filters | R1 record |
| C2-F′ (genuinely non-Markov exogenous) | 0 | D5 analysis |
| M-A (Markov); M-A′ (non-Markov) | ε_R^{T_R1} ≥ 1.915×10⁻² | D5 analysis |
| M-B | ε_R^mono ≥ 7.98×10⁻³ | Evidence grade |
| E2 | ε_R > 0 with no response. The pipeline never returns R1-PASS | Frozen pre-result |
| Prop. E product latent (HB-9) | MODE SELECTION | Frozen pre-result |

- For each control the card also reports whether it lies in Im(Sol), and its ℛ value.
- Any relation linking ε_R to Markovianity must respect DEF-10.
- Rows of pending grade are scored under PV-3.

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
| HB-11 | Two-temperature or driven steady-state baths | N | Nonequilibrium witnesses |
| HB-12 | Finite Markov jump processes with local detailed balance; discrete records | N / G | Discrete-record chart; RH-DB controls |

- **Ranges:** β ∈ [0.25, 4]; frequencies ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8.
- Members may be composed by juxtaposition or by coupling.
- **Witness rules.** A card-added witness (for Q3 or for dim_lb) counts only if it:
  - (i) comes from the HB families or their compositions within the frozen ranges;
  - (ii) satisfies BP-3 at the hostile fiber;
  - (iii) receives the B-SRB inputs through θ_dict;

  and only after the skeptic fails to refute (i)–(iii). The evaluator adds no witness that helps the card. It does add the draws for Q3(b) and Q3(c) (BP-7).
- **Containment report:** which HB members Im contains.

### 15.5 B-SRB: standard response theory with the reference package
- **Input:** the BP-5 union.
- **Procedure (before anything is unsealed):**
  - J_SRB := hull{o⃗(m) : m is a certified regime-matched standard witness (B-HB, or card-added and verified) consistent with every BP-5 input}, intersected with the region predicted by each standard scheme valid under H(x), with that scheme's error bars.
  - The schemes come from SFP-1 to SFP-7 and from auditor additions, with 𝒮 closed under mathematics and under DEF-1 to DEF-17. Each scheme's predicted record families are pushed through the charter's ε and witness code at T_Π.
  - Finally J_SRB is intersected with W.
  - J_SRB is never an outer bound from the constraints, never a window, and never the hull of all 𝒮-admissible models.
  - Auditor derivations may only shrink it.
  - "No standard formula exists for this quotient" is not silence: J_SRB is then the witness hull.
  - If no two certified witnesses differ by more than |I_K|, MC-4 fails.

| Outcome | Verdict |
|---|---|
| J_K ⊇ J_SRB, or b_meas < log₂ Q_min | RESTATED. Precedent: BRI1's Tier-1 value is a Kubo/FDT quantity |
| J_K ∩ J_SRB = ∅ under experimentally established hypotheses | KU-4, unless this contradiction is the declared ℛ★ and is consistent with existing bounds |
| Otherwise | PASS; b_meas is computed |

### 15.6 B-NULL: the nulls
- **NULL-ΠT.** Ξ is any SFP model of the declared type; Π, Z, [h] and T are chosen by hand; Γ = Obs. Its realized set is FB. Its price is given in §4.4.
- **NULL-M.** As in §4.4.
- **Required:** Im ⊊ FB; some qualifying ℛ holds on Im and fails on FB; and §4.4 holds against every null.
- **E-B twin.**
  - For every realized Γ, the auditor builds the product latent μ = ⊗_a P_a with h_a = π_a, and its causal prefix-tree version.
  - Reciprocity statements must rest on a derived carrier; otherwise the verdict is NO RECIPROCITY VERDICT.
  - Where the twin can be expressed in the declared type, X_h and X_T applied to it must return carrier FAIL or MODE SELECTION (NR-10(l)). ℛ★ need not separate it.
  - A relation satisfied by the E-B twin of every family is record-only and earns no reciprocity credit.
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
- (viii) an SFP-7/SPS comparison on AI-2 and AI-3 and on the realized dynamics. If Π is extensionally a standard mechanism (the same Π from the same data), the result is STANDARD-MECHANISM: allowed, but with no differentiation novelty, and ΔF_Π := 0. If ℛ is an STD-10 relation, it is RESTATED;
- (ix) the coarse-graining scale window (§1.3);
- (x) the size test b_Π (§1.3).

### 15.8 Anchors
- **Mandatory ALLOW anchors:** SEL-1, SEL-2, SEL-5, SEL-6, SEL-7 and SEL-8.
- **Standard-regime anchor.** For every B-REC scenario inside the declared scope, Im(Sol) contains at least one triple realized by an experimentally established standard regime (equilibrium FDT and Onsager behaviour).
- Forbidding an anchor is a FAIL and fires KU-5. Freedom reduction obtained by forbidding anchors, or by emptying Sol, earns nothing.

### 15.9 Sealed holdouts
- **Protocol.** `F0_SD0_HOLDOUT_PROTOCOL_01.md`, adapted.
  - The Selector is invoked only after the batch closes.
  - It receives the protocol, the exclusion lists, the scenario conventions and each card's bare input/output signature, and nothing else.
  - The selection is committed by hash before any evaluation on the selected cases.
- **Pools:**
  - (a) Selectivity: support-level cases with an established classification (eligibility E1–E4). Excluded: everything in §15.1, G1–G3, H1–H4, and the whole (2,2,2) scenario. At least 3.
  - (b) Reciprocity: standard-model environments with exactly computable ε_R, outside the frozen HB parameter points. At least 3. Before unsealing, the card predicts whether each lies in Im(Sol) on the relevant fiber and, if so, its ℛ★ value. A holdout in Im that violates ℛ★ is a Q1 failure.
  - (c) AI-5 instances.
  - (d) LOCK-H datasets (MC-8).
- Holdout results are tallied separately and never enter ΔL.
- A failure on an item of mandatory type fails the gate.
- A void caused by the author side → FAIL. A void caused by the auditor side → one disclosed reselection.

### 15.10 Stage-4 gates (picked card only)
Each gate is recomputed by an agent that did not build the card, checked externally before banking, and followed by checkpoint (e).

**G4-SEL.** §15.1 and §15.2, recomputed, including SEL-H.

**G4-DIF.**
- **DIF-1** Π is computed by the frozen algorithm on every in-domain solution.
- **DIF-2** Persistence holds (δ_Π, η, δ_∂, H with τ_slow) across A_{r★★} and the whole horizon; horizon doubling passes; the scale window passes.
- **DIF-3** Π is nontrivial, size test included (§1.3).
- **DIF-4** Π is GENERATED-STRONG or GENERATED-WEAK.
- **DIF-5** The carrier, [h] and T_Π are GENERATED:
  - (a) T_Π ∈ 𝕃_T^adm;
  - (b) T_Π is nontrivial: some B-REC or B-DIF family has ε^{T_Π} > 0, and some has ε^{T_Π} = 0;
  - (c) T_Π is placed relative to T_R1, T_mono and J;
  - (d) T_Π is not a GY-11 or GY-12 class (behavioural test, §21.2);
  - (e) **exogenous null through the card's maps:** every exogenous B-REC/HB family, passed through the card's static record maps, gives ε^{T_Π} = 0.
- **DIF-6** Π is unchanged within δ_Π under relative perturbations of 2^(−p★) applied to every numeric input while preserving Aut(inputs).
- **DIF-7** Universality: on all of Sol, on every in-domain instance.
  - The domain is a decidable predicate frozen in C16 at card freeze and never edited.
  - It contains AI-1 and AI-2, and its coverage of the AI-3 draws must be ≥ θ_gen.
  - IP-13 prices it.
- **DIF-8** Covariance (NR-8).
- **DIF-9** The environmental identity across interventions, and the environment's state variable, are outputs.
- **DIF-10** The B-DIF (viii) classification is recorded.

**G4-NR.** NR-0 to NR-17 are re-run computationally on AI-1 to AI-5. The reader and decoder batteries are run by an agent that has not seen the card's derivation of Π.

### 15.11 Stage-5 gates
- **G5-LOCK.**
  - Q1–Q12 and the scope are re-verified independently at r★ and r★★.
  - DISTINCTIVE (P) is re-confirmed.
  - The preregistration is a byte-identical copy of C13. The only allowed differences are fields that C13 explicitly deferred to a frozen deterministic rule, such as a device the Selector draws. Any other difference is a BU-3 modification.
  - MC-5 to MC-11 apply. LOCK-INCONCLUSIVE fails G5-LOCK.
- **G5-HOLD.**
  - After G5-LOCK, a hostile auditor selects at least max(2, number of lock observables) holdouts. They come from the at least 2·max(2, n_obs) candidate classes listed in C13, plus the auditor's own.
  - Each holdout is a physically realized system class inside the declared scope that the card does not reference.
  - Measured data only. Their hashes are committed before evaluation.
  - **PASS:** each holdout meets MC-5's confirmation condition against the I_K that the card's frozen prediction procedure gives for it, computed and committed by hash before evaluation.
  - MC-5 falsification on any holdout fires KU-12.
  - If the auditor cannot find the required number of classes inside the scope, G5-HOLD FAILS.
  - At most one holdout may be replaced by a prospective experiment that the hostile auditor designs or approves.
- **G5-MDL.** On the sealed data, b_meas is recomputed with the realized σ_eff, and must remain ≥ log₂ Q_min.
- Only sealed real data can confer PREDICTIVE.

### 15.12 Stage 6 (pointer; its own charter)
- The same 𝒦, unmodified, must yield the quantum, thermodynamic and gravitational regimes. ε_R is exported as in XS-10.
- Any need to modify 𝒦 → STAGE3-ROUTE-TERMINATED.
- Stage 6 opens only under a Stage-6 charter frozen alone, with its own gates and clock. Failing a Stage-6 gate terminates the route.
- Memory, viscoelasticity and crystalline order are checked as effective regimes after Stage 4.
- B-SEL OUTER cards carry a flag on the quantum regime.

---

## 16. Decidability and scorability

- **DC-1 Total procedures.**
  - Every gate predicate, Sol membership, and every chain map at r★ and r★★ needs a frozen decision procedure with a termination argument: a proof, or a finite bound on an enumeration.
  - An enumeration bound is a law constant priced under IP-5. Its timeout branch is declared and scored.
  - A verdict that flips at half the bound or at twice the bound is BATTERY-TUNED.
- **DC-2 Resources.**
  - The card declares time and memory per item.
  - Absolute ceilings R_item and R_card [P] apply. Declared resources above them make the card CARD-UNDECIDABLE at S2.
  - The evaluator runs each item for min(κ·declared, R_item). An overrun is UNSCORABLE.
  - There is no "pending compute" status.
- **DC-3 Exactness.**
  - Zero tests, equalities and memberships are decided in exact arithmetic (ℚ or algebraic numbers), or by certified intervals separated from the decision boundary by at least 2^(−p★). ε-claims follow §1.4.
  - A tolerance-based "≈ 0" is UNSCORABLE, unless the tolerance is part of the frozen law, in which case it is priced and its robustness is checked.
- **DC-4 Truncation.**
  - Unbounded quantifiers (over all dimensions, all n, all extensions) need a frozen finite truncation level. That level is part of the law, is priced, counts as VB-10, and is what gets scored.
  - Every FORBID must hold at levels n, n+1 and 2n. A verdict that flips within that range is a size discriminator: a GY-4 return.
  - The card declares resources for levels n+1 and 2n. If a check does not finish within κ times those resources, the relation is a truncation artifact and earns zero.
  - Claims about the limit earn nothing.
- **DC-5 Possibly undecidable targets.**
  - Exact quantum correlation and support families may be undecidable (Slofstra).
  - OUTER or INNER status is declared in C4 at freeze. A claim of exactness without a proof → CARD-UNDECIDABLE, and the card is never relabelled.
  - A solution set defined by reference to an object whose membership cannot be checked in finitely many steps is priced as that object (IP-6).
  - No exactness is claimed beyond the battery (FR9).
- **DC-6 Gate semantics.**
  - A gate is PASS only if every mandatory item is scored and passes.
  - An UNSCORABLE mandatory item means the gate is not passed. Such a card cannot advance, and its GRAVEYARD line follows T-1.
- **DC-7 No pending status.** An UNSCORABLE verdict is never reopened within the route, whether by later tooling, a larger κ or another truncation level. Another truncation level would make a new card.
- **DC-8 Consistency cards (semantic flag).**
  - The harness flags a card if, on every B-SEL embedding and on an AI-3 sample, supp(Sol) equals the survivor set of some B-CF* member up to Emb.
  - A flagged card earns D_sel only by surviving §15.2.
  - It can claim differentiation only under FR8: its C7 algorithm must compute Π as an output. A veto generates nothing.
  - It has ε values only through a weight rule within supports (FR15(b)). That weight rule is then the actual law, priced and judged as such.
  - Weights that are a fixed function of the support (uniform, or maximum entropy on the support) are a convention. ε-relations under them are scored as support relations, with ε credit 0. ε credit requires a W-pipe showing that the weights change under clause ablation while the support stays fixed.
  - No weight rule → CARD-UNMEASURABLE.
  - Its quantum claims are capped at OUTER.
- **DC-9 Reference implementation.** Frozen with the card and run unchanged (PC-8). Changing it is a modification, except for a §19.2 tooling repair.
- **DC-10 One decision procedure.** Each card freezes one sound procedure, declared as an outer or inner approximation, with a single level for all items. Its verdicts are the card's verdicts. UNDECIDED = FAIL for gating, and zero credit.

---

## 17. Required card template (fields)
Each card is one committed file plus its reference implementation. The SHA is recorded before any scoring. Every field is mandatory.

| Field | Content |
|---|---|
| C1 Identity | Card number; slot; freeze SHA; charter SHA; harness SHA; n_drafts and τ_sel, with the search code and logs; the datasets and items the author has seen; the nearest earlier card and the non-variant argument (BU-4, including mechanism distinctness); designer provenance |
| C2 Exact law | 𝒳 and V_Ξ; the type of 𝒞 and its FR11 meaning in L₀; 𝒦 in L₀ plus priced vocabulary, with every quantifier explicit; normal form and normalized skeleton; the notion of solution; truncation levels; uniform instantiations at r★ and r★★; the reference implementation |
| C3 Ontology declarations | Gluing as an explicit act (FR2); the source of temporal order and of the time unit (FR7); compatibility scope and Emb (FR6); subsidiary possibility dependencies (FR14); the G0-trichotomy landing, including weights within supports (FR15) |
| C4 Decidability | The single decision procedure (DC-10); OUTER/INNER status; termination arguments; resources per item and for levels n+1 and 2n |
| C5 Price ledger | §4.6 in full |
| C6 Input inventory | The §5.2 list; the expected outcome of every NR test; any declared supplied structures |
| C7 Generated structures | Π (δ_Π, η, δ_∂, H, τ_int, τ_slow, scale window, b_Π); the derivation of Z_Π and the carrier, including NR-10(h)–(l); [h]_{T_Π}; T_Π, with its placement and s_T; Γ_Π. For each: algorithm or proof, responsibility map, grade, and expected NR label |
| C8 Lock register | ℛ★: formula, coordinates, at most 3 lock observables, frozen witness families, rectangle witness, lock fibers (including the platform-matched one), the I_𝒦 rule, claimed c_J/κ_J, the derivation 𝒦 ⇒ ℛ★ with its grade, Q3 witnesses per framework and regime, W-pipe, and the DEF and JN arguments. An optional secondary relation is given in the same format |
| C9 Response scope | Per relation (§14), with the scope conditions; evidence of non-vacuity; the expected carrier verdict at measurement and how it will be certified |
| C10 Certificates | Q1–Q12, as code plus machine-readable output |
| C11 Freedom and compression | c_J, κ_J and the dimension certificates per credit instance; b_J; b_meas; I_int; claimed D_sel; Price; ΔL, ΔL₀ and ρ at p = 6, 10 and 16; §4.4 against NULL-ΠT and NULL-M |
| C12 Hostile baseline | The regime map H(x) for every realization class (Appendix-F surrogates) and the hostile fibers; the attempted derivation of ℛ★ from 𝒮 and why it fails; the predicted J_SRB; the B-HB witnesses with genericity and transplant predictions; the boundary-rule check; the D5 reverse-direction relations; B-CF*; the conjunction test; the predicted outcome of every battery item |
| C13 Measurable target | The LT-1 instantiation: the named platform and its class; the operational definition of each coordinate; the interface-side data sources and calibration-only protocols; the identification plan; A; tier; estimator; J_K; σ_pre; Θ_std; the live rival; effect size; N_req; power; platform time; sealing route; at least 2·max(2, n_obs) candidate holdout classes; the declared scope domain |
| C14 Kill conditions | Acknowledgement of KU-1 to KU-13; the card-specific kill conditions, meeting KP-1 to KP-4 and KP-2′ |
| C15 Selectivity interface | Emb; the support object; every SEL verdict, with its decision procedure |
| C16 Audit instances | AI-1; the input type for the AI-3 reference measure; the frozen domain predicate and its price |
| C17 Representation | The declared moves (RM1–RM5 plus priced extras) with their generating set; the covariance argument. No unique formula for h |
| C18 Tradeoff declaration | Whether any monotone identity–response relation appears. If so, its derivation from 𝒦 and the W-pipe for the opposite sign |
| C19 FR and GY standings | The tables of §21 |
| C20 Dependencies, transfer, non-claims | The pending R1 items used (scored per PV-3); the transfer plan (the θ ledger with the θ_dict count and ranges, the sector pair, the transfer observable, the SI witnesses, the exported T_Π class); explicit non-claims |

---

## 18. Scoring procedure, step by step

### 18.1 Sequence
0. **Preconditions.** The charter is frozen; the harness work order is validated and externally checked (§19.3); the B-CF* vectors, the chart and the coder are tested.
1. **Draft ledger.** Every draft is logged (BU-5).
2. **Card freeze.** Each card is one commit with its SHA, the reference implementation and C1–C20, battery predictions included. τ_sel is computed.
3. **Batch close** (BU-6).
4. **Intake, for all cards together:**
   - S0;
   - S1: the variant check and the GY declarations;
   - S2: decidability;
   - the static NR tests: NR-0, NR-1, NR-2 and NR-14.

   No intake result is visible to any author before the batch closes.
5. **Selection.** The Selector fixes and commits by hash: the AI-3 seeds, the credit-instance draws, the AI-2 constructions, the B-DIF and NR-8 seeds, the Emb scramble seeds, SEL-H, the reciprocity holdouts and AI-5.
6. **Evaluation.** The Evaluator runs screens S0–S8 on every card. S9 runs on every card that clears S0–S8, and must be complete within T_audit.
7. **Recomputation.** A second agent recomputes every screen result before anything is reported.
8. **Checkpoint (d).** At most 5 lines per card. The owner picks among the ADMISSIBLE cards, or the route terminates.
9. **Stage 4** on the picked card (§15.10), with checkpoint (e) after each gate.
10. **Stage 5** (§15.11): G5-LOCK, G5-HOLD, G5-MDL and the LT-1 unsealing, with checkpoint (e).
11. **Banking** under §11.

### 18.2 Screens (in order)

| Screen | Tests | Terminal if this is the first failing screen |
|---|---|---|
| S0 Completeness and intake | C1–C20 present and non-empty; KP-1 to KP-4 and KP-2′; FR2, FR3, FR6, FR7, FR11, FR14 and FR15 declarations valid | CARD-INCOMPLETE |
| S1 Distinctness and graveyard | BU-4, VAR-1 to VAR-6, BU-9; the GY return test at card level | CARD-VARIANT; CARD-GRAVEYARD |
| S2 Decidability | DC-1 to DC-10 | CARD-UNDECIDABLE (UNSCORABLE included) |
| S3 Nonrelocation | PC-6, PC-7; NR-0 to NR-17; §5.6 | CARD-RELOCATED; CARD-NONGENERATIVE; CARD-DEFINITIONAL (PC-6) |
| S4 Chain and consistency | KU-1; every chain map at r★ and r★★; persistence, size and nontriviality on the lock fibers; 𝒮 (KU-2 to KU-4); B-REC (KU-6); anchors (KU-5) | CARD-EMPTY; CARD-UNDIFFERENTIATED; CARD-INCONSISTENT |
| S5 Lock certificates | Q1 to Q12 on ℛ★ at r★ and r★★, including transplant, genericity, JN, B-SRB, B-NULL, and the reverse-direction and boundary screens | CARD-UNFORCED (Q1); CARD-DEFINITIONAL (Q2); CARD-STANDARD (Q3); CARD-PIPELINE (Q4, Q11); CARD-NONJOINT (Q5); CARD-UNINFORMATIVE (Q6); CARD-NONINVARIANT (Q7, Q8); CARD-VACUOUS (Q9); CARD-UNSCOPED (Q10); CARD-INCOMPLETE (Q12) |
| S6 Freedom and compression | SC1; §4.4 against every null; §4.5 | CARD-RELOCATED (LOOKUP); CARD-NONCOMPRESSIVE |
| S7 Measurability | §3.3, including MC-11 and lock-fiber robustness | CARD-UNMEASURABLE |
| S8 Selectivity | §15.1 and §15.2, computed by the harness after the batch closes | CARD-UNSELECTIVE |
| S9 Originality | The complete assembled-law audit (§8), within T_audit | CARD-RESTATED; CARD-ASSEMBLY (bankable per OR-5) |
| — | Otherwise | **CARD-ADMISSIBLE** |

---

## 19. Freezing and preregistration

### 19.1 Charter freeze
- **FZ-1 Preconditions:**
  - (a) the owner fixes the Appendix-A constants and decides the points in Appendix C;
  - (b) the self-tests ST-1 to ST-11 (§24.2) return their stated verdicts on paper;
  - (c) ST-10 (credit feasibility) shows that SC1–SC3 are jointly reachable for an honest relation at the frozen constants. If not, the constants are changed before the freeze;
  - (d) an auditor confirms that the cited rules catch every CHARTER TEST (CT-01 to CT-59 and every ledger row), and the definitional lens is re-run on v1, because the bodies of Report D's CT-D01–CT-D10 were not available to the reviser. A pattern that no rule catches is a charter defect, and it is fixed before the freeze.
- **FZ-2** The charter is committed **alone**, with a `pending` CHECKS line. Every card cites its SHA.
- **FZ-3** STOP for owner review.

### 19.2 Repairs and interpretations
- **After the charter freeze:** every repair (numbered CR-n, by owner ruling) may only tighten a rule. A loosening requires a fresh charter freeze, together with a certification that no draft has been logged since the previous freeze.
- **After Card 1 is frozen:**
  - the charter text is immutable for Stages 3–6;
  - a **tooling repair** may only fix a crash or a failure to terminate, and must reproduce all prior outputs byte for byte;
  - an error repair ruled by the owner may only tighten a rule. It applies to every card, and rescoring may move verdicts only toward failure;
  - a harness fix made after the batch closes is rerun on every card, null and self-test. Any verdict that changes in a card's favour needs the Recomputer's confirmation and an external check;
  - interpretations follow CV-7 (CI-n).

### 19.3 The harness work order
- **Scope.** After owner authorization, and while no card exists, one bounded work order implements §§1–5, §§12–16, the chart, B-CF*, the Appendix-F surrogates, the VB axiom checklists, the normalizer and the price coder.
- **Who.** It is **executed by an agent context that authors no card.**
- **Time box.** It is limited to T_harness [P].
  - Anything it cannot compute within the box takes the hostile default that a CR sets before Card 1.
  - An overrun leads to a CR or to STAGE3-OWNER-HALT, never to an extension.
- **Checking.** Its outputs are externally checked before the first draft is logged. Every card cites the harness SHA.
- **Not a prerequisite campaign.** It is not Card 1. Its complete deliverable is the validation list below.
- **Validation list:**
  - the SEL counts 2961 / 1721 / 1232 / 8, the 240 gap and 2721;
  - the PR-forcing lemma;
  - ε ≡ 0 on single-protocol families;
  - the exact zeros on HB-1, HB-3, HB-4, and HB-5 under T_lin with its calibrated filters;
  - HB-9 returning MODE SELECTION;
  - the sign of BRI1's Tier-1 PASS on HB-2;
  - STD-1 holding exactly on every HB family;
  - the B-CF* vectors;
  - the price coder on Appendix B;
  - ST-6 to ST-9.
- **Rejection tests.** The following patterns, built only from HB models plus supplied structure, must each be rejected with the stated terminal:
  - CT-18, CT-21 and CT-22;
  - an X_T that reads Γ on HB-2 → CARD-DEFINITIONAL;
  - a disjunctive pin → NONJOINT;
  - a tier-swap rectangle → NONJOINT;
  - an invariant but non-maximal s_T → Q8 void;
  - protocol-induced maps added to T on HB-1 → CARD-DEFINITIONAL;
  - a static map applied on HB-4 → DIF-5(e) fails;
  - a log-reparametrized observable → b_meas computed in frozen units;
  - generated-premise laundering and automatic detailed balance (S:RT-S-01/02) → STANDARD;
  - amplitude interpolation → STANDARD;
  - rank at a chosen point → the generic rank governs.

### 19.4 Card preregistration and the batch-freeze rule
- Every field, every battery prediction and the lock register are frozen before that card's evaluation.
- **Batch freeze** (OD-1, BU-6). No card is scored before the batch closes. Intake runs at batch close, for all cards together.
- **Information hygiene.** Authors never see sealed holdouts, seeds, intake results or another card's scores before the batch closes.
- **Lock preregistration** follows MC-5, MC-8 and G5-LOCK.

---

## 20. Staircase prohibition

**The staircase test.** A **forbidden staircase move** is any work item that delivers an ingredient for a present or future 𝒦 card and is not one of: a frozen card, the §19.3 work order, a gate result, or a terminal record. The motivation behind the work item is irrelevant.

**Forbidden at any time, before or after termination:**
- **SM-1** A "missing ingredient", "deeper prerequisite" or "foundations" campaign. Examples: a theory of the carrier, of weights, of temporality, of the partition, of the interface class, of Gibbs structure, of the representation of Ξ, of decidability, or of standard persistence; J_SRB tooling; d_op for a generated T.
- **SM-2** Any change to a gate, battery, baseline, chart, pricing rule or constant that would let a failed card pass, or any rescoring under modified rules (§19.2).
- **SM-3** Describing a failed card as "partial progress" or "future work", or opening an extension stage for it.
- **SM-4** Budget laundering (BU-8), or a fourth card.
- **SM-5** Reopening R1: new interface classes, a change to d_op or to the verdict table, or reinterpreting WO-002.
- **SM-6** Treating UNSCORABLE or UNRESOLVED as "pending better tools".
- **SM-7** Mining GRAVEYARD entries for "repaired" candidates (§21.2).
- **SM-8** Opening a new generative route by any means other than an explicit new owner ruling (T-5).
- **SM-9** Treating a failure traced to a missing premise as licence for a prerequisite study. Such a failure ends that card (RULES 4).

**Non-blocking items.** M5, D4, Tier-2 carrier necessity, triviality of the join, WO-001 C3/C4 and the pending external checks continue as housekeeping.
- They are **never prerequisites** of any Stage-3, 4 or 5 step.
- Verdicts that touch them are scored under PV-3's hostile reading.
- Their results cannot reopen this route.

---

## 21. Relation to FR1–FR15 and the GRAVEYARD

### 21.1 FR1–FR15
Each FR receives a standing of SATISFIED (with its argument), SCOPED-OUT (declared and priced), N/A (with a reason the auditor may contest), or VIOLATED. No FR is claimed discharged without an external check.

| FR | Stage-3 form | Where | Consequence of violation |
|---|---|---|---|
| FR1 Representation invariance | Covariance under the declared, protocol-uniform moves only | §1.6, Q7, NR-8 | NONGENERATIVE, or the relation is NONINVARIANT |
| FR2 Gluing is an explicit act | Composition of Ξ-instances is declared | C3, SEL-12 | INCOMPLETE |
| FR3 No inaccessible-context data | Per-protocol laws only | §1.3, Q7, NR-0 | INCOMPLETE (inputs) or NONINVARIANT (relation) |
| FR4 Observer independence | Π and [h] come from Ξ | DIF-9 | NONGENERATIVE |
| FR5 No unpriced split | Strengthened: even a declared split fails. Pricing never substitutes for generation of protected structures (§5.1) | §5.6 | NONGENERATIVE (declared); RELOCATED (hidden) |
| FR6 Compatibility scope | Declared in Emb | C3, §15.1 | INCOMPLETE |
| FR7 Earned temporality | Time is primitive and priced (VB-9), or earned; the instantaneous-state designation is derived; DEF-16 | C3, NR-10 | INCOMPLETE; RELOCATED if hidden |
| FR8 Constraint ≠ selection | Q1 holds on all of Sol; DIF-7; DC-8 | §3, §15.10 | UNFORCED or NONGENERATIVE |
| FR9 No outer→exact upgrade | B-SEL grades; DC-5 | §15.1, §16 | The claim is not credited |
| FR10 Information price | §4 | §4 | An unpriced input → RELOCATED |
| FR11 Declared meaning of 𝒞 | An L₀ statement, priced | C2, IP-2 | INCOMPLETE |
| FR12 Convention fixes | Adopted for the B-SEL encodings | §15.1 | Correction required |
| FR13 A deeper Γ object | Γ_Π = Obs_Π(Ξ) is built; Γ as an empirical model counts as SUPPLIED | §1.3, C7 | NONGENERATIVE |
| FR14 Subsidiary possibility facts | Dependency declared | C3 | INCOMPLETE if hidden |
| FR15 G0 trichotomy | Landing declared; weights within supports (b) are addressed | C3, DC-8 | INCOMPLETE; no weight rule → UNMEASURABLE |

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
| (T-1) | Every screen failure recorded for an earlier card of this route or any earlier route |

- **Declarations.** For each entry the card declares one of: NOT USED; COMPARATOR ONLY; COMPONENT (priced, with every distinction it alone produces removed); RESEMBLES (with an argument that distinguishes the card from it).
- **Behavioural equivalence.**
  - A component that reproduces a GY entry's verdict pattern on that entry's finite test domain **is** that entry, whatever its name. The test domains are the SD0 battery for discriminators, and the R1 ladder plus the E1/D1 constructions for T classes.
  - A generated T_Π or [h]-class is GY-11/GY-12 if, on the declared finite projection, it absorbs every family that a GY-killed class absorbs (unrestricted bimeasurable bijections; protocol-dependent linear readouts; a latent-dimension-only constraint).
- **Return test.** A claim's responsibility map contains a component equivalent to a GY entry (under VAR-1, VAR-2, or behaviourally), and the claim vanishes when that component is ablated.
  - **Claim level:** the claim is not credited.
  - **Card level, CARD-GRAVEYARD (KU-9):** the returning component carries the selectivity discriminator, the mechanism that generates Π, or ℛ★; or every credited claim fails the test.
- **GY-10** reopens only with a new named candidate. A card that is a selector must say so, and it is audited against GY-10's screen.

---

## 22. Not credited (index)
FC-4 and §13 govern. The following are never credited:
- **Definitional and standard content:** DEF-1 to DEF-17 and any bits on 𝒜_ε; 𝒮 consequences, including the near-regime and boundary rules; the D5 reverse-direction relations; RECOVERY.
- **Calibration-only results:** BRI1's Tier-1 value and its rate, the harmonic R1-NULL, and the C2 and M controls.
- **Consequences** of priced inputs or of supplied structures.
- **Relations without a W-pipe**, or that fail JN.
- **Reductions** that are marginal, inequality-only or off the chart; ΔF_Π, ΔF_T and ΔF_supp.
- **Persistence and differentiation:** these are gates.
- **Pseudo-couplings:** single-axis restrictions; Π–T-only couplings; disjunctive pins; ε-class couplings.
- **Scope-Q relations** in the ε ≡ 0 blind spot; ε at a non-admissible T; truncation artifacts; redundant instances.
- **Relations** that are sign-only, single-protocol, from a hand-picked repertoire, dependent on a representative, built on joint laws across protocols, or record-only.
- **Readings** of R1-NULL as "no response".
- **Selectivity** reached through bounded-width consistency; structural or automatic SEL items.
- **Holdout successes** as compression; **in-silico locks** as PREDICTIVE.
- **Analogy** or same-regime replication as CROSS-SECTOR.
- **Novelty** of components, representations or names.
- **Re-presented post-result seeds:** Z_A, the measurement-invariance framing, and [h]_T in its known forms.
- **"ε_R > 0 somewhere".**
- **A presumed monotone identity–response tradeoff.**

---

## 23. Governance and roles
- No agent context both authors and audits the same card. The **Harness builder** authors no card.
- **Roles:**
  - **Author:** the builder (Claude Code), in contexts that build no harness and audit nothing.
  - **Intake auditor:** independent and hostile; runs at batch close.
  - **Evaluator** and **Recomputer:** independent of each other and of the author.
  - **Selector:** sees the card signatures only.
  - **Comparator panel:** analysts and skeptics.
  - **External checkers:** via `CHECKS.md`.
  - **Owner:** rulings (CV-7), the pick, and the final count.
- The hostile default (CV-1) governs every dispute until the owner rules.
- **Records.** Each card, intake audit and gate result gets a CHECKS line once it is verified on the remote. Checkpoint reports are 5 lines or fewer: stage · result · scoreboard change · next action · blockers.

---

## 24. CHARTER TESTS and charter self-tests

### 24.1 CHARTER TESTS
**Every row is an abstract gaming pattern labelled CHARTER TEST, never a physical proposal.** If a card instantiates a pattern, it is presumed to receive that pattern's classification, and the card carries the burden of rebuttal. **CT-60 onward are the rows of the Red-team ledger**, each with its blocking clause.

| ID | CHARTER TEST pattern (abstract) | Caught by | Outcome |
|---|---|---|---|
| CT-01 | An input asymmetry from which Π can be read cheaply, e.g. a weighted structure whose cut or community equals Π | NR-5, NR-6, NR-7 | RELOCATED |
| CT-02 | Sorts or labels of Ξ's type whose classes coincide with S/E | NR-1, NR-6 | RELOCATED, or NONGENERATIVE if declared |
| CT-03 | A clause that asserts a bipartition with a persistence or decoupling property | NR-1 | NONGENERATIVE |
| CT-04 | A table of constants whose block or zero pattern is Π | NR-6, IP-3 | RELOCATED |
| CT-05 | A vanishing explicit seed in 𝒞 selects Π | NR-5 (λ at 0, 2^(−p★), 2^(−2p★)) | NONGENERATIVE |
| CT-06 | An extractor threshold tuned so that Π appears only on Sol | NR-3, DIF-2, IP-5 | RELOCATED (pipeline) |
| CT-07 | Π depends on a chosen basis or coordinate system | NR-8 | INVALID → NONGENERATIVE |
| CT-08 | Persistence obtained by pushing relata into the boundary ∂ | §1.3 | Not persistent |
| CT-09 | The carrier stated as an axiom, or Obs defined with one shared readout by construction | NR-1, NR-3, NR-10 | RELOCATED; NO RECIPROCITY VERDICT |
| CT-10 | The carrier variable declared to be the instantaneous E state by definition | NR-10(c), (i) | RELOCATED |
| CT-11 | Protocol-dependent readouts in disguise, used to obtain ε_R > 0 | NR-10(a), NR-11, B-NULL | MODE SELECTION; lock void |
| CT-12 | T_Π equal to the automorphism group of a supplied record structure | NR-10(f), (k) | NONGENERATIVE |
| CT-13 | T_Π picked from 𝒯 by a selector clause rather than constructed | NR-1, NR-10(f), IP-4 | NONGENERATIVE |
| CT-14 | A generated T_Π ⊇ J or T_univ, so ε ≡ 0 | Q8, DIF-5, B-NULL | Relations void; DIF-5 fails |
| CT-15 | R1 calibration data used as law inputs | NR-10(g), NR-14 | RELOCATED |
| CT-16 | Admissible states restricted to Gibbs, KMS or detailed-balanced states, or a temperature among the inputs | NR-1, NR-12, PS-5 | SUPPLIED with dependent claims at 0; RELOCATED if hidden or if ℛ★ uses it |
| CT-17 | Thermal structure entering through a weighting measure or a prior of Gibbs or maximum-entropy form | NR-9, NR-12 | RELOCATED (prior) |
| CT-18 | A known standard model, with its cut, readout and Gibbs ensemble, repackaged as a law | NR-1, NR-12, IP-7, OR-3, NULL-M | NONGENERATIVE / RESTATED |
| CT-19 | The lock smuggled in as a clause, or as the objective or penalty of an extremum principle | NR-2, NR-13, DEF-17 | RELOCATED |
| CT-20 | A tradeoff or sign imposed by an input clause, or a monotone identity–response tradeoff postulated | Q11, NR-13 | RELOCATED |
| CT-21 | A lock that is an identity of ε's definition or of R1's theorems | Q2, DEF-1 to DEF-17 | DEFINITIONAL |
| CT-22 | A lock that follows from KMS, FDT, a fluctuation theorem or Onsager, rewritten in (Π, T, ε) variables | Q3, STD-3, STD-4, NR-12, B-SRB | STANDARD |
| CT-23 | A lock equal to a D5 reverse-direction relation | Q3, §13.8 | STANDARD |
| CT-24 | A lock that is a size-scaling law of ε_R or of its witnesses | STD-9 | STANDARD |
| CT-25 | A lock of the form "an odd channel vanishes under a symmetric reference" | STD-5, Theorem C | STANDARD |
| CT-26 | Regime shopping: witnesses from another regime, or avoiding Gibbs structure so that the baseline is weaker | BP-3, BP-4, §13.5, §1.5 | Witness invalid; scored on the hostile fiber |
| CT-27 | Separate interface and response constraints presented as one relation | Q5, c_J | NONJOINT |
| CT-28 | A scope-Q relation on a realized set with ε_R ≡ 0 | Q9 | VACUOUS |
| CT-29 | Scope switching | §14 | Lock void / UNSCOPED |
| CT-30 | ε evaluated at a non-admissible, joined or universal T | Q8 | Void |
| CT-31 | A relation that holds for one representative h but not for the class | Q7 | NONINVARIANT |
| CT-32 | A relation that uses joint laws across protocols | Q7, FR3 | NONINVARIANT |
| CT-33 | A relation that holds only because \|A\| = 1, or only for a listed repertoire | Q1, §1.7, B-NULL | UNFORCED |
| CT-34 | A lock that predicts ε_R from the same Γ it is computed on, or a pin | MC-2, DEF-13 | DEFINITIONAL |
| CT-35 | An identification plan that certifies Π or T_Π by using ℛ★ or a record functional | MC-2 | UNMEASURABLE |
| CT-36 | A lock that needs more than N_max samples | MC-7 | UNMEASURABLE |
| CT-37 | Forcing claimed from numerics with a tolerance | Q1, DC-3 | UNFORCED |
| CT-38 | A truncation artifact | Ch-4, DC-4 | Zero |
| CT-39 | Inflation through grid, precision, instance copies or carrier size | Ch-1, Ch-3, Ch-5 | No gain |
| CT-40 | Freedom reduction obtained by forbidding anchors or emptying Sol | §15.8, §2.5 | No credit; KU-5 |
| CT-41 | A real constant tuned to make the lock hold or to flip one battery item | IP-5, IP-10 | Priced; distinction not credited |
| CT-42 | One symbol encoding a table; target vocabulary encoded as an isomorphic L₀ table or re-derived as a definition | IP-3, IP-6 closure, NR-6 | Priced in full; RELOCATED if Π is decodable from it |
| CT-43 | Selectivity by lookup: scenario name, party or setting count, dimension or capacity | IP-9, SEL-11, §21.2 | RELOCATED or GRAVEYARD |
| CT-44 | A law built only from consistency conditions, whose battery behaviour matches a B-CF* member's, with no weights | §15.2, DC-8 | D_sel = 0; UNMEASURABLE |
| CT-45 | An exact characterization claimed for a target that may be undecidable; membership quantified over all extensions with no truncation | DC-4, DC-5 | UNDECIDABLE or OUTER |
| CT-46 | Many drafts produced, the best frozen, the search undisclosed | IP-12, BU-5, KU-10 | Tax charged; void if undisclosed |
| CT-47 | A repair variant | VAR-1 to VAR-6, BU-4(e) | VARIANT; slot consumed |
| CT-48 | Items, domain or response scope declared OUT after results are seen | BU-3, DIF-7 | New card or VARIANT |
| CT-49 | Deferral: "ℛ follows once X is derived", "T_Π derived in a follow-up" | NR-15, §20 | SUPPLIED; no X campaign |
| CT-50 | A baseline, battery or chart edited after a card is seen | §19.2 | Forbidden |
| CT-51 | A pending item cited as checked | §11 PV-3 | Scored under the hostile reading |
| CT-52 | Protocols chosen so that the relation happens to hold | Ch-2, §1.7, Q1 | No effect |
| CT-53 | Memory, viscoelastic or crystalline-order input | NR-14 | RELOCATED |
| CT-54 | A record-only statement offered as evidence of back-reaction | STD-12, B-NULL | No reciprocity credit |
| CT-55 | Holdouts selected before the batch closes, or by an agent that has seen the mechanism | §15.9 | Evaluation void; one disclosed reselection |
| CT-56 | A weak set of comparators | OR-4 floor | Audit incomplete; no DISTINCTIVE |
| CT-57 | A "transfer" in which a B-side fit absorbs the prediction, B data enter the fit, a standard bridge links A and B, or B replicates A | XS-2, XS-6, XS-7 | Not CROSS-SECTOR |
| CT-58 | Threshold, platform, tier, repertoire or estimator chosen after card freeze | MC-5, MC-8, G5-LOCK | LOCK-VOID = LOCK-FALSIFIED |
| CT-59 | A discriminator that reduces to capacity or dimension, party count, a blanket ban on strong contextuality, maximal T, or a latent-dimension bound | §21.2 (behavioural) | CARD-GRAVEYARD |

### 24.2 Charter self-tests
These must hold at freeze (FZ-1). They are run on known objects only; none of them is a candidate.

| ID | Known object treated as if it were a card | Required verdict |
|---|---|---|
| ST-1 | BRI1's Tier-1 ε_R relation | S3: CARD-NONGENERATIVE (the partition, readout, bath and Gibbs state are all supplied). Independently, B-SRB: STANDARD (STD-3 nonlinear FDR plus STD-9) |
| ST-2 | The harmonic R1-NULL | STANDARD (STD-3, STD-6, Ford–Kac–Mazur). RS-1 applies: R1-NULL ≠ no response |
| ST-3 | ASP | S1: CARD-GRAVEYARD (GY-6). Also: SEL-10 (theta) and SEL-4 (the 240 tables) admitted, so NON-SELECTIVE; B-CF* collapse; no weights, so UNMEASURABLE |
| ST-4 | NULL-ΠT | Credited = 0, so ΔL ≤ 0: LOOKUP → RELOCATED. It is also NONGENERATIVE |
| ST-5 | The product-latent E-B model | NR-11: MODE SELECTION. STD-12: no credit |
| ST-6 | A textbook stochastic detailed-balance model from SFP-2, chosen by the harness. Its Π is produced by a standard SPS mechanism from its own realized dynamics on a symmetric input, and its reference state is reached by relaxation (RECOVERY). ℛ := its FDT or Onsager-regression relation, in (Π, T, ε) variables | S5: CARD-STANDARD (RH-DB, NR-12(b)); ΔF_Π = ΔF_T = 0 |
| ST-7 | A known k-parameter standard model class, with Π and T fixed by a standard rule | NON-COMPRESSIVE against NULL-M; c_J = 0 |
| ST-8 | An order-2 Volterra predictor of a₊₊ from {a₀, a₊, a₋} on HB-2 at small α | STANDARD (STD-14) |
| ST-9 | The Beenakker–Kindermann–Nazarov cascade correction on a standard P-2-type model | STANDARD (STD-7) |
| ST-10 | Credit feasibility (on paper): the maximum b_J for a relation of coupling codimension c on the frozen chart, with N_cred instances and at most 3 lock observables, against a lower bound on the price of the mandatory components in their shortest well-typed L₀ form | The SC1–SC3 thresholds are jointly reachable for some c ≤ 3. Otherwise Appendix A is changed before the freeze |
| ST-11 | Padding control: a known definitional relation (CT-21) conjoined with an arbitrary non-standard restriction on Γ alone | CARD-NONJOINT or CARD-DEFINITIONAL |

---

## 25. Hard stop
- This charter is committed **alone**, with a `pending` CHECKS line.
- No 𝒦 card is generated, frozen, scored or optimized until the owner has reviewed the frozen charter and authorized the harness work order and Card 1.
- After the freeze, the charter changes only under §19.2.

---

## Appendix A: Frozen numbers [P]
The owner may change any value before the freeze, subject to ST-10. No value may change after Card 1 is frozen.

| Symbol | Value |
|---|---|
| p★ | 10 bits; sensitivity reported at 6 and 16 |
| r★ | k = 3 grid times; maximal witness order m = 4; A = {a₀, a₊, a₋}; d_rec = 1 |
| r★★ | k = 4; m = 5 (m★★); A ∪ {a₊₊}; d_rec = 2 |
| Protocol templates | a₀ is null; a± are linear ramps of amplitude ±α starting at t₁; a₊₊ is a ramp of amplitude 2α. α = 1 standard deviation, under a₀, of the driven S variable (never of a record). t₁ := H/4. The template-to-Ξ map is part of Emb |
| Windows W | [−4, 4] for whitened cumulant coordinates; [0, 2] for ε; for scope G, the observable's range over B-HB at Θ_std |
| q (finite record alphabet) | 3, for support-level objects only (B-SEL, HB-12 supports). Binning: tertiles of P_{a₀} from an independent calibration run. ε is always computed on continuous records |
| Certification tolerance | 2^(−p★) |
| r_lock | max(2σ_pre, 2^(−p★)·\|W\|) per observable, frozen in C13 |
| δ_Π / η / δ_∂ | 0.05 / 0.05 / 0.10 |
| H | ≥ max(the protocol and record window, 10·τ_int, 3·τ_slow) |
| Horizon robustness; scale window w | (2η, 2H); w = 2 |
| b_Π (size of 𝒜_Π; selection beyond the ontology price) | 8 bits |
| θ_gen | 0.9 coverage of the AI-3 draws |
| n_min (AI-3 truncation floor) | 6 |
| N_cred (credit instances) | 16 (AI-1 plus 15 Selector draws) |
| N_ch (auditor chart coordinates) | 8 |
| Σ_L₀ | 64 tokens (6 bits each); 4 reserved and unavailable |
| τ_sel | log₂(1 + n_drafts), counted since G2-11; log₂ N_frozen at the pick |
| Compression | ρ ≥ 2; ΔL₀ ≥ p★ at p = 10; ΔL₀ > 0 at p = 16; ΔL ≤ 0 at p = 10 → LOOKUP |
| Coupling | c_J ≥ 1 or κ_J ≥ log₂ Q_min per lock fiber; one codimension = p★ bits |
| Q_min | 10 (3.32 bits) |
| σ_pre | ≤ \|I_K\|/4; realized systematics > 1.25·σ_pre → LOCK-VOID |
| N_max | 10⁹ effective records in total per card; ≤ 30 days of platform time in total |
| α, power | 0.0027; 0.9 |
| Lock thresholds | Falsified above 3σ_eff; confirmed within 2σ_eff, with σ_eff ≤ \|I_K\|/4 |
| Lock observables | ≤ 3 per card |
| In-silico budget | ≤ 10¹⁰ effective samples (evidence grade only) |
| c_dec; ℓ_dec; p_dec | 60 bits; max(½·F_X, c_dec); 0.5 |
| ℓ_tr, b_patch | 32 bits; 4 bits |
| κ; R_item; R_card | 10; 48 core-hours per item; 5000 core-hours per card |
| DIF-6 perturbation | 2^(−p★), relative |
| Default constant range | [10⁻³, 10³], log scale |
| SEL credit | 1 bit per verified distinction; at most 10; enters ρ only |
| Consistency collapse | B-CF* (k ≤ 6; Sherali–Adams ≤ 3; pairwise Boolean combinations); Hamming distance ≤ 1 |
| FORBID truncation check | Levels n, n+1 and 2n |
| Holdouts | ≥ 3 per Stage-3 pool; at Stage 5, ≥ max(2, n_obs), from ≥ 2·max(2, n_obs) candidates |
| LOCK-H pool N_pool | ≥ 5 eligible datasets |
| NR-16 test | One-sided binomial, α = 0.05 |
| Budget; relations | 3 cards, Stages 3–6; ≤ 2 relations per card, one of them primary |
| Transfer | d_B = 0; TG ≥ p★; TG_A ≥ p★; band ≤ ¼ of range; bridge ≥ Q_min× wider |
| HB ranges | β ∈ [0.25, 4]; ω ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8; quantum ≤ 4 sites; quartic λ ∈ [0, 2] |
| Alternate lock platforms | 1 |
| Clocks | T_harness 30 days; D_batch 90 days after harness validation; T_audit 60 days after batch close; T_lock 365 days after G5-LOCK |
| Regime thresholds | Appendix F |

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
| Reserved | — (unavailable to cards) | 4 |

The typing rule for base tokens is in §4.1.

**B.2 Priced vocabulary.**
- **Price:** P_v = max(L_stmt(def_v), ΔF_tgt(v)) (IP-6), with import subtraction and axiom-checklist closure.
- **Canonical definitions and checklists** are encoded in L₀ by the harness before Card 1.
- **Items:**
  - VB-1 metric
  - VB-2 inner product / orthogonality
  - VB-3 finite-dimensional Hilbert space and tensor product
  - VB-4 tensor-product or subsystem factorization, including block-splitting V_Ξ or 𝒳
  - VB-5 quantum correlation set
  - VB-6 GPT cone with order unit
  - VB-7 Born rule
  - VB-8 continuum analysis (ℝ, limits, exp/log), and continuous time or space beyond the declared resolution
  - VB-9 temporal order and time unit, unless earned
  - VB-10 dimension, capacity or any dimension-like parameter, including truncation levels (SD0 CR3)
  - VB-11 energy function / Hamiltonian
  - VB-12 locality graph of a generator
  - VB-13 probability measures, weights or priors on Ξ, unless generated (including base conditional-response tokens applied to Ξ)
  - VB-14 a symmetry group and its action, when not generated
  - VB-15 conserved-quantity declarations
  - VB-16 time-reversal parity / microscopic reversibility
- **Protected items** (cannot be bought; §5.6):
  - VB-17 invariant measure, temperature, Gibbs weight, detailed balance or KMS, and every PS-5 input
  - VB-18 group action on record space
  - VB-19 readout map or class
  - VB-20 partition sorts
  - VB-21 target-level coordinates in clauses
- Supplying or matching VB-5, VB-6 or VB-7 makes every selectivity result RELOCATED.

## Appendix C: Owner decision points before freeze
- **OD-1** The batch-freeze rule. Adopted.
- **OD-2** The theta parity system as a mandatory FORBID. Adopted.
- **OD-3** Cards rejected at intake consume their slot. Adopted.
- **OD-4** The Appendix-A constants, in particular r★★ (d_rec = 2, a₊₊ = 2α), N_cred, c_dec, b_Π, the clocks, and R_item/R_card.
- **OD-5** The reading of 𝒞 is kept neutral.
- **OD-6** d_op for a generated T_Π: a maximal, faithful s_T supplied by the card and run by charter code. This counts as a use of R1, not a modification.
- **OD-7** The closure of 𝒮 includes the fluctuation theorems. v1 extends this to an open floor that is retroactive until banking (§13.4). Adopted.
- **OD-8** UNSCORABLE is final within the route. Adopted.
- **OD-9** R1's 10-item checklist (Appendix G) is the lock-platform certification standard.
- **OD-10** A complete assembled-law audit before the pick, with DISTINCTIVE (P) required.
- **OD-11** No "in-principle" measurability grade.
- **OD-12** Authorization of the §19.3 harness work order, executed by a context that authors no card.
- **OD-13 Credit structure (new).**
  - v1 credits b_J over N_cred Selector-drawn instances, restricted to equations the lock tests, and makes b_meas an SC3 gate.
  - v0 took min(b_struct, b_meas). By C:§0's paper estimate, that caps credit at tens of bits against prices of hundreds, so SC2 was likely unreachable for an honest card.
  - The alternative is to keep v0's min and lower ρ. The owner decides together with ST-10.
- **OD-14** Two relations per card are retained (one primary). The secondary is priced at 1 bit, is Bonferroni-corrected, and can kill the card. Report L proposed exactly one relation.
- **OD-15** Intake runs at batch close, for all cards together.

## Appendix D: Provenance of rule choices
- v0 merged three drafts, keeping the most precise and most conservative rule at each conflict. v0's Appendix D records those 31 choices. They stand except where the Red-team ledger records a change.
- **Changed in v1:**
  - lock credit (OD-13);
  - decoder budget (c_dec floor; NOT-FOUND grading);
  - persistence (both tests; τ_slow);
  - measurability (N_max per card in effective samples, computed by the Evaluator);
  - credit instances (Selector draws; per-instance minimum);
  - intake timing (OD-15);
  - 𝒮 closure (open floor, retroactive until banking).

## Appendix E: Traceability

| Requirement | Where |
|---|---|
| Item 1: baseline spaces 𝒜_Π, 𝒜_T, 𝒜_Γ, with 𝒜_ε as an image | §2, §12, Appendix F |
| Item 2: success criterion (reduction + compression + measurable consequence) | §2.5, §3, §4.5 |
| Item 3: compression and information price | §4, Appendix B |
| Item 4: nonrelocation of carrier, partition, interface class, readout class, Gibbs/FDT structure and target relation | §5 (PS-1 to PS-6, NR-0 to NR-17), PC-6, PC-7 |
| Item 5: at most 3 genuinely distinct cards | §6 |
| Item 6: card contents | §7, §17 |
| Item 7: originality at the assembled-law level | §8, NR-17 |
| Item 8: parameter transfer | §9 |
| Item 9: stopping rule; no staircase | §10, §20 |
| A1: merge = provenance | §11 |
| A2: ε_R derived; definitional relations; joint restriction | §12, Q2, Q5, §2.5 |
| A3: baseline after causality, positivity, KMS/FDT, Onsager and conservation | §13, Q3, NR-12, BP-4, BP-5 |
| A4: response scope | §14 |
| Carrier and readout derived modulo representation; no unique h | §1.3, §1.6, NR-10, C17 |
| No presumed monotone tradeoff | Q11, NR-13, C18 |
| R1's identifying assumption becomes a Stage-3 target | NR-10(h)–(l), DIF-5, DIF-9, MC-6 |
| Environmental identity (NORTH_STAR) | PS-2, DIF-9 |
| Stage 4–6 gates (selectivity, differentiation, nonrelocation; lock; Stage-6 export) | §15.10–§15.12, XS-10 |
| Risk: R1 grows into a prerequisite staircase | §20, PV-3, the §19.3 time box |
| Risk: a card built only from consistency conditions; the undecidability boundary | §15.2, DC-4, DC-5, DC-8, DC-10, CT-44, CT-45 |
| Risk: no named lock target | §3.3, Q12, C8, KP-4 |
| Risk: selectivity checked without a concrete battery | §15.1, §15.2 |
| Killed ideas must not return | §21.2 (behavioural), KU-9, SM-7, T-1, CT-59 |
| FR1–FR15 binding | §21.1, C19 |
| The charter frozen alone; STOP before Card 1 | §19.1, §25 |

## Appendix F: Regime hypotheses: operational surrogates and constraint lists
- Each hypothesis is decided on the realized process, at record level, by its surrogate.
- Defects are normalized to [0, 1]. A hypothesis **holds** unless its certified defect is at least max(2^(−p★), the BP-4 platform threshold 3·r_lock).
- The frozen regime metric for near-regime bounds is given where relevant.
- Fitting β or another regime parameter costs the baseline nothing.
- Each hypothesis imposes on 𝒜_Γ the STD items listed in the last column.

| RH | Surrogate (defect) | Imposes |
|---|---|---|
| RH-HAM | The S+E map at record resolution is deterministic, invertible and measure-preserving | STD-3, STD-6 |
| RH-KMS | Classical: the reference process is time-reversal invariant with declared parities (d_BL between the path law and its reversed image). Quantum: the KMS defect for its certified evolution at an auditor-fitted β. Metric: relative entropy to the nearest KMS state; KMS defect at the fitted β | STD-3, STD-4(b), STD-8, STD-13 |
| RH-MR | Path-reversal invariance with parities and field reversal | STD-4(a) |
| RH-DB | Kolmogorov's cycle criterion on the realized generator (exact on acyclic state graphs); quantum detailed balance with respect to the reference | STD-3, STD-4(a) |
| RH-LDB | Local detailed-balance defect on each transition | Fluctuation theorems and TURs (STD-3) |
| RH-MK | Conditional-independence defect of the records given the present state, at record resolution | STD-3 (NESS forms), STD-7 |
| RH-STAT | Time-shift defect of the reference process | STD-3 (NESS forms), STD-13 |
| RH-GAU | The a₀ records of E are jointly Gaussian, and E's response to S is affine | STD-3 (Gaussian completeness), STD-7, DEF-15; ε^T = 0 for T ⊇ T_caus |
| RH-SYM(G) | Invariance defect of the reference law and the dynamics under G | STD-5; G-covariant baseline |
| RH-CQ, RH-GGE | Conservation defect of the declared charges; GGE fit defect | STD-5; generalized FDT |
| RH-WC | Dimensionless coupling or timescale ratio | STD-7, STD-13, STD-15 |
| RH-LIN | Readout linearity defect and coupling weakness | STD-7 |
| RH-MF, RH-LOC, RH-ERG | A normalized aggregate of n units; finite generator range; decay of the mixing coefficients | STD-9, STD-13 (Lieb–Robinson) |
| RH-AN | An order-m Volterra truncation matches the records to 2^(−p★) at the template amplitudes | STD-14, STD-15 |
| RH-NESS, RH-NEQ | Stationary nonequilibrium Markov; affinity magnitude. Metric: entropy-production rate | STD-3 (NESS forms); near-regime Onsager |
| RH-MC | Finite bath size with a microcanonical reference | Ensemble-equivalence corrections |
| RH-ORD | An order-parameter, critical or pattern-forming signature | STD-10 |
| RH-TH | The macroscopic thermodynamic limit is essential | STD-8 |
| RH-Q | Noncommuting realized observables, or VB-3/VB-5/VB-6/VB-7 present | STD-2 (all of quantum theory and quantum information) |

- An undecidable surrogate means the hypothesis holds (BP-4).
- Hypotheses the auditor adds (§13.4) must come with a surrogate of this form.

## Appendix G: The frozen carrier-certificate checklist (R1 post-result seed, adopted for MC-6)
1. The interface is deterministic, invertible and calibrated. Residual uncalibrated curvature is below the witness: 3σ·|φ″_res/φ′| < |witness| at every operating point.
2. Readout noise is protocol-independent and calibrated. Calibrated nonlinearities are removed on noise-free data or with a noise model (additive noise is a kernel, not a map).
3. There are no random run-to-run interface gains or offsets beyond a calibrated stationary model.
4. There is one fixed time base, sampling grid and trigger phase. There is no protocol-dependent clock jitter, latency, window, or phase of a nonstationary environment.
5. There is one readout channel with fixed weights. There is no push-pull reweighting of environmental sources.
6. Record completeness: the record contains the full support of every interface kernel, past and future, at driver resolution, with every kernel invertible on the record. Injectivity is required into the observed record.
7. There is no outcome-dependent selection: no vetoes, cuts or lock-loss rejection.
8. Only invertible calibrated nonlinearities are present. Saturation, clipping and quantization are excluded unless provably inactive.
9. The protocol acts on the environment only through the system. There is no actuator heating, EMI, vibration or other cross-talk.
10. Estimation is controlled: per-protocol sample sizes are equal or modelled.

---

## Red-team ledger

- Every row is a **CHARTER TEST**: an abstract gaming pattern, never a physical proposal. The rows of Table L1 are CT-60 onward (§24.1).
- Prefixes: D definitional; L relocation; S standard physics; C accounting; M measurability and stopping.
- "Applied" means the fix is in v1. It may have been merged with an overlapping fix from another report, which is then named.

### Table L1: attacks

| ID | Pattern (one line) | Targeted | Fix | Now blocked by |
|---|---|---|---|---|
| D:CT-D01 | X_T reads Γ, so the T_Π–Γ relation is definitional | §1.2 components | Applied (reconstructed): upstream-only reads | PC-6, §5.6, §19.3 |
| D:CT-D02, CT-D05 | Bodies not received by the reviser | — | Not applied, because the content is unknown; the D lens is to be re-run on v1 | FZ-1(d) |
| D:CT-D03 | Disjunctive pin: a union of single-axis restrictions passes the rectangle test | Q5 | Applied: coupling measured on Rect(Im) and Rect(Z_ℛ); one witness is insufficient | Q5, §2.5 |
| D:CT-D04 | Tier-swap rectangle: coupling only via ε's T-argument | Q5 coordinates | Applied: ε is never a coordinate; fixed-T fibers | Q5, DEF-14, §2.5 |
| D:CT-D06 | "Derivable from 𝒮" is only semi-decidable, so the card waits out the search | §13.4 | Applied (reconstructed): constructive-witness rule | Q3(e), §13.4 |
| D:CT-D07 | An invariant but non-maximal s_T reshapes ε | §1.4 | Applied: maximal, faithful s_T, checked by the Recomputer | §1.4, Q8 |
| D:CT-D08 | Protocol-induced maps added to T absorb back-reaction | NR-10, B-NULL | Applied: upstream reads; E-B twin through the components; protocol-uniform moves | PC-6, NR-10(l), §1.6 |
| D:CT-D09 | A static record map on an exogenous family fakes ε > 0 at T_Π | B-REC | Applied: B-REC through the card's static maps, at T_Π | §15.3, DIF-5(e) |
| D:CT-D10 | Response carried by relata that switch sides within tolerance | §1.3, NR-11 | Applied: core-only records (reconstructed); boundary ablation | §1.3, NR-11(b) |
| D:CT-D11 | The card's pipeline makes ℛ★ hold for generic standard models | Q3, BP-1, STD-9 | Applied: transplant test; hand-supplied witnesses insufficient; RH-LOC | Q3(c),(d), STD-9 |
| D:CT-D12(a) | A generic standard identity with one exotic witness | Q3 | Applied: genericity; RH-AN, STD-14 (merged with S:RT-S-12) | Q3(b), STD-14 |
| D:CT-D12(b) | B-SRB starved of the constants' data, or "silent" | BP-5, B-SRB | Applied (merged with S:RT-S-09, C:RT-09, M:RT-01) | BP-5, §15.5 |
| D:CT-D13(a) | Coordinate stretching (log ε, 1/ε) inflates the ratio | FC-1 b_meas | Applied: frozen coordinates; minimum over identity and log | MC-4 |
| D:CT-D13(b) | Observables linked by DEF identities counted as independent | FC-1 | Applied via the joint cell-count b_meas (C:RT-07) instead of an independence test | MC-4, MC-9 |
| D:CT-D13(c) | O predicted from sub-grid or marginal records of the same protocols | MC-2, LT-1 | Applied | DEF-13, LT-1(ii) |
| D:CT-D13(d) | A decorative interface input, so the lock tests a pin | MC-2 | Applied (merged with M:RT-10, C:RT-08) | MC-2 sensitivity |
| D:CT-D13(e) | The platform cut chosen by maximizing a record functional | MC-2 | Applied | MC-2 platform interface |
| D:CT-D14 | Credit obtained by dropping non-standard realizations from Im* | §2.5 | Applied (merged with C:RT-06) | §2.5, §2.3 |
| D:CT-D15 | dim_ub from the rank at a singular point | §2.5 | Applied (merged with S:RT-S-22, M:RT-30) | §2.5 |
| D:CT-D16 | The same structural credit under two relations | FC-1 | Applied: computed once on the conjunction (equivalent to C:RT-02) | FC-1 |
| D:harness | Seven rejection tests before the freeze; priority list 1–6 | §19.3 | Applied (all six priority items are in v1) | §19.3 |
| L:M0 | Coverage rows missing for items 3–8 and A2–A4 | App. E | No change needed: v0's App. E already mapped them (the reviewer saw only the tail); rows expanded | App. E |
| L:§A | Shared instruments NR-D, NR-S, JN, P-rules (i)–(iv), FB | §5, §4, §2 | Applied: NR-D → NR-6; NR-S → NR-5; JN → NR-17; P-rules → IP-5 window, IP-2 D_KL, IP-6 closure, DC-5/IP-6; FB → §2.3 | NR-5, NR-6, NR-17, IP-2, IP-5, IP-6, §2.3 |
| L:RT-1 | Declared, priced supply claimed as generation | FR5 / RULES 1 | Applied | §5.1, FR5 |
| L:RT-2 | Π encoded in an input asymmetry, with the symbol never appearing | Nonrelocation | Applied: full input list; NR-D merged into NR-6; NR-S into NR-5 | NR-5, NR-6, §5.2 |
| L:RT-3 | An ontology with a tiny 𝒜_Π makes selection trivial | 𝒜_Π | Applied: size test; ontology priced | §1.3, IP-14, B-DIF(x) |
| L:RT-4 | Π defined as the extremizer of a response functional | DEF | Applied | PC-6, DEF-17(a) |
| L:RT-5 | ℛ is a separable conjunct of 𝒦 | Originality | Applied: JN | NR-17, OR-2 |
| L:RT-6 | Carrier taken from the chosen representation | NR-10 | Applied | NR-10(h)–(j) |
| L:RT-7 | Protocol-indexed moves; ε ≡ 0 via a huge class | §1.6, GY | Applied | §1.6, §21.2, Q8 |
| L:RT-8 | T_Π equals a built-in symmetry or calibration | NR-10 | Applied | NR-10(k), §1.4 |
| L:RT-9 | Gibbs/FDT reached through a chain of premises | PS-5 | Applied: operational PS-5 | PS-5, NR-12 |
| L:RT-10 | Baseline under-imposed ("FDT" read as linear only) | §13 | Applied (merged with S:RT-S-04, S:RT-S-18) | §13.2–§13.4 |
| L:RT-11 | Reduction only on degenerate, unrealized or pre-excluded sets | §2.5 | Applied | §2.5, Q9 |
| L:RT-12 | Tailored repertoire | Repertoire | Applied | §1.7, Q9 |
| L:RT-13 | Tuned persistence windows; unbounded error terms | §1.3, MC-3 | Applied | §1.3, MC-3 (UNFALSIFIABLE) |
| L:RT-14 | Battery verdicts encoded by the translation layer | §15.1 | (a)–(e) applied. (f) declined: the mandatory FORBIDs already require explicit exclusions, and reduction at the record-law level is SC1's job | §15.1, FC-2, IP-6 |
| L:RT-15 | Decision level chosen per item; undecidable reference objects | §16 | Applied | DC-10, DC-5 |
| L:RT-16 | An identity measure defined from Γ and related to ε | DEF | Applied | PC-6, DEF-17(b),(c) |
| L:RT-17 | Scope switched or mis-declared | §14 | Applied | §14, Q10, RS-5 |
| L:RT-18 | A loose, post-hoc, infeasible or retrodicted lock | LT-1 | Applied, except "exactly one ℛ": at most 2 kept, with a priced secondary that can kill the card | Q12, MC-7, MC-8, OD-14 |
| L:RT-19 | Sectors already linked, or leakage between them | §9 | Applied | XS-2, XS-6 |
| L:RT-20 | A pass resting on unproved or pending premises | §20 | Applied, in M:RT-45's stricter form | NR-15, PV-3, SM-9 |
| L:RT-21 | Budget multiplied by switches, gauges or post-hoc parameters | §6 | Applied | BU-9, IP-9, BU-3, BU-4 |
| L:RT-22 | A killed idea renamed inside a component | §21.2 | Applied: behavioural equivalence | §21.2 |
| L:RT-23 | Record coordinates, witnesses or distance chosen per card | §1.4 | Applied | §1.3, §1.4 |
| S:RT-S-01 | A generated Gibbs/DB premise launders FDT consequences | NR-12(b) | Applied | NR-12(b),(c) |
| S:RT-S-02 | Non-Hamiltonian detailed balance escapes STD-3/4/6 | STD-3, 4, 6 | Applied: RH-DB; rewritten hypotheses | STD-3, STD-4, STD-6, ST-6 |
| S:RT-S-03 | Regime hypotheses declared ill-typed, hence false | BP-4 | Applied | BP-4, App. F |
| S:RT-S-04 | Structural-class theorems outside the closed RH list | §13.4 | Applied: open floor, new RHs, RH-Q | §13.2, §13.4 |
| S:RT-S-05 | Standard-model compression counted as the law's | §4.4 | Applied: NULL-M | §4.4, ST-7 |
| S:RT-S-06 | A generically standard relation, with its codimension coming from elsewhere | §2.5, Q3, Q6 | Applied | §2.5 c_J(c), Q3(b) |
| S:RT-S-07 | Marginal reductions leak into joint credit | ΔF | Applied (merged into b_J); SPS on the realized dynamics | §2.5, §2.3, FC-3 |
| S:RT-S-08 | A persistence statistic tied to response by regression or rates | LT-1, BP-1, Q5 | Applied | §2.2 single model, STD-13 |
| S:RT-S-09 | The baseline lacks the reference correlators | BP-5 | Applied | BP-5 |
| S:RT-S-10 | Escape just outside KMS, at the card's resolution | BP-4 | Applied | BP-4, §13.5, App. F |
| S:RT-S-11 | Saturation of a standard bound credited | §2.5 | Applied | §13.5 boundary rule, Q3(f) |
| S:RT-S-12 | Amplitude or parity interpolation across the templates | §2.3, LT-1 | Applied | STD-14, MC-4, ST-8 |
| S:RT-S-13 | A small T_Π re-exposes linear response under scope Q | §14 | Applied | §14, RS-3, RS-4 |
| S:RT-S-14 | Conditional definitional identities | Q2 | Applied | DEF-15, App. F |
| S:RT-S-15 | Scaling via generated sizes or coupling order | STD-9 | Applied (merged with D:CT-D11) | STD-9, STD-15 |
| S:RT-S-16 | Selection rules from the residual symmetry of a generated Π | STD-5 | Applied | STD-5, §2.3 |
| S:RT-S-17 | Modular / thermal-time KMS tautology | DEF | Applied | DEF-16, NR-12(e) |
| S:RT-S-18 | Gaps in the nonequilibrium FDRs | STD-3, SFP-2 | Applied | STD-3, SFP-2, Q3(f) |
| S:RT-S-19 | Cascade FCS corrections on P-2 | SFP-5, STD-7 | Applied | STD-7, SFP-5, ST-9 |
| S:RT-S-20 | Reciprocity theorems outside Onsager–Casimir | STD-4 | Applied | STD-4(a), SFP-3 |
| S:RT-S-21 | Credit fibers in an FDT-silent regime while the platform is thermal | §1.5 | Applied | §1.5, MC-11 |
| S:RT-S-22 | Rank at a chosen symmetric point | §2.5 | Applied | §2.5 |
| S:RT-S-23 | Frameworks claimed inapplicable to a generated Π | Q3 | Applied | BP-6, Q3(a) |
| S:§3 | New CT rows, ST-6–ST-9, harness patterns | §24, §19.3 | Applied (the CT rows are this ledger) | §24, §19.3 |
| C:§0 | Credit scale unreachable for an honest card, so loopholes pay | FC-1, SC2 | Applied option (a): b_J over N_cred draws, restricted to equations the lock tests; b_meas a gate. Option (b) left to the owner | FC-1, §2.5, ST-10, OD-13 |
| C:RT-01 | Rigidity credited as the relation | FC-1 | Applied | §2.5 b_J |
| C:RT-02 | The same bits counted under two relations | Credited | Applied (D:CT-D16 form) | FC-1 |
| C:RT-03 | Conjunctive padding carries the certificates | Q2, Q3, Q5, Q6 | Applied | Q2, Q3(a), Q5, Q6, ST-11 |
| C:RT-04 | Differentiation bits credited despite FC-3 | ΔF | Applied | FC-3 |
| C:RT-05 | Chart inflation | Chart | Applied (plus D:A-9's auditor coordinates) | §1.5, §2.5 |
| C:RT-06 | Credit from realizations outside the baseline | Im* | Applied | §2.5 |
| C:RT-07 | Lock observables multiplied | b_meas, MC-7 | Applied: joint b_meas; N_max per card. The proposed cap b_meas ≤ structural bits is moot, because b_meas adds no credit | MC-4, MC-7, MC-9 |
| C:RT-08 | A response-only lock with a token interface input | LT-1, MC-2 | Applied as the gate I_int ≥ log₂ Q_min (the cap is moot) | MC-2 |
| C:RT-09 | SRB starved; constants match published platform values | BP-5, IP-11 | Applied | BP-5, IP-11 |
| C:RT-10 | Reparametrized O; I_SRB taken as an outer bound | b_meas, B-SRB | Applied | MC-4, §15.5, App. A |
| C:RT-11 | Two-part code computed on the card's own data | §4.4 | Partly declined: kept as a Stage-3 gate, because NULL-M makes it informative. The code, the null price and single counting are fixed, and a Stage-5 form is added | §4.4, G5-MDL |
| C:RT-12 | Vocabulary leverage measured "alone" | IP-6 | Applied | IP-6 |
| C:RT-13 | Protected structure inside an import | IP-8 | Applied | IP-8 |
| C:RT-14 | Base tokens encode measures or splits | B.1 | Applied | §4.1, App. B |
| C:RT-15 | Vocabulary re-derived in plain L₀ | IP-6 | Applied (merged with L's P-rule (iii)) | IP-6 closure |
| C:RT-16 | Target vocabulary carried in the battery files | Emb | Applied | §15.1 |
| C:RT-17 | Unpriced selection in the implementation | DC-9 | Applied | PC-8 |
| C:RT-18 | A narrow declared range makes constants cheap | IP-5 | Applied (plus M:RT-22) | IP-5 |
| C:RT-19 | Numerological "forced" constants | IP-5 | Applied | IP-5 |
| C:RT-20 | The decoder dodged by small instances | NR-6 | Applied with a 60-bit floor (D:A-10) rather than 24 | NR-6 |
| C:RT-21 | Search kept outside the selection tax | IP-12 | Applied | IP-12 |
| C:RT-22 | Citing a small family lowers the selection price | IP-4 | Applied | IP-4 |
| C:RT-23 | A per-item clause spread onto report items | IP-10 | Applied | IP-10 |
| C:RT-24 | ALLOW anchors credited; D_sel fills the margin | FC-2, §4.5 | Applied | FC-2, §4.5 (ΔL₀) |
| C:RT-25 | Baseline inflated by declarations | §2.3, I_𝒦 | Applied | §2.3, §1.5 |
| C:RT-26 | A coarse, non-separating s_T | §1.4 | Applied | §1.4 |
| C:RT-27 | Cheap exclusion of instances | IP-13 | Applied | IP-13 |
| C:RT-28 | Card-added witnesses inflate dim_lb | B-HB | Applied | §15.4, BP-7 |
| C:RT-29 | The harness written by the future card author | §19.3 | Applied | §19.3, §23 |
| C:§E | Feasibility and padding self-tests | §24.2 | Applied | ST-10, ST-11, FZ-1 |
| M:RT-01 | The prediction avoids FDT inputs, starving the baseline | BP-5 | Applied | BP-5 |
| M:RT-02 | I_SRB wide because of intractability | B-SRB | Applied | §15.5 |
| M:RT-03 | A noise-floor lock with no live rival | MC-4 | Applied | MC-4 |
| M:RT-04 | σ inflated to stay inconclusive | MC-5 | Applied | MC-3, MC-5, T-3(b) |
| M:RT-05 | Self-reported feasibility | MC-7 | Applied | MC-7 |
| M:RT-06 | A one-sided witness lock | MC-1 | Applied | MC-1 |
| M:RT-07 | A knife-edge lock fiber | §1.5 | Applied | §1.5 robustness |
| M:RT-08 | Violations routed to NO RECIPROCITY VERDICT | MC-6 | Applied | MC-6 |
| M:RT-09 | A platform class that cannot be certified | SC3 | Applied | MC-11 |
| M:RT-10 | A token independent input | MC-2 | Applied (merged) | MC-2 |
| M:RT-11 | Postdiction from a known archive | MC-8 | Applied | MC-8 |
| M:RT-12 | A narrow holdout scope; self-chosen replacements | G5-HOLD | Applied. The tolerance is set to the MC-5 thresholds on the holdout's own I_K (one rule) instead of σ_pre + \|I_K\| | G5-HOLD |
| M:RT-13 | Persistence by choice of horizon | §1.3 | Applied | §1.3, DIF-2 |
| M:RT-14 | Kill conditions with no risk | KP | Applied | KP-2′ |
| M:RT-15 | Lock drift between freeze and unsealing | MC-5, G5-LOCK | Applied | MC-5, G5-LOCK |
| M:RT-16 | Hedging across relations and observables | MC-9, MC-10 | Applied | MC-9, MC-10, KU-12 |
| M:RT-17 | The alternate platform used as a second draw | MC-6 | Applied | MC-6 |
| M:RT-18 | Domain carved after the seeds are drawn | DIF-7 | Applied | DIF-7, C16 |
| M:RT-19 | Transfer plan chosen after Stage 5 | BU-3 | Applied | BU-3 |
| M:RT-20 | Undefined lock resolution exploited in both directions | BP-4, Q3 | Applied | r_lock, BP-4, Q3(a) |
| M:RT-21 | A loosening repair informed by drafts | §19.2 | Applied | §19.2 |
| M:RT-22 | The card declares its own constant ranges | IP-5 | Applied | IP-5 |
| M:RT-23 | Flooding the owner with disputes | CV-1 | Applied | CV-7 |
| M:RT-24 | A consistency selector that just misses the collapse test | §15.2 | Applied | §15.2 B-CF* |
| M:RT-25 | A consistency card in disguise | DC-8 | Applied | DC-8 |
| M:RT-26 | A token weight rule | DC-8 | Applied | DC-8 |
| M:RT-27 | Enumeration depth tuned to the battery | DC-1 | Applied | DC-1, SEL-H |
| M:RT-28 | A truncation level used as a size threshold | DC-4 | Applied | DC-4, VB-10 |
| M:RT-29 | An infeasible next truncation level | Ch-4 | Applied | DC-4 |
| M:RT-30 | An unsound dimension certificate | §2.5 | Applied (merged) | §2.5 |
| M:RT-31 | Exactness kept as an option | DC-5 | Applied | DC-5 |
| M:RT-32 | Unbounded declared resources | DC-2 | Applied | DC-2 |
| M:RT-33 | An intractable baseline claimed as maximal | §2.3 | Applied | §2.3, §2.5 |
| M:RT-34 | A transfer that uses no information from A | XS-7 | Applied | XS-7 TG_A |
| M:RT-35 | Battery verdicts used as sector A | XS-1 | Applied | XS-1 |
| M:RT-36 | θ_K both frozen and fitted | XS-5 | Applied | XS-4, XS-5 |
| M:RT-37 | Regime labels assigned by vocabulary | XS-3 | Applied | XS-3 |
| M:RT-38 | A constant tiled across cards | BU-4, BU-7 | Applied | BU-4(e), BU-7′ |
| M:RT-39 | VAR-6 too broad or too narrow | VAR-6 | Applied | VAR-6 |
| M:RT-40 | A template logged as one draft | IP-12 | Applied (merged with C:RT-21) | IP-12 |
| M:RT-41 | Intake used as an oracle | §19.4 | Applied | §18.1, §19.4, OD-15 |
| M:RT-42 | A staircase begun before any failure | §20 | Applied | §20 |
| M:RT-43 | The batch never closes | BU-6 | Applied | BU-6 |
| M:RT-44 | The harness work order grows into foundations work | §19.3 | Applied | §19.3 |
| M:RT-45 | Conditional verdicts make pending items prerequisites | PV-3 | Applied | PV-3 |
| M:RT-46 | Stage 6 unbounded; slots reused there | T-3(c), §15.12 | Applied | T-3(c), §15.12, BU-6 |
| M:RT-47 | Terminals stuck in limbo | OR-6, MC-8, §15.9 | Applied | OR-6, MC-8, §15.9, T-2, T-3 |
| M:RT-48 | The terminal laundered via an early unscorable item | T-1 | Applied | T-1, §21.2 |
| M:RT-49 | Library banking seeds a new route | T-5 | Applied | T-5 |
| M:RT-50 | Tooling repair as a free option | BU-3, §19.2 | Applied | PC-8, §19.2 |

### Table L2: ambiguous or uncomputable clauses (resolutions)

| ID | Clause | Resolution |
|---|---|---|
| D:A-1 | NR-1 scope | NR-1 covers 𝒦, 𝒞, 𝒳, priors and Emb; components fall under PC-6 and PC-7 |
| D:A-2 | §5.6 "content implying ℛ★" versus Q1 | "Supplied" is defined in §5.6 |
| D:A-3 | The E-B twin clause is vacuous or over-broad | NR-10(l), §15.6 |
| D:A-4 | ε among Q5's coordinates | ε is never a coordinate (Q5, DEF-14) |
| D:A-5 | Range of 𝒟 | §2.3 𝒟 |
| D:A-6 | 𝔐_F; "applicable" | Q3(a), BP-6; at least 2 applicable frameworks |
| D:A-7 | How I_SRB is built; what \|·\| means | §15.5; MC-4 cell counts within W |
| D:A-8 | Hostile enlargement cuts both ways | BP-7 |
| D:A-9 | Minimum over an unbounded chart family | §1.5: frozen chart plus N_ch registered coordinates |
| D:A-10 | ℓ_dec smaller than one token | ℓ_dec = max(½F_X, c_dec = 60); RB/SPS uncapped |
| D:A-11 | NR-10(c) has no test | NR-10(c), via the NR-3 W-pipe in Dom_pre^carrier |
| D:A-12 | B-REC "through the card's interface" | §15.3, DIF-5(e) |
| D:A-13 | §4.4 code unspecified | §4.4 |
| D:A-14 | α and t₁ undefined | App. A |
| D:A-15 | Time-indexed versus global Π tests | Both required (§1.3) |
| D:A-16 | NR-7 and NR-16 have no statistic | NR-7, NR-16 |
| D:A-17 | Derivability from 𝒮 is only semi-decidable | Q3(e) |
| D:A-18 | Q1 uses Im* but says "all of Sol" | Im throughout |
| D:A-19 | FC-2 ablation scope | FC-2 (𝒦_∅ and 𝒦_𝒮 on Dom_pre) |
| L:C1 | "Not independently imposed" is open-ended | Open floor, retroactive until banking (§13.4). A closed list with a window closing before Card 1 is declined as less hostile |
| L:C2 | "Nontrivial freedom reduction" | §2.5 (cells; relative interior) |
| L:C3 | Units of "positive compression" | §4.3–§4.5 |
| L:C4 | "Measurable" | MC-7, N_max |
| L:C5 | Persistence timescales; earned time | §1.3; FR7, VB-9 |
| L:C6 | Grading of "generated, not supplied" | NOT FOUND within the hostile window (NR-6, §5.5) |
| L:C7 | Baseline needed before Ξ exists | §1.5: 𝒜_Π on the card's V, with the ontology priced (IP-14) |
| L:C8 | Freedom on the 𝒜_T lattice | Finite 𝒯 ∪ {⊥}; T-term reported only (FC-3) |
| L:C9 | Where KMS and Onsager apply | App. F; NESS forms; near-regime rule |
| L:C10 | Quotient-irreducible relative to which T; Stage-6 export | §14 (T_Π ⊇ E₂±); XS-10 |
| L:C11 | Selectivity wording | §15.1 grades, FC-2 |
| L:C12 | "Genuinely distinct"; "GRUT-specific fit"; "definitional" | BU-4; XS-6; DEF-1 to DEF-17 |
| L:C13 | A kill condition must be able to fire | KP-2, KP-2′ |
| L:C14 | Who picks the comparators | OR-4 floor, plus the §13 floor, plus the ten D5 comparators |
| L:C15 | Undecidability of consistency-only cards | DC-5, DC-10 |
| L:C16 | Originality versus non-independence | OR-2, NR-17 |
| L:C17 | Price of Ξ's type | IP-1, IP-14 |
| L:C18 | ε under an approximate Π | Core-only records; NR-11(b); MC-3 leakage bound |
| L:C19 | Derived carrier versus laboratory carrier | MC-6 certifies the derived carrier |
| L:C20 | Charter constants | CV-6, App. A |
| S:A1 | 𝔐_std is open-ended | §2.2 frozen grammar |
| S:A2 | Level of comparison is contradictory | §1.5; §2.2 θ_dict; NULL-M |
| S:A3 | "Fixes dynamics"; "some m" | §2.3 |
| S:A4 | Lock resolution controlled by the card | r_lock; charter resolution for regimes |
| S:A5 | RH disjunctions; no thresholds | App. F |
| S:A6 | No constraint lists for the RHs | App. F, "Imposes" column |
| S:A7 | STD-3 higher-order wording | STD-3 |
| S:A8 | B-SRB omits SFP-7 | §15.5 |
| S:A9 | dim_ub error | §2.5 |
| S:A10 | "Persistence statistic" undefined | LT-1(i): the chart's interface-side observables |
| S:A11 | §13.5 too narrow | §13.6, §13.8 |
| S:A12 | Converse reading of NR-12(b) | NR-12(b) |
| S:A13 | Generated regime property | BP-3, §13.6 |
| S:A14 | Scope of STD-2's quantum part | STD-2, RH-Q |
| S:A15 | Violation metric for discrete relations | Q3(a): membership change |
| S:A16 | Unbounded I_SRB | Intersected with W (§15.5, MC-4) |
| S:A17 | Timing of additions to 𝒮 | §13.4: retroactive until banking |
| S:A18 | KU-4's tested domains | KU-4 |
| S:A19 | OR-5 banking on inflated S6 | OR-5 (NULL-M, c_J) |
| C:D1 | Chart admissibility; the minimum | §1.5 |
| C:D2 | "Same inputs" across ontologies | θ_dict (§2.2, IP-2) |
| C:D3 | Independent observables, distinct instances, implication | Joint b_meas (MC-4); distinctness (§1.5) |
| C:D4 | Internal contradictions | Im (§2.5); FC-3; FC-4 counts no freedom bits on 𝒜_ε, and b_meas is a gate |
| C:D5 | IP-5 passing window of width 0 | IP-5 (¼\|I_K\|) |
| C:D6 | IP-4 family unbounded; can exceed the MDL bound | Families must be finite (cited or L₀-generated). Charging above L_stmt is kept: it is a deliberate look-elsewhere price |
| C:D7 | NR-6 enumeration infeasible | Exhibited decoders within the hostile window (NR-6) |
| C:D8 | §4.4 terms | §4.4 |
| C:D9 | SRB as inner or outer bound; vector observables; scope-G windows | §15.5, MC-4, App. A |
| C:D10 | Chart for 𝒟 | The frozen chart |
| C:D11 | AI-3 parametrization | §1.5 canonical parametrization; n_min |
| C:D12 | NR-7 draws of function-valued components | NR-7 |
| C:D13 | VAR-1 search | BU-4 VAR-1 |
| C:D14 | Credit at r★ versus r★★ | Ch-1 minimum |
| C:D15 | Price of the FR11 meaning | IP-2 |
| C:D16 | Clause normal form | §4.1 |
| C:D17 | Reserved tokens | Unavailable |
| C:D18 | MC-7 per observable or per card | Per card |
| C:D19 | Arithmetic of p·c in cells | One codimension = p★ bits (§2.5) |
| C:D20 | ΔF_supp baseline | Reported only; 2721 record-law supports |
| C:D21 | Interface-side versus response data | MC-2 platform interface |
| C:D22 | Quantifying over an input list | IP-3 |
| C:D23 | What Emb receives | §15.1 |
| M:H1 | Lock resolution | r_lock (App. A) |
| M:H2 | Consequence of LOCK-INCONCLUSIVE | G5 FAIL (MC-5, T-3) |
| M:H3 | q = 3 alphabet versus GL(k) | ε on continuous records; q for supports; frozen binning |
| M:H4 | t₁; the coordinate for α | App. A |
| M:H5 | ε not exactly computable | §1.4 decision semantics |
| M:H6 | "Independent records" | Effective sample size (MC-7) |
| M:H7 | Chart minimum | §1.5 |
| M:H8 | "Some m"; "the smaller construction" | §2.3 |
| M:H9 | NR-4 quantifier | NR-4 |
| M:H10 | NR-5 limit λ → 0 | NR-5: three values |
| M:H11 | ℓ_dec | NR-6 |
| M:H12 | n_B, F_p undefined | XS-7 |
| M:H13 | LT-1 disjointness with a₀ | §1.7, LT-1(ii) |
| M:H14 | Test object for reciprocity holdouts | §15.9(b) |
| M:H15 | b_struct is not specific to ℛ | b_J (§2.5) |
| M:H16 | Who declares the final count | The owner (BU-6) |
| M:H17 | DIF-6 "ε_C" | Deleted |
| M:H18 | KP-4 "without new theory" | Defined in KP-4 |
| M:H19 | Structural distinctness | §1.5 |
| M:H20 | VAR-1 universe and search | BU-4 |
| M:H21 | Checklist not quoted | App. G |
| M:H22 | No RH thresholds | App. F |
| M:H23 | 𝒮 closure never final | Retroactive until banking. "Freeze at S9" declined as less hostile |
| M:H24 | Unbounded owner discretion | CV-7 |
| M:[P] | New constants needed | All are in App. A |