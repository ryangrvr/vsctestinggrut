# STAGE-3 CHARTER: the law cards 𝒦[𝒞, Ξ] = 0 (DRAFT)

**Date:** 2026-10-07 · **Branch:** `grut2-stage3` (equal to `main` after the G2-11 merge) · **R1 boundary:** `dbfd64b`.

**Status: DRAFT, NOT FROZEN.**
- Ruling G2-11 requires this charter to be written before any 𝒦 candidate exists.
- Once the owner approves it, it is committed **alone**. That commit's SHA becomes the **charter SHA**.
- Work then STOPS for owner review before Card 1.
- Under this draft, no card is generated, frozen, scored or optimized.

**Absolute exclusion.**
- This charter proposes no law. It contains no candidate 𝒦, no example 𝒦 and no sketch of one.
- Every construction in §16 is a **CHARTER TEST**: an abstract gaming pattern that the rules must catch. CHARTER TESTS are not physical proposals.
- If a card's law instantiates a CHARTER TEST pattern, the card is presumed to have the classification §16 gives that pattern. The card carries the burden of rebuttal.

**Scope.**
- The charter covers all nine G2-11 charter items and the four G2-11 owner additions.
- The anti-gaming rules are made operational: nonrelocation, distinctness, preregistration, decidability and stopping.
- §20 maps each owner item to the section that covers it.

---

## 0. Sources and naming

**Governing documents.**
- `PROGRAM/OWNER_RULINGS.md` G2-11: the ruling, additions 1–4, and the reconciliation note on 𝒜_ε.
- `PROGRAM/STATE.md`: the Stage 3–6 definitions.
- `PROGRAM/RULES.md`.
- `PROGRAM/NORTH_STAR.md`.
- `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md` §§1–3, 7, 11, 12.
- `PROGRAM/RESULTS/R1/D5_COMPARATOR_AUDIT.md` §§2.3, 3, 6.
- `PROGRAM/SCOREBOARD.md` and `PROGRAM/GRAVEYARD.md`.
- `F0_REQUIREMENTS_CONSOLIDATION_01.md`, the requirements map, at `0a9a941` as cited by the SD0 charter.

**Precedents adopted.**
- `F0_SD0_CHARTER.md`: a charter frozen alone; candidate preregistration; a post-hoc modification makes a new candidate.
- `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`: bit-priced free choices weighed against distinctions; lookup structure is classed RELOCATED.
- `F0_SD0_HOLDOUT_PROTOCOL_01.md`: independent holdout selection after the freeze.
- `F0_SD0_RECON_01.md` and `F0_SD0_RESULT.md`:
  - the exact selectivity battery;
  - ASP's over-allowance of the theta system;
  - the flagged, unaudited decidability caveat.

**Naming.**
- **FR1–FR15** are requirements R1–R15 of the requirements map. They are renamed here only, so they cannot be confused with Stage 2.
- **R1** is the Stage-2 observable and its terminal record.
- **ℛ** is a card's target relation.
- **Card** means one frozen 𝒦 candidate with all §10 contents.
- **GY-n** is a GRAVEYARD entry, numbered in §10.3.
- **Auditor** means an independent agent context that did not author the card being audited (§17).

## 1. Objects (imported, not redefined)

| Symbol | Meaning | Stage-3 status |
|---|---|---|
| Ξ | Relational process object: the ontology a card constrains | The card declares its type in L₀ (§6) |
| 𝒦[𝒞, Ξ] = 0 | The law | The card |
| Sol(𝒦) | {Ξ of the declared type : 𝒦[𝒞, Ξ] = 0} | Derived |
| 𝒞 | The card's declared commitment data. If a card reads 𝒞 as F0's context/compatibility structure, FR11 applies | Input: priced (§6) and audited (§7) |
| Π = (S, E) | Persistent, possibly approximate partition into system and environment | Must be generated |
| [h]_{T_Π} | Readout equivalence class (environment state → record), modulo representation | Must be generated. No unique formula for h is credited |
| T_Π | Interface class | Must be generated |
| Γ_Π = Obs_Π(Ξ) | {P_a : a ∈ A}: the intervention-conditioned record laws for a repertoire A | Must be generated. Never an input (FR13) |
| ε_R = ε[Γ_Π, T_Π] | The frozen R1 functional inf_{P★} max_{a∈A} d_op^{T_Π}(P_a, T_Π·P★) | Derived by definition. Computed by charter tooling, never by card code |
| ℛ | ℛ(Π, T_Π, ε_R, Γ_Π) = 0 | Named in the card and frozen with it |

**Distance rule.**
- For T_Π ∈ {T_R1, T_mono}, d_op is the frozen R1 distance (Tier 1 and Tier 2 respectively).
- For any other generated T_Π, d_op^{T_Π}(P, T_Π·Q) := inf over t ∈ T_Π of d_BL(P, t#Q), using the frozen d_BL and its normalization.
- This applies the R1 functional. It does not modify R1, extend R1's closed ladder (G2-10) or change any banked value. This is owner decision point §19.6.

**Post-result seeds.** D5 classed Z_A and the measurement-invariance framing as RESTATED, and found [h]_T known in nearby form. A card earns nothing by re-presenting them (§4).

## 2. The pipeline and its observable-level interface

**Chain.** 𝒦 → Sol(𝒦) →[X_Π] Π →[X_h] [h]_{T_Π} →[X_T] T_Π →[Obs] Γ_Π →[ε, charter code] ε_R → ℛ.

**Components the card supplies.**
- X_Π: the partition extractor.
- X_h and X_T: the constructions of the readout class and the interface class.
- Obs: the record map.
- Emb: the rule that realizes a battery scenario's ports and repertoire inside Ξ.

**Components the charter supplies.**
- The ε_R implementation (the R1 code).
- The batteries (§8).
- The 𝒮-checker (§3).
- The ablation and representation harness (§7).

**Rules for components.**
- **PC-1 Uniform.** Each component has one definition across all battery items. It may not branch on scenario name, size, party count, setting count, dimension or item identity. This is the SD0 no-lookup rule.
- **PC-2 Priced.** Components are priced exactly like law clauses (§6). Calling a component "extraction, not law" earns no discount.
- **PC-3 Covariant** under the representation moves of §7.4.
- **PC-4 Decidable** within the declared resources (§9).
- **PC-5 Ablatable.** Every component must run unchanged when 𝒦 is replaced by a null law (§7, NR-3).

**The observable level.**
- A battery scenario σ is specified independently of any card, by:
  - a finite port set Ports(σ) of intervention ports and record ports;
  - a repertoire A_σ;
  - a time grid τ_σ, where relevant;
  - a record space Y_σ.
- For each σ, the pipeline emits Im_σ(Sol) ⊆ 𝒜_Π(σ) × 𝒜_T(σ) × 𝒜_Γ(σ).
- All freedom counts, witnesses and gate tests are computed at this level, so they do not depend on the card's ontology.
- In the support scenarios of B-SEL (§8.1), only the Γ axis is scored: the admitted supports or record laws. Π and T are reported there but not scored.

## 3. Baseline freedom spaces (item 1; additions 2 and 3)

### 3.1 The standard constraint set 𝒮

𝒮 is imposed before any freedom is counted. A relation implied by 𝒮 earns no credit.

- **𝒮_caus (causality).**
  - Non-anticipation: for every t in τ_σ, the law of the record up to t depends on the protocol only through the protocol up to t.
  - In support scenarios: possibilistic no-signalling, or no-disturbance.
- **𝒮_pos (positivity).**
  - Each P_a is a probability law: nonnegative and normalized.
  - Every context support in a support table is nonempty.
  - In quantum baseline models, the generating maps are completely positive.
- **𝒮_KMS/FDT.** This applies when a baseline model's undriven environment is thermal:
  - the undriven law is stationary and consistent with KMS/Gibbs;
  - the response of every order to a Hamiltonian perturbation equals its standard expression in equilibrium correlations: linear FDT and Green–Kubo; nonlinear Kubo and Bochkov–Kuzovlev;
  - the standard fluctuation theorems hold for driven protocols.
- **𝒮_Ons (Onsager reciprocity).** Onsager–Casimir symmetry of linear response and transport coefficients, with their time-reversal parities.
- **𝒮_cons (conservation).** Each declared conserved quantity (energy, momentum, charge, probability) balances across S and E.
- **Closure.**
  - 𝒮 includes every relation derivable from the items above by published standard theorems.
  - An auditor who cites such a derivation moves the relation into 𝒮.
  - Disputes go to the owner. Until the owner rules, the stricter reading governs.
- **Precedent, fixed in advance.**
  - BRI1's Tier-1 ε_R value lies in 𝒮. D5 shows it is a Kubo/FDT third-cumulant response fixed by P0's connected 4-point function.
  - So does any relation that expresses ε_R through the same environment's equilibrium correlations.
- **Regime.**
  - Where FDT is silent, 𝒮_KMS/FDT does not apply, for example in an undriven environment that is not thermal. The baseline is correspondingly larger there.
  - Credit is computed separately for each regime.

### 3.2 The three axes and the derived image

For a battery scenario σ:

- **𝒜_Π(σ)** := {(S, E) : S ⊔ E = Ports(σ), S ≠ ∅ ≠ E} ∪ {⊥}, taken modulo the scenario's declared relabelling group.
  - ⊥ means "no persistent partition".
  - Before symmetry reduction, the set has 2^|Ports(σ)| − 1 elements.
- **𝒜_T(σ)** := 𝒯 ∪ {⊥}.
  - 𝒯 = {E₂±, T_caus, T_lin = T_R1, T_mono}, as frozen in `R1_T_LADDER.md`. On the ladder, E₂± ⊂ T_caus ⊂ T_lin.
  - 𝒯 also contains every class a frozen card generates. Such classes are added at evaluation and never removed.
  - Excluded from 𝒯 (GY-11, GY-12):
    - unrestricted bimeasurable bijections;
    - linear readouts from a latent of unrestricted dimension, or with protocol-dependent carriers;
    - "latent dimension ≤ k".
  - The join of T_lin and T_mono may enter 𝒯, but it carries R1's expectation of triviality (R1 §9). A card that generates T_Π ⊇ join must prove that ε_R is nontrivial for it.
- **𝒜_Γ(σ)** := the families {P_a}_{a∈A_σ} on Y_σ that satisfy 𝒮.
- **𝒜_ε(σ)** := {ε[Γ, T] : (Γ, T) ∈ 𝒜_Γ(σ) × 𝒜_T(σ)}.
  - This is an **image, not an axis** (addition 2; reconciliation note).
  - It carries no freedom count.
  - No identity of the map ε earns credit.

### 3.3 The baseline

𝒜^base(σ) := {(Π, T, Γ) ∈ 𝒜_Π × 𝒜_T × 𝒜_Γ : 𝒮 holds and at least one explicit standard model realizes the triple}.

- **Standard model.** A classical Hamiltonian or stochastic model, or a quantum open-system model, in which the following are each chosen independently:
  - the system;
  - the environment;
  - the coupling;
  - the initial state;
  - the readout;
  - the partition;
  - the calibration class.
- Standard physics therefore treats Π, T and the data that generate Γ as independent modelling choices, coupled only through 𝒮.
- **This near-product structure is the null hypothesis Stage 3 must break** ("make interface/response structure non-independent").

### 3.4 Values fixed now

- **(2,2,2) support scenario, possibilistic object:** |𝒜_Γ| = 2961 pNS tables.
  - 1721 are local.
  - 1232 are logically contextual. Of these, 992 have an exact-support probabilistic realization and 240 do not.
  - 8 are strongly contextual; these are exactly the 8 PR boxes.
- **(2,2,2), probabilistic object:** 2721 realizable supports (`F0_SD0_RECON_01.md` §1).
- **Interface catalogue:** |𝒯| = 4 named classes at freeze, so 𝒜_T has 5 elements including ⊥.
- **Everything else:** all other scenario-specific counts are computed by the evaluator with the frozen procedures of §3.5. They are never computed by the card.

### 3.5 How freedom reduction is measured

Let Im*_σ := Im_σ(Sol) ∩ 𝒜^base(σ). A triple in Im_σ(Sol) \ 𝒜^base(σ) is reported as a non-standard realization. Each such triple is a declared prediction and needs its own kill condition.

- **Discrete axes:** ΔF_disc(σ) = log₂|𝒜^base(σ)/~| − log₂|Im*_σ/~| bits.
- **Continuous axes:** ΔF_cont(σ) = the codimension of Im*_σ in 𝒜^base(σ), i.e. the number of independent real equations. It is established by proof, or by an exact rank computation at an explicit point.
- **A reduction is nontrivial** only if all of the following hold:
  - (i) ΔF > 0 on the joint coordinates (§4, L3);
  - (ii) the §4 witnesses exist (L2);
  - (iii) anchors are retained (§8.6). A reduction bought by forbidding established physics earns nothing;
  - (iv) Im_σ(Sol) satisfies 𝒮. The only exception is a declared violation outside 𝒮's established domain, which needs its own kill condition.

## 4. Success criterion and credit tests (item 2)

**Success criterion.**
- A card succeeds only through:
  - **nontrivial freedom reduction** (§3.5);
  - **positive compression** (§6);
  - **a measurable consequence** (L4).
- It succeeds only while it remains admissible (§7, §9, §10).
- **Definitional relations do not count.**

**Credit tests for a target relation ℛ.** A lock requires all of them.

- **L1 Forced.**
  - ℛ = 0 holds on Im(Sol), at DERIVED grade, on the declared scope.
  - Exact computation on every battery item supports it.
  - Evidence-grade forcing earns at most PROVISIONAL status and cannot lock (§14).
- **L2a Not definitional.** After the substitution ε_R := ε[Γ, T], some triple in the unconstrained observable space (before 𝒮 is imposed) violates ℛ.
- **L2b Not implied by standard physics: the standard witness W-std.**
  - An explicit standard model realizes a triple w ∈ 𝒜^base with ℛ(w) ≠ 0.
  - The violation must be larger than the L4 resolution.
  - L2b implies L2a.
- **L2c Not implied by the pipeline: the pipeline witness W-pipe.**
  - Some Ξ of the card's declared type, with Ξ ∉ Sol(𝒦), has a pipeline image that violates ℛ.
  - Without W-pipe, ℛ comes from the extractors, Obs, the type or the representation, not from 𝒦.
- **L3 Joint.**
  - The zero set of ℛ within 𝒜^base must not have the form 𝒜^base ∩ (A′ × B′ × C′) for subsets A′, B′, C′ of the three axes.
  - So ℛ must couple at least two of Π, T_Π and Γ_Π. ε_R counts through its arguments (Γ, T).
  - A restriction on a single axis may count as Stage-4 selectivity, but never as ℛ.
- **L4 Measurable.** The card names:
  - a platform class, a protocol, an estimator, and a sample complexity N(ℛ) ≤ N_max that separates ℛ = 0 from W-std at level α with power 1 − β (§18);
  - an **identification plan**: how Π and T_Π are certified for the test system independently of the records used to test ℛ.
    - A certification that presupposes ℛ is circular and fails L4.
    - R1's identification limit applies: the carrier cannot be tested from records (R1 §3, §7.1).
- **L5 Scope.** A response-scope declaration (§5) and a regime of validity.
- **L6 Not relocated** (§7).
- **L7 Compressive** (§6).

**Not credited** (explicit list).
1. **Identities of ε:**
   - ε_R ≥ 0;
   - ε_R = 0 if and only if the family is T-separable (Theorems A, A-BL, M1);
   - T ⊆ T′ ⇒ ε^{T′} ≤ ε^{T};
   - ε_R ≡ 0 on single-protocol families;
   - invariance under T;
   - the bounds of Theorem F and Prop. G.
2. **Anything in 𝒮**, including:
   - ε_R values predicted by FDT/Kubo;
   - Onsager-symmetric responses;
   - conservation balances.
3. **Relations without a W-pipe**, i.e. produced by the pipeline alone.
4. **Relations among supplied structures**, and relations whose premises include a supplied protected structure (§7.1).
5. **Single-axis restrictions** presented as ℛ.
6. **Existence claims** of the form "ε_R > 0 somewhere". R1 already has BRI1.
7. **Relations whose only test needs more than N_max samples.** BRI1's single-time witness needs about 10¹¹.
8. **Analogy, shared vocabulary and renaming** (RULES 3).
9. **A presumed monotone tradeoff between identity and response.**
   - If ℛ is monotone, its sign and functional form must trace back to 𝒦's clauses through the responsibility map (NR-3).
   - W-pipe must show that the pipeline on its own would also admit the opposite sign.
10. **Novelty of a component, of a representation, or of a name** (§12).
11. **Re-presentation of the post-result seeds:** Z_A, the measurement-invariance framing, and [h]_T in its nearby known forms (D5 §5).
12. **Readings of R1-NULL as "no response".**

## 5. Response scope (addition 4)

At freeze, every ℛ declares exactly one of three scopes.

- **RS-Q: quotient-irreducible back-reaction.**
  - ℛ constrains ε_R, its zero set, or other content that cannot be explained away modulo T_Π (nonlinear or non-Gaussian content).
  - It is measured through ε_R under R1's verdict table:
    - carrier PASS + different orbits → R1-PASS;
    - carrier FAIL + different orbits → MODE SELECTION;
    - carrier UNRESOLVED + different orbits → NO RECIPROCITY VERDICT.
  - It does not cover any response that T_Π explains: mean response of every order, linear back-reaction, and affine or Gaussian change of the latent.
  - A prediction that ε_R = 0 is never a prediction of "no response".
- **RS-G: response in general**, including mean, linear and Gaussian response.
  - It is measured by a declared standard response observable, not by ε_R, because ε_R is blind to linear response.
  - Its W-std must satisfy linear FDT, Green–Kubo and Onsager.
  - Comparators 2 and 3 in the reverse direction (D5 §2.3) are mandatory baselines here. They are the GLE / linear-response route and process-tensor signalling, both of which detect the linear back-reaction that ε_R discards.
- **RS-MIX.** The two parts are declared separately, and each must pass L1–L7 on its own.

**Rules.**
- If no scope is declared, the card is INADMISSIBLE.
- Changing the declaration after freeze makes a new card.
- Testing an RS-Q relation with linear-response data is void.
- An RS-G relation stated through ε_R is reclassified as RS-Q. Credit is then limited to its quotient-irreducible part.
- The card states which carrier verdict it expects at the measurement, and how that verdict will be certified.

## 6. Compression accounting and information price (item 3)

This procedure extends `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`. It is frozen with the charter and may not change after any card SHA exists.

### 6.1 Base language and priced vocabulary

- **L₀:** finite sets, maps, interventions, conditional response, composition and logic (RULES 2).
- **Priced vocabulary.** These are allowed, but they carry a price, and import subtraction applies (P5):
  - from RULES 2: Hilbert space, orthogonality, quantum set, GPT cone, Born rule, metric;
  - added for Stage 3:
    - inner products;
    - probability measures or priors on Ξ;
    - continuous time or space beyond the declared finite resolution;
    - any dimension-like structure (SD0 CR3);
    - symmetry groups that 𝒦 does not generate;
    - microscopic reversibility.
- **Protected structures (§7.1) cannot be bought.**
  - Supplying one openly is a COMMITMENT. The gate that structure belongs to then fails.
  - Supplying one covertly is RELOCATED.

### 6.2 Free choices F

Every row is listed together with its information content. The rows are:
- the law clauses, counted as structural selections;
- constants and discrete parameters;
- thresholds and tolerances (η, H, resolutions);
- selected invariants;
- categorical branches;
- the declaration of Ξ's type (sorts, arities, labels);
- imports of priced vocabulary;
- the pipeline components: X_Π, X_h, X_T, Obs and Emb;
- priors and measures;
- truncation levels (§9);
- representation moves declared beyond RM1–RM5;
- declared scope exclusions.

Choices forced by FR1–FR15 or by this charter's firewalls are listed separately as constraints and carry no price.

### 6.3 Pricing rules

- **P1 Selection.**
  - Choosing one item from a family of m alternatives costs log₂ m bits.
  - m is the **largest natural family an auditor exhibits** (hostile family size).
  - The card may argue for a smaller family by citing the published family it actually chose from.
- **P2 Real constants.**
  - A real constant costs log₂(range/δ). δ is the coarsest resolution at which no credited verdict or prediction changes; it is set by sensitivity.
  - A value forced by other priced choices costs nothing.
- **P3 Tables.** Every row counts. A symbol that encodes a table costs as much as the table.
- **P4 Item-specific structure.** A constant or clause whose effect is confined to one battery item counts as a table row. The distinction it produces is removed from D.
- **P5 Imports.**
  - An import costs its selection price: P1 applied over the alternative structures of its kind.
  - **Import subtraction:** delete 𝒦's clauses; every distinction the import still reproduces on the battery is removed from D.
- **P6 Pipeline components** are priced as clauses (PC-2).

### 6.4 Distinctions D

- **D_sel.**
  - One distinction for each mandatory B-SEL verdict class the card reproduces (§8.1), up to a maximum of 10.
  - Removed from D_sel:
    - distinctions logically implied by other counted distinctions together with background facts that do not depend on the card; the implication must be argued explicitly;
    - distinctions removed by import subtraction or by P4;
    - distinctions that collapse to a bounded consistency level (§8.7, G-SEL(d)).
- **D_lock.**
  - Each ℛ that passes L1–L6 earns c·b_res bits.
  - c is the codimension of ℛ.
  - b_res = log₂(range of the constrained quantity over 𝒜^base ÷ its resolution at N_max).
  - Credit therefore cannot exceed what can be measured.
- **D_diff = 0**, unless a generated Π is checked against an independently established fact.
- **Holdout and generalization results** are tallied separately and are not part of D.

### 6.5 The test

G := I(D) − I(F).

| Condition | Classification |
|---|---|
| G ≤ 0 | **LOOKUP.** Classed RELOCATED, whatever the gate results (SD0 rule) |
| G > 0 and I(F) > ½·I(D) | **MARGINAL.** The owner rules |
| I(F) ≤ ½·I(D) | **COMPRESSIVE** |

The full F/D table is exposed for hostile review. Any price the auditor raises governs until the owner rules.

## 7. Nonrelocation (item 4)

### 7.1 Protected structures

The following may not be hidden in inputs, parameters, priors, the choice of battery, or the choice of representation:
1. **The carrier (environmental identity).** This includes which state variable counts as "the environment": the instantaneous or the initial state (R1 Remark D3). NORTH_STAR requires that 𝒦 generate stable subsystem identity, then a stable interface carrier, then T, then ε_R.
2. **The partition Π.**
3. **The interface class T_Π.**
4. **The readout class [h].**
5. **Gibbs/FDT structure** supplied as an input: Gibbs or KMS states, temperature, FDT, detailed balance, Onsager symmetry.
6. **The target relation ℛ.**

Also protected:
- R1's calibration data: the BRI1 grid, the protocols and the calibrated maps (R1 §12 item 5).
- Memory, viscoelasticity and crystalline order. Per STATE these are not inputs; they are checked as effective regimes after Stage 4.
- Any monotone tradeoff between identity and response.

### 7.2 Input inventory

The card lists every input item I_j, in these classes:
- clauses;
- constants in 𝒞;
- the type of Ξ and its representation;
- pipeline components;
- priors and measures;
- Emb;
- truncation levels;
- scope declarations.

The card does not choose battery items or repertoires (§8).

### 7.3 Auditor tests

Each test has a finite procedure and a fixed outcome.

| Test | Procedure | Outcome if it fires |
|---|---|---|
| **NR-0 Inventory** | The evaluator reproduces every verdict from the listed inputs alone. The reference implementation may read nothing else: no files, no embedded data, no literals | An undeclared input → RELOCATED |
| **NR-1 Vocabulary firewall** (syntactic) | Unfold all frozen definitions. No clause of 𝒦 may then contain a protected symbol, or an L₀ term definitionally equal to one. Protected symbols: Π, S/E labels, h, [h], T, Γ, Obs, ε, P★, d_op, carrier, Gibbs, KMS, temperature, FDT, Onsager, ℛ | Declared openly → that structure is a COMMITMENT and its gate FAILS. Found by audit → RELOCATED |
| **NR-2 Two-witness** | For each generated X ∈ {Π, [h], T_Π, carrier, Gibbs/FDT if claimed, ℛ}, find a W-pipe: some Ξ ∉ Sol of the declared type whose pipeline output lacks X or yields a different X. For ℛ, a W-std is also required | No W-pipe → X RELOCATED (into the type, the pipeline or the representation) |
| **NR-3 Law ablation** | Run the pipeline with 𝒦 replaced by 𝒦_∅ (type only), then by 𝒦_𝒮 (type plus 𝒮), then with single clauses deleted. This yields the **responsibility map**: which clauses each X and each credited claim depend on | X appears under 𝒦_∅ → RELOCATED. X appears under 𝒦_𝒮 but not under 𝒦_∅ → STANDARD-IMPLIED |
| **NR-4 Decoder** | For each input item I_j and protected X: can a uniform decoder of price ≤ ℓ_dec reconstruct X from I_j alone, on every battery item where X is claimed? Typical hits: sort labels aligned with S/E; constants with block structure; a repertoire that changes the readout; a prior of Gibbs form | A decoder exists → X RELOCATED in I_j |
| **NR-5 Representation** | Apply RM1–RM5 and the card's declared moves, with seeds committed after the card is frozen. Outputs must transform covariantly | A non-covariant X → INVALID (a representation artifact). X moved by a declared gauge move → RELOCATED in the representation |
| **NR-6 Prior ablation** | If the card uses a measure μ on Ξ, run (a) with the law removed and μ kept, and (b) with μ replaced by the charter's reference measure (uniform on the declared finite truncation) and the law kept | X appears under (a) → RELOCATED in the prior. X disappears under (b) → RELOCATED in the prior |
| **NR-7 Battery independence** | Score the sealed holdouts and the B-DIF instances the evaluator generates (§8) | A holdout failure on a mandatory-type item → the gate FAILS. A systematic pattern of passing public items but failing holdouts → BATTERY-TUNED, reported as RELOCATED |
| **NR-8 Carrier discrimination** (the Prop. E test) | For every family the card reads as reciprocity (ε_R > 0), show two things: (i) 𝒦 itself excludes, or classifies as a non-solution, the exact product-latent mode-selection representation of the same family (D5 Theorem D1); (ii) the environment state variable is an output of the law | If the carrier verdict comes from a pipeline choice that would equally certify the D1 representation → carrier RELOCATED, and those families get NO RECIPROCITY VERDICT |
| **NR-9 Audit of Gibbs/FDT premises** | List every premise of each credited derivation | A Gibbs, KMS, FDT, detailed-balance or Onsager premise that 𝒦 does not generate (with a W-pipe) → the claim is STANDARD-IMPLIED. Such a premise hidden in the inputs → RELOCATED |
| **NR-10 Target firewall** | Up to RM moves and definitional unfolding, ℛ may not be a clause, a conjunct of a clause, or a consequence of the clauses that mention only observable-level or pipeline terms. At freeze, ℛ is entered in the **lock register** | Firing → RELOCATED. Any later change of target makes a new card |
| **NR-11 Calibration independence** | T_Π and [h] are computed without R1's calibration data | Using the BRI1 grid, protocols or calibration constants as law inputs → RELOCATED |

### 7.4 Representation moves (FR1)

- **RM1** Relabel the elements of finite sets.
- **RM2** Relabel outcomes, interventions and ports.
- **RM3** Reparametrize continuous parameters by declared bijections.
- **RM4** Use an equivalent presentation of the conditional-response kernels (one that induces the same laws).
- **RM5** Re-bracket compositions.

A card's declared moves must include RM1–RM5. Any additional move is priced (§6.2). Only the declared moves count (FR1).

### 7.5 Outcome classes

| Class | Meaning | Consequence |
|---|---|---|
| CLEAN | No NR test fires | None |
| COMMITMENT-DECLARED | A protected structure is supplied openly | The gate for that structure fails |
| STANDARD-IMPLIED | The claim follows from 𝒮 | The claim is not credited |
| RELOCATED | A protected structure is hidden | The card is dead. After external check, a GRAVEYARD line reads "RELOCATED in ⟨input⟩" |

## 8. Frozen batteries and gate specifications (Stage 4 and the Stage-5 lock)

**General rules.**
- The batteries are frozen with the charter. Cards may not add, remove or reweight items.
- At freeze, a card may declare non-mandatory items OUT. OUT items earn nothing.
- Public items are development data, and cards may be designed with them in view. That is why:
  - public items earn credit in D only under §6.4;
  - sealed holdouts and seeds fixed after the freeze exist.

### 8.1 B-SEL: the selectivity battery (exact; SD0 code and instances)

| Item | Instance | Required verdict |
|---|---|---|
| B-SEL-1 | (2,2,2) pNS landscape, 2961 tables | ADMIT all 1721 local tables. ADMIT the plain Hardy class. FORBID all 8 PR boxes |
| B-SEL-2 | The 240 pNS tables with no exact-support probabilistic realization | The card declares its object. An object at record level (Γ_Π) must FORBID all 240. Admitting any of them is an internal inconsistency → FAIL |
| B-SEL-3 | GHZ (3,2,2) | ADMIT |
| B-SEL-4 | Peres–Mermin square | ADMIT |
| B-SEL-5 | Bipartite 3×3 CHTW KS-game support (SD0's certified core of 94 rays and 67 triads) | ADMIT |
| B-SEL-6 | SD-K7(i): the finite qubit-side family (SD0 frozen instance, `f0_sd0_evaluate.py`) | FORBID |
| B-SEL-7 | SD-K8: the capacity pair, qubit versus boxworld gbit, both of capacity 2 | Exclude the gbit's realization of PR. The responsibility map may contain no clause on capacity, dimension or party count (GY-4, GY-5) |
| B-SEL-8 | The theta parity system: {p,q,r} even, {p,q,s} even, {r,s} odd. It is strongly contextual and has no operator model (J = e) | FORBID (owner decision point §19.2) |
| B-SEL-9 | Other SD0 super-quantum items: strong XOR-(2,3,2) (480/480), embedded PR, fine-grained PR, PR⊗PR, Specker triangle, chained-PR 6-cycle | Scored. Each admission is recorded as an over-allowance |
| B-SEL-10 | SD0 items G1–G3 and H1–H4, now public (H1 is the C7 odd-cycle box) | Scored against their SD0 literature classifications, as development items |

### 8.2 B-REC: the reciprocity calibration battery

These are exact-identity controls, not credit items. Each R1 record below is fed through the card's Γ_Π interface into the charter's ε code. The result must reproduce the R1 value (RULES 6 exact-identity control):
- **BRI1 X1:** the sign structure of Theorem C, and the two-protocol identity ε_R = ½·d_q (Theorem F);
- **the harmonic bath:** ε_R = 0;
- **C2-G and C2-NG:** 0;
- **C2-F:** zero under the calibrated filters;
- **E2:** ε_R > 0 with no response. The card's pipeline must never return R1-PASS here;
- **M-A and C2-F′:** D5 evidence grade, labelled as such.

For each configuration, the card also reports whether it lies in Im(Sol) and what its ℛ value is. These are reports, not anchors (§8.6).

### 8.3 B-DIF: the differentiation battery

The evaluator generates these instances from the card's declared type of Ξ, using seeds committed after the card is frozen:
- **(i) Null-witness search.** This feeds NR-2.
- **(ii) A symmetric instance**, with a transitive automorphism group. This tests covariance: any Π found must be reported as an orbit, not as a labelled choice.
- **(iii) A planted, decoupled instance.** This is a sanity check on the extractor and earns no credit.
- **(iv) Horizon extension.** At H → 2H with tolerance 2η, the extracted Π must be the same.
- **(v) Random solution instances** at the declared truncation.

### 8.4 B-STD: the standard-witness library

- **Frozen content:** the R1 control models of §8.2, in their standard-model forms, each with a verified 𝒮 status.
- **Card additions:** cards may add witnesses. Each added witness is checked independently for 𝒮-admissibility and for realization by a standard model.
- **No evaluator discretion:** the evaluator adds nothing to the library.

### 8.5 Sealed holdouts

`F0_SD0_HOLDOUT_PROTOCOL_01.md` applies, with these adaptations:
- **Pool, by sector.** Support-level cases whose classification is established in the literature, and standard-model environments with computable ε_R.
- **Exclusions.** Everything listed in §8.1–8.4.
- **Size.** At least 3 holdouts per sector.
- **Selector.** An independent selector, invoked only after the card SHA exists. The selector sees only the protocol and the card's bare input/output signature.
- **Timing.** The selection is committed before evaluation. The card is immutable throughout.

### 8.6 Anchors

- **Mandatory ADMIT anchors:**
  - from B-SEL-1, the local tables and the Hardy class;
  - B-SEL-3, B-SEL-4 and B-SEL-5.
- **Standard-regime anchor.** For every B-REC scenario within the card's declared scope, Im(Sol) must contain at least one triple realized by an experimentally established standard regime, i.e. equilibrium FDT and Onsager behaviour.
- **Consequences:**
  - forbidding an anchor is a FAIL;
  - **freedom reduction obtained by forbidding anchors, or by emptying Sol, earns nothing.**

### 8.7 Gates (frozen now: Stage 4 per STATE, and the Stage-5 forcing test)

**G-SEL: selectivity.** The gate PASSES if and only if:
- (a) Im(Sol) is a strict subset of the unconstrained space on B-SEL;
- (b) every mandatory verdict is correct;
- (c) the responsibility map for the B-SEL-6 and B-SEL-7 distinctions contains no clause on capacity, dimension or party count.

Two further rules apply:
- (d) **Consistency-collapse test.** Suppose the FORBID set on B-SEL equals the set refutable by k-consistency for some k ≤ 3. Then the gate may still pass, but D_sel = 0, because the result is a known sector (bounded-width CSP; GY-6).
- (e) The list of over-allowances is reported.

**G-DIF: differentiation.** The gate PASSES if and only if both of the following hold.

Π is:
- **P-a persistent:** the assignment stays constant over the horizon H, up to a reassigned fraction η;
- **P-b nontrivial:** Π ≠ ⊥, and Γ_Π is non-constant across A;
- **P-c universal:** it holds over all of Sol(𝒦), or over an explicitly priced sub-condition. It may never rest on "generic" under an unpriced measure;
- **P-d covariant** (NR-5);
- **P-e generated** (NR-1, NR-2, NR-3).

T_Π and [h] are:
- **T-1 uniform;**
- **T-2 nontrivial:**
  - some B-REC or B-DIF family has ε_R^{T_Π} > 0, and some has ε_R^{T_Π} = 0;
  - T_Π is not one of the GY-11 or GY-12 classes;
- **T-3 carrier-discriminating** (NR-8);
- **T-4 environmental identity is an output:** the identity across interventions, and the environment's state variable;
- **T-5 calibration-independent** (NR-11);
- **T-6 placed** relative to T_R1, T_mono and their join;
- **defined modulo representation:** every claim holds for every representative of [h].

**G-NR: nonrelocation.** The gate PASSES if and only if:
- every NR test is CLEAN for Π, T_Π, [h] and the carrier; and
- no credited claim is RELOCATED.

Gibbs/FDT structure declared as a COMMITMENT is allowed only if no credited claim depends on it.

**G-LOCK: Stage-5 forcing.**
- ℛ passes L1 at DERIVED grade, and L2–L7.
- A sealed holdout or experiment is then preregistered from the L4 plan before any test data are seen.

## 9. Decidability and scorability

- **DC-1 Total procedures.** Every predicate that a gate evaluates on a battery item needs:
  - a frozen reference decision procedure; and
  - a termination argument: a proof, or a finite bound on an enumeration.
- **DC-2 Resources.**
  - At freeze, the card declares the time and memory each item needs.
  - The evaluator allows κ times that amount.
  - An item that exceeds it is UNSCORABLE.
- **DC-3 Exactness.**
  - Zero tests, equalities and membership tests that involve real numbers must be decided either in exact arithmetic (ℚ, algebraic numbers) or by certified intervals separated from the decision boundary.
  - A tolerance-based "≈ 0" is UNSCORABLE, unless the tolerance is part of the frozen law. In that case it is priced and checked for robustness.
- **DC-4 Unbounded quantifiers.**
  - A clause may quantify over unbounded structures: all dimensions, all extensions, all n, all finite-dimensional representations.
  - Such a clause must come with a frozen finite truncation level.
  - That level is part of the law, is priced (§6.2), and is what gets scored.
  - Claims about the limit carry no credit.
- **DC-5 One-sided decidability.**
  - If ADMIT or FORBID is only semi-decidable, any item that does not terminate is UNSCORABLE.
  - The SD0 record flags, without having audited it, that exact quantum support families may be undecidable (Slofstra).
- **DC-6 Gate semantics.**
  - A gate is PASS only if every mandatory item is scored and passes.
  - A mandatory item that is UNSCORABLE makes the gate UNSCORABLE. That gate has **not passed**.
  - An UNSCORABLE card cannot advance, and it counts as a budget failure.
  - Its GRAVEYARD line reads "UNSCORABLE AT FROZEN BATTERY", not "refuted" (NOT FOUND ≠ IMPOSSIBLE).
- **DC-7 No pending status.** Within this route, an UNSCORABLE verdict is never reopened. Later tooling, a larger κ or a lower truncation level does not reopen it; a lower truncation level would in any case make a new card.
- **DC-8 Cards built only from consistency conditions.**
  - A card whose clauses are all consistency or compatibility conditions is flagged at intake.
  - To earn D_sel, it must pass G-SEL(d).
  - To claim differentiation, it must satisfy FR8: a veto does not generate Π.

## 10. Required card contents (item 6), FR standing and GRAVEYARD standing

### 10.1 Contents

A card that lacks any of these items is INADMISSIBLE at intake.

| # | Content |
|---|---|
| C1 | **Identity:** card number, slot and SHA. Also the nearest earlier card, and the argument that this card is not a variant of it (§11.3) |
| C2 | **The exact law** 𝒦[𝒞, Ξ] = 0 in L₀: the type of Ξ, every quantifier explicit, the normalized skeleton, the truncation levels, and a frozen reference implementation |
| C3 | **Information price:** the full F table (§6.2–6.3), with hostile family sizes |
| C4 | **Generated structures:** Π (with η and H), [h]_{T_Π}, T_Π, Γ_Π = Obs_Π(Ξ) and Emb. For each one: its derivation from 𝒦, its responsibility map, and its grade (DERIVED, evidence, or conjectured) |
| C5 | **Measurable target:** ℛ as entered in the lock register; its axes and the L3 argument that it is joint; W-std and W-pipe; the L4 protocol, estimator and N(ℛ); the identification plan |
| C6 | **Response scope:** RS-Q, RS-G or RS-MIX (§5) |
| C7 | **Hostile baseline comparison:** the attempted derivation of ℛ from 𝒮 and why it fails; the comparator floor (§12.3); the conjunction test (§12.2) |
| C8 | **Kill conditions** (§10.4) |
| C9 | **Battery predictions:** a verdict for every public item. Mandatory items may not be declared OUT |
| C10 | **Input inventory and NR self-declaration** (§7.2), with the expected outcome of each NR test |
| C11 | **Decidability declaration** (§9): procedures, resources and termination arguments |
| C12 | **Standing on FR1–FR15** (§10.2) |
| C13 | **Standing on the GRAVEYARD** (§10.3) |
| C14 | **Sector and transfer plan** (§13): which parameters are fixed in which sector, and what they predict in which other sector. Declared at Stage 3 but not scored |
| C15 | **Representation:** the declared moves and the covariance argument. No unique formula for h |
| C16 | **Tradeoff declaration:** whether any monotone relation between identity and response appears, and if so its derivation from 𝒦 (§4, not-credited item 9) |

### 10.2 Standing on FR1–FR15

Each FR receives exactly one of these standings:
- **SATISFIED**, with its argument;
- **SCOPED-OUT**, declared and priced, with its consequence stated;
- **N/A**, with a reason the auditor may contest;
- **VIOLATED.**

| FR | What it means in Stage 3 | A violation is |
|---|---|---|
| FR1 | Covariance under the declared moves, and only those (§7.4) | INVALID |
| FR2 | Any gluing of contexts or subsystems is an explicit act of the law | INADMISSIBLE |
| FR3 | No data from contexts or protocols outside the repertoire, i.e. no counterfactual records | INADMISSIBLE |
| FR4 | Π and [h] are not relative to an observer. Modal or counterfactual framing does not count | G-DIF FAIL |
| FR5 | No supplied split. In Stage 3, even a declared split fails G-DIF | G-DIF FAIL if declared; RELOCATED if hidden |
| FR6 | The scope of compatibility is declared in Emb | INADMISSIBLE |
| FR7 | Persistence and causality use time. Time must be declared either primitive (and priced) or earned | INADMISSIBLE if undeclared |
| FR8 | Constraint ≠ selection. A forced Π must hold on all of Sol, not merely survive a veto | G-DIF FAIL |
| FR9 | No upgrade of quantum-status labels from outer to exact. An outer approximation is labelled as one | Correction required before scoring |
| FR10 | Every input is priced | RELOCATED |
| FR11 | A 𝒞 read as compatibility declares its meaning and pays its price. Gate F0-PHYS-OPEN-02 applies | INADMISSIBLE |
| FR12 | The convention fixes are adopted or declared | Correction required |
| FR13 | Γ_Π is built from Ξ. Reading "Γ as an empirical model" makes Γ supplied | G-DIF and G-NR FAIL |
| FR14 | Any dependence on possibility facts in constructor-theory style is declared | INADMISSIBLE if hidden |
| FR15 | The card declares where it lands: support determination, within-support selection, or the p = 0 boundary | INADMISSIBLE |

### 10.3 Standing on the GRAVEYARD

| GY | Killed idea |
|---|---|
| GY-1 | Restatement as constructor theory |
| GY-2 | "Forbid strong contextuality" |
| GY-3 | "Bipartite ≥ 3 settings" |
| GY-4 | Counting capacity or dimension |
| GY-5 | Counting parties |
| GY-6 | ASP as a new generative support law (banked only as a known sector, SCOREBOARD #6) |
| GY-7 | Pairwise or sub-cover locality, single-context deletion, cohomology/AvN classes |
| GY-8 | Support determination as a standalone line |
| GY-9 | A distinctive payoff from the bridge or scouts at their premise envelopes |
| GY-10 | The selector campaign at the current screen |
| GY-11 | The "maximal" T read literally |
| GY-12 | "Latent dimension ≤ k" |

For each entry, the card declares one of:
- **NOT USED;**
- **COMPARATOR ONLY;**
- **COMPONENT:** priced, with every distinction it alone produces removed from D;
- **RESEMBLES:** with an argument that distinguishes the card from it.

**Return test.**
- A killed idea "returns" when both of the following hold:
  - a credited claim's responsibility map contains a component equivalent to a GY entry, under the V1/V2 relations of §11.3; and
  - the claim vanishes when that component is ablated.
- A claim in which a killed idea returns is not credited.
- If every credited claim fails the return test, the card is INADMISSIBLE.
- GY-10 reopens only with "a new named candidate". A card that is a selector must say so and is audited against GY-10's screen.

### 10.4 Kill conditions

- **K-1 Finite and decidable** on the frozen battery, or a named experimental outcome.
- **K-2 Reachable:** some 𝒮-admissible outcome would trigger it. A vacuous kill condition makes the card INADMISSIBLE.
- **K-3 Automatic:** no reinterpretation after the fact.
- **K-4 Coverage:** at least one kill condition on B-SEL or B-DIF, and at least one on the lock target ℛ.

## 11. Budget, genuinely distinct cards, freezing and preregistration (item 5)

### 11.1 Budget

- **This generative route has at most three cards, across Stages 3–6.**
- A slot is **consumed when the card is committed**.
  - Withdrawing a card after commit does not refund its slot.
  - A card rejected at intake, as INADMISSIBLE or VARIANT, still consumes its slot (owner decision point §19.3).
- Stage 6 requires the same 𝒦, unmodified. Modifying 𝒦 at any later stage makes a new card, which needs an unused slot.

### 11.2 Any modification makes a new card

Any change after freeze to any of the following makes a new card:
- the statement, the constants, or the type of Ξ;
- the pipeline components, the truncation levels, or the tolerances;
- the scope, the response-scope declaration, or the kill conditions;
- ℛ;
- the battery predictions.

**The only exception is a tooling repair** that realigns code to the frozen statement. It is logged, its diff is reviewed, and it changes no statement (SD0 precedent).

### 11.3 The variant relation

Card B is a **VARIANT** of an earlier card A, and is rejected at intake, if any of the following holds:
- **V1 Representation.** A translation built from RM1–RM5, variable renaming and reparametrization of constants, priced at most ℓ_tr, maps Sol(A) onto Sol(B) on the whole battery universe.
- **V2 Constants.** A and B have the same normalized skeleton (constants replaced by placeholders, names canonicalized, logic normalized) and differ only in constant values.
- **V3 Patch.** B keeps every other normalized clause of A and differs from it in exactly one of these ways:
  - (a) one clause is added;
  - (b) one clause is deleted;
  - (c) one conjunct or disjunct is added to or removed from one clause;
  - (d) one clause is changed by a V1 or V2 move.

  Also a patch: B = A ∧ Q, where Q's only effect on the battery is to change verdicts on items where A failed.
- **V4 Scope.** B is A with a changed scope, battery exclusion, extractor, tolerance, truncation level, or response-scope declaration.
- **V5 Combination.** B is a conjunction or disjunction of earlier cards, or of their clause sets.
- **V6 Composite.** B is obtained from A by any composition of V1–V5.

**Procedure.**
- The author names the nearest earlier card and gives the argument that B is not a variant of it (C1).
- The intake auditor rules.
- Disputes go to the owner. Until the owner rules, the card counts as a VARIANT.

### 11.4 Freezing and preregistration, in sequence

1. **Charter freeze.** The charter is frozen alone. The owner then reviews it and authorizes Card 1.
2. **Card freeze.**
   - Each card is committed as one artifact, with its reference implementation and all of C1–C16.
   - This includes every battery prediction.
   - It all happens **before any evaluation of that card**.
3. **Batch-freeze rule** (recommended; §19.1).
   - No card is scored on B-SEL, B-DIF, B-REC, the holdouts or the lock until one of two things has happened:
     - every card the route will submit has been frozen; or
     - the route has declared its final card count (at most 3).
   - Intake audits are static, and may run card by card. They cover:
     - completeness;
     - NR-0, NR-1 and NR-10;
     - the variant check;
     - standing on the GRAVEYARD and on FR1–FR15;
     - the decidability declaration.
4. **Checkpoint (d)** (RULES). The cards and their intake audits are reported, and the owner picks one.
5. **Holdout selection.** Holdouts are selected after the freeze (§8.5), and the selection is committed.
6. **Stage-4 evaluation.**
   - The independent evaluator scores the picked card.
   - The evaluation produces machine-readable outputs, generated tables, the exact-identity controls and a CHECKS line.
   - If the picked card fails, the owner may advance another frozen card.
   - No card may be added beyond the budget.
7. **Checkpoint (e)** after each gate result.
8. **Stage 5.** The lock test, then the preregistered sealed holdout or experiment.

This sequence follows the short ladder of RULES 4:
- conjecture (the card);
- derivation (C4);
- hostile control (the gates);
- holdout (§8.5);
- extension (Stage 6);
- then KILL, BANK or EXTEND.

### 11.5 Information hygiene

- Card authors never see the sealed holdouts or the B-DIF seeds before freezing their card.
- Under the batch-freeze rule, they also never see other cards' gate scores.

## 12. Originality (item 7)

### 12.1 The rule

Familiar component theories are allowed and expected. **Novelty is judged only at the level of the assembled law.**

Not credited:
- the novelty of a component, a name, a notation or a representation;
- relations that follow from the standard conjunction of the component theories.

### 12.2 The conjunction test

- Suppose a card is assembled from components C₁ … C_m.
- The conjunction C₁ ∧ … ∧ C_m, each component as standardly stated, together with 𝒮, is a mandatory comparator.
- If ℛ follows from that conjunction without the card's coupling clauses (located by NR-3), ℛ is not novel.

### 12.3 The comparator floor

The auditor may add comparators, but none may be removed. Literature is verified against primary sources (RULES 5). Otherwise the citation is labelled UNVERIFIED and cannot support a verdict on its own.

- **Response theory:**
  - Kubo linear and nonlinear response;
  - FDT and Green–Kubo;
  - Bochkov–Kuzovlev and the fluctuation theorems;
  - Onsager–Casimir;
  - Ford–Kac–Mazur / Zwanzig (the GLE).
- **The ten D5 comparators.**
- **The readout class:**
  - measurement invariance;
  - Stevens scale types;
  - IRT linking and equating;
  - interventional-CRL identifiability classes (R1 §12 item 1).
- **Differentiation and subsystem emergence:**
  - einselection and pointer states;
  - quantum Darwinism;
  - selection of tensor-product structure;
  - Markov blankets;
  - coarse-graining and causal emergence;
  - spontaneous symmetry breaking and order parameters;
  - renormalization;
  - baselines from planted-partition and community detection.
- **Selectivity:**
  - the Abramsky–Brandenburger hierarchy;
  - KS sets;
  - Local Orthogonality;
  - the Hardy, CDP and Masanes–Müller reconstructions;
  - the JGBB polygon geometries;
  - bounded-width CSP and operator assignment (Atserias–Kolaitis–Severini; Bulatov–Živný);
  - Slofstra.
- **Constructor theory** (GY-1).

### 12.4 Preregistered categories

- Mathematics (M) and physical interpretation (P) are classified separately (D5 precedent).
- Each comparator gets at least one skeptic instructed to argue RESTATED.

| Category | Meaning |
|---|---|
| **RESTATED** | Up to representation, the image of Sol equals an existing framework's image. No new relation |
| **KNOWN ASSEMBLY** | The combination already exists in the literature |
| **STANDARD COMPONENTS, NEW ASSEMBLY, NO NEW RELATION** | Every credited relation follows from the conjunction test or from the comparators |
| **DISTINCTIVE** | ℛ is forced and passes L1–L7, and neither any comparator nor the conjunction imposes it |

- **Only a DISTINCTIVE (P) classification of ℛ counts toward G-LOCK.**
- The middle categories may be banked as a COMPRESSIVE known or assembled sector, as ASP was. They do not make a law.
- No category is favoured in advance.

## 13. The cross-sector gold standard: parameter transfer (item 8)

**Definition.** CROSS-SECTOR means that quantities fixed in sector A predict sector B **without a new fit specific to GRUT** (RULES 3; G2-11 item 8).

**The test.**
- **PT-1 Independence witness.** Two standard models agree on every sector-A observable but differ on the sector-B target. This shows that A and B are otherwise independent.
- **PT-2 Freeze in A.** The card's parameters θ are fixed from sector-A data only, by a procedure frozen before any B data are seen.
- **PT-3 No new fit.**
  - The B prediction uses θ and introduces no new GRUT parameter.
  - Standard nuisance parameters on the B side are fixed only by declared B calibration data that are independent of the predicted quantity.
- **PT-4 Preregistration.** A numeric prediction, with an uncertainty band, is preregistered before the B data are opened.
- **PT-5 Sharpness.** The band is no wider than a fraction ρ of the target's range over 𝒜^base.
- **PT-6 Not credited:**
  - shared vocabulary, analogy, dimensional analysis and unit conventions;
  - the same functional form with a refitted constant;
  - links that standard physics already supplies within a sector. FDT linking fluctuation and response is **not** cross-sector;
  - in the gravitational export, local back-reaction used as the predicted quantity. It is calibration only (STATE, Stage 6).

**Stage 6, fixed now.**
- The same 𝒦, unmodified.
- ε_R is exported with the same quotient and the same distance used at the lock.
- Any change makes a new card (§11.1).

## 14. Verdicts and terminals

**Verdicts on a card.**
- INADMISSIBLE (at intake).
- VARIANT.
- RELOCATED.
- UNSCORABLE.
- FAIL-⟨G-SEL | G-DIF | G-NR | G-LOCK⟩.
- STANDARD-IMPLIED or DEFINITIONAL, assigned claim by claim.
- RESTATED.
- PROVISIONAL: forcing shown only at evidence grade. A PROVISIONAL card cannot lock.
- LOCK-ELIGIBLE.
- Then either LOCKED, or KILLED-AT-HOLDOUT/EXPERIMENT.

**Mapping to the scoreboard** (RULES status vocabulary):

| Card verdict | Scoreboard status |
|---|---|
| RELOCATED | RELOCATED |
| RESTATED | RESTATED |
| Structures declared as a COMMITMENT | COMMITMENT |
| A compressive known or assembled sector | COMPRESSIVE |
| ℛ with L1 at DERIVED grade | DERIVED |
| ℛ confirmed | PREDICTIVE |
| Passes §13 | CROSS-SECTOR |

Nothing is banked before an external check (RULES 8).

**Terminals of the route.** Exactly one applies.
- **S3-LOCK-ELIGIBLE.**
  - A frozen card passes G-SEL, G-DIF, G-NR and G-LOCK.
  - The sealed holdout or experiment follows.
  - If the card is killed there and frozen cards remain, the owner may advance another one. Otherwise the route ends in S3-TERMINATED.
- **S3-TERMINATED.** The budget is exhausted and no card is LOCK-ELIGIBLE.
- **S3-OWNER-HALT.**

## 15. The stopping rule and forbidden staircase moves (item 9)

**The rule.**
- If the authorized budget of three cards fails to produce a law that meets the frozen gates, **this generative route terminates**.
- After external check, the failures are recorded in the GRAVEYARD, and the stage stops (RULES 4).

**The staircase test.** A proposed work item is a **forbidden staircase move** if both of the following hold:
- (i) it is motivated by a card failure, a gate failure or a missing input; **and**
- (ii) what it delivers is an ingredient for a future card, rather than a card, a gate result or a terminal record.

**Explicitly forbidden**, both before and after termination:
- **SM-1** A campaign to derive a "missing ingredient" as a precondition for a card. Examples: a theory of the carrier, a representation theory of Ξ, a partition principle, an interface-class principle, a theory of decidability.
- **SM-2** A re-chartering or "repair" that changes a gate, a battery, the baseline, a pricing rule or a constant so that a failed card would pass.
  - A repair never changes a verdict that has already been computed.
  - After any card is frozen, repairs may only make the rules stricter, and only by owner ruling.
- **SM-3** Declaring a failed card "partially successful" and opening an extension stage for it.
- **SM-4** Budget laundering: splitting one law across several cards, or submitting uncounted "proto-laws", "lemma cards" or "pre-cards".
- **SM-5** Reopening R1. This includes:
  - adding new interface classes;
  - reinterpreting WO-002;
  - making any of M5, D4, carrier necessity or join triviality a prerequisite of a card or a gate.

  These R1 upgrades continue as non-blocking work (G2-11). Their results cannot reopen this route.
- **SM-6** Treating UNSCORABLE as "pending better tools" (DC-7).
- **SM-7** Mining GRAVEYARD entries for "repaired" candidates (see the return test, §10.3).
- **SM-8** Opening a new generative route by any means other than an owner ruling. That ruling must:
  - name it as a **new route**, with its own charter;
  - give it no inherited budget;
  - not frame it as a prerequisite for, or a continuation of, this route.

**Permitted after termination:**
- banking a COMPRESSIVE known or assembled sector;
- writing GRAVEYARD lines;
- writing the terminal report;
- continuing R1's non-blocking upgrades.

## 16. CHARTER TESTS (abstract gaming patterns, not proposals)

**CHARTER TEST: not a law, not a proposal.** Every row below is abstract.
- Before freeze, an auditor confirms that the cited rules catch each row.
- A row that no rule catches is a charter defect and must be fixed before freeze.

| ID | Abstract gaming pattern | Caught by | Classification |
|---|---|---|---|
| CT-1 | The sorts or labels of Ξ's type have classes that coincide with S/E | NR-4; NR-2 (no W-pipe); NR-5 | RELOCATED (in the representation) |
| CT-2 | A clause asserts a bipartition with a persistence or decoupling property | NR-1 | COMMITMENT, so G-DIF FAILS |
| CT-3 | A table of constants whose block or zero pattern is Π | NR-4; P3 | RELOCATED (in the parameters) |
| CT-4 | Obs is defined with one shared readout by construction, so the carrier is certified for every Ξ | NR-2; NR-3; NR-8 | Carrier RELOCATED; NO RECIPROCITY VERDICT |
| CT-5 | T_Π is picked from 𝒯 by a selector clause instead of being constructed from Sol | T-1; T-6; P1 | Supplied, so G-DIF FAILS |
| CT-6 | A prior over Ξ of Gibbs or maximum-entropy form, which produces thermal structure | NR-6; NR-9 | RELOCATED (in the prior) |
| CT-7 | ℛ is Kubo, FDT or Bochkov–Kuzovlev rewritten in ε_R variables | L2b; NR-9 | STANDARD-IMPLIED |
| CT-8 | ℛ is monotonicity of ε in T, or ε = 0 on single protocols, or a Theorem F bound | L2a | DEFINITIONAL |
| CT-9 | A constant whose effect is confined to one battery item | P4; holdouts | LOOKUP, hence RELOCATED |
| CT-10 | A repertoire or Emb under which the protocols change the readout | NR-4; NR-8; R1 verdict table | MODE SELECTION, not reciprocity |
| CT-11 | Card k+1 is Card k with renamed symbols or rescaled constants | V1; V2 | VARIANT; the slot is consumed |
| CT-12 | Card k+1 is Card k ∧ (a constraint excluding the items k failed) | V3 | VARIANT |
| CT-13 | Membership quantifies over all finite-dimensional extensions, with no truncation | DC-4; DC-5 | UNSCORABLE |
| CT-14 | Forcing is claimed from numerics with a tolerance | L1; DC-3 | PROVISIONAL; cannot lock |
| CT-15 | Items or the response scope are declared OUT after results are seen | §11.2; §5 | New card, or VARIANT |
| CT-16 | A lock target that needs more than N_max samples | L4 | Not measurable; no lock |
| CT-17 | A monotone identity–response tradeoff written into a clause | NR-1; not-credited item 9 | Not credited; COMMITMENT |
| CT-18 | An extractor threshold tuned so that Π appears only on Sol | P-c; B-DIF(iv); P2; NR-2 | RELOCATED (in the pipeline) |
| CT-19 | Target vocabulary (a tensor-product structure, a lattice of subspaces) encoded as an isomorphic L₀ table to avoid its price | P3; NR-4; import subtraction | Priced in full; RELOCATED if Π can be decoded from it |
| CT-20 | Two failed cards conjoined and presented as a "new" card | V5 | VARIANT |
| CT-21 | Holdouts selected before the freeze, or by an agent that has seen the mechanism | §8.5; §11.5 | The evaluation is void; holdouts are reselected |
| CT-22 | A weak set of comparators | The §12.3 floor; auditor additions | Comparator audit incomplete, so no DISTINCTIVE |
| CT-23 | A "transfer" in which the B-side nuisance fit absorbs the prediction | PT-3; PT-4 | Not CROSS-SECTOR |
| CT-24 | T_Π ⊇ the join of T_lin and T_mono, or an unrestricted class | T-2; GY-11 | ε_R trivial, so G-DIF FAILS |
| CT-25 | Π depends on a chosen basis or coordinate system | NR-5 | INVALID |
| CT-26 | A law of the form "there exists a structure X with property P", with X to be supplied later | C2; DC-1; SM-1 | INADMISSIBLE; a staircase move |
| CT-27 | The identification plan certifies Π or T_Π by using ℛ | L4 | Circular, so L4 FAILS |
| CT-28 | Freedom reduction obtained by forbidding anchors or by emptying Sol | §8.6; §3.5(iii) | No credit; FAIL |

## 17. Governance

**Roles.** No agent context both authors and audits the same card.
- **Author:** the builder, Claude Code.
- **Intake auditor:** independent and hostile.
- **Evaluator:** independent. Runs the reference implementations and the charter tooling, writes machine-readable outputs, and generates the tables.
- **Holdout selector:** independent, with access to the card's signature only.
- **Comparator panel:** analysts plus skeptics.
- **External checkers:** via `CHECKS.md`.
- **Owner:** issues rulings.

**Hostile default.** Until the owner rules on a dispute, the stricter reading governs.

**A merge is provenance, not endorsement (addition 1).**
- Merging charter, card or result commits changes no status. CHECKS lines stay pending until they are checked, and nothing is banked before then (RULES 8).
- Some R1 items are still pending external check: A-BL, F, M1–M3, Prop. G, and the D5 analyses C1–C6.
  - A card may cite them only with that label.
  - Claims that depend on them inherit "pending".
  - Gate verdicts that depend on them are PROVISIONAL.

**Repairs.** Repairs are numbered CR-n and require owner approval. Each comes with a diff and a list of the cards it affects. They are restricted as SM-2 states.

**Records.**
- Each card, intake audit and gate result gets a CHECKS line once it is verified on the remote.
- Checkpoint reports are five lines or fewer.
- The numerics pipeline follows RULES 6, with at least one exact-identity control (§8.2).

## 18. Charter constants

These are defaults. The owner may change them before freeze; after freeze they cannot change.

| Constant | Default | Where used |
|---|---|---|
| Budget | 3 cards per route, across Stages 3–6 | §11.1 |
| η_max | 0.1 (fraction of elements reassigned) | P-a |
| H_min | 10·τ_int, where τ_int is the card's declared shortest internal time scale (priced) | P-a; FR7 |
| Robustness window | (2η, 2H) | B-DIF(iv) |
| N_max | 10⁹ independent records | L4; D_lock |
| α and 1 − β | 0.01 and 0.9 | L4 |
| ℓ_dec | min(32 bits, ¼ of the bits the card claims for X) | NR-4 |
| ℓ_tr | 32 bits | V1 |
| κ | 10 | DC-2 |
| Compression bands | G ≤ 0 → LOOKUP; I(F) > ½·I(D) → MARGINAL | §6.5 |
| Consistency-collapse levels | k ≤ 3 | G-SEL(d) |
| Holdouts | At least 3 per sector | §8.5 |
| ρ (PT-5) | ¼ | §13 |

## 19. Owner decision points (before freeze)

1. **The batch-freeze rule** (§11.4, step 3). Recommended. The alternative, sequential evaluation, lets later cards be tuned to earlier results, with only V3 to catch it.
2. **The theta parity system.** Either a mandatory FORBID, or scored only. Mandatory FORBID is recommended; otherwise a card can reproduce ASP's known over-allowance at no cost.
3. **Whether a card rejected at intake as VARIANT or INADMISSIBLE consumes its slot.** Recommended: yes.
4. **The numeric constants of §18.**
5. **The reading of 𝒞** (§1). The draft keeps it neutral.
6. **The d_op rule for a generated T_Π outside the frozen tiers** (§1). Confirm that it is a use of R1, not a modification.
7. **Whether the closure of 𝒮 includes the fluctuation theorems.** Recommended: yes.
8. **DC-7:** UNSCORABLE is final within the route.

## 20. Traceability

| Requirement | Where it is covered |
|---|---|
| G2-11 item 1: baseline spaces 𝒜_Π, 𝒜_T, 𝒜_ε, 𝒜_Γ | §3 |
| Item 2: success criterion | §4 |
| Item 3: compression and information price | §6 |
| Item 4: nonrelocation | §7 |
| Item 5: a budget of three distinct cards | §11 |
| Item 6: card contents | §10 |
| Item 7: originality | §12 |
| Item 8: parameter transfer | §13 |
| Item 9: stopping rule | §15 |
| Addition 1: merge = provenance | §17 |
| Addition 2: ε_R derived; definitional relations; joint restriction | §1; §3.2; §4 (L2a, L3) |
| Addition 3: baseline computed after 𝒮 | §3.1; §4 (L2b); NR-9 |
| Addition 4: response scope | §5 |
| Derive [h] modulo representation | §1; G-DIF; C15 |
| No presumed monotone tradeoff | §4 (item 9); C16; CT-17 |
| R1's identifying assumption becomes a Stage-3 target | NR-8; T-3; T-4 |
| Environmental identity (NORTH_STAR) | §7.1; T-4 |
| Risk: R1 grows into a staircase | SM-5 |
| Risk: cards built only from consistency conditions, and undecidability | §9 (DC-4, DC-5, DC-8); G-SEL(d) |
| Risk: no named lock target | C5; NR-10 lock register; K-4 |
| Risk: selectivity checked without a battery | §8.1 |

## 21. Hard stop

- This charter is committed alone.
- No 𝒦 card is generated, frozen, scored or optimized until the owner has reviewed the frozen charter and authorized Card 1.
- After freeze, the charter changes only by numbered repair, under §17 and SM-2.