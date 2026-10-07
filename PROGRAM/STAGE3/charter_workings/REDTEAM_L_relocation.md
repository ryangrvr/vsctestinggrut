# Stage-3 Charter v0: red-team findings (lens: relocation)

**What I received.** The v0 text I was given is only the risk-coverage table: eight rows, starting mid-table with no header row. The clause bodies were not included. That covers §3.3, §15.1–§15.12, §16, §19.1, §20, §21, §25, C8, C19, KP-4, KU-9, SM-1/5/7, CT-44/45/59 and Q12. Under "Slips through", each finding quotes two things word for word:
- the v0 coverage row; and
- the governing text that the cited clause implements (G2-11, STATE, RULES, FR1–FR15).

Each fix is written as a standalone replacement or insert, so it applies whatever v0's exact wording is. Every construction is a **CHARTER TEST**: an abstract gaming pattern, not a physical proposal.

**M0 (coverage gap).** The visible rows do not map these G2-11 items:
- item 3 (compression and information price);
- item 4 (nonrelocation of carrier, readout, Gibbs/FDT structure and target relation);
- item 5 (budget);
- item 7 (originality);
- item 8 (cross-sector);
- additions 2–4 (ε_R derived; baseline after standard theory; response scope).

These are the items most exposed to relocation. If the missing rows cover them, ignore M0. Otherwise:
- **Fix:** add one coverage row for each of G2-11 items 1–9 and additions 1–4. Each row names the clause and the CT that exercises it.

---

## A. Shared instruments (the fixes refer to these; insert them as a new § before §15)

**NR-D (decoder test).**
- **Protected structures** (all six): carrier, Π, [h]_{T_Π}, T_Π, Gibbs/FDT structure, ℛ.
- **Inputs** means every one of these:
  - Ξ-level data, typings, weights and boundary/initial conditions;
  - parameter values and priors/reference measures;
  - the representation/gauge;
  - the protocol repertoire;
  - coarse-graining scales and thresholds;
  - the Ξ→battery translation map;
  - apparatus calibrations.
- A protected structure X is **RELOCATED** if any party exhibits an L₀ decoder of at most ⟨c_dec⟩ bits that computes X from the inputs.
  - The decoder may not invoke the card's selection, fixed-point, solver or evolution step.
  - ⟨c_dec⟩ is a charter constant fixed before Card 1.
- Checking a decoder someone exhibits is a finite task. So NR-D passes means "no decoder exhibited within the hostile-review window". It is graded as NOT FOUND, not IMPOSSIBLE.

**NR-S (symmetrization test).**
- Let G_X be a group of input transformations that preserves the card's stated input class and acts transitively on the admissible alternatives for X (for example, all partitions in 𝒜_Π of the same type).
- Run K on a G_X-invariant input.
- **Generation** requires that K still outputs some persistent X, up to K's own symmetry.
- If X appears only on non-invariant inputs and moves equivariantly with them, the bits that select X were supplied. The generation gate for X fails.

**JN (joint necessity).**
- Consider any L₀ split K ≡ K₁ ∧ K₂, offered by the author or the reviewer.
- If K₂ alone implies ℛ, with Π, T_Π and Γ_Π treated as free variables, and price(K₂) ≤ price(ℛ) + ⟨c_dec⟩, then ℛ is **imposed, not forced**.

**P-rules (pricing; extends §3 compression accounting).**
- **(i) Continuous parameters.** Price = log₂(range/δ). δ is the largest perturbation that leaves every claimed gate verdict and ℛ intact. δ is computed, not declared.
- **(ii) Priors and reference measures on finite spaces.** Price = D_KL(prior ‖ the charter reference measure), in bits.
- **(iii) Vocabulary closure.** Any structure from which a RULES-2 item (Hilbert space, orthogonality, quantum set, GPT cone, Born rule, metric) is L₀-definable within ⟨c_dec⟩ bits is priced as that item. This also covers symmetry groups, quadratic forms and Gaussian reference measures, positivity cones and time-reversal involutions.
- **(iv) Verdict-equivalent pricing.** An item that alone decides a battery distinction or ℛ is priced at the information content of what it decides. Those distinctions are removed from the credit side.

**FB (fibered baseline).**
- B := {(Π, T, Γ) : Π ∈ 𝒜_Π(Ξ), T ∈ 𝒜_T(Π), Γ ∈ 𝒜_Γ(Π)}.
- B is computed after §BASE (RT-10) and after removing the classes killed in GRAVEYARD.
- It includes every type-level dependency of Γ_Π = Obs_Π(Ξ) on Π.
- Freedom reduction is always measured inside B, never against the product 𝒜_Π × 𝒜_T × 𝒜_Γ.

---

## B. Gaming patterns (all CHARTER TESTS)

### RT-1: Priced supply passes as generation
- **Pattern.** The card supplies Π (or T_Π, [h] or the carrier) explicitly and declares and prices it.
  - A bipartition of n units costs about n bits, which is far less than the credited distinctions, so compression stays positive.
  - The card then claims the Stage-4 differentiation gate on the grounds that Π was "declared and priced".
- **Slips through.**
  - C19/§21.1 binds FR5: "No supplied subsystem split without declaring and pricing it."
  - RULES 1: "Commitment ≠ relocation. Postulates are allowed if they are priced."
  - Both sit next to STATE Stage 4 ("a stable approximate partition Π and its T_Π are generated, not supplied") with no stated precedence.
- **Fix (add to §21.1).** "For the six protected structures, pricing never substitutes for generation. A card that supplies any protected structure, at any price, FAILS the corresponding generation and nonrelocation gate. FR5 and RULES 1 govern unprotected inputs only."

### RT-2: The partition is already in the input structure
- **Pattern.** Ξ's input data carries an asymmetry whose induced cut is Π. The asymmetry can be any of:
  - typed nodes or two interaction alphabets;
  - a weighted cut;
  - a boundary or initial condition;
  - a prior concentrated on Π-realizing configurations.

  Any rule that respects the asymmetry then "generates" Π, and the symbol Π never appears in the inputs.
- **Slips through.** STATE: "Nonrelocation: neither Π nor T_Π is encoded in the inputs." G2-11 item 4: "may not be hidden in inputs." As written, both read as syntactic tests (the coverage row "Stage 4–6 gates made concrete | §15.10–§15.12" puts this at §15.12).
- **Fix (§15.12).** "Nonrelocation is operational. Π, [h]_{T_Π}, T_Π and the carrier pass only if they survive NR-D and NR-S, over the full input list in §A. Bits of the inputs that select one of them make its gate FAIL (RT-1)."

### RT-3: An ontology too small to fail
- **Pattern.** Ξ's carrier set or relation type is chosen so that 𝒜_Π(Ξ) contains only one nontrivial persistent candidate, or a handful. "K selects Π" is then forced by the choice of ontology. The reduction log₂|𝒜_Π| is tiny but not zero.
- **Slips through.**
  - STATE: "the solution set is strictly smaller than the unconstrained space."
  - G2-11 item 1: "the ordinary baseline freedom spaces for 𝒜_Π." That baseline depends on the card's own Ξ.
- **Fix (§15.11).** "Differentiation counts only if log₂|𝒜_Π(Ξ)| ≥ ⟨b_Π⟩ on the card's Ξ, and K's selection removes at least ⟨b_Π⟩ bits beyond the price of the Ξ-ontology choice. The ontology choice (the type of Ξ, its alphabet, its arity) is priced under the P-rules."

### RT-4: Π defined as the extremizer of a response functional
- **Pattern.**
  - The generated Π (or T_Π, or the carrier) is defined as the argmin, argmax or fixed point of a functional of Γ_Π or ε_R.
  - Its stationarity condition is then reported as ℛ(Π, Γ_Π) = 0.
  - Any identity–response "tradeoff" is just that first-order condition.
- **Slips through.** Addition 2: "Definitional relations do not count." v0 appears to read "definitional" as covering only the definition of ε_R, not the card's own selection rule.
- **Fix (a new §DEF).** "Definitional relations are:
  - (a) consequences of ε = ε[Γ, T] together with R1's proved properties: Theorems A, A-BL, M1 and F; Prop. E, D1 and D2; rank invariance; and ε ≡ 0 on single-protocol families;
  - (b) the stationarity, fixed-point or extremality conditions of any rule the card uses to define Π, [h], T_Π or the carrier, and every consequence of those conditions;
  - (c) consequences of the card's own definitions of persistence or identity measures.

  ℛ qualifies only if it shrinks FB beyond (a)–(c)."

### RT-5: The target relation is a separable conjunct
- **Pattern.**
  - K = K_diff ∧ K_resp, where K_resp is ℛ, or one L₀ step away from ℛ, written in Ξ-variables.
  - The assembled law looks original. ℛ is cheap, and the card counts it as derived.
- **Slips through.**
  - G2-11 item 7: "novelty is judged only at the assembled-law level."
  - The central task: "makes interface/response structure non-independent."
- **Fix (§16 and the originality clause).** "ℛ is forced only if it survives JN. A card that passes only with ℛ (or an L₀-equivalent within ⟨c_dec⟩ bits) as a separable conjunct is RELOCATED on the target relation. Assembled-level novelty does not override this."

### RT-6: The carrier comes from the chosen representation (instantaneous-state convention)
- **Pattern.**
  - Ξ is written in coordinates that single out an "environment state" variable.
  - The readout is taken as the canonical projection of E's current state.
  - R1's identifying assumption (one common h on the instantaneous state) becomes a gauge artifact that looks derived.
  - But Prop. E, D1 and Remark D3 guarantee that an exact initial-state-latent (E-B) representation always exists. So the tie between E-B and E-C was broken by the card's choice, not derived.
- **Slips through.**
  - G2-11: "derive objective persistent carrier/readout structure rather than supplying it"; "derive physical structure modulo representation."
  - R1_SYNTHESIS §12.5: "Not to be assumed: the carrier; the instantaneous-state choice."
- **Fix (§CAR).** "A carrier derivation must do three things.
  - (i) Output [h] as a class that is invariant under every K-preserving representation move, verified against a declared generating set of such moves.
  - (ii) Name the K-internal property that excludes the D1/D3 E-B representation for this Ξ. That property must survive NR-D: it may not be L₀-equivalent, within ⟨c_dec⟩ bits, to 'the readout is a function of the instantaneous state'.
  - (iii) Derive each item it relies on from the R1 10-item certificate, or mark that item SUPPLIED (gate FAIL per RT-1)."

### RT-7: Representation moves that absorb mode selection, or a class so large that ε_R is always zero
- **Pattern.** The card's "modulo representation" equivalence is gamed in one of two ways.
  - It includes protocol-indexed moves (h_a). MODE SELECTION verdicts then collapse into PASS.
  - Or the class is made large enough that ε_R ≡ 0 on the repertoire, which yields a "forced" relation ε_R = 0.
- **Slips through.** G2-11: "derive physical structure modulo representation." The coverage row "Killed ideas must not return | §21.2, KU-9, SM-7, CT-59" kills the maximal T by name only.
- **Fix (§15.12 and §21.2).** "Representation moves act identically on every protocol in the repertoire; any protocol-indexed move is mode selection (frozen R1 §0). A generated T_Π or [h]-class is the killed maximal-T idea if, on the declared finite projection, it absorbs every family that a GRAVEYARD-killed class absorbs (unrestricted bimeasurable bijections; protocol-dependent linear readouts; a latent-dimension-only constraint). The test is behavioral, not by name."

### RT-8: The interface class equals a symmetry or calibration built into K
- **Pattern.**
  - K is stated with an explicit symmetry group, or T_Π includes "calibrated maps" supplied by the apparatus.
  - The generated T_Π is that group (or the stabilizer of an input structure).
  - It may be chosen to coincide with T_R1 or T_mono so that the card inherits R1's theorems.
- **Slips through.**
  - R1_SYNTHESIS §12.2: "T_Π should be generated by 𝒦's differentiation, not declared."
  - RULES 2 prices "metric" but not groups.
- **Fix.** "T_Π is SUPPLIED if it equals a symmetry group, invariance requirement or calibration map stated in K or its inputs, or is L₀-definable from one within ⟨c_dec⟩ bits.
  - Calibration maps may appear only as an apparatus layer outside T_Π, and ℛ may not depend on them.
  - If a generated T_Π equals T_R1 or T_mono, that equality is a result to be proved. It never imports R1's theorems."

### RT-9: Gibbs/FDT structure reached through a chain of premises
- **Pattern.**
  - The card never states Gibbs, KMS or detailed balance.
  - Instead it supplies premises from which one of them follows by a standard theorem: a conserved quantity plus max-entropy closure; a reversible kernel; ergodicity plus weak coupling; an exponential-family stationary law; a time-reversal involution plus stationarity; or an exponentially weighted reference measure.
  - ε_R then takes its Kubo/FDT value (D5 comparator 1, reverse direction).
- **Slips through.**
  - G2-11 item 4: "Gibbs/FDT structure … may not be hidden in inputs."
  - R1_SYNTHESIS §12.5: the Gibbs/FDT structure is not to be assumed.
- **Fix (define the protected term).** "Gibbs/FDT structure means any input from which one of the following follows by a standard theorem (cited by the author or exhibited by the reviewer): a KMS state; detailed balance or microscopic reversibility; an exponential-family stationary law; canonical typicality; a fluctuation–response identity of any order. Such an input is a protected structure (RT-1)."

### RT-10: The baseline is under-imposed ("FDT" read as linear only)
- **Pattern.** ℛ is presented as holding "where FDT is silent", but it is actually one of these known relations:
  - a nonlinear FDR (Stratonovich, Bochkov–Kuzovlev, Efremov);
  - a nonequilibrium response relation (Agarwal, Harada–Sasa, Baiesi–Maes–Wynants);
  - a fluctuation theorem (Crooks, Jarzynski, Gallavotti–Cohen);
  - a TUR;
  - a Kramers–Kronig relation or sum rule;
  - comparator 1's "leading-order Tier-1 ε_R from undriven 4-point correlations".
- **Slips through.** Addition 3: "computed after imposing causality, positivity, KMS/FDT, Onsager reciprocity, and conservation laws."
- **Fix (§BASE).** "The baseline imposes the closure of:
  - causality, including Kramers–Kronig and sum rules;
  - positivity and complete positivity;
  - no-signalling;
  - KMS and FDT at all orders, including nonlinear FDRs;
  - nonequilibrium response relations, fluctuation theorems and TURs;
  - Onsager–Casimir reciprocity;
  - conservation laws with their Noether and Ward identities;
  - the second law;
  - every relation in D5 §2.3's 'Reverse direction' list.

  During the review window before Card 1, the reviewer may extend this list by exhibiting a published derivation. ℛ loses credit for any part implied by the list."

### RT-11: Baseline inflation, or reduction claimed only on an empty or degenerate region
- **Pattern.**
  - ℛ excludes only configurations that §BASE or GRAVEYARD already exclude.
  - Or it restricts only a measure-zero locus (the ε_R = 0 set, a trivial Π) or a region the card never realizes.
  - Or 𝒜_Γ is taken as a product space, so the fibering of Γ_Π over Π is counted as a reduction.
- **Slips through.**
  - G2-11 item 2: "nontrivial freedom reduction."
  - Addition 2: "must restrict the jointly realized (Π, T_Π, Γ_Π)."
- **Fix (§SUCC-1).** "Freedom reduction is measured inside FB, on the declared finite projection (repertoire, time grid, witness set). Nontrivial means the excluded set:
  - has nonempty relative interior in FB (positive reference measure on discrete parts);
  - intersects {ε_R > 0}; and
  - intersects the region where the card's Π is realized."

### RT-12: The protocol repertoire is tailored
- **Pattern.** The card chooses repertoire A so that ℛ is vacuous or forced:
  - single-protocol or T-coincident protocols (ε_R ≡ 0 by definition);
  - Gaussian or linear protocols only (ε_R cannot see them, so R1-NULL is forced);
  - protocols defined by reference to the intended Π;
  - a subset selected after the fact.
- **Slips through.**
  - The STATE/R1 object definition: "Γ_Π = Obs_Π(Ξ) (family of intervention-conditioned record laws for a protocol repertoire)."
  - G2-11 item 6: "measurable target."
- **Fix (§REP).** "The charter fixes the repertoire as a functor of the generated Π: a declared L₀ protocol type applied to the generated S, not a list.
  - Restricting to a sub-repertoire costs log₂(number of choices) and must be done before evaluation.
  - ℛ qualifies only on repertoires where FB admits ℛ = 0, ℛ ≠ 0, ε_R = 0 and ε_R > 0."

### RT-13: Coarse-graining and persistence windows
- **Pattern.**
  - Persistence time, the approximation tolerance of Π, the battery's support threshold and the scales are all free.
  - Π exists only inside a tuned window.
  - Or ℛ holds "up to O(ε_Π)" with ε_Π unbounded, which makes it unfalsifiable.
- **Slips through.** STATE: "a stable approximate partition Π"; the object definition "persistent, possibly approximate partition."
- **Fix (§PERS).** "Persistence thresholds, tolerances and coarse-graining scales are parameters priced by P-rule (i).
  - Π is persistent only if it is the same up to K's symmetry across a computed scale window of at least ⟨w⟩ and a horizon of at least ⟨h⟩ times K's fastest internal time scale.
  - Every error term entering ℛ must be bounded by K, and the predicted effect must exceed that bound by ⟨r⟩. Otherwise the lock is UNFALSIFIABLE, which counts as FAIL.
  - Battery supports are exact (p > 0)."

### RT-14: The battery's answers are public, and a translation layer encodes them
- **Pattern.**
  - Every B-SEL verdict is in the exact SD0 record.
  - The card supplies a Ξ→support-table map that encodes those verdicts. The map can:
    - reference a cheap priced item (quantum set, GPT cone, operator assignment);
    - use a consistency level tuned between K3 and K4 (the SD0 F1 tuning signal);
    - use scenario or dimension features.
  - Most items are structurally trivial: SD0 T1 says non-strongly-contextual tables are admitted by any rule that respects global sections; SD0 T2 says forbidding strong contextuality is automatic in the pairwise-binary sector.
- **Slips through.**
  - Coverage row: "Risk: selectivity checked without a concrete battery | §15.1 (B-SEL, from the exact SD0 record), §15.2."
  - RULES 2: "Target-encoding vocabulary carries a price."
- **Fix (§15.1).**
  - "(a) The translation map belongs to the card: frozen with it, uniform across items, priced, and free of references to scenario names, party or setting counts, dimensions or individual items (the SD0 §3.3 firewall).
  - (b) Credit is counted modulo implication and modulo T1/T2 structural triviality (SD0 compactness accounting §2). A verdict forced by structure earns zero.
  - (c) P-rule (iv) applies.
  - (d) Every item, including theta parity, gets a verdict. UNDECIDED counts as FAIL.
  - (e) ⟨k⟩ sealed holdouts are chosen after the card is frozen, by a procedure fixed in the charter. Failing any one fails selectivity.
  - (f) Selectivity must also exclude a nonempty-interior subset of FB, not only support tables."

### RT-15: Decision level chosen per item, or undecidable objects used as references
- **Pattern.**
  - K consists only of consistency conditions, and deciding membership is undecidable or very expensive.
  - The level of the decision hierarchy is chosen item by item, UNDECIDED results count as neutral, or the solution set is defined by reference to an undecidable object so that the card inherits its verdicts.
- **Slips through.** Coverage row: "a card built only from consistency conditions; the undecidability boundary | §15.2, §16 (DC-4, DC-5, DC-8), CT-44, CT-45."
- **Fix.** "Each card freezes one sound decision procedure, declared as an outer or inner approximation, with a single level for all items. Its verdicts are the card's verdicts. UNDECIDED means FAIL for gating and zero credit. A solution set defined by reference to an object whose membership cannot be checked in finitely many steps is priced as that object (P-rule iv)."

### RT-16: An "identity" measure defined from response
- **Pattern.** Identity or persistence strength is defined as a functional of Γ_Π, for example cross-cut dependence. The card then reports a relation between that measure and ε_R, but both are functionals of the same Γ.
- **Slips through.** G2-11: "Do not presume any monotonic identity–response tradeoff … sign and functional form must come from the law."
- **Fix.** "Identity and persistence measures are defined from Ξ-level structure without reference to Γ_Π, records or ε_R. A relation between two functionals of Γ_Π qualifies only if FB admits its violation (§DEF (c))."

### RT-17: Switching the response scope
- **Pattern.**
  - The scope is declared after evaluation.
  - Or the scope "response in general" is used so that a Kubo/Onsager restatement counts.
  - Or "quotient-irreducible" is declared while the measured channel is T-explainable.
  - Or a general-scope ℛ has no real dependence on Π or T_Π.
- **Slips through.** Addition 4: "Each target relation declares whether it concerns quotient-irreducible … or response in general."
- **Fix.** "The scope is frozen with the card, one per ℛ.
  - **QI scope:** ℛ is stated through ε_R under the generated T_Π and is invariant when any T_Π-explainable response is added. It must fail when the card's Π is replaced by an arbitrary Π′ ∈ FB.
  - **GEN scope:** §BASE additionally includes full linear-response theory (Kubo, Onsager–Casimir, Kramers–Kronig, the GLE/Zwanzig decomposition). FB must admit a violation of ℛ when Π or T_Π varies with the linear part of Γ held fixed."

### RT-18: A loose, post-hoc, infeasible or retrodicted lock target
- **Pattern.**
  - LT-1 names a family of relations, and the member that fits is picked later.
  - Or it names a value that has already been measured.
  - Or it names a target needing about 10¹¹ samples (D4) — "measurable" only in principle.
  - Or it uses a Gibbs environment, where §BASE already predicts ε_R.
- **Slips through.**
  - Coverage row: "no named lock target | §3.3 (LT-1), Q12, the lock register (C8), KP-4."
  - G2-11 item 2: "measurable consequence."
- **Fix (§3.3 / C8).** "Each card names exactly one ℛ.
  - All constants are fixed by K, or by sector-A data frozen before the card.
  - The estimator, the witness family, the repertoire, the regime and the kill value are frozen.
  - Naming k alternative ℛs costs log₂ k bits and requires a look-elsewhere correction.
  - **Measurable** means the required sample size n*, computed from K's predicted effect in the D4 per-witness form, is at most ⟨N_max⟩.
  - Already-measured values are calibration, not a lock.
  - A lock environment where §BASE predicts the value earns zero."

### RT-19: Cross-sector transfer between sectors that standard theory already links, or with leakage
- **Pattern.**
  - Sectors A and B are already linked by standard theory (for example the two sides of FDT), so the "transfer" is just the standard link.
  - Or sector-A calibration data contains the sector-B observable.
  - Or sector B brings in a "standard" non-GRUT fit, or a new choice of carrier, T, Π, repertoire or units.
- **Slips through.**
  - G2-11 item 8: "without a new GRUT-specific fit."
  - RULES 3: "otherwise independent sectors."
- **Fix.** "Sectors are independent if and only if FB after §BASE admits their joint values as a product.
  - All sector-A quantities are hashed and committed before any sector-B data is read.
  - In sector B, no fitted quantity of any origin may enter beyond apparatus constants measured independently and declared beforehand. The same applies to any new choice of carrier, Π, T_Π, [h], repertoire, coarse-graining, calibration or units."

### RT-20: A staircase built from conditional premises
- **Pattern.**
  - The card's pass rests on a lemma still to be proved.
  - Or on R1's open upgrades (M5, D4, carrier necessity).
  - Or on DERIVED items whose external check is still pending (A-BL, F, M1–M3, Prop. G, C1–C6), treated as established.
  - The missing piece then becomes "what Stage 3b must prove".
- **Slips through.**
  - Coverage row: "R1 grows into a prerequisite staircase | §20 (SM-1, SM-5), the non-blocking items."
  - Addition 1: "Merge = provenance, not endorsement."
- **Fix (§20).** "A premise not proved when the card is frozen counts as SUPPLIED. If it is a protected structure, the gate fails (RT-1).
  - R1 open upgrades and pending-check items may appear only as named conditionals. A verdict that depends on them is CONDITIONAL: it cannot be banked and cannot count as success under the stopping rule.
  - A failure traced to a missing premise ends that card. It does not license a prerequisite study (RULES 4)."

### RT-21: Multiplying the budget
- **Pattern.**
  - One "card" contains a discrete switch among sub-laws.
  - Or a parameter is selected after the gates are seen.
  - Or the same law is resubmitted in a different gauge.
- **Slips through.** G2-11 item 5: "at most three genuinely distinct 𝒦 cards."
- **Fix.** "A card is identified by its frozen text and SHA.
  - A selector among m sub-laws counts as m cards, unless it is chosen and priced before evaluation.
  - Two presentations with identical verdicts on every gate are one card.
  - Any change after evaluation makes a new card that consumes budget."

### RT-22: Killed ideas return under new names
- **Pattern.** A killed idea returns inside a component under a new name. Examples:
  - capacity or dimension counting, rephrased as "number of interface states";
  - "forbid strong contextuality";
  - maximal T;
  - latent-dimension ≤ k.
- **Slips through.** Coverage row: "Killed ideas must not return | §21.2, KU-9, SM-7, CT-59."
- **Fix.** "Behavioral equivalence: if a component reproduces a GRAVEYARD entry's verdict pattern on that entry's finite test domain, it is that entry, whatever its name. The test domains are the SD0 battery for discriminators, and the R1 ladder plus the E1/D1 constructions for T classes."

### RT-23: Record coordinates and witnesses chosen per card
- **Pattern.**
  - The card picks the record embedding in ℝᵏ, the variables and the calibration, so that the generated T_Π is linear in those coordinates.
  - Or it picks witness functions f after seeing the data.
  - Or it uses its own distance or normalization in "ε_R".
- **Slips through.** "ε_R = ε[Γ_Π, T_Π] (frozen R1 definition)." The frozen definition fixes d_op only for T_R1 and T_mono.
- **Fix.** "The record space, its coordinates and its σ-algebra are outputs of the [h]_{T_Π} derivation.
  - ε is the frozen construction: an inf over a shared law of a max over protocols of d_BL, minimized over the orbit of the generated T_Π.
  - No per-card normalization or alternative distance is allowed.
  - Witness families are frozen with the card."

---

## C. Ambiguous or uncomputable clauses

1. **"Not independently imposed by existing frameworks."** This is open-ended and cannot be decided. Replace it with the closed §BASE list plus a reviewer extension window that closes before Card 1.
2. **"Nontrivial freedom reduction."** 𝒜_Γ is infinite-dimensional, and no measure is given on it. Use a finite projection, relative-interior or positive-measure exclusion, and bits at a computed resolution (RT-11).
3. **"Positive compression."** No units or formula are given. State it as: price(K) + price(all inputs), in bits, is less than credited distinctions. Credited distinctions are counted modulo implication, §BASE and structural triviality.
4. **"Measurable."** Is it in principle or feasible? Fix ⟨N_max⟩ (RT-18).
5. **"Persistent / stable / approximate."** There is no time scale or tolerance. Persistence also presupposes a time structure, and FR7 requires that temporality be earned. Price the time structure, or require K to generate it (RT-13).
6. **"Generated, not supplied / not encoded in inputs."** Only the refutation side can be computed (NR-D/NR-S). The grade must read "survived the hostile window", not "proved unencoded".
7. **𝒜_Π and 𝒜_T before Ξ exists.** The baseline depends on the ontology each card picks, which is circular. Compute the baseline per card on that card's Ξ, and price the ontology (RT-3).
8. **What 𝒜_T contains.** The R1 interface classes form a lattice, not a chain: linear and per-time nonlinear classes are incomparable. The freedom measure on a lattice of classes is undefined. Declare a finite class catalogue and count bits.
9. **Where KMS and Onsager apply.** KMS needs a time-translation group and β. Onsager needs time reversal and near-equilibrium conditions. Say what the baseline imposes when neither applies (the nonequilibrium analogues in §BASE). Silence favors the card.
10. **"Quotient-irreducible", relative to which T?** It could be the generated T_Π, or T_R1/T_mono. Stage 6's "same ε_R (same quotient, same distance)" conflicts with a T_Π that K generates and that may differ between sectors. Require T_Π to be invariant across sectors, or declare which T applies.
11. **The selectivity wording.** "Strictly smaller" is met by removing one point, and "indiscriminately" is undefined. Make it quantitative (RT-14(f)).
12. **"Genuinely distinct"** (RT-21), **"GRUT-specific fit"** (RT-19) and **"definitional"** (enumerate as in §DEF).
13. **"Kill condition."** It must be finite, preregistered and actually able to fire on data that could be realized. A kill condition that can never fire makes the card invalid.
14. **"Hostile baseline comparison."** v0 does not say who picks the comparator. Fix a mandatory set: the 10 D5 comparators plus the §BASE list.
15. **Exact law vs decidability.** For consistency-only cards, "K generates Π" may itself be undecidable (RT-15).
16. **Originality vs non-independence.** Item 7 can be read as excusing a separable assembly. State that assembled-level novelty requires the card to survive JN.
17. **The price of Ξ itself.** v0 does not say whether the type of the relational process object is free. If it is free, it becomes the main hiding place. Price it.
18. **ε_R under an approximate Π.** When the cut leaks, record laws depend on the leakage, and ε_R is not well-defined without a bound fixed by K.
19. **The derived carrier vs the laboratory-certified carrier.** A measured lock still needs an apparatus carrier certificate (R1 §7.1, which cannot be tested from records). v0 has no criterion requiring the carrier K derives to match the one the laboratory certifies. Without one, the lock tests a different object.
20. **Charter constants.** ⟨c_dec⟩, ⟨b_Π⟩, ⟨w⟩, ⟨h⟩, ⟨r⟩, ⟨k⟩ and ⟨N_max⟩ must all be fixed at freeze. Otherwise the first card sets them, which is exactly what the owner's "candidate redefines what counts as impressive" concern forbids.