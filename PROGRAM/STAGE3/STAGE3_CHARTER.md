# GRUT 2 — STAGE-3 CHARTER: rules for judging 𝒦 cards (frozen alone)

**Date:** 2026-10-07 · **Branch:** `grut2-stage3`, based on `main` at the G2-11 merge
`86bf5a0` · **R1 terminal boundary:** `dbfd64b` · **Governing ruling:** G2-11 (ruling
block, additions 1–4, and the reconciliation note on 𝒜_ε) · **Working record:**
`PROGRAM/STAGE3/charter_workings/` (non-normative; §0.5).

> **Status: CHARTER FROZEN ALONE.**
> - This file contains **no candidate law**. No 𝒦 is proposed, sketched, named,
>   exemplified or optimized here. Every construction in §24 is an abstract gaming
>   pattern labelled **CHARTER TEST**; the self-tests use only known textbook objects.
> - **STOP for owner review before Card 1** (G2-11). No card is drafted, frozen,
>   scored or optimized, and the evaluation kit of §19.3 is not built, until the owner
>   has reviewed this charter.
> - The freeze commit contains no 𝒦 card, draft, candidate or kit artifact.
> - Nothing here is banked. After the freeze commit is pushed and verified on the remote,
>   a separate commit adds its `pending` line to `PROGRAM/CHECKS.md` (RULES rule 8).

**How to read this charter.**
- G2-11 items 1–9 are §§2–10; additions 1–4 are §§11–14. Appendix E maps every G2-11
  sentence to its clause.
- Rule IDs (Q-, NR-, DEF-, STD-, MC-, BU-, …) follow the working draft v1 wherever the
  rule is kept, so the CHARTER TEST catalogue (§24) can be read against this text.
- Numbers marked **[A]** are frozen in Appendix A.

---

## 0. Status, sources, conventions

### 0.1 Sources
- **Rulings and state:** `OWNER_RULINGS.md` (G2-11; also G2-08 and G2-10 where cited),
  `STATE.md` (Stage 3–6 definitions), `RULES.md`, `NORTH_STAR.md`, `SCOREBOARD.md`,
  `GRAVEYARD.md`.
- **R1:** `RESULTS/R1/R1_SYNTHESIS.md` (§§1–3, 7, 11, 12), `R1_T_LADDER.md` (§0, §1,
  §10), `D5_COMPARATOR_AUDIT.md`, `D5_IDENTIFICATION.md`.
- **F0 and SD0:** `F0_REQUIREMENTS_CONSOLIDATION_01.md` at `0a9a941` (requirements
  FR1–FR15, renamed from its R1–R15), `F0_SD0_CHARTER.md`,
  `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`, `F0_SD0_HOLDOUT_PROTOCOL_01.md`,
  `F0_SD0_RECON_01.md`, `F0_SD0_RESULT.md`.

### 0.2 Precedents adopted from SD0
- The charter is frozen alone; candidates are preregistered; any later modification
  makes a new candidate; repairs are numbered (CR-n).
- Free choices are weighed against distinctions. A symbol that encodes a table costs the
  table. A constant that matters for one control only is fitted to that control.
  Lookup structure is RELOCATED.
- Holdouts are chosen after the freeze by a selector that has not seen the mechanism.

### 0.3 Naming
- **FR1–FR15:** the F0 requirements. **R1:** the Stage-2 observable and its record.
- **ℛ★:** a card's primary target relation (its lock relation). **GY-n:** a GRAVEYARD
  entry (§21.2). **Card:** one frozen 𝒦 candidate with every field of §17.
- **Roles (§23):** Author, Kit builder, Intake auditor, Evaluator, Recomputer, Selector,
  Comparator panel, external checkers, Owner.

### 0.4 Conventions (binding throughout)
- **CV-1 Hostile default.** An ambiguity, an unresolved dispute or an unresolved regime
  question is resolved **against the card** until the owner rules. A dispute goes to the
  owner with both computations.
- **CV-2 Burden.** The card carries the burden of every certificate. The evaluator adds
  nothing that helps a card; it may add anything that lowers credit, within BP-7.
- **CV-3 Honesty (RULES 5).** No theorem without a proof. NOT FOUND ≠ IMPOSSIBLE.
  Literature is verified against primary sources; an unverified citation cannot carry a
  verdict on its own.
- **CV-4 Numerics (RULES 6).** Computed → machine-readable output → generated tables,
  with at least one exact-identity control.
- **CV-5 Neutrality.** The charter preregisters and favours no target relation, sign,
  monotonicity or functional form. Any sign or form in ℛ★ must come from 𝒦 (G2-11).
- **CV-6 Constants.** Every threshold, constant and catalogue is fixed in this charter,
  or by the §19.3 kit (and externally checked) before the first draft is logged. No card,
  including the first, sets or moves one.
- **CV-7 Interpretations.** After Card 1 is frozen, an owner ruling on a dispute
  chooses between the two submitted computations. It is recorded as interpretation
  CI-n. It applies to the card whose dispute raised it (whose affected screens are re-run
  under it, with the Recomputer's confirmation) and to every later card, null and
  self-test; it applies to other cards already scored only if it moves their verdicts
  toward failure. It is void if it changes a self-test verdict (§24.2).

### 0.5 Working record (non-normative)
- `PROGRAM/STAGE3/charter_workings/` holds the drafting record: three independent
  drafts, the merged draft v0, five red-team reports (lenses: definitional, relocation,
  standard physics, accounting, measurability/stopping), and the revised draft v1 with
  its red-team ledger.
- **This file governs.** The working record binds only through the CHARTER TEST
  presumption of §24.1.
- This charter is a distillation of v1. v1 (about 200 KB) could not be frozen as
  written: it required owner decisions before freezing, its credit scale was probably
  unreachable for an honest card (accounting report §0), and one red-team report reached
  its reviser truncated. Appendix D lists the builder's choices that differ from v1.

### 0.6 The charter in one page (summary; the sections govern)
1. **Baseline (§2, §13).** Standard physics with Π, carrier, [h] and T **chosen by
   hand**, after causality, positivity, KMS/FDT, Onsager, conservation and every other
   standard consequence that holds in the regime (hostile regime default). Its freedom
   is the fibered joint space FB. 𝒜_ε is only the image of 𝒜_Γ × 𝒜_T; no bits are
   counted on it.
2. **Success (§3).** One primary relation ℛ★(Π, [h], T_Π, Γ_Π) = 0 must be:
   - forced on all of Sol;
   - non-definitional, and not a consequence of ε's mathematics or of the card's own
     components;
   - non-standard: generic standard witnesses violate it, and the card's own pipeline
     run on standard models does not reproduce it;
   - law-dependent (a W-pipe off Sol) and not imposed by a cheap sub-conjunct (JN);
   - **joint**: the coupling is witnessed by realized interface values that differ in Π,
     carrier or interface statistics, never by the tier at which ε is evaluated;
   - informative, invariant, at an admissible interface class, non-vacuous, scoped,
     neutral and named in the lock register.

   It must also be COMPRESSIVE and lockable on a named existing platform with a feasible
   sample size.
3. **Compression (§4).**
   - Price: 6 bits per L₀ token for everything the card supplies, plus tuned constants,
     tables, selections and a tax on drafts.
   - Credit: the coupling bits b_J forced by ℛ★ — p★ = 10 bits per codimension on each
     of up to 100 structurally distinct post-freeze instances, capped so that a constant
     shared across instances counts once and no instance exceeds what survives on the
     lock fibers. Generating Π, carrier, [h] and T_Π is a gate, not a credit.
   - Required (§4.4): b_J − Price ≥ 10 bits at p = 10 and > 0 at p = 16. Verified
     selectivity bits (≤ 10, not multiplied) count only toward the LOOKUP test.
4. **Nonrelocation (§5).** Partition, carrier, readout class, interface class,
   Gibbs/FDT structure and the target relation may not be hidden in the inputs:
   - supplying the first four, even when priced, fails generation;
   - a Gibbs/FDT premise poisons every consequence, even when 𝒦 generates it;
   - supplying ℛ★ relocates the card.
5. **Budget (§6).** Three cards in total, for Stages 3–6. A slot is consumed at freeze.
   Variants are detected, and cards are evaluated sequentially with fresh sealed draws.
6. **Card contents (§7, §17).** Twenty mandatory fields, universal kill conditions and
   card-specific kill conditions with coverage rules.
7. **Originality (§8).** Familiar components are fine. Only a DISTINCTIVE physical
   relation for the assembled law admits a card.
8. **Cross-sector (§9).** Parameters fixed in sector A predict sector B with zero
   GRUT-specific adjustment, against a standard bridge panel. Stage 3 claims none.
9. **Stopping (§10, §20).** The route terminates under T-3 (budget spent or final count
   declared without an ADMISSIBLE card; every ADMISSIBLE card failing Stage 4 or 5; or
   Stage 6 needing a modified 𝒦). There are no extension stages, no prerequisite
   campaigns, and no rescoring except toward failure.
10. **Hard stop (§25).** Frozen alone. Owner review before the evaluation kit or Card 1.

---

## 1. Objects and the pipeline

### 1.1 Law, solutions, domains
- **Ξ** is the relational process object. The card declares and prices its kinematic
  type 𝒳 and its carrier of relata V_Ξ (IP-1, IP-14).
- **𝒞** is the card's commitment data. Its meaning is stated in the base language L₀,
  declared and priced (FR11). Possibility talk means *declared* possibility.
- **The law:** 𝒦[𝒞, Ξ] = 0. **Sol_𝒦(𝒞)** := {Ξ ∈ 𝒳 : 𝒦[𝒞, Ξ] = 0}.
- **Nonvacuity:** ∅ ≠ Sol ⊊ 𝒳 on every in-domain instance, at r★ and at r★★ [A].
- **Pre-law domain Dom_pre(ι):** every Ξ ∈ 𝒳 consistent with 𝒞_ι and the embedding
  Emb at the declared truncation, with no law clause imposed.
- **Gate domain Dom_gate(ι) ⊆ Dom_pre(ι):** the Ξ at which every chain map (§1.2) is
  defined at r★ and r★★, Π is persistent, A-stable and nontrivial (§1.3), the carrier
  form holds at Ξ (the chain at Ξ returns one h and t_a ∈ T_Π with
  Y_a = t_a(h(Z_Π)) for every a in A_{r★★}), and T_Π is admissible (§1.4). **Dom_gate^X** drops the conditions that X
  itself must meet. Extractors are total on Dom_pre and return a declared ⊥ outside
  their domain.

### 1.2 The pipeline
  𝒦 → Sol →[X_Π] Π →[X_Z] Z_Π →[X_h] [h]_{T_Π} →[X_T] T_Π →[Obs] Γ_Π →[charter ε code] ε_R → ℛ

- **Card-supplied components:** X_Π (partition), X_Z (carrier variable), X_h (readout
  class), X_T (interface class), Obs (record map), Emb (embedding of scenarios and
  repertoires into Ξ), and s_T (a canonical reduction, needed only when T_Π lies outside
  the catalogue 𝒯).
- **Charter-supplied:** the ε_R code (built by the kit from R1's frozen definition and
  this charter's §1.4 conventions), the batteries, the chart, and the evaluation kit
  (§19.3).

**Rules for card components.**
- **PC-1 Uniform.** One L₀ definition for every instance. No branch on scenario name,
  size, party or setting count, dimension, resolution or item identity.
- **PC-2 Priced** exactly like law clauses (§4). "Extraction, not law" earns no discount.
- **PC-3 Covariant** under the representation moves (§1.6).
- **PC-4 Decidable** within the declared resources (§16).
- **PC-5 Ablatable.** A component runs unchanged when 𝒦 is replaced by a null law
  (NR-4), and is total on Dom_pre.
- **PC-6 Upstream-only reads.**
  - X_Π reads (Ξ, 𝒞). X_Z reads (Ξ, Π). X_h reads (Ξ, Π, Z_Π) and the definition of Obs
    as a map. X_T reads (Ξ, Π, Z_Π, [h]) and the definition of Obs as a map. Obs reads
    (Ξ, Π, [h]) and each protocol's action on S. s_T reads T_Π.
  - **No component other than Obs evaluates a protocol,** and no component reads
    protocol identity beyond the protocol's action on S. No component other than Obs
    evaluates, estimates or recomputes (from Ξ or otherwise) a record law P_a, and no
    component evaluates, estimates or recomputes any further functional of Γ_Π, ε, d_op,
    P★, a chart coordinate, a battery verdict or a charter scoring function.
  - **No component evaluates the law:** not 𝒦, not any clause of 𝒦, not Sol
    membership, and not any condition L₀-equivalent within c_dec bits to a clause of 𝒦.
    In NR-3 and NR-4 any such internal copy is replaced together with 𝒦.
  - X_h reads Obs only with its [h]-argument unbound; selecting [h] by any criterion
    evaluated through Obs is DEF-17(a). s_T's output is the map s, built from T_Π alone;
    s is applied to record laws only by charter code.
  - Persistence and identity measures used anywhere in the chain are functionals of
    Ξ-level structure only.
  - **Enforcement:** call-graph inspection of the reference implementation, and a
    substitution test: replacing every per-protocol law that Obs produces by an
    independent draw of the same type must leave the outputs of X_Π, X_Z, X_h, X_T and
    s_T unchanged; and a **record-factorization test**: if an auditor exhibits an L₀ map
    F of length ≤ c_dec, not constant on Dom_gate, with the output of X_Π, X_Z, X_h,
    X_T, s_T or Emb = F(Γ_Π) on Dom_gate, that component recomputes a functional of
    Γ_Π.
  - **Violation:** every relation whose dependence passes through the illicit read is
    CARD-DEFINITIONAL.
- **PC-7 Components carry no target content.**
  - **(a)** The target-level firewall (NR-2), the decoder tests (NR-6, NR-7) and joint
    necessity (NR-17) apply to components exactly as to clauses. If the components,
    with the type and 𝒮, imply ℛ★ on Dom_gate, then ℛ★ is DEF-12.
  - **(b) Static maps are calibrated out.** The card's **static maps** are every map
    that depends on neither protocol nor state: the declared static tail (record-space
    maps applied after Obs's last read of Ξ), and the per-relatum maps and the
    aggregation of PC-7(c). Obs′ is Obs with the tail removed. The card declares its
    static maps at freeze; an undeclared static tail found by the auditor → RELOCATED
    (NR-0). Every static map is tested by DIF-5(e). ε and the chart are
    computed on Obs′ (as in R1 §1); the auditor does not re-factor Obs. A relation stated
    through the static tail is CARD-DEFINITIONAL.
  - **(c) The readout is blind to the partition.** Obs reads E-relata through one
    uniform map per relatum and one fixed symmetric aggregation declared at freeze.
    Weighting relata by any function of Π (distance to S, boundary membership, block
    size) is a supplied readout structure (PS-3) unless 𝒦 generates it with a W-pipe
    (NR-3).
  - **(d) Boundary ablation.** Every credited quantity is recomputed with the records of
    relata in ∪_a (Π_a Δ Π_ref) ∪ ∂ removed: each lock-observable prediction must stay
    within r_lock [A], and c_J, κ_J, every c_ι and κ_ι, and every gate verdict must be
    unchanged. Otherwise the verdict is MODE SELECTION.
- **PC-8 Statement and implementation.**
  - The L₀ statement is normative. The Recomputer derives Sol and every credited
    quantity from it independently.
  - Where the statement is ambiguous, the frozen reference implementation fixes the
    reading, and that behaviour is priced as a clause.
  - Implementation behaviour that selects within Sol and is not fixed by L₀
    (tie-breaking, ordering, initialization, tolerance) makes the affected claims
    CARD-UNFORCED.
  - A call from card code into charter code (B-HB, the ε code, the kit's regime
    surrogates and 𝒮 derivations) → RELOCATED.

### 1.3 Generated structures
**Π(Ξ), the partition.**
- Blocks: one designated environment block E and one or more system blocks S
  (S₁ … S_m for multipartite embeddings, §15.1).
- An approximate Π is an assignment V → Δ(blocks) with an unassigned boundary ∂,
  |∂|/|V| ≤ δ_∂ [A]. Records are read from the **persistent core** (relata never
  reassigned across A and t ≤ H_hor).
- **Persistent and A-stable** iff, with VI_norm := VI/log₂|V| (Meilă's variation of
  information under the uniform measure on V), **all** hold:
  - VI_norm(Π_a(t), Π_ref) ≤ δ_Π for every a ∈ A and t ≤ H_hor (Π_ref from the
    reference protocol a₀);
  - VI_norm(Π_a, Π_b) ≤ δ_Π pairwise across protocols;
  - the reassigned fraction is ≤ η [A], with ∂ counted as reassigned;
  - **non-vacuous:** on every lock fiber and credit instance, X_Π has a **relevant
    variable**: a Ξ-variable v, not set directly by a protocol template, such that at
    some Ξ ∈ Dom_gate(ι), changing v alone to another value it takes on Sol_ι (at another
    protocol in A_{r★★} or time ≤ H_hor, the realized laws differing by d_BL ≥ 2^(−p★))
    moves X_Π's output by more than δ_Π. A Π with no relevant variable is **FROZEN**: it
    is not persistent differentiation, and DIF-2 fails.
- **Horizon:** H_hor ≥ max(protocol and record window, 10·τ_int, 3·τ_slow), where the
  Evaluator computes the fastest internal timescale τ_int and the slowest relaxation
  time τ_slow from the law at the truncation, within the conserved sector of the
  realized reference state. If τ_slow is not computable, Π must be shown invariant under
  the realized stationary dynamics.
- **Scale window:** if the card uses any coarse-graining scale or threshold, Π must
  stay within δ_Π when each such scale is multiplied or divided by w [A].
- **Nontrivial:** S ≠ ∅ ≠ E; Π is not the partition into components already
  disconnected in the inputs; Γ_Π is not constant across A; and on the lock fibers
  log₂|𝒜_Π^hand(ι)/G_ι| − log₂ M(ι) ≥ b_Π [A], where 𝒜_Π^hand and G_ι are as in §2.3
  and M(ι) is the number of distinct persistent cores (∂ assigned to E) realized on
  Sol_ι, modulo G_ι — the law's selection must remove at least b_Π bits of hand choice.
  Before this test, inert relata are deleted. If one RB or SPS template τ of cost
  ≤ ℓ_dec — the same template on every lock fiber — applied to 𝒞_ι alone returns a
  nonempty set D_ι as one whole output block, D_ι lies within a single block of every Π
  realized on Sol_ι, and on a fraction ≥ p_dec of the AI-3 draws on which τ's
  corresponding block is nonempty that block lies within a single block of every
  realized Π, then D_ι is deleted from V_ι. At most one template is applied, and no
  relatum is deleted on its own. 𝒜_Π^hand, G_ι and M(ι) are computed on V_ι ∖ D_ι. This
  is the only reduction of V_ι or 𝒜_Π^hand by a template (§2.3).

**Z_Π, the carrier.** Its dimension is arbitrary. *Which* variable it is (instantaneous,
initial, or other) is a derived output and never a definition (R1 §12 item 5; D5
Remark D3).

**[h]_{T_Π}, the readout class.** h maps states of Z_Π into the record space 𝒴; it is
fixed only up to T_Π (h ~ t∘h). The class is derived as the readout redundancy of the
card's own observation map; the record space, its coordinates and its σ-algebra are
outputs of that derivation. **No unique coordinate formula for h is credited** (G2-11).

**T_Π, the interface class.**
- A group of record-space maps computed by X_T from (Ξ, Π, Z_Π, [h]) under PC-6.
- **One set for all protocols.** Every t ∈ T_Π is computed **without evaluating any
  protocol, any protocol's action on Ξ, or any solution's response.** A map that encodes
  how a protocol moves the system or the environment is response, not interface. If
  X_T's L₀ definition of any element or generator of T_Π refers to a protocol, a
  protocol's action on Ξ, a solution's response or a record law (a provenance test,
  checked by call-graph inspection and the PC-6 substitution test), carrier PASS is
  definitional and every reciprocity relation is CARD-DEFINITIONAL. The test also fails
  if X_T's definition contains, or computes and uses in building an element or generator
  of T_Π, a term L₀-equivalent within c_dec bits to the template-to-Ξ map, a protocol
  template, or the action of the driven S-variable on Ξ (its flow, linearization or
  response); content merely definable from X_T's inputs does not count. A
  catalogue-class element that coincides with some protocol's effect does not count if
  X_T's definition contains none of this content. If T_Π contains, on a lock fiber, a
  non-catalogue t_a with P_a = t_a#P_{a₀} within 2^(−p★), the card bears the burden of
  showing that the provenance test passes.
- Elements may differ per protocol in the R1 form Y_a = t_a(W), W := h(Z_Π),
  t_a ∈ T_Π.

**Γ_Π := Obs_Π(Ξ) = (P_a)_{a∈A}.** P_a is the law of the record Y_a ∈ 𝒴^τ under
protocol a. **Only per-protocol laws are data**; joint laws across protocols are
inaccessible-context data (FR3). A Γ given as an empirical model is supplied, not
generated (FR13).

**Carrier status.**
- **PASS** iff the card proves from 𝒦 that the carrier form Y_a = t_a(h(Z_Π)), with one
  h, t_a ∈ T_Π and Z_Π derived, holds at every Ξ ∈ Sol, for every a in every A ∈ 𝔄
  (§1.7).
- **FAIL** if the derivation produces protocol-dependent readouts h_a.
- **UNRESOLVED** otherwise; it counts as a failure (T-1).
- R1's verdict table applies unchanged: R1-PASS, R1-NULL, NO RECIPROCITY VERDICT,
  MODE SELECTION.

### 1.4 ε_R and admissible interface classes
- **Definition (frozen R1):** ε_R := ε[Γ_Π, T_Π] := inf over P★ of max over a ∈ A of
  d_op^{T_Π}(P_a, T_Π·P★). It is computed **only by charter code**, on continuous
  records, with no per-card normalization or alternative distance.
- **R1's frozen tiers** are T_R1 = T_lin (Tier 1: GL(k) with translations) and T_mono
  (Tier 2: coordinatewise strictly monotone continuous bijections), with their frozen
  distances (R1_SYNTHESIS §1): d_q^BL(P, Q) = min over O ∈ O(k) of d_BL(P̃, O#Q̃) after
  centering and whitening; and d_BL between normal-score (copula) laws minimized over
  the coordinate reflections ℛ; with ‖f‖_BL = max(‖f‖_∞, Lip f).
- **Charter catalogue classes.** E₂± (diagonal invertible affine maps) and T_caus
  (lower-triangular invertible affine maps: causal linear interfaces) are sub-classes of
  T_R1 from the R1 ladder (R1_T_LADDER §1). They are **charter catalogue classes, not R1
  tiers.** For them this charter fixes d_op(P, T·Q) := min over s ∈ {±1}^k of
  d_BL(s_T P, s·s_T Q), where s_T is per-coordinate standardization (E₂±) or the
  Cholesky innovations (T_caus) — the canonical forms and residual sign groups of
  R1_T_LADDER §1. R1's v1/v2 W₃ forms are not used. On laws without finite nonsingular
  covariance, ε at E₂± and T_caus is undefined and a claim using it fails Q8. This is a
  Stage-3 convention; it changes no R1 definition, distance, tier or verdict.
- **Terminology.** Elsewhere in this charter "tier" means any class of 𝒯 or T_Π, and a
  "T-tier verdict" is the R1 verdict-table outcome at that class; only T_R1 and T_mono
  are R1 tiers; "both tiers" in R1 records means T_R1 and T_mono.
- **The catalogue 𝒯** := {E₂±, T_caus, T_lin, T_mono}, with E₂± ⊂ T_caus ⊂ T_lin,
  E₂± ⊂ T_mono and T_lin ∩ T_mono = E₂±. Also named: the join J := the group generated by
  T_lin and T_mono (R1 makes no claim about it; R1_SYNTHESIS §9); T_univ := all
  bimeasurable bijections of the record space (GY-11; Prop. E); and the GY-11/GY-12
  classes.
- **Admissible set 𝕃_T^adm** := 𝒯 ∪ {generated T_Π with a valid s_T}. An ε value taken
  at J, at T_univ, or at a class without a valid s_T is **void** by rule.
- **Generated T_Π outside 𝒯.** The card supplies s_{T_Π} with residual compact group K,
  sets d_op^{T_Π}(P, T_Π·Q) := min over k ∈ K of d_BL(s(P), k#s(Q)), and proves on its
  declared law class:
  - (i) **invariance:** s(t#P) ∈ K·s(P) for every t ∈ T_Π;
  - (ii) **maximality:** s(P) ∈ K·s(Q) ⇒ P ∈ T_Π·Q;
  - (iii) **faithfulness:** d_op^{T_Π}(P, T_Π·Q) = 0 ⇔ P ∈ cl(T_Π·Q), so T_Π-orbits are
    closed in the declared law class; hence ε^{T_Π} = 0 iff the family is
    T_Π-separable;
  - (iv) **normalization:** s is the frozen canonical reduction of one catalogue class
    contained in T_Π and declared in C7 (centering and whitening for T_lin, Cholesky
    innovations for T_caus, per-coordinate standardization for E₂±, normal scores for
    T_mono), or the identity if T_Π contains no catalogue class, followed by a map built
    from T_Π alone; no fixed bijection of record space follows it, and any scale constant
    in s is a priced IP-5 constant.

  The declared law class contains every family on which charter code evaluates
  ε^{T_Π}: the image of Sol, B-REC, every B-HB family and composition within the frozen
  ranges, the Q3 witness and transplant draws, and the B-SRB scheme outputs. The kit
  checks (i)–(iv) on B-REC and all of B-HB with post-freeze seeds. s_T is priced as a
  component and run inside charter code. A failure of (i)–(iv) on any family on which
  ε^{T_Π} is used makes ε_R undefined for the card, and every ε-relation fails Q8.
- **Decision semantics.** ε is not exactly computable in general. An ε-equality or
  ε-inequality is decided by a theorem, or against the frozen enclosure [frozen witness
  lower bound, frozen-optimizer upper bound]: the claim holds iff the enclosure lies
  inside the claim's band and is separated from its boundary by at least 2^(−p★).
- **The R1 ladder stays closed** (G2-10). A generated T_Π, and the catalogue
  conventions above, are Stage-3 objects, never new R1 tiers. If T_Π equals T_R1 or T_mono, that is a result to be proved; it imports no R1
  theorem.

### 1.5 Instances, credit family, lock fibers, chart
**Scenario σ** (observable level, independent of any card): ports, repertoire A_σ, grid
τ_σ, record space 𝒴_σ. 𝒜_Γ and 𝒜_T are counted at this level; 𝒜_Π on the instance's
relata V.

**Audit instances ι = (𝒞_ι, V_ι, A_ι, τ_ι, 𝒴_ι):**

| Family | Content | Generated by |
|---|---|---|
| AI-1 | The smallest nontrivial instance, computed exactly | The card (evaluator may add) |
| AI-2 | Symmetric-input instances: Aut(𝒞) transitive on V or on the candidate partitions | The Evaluator |
| AI-3 | N_AI3 [A] draws from the charter reference measure (uniform on finite sets; log-uniform on default ranges, per primitive type in its canonical parametrization), relata count between n_min and 2·n_min [A], seeds committed by the Selector after the card's freeze | The Evaluator |
| AI-4 | Battery embeddings via Emb; never used for credit | The kit |
| AI-5 | Sealed holdout instances (§15.9), N_AI5 [A] per card | The Selector |

- **Credit family I_𝒦:** AI-1 if it has at least n_min relata, plus the first AI-3
  draws in seed order that satisfy the frozen domain predicate (DIF-7) and are
  structurally distinct from every instance already taken, up to N_cred [A] instances
  in total. If the committed draws are exhausted, the Selector draws further seeds, up
  to 10·N_cred attempts; further draws are AI-3 draws for Q1, NR-4, NR-6, IP-13 and
  DIF-7. **N_dist** is the number of instances obtained (≤ N_cred). Instances are
  **structurally distinct** iff (i) their 𝒞 are non-isomorphic after deleting, one at a
  time and keeping each earlier deletion, every datum whose replacement by a fixed
  default leaves Im(ι) unchanged up to relabelling;
  (ii) their seeds are disjoint; and (iii) their realized images Im(ι) are not equal up
  to relabelling of V and the declared moves. **Credit uses the minimum over I_𝒦,
  multiplied by N_dist** (§2.5).
- **Lock fibers:** at most 3 pairs (ι, H) — an instance and a regime class (§13.2) —
  declared at freeze. At least one is **regime-matched to the lock platform**
  (H(fiber) ⊇ H_host(platform), certified under BP-4 from the platform's interface-side
  data, MC-2). The **hostile fiber** at ι uses H_host: every hypothesis not certified to
  fail by at least δ_RH (§13.2).
- **Robustness:** Q1, Q5, Q6 and Q9 hold on a neighbourhood of each lock-fiber instance
  of relative size ≥ max(2^(−p★), the platform's certified parameter uncertainty).

**Chart φ_ι (frozen; built by the kit before Card 1).**
- Scope Q: every T-invariant witness coordinate of order ≤ m on the template grid.
  Scope G: the response functionals of the driven and recorded variables at the frozen
  templates and grid — mean response up to order m in the amplitude, two-time linear
  response functions, susceptibilities, power and cross spectra up to order m, and
  transport coefficients, in whitened units. Interface side: the observables of §3.3
  (VI_norm, reassigned and boundary fractions of Π, T-tier verdicts, carrier outcome).
- Box windows and resolution 2^(−p) per Appendix A. Cards neither add nor remove
  coordinates. The auditor may register up to N_ch [A] further coordinates before
  evaluation; credit is the minimum over the frozen chart and the chart plus those
  coordinates.
- **Ch-1** Every claim holds at r★ and r★★; credit is the minimum. **Ch-2** Frozen
  templates; the card chooses no battery items or scoring repertoires. **Ch-3** Finer
  grids, higher precision, copies of instances or a larger carrier earn nothing. **Ch-4**
  A relation that holds at r★ but fails at r★★ or at the next truncation level earns
  zero. **Ch-5** Credit is summed only across structurally distinct instances with
  independent data.

### 1.6 Representation moves (FR1)
RM1 relabel finite-set elements · RM2 relabel outcomes, interventions, ports · RM3
reparametrize continuous parameters by declared bijections · RM4 equivalent
presentations of a conditional-response kernel · RM5 re-bracket compositions. Further
moves are priced. **Every move acts identically on every protocol;** a move indexed by
protocol is mode selection (R1_T_LADDER §0). Invariance is claimed only under the declared moves,
against a declared generating set the kit verifies.

### 1.7 Repertoire
- The repertoire is a function of the generated Π: the frozen protocol templates
  (Appendix A) applied to the generated S through the template-to-Ξ map, which is part
  of Emb (uniform, priced, frozen). The template amplitude is set on the driven S
  variable under a₀, never on a record.
- A_{r★} and A_{r★★} are mandatory. 𝔄 is closed under sub-repertoires with |A| ≥ 2
  containing a₀. A restriction to a sub-repertoire is declared at freeze and costs
  log₂(number of admissible choices). No repertoire is selected after any score.

---
## 2. Item 1 — Baseline freedom spaces

### 2.1 Principles
- **BP-1 What the baseline is.** Everything established physics permits for operational
  data of the same type, in the same regime, from the same inputs (through θ_dict,
  §2.2), with Π, Z, [h] and T **supplied by hand**. It is computed **after** the standard
  constraint set 𝒮 (§13) and after removing the classes killed in the GRAVEYARD.
- **BP-2 Where standard theory leaves freedom.** Standard theory leaves Π, Z, [h] and T
  to the modeller and constrains Γ through 𝒮. **The null hypothesis Stage 3 must
  break:** standard physics treats Π, T and the generators of Γ as independent modelling
  choices, coupled only through 𝒮.
- **BP-3 Regime matching.** A claim about a realization x is compared only with the
  baseline under the regime hypotheses H(x) that hold at x. A witness from another
  regime is invalid. A regime property the card *generates* puts the fiber in that
  regime.
- **BP-4 Hostile regime default.** A hypothesis holds at x unless a deviation
  δ ≥ δ_RH (§13.2) is certified in its §13.2 surrogate metric, judged at charter
  resolution. A hypothesis that fails by δ still imposes its near-regime consequences
  with published perturbative error bounds (linear response about the regime;
  FDT-violation and Harada–Sasa bounds; ensemble-equivalence corrections; Onsager to
  first order in the affinity). An ill-typed hypothesis is evaluated through its
  §13.2 surrogate; if the surrogate is undecidable, the hypothesis holds.
- **BP-5 Same or more inputs.** The baseline receives, at zero price: every datum the
  card's prediction consumes; every datum used to fix a constant that enters the
  prediction (θ_K, θ_dict, platform calibration; XS-4); all carrier-certification data;
  and the **standard reference package**, measured on the lock platform (on the
  instance, for in-silico fibers) in a calibration run whose records are disjoint from
  the lock records, **whatever the prediction uses**:
  - every connected correlator of P_{a₀} of order ≤ m★★ = 5 at every grid time of r★★,
    and of any higher order the prediction or the derivation of ℛ★ uses;
  - the independently calibrated linear-response functions of the driven and recorded
    variables;
  - every regime parameter a standard modeller calibrates (e.g. temperature, spectral
    densities, conserved-charge values);
  - **Θ_std:** every further parameter a standard theory would use to predict the lock
    observables that can be measured without the lock records, declared in C13 (the
    auditor may add to it).
- **BP-6 Generation grants no exemption.** Every standard theorem conditioned on a
  supplied partition, readout or interface applies verbatim to a generated one. A
  framework applies at x unless the card proves one of its hypotheses fails at x by at
  least δ_RH.
- **BP-7 Asymmetric enlargement.** The evaluator may enlarge standard families for
  witness draws, transplant draws, 𝒮 derivations and narrowing J_SRB. It never
  enlarges FB or dim_lb, because that would help the card.

### 2.2 Standard models
- **𝔐_std(ι | H)** is the frozen generative grammar: the B-HB families (§15.4), their
  compositions by juxtaposition or by Hamiltonian or generator coupling within the
  frozen ranges, and card-added models from the HB families or their compositions within
  the frozen ranges, verified under the witness rules of §15.4. The SFP
  frameworks (§8) serve as derivation sources for 𝒮 and as comparators.
- A model belongs if it (i) produces data of the declared operational type on ι,
  (ii) satisfies every STD constraint whose hypotheses lie in H, (iii) uses the card's
  inputs through **θ_dict**, and (iv) takes Π, Z, [h] and T as supplied.
- **θ_dict** maps the card's instance inputs to standard-model parameters. It is
  declared, priced, and used identically for the baseline and the lock. The auditor may
  narrow it when the declared meaning of 𝒞 (FR11) fixes more standard parameters.
- **Single-model rule.** An interface-side quantity that is a functional of the dynamics
  (relaxation of ∂, exchange rates, persistence statistics) is computed from the **same**
  model m that produces Γ. A mixed point (u, Γ) is in the baseline only if a single
  m ∈ 𝔐_std(ι | H) realizes it.

### 2.3 The spaces
- **𝒜_Π(ι | H) := 𝒜_Π^hand(ι), partitions chosen by hand:** {⊥} ∪ {every partition of
  V_ι with S ≠ ∅ ≠ E, of the block count(s) the type admits} (2^|V| − 2 with one S;
  ordered set partitions with a designated E for multi-block embeddings). A modeller
  supplying Π by hand may designate any of them; the standard model then supplies the
  dynamics. A realized Π with boundary ∂ is matched in 𝒜_Π^hand by the crisp partition
  that assigns ∂ to E. Counts are taken modulo **G_ι**, the group generated by
  Aut(𝒞_ι) (computed by the kit) and the symmetry group of the realized dynamics of
  Sol_ι, acting on V_ι. **𝒜_Π^hand is never reduced by standard selectors** (except by
  the inert-relatum deletion of §1.3); FB, the
  b_Π size test (§1.3), ℓ_dec (NR-6) and §2.5 use it as defined here. Standard selectors
  enter in two ways:
  - applied to the **realized dynamics of Sol**, a match is STANDARD-MECHANISM
    (§15.7(viii)): recorded (no differentiation novelty), never a relocation;
  - applied to 𝒞 or to any other item of the §5.2 inventory, an SPS or RB template is an
    NR-6 decoder, and a match is RELOCATED. Where both apply, NR-6 governs.
- **𝒜_T(ι, Π | H), interface structures ([h], T):** T ∈ 𝒯 ∪ {⊥} with
  𝒯 = {E₂±, T_caus, T_lin, T_mono} the charter catalogue (§1.4); h is any readout of a declared E-state
  variable, common across A by hand; T must be causally implementable (STD-1),
  CP-implementable (STD-2), and contain the platform's calibrated maps. 𝒯 excludes the
  GY-11 and GY-12 classes, J and T_univ. For membership in the baseline, a generated
  T_Π counts as a class that could have been supplied by hand.
- **𝒜_Γ(ι, Π, [h], T | H), record families:** {Obs(m) : m ∈ 𝔐_std with this
  (Π, Z, [h], T)}. With H = ∅ it is the set of non-anticipating, positive families on
  𝒴^τ indexed by A; each hypothesis in H intersects it with its constraint list
  (§13.2). Under RH-SYM(G) the models are G-covariant and partitions are taken up
  to G.
- **𝒜_ε := {ε[Γ, T] : (Γ, ([h], T)) jointly admissible}.** It is the **image** of
  𝒜_Γ × 𝒜_T under ε, **not an axis** (addition 2). No bits are ever counted on it.
- **FB = 𝒜(ι | H), the fibered joint baseline:** pairs (u, Γ) with
  u = (Π, Z-class, [h], T, interface-side statistics), each component admissible given
  the earlier ones, under the single-model rule. The standard couplings (STD-5, STD-7,
  STD-10, STD-13) live inside the fibers. **Freedom reduction is measured inside FB,
  never against the product 𝒜_Π × 𝒜_T × 𝒜_Γ.**
- **𝒟(ι), the definitional space:** all well-typed tuples **before** 𝒮 — Π any
  partition of V, [h] any class, T ∈ 𝕃_T^adm ∪ {T_Π}, Γ any family of per-protocol laws
  on 𝒴^τ indexed by A — with ε substituted.
- **Intractable quantities.** A baseline quantity that no terminating frozen procedure
  computes within the kit's resources contributes zero credit on its axis.

### 2.4 Values fixed now
- (2,2,2), possibilistic: 2961 pNS tables — 1721 local; 1232 logically contextual (992
  with an exact-support realization, 240 without); 8 strongly contextual, exactly the 8
  PR boxes. Record-law object: 2721 exact-support-realizable supports.
- Interface catalogue: |𝒯 ∪ {⊥}| = 5.
- Partitions of n relata with one S: 2ⁿ − 2 (n = 8: 254, about 7.99 bits).
- Everything else is computed by the Evaluator with the procedures of §2.5, never by
  the card.

### 2.5 Measuring freedom reduction
**Realized image.** Im(ι) is the **full** image of Sol in chart coordinates (u, r):
- u: interface values — Π up to Aut, the carrier class, [h], T_Π, and the declared
  interface-side statistics;
- r: response values — frozen chart coordinates of Γ, with ε and every T-invariant
  functional evaluated **at each catalogue class of 𝒯 and at T_Π**.

A point of Im outside FB is a **non-standard realization**. It is reported as a
declared prediction with its own kill condition, and if it contradicts an established
relation inside that relation's tested domain, KU-4 applies. Non-standard realizations
are **never removed** to shrink the realized set.

**Realized coupling (the only credited reduction).**
- The **lock family** 𝓘 is the set of in-domain instances sharing one chart: AI-1, the
  credit family and the lock fibers. U and R are the realized interface and response
  values over 𝓘, and the **product hull** is 𝓗 := FB ∩ (cl U × cl R), under the
  single-model rule.
- **Fixed-class fibers (DEF-14).** A cross pair (u₁, r₂) enters 𝓗 only if every ε
  value and T-invariant functional in ℛ★ is evaluated at one class for both points.
  When ℛ★ uses only catalogue classes, any cross pair qualifies; when ℛ★ uses T_Π, u₁ and
  u₂ must carry the same T_Π. Codimensions are computed fiberwise, and the minimum is
  taken over the fibers that contain at least two realized interface values differing in
  Π, carrier class or a declared interface statistic that is not a function of T_Π alone
  (T-tier verdicts excluded); if no fiber does, c_J := κ_J := 0. A credit instance
  counts toward b_J only if its realized interface values lie in such a qualifying fiber
  (N_fib, below).
- **Coupling codimension:** c_J(ℛ★) is the minimum of
  - (a) dim_lb 𝓗 − dim_ub(𝓗 ∩ Z(ℛ★)); and
  - (b) for every **admissible comparison class** M: a B-HB family, a composition of
    B-HB families within the frozen ranges, or a model class of an SFP framework
    published before the card's freeze. Every such M is stated without reference to the
    card, to ℛ★ or to any lock observable; its parameters are constants of M (shared
    across instances or per instance), not functions of u, of ℛ★ or of the card's inputs
    except through θ_dict. M receives at zero price the card's instance inputs through
    θ_dict (§2.2) and the card's realized Π, carrier class, [h] and T_Π on every
    instance; its declared interface statistics are computed from M itself under the
    single-model rule (§2.2); generating the interface is a gate, never a credit
    (§4.3(b)). M qualifies if it realizes Im ∩ FB (non-standard realizations are scored
    by their own kill conditions and never disable this clause) and
    Price(M) ≤ Price(𝒦) at the same p. If Im ∩ FB is empty, (b) does not bind. The value
    is the codimension of Z(ℛ★) ∩ Obs(M) in Obs(M), where Obs(M) is M's image over the
    lock family with M's constants free over their ranges; the fitted values only show
    that M realizes Im ∩ FB, and they enter Price(M). Here Price(M) := the IP-4
    framework choice + L_stmt(M) + the IP-5 price of M's fitted constants (a constant
    shared across instances is priced once, a per-instance constant once per instance)
    + P_v for every VB item M uses. If no class qualifies, (b) does not bind.

  c_J never exceeds the number of functionally independent scalar equations of ℛ★ that
  a registered lock observable tests. For discrete coordinates, **κ_J** is the same
  minimum in log₂ cell counts at resolution 2^(−p★).
- **Per-instance coupling:** on credit instance ι, c_ι := the minimum, over the
  realized interface values u ∈ U_ι, of the codimension of Z(ℛ★)'s slice at u inside the
  response fiber FB(u) (κ_ι likewise for discrete coordinates). FB(u) is the response
  fiber over the card's (Π, carrier class, [h], T_Π) at ι, with Π taken in 𝒜_Π^hand;
  dynamical interface statistics are coordinates computed from the same standard model,
  not conditioning values. If no m ∈ 𝔐_std(ι | H) accepts the card's (Π, [h], T_Π),
  then c_ι := κ_ι := 0 and the point is reported as a non-standard realization.
- **Lock-fiber cap:** for each lock fiber f, c_f := the minimum, over the realized u of
  the fiber's instance, of the codimension of Z(ℛ★)'s slice at u inside
  FB(u | H_host(ι_f)) (κ_f likewise);
  c_lock := min over f of c_f (κ_lock likewise).
- **Family cap:** c_fam := the minimum, over every class M admissible in (b) — its
  price condition excepted — that realizes Im ∩ FB on all of I_𝒦 (receiving inputs and
  u as in (b)), of the codimension of Z(ℛ★) ∩ Obs_fam(M) in Obs_fam(M). Obs_fam(M) is
  M's joint image over I_𝒦 with its constants free; each constant takes one value on
  each group of instances on which one value realizes Im ∩ FB (the coarsest such
  grouping), and one value per instance otherwise (κ_fam likewise). A freedom that M
  carries in one shared constant is credited once per group, not once per instance. If
  no class qualifies, the family cap imposes no bound.
- **Coupling credit:**
  b_J(ℛ★) := min{ N_fib · min over ι ∈ I_𝒦 of [p★·min(c_ι, c_J, c_lock) +
  min(κ_ι, κ_J, κ_lock)], p★·c_fam + κ_fam },
  where N_fib ≤ N_dist counts the structurally distinct credit instances whose realized
  interface values lie in a qualifying fixed-class fiber (the minimum still runs over all
  of I_𝒦),
  computed after 𝒮, at r★ and r★★ (the minimum is taken). One codimension is worth p★
  bits at every sensitivity level p; window bits are not credited.

**Dimension certificates.**
- dim_ub is the **generic** rank. It is certified by a proof; or by explicit equations,
  verified by exact symbolic identity to vanish on Im within the window, whose Jacobian
  has the claimed generic rank with a lower-dimensional singular locus; or by a proof
  that the parametrization is analytic on a connected domain plus the exact rank at
  points drawn with post-freeze seeds (the maximum is taken). **A rank at a chosen point
  certifies only dim ≥ that rank.**
- dim_lb is certified on a regime-matched box around the same generic point by B-HB
  witnesses that meet the witness rules of §15.4.

**Reported, never credited:** marginal reductions (a projection of Im strictly inside
FB on one side); reductions of log-volume by inequalities; persistence,
differentiation and the generation of Π, carrier, [h] and T_Π (they are **gates**,
§5.5 and §15.10, never credits).

**Nontrivial reduction** (used by SC1): on every lock fiber, Q5 and Q6 hold, the
anchors are retained (§15.8), Im satisfies 𝒮 apart from declared violations outside
𝒮's established domain (each with its own kill condition), and the excluded set
FB ∖ Z(ℛ★) has nonempty relative interior in FB (positive reference measure on discrete
parts), meets {ε > r_lock}, and meets the region where the card's Π is realized.

---

## 3. Item 2 — Success criterion

### 3.1 The qualifying relation: certificates Q1–Q12
A relation has the form ℛ(Π, [h]_{T_Π}, T_Π, Γ_Π) = 0 with zero set Z(ℛ). ε_R enters
only as ε[Γ_Π, T_Π]; it is never a coordinate of its own. **ℛ★ must hold every
certificate at r★ and at r★★.**

- **Q1 Forced.** Im(ι) ⊆ Z(ℛ★) on every in-domain instance (AI-1 to AI-4 and the
  holdouts), for every A ∈ 𝔄 and every frozen grid, on **all of Sol** (FR8), at
  DERIVED grade: a theorem, or exact computation on every finite battery instance plus
  a proof for the declared scope. ε-claims follow §1.4's decision semantics. Forcing must
  not rely on any pending or evidence-grade item (§11). Forcing at evidence grade only
  gives CARD-UNFORCED.
- **Q2 Non-definitional.**
  - (a) ℛ★ is none of DEF-1 to DEF-17 (§12) and is not implied by them on the realized
    fibers FB(u), u ∈ U. DEF-12 is tested on Dom_gate, DEF-15 on Im, DEF-17(c) on FB,
    the others on 𝒟.
  - (b) **Fiberwise:** for every realized u ∈ U, the definitional fiber 𝒟(ι | u)
    contains a response value that violates ℛ★.
  - (c) ℛ★ restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R
    (addition 2). The auditor may exhibit a hypothesis P under which ℛ★ is a DEF
    consequence (DEF-15); the burden of rebuttal is the card's.
- **Q3 Non-standard.** For each regime class H on which ℛ★ is claimed:
  - (a) **Witnesses.** At least two SFP frameworks applicable under H (BP-6); fewer →
    Q3 fails. Inapplicable frameworks are listed with reasons. For each applicable
    framework F, a regime-matched witness m*_F ∈ 𝔐_std (from B-HB, or added by the card
    under the witness rules of §15.4) that satisfies every hypothesis of F at x, so that
    every consequence F imposes at x holds for it, with Obs(m*_F) ∈ 𝓗 ∖ Z(ℛ★), violating
    ℛ★ by at least 3·r_lock in some lock observable; for discrete coordinates, violation
    means a certified membership change. A witness that violates only a single-axis
    consequence of ℛ★ does not count. One witness may serve several frameworks; a
    framework that defines no model class (a constraint scheme, scale-type or invariance
    framework) is met by any witness consistent with it.
  - (b) **Genericity.** ℛ★ fails on an open neighbourhood of each witness within its
    standard family (positive reference measure for discrete families). If ℛ★ holds on
    an open dense subset of a family's image, it is STANDARD-GENERIC and fails Q3. The
    families here are admissible comparison classes in the sense of §2.5(b): stated
    without reference to the card, to ℛ★ or to any lock observable, with parameters
    that are constants rather than functions of u or of ℛ★.
  - (c) **Transplant.** For each lock fiber the Evaluator draws standard models of the
    declared type under H (B-HB, generic parameters under the reference measure,
    post-freeze seeds), runs the **card's own components** on them (the card's realized
    Π where X_Π is undefined), then the charter ε code. If ℛ★ holds within r_lock on a
    fraction ≥ 1/Q_min [A] of draws → CARD-STANDARD. If a draw cannot be expressed in
    the declared type, the card's frozen, priced standard-model embedding E_std
    (declared in C12) is used. E_std must be uniform and must preserve the draw's
    per-protocol record laws through the card's Obs within 2^(−p★), with the draw's own
    partition and readout mapped by E_std; E_std maps only the draw's degrees of
    freedom, couplings, state and readout, and reads no record law, response or
    functional of the draw's Γ; any auditor may substitute another embedding meeting these
    conditions at no greater price, and the transplant fraction is the largest over the
    embeddings exhibited. Where X_Z, X_h or X_T returns ⊥, or the carrier form fails, the
    card's realized Z_Π, [h] and T_Π from the lock fiber are substituted (as for Π); a
    draw leaves the denominator only if the chain is still undefined. If no E_std is
    declared, or fewer than half the draws are scorable, Q3(c) returns CARD-STANDARD.
  - (d) A witness whose interface is supplied by hand is reported but never satisfies
    Q3 by itself.
  - (e) **Constructive rule.** STANDARD status is decided constructively: without
    witnesses meeting (a) and (b), ℛ★ is STANDARD. Any cited standard derivation (§13.4)
    makes it STANDARD-IMPLIED.
  - (f) **Excluded forms:** the D5 reverse-direction relations (§13.8) and their
    consequences on the lock fibers; the saturation of a standard bound, unless it
    survives §13.5; any "response = X · correlation" unless X is predicted from
    interface-side data and beats B-SRB by Q_min.
- **Q4 Law-dependent.** A W-pipe exists: some Ξ ∈ Dom_gate(ι) ∖ Sol whose **defined**
  pipeline image violates ℛ★ by more than r_lock in some lock observable (a ⊥, undefined
  or non-persistent image never counts). The responsibility map (NR-4) shows that ℛ★
  does not appear under 𝒦_∅ and fails, on some lock-fiber instance, when some clause of
  𝒦 is deleted. Dependence on the type, components, representation or prior in
  addition to the clauses is allowed only where DEF-12, NR-9 and NR-17 do not fire. ℛ★
  survives joint necessity (NR-17).
- **Q5 Joint.** On the lock family, c_J ≥ 1 or κ_J > 0 (§2.5), and:
  - the reduction is witnessed by realized u₁, u₂ ∈ U that differ in Π, in the carrier
    class, or in a declared interface statistic that is not a function of T_Π alone
    (T-tier verdicts excluded), and whose ℛ★-slices differ;
  - it survives evaluating ε at one fixed class for all compared points (a catalogue
    class, or T_Π when T_Π is the same at all compared points)
    (variation of T_Π alone, or of the tier at which ε is evaluated, never establishes
    jointness — DEF-14);
  - if U is a single point, ℛ★ is NONJOINT;
  - the coupling is not carried by the instance inputs alone. Take any L₀ split
    𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the author or a reviewer in which neither part implies 𝒦 on
    Dom_pre and each part's Price_min (the L_stmt of its shortest statement exhibited by
    any party) is strictly below Price_min(𝒦). Ξ-level predicates R₁, R₂ ⊇ Sol with
    R₁ ∧ R₂ ≡ 𝒦 on Dom_pre may be offered on the same terms, so a part that restates 𝒦
    or contains it as a disjunct never qualifies. If, on every instance of 𝓘, every
    Ξ ∈ Dom_gate(ι) satisfying 𝒦₁ has that instance's realized interface value, and every
    Ξ ∈ Dom_gate(ι) satisfying 𝒦₂ has, read at that realized interface, that instance's
    realized response values, ℛ★ is NONJOINT.

  Not qualifying: a restriction on one axis; a coupling of Π and T alone; a disjunction
  of single-axis restrictions; a coupling carried only by ε's T-argument.
- **Q6 Informative.** c_J ≥ 1 or κ_J ≥ log₂ Q_min; c_f ≥ 1 or κ_f ≥ log₂ Q_min on
  every lock fiber f (§2.5); and the lock discrimination b_meas ≥ log₂ Q_min (MC-4). A relation fixing only a sign or a zero
  carries at most 1 bit and fails.
- **Q7 Representation-invariant.** Invariant under h ↦ t∘h for t ∈ T_Π, under the
  declared protocol-uniform moves (§1.6), and under relabellings of V. Depends on Γ only
  through per-protocol laws (FR3).
- **Q8 Admissible interface.** Every ε value is taken at a class in 𝕃_T^adm with a
  valid s_T (§1.4).
- **Q9 Non-vacuous.** Any scope: on each lock fiber, FB has points with ℛ★ = 0 and
  with ℛ★ ≠ 0. Scope Q additionally: every lock fiber has certified realized points with
  ε^{T_Π} > r_lock; FB has points with ε^{T_Π} = 0 and with ε^{T_Π} > 0; and ℛ★ is not
  satisfied merely because ε_R ≡ 0.
- **Q10 Scoped.** The relation declares exactly one response scope (§14), frozen with
  the card, and is consistent with it. The primary and the secondary relation each carry
  their own declaration.
- **Q11 Neutral.** Any sign, monotonicity, tradeoff or functional form in ℛ★ is an
  output of the derivation from 𝒦; the W-pipe shows the pipeline alone would also admit
  the opposite sign. A supplied sign is a supplied target relation (PS-6).
- **Q12 Named.** ℛ★ is entered in the lock register at freeze with its LT-1
  instantiation (§3.3).

**Number of relations.** Exactly one primary relation ℛ★ is credited. At most one
secondary relation may be declared: it is scored for Q1–Q12 and its kill conditions,
shares the Bonferroni correction (MC-9), can kill the card, and **earns no credit**.

### 3.2 Success thresholds
A card succeeds only through all of the following, and only while it remains admissible
under screens S0–S9 (§18):
- **SC1 Nontrivial freedom reduction.** Q1–Q12 hold at r★ and r★★, and the
  nontrivial-reduction conditions of §2.5 hold on every lock fiber, after 𝒮.
- **SC2 Positive compression.** COMPRESSIVE under §4.4.
- **SC3 Measurable consequence.** An admissible and **feasible** LT-1 instantiation
  (§3.3) on a named existing platform class. There is no "in-principle" grade.
- **SC4 Never credited toward SC1–SC3:** the items of §22.

### 3.3 Measurable consequence: the lock target LT-1
ℛ★ is tested on a physically realized environment with a certified carrier. It
predicts at most 3 lock observables o⃗, each a frozen chart coordinate (or a fixed
affine function of frozen coordinates, in Appendix-A units), in one of two ways:
- **(i) from interface-side quantities measured independently:** VI_norm and the
  reassigned and boundary fractions of the platform's Π, the T-tier verdicts, and the
  carrier-certification outcome, all obtained as MC-2 requires; or
- **(ii) from response-side data** on protocols, record channels **and** grid times all
  disjoint from those of the observables (a₀ may be shared only through independent
  runs). The map from those inputs to the prediction must not be derivable from
  DEF-1 to DEF-17 ∪ 𝒮 alone.

No parameter is fitted on lock data. **What is locked is the residual that standard
response theory (B-SRB), given the BP-5 inputs, leaves free.**

- **MC-1 Observable type matches scope.** Scope Q uses a T-invariant observable at a
  catalogue class of 𝒯 or at T_Π, or a frozen witness whose value ℛ★ fixes on the lock
  fiber.
  Scope G uses a response functional. A prediction interval with an endpoint at a
  DEF-2 or DEF-5 bound is a sign test and is inadmissible.
- **MC-2 Independence and sensitivity.**
  - **Sensitivity:** replacing every independent interface-side input by its full
    admissible range over the interface fibers of FB (Π ∈ 𝒜_Π, ([h], T) ∈
    𝒜_T(ι, Π | H)) must widen the predicted region J_K by a factor ≥ Q_min in cell
    count. Otherwise the lock is a pin: DEFINITIONAL, and SC3 fails.
  - **Platform interface:** the platform's Π and T_Π are obtained by applying the
    card's frozen X_Π and X_T, in silico, to Sol_𝒦(𝒞_platform), where 𝒞_platform is built
    from interface-side structural data only (geometry,
    independently measured couplings, apparatus specifications, records of declared
    calibration-only protocols outside A). No functional of the record laws of any
    protocol in A, or of the route-(ii) inputs, may be used. Selecting the cut by
    maximizing a record functional is prohibited.
  - Certification is independent of the records used to test ℛ★; the carrier cannot be
    certified from records (R1 §3); predicting ε_R from the same Γ it is computed on is
    definitional.
- **MC-3 Prediction.** J_K is frozen with every uncertainty propagated, truncation
  included. Every error term entering ℛ★ (leakage of an approximate Π, truncation,
  coarse-graining) is bounded by 𝒦, and the predicted effect exceeds that bound by a
  factor ≥ Q_min; otherwise the lock is UNFALSIFIABLE (a fail). The preregistered total
  uncertainty σ_pre, systematics included, satisfies σ_pre ≤ |J_K|/4.
- **MC-4 Discrimination.** b_meas := log₂( N(J_SRB ∩ W) / N(J_K ⊕ 2σ_tot) )
  ≥ log₂ Q_min, where σ_tot := max(σ_pre, σ_stat at N_max effective samples) and N counts
  2^(−p★) cells of the frozen chart coordinates in frozen units within the windows W [A].
  Reparametrizing o⃗ is prohibited; b_meas is the minimum over {the frozen coordinate,
  log|·| of it where it has one sign on J_SRB ∪ J_K}. **Live rival:** at
  least one verified standard witness consistent with every BP-5 input predicts the
  observable strictly more than 3σ_pre outside J_K; power (MC-7) is computed against the
  nearest such rival. Scope Q additionally requires J_K to be separated by at least
  3σ_pre from the value the observable takes on T_Π-separable families (0 for ε; 0 on
  both sides for a signed witness), unless J_SRB excludes that value by at least
  3σ_pre. A lock that
  predicts only from amplitude-scaled or sign-reversed versions of the observable's own
  protocol must beat order-(|A|−1) Volterra interpolation by Q_min (STD-14).
- **MC-5 Thresholds.** σ_eff := max(σ_pre, σ_stat). **LOCK-FALSIFIED** if
  dist(O_meas, J_K) > 3σ_eff. **LOCK-CONFIRMED** if dist ≤ 2σ_eff, σ_eff ≤ |J_K|/4 and
  MC-4 holds. **LOCK-VOID** if realized systematics exceed 1.25·σ_pre, or if any
  threshold, observable, tier, protocol set, grid, estimator, platform or exclusion
  rule changes after card freeze; LOCK-VOID counts as LOCK-FALSIFIED. **LOCK-
  INCONCLUSIVE** otherwise; on the primary platform (or the alternate, if used) it is a
  G5-LOCK fail.
- **MC-6 Carrier certification.** The platform passes the frozen 10-item checklist
  (Appendix G; adopted here as a Stage-3 rule, not an edit to R1). It is completed and
  frozen by hash, by an agent blind to the observable, before unsealing, and never
  revised with lock data. It certifies **the carrier the card derives** (the
  state-variable class and readout class derived in the card's C7 and declared for
  measurement in C9, RS-6). One preregistered alternate platform is allowed: a
  certification failure on the primary before any lock datum is unsealed moves the lock
  to the alternate. On the platform actually used, if the card predicted a certifiable
  carrier there, a failed certification, MODE SELECTION or NO RECIPROCITY VERDICT counts
  as LOCK-FALSIFIED; otherwise as LOCK-INCONCLUSIVE.
- **MC-7 Feasibility.** The Evaluator computes N_req by simulating the frozen estimator
  on the card's in-silico realization at the lock fiber and on the live rival, in
  effective samples (frozen integrated-autocorrelation estimator); the larger of the
  card's and the Evaluator's values governs. Required: N_req ≤ N_max [A] per card at the
  α and power of Appendix A, and total platform time ≤ the Appendix-A limit. Otherwise
  CARD-UNMEASURABLE. Estimation uses per-witness forms; R1's D4 is not a prerequisite.
- **MC-8 Sealing.** **LOCK-H:** an eligible pool of ≥ N_pool [A] archived datasets
  passing MC-6, excluding those the author declared seen, those the card cites, and
  those whose observable value was published before card freeze (that is calibration);
  the Selector draws with a committed seed. **LOCK-E** (when LOCK-H is unavailable): a
  prospective experiment with its protocol committed before any data exist, unsealed
  within T_lock [A] of G5-LOCK, or G5-LOCK fails. In-silico evaluation is evidence grade
  only (in-silico budget, Appendix A) and never confers PREDICTIVE.
- **MC-9 Multiplicity.** At most 3 lock observables per card. The adjustment is fixed at
  card freeze and never changed by a later card: each observable is tested at
  α_obs := α/(3·n_obs), where 3 is the card budget (BU-1). The MC-5 falsification
  multiplier 3 becomes z_obs := Φ⁻¹(1 − α_obs/2); the confirmation multiplier stays 2,
  because confirmation requires every observable (MC-10); MC-7 power is computed at
  α_obs.
  Lock observables are independent only if none is implied by the others under
  𝒮 ∪ DEF-1 to DEF-17 and their estimators share no records; a dependent observable is
  removed before MC-4 is computed.
- **MC-10 Status.** LOCK-CONFIRMED requires every observable of ℛ★ to be confirmed on
  sealed real data; with an external check it confers PREDICTIVE on ℛ★ only.
  LOCK-FALSIFIED on any observable of any registered relation fires KU-12.
- **MC-11 Platform.** The card names an existing platform with published operating
  parameters in one declared class: P-1 classical mechanical or stochastic environments
  with independently calibrated readouts; P-2 mesoscopic electronic environments with
  calibrated counting statistics; P-3 engineered quantum environments with calibrated
  input–output readout; P-4 archived datasets meeting MC-6 (LOCK-H only). The Intake
  auditor pre-assesses each Appendix-G item as satisfiable on that platform; otherwise
  CARD-UNMEASURABLE. If the platform's H contains RH-KMS, Q3 and B-SRB run with STD-3 in
  force on the platform-matched fiber.

---

## 4. Item 3 — Compression accounting and information price

### 4.0 What "positive compression" measures
- **Price** is the information a card supplies: every free choice, in bits, under the
  mechanical code of §4.1–§4.2.
- **Credit** is the joint freedom the card's relation removes from the post-standard
  baseline: the coupling ℛ★ forces between interface and response (b_J, §2.5). Verified
  selectivity distinctions (D_sel) count only toward the LOOKUP test. **Generating Π,
  the carrier, [h] and T_Π is a gate, never a credit** (§5.5, §15.10): a generated
  structure is the card's own output, and counting it would credit the card for
  compressing what it produced itself.
- **Scale.** The coupling is counted over a frozen credit family of up to N_cred
  structurally distinct instances drawn after the card's freeze, capped by the family
  and lock-fiber caps of §2.5. The card must therefore pay for itself within about
  N_cred independent applications. Appendix A records the paper feasibility check
  (ST-10).

### 4.1 Base language and code
- **L₀ (RULES 2):** finite sets, maps, interventions, conditional response,
  composition, logic. **Code:** the frozen 64-token alphabet in Polish notation
  (Appendix B.1), **6 bits per token**. The 4 reserved tokens are unavailable to cards.
- **Typing of base tokens.** `pair`, `×` and `⊗` applied to V_Ξ or relata are base
  tokens when they form tuples or relations; splitting V_Ξ or 𝒳 into blocks is VB-4.
  `kernel`, `cond-prob`, `E`, `law`, `marginal` and `support` applied to Ξ, 𝒞 or relata
  are VB-13 when they supply a prior, weight or reference measure that 𝒦 does not
  generate. 𝒦's own transition rule is priced as law clauses (IP-1), its numbers under
  IP-5, and its PS-5 content under NR-1 and NR-12. The charter reference measure used
  unchanged is not VB-13. A kernel whose output law does not depend on its input on
  Dom_pre is a measure (VB-13; NR-9), not a transition rule.
- **Normal form:** prenex negation normal form with explicit quantifiers and no Skolem
  symbols. L_stmt is computed on the card's own form instead if that form is shorter and
  proved equivalent.
- **Statement length:** L_stmt(X) := 6·#tokens(X) + Σ over variable occurrences
  ⌈log₂(v_X + 1)⌉ + Σ over literals ℓ(lit), where v_X is the number of distinct
  variables, ℓ(n) is the Elias-δ length of n + 1, ℓ(n/d) := ℓ(n) + ℓ(d) + 1, and a real
  literal at precision p costs p + ℓ(|exponent|) + 1. A defined symbol costs its
  definition once, then ⌈log₂(#definitions + 1)⌉ bits per use.

### 4.2 Price components — Price(𝒦) := IP-1 + … + IP-14
- **IP-1 Statement:** L_stmt of 𝒦 in normal form (the declaration of 𝒳 is priced under
  IP-14).
- **IP-2 Inputs:** every supplied datum under the same code — 𝒞 and its FR11 meaning;
  carrier size, initial data, couplings, constants, scales, time unit; Emb (with the
  template-to-Ξ map) and the selectivity interface; X_Π, X_Z, X_h, X_T, Obs, s_T;
  θ_dict; truncation levels, tolerances, thresholds and enumeration bounds; moves beyond
  RM1–RM5; domain restrictions; disambiguating implementation behaviour (PC-8). A prior
  or measure costs max(L_stmt, D_KL(prior ‖ charter reference measure) in bits).
- **IP-3 Tables:** a symbol that encodes a table costs the whole table. Hand-listed
  configurations are tables; quantifying over a list supplied in the inputs is a table.
- **IP-4 Selection:** choosing an invariant, clause shape, component, framework or
  relation from a family costs log₂ m, where m is the size of the largest finite family
  any auditor exhibits in the same role (by citation or by an L₀ generator), counting
  only members whose full L₀ unfolding (IP-8) is no longer than the selected item's. The
  family must be finite and disclosed before S6. The item costs max(L_stmt, log₂ m).
- **IP-5 Constants:** max(literal length at p, log₂(R / passing window)), where
  R := max(declared range, the charter default for its type, the largest range any
  auditor exhibits, bounded at the default widened by 3 decades on each side) — default [10⁻³, 10³] on a log scale for a dimensionless
  positive constant — and the passing window is the largest window inside which J_K
  moves by less than ¼|J_K| and no verdict changes. A value costs 0 only if a DERIVED
  theorem from 𝒦's clauses fixes it with no expression introduced for the purpose.
  Constants are repriced at p = 6, 10, 16.
- **IP-6 Priced vocabulary** (Appendix B.2). Using an item VB-1 to VB-16 in its
  canonical form (the kit's frozen definition and axiom checklist) costs
  P_v := ⌈log₂ 16⌉ = 4 bits, the price of selecting it from the menu. A canonical form
  is the generic structure with its defining axioms: it fixes no instance, parameter,
  graph, group, measure, unit or value. **All
  card-specific content of the item** — the particular metric, Hamiltonian, measure,
  locality graph, symmetry, time unit or charge, its parameters and any added axiom — is
  part of the card's statement or inputs and is priced there (IP-1 to IP-5), never
  hidden inside the item. A non-canonical variant (modified axioms) costs
  L_stmt(modified definition) + 4 bits. Truncation levels (VB-10) are priced under IP-5
  and tested under DC-4. VB-16 used as microscopic reversibility, rather than as a
  parity label, is a PS-5 input priced under IP-7 and governed by NR-12. **Closure:** a
  defined symbol, or a structure that the card's derivations or components use (by the
  responsibility map), whose interpretation satisfies an item's frozen axiom checklist on
  any audit or battery instance, or from which the item is L₀-definable within c_dec bits
  **and is used as that item**, *is* that item; an undeclared match → RELOCATED. A
  structure from which an item is merely definable, but which no derivation uses as that
  item, is not a match. For VB-5, VB-6 and VB-7 a match is decided on the checklist
  alone and requires non-classical structure (a non-simplicial state cone, a
  Hilbert-space representation, or the Born rule): a classical state space (a simplex of
  probability laws), the base tokens of B.1 and the charter's record-law objects never
  match. Closure never applies to verdict patterns: reproducing the quantum-realizable
  supports is not "matching VB-5". Supplying or matching VB-5, VB-6 or VB-7 makes every
  selectivity result RELOCATED (SD0 firewall). Items VB-17 to VB-21 are protected: paying for them never makes them
  generated or creditable (§5.1, §5.6).
- **IP-7 Supplied commitments:** a declared PS-5 structure, or an asymmetry priced under
  NR-5, costs P_X := max(L_stmt(X), ΔF_tgt(X)), where ΔF_tgt(X) := the loss in b_J
  (§2.5) when X is replaced by an independent draw of its type from the charter
  reference measure (the larger loss over two post-freeze seeds). Deleting X is not a
  test. **Pricing never substitutes for generation** (§5.1).
- **IP-8 Imports:** an imported standard component is unfolded into L₀ before every
  firewall and pricing test; price := max(log₂|menu| + its constants, L_stmt(unfolding),
  Σ P_v of the VB items it uses). Its consequences are baseline.
- **IP-9 Case splits:** each branch costs 1 bit plus the price of its condition.
  Branches keyed to scenario names, party or setting counts, dimensions, capacities,
  sizes, resolution or item identity are LOOKUP → RELOCATED. A switch among m sub-laws
  not fixed by a priced, input-decidable condition consumes m budget slots (BU-9).
- **IP-10 Per-instance structure:** a constant or clause whose ablation changes at most
  2 credited verdicts or instances costs max(L_stmt, the bits it flips), and its
  distinctions leave D_sel.
- **IP-11 Lock-side fits:** a constant set on lock data costs log₂(range / posterior
  width) and turns the prediction into a fit that cannot serve as a lock. A law constant
  whose implied value falls within the passing window of a published platform-specific
  value of a candidate LOCK-H dataset is a lock-side fit.
- **IP-12 Selection tax:** τ_sel := log₂(1 + n_drafts), where n_drafts counts every
  distinct 𝒦, or distinct assignment of constants, for which any score, verdict, price
  or chain output was computed or estimated by a program, or recorded in any logged
  artifact, since G2-11
  (2026-10-07). A template counts the number of its instances for which an output was
  computed; symbolic evaluation in a free constant that is then priced under IP-5 counts
  as one draft. Reusing an archived proposal adds log₂(archive size). Self-test objects,
  nulls and kit rejection tests are not drafts. Search code and logs are disclosed in C1;
  undisclosed search voids the card (KU-10). At the owner's pick, log₂ N_frozen is added,
  where N_frozen is the number of frozen CARD-ADMISSIBLE cards at the pick (this moves
  verdicts only toward failure).
- **IP-13 Domain restriction:** max(L_stmt(predicate), log₂ C(N_AI3, ⌈N_AI3·k_ex/N⌉)),
  where N := N_AI3 [A] plus any redraws (§1.5) and k_ex counts every excluded draw,
  committed or redrawn.
- **IP-14 Ontology:** the choice of Ξ's type, alphabet and arity (the declaration of 𝒳:
  sorts, arities, labels) costs max(L_stmt(declaration), log₂ m), with m the IP-4 family
  of types any auditor exhibits; this replaces the declaration term, it is not added to
  it.

### 4.3 Credited content
- **(a) Coupling credit b_J := b_J(ℛ★)** (§2.5). It is awarded only if the MC-4
  discrimination gate passes. Import subtraction applies: coupling that an import alone
  produces is removed.
- **(b) Generated structure is not credited.** Persistence, differentiation and the
  generation of Π, carrier, [h] and T_Π are gates (DIF-1 to DIF-10, §5.5). (FC-3 of the
  working draft, kept.)
- **(c) Selectivity distinctions D_sel** (LOOKUP test only): 1 bit for each verified B-SEL verdict class,
  mandatory or graded, that the card reproduces, up to 10 bits. A class earns its bit
  only if the closest B-CF member (by Hamming distance on the mandatory and graded items)
  gets it wrong, and the reference law admitting every no-signalling support does not
  give the same verdict. Removed: distinctions implied by counted ones or by structural
  facts of the SD0 record (each implication argued); distinctions reproduced under 𝒦_∅
  or 𝒦_𝒮 on Dom_pre, or by a vocabulary item or import alone; IP-10 structure;
  consistency collapse (§15.2); the automatic items SEL-0, SEL-4 and SEL-12.
- **(d) Never counted:** bits on 𝒜_ε; restrictions implied by 𝒮 (RECOVERY);
  definitional relations; consequences of priced inputs alone; holdout successes; credit
  obtained by removing realizations; any credit from the secondary relation.

- **ΔL₀ := b_J − Price** (the compression margin) and **ΔL := b_J + D_sel − Price**
  (the lookup test), computed at p = 6, 10 and 16. b_J uses p★ bits per codimension at
  every p; only prices, and the admissibility of comparison classes in §2.5(b), are
  recomputed at each p.

### 4.4 Compression verdict

| Condition | Verdict |
|---|---|
| ΔL ≤ 0 at p = 10 | **LOOKUP** → CARD-RELOCATED (SD0 rule) |
| ΔL₀ ≥ p★ at p = 10, and ΔL₀ > 0 at p = 16 | **COMPRESSIVE** (SC2 met; p = 6 reported) |
| Otherwise | **NON-COMPRESSIVE** |

### 4.5 Ledger and disputes
- **Mandatory ledger (card field C5):** one row per item — item · class (statement /
  input / vocabulary / supplied commitment / selection / domain / ontology) · L₀
  encoding · bits · hostile family size · rule applied. Then, per credit instance: c_ι
  and κ_ι with the dimension certificates; c_J, κ_J, c_lock, c_fam, N_dist, N_fib; b_J,
  D_sel
  (removals argued), b_meas; Price, ΔL₀ and ΔL at p = 6, 10, 16.
- An ambiguity goes against the card. The higher price an auditor raises governs until
  the owner rules (CV-7). Thresholds are never loosened; they change only by a tightening
  repair (§19.2).

---

## 5. Item 4 — Nonrelocation

### 5.1 Protected structures
- **PS-1 The partition Π**, including the party structure of embedded scenarios.
- **PS-2 The carrier (environmental identity):** which E state variable counts as "the
  environment" (instantaneous versus initial; D5 Remark D3) and the protocol invariance
  of the readout.
- **PS-3 The readout class [h]:** any common-readout axiom, designated observable list,
  or readout clause indexed by protocol.
- **PS-4 The interface class T:** its calibration and any group action on record space.
- **PS-5 Gibbs/KMS/FDT structure, defined operationally:** any input from which a
  standard theorem (cited by the author or exhibited by a reviewer) derives a KMS state,
  detailed balance or microscopic reversibility, an exponential-family stationary law,
  canonical typicality, or a fluctuation–response identity of any order. Examples:
  invariant or thermal measures; temperatures; energy-weighted measures; a conserved
  quantity plus maximum-entropy closure; a reversible kernel; ergodicity plus weak
  coupling; a time-reversal involution plus stationarity.
- **PS-6 The target relation ℛ★**, any relation implying it, any monotone of it, any
  penalty, objective or selection criterion containing it, and any presumed sign or
  identity–response tradeoff.

**Pricing never substitutes for generation.** Supplying PS-1 to PS-4 at any price fails
the corresponding generation gate (CARD-NONGENERATIVE). PS-5 supplied and declared is a
priced commitment whose dependent claims earn 0. PS-6 supplied in any form →
CARD-RELOCATED. FR5 and RULES 1 ("postulates are allowed if priced") govern unprotected
inputs only.

**Prohibited inputs:** memory kernels, viscoelastic constitutive laws and crystalline
order (STATE); R1 calibration data (the BRI1 grid, protocols, calibrated maps and
constants).

**"Supplied"** means present, declared, in any input of the §5.2 inventory, or in a
clause NR-2 flags as target-level. A law that merely *implies* ℛ★ is what Q1 requires; that is
not supplying it. **"Hidden"** means present without being declared in any input of the
inventory (§5.2).

### 5.2 Input inventory
Clauses; Ξ-level data, typings, weights, boundary and initial conditions; 𝒞 constants and
parameter values; priors and reference measures; the type and representation (gauge) of
Ξ; components; Emb with the Ξ→battery and template-to-Ξ maps; the protocol repertoire;
coarse-graining scales, thresholds, tolerances and truncation levels; θ_dict; apparatus
calibrations; scope declarations; imports, unfolded.

### 5.3 Tests (each a finite procedure run by the auditor)
- **NR-0 Inventory closure.** The evaluator reproduces every verdict from the inventory
  alone, and the reference implementation reads nothing else. An undeclared input →
  RELOCATED.
- **NR-1 Vocabulary firewall** (syntactic; definitions and imports unfolded; scope 𝒦,
  𝒞, 𝒳, priors and Emb — components are governed by PC-6 and PC-7). Flag any symbol
  that names or encodes a protected structure: Π or S/E labels and typed sorts or
  blockings of V_Ξ that pre-split the relata; h, [h] or readout maps; T or record-space
  group actions; Γ, Obs, ε, P★, d_op or "carrier"; invariant, thermal, prior or
  reference measures and weights, temperatures, Gibbs, KMS, FDT, Onsager; target-level
  coordinates or ℛ. A transition rule of 𝒦, stochastic or not, is flagged only where its
  unfolded statement names or encodes a PS-5 structure (a temperature; a Gibbs,
  energy-weighted or maximum-entropy form; an explicit reversibility, detailed-balance
  or KMS condition; an invariant or reference measure). PS-5 structure that a standard
  theorem derives from an unflagged rule is generated: it is governed by NR-12(b) and
  NR-17's last sentence, not flagged here. Flagged and declared →
  SUPPLIED; flagged and undeclared → RELOCATED.
- **NR-2 Target-level firewall.** A clause or component is target-level if it mentions
  records, chart coordinates, ε, interface maps, partition labels or readouts. RELOCATED
  if, up to representation moves and unfolding, the target-level clauses with 𝒮 imply
  ℛ★ on 𝒟, or ℛ★ is a clause, a conjunct, or a consequence of the clauses that mention
  only observable-level or pipeline terms.
- **NR-3 Two-witness (W-pipe).** For each claimed generated X ∈ {Π, Z_Π, [h], T_Π,
  Gibbs/FDT if claimed, ℛ★}: for X = Π, some Ξ ∈ Dom_pre ∖ Sol with no persistent
  nontrivial Π, or with VI_norm > δ_Π from every Π realized on Sol of the same instance;
  for every other X, some Ξ ∈ Dom_gate^X ∖ Sol whose
  pipeline yields a **defined and different** X (carrier FAIL, a different readout or
  interface class, or a Q4 violation of ℛ★). "Lacks X" counts only for Π. No W-pipe → X
  RELOCATED (into the type, the pipeline or the representation).
- **NR-4 Law ablation and responsibility map.** Run the pipeline on Dom_pre with 𝒦
  replaced by 𝒦_∅ (type only), then by 𝒦_𝒮 (type plus 𝒮), then with single clauses
  deleted. If X appears under 𝒦_∅ on a reference-measure fraction ≥ p_dec [A] of
  Dom_gate^X (for X = ℛ★ the threshold p_dec is replaced by 1/Q_min), or on such a
  fraction of Dom_gate^X(ι) at every lock-fiber instance ι → RELOCATED. If it appears under 𝒦_𝒮 but
  not under 𝒦_∅ → STANDARD-IMPLIED. ℛ★ "appears" at Ξ if Ξ's defined pipeline image
  satisfies ℛ★ within r_lock; ℛ★ appears under an ablated law if it does so on a
  reference-measure fraction ≥ 1/Q_min of Dom_gate (the transplant threshold of Q3(c)). Any internal copy of a law clause inside a component (PC-6) is
  ablated together with 𝒦. The responsibility map is recorded and feeds Q4, Q11, D_sel, JN and the
  GRAVEYARD return test.
- **NR-5 Symmetric-input probe** (mandatory). On AI-2 instances (Aut transitive on V
  or on the candidate partitions), every solution carries a persistent, nontrivial,
  A-stable Π, and {Π(Ξ)} is Aut-invariant, reported as an orbit. A symmetry-breaking
  parameter λ in 𝒞 is evaluated at λ = 0 (if in the domain), 2^(−p★) and 2^(−2p★);
  differentiation must persist at all three, and only which side carries which label may
  follow the sign of λ. **Generalization:** for any protected X with a group of input
  transformations acting transitively on X's alternatives, a G-invariant input must still
  yield some persistent X up to 𝒦's own symmetry; an X that appears only on
  non-invariant inputs and moves equivariantly with them was supplied. If 𝒞's type
  cannot be symmetric, its asymmetry is priced under IP-7 as a supplied commitment, NR-6
  and NR-7 apply at full strength, and Π cannot be GENERATED-STRONG. Fail →
  CARD-NONGENERATIVE.
- **NR-6 Decoder test.** A decoder reads only the inventory, is uniform, and may not
  invoke 𝒦's selection, fixed-point, solver or evolution step. It **fires** if it
  recovers X within tolerance (VI_norm ≤ δ_Π for Π; the same class for T and [h]; the
  same variable for the carrier) on a fraction ≥ p_dec of AI-3 or on every lock-fiber
  instance. The RB and SPS templates (§5.4) always run, whatever their cost; as decoders
  they read only the inventory (an SPS template applied to the realized dynamics of Sol
  is not a decoder; a match there is STANDARD-MECHANISM, §15.7(viii), never RELOCATED).
  Any other decoder costs at most ℓ_dec := max(½·log₂|𝒜_X(ι)|, c_dec) [A]. Decoders may be
  exhibited by the Intake auditor, the Evaluator or the Comparator panel until S9
  completes. For T_Π, [h] and the carrier, a decoder must read some instance input; a
  "decoder" whose output is the same on every instance is not a decoder, and whether a
  structure that is the same on every instance was supplied is decided by NR-3, NR-4
  and NR-10(f), (k). Fires → X RELOCATED in that input. Passing is graded "NOT FOUND within the
  hostile window", never "proved unencoded".
- **NR-7 Scramble.** Replace each priced input datum (𝒞 constants and parameter values,
  tables, priors, θ_dict, Emb's numeric content, coarse-graining scales and thresholds),
  and each numeric constant or table inside a §1.2 component, by an independent draw of
  its type from the reference measure. The components' L₀ structure is not scrambled,
  and the extractor of X is never scrambled when X is tested. If a decoder of cost
  ≤ ℓ_dec that reads the scrambled datum recovers the scrambled instance's X on a
  fraction ≥ p_dec of draws (X tracks the datum), that datum carries X: RELOCATED.
- **NR-8 Representation.** Apply RM1–RM5 and the declared moves with post-freeze seeds.
  A non-covariant X is INVALID (not generated); an X moved by a declared gauge move is
  RELOCATED in the representation.
- **NR-9 Prior ablation.** Remove the law and keep the prior: if X appears → RELOCATED
  in the prior. Replace the prior by the reference measure and keep the law: if X
  disappears → RELOCATED in the prior.
- **NR-10 Carrier, readout and interface.** All must hold:
  - (a) no clause of 𝒦, Emb or any §1.2 component is indexed by protocol identity
    beyond the protocol's action on S;
  - (b) the common-carrier form is proved for every A ∈ 𝔄 and every protocol in
    A_{r★★};
  - (c) Z_Π is derived from 𝒦 under PC-6, with the NR-3 carrier W-pipe;
  - (d) for every family read as reciprocity, 𝒦 excludes (or classifies as a
    non-solution) both the exact product-latent representation (D5 Theorem D1) and its
    causal prefix-tree version (D2);
  - (e) **E2 test:** on any instance on which the two-mode configuration is expressible
    in the sense of (n) (a
    symmetric mode read by a₀; the symmetric mode plus a skewed mode read by the driven
    protocol; an environment law independent of the protocol), the carrier derivation
    does not return PASS (it returns FAIL, MODE SELECTION or ⊥);
  - (f) no input names or encodes a record-space group action or a readout class beyond
    the L₀ arithmetic of Obs's codomain (a designated group, metric, order, partition or
    calibration map). A component supplies a class or group (PS-3/PS-4) if its output is
    the same at every Ξ ∈ Dom_gate^X as a function of its definition alone, or if it
    selects, by a branch (ite, case split, table or threshold) on any condition, among
    classes, groups or readouts that its definition names (identifies by a constant
    symbol, literal or menu index) rather than constructs from Ξ-level structure. A case
    split inside a construction, or the selection of a Ξ-variable as readout by an
    extremal or threshold criterion, is not a named choice; it is tested by NR-3, NR-6
    and DEF-17(a). T_Π ≠ Aut(R) for any such named or encoded structure
    R; the kit verifies T_Π's generators on the chart. A T_Π equal to a catalogue class
    is GENERATED only when X_T computes it as the group generated by maps it constructs
    from Ξ-level structure without naming any class, NR-3 shows that the same
    construction yields a different group off Sol, and NR-10 is otherwise clean (§1.4);
  - (g) T_Π and [h] are computed without R1 calibration data;
  - (h) [h] is invariant under every 𝒦-preserving representation move, verified
    against a declared generating set;
  - (i) the card names the 𝒦-internal property that excludes the product-latent
    representation for this Ξ, and that property survives NR-6: it is not L₀-equivalent,
    within c_dec bits, to "the readout is a function of the instantaneous state";
  - (j) each Appendix-G item the carrier claim uses is derived from 𝒦 or marked
    SUPPLIED (→ CARD-NONGENERATIVE);
  - (k) T_Π is SUPPLIED if it equals, or is L₀-definable within c_dec bits from, a
    symmetry group, invariance requirement or calibration map stated in 𝒦 or its inputs;
    calibration maps exist only as an apparatus layer outside T_Π, and ℛ★ may not
    depend on them;
  - (l) where the auditor can express the product-latent twin (§15.6) in the declared
    type, X_h and X_T applied to the twin return carrier FAIL or MODE SELECTION;
  - (m) Z_Π, [h]_{T_Π} and T_Π are unchanged under horizon doubling (2·H_hor) and the
    scale window, at r★ and r★★ (objective *persistent* carrier and readout, G2-11);
  - (n) expressibility in (e) and (l) concerns the environment's latent state, not the
    readout. The configuration of (e), or the twin of (l), is expressible if, on some
    instance of the declared type (any size the type admits; the auditor chooses), the
    E-state space can carry the configuration's latent state; the auditor supplies, at no
    price to the card, the protocol-indexed readout the configuration needs. At a Ξ of
    such an instance at which X_Π and X_Z are defined (if there is none, the card's
    realized Π and Z_Π from a lock fiber are substituted, as in Q3(c)), X_h and X_T,
    given that readout, must not return carrier PASS. If no instance of the declared type can carry that latent state for some
    realized record family, and the card's carrier derivation (C7) uses that
    inexpressibility, the exclusion is carried by the type: the carrier is SUPPLIED
    (→ CARD-NONGENERATIVE).
- **NR-11 Mode selection.** Readouts h_a ∉ [h]_{T_Π} make the carrier FAIL. Every
  ε-relation then earns no reciprocity credit, the R1 verdict is read from the unchanged
  table (MODE SELECTION where the T-orbits differ, R1-NULL where they coincide), and the
  lock is void (kit control: HB-9 must return MODE SELECTION). PC-7(d) boundary ablation
  applies.
- **NR-12 Gibbs/FDT premises.**
  - (a) PS-5 items are absent from the inputs, or declared and priced.
  - (b) Every premise of each credited derivation is listed. If any premise is a PS-5
    structure (an invariant, Gibbs or KMS measure; detailed balance; an FDT kernel; a
    fluctuation-theorem premise; Onsager symmetry), **whether supplied, hidden or
    generated by 𝒦**, then every claim whose derivation passes through it is
    STANDARD-IMPLIED and earns 0. Generation changes only the label of the premise
    itself (SUPPLIED → RECOVERY), never the status of its consequences. A hidden premise →
    RELOCATED.
  - (c) **Substitution test:** replace Sol by standard models with the same PS-5 premise
    and the same H(x); if ℛ★ holds on all of them → STANDARD-IMPLIED.
  - (d) On an instance whose reference state is not KMS, if ℛ★'s credited content
    vanishes there, it lived in FDT and earns 0.
- **NR-13 Neutrality.** No objective, penalty or selection criterion is monotone in ℛ★
  or has ℛ★ as its stationarity condition, and no sign is presumed.
- **NR-14 Exclusion audit:** the STATE exclusions, IP-9 branches, R1 calibration data.
- **NR-15 No promissory structure.** Every structure claimed as generated is computed by
  the card's frozen algorithms at r★ and r★★. A premise not proved at card freeze counts
  as SUPPLIED. "To be derived later" means SUPPLIED, and no follow-up may supply it
  (§20).
- **NR-16 Battery independence.** A preregistered one-sided binomial test at the
  Appendix-A level compares the holdout failure rate with the public failure rate.
  Rejection → BATTERY-TUNED, reported as RELOCATED.
- **NR-17 Joint necessity (JN).** Consider any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the
  author or a reviewer in which 𝒦₂ does not imply 𝒦₁ on Dom_pre. A Ξ-level predicate
  R ⊇ Sol may be offered as 𝒦₂ (since 𝒦 ≡ 𝒦 ∧ R) only if Price_min(R) is strictly
  below Price_min(𝒦), the L_stmt of the shortest statement of 𝒦 exhibited by any party;
  so 𝒦 ∨ X, 𝒦 with points added, or any restatement of 𝒦 is never a split, while R may
  contain clauses of 𝒦. Let Price_min(𝒦₂)
  be the L_stmt of the shortest L₀ statement equivalent to 𝒦₂ on Dom_pre exhibited by
  any party, and **L★** the L_stmt of ℛ★ written with Π, Z_Π, [h], T_Π, Γ_Π, ε, d_op
  and the frozen chart coordinates as primitive symbols, one token each. If
  Price_min(𝒦₂) ≤ L★ + c_dec, and either
  - (a) 𝒦₂ alone implies ℛ★ with Π, Z_Π, [h], T_Π and Γ_Π treated as free variables; or
  - (b) on every lock-fiber instance, ℛ★ holds within r_lock on the defined pipeline
    image of a fraction ≥ 1 − 1/Q_min of Dom_gate(ι) ∩ Sol(𝒦₂) (reference measure if that
    set has positive reference measure; otherwise the natural measure of its
    top-dimensional part; if neither exists, (b) does not fire),

  then ℛ★ is **imposed, not forced**: RELOCATED on the target relation. Novelty at the
  assembled-law level does not override this. A 𝒦₂ that is, or is L₀-equivalent within
  c_dec bits to, a PS-5 structure generated by 𝒦 is assessed under NR-12(b) as a premise
  of ℛ★'s derivation (STANDARD-IMPLIED; CT-75): JN is recorded for it, not applied.

### 5.4 Decoder templates
- **RB, the reader battery** (cost = template index plus parameters, in L₀ bits): RB1
  any input label or sort; RB2 threshold or top-n of any input weight; RB3 connected
  components, k-cores or degree thresholds of any input relation or its complement; RB4
  blocks of the finest module decomposition of any input matrix or relation; RB5 unions
  of orbits of Aut(inputs); RB6 balls of any radius around an input-designated element
  in any input distance.
- **SPS, the standard partition selectors:** min-cut, max-cut, spectral bisection and
  modularity on any graph or weight structure in 𝒞 or in the realized dynamics;
  conserved-charge and symmetry-sector partitions; explicit labelling; slow/fast splits
  by timescale; heterogeneity thresholds; support co-occurrence; for [h],
  "most-coupled-variable" readouts and declared observable lists.

### 5.5 Generation grades
- **Π GENERATED-STRONG:** NR-5 passes on a transitive instance on which every solution
  has a persistent nontrivial Π; at least one lock fiber is drawn from such instances
  and also passes the b_Π size test (so its symmetry group cannot be the full symmetric
  group at the frozen sizes); every other NR test is clean.
- **Π GENERATED-WEAK:** NR-5 passes (or 𝒞's asymmetry is priced), no decoder is found,
  and every other test is clean.
- **Carrier, [h] and T_Π GENERATED** iff NR-3, NR-4, NR-10(a)–(n) and DIF-5(a)–(e) are
  clean and T_Π ∈ 𝕃_T^adm.
- Every grade reads "no decoder found within the hostile window".

### 5.6 Consequences

| Finding | Consequence |
|---|---|
| A protected structure RELOCATED (hidden) | **CARD-RELOCATED**; after external check, a GRAVEYARD line "RELOCATED in ⟨input⟩" |
| Π, carrier, [h] or T_Π SUPPLIED, even when declared | **CARD-NONGENERATIVE** |
| Gibbs/FDT SUPPLIED and declared | COMMITMENT priced under IP-7; every dependent claim earns 0; if the derivation of ℛ★ uses it → **CARD-RELOCATED** |
| ℛ★ (or content implying it) supplied; or ℛ★ fails JN | **CARD-RELOCATED** |
| A STATE-excluded input, or R1 calibration data | **CARD-RELOCATED** |
| STANDARD-IMPLIED (single claim) | That claim is not credited |
| INVALID (non-covariant) | **CARD-NONGENERATIVE** |
| Illicit upstream read (PC-6) | **CARD-DEFINITIONAL** for every relation coupled through it |

---

## 6. Item 5 — Budget and genuine distinctness
- **BU-1** At most **three frozen cards** for the whole generative route, Stages 3–6
  included. **There is no fourth card.**
- **BU-2** A slot is consumed at commit (the card has a freeze SHA), whatever happens
  afterwards. Withdrawn, INCOMPLETE, VARIANT and intake-rejected cards consume slots.
- **BU-3 Modification.** Any change after freeze makes a new card: statement, constants,
  type, components, truncation, tolerances, scope, response scope, kill conditions, ℛ★,
  battery predictions, domain predicate, lock design, transfer plan. A change made after
  any score was visible is labelled REPAIR. The only exception is a tooling repair
  (§19.2).
- **BU-4 Genuinely distinct.** Card K_j is distinct from every earlier K_i only if:
  - (a) their normal forms differ by more than numeric literals, thresholds, renaming or
    equivalent rewriting;
  - (b) a certified point lies in the symmetric difference of their realized sets (on
    AI-1, AI-2, AI-4 or a lock fiber), or their SEL verdict vectors differ;
  - (c) a certified point lies in Z(ℛ★_i) Δ Z(ℛ★_j) within FB;
  - (d) K_j is not a variant of K_i: **VAR-1** a translation of price ≤ ℓ_tr [A]
    (representation moves, renaming, reparametrization of constants) maps Sol(K_i) onto
    Sol(K_j) on the battery universe (the battery, AI-1 to AI-3 and the lock fibers; the
    card bears the burden; the auditor's search is capped at R_item); **VAR-2** the same normalized skeleton with
    different constants; **VAR-3 patch:** one clause added or deleted, one conjunct or
    disjunct changed, one clause changed by VAR-1/VAR-2, K_j = K_i ∧ Q with Q changing
    battery verdicts only where K_i failed, or clause changes worth ≤ b_patch [A] bits in
    total; **VAR-4** a changed scope, battery exclusion, extractor, tolerance, truncation
    or response scope; **VAR-5** a conjunction or disjunction of earlier cards or their
    clause sets; **VAR-6** a composition of VAR-1 to VAR-5 with total edit ≤
    max(3·b_patch, 25% of K_i's clauses), or that preserves the clauses carrying ℛ★ and
    Π;
  - (e) **mechanism distinctness:** the clause sets carrying ℛ★ and Π in the NR-4
    responsibility maps are not equivalent under VAR-1 or VAR-2.

  Failure → **CARD-VARIANT**, slot consumed. The author names the nearest earlier card
  and argues distinctness; the Intake auditor rules; disputes go to the owner, and the
  card counts as a VARIANT until the owner rules.
- **BU-5 Draft ledger.** Every draft and every evaluated instance (IP-12) is logged with
  a hash and time. A draft found unlogged later → repricing with the corrected n_drafts,
  flagged; deliberate non-disclosure → KU-10.
- **BU-6 Sequential evaluation with fresh sealed draws.** Each card is frozen, then
  scored, then reported to the owner before the next card is drafted. A later card may
  learn from earlier verdicts. The price of that learning:
  - the VARIANT rules (BU-4) and the selection tax (IP-12, counting every draft since
    G2-11);
  - sealed items (AI-3 seeds, credit-family draws, holdouts, lock datasets) are drawn
    after each card's freeze by a fresh Selector context that has seen no card's
    statement, evaluation or report, from pools from which every item unsealed or
    evaluated for an earlier card has been removed; such items join the public battery
    for later cards (§15.9);
  - every decoder, witness family, transplant draw and comparator argument used on an
    earlier card is re-run on every later card;
  - every intake ruling on a disputed NR-1, NR-2, S1 or S2 point is recorded as an
    interpretation CI-n before the next card is drafted; it applies to that card and
    going forward (CV-7);
  - **clock:** card j+1 must be frozen within D_card [A] of the later of the owner
    checkpoint on card j and the recording of every CI-n required before the next draft; otherwise the unused slots are forfeit and T-3(a) is evaluated. Declaring the
    final count also forfeits the unused slots.
  - The owner commits the pick order among frozen ADMISSIBLE cards before any lock datum
    is unsealed (BU-7).
- **BU-7 Owner's pick.** Only among CARD-ADMISSIBLE cards; it costs log₂ N_frozen bits.
  If the picked card fails Stage 4 or 5, the owner may take another frozen ADMISSIBLE
  card, unmodified.
- **BU-7′ No lock reuse.** An unsealed lock dataset never serves another card. Cards
  sharing a lock observable on a shared platform class are a VARIANT pair. Lock
  thresholds use the fixed adjustment of MC-9.
- **BU-8 No budget laundering.** Any artifact that states a law in L₀ for evaluation is a
  card. "Proto-laws", "lemma cards" and "pre-cards" are prohibited. Exempt: the §24.2
  self-tests, the §19.3 rejection tests and the §15.6 nulls — charter controls built from
  known objects or standard models. They consume no slot, are not 𝒦 drafts for IP-12,
  and may not be submitted as cards.
- **BU-9 Sub-law switches.** A card containing a switch among m sub-laws not fixed by a
  priced, input-decidable condition consumes m slots; if that exceeds the budget, it is
  CARD-VARIANT.

---

## 7. Item 6 — Required card contents and kill conditions

### 7.1 Required contents

| G2-11 required content | Template fields (§17) |
|---|---|
| Exact law | C2, C3, C4 |
| Information price | C5, C6 |
| Generated structures | C7 |
| Measurable target | C8, C13 |
| Hostile baseline comparison | C12 |
| Kill condition | C14 |
| Declared response scope (addition 4) | C9 |

A missing or empty field → **CARD-INCOMPLETE**; the slot is consumed.

### 7.2 Universal kill conditions (automatic for every card)

| ID | Kill condition |
|---|---|
| KU-1 | Sol empty on an in-domain instance at r★ or r★★, or Sol = 𝒳 |
| KU-2 | Causality violated: later protocol segments signal into earlier records; superluminal signalling between blocks of a spatial embedding; pNS violated in a Bell embedding |
| KU-3 | Positivity violated: negative probabilities; non-CP record maps; negative spectral densities; negative entropy production under RH-TH |
| KU-4 | An experimentally established standard relation is contradicted inside its tested domain (FDT/KMS in equilibrium, Onsager–Casimir near equilibrium, energy–momentum conservation, the second law), or a standard consequence of a regime whose hypotheses the card's own construction meets. The card cites tested domains at freeze; the auditor may add; in doubt, inside. Sole exception: the contradiction is the declared ℛ★ and is consistent with existing bounds cited at freeze |
| KU-5 | A mandatory ALLOW anchor is forbidden (§15.8) |
| KU-6 | B-REC is contradicted while those environments are claimed as realizable |
| KU-7 | ℛ★, or the declared secondary relation, fails any of Q1–Q12 |
| KU-8 | A protected structure is RELOCATED |
| KU-9 | A GRAVEYARD idea returns at card level (§21.2) |
| KU-10 | Undisclosed search, or modification after freeze: the card is void |
| KU-11 | ΔL₀ < p★ at p = 10, or ΔL₀ ≤ 0 at p = 16 (§4.4) |
| KU-12 | LOCK-FALSIFIED (LOCK-VOID included) on any observable of any registered relation; or a G5-HOLD holdout violates ℛ★ inside the declared scope |
| KU-13 | A card-specific kill condition fires |

### 7.3 Card-specific kill conditions
Each card states its own kill conditions, which together meet:
- **KP-1** finite and decidable on the frozen battery, or a named experimental outcome;
- **KP-2** reachable: some 𝒮-admissible, realizable outcome triggers each one (a vacuous
  kill condition makes the card CARD-INCOMPLETE);
- **KP-3** decided on post-freeze seeds, sealed holdouts or the lock (kill conditions
  decided on public items are consistency checks and do not count toward KP-5);
- **KP-4** automatic, with no reinterpretation after the fact;
- **KP-5 coverage:** at least one observable kill condition on ℛ★ with a threshold; at
  least one structural kill condition decidable at Stage 4 from the frozen kit and the
  card's reference implementation; at least one on B-SEL or B-DIF.

**No rescue.** Once a kill fires, the card is not repaired.

---
## 8. Item 7 — Originality (assembled-law level)
- **OR-1** Familiar component theories are allowed and expected. Familiarity is neither
  a defect nor a credit.
- **OR-2** Novelty is judged **only for the assembled law**: 𝒦 with its generated chain,
  its qualifying relation and its realized joint set, and only for a card whose ℛ★
  survives JN (NR-17).
- **OR-3 Conjunction test** (mandatory comparator). Take the conjunction C₁ ∧ … ∧ C_m of
  the card's components, each in its standard form, together with 𝒮. If ℛ★ follows
  without the card's coupling clauses (located by NR-4), ℛ★ is not novel.
- **OR-4 Comparator floor.** The auditor may add comparators; none may be removed; each
  is verified against primary sources at audit time.
  - **SFP-1** Linear and nonlinear response: Kubo; higher-order FDRs
    (Stratonovich–Efremov; Bochkov–Kuzovlev); Kramers–Kronig; sum rules.
  - **SFP-2** Equilibrium and nonequilibrium statistical mechanics: KMS and FDT;
    fluctuation theorems (Jarzynski, Crooks, Bochkov–Kuzovlev, Evans–Searles,
    Gallavotti–Cohen); NESS response (Agarwal; Harada–Sasa; Baiesi–Maes–Wynants;
    Seifert–Speck; Prost–Joanny–Parrondo); effective-temperature FDRs
    (Cugliandolo–Kurchan–Peliti); frenetic higher-order response; TURs; stochastic
    thermodynamics; typicality, ETH, GGE.
  - **SFP-3** Reciprocity: Onsager–Casimir; dynamical reciprocity; nonlinear reciprocity
    (Andrieux–Gaspard); Lorentz, Rayleigh–Carson, Betti–Maxwell, Helmholtz reciprocity;
    S-matrix symmetry.
  - **SFP-4** Projection and GLE: Mori–Zwanzig; Ford–Kac–Mazur; Caldeira–Leggett;
    Feynman–Vernon.
  - **SFP-5** Open systems and measurement: GKSL; Davies; Redfield; process tensors;
    input–output theory; quantum regression; imprecision–back-action and the SQL; full
    counting statistics and environmental-feedback corrections (Levitov–Lesovik; Nagaev;
    Beenakker–Kindermann–Nazarov); einselection, quantum Darwinism, Brandão–Piani–Horodecki
    objectivity; information–disturbance relations.
  - **SFP-6** Dissipative field theory: Schwinger–Keldysh EFT with dynamical KMS; MSR /
    Janssen–De Dominicis; GENERIC.
  - **SFP-7** Differentiation and subsystems: SSB, Landau theory, Goldstone,
    Mermin–Wagner–Hohenberg, Halperin–Hohenberg; critical phenomena and RG; Turing
    patterns; Cahn–Hilliard; slow manifolds; near-decomposability (Simon–Ando);
    lumpability (Kemeny–Snell); observable-induced tensor-product structures (Zanardi;
    Zanardi–Lidar–Lloyd); quantum mereology (Carroll–Singh); Markov blankets (Pearl;
    Friston); coarse-graining and causal emergence; conserved-charge sectors; graph
    decompositions; community-detection baselines; Lieb–Robinson bounds.
  - **SFP-8** The ten D5 comparators, applied to ℛ★ (not to ε_R).
  - **SFP-9** Readout classes: measurement invariance; Stevens scale types; IRT linking
    and equating; interventional-CRL identifiability classes.
  - **SFP-10** The correlation sector: Abramsky–Brandenburger and AvN; KS sets; Local
    Orthogonality; reconstructions (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller);
    JGBB polygons and boxworld; bounded-width CSP and operator assignment
    (Atserias–Kolaitis–Severini; Bulatov–Živný; Ciardo; Ó Conghaile); Slofstra.
  - **SFP-11** Constructor theory (GY-1).
- **OR-5 Categories** (preregistered; the mathematics (M) and the physical relation (P)
  are classified separately; none is favoured):

| Category | Meaning |
|---|---|
| RESTATED | Up to representation, the image of Sol equals an existing framework's image; no new relation |
| KNOWN ASSEMBLY | The combination already exists in the literature |
| STANDARD COMPONENTS, NEW ASSEMBLY, NO NEW RELATION | Every credited relation follows from the conjunction test or a comparator |
| DISTINCTIVE | ℛ★ passes Q1–Q12, survives JN, and neither any comparator nor the conjunction imposes it |

  **Only DISTINCTIVE (P) for ℛ★ makes a card ADMISSIBLE**; it is re-confirmed at
  G5-LOCK. A middle category may be banked as a COMPRESSIVE known or assembled sector
  only if S6 still passes when recomputed with c_J(b) and the §2.5 family cap; never as a
  law.
- **OR-6 Procedure.** Each comparator family gets an analyst and a skeptic instructed to
  argue RESTATED. The more conservative of the verdicts that meet CV-3 governs: a
  RESTATED, KNOWN ASSEMBLY or NO NEW RELATION verdict must exhibit the derivation, or the
  primary-source result, that imposes ℛ★. The audit is complete, with every floor
  comparator returned, within T_audit [A] of the card's freeze. Incompleteness caused by
  the author side → CARD-RESTATED; caused by the auditor side → one disclosed re-run of
  the missing families by fresh panels. No novelty claim is made before then (RULES 7).

---

## 9. Item 8 — Cross-sector gold standard: parameter transfer
- **XS-1 Sector:** σ = (platform class, regime hypotheses H_σ, standard description
  F_σ ∈ SFP, observable set O_σ, dataset D_σ). **Sector data are empirical measurements
  on physical systems**; battery items, classifications and theorems are card design and
  never sector data.
- **XS-2 Independence.** Sectors A and B are independent only if FB after §13 admits
  their joint values as a product and:
  - **SI-1 Data:** disjoint datasets frozen by hash; every A quantity hashed and committed
    before any B datum is read; no B datum fixes anything in A.
  - **SI-2 Physics:** no shared degree of freedom, sample or apparatus beyond generic
    calibration standards; F_A and F_B share no parameter standard physics would fit
    jointly.
  - **SI-3 No standard bridge:** the Standard Bridge Panel (FDT/KMS; Onsager;
    Kramers–Kronig and sum rules; dimensional analysis with universality and scaling;
    symmetry and Ward identities; conservation; ensemble equivalence; Mori–Zwanzig; EFT
    matching; CLT and large-N; every item of §13), applied to A's data with B's standard
    parameters, gives an interval for the B target at least Q_min times wider than the
    transfer prediction.
  - **SI-4 Not a replication:** B is not A at another control-parameter value within the
    same H and F_σ.
  - **SI-5 Zero-transfer certificate:** two standard models agree on every A observable
    but differ on the B target, and standard model pairs realize every combination in a
    product box of positive dimension.
- **XS-3 North-Star lock.** A and B lie in different regimes, decided operationally:
  *quantum* — the target changes by at least 3σ between F_σ and its classical limit;
  *thermodynamic* — an RH-TH observable whose large-N limit is essential;
  *gravitational* — F_σ contains gravitational coupling. F_A and F_B are different SFP
  entries.
- **XS-4 Parameter ledger:** θ_K (law constants, frozen at card freeze); θ_dict
  (dictionary constants, count and ranges declared in C20); θ_std,σ (standard parameters
  of sector σ, measured without the target observable); θ_cal (calibration of the ε
  machinery). GRUT-specific parameters are θ_K, θ_dict and every discrete choice.
- **XS-5 Protocol:** (1) fit only θ_dict, on D_A alone, by a frozen procedure, each
  fitted parameter priced and subtracted from TG, and freeze the result by hash;
  (2) measure θ_std,B independently and freeze it by hash before B's target data are
  unsealed; (3) preregister y_B = f_B(θ̂_A) with its band; (4) refit nothing.
- **XS-6 Prohibited (a GRUT-specific fit in B):** adjusting θ_K or θ_dict on B data; any
  new constant; any fitted quantity beyond independently measured, pre-declared apparatus
  constants; any discrete choice made after B's data are accessible (T tier; which Π
  unless 𝒦 selects it; carrier, [h] or representative; scope; protocol subset; grid or
  window; coarse-graining; units; estimator or exclusions); a nuisance fit that absorbs
  the prediction.
- **XS-7 Gold standard.** With F_p(X) := log₂ of the number of 2^(−p) frozen-chart cells
  meeting X; 𝒜_B^base := the post-standard fibered baseline FB of sector B (§2.3) under
  H_σB, after §13, intersected with the interval the Standard Bridge Panel (SI-3) gives
  from A's data; and Im_{𝒦,B}(θ) := the image of Sol_𝒦 in B's frozen chart coordinates: **d_B = 0** (no GRUT-specific degree of freedom adjusted in B), n_B ≥ 1 B
  targets predicted; **TG** := F_p(𝒜_B^base) − F_p(Im_{𝒦,B}(θ̂_A)) ≥ p★;
  **TG_A** := F_p(Im_{𝒦,B}(priors)) − F_p(Im_{𝒦,B}(θ̂_A)) ≥ p★ (at least one parameter
  fixed on D_A sets the B prediction, by the responsibility map); band ≤ ¼ of the
  target's range over 𝒜_B^base; SI-3 ratio ≥ Q_min.
- **XS-8 Not credited:** analogy; shared vocabulary or formalism; dimensional analysis;
  unit conventions; the same functional form with a refitted constant; links inside one
  sector (FDT linking fluctuation and response is **not** cross-sector); same-regime
  replications; local back-reaction used as the predicted quantity in the gravitational
  export.
- **XS-9 Status.** CROSS-SECTOR is awarded only after LOCK-CONFIRMED in B on sealed real
  data under §3.3, plus an external check. **Stage 3 claims none;** a card only declares
  a transfer plan, frozen under BU-3.
- **XS-10 Stage-6 export.** The same 𝒦, unmodified. ε_R is exported with the same
  quotient and distance used at the lock. If 𝒦 generates T_Π per sector, the exported
  class is the same up to isomorphism in every sector, or the export uses the class
  frozen in C20; otherwise the export fails. Local back-reaction sets θ_cal only.

---

## 10. Item 9 — Stopping rule and terminals
- **T-1 Card terminals.** Each frozen card gets exactly one terminal. Screens S0–S8
  always run and are reported; S9 runs on cards that clear S0–S8. The first failing
  screen (§18.2) names the terminal; within one screen, the terminal is the first one
  listed in §18.2 whose condition holds (for S5 the order is Q1 to Q12; a clause's own
  label, such as MODE SELECTION or MC-2's "pin", is recorded under the screen's
  terminal), and every other failure is recorded on the
  GRAVEYARD line. Otherwise the card is **CARD-ADMISSIBLE**.
  UNSCORABLE and UNRESOLVED count as failures and are final within the route. The
  GRAVEYARD line lists every failed screen from S0 to S8, and each listed failure is a
  killed idea for the GRAVEYARD return test, in this route and any later one.
- **T-2 Route terminals** (exhaustive; there is no OPEN terminal):
  **STAGE3-PICK** (the owner picks an ADMISSIBLE card; Stage 4 follows);
  **STAGE3-ROUTE-TERMINATED**; **STAGE3-OWNER-HALT**.
- **T-3 Termination.** The route terminates when any of these holds:
  - (a) the three slots are spent, or the owner declares the final count, with no
    ADMISSIBLE card;
  - (b) every frozen ADMISSIBLE card has failed a Stage-4 or Stage-5 gate
    (LOCK-INCONCLUSIVE counts as a failure; a void caused by the author side is a
    failure; a void caused by the auditor side allows one disclosed reselection);
  - (c) Stage 6 would require modifying 𝒦.

  Termination is recorded in GRAVEYARD (after external check) and in STATE, and the
  stage stops (RULES 4).
- **T-4 Prohibited:** see §20.
- **T-5 Allowed after termination:** banking DERIVED sub-results as a library after
  external check (excluding interface classes, distances, s_T, carrier constructions and
  any result whose stated use is a law ingredient); banking a COMPRESSIVE known or
  assembled sector (OR-5); GRAVEYARD lines and the terminal report; continuing R1's
  non-blocking upgrades; a **new** program only by a new explicit owner ruling naming it
  as a new route, with its own charter and no inherited budget. A new route inherits this
  route's GRAVEYARD and FR standings and cannot cite library items as discharging an FR.

---

## 11. Addition 1 — Merge = provenance, not endorsement
- **PV-1** The merge `86bf5a0` and the boundary `dbfd64b` are provenance markers. They
  change no status; nor does merging this charter, a card or a result.
- **PV-2** Pending items keep their status and their CHECKS lines stay pending: A-BL, F,
  M1–M3, Prop. G, and the D5 analyses (D5 C1–C6, D5 D1–D3).
- **PV-3 No conditional verdicts.** Every credited claim or gate verdict that depends on
  a pending or evidence-grade item is scored **now, under the hostile reading** of that
  item (treated as false or absent wherever that hurts the card). If an external check
  later finds an issue, the affected scores are recomputed under unchanged thresholds
  and may move only toward failure.
- **PV-4** Nothing is banked until its CHECKS line shows an external check with no open
  issue (RULES 8), this charter's freeze commit included.
- **PV-5 Items this charter uses:**

| Item | Role here | Status |
|---|---|---|
| ε_R definition, T_R1, d_op, verdict table, common-carrier commitment, Prop. E/E1/E2, G2-08 certificate (`82d311e`) | ε code, carrier semantics, NR-11 | Frozen pre-result; checked: Claude |
| Theorems A and C | DEF-2, B-REC, HB-2 calibration | DERIVED (R1_SYNTHESIS §6); Theorem C checked (G2-01; `82d311e`) |
| A-BL, F, M1–M3, Prop. G | DEF-2, DEF-5, witness enclosures, Tier-2 zero set, B-REC rate | DERIVED; external check pending (hostile reading, PV-3) |
| BRI1 Tier 2 (`cb81a3b`) | B-REC | DERIVED at evidence grade; checked: Claude |
| D5 C1–C6, D1–D3, reverse-direction relations, M-A/M-A′/M-B, C2-F′ | Baseline, B-REC, DEF-9, DEF-10 | D5 analysis; evidence grade; not externally checked |
| 10-item checklist (Appendix G), instantaneous-state form, Z_A, [h]_T, MI framing | MC-6 (adopted as a Stage-3 rule); not-credited seeds | POST-RESULT seed |
| SD0 counts 2961/1721/1232/8, the 240 gap, 2721, the PR-forcing lemma | B-SEL, kit validation | DERIVED, exact |
| SD0 T1; SD0 T2 (2-SAT equivalence) | D_sel structural discount; B-CF behaviour | SD0 record; T2 unresolved |
| ASP (`aacbc52`) | B-CF member | COMPRESSIVE, known sector (SCOREBOARD #6) |

- **PV-6 Scoreboard mapping** (each after external check): card frozen and ADMISSIBLE →
  COMMITMENT; 𝒦 ⇒ ℛ★ proved → DERIVED; SC2 met → COMPRESSIVE; LOCK-CONFIRMED on sealed
  real data → PREDICTIVE; §9 passed → CROSS-SECTOR; an NR violation or LOOKUP →
  RELOCATED; B-SRB, a comparator or the audit restates it → RESTATED; a kill → GRAVEYARD.

---

## 12. Addition 2 — ε_R is derived
- ε_R = ε[Γ_Π, T_Π] by definition, computed only by charter code from the card's Γ_Π
  and T_Π (and s_T where needed).
- 𝒜_ε is the image of 𝒜_Γ × 𝒜_T. It is never an independent axis, and no bits are ever
  counted on it.
- A qualifying relation restricts the jointly realized (Π, T_Π, Γ_Π) beyond the
  definition (Q2) and couples interface with response (Q5). "ε_R > 0 somewhere" is not
  credited.

**Definitional relations — never credited.**
- **DEF-1** ε_R = ε[Γ_Π, T_Π] and any algebraic rewriting of it.
- **DEF-2** ε_R ≥ 0; ε_R = 0 iff the family is T-separable (Theorems A, A-BL, M1);
  ε_R ≤ 2.
- **DEF-3** ε_R ≡ 0 when |A| = 1.
- **DEF-4** Zero-set monotonicity in T: if T ⊆ T′ and ε^T = 0, then ε^{T′} = 0
  (R1_T_LADDER §2). R1 does not claim that the *value* of ε is monotone in T, because the
  distances are T-adapted; any cross-class value comparison is assessed under DEF-13 and
  DEF-14.
- **DEF-5** Witness bounds with frozen constants and their consequences for any family:
  Theorem F (ε = ½·d_q for two protocols with symmetric P0; ε ≥ ½·|E f_odd|/‖f‖_BL), M2,
  Prop. B, and the rate in Prop. G.
- **DEF-6** Invariance under h ↦ t∘h for t ∈ T.
- **DEF-7** Data-processing and garbling identities; invariance-reduction identities
  (Blackwell plus Lehmann; D5 §3 B).
- **DEF-8** The logic of the R1 verdict table.
- **DEF-9** Triviality and representation statements: Prop. E and E1; D5 Theorems D1,
  D2; ε^{T_univ} ≡ 0; the ladder's time-marginalization facts.
- **DEF-10** D5's four-cell independence of (Markov or not) × (ε zero or positive), and
  its one-way links.
- **DEF-11 Tautology:** any statement true for every well-typed tuple of 𝒟(ι).
- **DEF-12 Pipeline identity:** ℛ holds at every Ξ ∈ Dom_gate(ι) on every in-domain
  instance, whether or not Ξ ∈ Sol; or ℛ follows from the components with the type and
  𝒮 (PC-7).
- **DEF-13 Mathematics of ε:** everything that follows by valid mathematics, published
  or not, from the definitions of ε and d_op at any admissible class (the catalogue 𝒯,
  or T_Π with its s_T) and from the card's component definitions, with any constants —
  including repertoire monotonicity (A ⊆ A′ ⇒ ε(A) ≤ ε(A′)), ½·D_T ≤ ε ≤ D_T with
  D_T := max_{a,b} d_op^T(P_a, T·P_b) wherever d_op^T is an orbit pseudo-metric, the
  time-marginalization and coarse-graining facts, exact two-protocol formulas, witness
  bounds, and every prediction of a full-repertoire or full-grid quantity from
  sub-repertoire, sub-grid, channel-marginal or overlapping-sub-repertoire records of the
  same protocols through these bounds.
- **DEF-14 ε-class coupling:** any coupling between T and Γ carried by the T-argument of
  ε (the class at which ε is evaluated varies across compared points), including
  cross-tier comparisons implied by DEF-4. Hence jointness is tested in fixed-T fibers.
- **DEF-15 Definitional given a hypothesis:** if a single-axis property P (Γ-only, or
  (Π, [h], T)-only) holds on Im, and P ⇒ ℛ is a consequence of DEF-1 to DEF-14, of R1's
  theorems, or of valid mathematics (DEF-11, DEF-13), then ℛ is assessed as P: NONJOINT if P is single-axis, uncredited if P
  is an open (inequality) condition. Examples: nonsingular Gaussian families are
  T_caus- and T_lin-separable in every regime; tier coincidences at record dimension 1;
  Theorem F under any symmetric P0.
- **DEF-16 Self-referential flows:** KMS, detailed-balance or FDT forms relative to a flow
  constructed from the state itself (modular or thermal-time constructions; a time unit
  calibrated on the reference law). KMS-type credit or RECOVERY needs a time evolution
  certified independently, with the FR7 order fixed before the state is considered.
- **DEF-17 The card's own definitions:** (a) the stationarity, fixed-point or extremality
  conditions of any rule the card uses to define Π, [h], T_Π or the carrier, and all
  their consequences; (b) consequences of the card's own persistence or identity
  measures; (c) a relation between two functionals of Γ_Π qualifies only if FB admits
  its violation.

---
## 13. Addition 3 — Baseline after standard theory

### 13.1 Rule
The standard constraint set 𝒮 is imposed **before** any freedom is counted. Relations
implied by 𝒮 earn nothing. 𝒮(x) is the set of relations implied, by any valid derivation
from a published standard theorem (verified against primary sources), by **any** standard
hypothesis that holds at x (BP-4).

### 13.2 Regime hypotheses (a floor; each decided by its operational surrogate)
Each hypothesis is decided on the realized process, at record level, by its surrogate
metric m, mapped to [0, 1] by m ↦ m/(1 + m) when m is unbounded. A hypothesis **holds**
unless its certified defect is at least
**δ_RH := max(2^(−p★), 3·r̂_lock)**, with r̂_lock := the maximum over the card's lock
observables of r_lock/|W|. An undecidable surrogate means the hypothesis holds. Fitting β
or another regime parameter costs the baseline nothing. δ_RH is used throughout (BP-4,
BP-6, §1.5, §13.5).

| RH | Holds when (surrogate) | Imposes |
|---|---|---|
| RH-HAM | S+E evolve under a closed generator at record resolution (map deterministic, invertible, measure-preserving) | STD-3, STD-6 |
| RH-KMS | Reference state of E (or S+E) is KMS/Gibbs for the realized evolution (classical: path law time-reversal invariant with declared parities; quantum: KMS defect at an auditor-fitted β) | STD-3, STD-4(b), STD-8, STD-13 |
| RH-MR | Microreversible dynamics, with parities and field reversal | STD-4(a) |
| RH-DB | Realized generator satisfies classical or quantum detailed balance w.r.t. its reference state, **including detailed balance implied by Kolmogorov's criterion (e.g. on acyclic state graphs)** | STD-3, STD-4(a) |
| RH-LDB | Local detailed balance on each transition | Fluctuation theorems, TURs |
| RH-MK | Records or reduced dynamics Markov at record resolution | STD-3 (NESS forms), STD-7 |
| RH-STAT | Stationary reference process | STD-3 (NESS forms), STD-13 |
| RH-GAU | E Gaussian or harmonic, coupling linear in E's variables | STD-3, STD-7, DEF-15; ε^T = 0 for T ⊇ T_caus |
| RH-SYM(G) | Reference law and dynamics invariant under G | STD-5; G-covariant baseline |
| RH-CQ / RH-GGE | Conserved quantities / generalized Gibbs reference | STD-5; generalized FDT |
| RH-WC | Weak coupling or timescale separation | STD-7, STD-13, STD-15 |
| RH-LIN | Readout is a linear detector of a weakly coupled E observable | STD-7 |
| RH-MF / RH-LOC / RH-ERG | N weakly coupled units with a normalized collective readout / finite generator range, or local or mixing E read by a normalized aggregate / finite correlation length or time | STD-9, STD-13 |
| RH-AN | Record laws analytic in the drive amplitude (order-m Volterra truncation matches records to 2^(−p★) at the template amplitudes) | STD-14, STD-15 |
| RH-NESS / RH-NEQ | Stationary nonequilibrium Markov / small affinities | STD-3 (NESS forms); near-regime Onsager |
| RH-MC | Finite bath, microcanonical reference | Ensemble-equivalence corrections |
| RH-ORD | Ordered phase, critical point or pattern-forming instability | STD-10 |
| RH-TH | Macroscopic thermodynamic limit essential | STD-8 |
| RH-Q | Quantum structure present (noncommuting realized observables, or VB-3/5/6/7) | STD-2 (all of quantum theory and quantum information) |

### 13.3 Standard constraints (floor)
Each line: what it imposes, and what therefore earns **no credit**.
- **STD-1 Causality** (always): non-anticipation; retarded response, Kramers–Kronig,
  sum rules; no-signalling (pNS for multi-block supports; relativistic causality in
  spatial embeddings).
- **STD-2 Positivity** (always): valid probability laws; positive-semidefinite
  covariances and spectral densities (Bochner); CP processes (positive combs; GKSL for
  Markov semigroups). Under RH-Q every theorem of quantum theory and quantum information
  (uncertainty relations, Tsirelson-type bounds, information–disturbance, no-cloning).
- **STD-3 KMS / FDT / fluctuation relations.** Equilibrium forms under RH-KMS with any
  one of RH-HAM, RH-DB or RH-MK; NESS forms under any stationary Markov reference. KMS for
  every multi-time correlator; linear FDT; n-th order response as reference correlators
  with nested commutators or Poisson brackets (Stratonovich–Efremov, Bochkov–Kuzovlev,
  quantum nonlinear FDRs; entropic plus frenetic path-space forms) — KMS converts the
  first order fully and higher orders only partially, so measurable symmetrized
  correlators fix higher-order response only through the cited published forms; fluctuation theorems
  for every protocol; a Gaussian E fixed entirely by (J(ω), β) with its exact exogenous
  decomposition (Feynman–Vernon, Caldeira–Leggett, Ford–Kac–Mazur); NESS forms (Agarwal,
  Seifert–Speck, Harada–Sasa, Baiesi–Maes–Wynants, Prost–Joanny–Parrondo);
  effective-temperature FDRs; generalized FDT under RH-GGE. Under RH-KMS, RH-GAU and
  linear coupling, 𝒜_ε = {0}. Under the BRI1 class, the leading Tier-1 value is fixed by
  the reference 4-point function. **No credit:** any ε value or Γ restriction fixed by
  reference correlators among the BP-5 inputs; any fluctuation-theorem identity;
  "harmonic baths are R1-NULL"; any "response = X · correlation" unless X is predicted
  from interface-side data and beats B-SRB by Q_min.
- **STD-4 Reciprocity:** (a) dynamical reciprocity S_ij = ε_iε_j S_ji under RH-MR or
  RH-DB at any temperature, and Lorentz / Rayleigh–Carson / Betti–Maxwell / Helmholtz
  reciprocity and S-matrix symmetry for time-reversal-symmetric linear dynamics;
  (b) Onsager–Casimir under (a) plus RH-KMS; (c) nonlinear forms (Andrieux–Gaspard) under
  the fluctuation-theorem hypotheses. R1's operational "reciprocity" is a different thing;
  a relation reducing to any of these earns nothing under either name.
- **STD-5 Conservation and symmetry** (RH-CQ, RH-SYM): continuity equations, sum rules,
  Ward identities; energy and momentum balance; charge and superselection partitions as
  standard selectors; Curie and selection rules — a symmetric reference read through a
  covariant interface has no odd statistics (Theorem C's mechanism) — including selection
  rules relative to the unbroken subgroup Stab(Π) of a supplied or generated partition or
  ordered state (Curie, Wigner–Eckart, Landau, Goldstone counting, Halperin–Hohenberg).
- **STD-6 Mori–Zwanzig / GLE** (always, for any linear generator and any projection,
  supplied or generated): exact GLE with memory kernel and projected noise; the second
  FDT under RH-KMS; the Markov limit under RH-WC; harmonic E gives exogenous noise plus
  linear memory exactly. **No credit:** memory, non-Markovianity, viscoelastic response,
  "E carries S's history".
- **STD-7 Open-system and measurement response:** GKSL, Davies, Redfield, quantum
  regression; process tensors; influence functionals; input–output theory; the
  imprecision–back-action bound and the SQL; measurement rate ≤ dephasing rate; full
  counting statistics and environmental-feedback corrections to higher cumulants;
  information–disturbance relations. **No credit:** any interface–response tradeoff of
  these kinds.
- **STD-8 Stability and the second law** (RH-TH or RH-KMS): non-negative entropy
  production; passivity; Clausius; Landauer (with Sagawa–Ueda); positive-definite static
  susceptibilities; Le Chatelier–Braun.
- **STD-9 Large-N, CLT and Edgeworth** (RH-MF, RH-LOC, RH-ERG; whenever a recorded
  quantity is a sum or average over many weakly dependent contributions, with "N"
  including any extensive size of a generated structure — |E_Π|, |∂|, block counts):
  cumulant scaling with N and dilution; Gaussian reservoir limits. **No credit:** scaling
  of ε_R or its witnesses with N, block sizes, or boundary-to-bulk ratios of Π.
- **STD-10 Differentiation–response relations** (RH-ORD): Goldstone;
  Mermin–Wagner–Hohenberg; scaling relations; susceptibility versus correlation length;
  Landau relations; interface tension and capillary-wave statistics; Turing wavelength
  selection; slow-manifold selection of persistent variables.
- **STD-11 Representation freedom** (always): only T-invariants are observable;
  readout classes, maximal invariants, copulas modulo reflections and measurement
  invariance are known mathematics. **No credit** for the existence or form of [h]_T as
  such.
- **STD-12 Universal exogenous representation** (always; mathematics): every
  non-anticipating family has an exact exogenous representation with protocol-dependent
  readouts (Prop. E/E1; D1; D2). **No credit** for any back-reaction claim made from
  records alone, or any relation not involving the derived carrier.
- **STD-13 Regression and rate–response:** Onsager regression (RH-KMS); golden-rule /
  Davies rates and susceptibilities sharing J(ω) (RH-WC); the second FDT; Harada–Sasa;
  Green–Kubo and Einstein relations; Wiener–Khinchin (RH-STAT); matrix-tree response
  equalities for Markov jump networks; Lieb–Robinson light cones (RH-LOC). **No credit:**
  relations between interface dynamics (relaxation of ∂, exchange rates, decay of S–E
  correlation) and response content these results fix.
- **STD-14 Amplitude analyticity** (RH-AN): the leading amplitude power in each
  T-irreducible channel, the ratios across a₊, a₋, a₊₊ that this power and symmetry fix,
  and every relation among scalings or sign-reversals of one template implied by an
  order-m Volterra truncation, m being the smallest order at which RH-AN's surrogate
  holds (at most |A| − 1), or by parity under RH-SYM.
- **STD-15 Power counting** (RH-WC or RH-AN): each witness scales with coupling and drive
  at the lowest nonvanishing order; exponents and leading coefficients expressed through
  E's undriven cumulants and intrinsic response kernels are standard in any regime.

### 13.4 Closure
- The tables above are a floor. The auditor may add any published structural or regime
  hypothesis with an operational test; BP-3 and BP-4 apply to it.
- Membership is **retroactive until banking**: a derivation cited at any time before
  banking removes the credit, and rescoring moves only toward failure.
- Non-standardness is established only constructively (Q3(e)).

### 13.5 Boundary and near-regime rules
- **Boundary rule.** If ℛ★ implies, on a lock fiber, equality in a published standard
  inequality (imprecision–back-action and the SQL; TUR or KUR; Clausius, Landauer or
  Sagawa–Ueda; Cramér–Rao; uncertainty relations; Tsirelson), the baseline is the
  saturating standard subclass under H(x), with every regime in which saturation is a
  published consequence added to H. If a saturating standard subclass realizes Im with
  matching inputs → STANDARD-IMPLIED; otherwise the credit is only the codimension ℛ★
  cuts inside that subclass.
- **Near-regime rule** (BP-4): a hypothesis failing by δ ≥ δ_RH in its frozen metric (relative
  entropy to the nearest KMS state; entropy-production rate; KMS defect at a fitted β)
  still imposes its consequences with published perturbative bounds; J_SRB includes them.

### 13.6 Precedents and RECOVERY
- BRI1's Tier-1 ε_R value lies in 𝒮 (a Kubo/FDT third-cumulant response fixed by P0's
  connected 4-point function; D5). So does any relation expressing ε_R through reference
  correlators of **any** environment with the same reference law, for any driven/recorded
  pair, at any order.
- Generating KMS or Gibbs states, thermalization or memory from dynamics is standard
  (typicality, ETH, Davies, ergodic theory). It earns **RECOVERY**: a Stage-6
  consistency item with zero Stage-3 credit. Its consequences follow NR-12(b).

### 13.7 Regimes where FDT is silent
The baseline is larger there; credit is computed per regime class after the near-regime
rule. Regime shopping is defeated by BP-3, BP-4, §13.5 and the platform-matched lock
fiber (§1.5).

### 13.8 D5 reverse-direction relations (baseline relations comparators give and R1 does not)
(i) For a Gibbs environment driven through any variable, FDT predicts the leading Tier-1
ε from undriven 4-point correlations; (ii) the GLE / linear-response route detects
linear back-reaction; (iii) process-tensor signalling detects the harmonic bath's
response. ℛ★ must be none of these and not implied by them on its lock fibers.

---

## 14. Addition 4 — Response scope
At freeze every relation declares exactly one scope, frozen with the card.
- **SCOPE-Q: quotient-irreducible back-reaction.** The relation constrains Γ only through
  T_Π-invariant content (ε_R, its zero set, its witnesses, the maximal invariant), under
  R1's verdict table. Available **only if T_Π ⊇ E₂±** and the kit verifies ε^{T_Π} = 0
  exactly on HB-1, HB-3, HB-4 and every Gaussian family under linear coupling. ℛ is
  invariant when any T_Π-explainable response is added to Γ, and fails when the card's Π
  is replaced by some Π′ ∈ FB with Γ and T held fixed. It is silent on mean response of
  every order, on linear back-reaction, and on affine or Gaussian latent change;
  linear-response data neither confirm nor refute it.
- **SCOPE-G: response in general.** Observables are response functionals
  (susceptibilities, response functions, noise spectra, transport coefficients), **never
  ε_R alone.** B-SRB applies at full strength, starting with STD-1, 3, 4, 6, 7, 13 and full
  linear-response theory. FB must admit a violation of ℛ when Π or T_Π varies with the
  linear part of Γ held fixed. D5 comparators 2 and 3, in the reverse direction, are
  mandatory baselines.
- **RS-1 R1-NULL does not mean "no response."** A claim "ε_R = 0 ⇒ no back-reaction" or
  "ε_R > 0 ⇒ the environment is nonlinear" is void, and a relation whose derivation uses
  one fails Q10. (The harmonic bath responds yet is R1-NULL; the parametric harmonic
  control escapes both tiers with linear bath dynamics.)
- **RS-2** No cross-subsidy between scopes. **RS-3** SCOPE-Q faces B-REC first (at the
  catalogue classes **and** at T_Π; it must predict ε = 0 wherever RH-GAU with linear coupling
  holds), then B-HB; SCOPE-G faces B-SRB first.
- **RS-4 Mismatches.** A scope/observable mismatch voids the lock. A SCOPE-G relation
  stated only through ε_R is reclassified SCOPE-Q, credit limited to its
  quotient-irreducible part. A SCOPE-Q relation failing the T_Π ⊇ E₂± condition or the
  kit check is reclassified SCOPE-G with full B-SRB.
- **RS-5** No scope declared → CARD-INCOMPLETE; a scope change after freeze is a new
  card. **RS-6** The card states which carrier verdict it expects at measurement and how
  it will be certified (feeds MC-6).

---

## 15. Frozen batteries
The batteries are frozen with the charter; cards may not add, remove or reweight items.
Public items are development data and earn credit only under §4.3(c).

### 15.1 B-SEL: selectivity (the exact SD0 record)
- **Embedding.** Emb is uniform, priced and frozen with the card. It receives **only the
  abstract signature** of a scenario (ports, alphabets, context hypergraph, support),
  with labels scrambled under RM1/RM2 by post-freeze seeds; rays, operator or vector
  representations, quantum witnesses, literature names and file order are withheld;
  verdicts must agree across ≥ 2 seeds. Emb adds no relata, relations or weights beyond a
  uniform image of the incidence structure, and references no scenario name, party or
  setting count, dimension or item. Mapping: measurements → interventions; contexts →
  jointly performed protocol sets (FR6); outcomes → records; **parties and sites →
  generated blocks of Π**.
- **Object:** 𝔖_𝒦(Σ) := {supp Γ_Π : Ξ ∈ Sol_𝒦(Emb(Σ))}, the set of supports of record
  laws. **ALLOW** = the card exhibits or proves a realization with exactly that support;
  **FORBID** = it proves none exists. Verdicts come from the card's single frozen decision
  procedure (DC-10); an undecided item is UNSCORABLE. A card that cannot embed Bell
  scenarios fails G-SEL.

| ID | Instance | Requirement | Class |
|---|---|---|---|
| SEL-0 | Every embedded instance | ∅ ≠ Sol ⊊ 𝒳 | Mandatory (structural; earns 0) |
| SEL-1 | The 1721 possibilistically local (2,2,2) tables | ALLOW all | Mandatory anchor |
| SEL-2 | The Hardy support and its orbit under the 128-element relabelling group | ALLOW | Mandatory anchor |
| SEL-3 | The 8 PR boxes | FORBID all | Mandatory |
| SEL-4 | The 240 pNS (2,2,2) tables with no exact-support realization | FORBID all (as record-law supports) | Mandatory (automatic; earns 0) |
| SEL-5 | GHZ (3,2,2) | ALLOW | Mandatory anchor |
| SEL-6 | Peres–Mermin square | ALLOW | Mandatory anchor |
| SEL-7 | CHTW 3×3 KS game, certified core of 94 rays / 67 triads (abstract signature only) | ALLOW | Mandatory anchor |
| SEL-8 | Mermin pentagram; bipartite magic square; CEG-18 bipartite; GHZ (4,2,2) | ALLOW all | Mandatory anchors |
| SEL-9 | SD-K7(i) family: PR ×8; the 480 strong XOR-(2,3,2) tables; embedded PR (2,3,2); fine-grained PR | FORBID all | Mandatory |
| SEL-10 | Theta parity system {p,q,r} even, {p,q,s} even, {r,s} odd (no operator model) | FORBID | Mandatory |
| SEL-11 | Qubit versus boxworld gbit at capacity 2 | Exclude the gbit's PR realization; the responsibility map has no clause on capacity, dimension, party or setting count | Mandatory audit |
| SEL-12 | Closure: mixing-union over whole admitted families; independent products (Hardy ⊗ GHZ admitted; PR ⊗ PR forbidden) | Respected | Mandatory (structural; earns 0) |
| SEL-13 | Specker triangle; chained-PR 6-cycle; C7 odd-cycle box | FORBID | Graded |
| SEL-14 | Padded-PR (2,2,3) | Reported; no credit | Report |
| SEL-15 | SD0 items G2, G3, H3, H4 | Reported against literature status | Report |
| SEL-16 | Audit against the POVM-inclusive BMT boundary | Recorded; UNRESOLVED allowed for a dimension-blind card | Audit |
| SEL-H | ≥ 3 blind holdouts (§15.9); where the pool allows, one with a shortest known certificate longer than twice the battery maximum | Literature status | Holdout |

- **Grades:** EXACT-ON-BATTERY (every mandatory and graded item passes); OUTER (every
  mandatory item passes, some graded FORBID over-allowed — labelled an outer
  approximation, never upgraded, FR9); NON-SELECTIVE (any mandatory failure).
- **G-SEL PASS** requires at least OUTER, SEL-11 passed, and every SEL-H holdout passed
  (an over-allowed holdout fails G-SEL even for an OUTER card). Consistency collapse
  (§15.2) does not by itself fail G-SEL; it sets D_sel = 0, labels the selectivity a
  KNOWN SECTOR, and makes the SFP-10 comparators mandatory.
- A truncation level priced under IP-5 and used uniformly across items is not a clause
  on dimension for SEL-11, provided every FORBID passes the DC-4 levels n, n+1, 2n.

### 15.2 B-CF: the consistency family
- Members: (j,k)-consistency for j ≤ k ≤ 4; singleton linear arc-consistency; BLP; AIP;
  BLP+AIP; ASP (SCOREBOARD #6); every conjunction or disjunction of two members. The kit
  computes their SEL verdict vectors before Card 1.
- **Consistency collapse** holds if the card's SEL vector is within Hamming distance 1 of
  a B-CF vector on the mandatory and graded items (the differing item is treated as
  IP-10 structure), or if the responsibility map shows the card's FORBID verdicts are
  bounded-width refutations of width ≤ 6, or Sherali–Adams refutations of level ≤ 3,
  which any auditor may exhibit within the hostile window (the kit need not precompute
  them). Then its selectivity is a KNOWN SECTOR, D_sel = 0, and the SFP-10 comparators
  are mandatory in its audit.
- The kit also reports the Hamming distance from every B-CF vector to the all-correct
  vector, as a diagnostic.

### 15.3 B-REC: R1 calibration controls (exact-identity controls; no credit)
Each record is passed through the card's static record maps (the declared static tail
removed, PC-7(b)) into the charter ε code, evaluated **at the catalogue classes 𝒯 and
at T_Π**. For the exogenous controls C2-G, C2-NG, C2-F′, HB-3, HB-4 and HB-5 with
calibrated filters, the required value at T_Π is exactly 0, and HB-8 (E2) never returns
R1-PASS. Each exogenous control (HB-3, HB-4, HB-5 with calibrated filters, C2-F′) is
also run, as an exogenous E-relatum process on AI-1, through the card's per-relatum maps,
aggregation and static tail (PC-7(b)); the control's per-protocol action is applied to
each relatum before the per-relatum maps, and if the relatum state space cannot carry
the control, it enters at the per-relatum maps' outputs and the check covers the
aggregation and tail. These checks run at S4 on **every** card, whether
or not it claims the environments realizable. If any fails, T_Π is not GENERATED and
every relation that uses ε^{T_Π} fails Q8; the failure is recorded at S4 and takes
effect at S5 (Q8), not as an S4 terminal.

| Control | Required value | Grade |
|---|---|---|
| BRI1 X1, Duffing bath, Gibbs; protocols P0, P1, P2; grid (π, 3π/2, 2π) | Theorem C sign structure; ε_R = ½·d_q for two protocols | DERIVED (C checked; F pending) |
| BRI1 rate | liminf N_B·ε_R ≥ abs(K)·V*/(12·m₂^(3/2)), V* = 0.943578 | Prop. G pending |
| BRI1 Tier 2 | R1-PASS (odd 7/7, even 3/3, scaling 1/N_B) | Evidence grade |
| Harmonic twin | ε_R = 0 at both tiers (≈ 1.27×10⁻¹⁴); the bath responds through friction | DERIVED (numerical control) |
| Parametric harmonic control | ε_R > 0 at both tiers, with linear bath dynamics | D5 analysis |
| C2-G, C2-NG | 0 | R1 record |
| C2-F (coloured AR(1)) | > 0 under E₂±; 0 under T_lin with calibrated filters | R1 record |
| C2-F′ (non-Markov exogenous) | 0 | D5 analysis |
| M-A (Markov), M-A′ (non-Markov) | ε_R^{T_R1} ≥ 1.915×10⁻² | D5 analysis |
| M-B | ε_R^mono ≥ 7.98×10⁻³ | Evidence grade |
| E2 | ε_R > 0 with no response; the pipeline never returns R1-PASS | Frozen pre-result |
| Prop. E product latent (HB-9) | MODE SELECTION | Frozen pre-result |

For each control the card also reports whether it lies in Im(Sol) and its ℛ★ value. Any
relation linking ε_R to Markovianity respects DEF-10. Pending rows are scored under PV-3.

### 15.4 B-HB: the hostile standard-model library

| ID | Family | Regime | Role |
|---|---|---|---|
| HB-1 | Harmonic bath, bilinear coupling, Gibbs | G-cl | R1-NULL while responding |
| HB-2 | Duffing / BRI1-class bath, Gibbs; quartic λ ∈ [0, 2] | G-cl | Tier-1 PASS; Kubo third-cumulant response |
| HB-3 | Exogenous Gaussian (C2-G) | X | Exact zero |
| HB-4 | Exogenous affine-entry non-Gaussian (C2-NG) | X | Exact zero |
| HB-5 | Exogenous filtered non-Gaussian with calibrated filters (C2-F, C2-F′) | X | T-dependence of the zero set; non-Markov null |
| HB-6 | Markov responding environment (M-A) and non-Markov variant (M-A′) | N | ε > 0 with and without memory |
| HB-7 | Parametric coupling to a harmonic bath | G-cl | Escapes both tiers with linear bath dynamics |
| HB-8 | Gaussian latent configural change (the E2 class) | X / 0 | ε > 0 with no response |
| HB-9 | Product latent with selection readouts (Prop. E / D1) | — | MODE SELECTION control |
| HB-10 | ≤ 4 qubits or qutrits; local Hamiltonians from a kit-frozen ensemble; KMS reference; Hamiltonian coupling; fixed measurement model | G-q | Quantum standard witnesses |
| HB-11 | Two-temperature or driven steady-state baths | N | Nonequilibrium witnesses |
| HB-12 | Finite Markov jump processes with local detailed balance; discrete records | N / G | Discrete-record chart and RH-DB controls only; not an ε witness |

- **Regime key:** G-cl classical Gibbs; G-q quantum KMS; N nonequilibrium; X exogenous
  (no back-reaction); 0 no response; "/" either.
- **Ranges:** β ∈ [0.25, 4]; frequencies ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8. Members
  may be composed by juxtaposition or coupling.
- **Witness rules:** a card-added witness (for Q3 or dim_lb) counts only if it comes from
  the HB families or their compositions within the frozen ranges, meets BP-3 at the
  hostile fiber, and receives the B-SRB inputs through θ_dict — and only after the
  skeptic fails to refute these. The evaluator adds the draws for Q3(b) and Q3(c).

### 15.5 B-SRB: standard response theory with the reference package
- **Input:** the BP-5 union. **Before anything is unsealed:** J_SRB := hull of o⃗(m) over
  certified regime-matched standard witnesses consistent with every BP-5 input,
  intersected with the region each standard scheme valid under H(x) predicts (with its
  error bars), each scheme's predicted record families pushed through the charter ε and
  witness code at T_Π; then intersected with W.
- J_SRB is never an outer bound from the constraints, a window, or the hull of all
  𝒮-admissible models. Auditor derivations may only shrink it. 𝒮 is closed under valid
  mathematics and under DEF-1 to DEF-17: J_SRB is intersected with the set on which every
  DEF identity among the lock observables holds, and "hull" means the hull within that
  set. "No standard formula exists for this quotient" is not silence: J_SRB is then the
  witness hull. If no two certified
  witnesses differ by more than |J_K|, MC-4 fails.

| Outcome | Verdict |
|---|---|
| J_K ⊇ J_SRB, or b_meas < log₂ Q_min | RESTATED (precedent: BRI1's Tier-1 value is a Kubo/FDT quantity) |
| J_K ∩ J_SRB = ∅ under experimentally established hypotheses | KU-4, unless this contradiction is the declared ℛ★ and consistent with existing bounds |
| Otherwise | PASS; b_meas is computed |

### 15.6 B-NULL: the nulls
- **NULL-ΠT:** Ξ is any SFP model of the declared type; Π, Z, [h] and T chosen by hand;
  Γ = Obs. Its realized set is FB. Required: Im ⊊ FB, and ℛ★ holds on Im and fails on FB.
- **Product-latent (E-B) twin:** for every realized Γ, the auditor builds μ = ⊗_a P_a with
  h_a = π_a, and its causal prefix-tree version. Reciprocity statements rest on a derived
  carrier, else NO RECIPROCITY VERDICT. Where the twin is expressible in the declared
  type, NR-10(l) applies. ℛ★ need not separate the twin. A relation satisfied by the
  twin of every family — the twin's record family paired with the interface the twin's
  own pipeline returns — is record-only and earns no reciprocity credit.
- **Information nulls:** a lookup law ("Ξ is one of the listed realizations") is priced as
  its table and must be beaten; the definitional law (R1 definitions plus the verdict
  table) earns 0; for a maximal-interface null (T ⊇ J or T_univ), ε at such a class is
  void by rule (§1.4) and ε-relations there earn nothing (ε^{T_univ} ≡ 0 is DEF-9; R1
  makes no claim about J); a single-protocol or hand-picked repertoire makes the relation a table; a
  sign-only null carries at most 1 bit and fails Q6.

### 15.7 B-DIF: differentiation
Generated by the Evaluator from the declared type with post-freeze seeds: (i) a W-pipe
search (NR-3); (ii) symmetric instances (NR-5); (iii) a planted, decoupled instance (an
extractor sanity check, no credit); (iv) horizon doubling — at (2η, 2·H_hor) the same
Π;
(v) random solution instances at the declared truncation; (vi) the AI-3 ensemble;
(vii) perturbation instances (DIF-6); (viii) an SPS comparison on the realized dynamics
of Sol on AI-2 and AI-3 (SPS applied to 𝒞 or other inventory items is NR-6, §2.3) — if
Π is extensionally a standard mechanism of the realized dynamics, the result is
STANDARD-MECHANISM (allowed and recorded; no differentiation
novelty; never a relocation), and if ℛ★ is an STD-10 relation it is RESTATED; (ix) the
scale window;
(x) the size test b_Π.

### 15.8 Anchors
- Mandatory ALLOW anchors: SEL-1, SEL-2, SEL-5, SEL-6, SEL-7, SEL-8.
- **Standard-regime anchor:** for every B-REC scenario inside the declared scope, Im(Sol)
  contains at least one triple realized by an experimentally established standard regime
  (equilibrium FDT and Onsager behaviour).
- Forbidding an anchor is a FAIL and fires KU-5. Freedom reduction obtained by forbidding
  anchors or emptying Sol earns nothing.

### 15.9 Sealed holdouts
- **Protocol:** `F0_SD0_HOLDOUT_PROTOCOL_01.md`, adapted. The Selector is invoked only
  after the card's freeze; it receives the protocol, the exclusion lists, the scenario
  conventions and the card's bare input/output signature, and nothing else. The selection
  is committed by hash before any evaluation on the selected cases.
- **Pools:** (a) selectivity — support-level cases with an established classification,
  excluding everything in §15.1, G1–G3, H1–H4 and the whole (2,2,2) scenario, ≥ 3;
  (b) reciprocity — standard-model environments with exactly computable ε_R outside the
  frozen HB parameter points, ≥ 3; before unsealing, the card predicts whether each lies
  in Im(Sol) on the relevant fiber and, if so, its ℛ★ value (a holdout in Im that violates
  ℛ★ is a Q1 failure); (c) AI-5 instances; (d) LOCK-H datasets (MC-8).
- **Sequential cards.** For each card the Selector is a fresh context that has seen no
  card's statement, evaluation or report. Every item unsealed or evaluated for an earlier
  card is removed from the pools and joins the public battery for later cards (a later
  card's verdict on it is a consistency check, KP-3, never holdout evidence). A pool that
  cannot supply the required number of fresh items is an auditor-side void; if the one
  reselection still cannot supply fresh items, the gate is decided on the fresh items
  available, provided at least one exists, and otherwise the item class is reported void
  for that card and does not count against it.
- Holdout results are tallied separately and never enter ΔL or ΔL₀. A failure on an item of
  mandatory type fails the gate. A void caused by the author side → FAIL; by the auditor
  side → one disclosed reselection.

### 15.10 Stage-4 gates (picked card only)
Each gate is recomputed by an agent that did not build the card and checked externally
before banking.
- **G4-SEL:** §15.1 and §15.2 recomputed, including SEL-H.
- **G4-DIF:** **DIF-1** Π computed by the frozen algorithm on every in-domain solution;
  **DIF-2** persistence (δ_Π, η, δ_∂, H_hor with τ_slow; non-vacuous, §1.3) across
  A_{r★★} and the whole horizon, horizon doubling, scale window; **DIF-3** nontrivial, size test included;
  **DIF-4** Π GENERATED-STRONG or GENERATED-WEAK; **DIF-5** carrier, [h] and T_Π
  GENERATED — (a) T_Π ∈ 𝕃_T^adm, (b) nontrivial (some B-REC or B-DIF family has
  ε^{T_Π} > 0 and some has ε^{T_Π} = 0), (c) placed relative to T_R1, T_mono and J,
  (d) not a GY-11 or GY-12 class (behavioural test, §21.2), (e) every exogenous control
  listed in §15.3, passed through the card's static maps (tail, per-relatum maps and
  aggregation), gives ε^{T_Π} = 0, and HB-8 never returns R1-PASS;
  **DIF-6** Π unchanged within δ_Π under relative perturbations of 2^(−p★) to every
  numeric input, preserving Aut(inputs); **DIF-7** universality on all of Sol on every
  in-domain instance, the domain being a decidable predicate frozen in C16 that contains
  AI-1 and AI-2 and covers ≥ θ_gen [A] of the AI-3 draws (priced, IP-13); **DIF-8**
  covariance (NR-8); **DIF-9** the environmental identity across interventions, and the
  environment's state variable, are outputs; **DIF-10** the B-DIF (viii) classification
  recorded.
- **G4-NR:** NR-0 to NR-17 re-run computationally on AI-1 to AI-5; the reader and decoder
  batteries are run by an agent that has not seen the card's derivation of Π.

### 15.11 Stage-5 gates
- **G5-LOCK:** Q1–Q12 and the scope re-verified independently at r★ and r★★; DISTINCTIVE
  (P) re-confirmed; the preregistration is a byte-identical copy of C13 (fields C13
  explicitly deferred to a frozen deterministic rule excepted); MC-5 to MC-11 apply;
  LOCK-INCONCLUSIVE fails.
- **G5-HOLD:** after G5-LOCK, a hostile auditor selects ≥ max(2, number of lock
  observables) holdouts from the ≥ 2·max(2, n_obs) candidate classes listed in C13 plus
  its own. Each is a physically realized system class inside the declared scope that the
  card does not reference; measured data only; hashes committed before evaluation.
  PASS: each holdout meets MC-5's confirmation condition against the J_K the card's
  frozen procedure gives for it (committed by hash before evaluation). MC-5
  falsification on any holdout fires KU-12. If the auditor cannot find enough in-scope
  classes, G5-HOLD fails. At most one holdout may be replaced by a prospective
  experiment the hostile auditor designs or approves.
- **G5-MDL:** on the sealed data, b_meas is recomputed with the realized σ_eff and must
  remain ≥ log₂ Q_min.
- Only sealed real data can confer PREDICTIVE.

### 15.12 Stage 6 (pointer; its own charter)
The same 𝒦, unmodified, must yield the quantum, thermodynamic and gravitational regimes;
ε_R is exported as in XS-10. Any need to modify 𝒦 → STAGE3-ROUTE-TERMINATED. Stage 6
opens only under a Stage-6 charter frozen alone. Memory, viscoelasticity and crystalline
order are checked as effective regimes after Stage 4. B-SEL OUTER cards carry a flag on
the quantum regime.

---

## 16. Decidability and scorability
- **DC-1 Total procedures.** Every gate predicate, Sol membership and chain map at r★
  and r★★ has a frozen decision procedure with a termination argument (a proof, or a
  finite enumeration bound). An enumeration bound is a priced law constant with a
  declared, scored timeout branch; a verdict that flips at half or twice the bound is
  BATTERY-TUNED.
- **DC-2 Resources.** The card declares time and memory per item; ceilings R_item and
  R_card [A] apply (declared resources above them → CARD-UNDECIDABLE at S2). The
  evaluator runs each item for min(κ_res·declared, R_item); an overrun is UNSCORABLE. There is
  no "pending compute" status.
- **DC-3 Exactness.** Zero tests, equalities and memberships are decided in exact
  arithmetic (ℚ or algebraic numbers) or by certified intervals separated from the
  decision boundary by ≥ 2^(−p★). ε-claims follow §1.4. A tolerance-based "≈ 0" is
  UNSCORABLE unless the tolerance is part of the frozen law, priced and
  robustness-checked.
- **DC-4 Truncation.** Unbounded quantifiers need a frozen finite truncation level, which
  is part of the law, priced (VB-10) and scored. Every FORBID holds at levels n, n+1 and
  2n; a verdict that flips in that range is a size discriminator (a GY-4 return). Claims
  about the limit earn nothing.
- **DC-5 Possibly undecidable targets.** Exact quantum correlation and support families
  may be undecidable (Slofstra). OUTER or INNER status is declared in C4 at freeze; a
  claim of exactness without proof → CARD-UNDECIDABLE, never relabelled. A solution set
  defined by reference to an object whose membership is not finitely checkable is priced
  as that object. No exactness is claimed beyond the battery (FR9).
- **DC-6 Gate semantics.** A gate passes only if every mandatory item is scored and
  passes; an UNSCORABLE mandatory item means the gate is not passed.
- **DC-7 No pending status.** UNSCORABLE is never reopened within the route — not by
  later tooling, a larger κ_res or another truncation level (which would be a new card).
- **DC-8 Consistency cards.** The kit flags a card if, on every B-SEL embedding and an
  AI-3 sample, supp(Sol) equals the survivor set of some B-CF member up to Emb. A flagged
  card earns D_sel only by surviving §15.2, claims differentiation only if its C7
  algorithm computes Π as an output (a veto generates nothing), and has ε values only
  through a weight rule within supports (FR15(b)), which is then the actual law, priced
  and judged as such. Weights that are a fixed function of the support are a convention
  with ε credit 0; ε credit needs a W-pipe in which the weights change under clause
  ablation while the support stays fixed. No weight rule → CARD-UNMEASURABLE. Quantum
  claims are capped at OUTER.
- **DC-9 Reference implementation.** Frozen with the card and run unchanged; changing it
  is a modification, except a §19.2 tooling repair.
- **DC-10 One decision procedure.** Each card freezes one sound procedure, declared as an
  outer or inner approximation, with one level for all items. UNDECIDED = FAIL for gating
  and zero credit.

---
## 17. Required card template
Each card is one committed file plus its reference implementation; the SHA is recorded
before any scoring; every field is mandatory.

| Field | Content |
|---|---|
| C1 Identity | Card number; slot; freeze SHA; charter SHA; kit SHA; n_drafts and τ_sel with search code and logs; datasets and items the author has seen; what was learned from earlier verdicts; the nearest earlier card and the non-variant argument (BU-4, including mechanism distinctness) |
| C2 Exact law | 𝒳 and V_Ξ; the type of 𝒞 and its FR11 meaning in L₀; 𝒦 in L₀ plus priced vocabulary, every quantifier explicit; normal form and normalized skeleton; the notion of solution; truncation levels; uniform instantiations at r★ and r★★; the reference implementation |
| C3 Ontology declarations | Gluing as an explicit act (FR2); source of temporal order and time unit (FR7); compatibility scope and Emb (FR6); subsidiary possibility dependencies (FR14); G0-trichotomy landing, including weights within supports (FR15) |
| C4 Decidability | The single decision procedure (DC-10); OUTER/INNER status; termination arguments; resources per item and for levels n+1 and 2n |
| C5 Price ledger | §4.5 in full |
| C6 Input inventory | The §5.2 list; the expected outcome of every NR test; any declared supplied structures |
| C7 Generated structures | Π (δ_Π, η, δ_∂, H_hor, τ_int, τ_slow, scale window, b_Π); the derivation of Z_Π and the carrier, including NR-10(h)–(n); [h]_{T_Π}; T_Π with placement and s_T; Γ_Π. For each: algorithm or proof, responsibility map, grade, expected NR label |
| C8 Lock register | ℛ★: formula, coordinates, ≤ 3 lock observables, frozen witness families, lock fibers (including the platform-matched one), the claimed c_J/κ_J with Q5 witnesses, the derivation 𝒦 ⇒ ℛ★ with its grade, Q3 witnesses per framework and regime, the W-pipe, the DEF and JN arguments; an optional secondary relation in the same format |
| C9 Response scope | Per relation (§14), with the scope conditions, evidence of non-vacuity, and the expected carrier verdict at measurement and how it will be certified |
| C10 Certificates | Q1–Q12 as code plus machine-readable output |
| C11 Freedom and compression | Per credit instance c_ι, κ_ι and the dimension certificates; c_J, κ_J, c_lock, c_fam, N_dist, N_fib; b_J, D_sel; b_meas; MC-2 sensitivity; Price, ΔL₀ and ΔL at p = 6, 10, 16 |
| C12 Hostile baseline | The regime map H(x) for every realization class and the hostile fibers; the standard-model embedding E_std used for Q3(c) transplants; the attempted derivation of ℛ★ from 𝒮 and why it fails; the predicted J_SRB; B-HB witnesses with genericity and transplant predictions; the boundary-rule check; the D5 reverse-direction relations; B-CF; the conjunction test; the predicted outcome of every battery item |
| C13 Measurable target | The LT-1 instantiation: named platform and class; operational definition of each coordinate; interface-side data sources and calibration-only protocols; identification plan; A; tier; estimator; J_K; σ_pre; Θ_std (BP-5); the live rival; effect size; N_req; power; platform time; sealing route; ≥ 2·max(2, n_obs) candidate holdout classes; the declared scope domain |
| C14 Kill conditions | Acknowledgement of KU-1 to KU-13; the card-specific kill conditions meeting KP-1 to KP-5 |
| C15 Selectivity interface | Emb; the support object; every SEL verdict with its decision procedure |
| C16 Audit instances | AI-1; the input type for the AI-3 reference measure; the frozen domain predicate and its price |
| C17 Representation | Declared moves (RM1–RM5 plus priced extras) with their generating set; the covariance argument; no unique formula for h |
| C18 Tradeoff declaration | Whether any monotone identity–response relation appears; if so, its derivation from 𝒦 and the W-pipe for the opposite sign |
| C19 FR and GY standings | The tables of §21 |
| C20 Dependencies, transfer, non-claims | Pending R1 items used (scored per PV-3); the transfer plan (θ ledger with the θ_dict count and ranges, sector pair, transfer observable, SI witnesses, exported T_Π class); explicit non-claims |

---

## 18. Scoring procedure

### 18.1 Sequence (per card)
0. **Preconditions:** this charter frozen and reviewed by the owner; the evaluation kit
   (§19.3) built, validated and externally checked.
1. **Draft ledger** (BU-5).
2. **Card freeze:** one commit with SHA, reference implementation and C1–C20, battery
   predictions included; τ_sel computed. Its CHECKS line is added after the push is
   verified on the remote (§23).
3. **Selection** (only after S0 passes; a CARD-INCOMPLETE card triggers no selection and
   no holdout evaluation): a fresh Selector fixes and commits by hash the AI-3 seeds, the
   credit-family draws, the AI-2 constructions, the B-DIF and NR-8 seeds, the Emb scramble seeds, SEL-H,
   the reciprocity holdouts and AI-5.
4. **Intake:** S1 (variant and GRAVEYARD declarations), S2 (decidability) and the
   static NR tests (NR-0, NR-1, NR-2, NR-14).
5. **Evaluation:** the Evaluator runs S3–S8; S9 runs if S0–S8 are cleared, within T_audit.
6. **Recomputation:** a second agent recomputes every screen result before anything is
   reported.
7. **Checkpoint:** at most 5 lines to the owner (stage · result · scoreboard change · next
   action · blockers). The next card may be drafted only after this checkpoint.
8. After the budget is spent or the final count declared: the owner picks among
   ADMISSIBLE cards, or the route terminates. Stage 4 (§15.10) and Stage 5 (§15.11) follow
   on the picked card, with a checkpoint after each gate. Banking under §11.

### 18.2 Screens (in order)

| Screen | Tests | Terminal if first failing |
|---|---|---|
| S0 Completeness | C1–C20 present and non-empty; KP-1 to KP-5; FR2, FR3, FR6, FR7, FR11, FR14, FR15 declarations valid | CARD-INCOMPLETE |
| S1 Distinctness and GRAVEYARD | BU-4, VAR-1 to VAR-6, BU-9; GRAVEYARD return test at card level | CARD-VARIANT; CARD-GRAVEYARD |
| S2 Decidability | DC-1 to DC-10 | CARD-UNDECIDABLE (UNSCORABLE and BATTERY-TUNED included); CARD-UNMEASURABLE (DC-8, no weight rule) |
| S3 Nonrelocation | PC-6, PC-7; NR-0 to NR-17; §5.6 | CARD-RELOCATED; CARD-NONGENERATIVE; CARD-DEFINITIONAL (PC-6) |
| S4 Chain and consistency | KU-1; every chain map at r★ and r★★; persistence, size and nontriviality on the lock fibers; 𝒮 (KU-2 to KU-4); B-REC (KU-6); anchors (KU-5) | CARD-EMPTY; CARD-UNDIFFERENTIATED; CARD-INCONSISTENT |
| S5 Lock certificates | Q1 to Q12 on ℛ★ at r★ and r★★, including transplant, genericity, JN, B-SRB, B-NULL, the reverse-direction and boundary screens | CARD-UNFORCED (Q1); CARD-DEFINITIONAL (Q2); CARD-STANDARD (Q3); CARD-PIPELINE (Q4, Q11); CARD-NONJOINT (Q5); CARD-UNINFORMATIVE (Q6); CARD-NONINVARIANT (Q7, Q8); CARD-VACUOUS (Q9); CARD-UNSCOPED (Q10); CARD-INCOMPLETE (Q12) |
| S6 Freedom and compression | SC1 (§2.5 nontrivial reduction); §4.4 | CARD-UNINFORMATIVE (SC1); CARD-RELOCATED (LOOKUP); CARD-NONCOMPRESSIVE |
| S7 Measurability | §3.3, including MC-11 and lock-fiber robustness | CARD-UNMEASURABLE |
| S8 Selectivity | §15.1, §15.2 | CARD-UNSELECTIVE |
| S9 Originality | The assembled-law audit (§8), within T_audit | CARD-RESTATED; CARD-ASSEMBLY (bankable per OR-5) |
| — | Otherwise | **CARD-ADMISSIBLE** |

---

## 19. Freezing, repairs and the evaluation kit

### 19.1 Charter freeze
- **FZ-1** This charter is frozen **alone**: the freeze commit contains no 𝒦 card,
  draft, candidate or kit artifact. The non-normative working record `charter_workings/`,
  including `FREEZE_VERIFICATION.md`, is in the freeze commit. After the push is
  verified on the remote, a separate commit adds the `pending` CHECKS line (RULES 8).
  Every card cites the freeze SHA.
- **FZ-2** Before the freeze, independent read-only audits checked this text in rounds
  (round 1 on the pre-freeze draft; later rounds on the revisions): coverage of every
  red-team pattern, conformance with G2-11, internal consistency, the self-tests ST-1 to
  ST-11 (§24.2), the feasibility check ST-10 (Appendix A note), and an adversarial
  attack on every rewritten rule. Their findings, the
  disposition of each, and any residual item are recorded in
  `charter_workings/FREEZE_VERIFICATION.md`. A residual item is never a hidden open
  decision: it is listed for the owner's review. Three audit rounds were applied before
  the freeze; a loop-until-dry round was stopped to conserve budget, and its completion
  is recommended as a charter repair (CR-1) before Card 1 (FREEZE_VERIFICATION §10).
- **FZ-3** STOP for owner review.

### 19.2 Repairs and interpretations
- **Before Card 1 is drafted:** the owner may amend any rule in either direction by a
  numbered charter repair CR-n, with a re-freeze commit. The repair records that no 𝒦
  draft has been logged.
- **After the first 𝒦 draft is logged:** a repair (by owner ruling) may only tighten a
  rule; it applies to every card, null and self-test, and rescoring moves only toward
  failure. A tooling repair may only fix a crash or failure to terminate and must
  reproduce all prior outputs byte for byte. A kit fix is rerun on every card, null and
  self-test; any verdict that changes in a card's favour needs the Recomputer's
  confirmation and an external check. Interpretations follow CV-7.
- **After Card 1 is frozen** the charter text is immutable for Stages 3–6 apart from
  tightening repairs.

### 19.3 The evaluation kit
- **What it is:** a bounded work order, authorized by the owner after review of this
  charter and before any 𝒦 draft, executed by an agent context that authors no card,
  time-boxed to T_kit [A]. It is **not Card 1 and not a prerequisite campaign**; its
  complete deliverable is the validation list below. Anything it cannot compute within
  the box takes the hostile default set by a CR before Card 1; an overrun leads to a CR or
  to STAGE3-OWNER-HALT, never to an extension.
- **Scope (reusing the R1 and SD0 code):** the ε code and witness enclosures (R1); B-SEL
  and B-CF vectors (SD0 enumeration and solvers); B-REC and B-HB (R1/WO-001/WO-002 code);
  the frozen chart; the regime surrogates of §13.2; the VB axiom checklists; the L₀
  normalizer and price coder; the decoder battery (RB, SPS); the transplant, W-pipe,
  ablation and substitution harnesses.
- **Validation list:** the SEL counts 2961 / 1721 / 1232 / 8, the 240 gap and 2721; the
  PR-forcing lemma; ε ≡ 0 on single-protocol families; the exact zeros on HB-1, HB-3,
  HB-4, and HB-5 under T_lin with calibrated filters; HB-9 returning MODE SELECTION; the
  sign of BRI1's Tier-1 PASS on HB-2; STD-1 holding exactly on every HB family; the B-CF
  vectors; the price coder on Appendix B; ST-6 to ST-9 computed.
- **Rejection tests** (built from HB models plus supplied structure, no law): CT-18,
  CT-21, CT-22; an X_T that reads Γ on HB-2 → CARD-DEFINITIONAL; a disjunctive pin →
  NONJOINT; a tier-swap rectangle → NONJOINT; an invariant but non-maximal s_T → Q8 void;
  protocol-induced maps added to T on HB-1 → CARD-DEFINITIONAL; a static map applied on
  HB-4 → DIF-5(e) fails; a log-reparametrized observable → b_meas in frozen units;
  generated-premise laundering and automatic detailed balance → STANDARD; amplitude
  interpolation → STANDARD; a rank at a chosen point → the generic rank governs.
- Its outputs are externally checked before the first draft is logged; every card cites
  the kit SHA.

### 19.4 Card preregistration and information hygiene
Every field, battery prediction and the lock register are frozen before the card's
evaluation. Authors never see that card's sealed holdouts, seeds or intake results
before it is frozen (earlier cards' verdicts are visible under BU-6). Lock preregistration follows MC-5, MC-8 and G5-LOCK.

---

## 20. Staircase prohibition
**A forbidden staircase move** is any work item that delivers an ingredient for a present
or future 𝒦 card and is not one of: a frozen card, the §19.3 kit, a gate result, or a
terminal record. Motivation is irrelevant. Forbidden at any time, before or after
termination:
- **SM-1** a "missing ingredient", "deeper prerequisite" or "foundations" campaign (a
  theory of the carrier, of weights, of temporality, of the partition, of the interface
  class, of Gibbs structure, of the representation of Ξ, of decidability, of standard
  persistence; J_SRB tooling or d_op for a generated T beyond the kit);
- **SM-2** any change to a gate, battery, baseline, chart, pricing rule or constant that
  would let a failed card pass, or rescoring under modified rules;
- **SM-3** describing a failed card as "partial progress" or "future work", or opening an
  extension stage for it;
- **SM-4** budget laundering (BU-8) or a fourth card;
- **SM-5** reopening R1: new interface classes, a change to d_op or the verdict table,
  reinterpreting WO-002;
- **SM-6** treating UNSCORABLE or UNRESOLVED as "pending better tools";
- **SM-7** mining GRAVEYARD entries for "repaired" candidates;
- **SM-8** opening a new generative route other than by an explicit new owner ruling
  (T-5);
- **SM-9** treating a failure traced to a missing premise as licence for a prerequisite
  study; such a failure ends that card (RULES 4).

**Non-blocking items** (M5, D4, Tier-2 carrier necessity, triviality of the join, WO-001
C3/C4, the pending external checks) continue as housekeeping. They are **never
prerequisites** of any Stage-3, 4 or 5 step, verdicts touching them are scored under
PV-3, and their results cannot reopen this route.

---

## 21. FR1–FR15 and the GRAVEYARD

### 21.1 FR1–FR15
Each FR gets a standing — SATISFIED (with argument), SCOPED-OUT (declared and priced),
N/A (with a reason the auditor may contest) or VIOLATED. No FR is claimed discharged
without an external check.

| FR | Stage-3 form | Where | Violation |
|---|---|---|---|
| FR1 Representation invariance | Covariance under declared, protocol-uniform moves only | §1.6, Q7, NR-8 | NONGENERATIVE, or the relation is NONINVARIANT |
| FR2 Gluing is an explicit act | Composition of Ξ-instances declared | C3, SEL-12 | INCOMPLETE |
| FR3 No inaccessible-context data | Per-protocol laws only | §1.3, Q7, NR-0 | INCOMPLETE or NONINVARIANT |
| FR4 Observer independence | Π and [h] come from Ξ | DIF-9 | NONGENERATIVE |
| FR5 No unpriced split | Strengthened: a declared split of a protected structure also fails | §5.6 | NONGENERATIVE (declared); RELOCATED (hidden) |
| FR6 Compatibility scope | Declared in Emb | C3, §15.1 | INCOMPLETE |
| FR7 Earned temporality | Time primitive and priced (VB-9), or earned; instantaneous-state designation derived; DEF-16 | C3, NR-10 | INCOMPLETE; RELOCATED if hidden |
| FR8 Constraint ≠ selection | Q1 on all of Sol; DIF-7; DC-8 | §3, §15.10 | UNFORCED or NONGENERATIVE |
| FR9 No outer→exact upgrade | B-SEL grades; DC-5 | §15.1, §16 | Not credited |
| FR10 Information price | §4 | §4 | Unpriced input → RELOCATED |
| FR11 Declared meaning of 𝒞 | An L₀ statement, priced | C2, IP-2 | INCOMPLETE |
| FR12 Convention fixes | Adopted for the B-SEL encodings | §15.1 | Correction required |
| FR13 A deeper Γ object | Γ_Π = Obs_Π(Ξ) is built; Γ as an empirical model is SUPPLIED | §1.3, C7 | NONGENERATIVE |
| FR14 Subsidiary possibility facts | Dependency declared | C3 | INCOMPLETE if hidden |
| FR15 G0 trichotomy | Landing declared; weights within supports addressed | C3, DC-8 | INCOMPLETE; no weight rule → UNMEASURABLE |

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

- **Declarations:** for each entry the card declares NOT USED, COMPARATOR ONLY, COMPONENT
  (priced, with every distinction it alone produces removed), or RESEMBLES (with a
  distinguishing argument).
- **Behavioural equivalence:** a component that reproduces a GY entry's verdict pattern
  on that entry's finite test domain **is** that entry, whatever its name (test domains:
  the SD0 battery for discriminators; the R1 ladder plus the E1/D1 constructions for T
  classes). A generated T_Π or [h]-class is GY-11/GY-12 if, on the frozen chart's finite
  projection (template grid, A_{r★★}), it absorbs every family a GY-killed class absorbs
  (unrestricted bimeasurable bijections; protocol-dependent linear readouts; a
  latent-dimension-only constraint).
- **Return test:** a claim's responsibility map contains a component equivalent to a GY
  entry and the claim vanishes when it is ablated → the claim is not credited. At card
  level (**CARD-GRAVEYARD**, KU-9): the returning component carries the selectivity
  discriminator, the mechanism generating Π, or ℛ★; or every credited claim fails the
  test. GY-10 reopens only with a new named candidate; a selector card says so and is
  audited against GY-10's screen. Selecting a partition by an SPS template applied to the
  realized dynamics of Sol is not a GY-10 selector (it is STANDARD-MECHANISM,
  §15.7(viii)); applied to 𝒞 or another inventory item it is an NR-6 decoder.

---

## 22. Not credited (index)
§4.3(d), §12 and §13 govern. Never credited: DEF-1 to DEF-17 and bits on 𝒜_ε; 𝒮
consequences, including near-regime and boundary rules; the D5 reverse-direction
relations; RECOVERY; calibration-only results (BRI1's Tier-1 value and rate, the harmonic
R1-NULL, the C2 and M controls); consequences of priced or supplied inputs; relations
without a W-pipe or failing JN; marginal, inequality-only or off-chart reductions;
persistence, differentiation and the generation of Π, carrier, [h] and T_Π (gates,
§4.3(b)); pseudo-couplings (single-axis restrictions, Π–T-only couplings, disjunctive pins,
ε-class couplings); scope-Q relations in the ε ≡ 0 blind spot; ε at a non-admissible T;
truncation artifacts; redundant instances; sign-only, single-protocol, hand-picked-
repertoire, representative-dependent, cross-protocol-joint-law or record-only relations;
readings of R1-NULL as "no response"; selectivity reached through bounded-width
consistency, and structural or automatic SEL items; holdout successes as compression;
in-silico locks as PREDICTIVE; analogy or same-regime replication as CROSS-SECTOR; novelty
of components, representations or names; re-presented post-result seeds (Z_A, the
measurement-invariance framing, [h]_T in its known forms); "ε_R > 0 somewhere"; a presumed
monotone identity–response tradeoff; anything from a secondary relation.

---

## 23. Governance and roles
- No agent context both authors and audits the same card. The Kit builder authors no
  card.
- **Author:** the builder (Claude Code), in contexts that build no kit and audit nothing.
  **Intake auditor:** independent and hostile. **Evaluator** and **Recomputer:**
  independent of each other and of the author. **Selector:** a fresh context per card,
  which sees that card's signature only.
  **Comparator panel:** analysts and skeptics. **External checkers:** via `CHECKS.md`.
  **Owner:** rulings (CV-7), repairs (§19.2), the pick and the final count.
- The hostile default (CV-1) governs every dispute until the owner rules.
- Each card, intake audit and gate result gets a CHECKS line once verified on the remote.

---

## 24. CHARTER TESTS and self-tests

### 24.1 CHARTER TESTS
**Every row is an abstract gaming pattern labelled CHARTER TEST, never a physical
proposal.** A card that instantiates a pattern is presumed to receive that pattern's
classification and carries the burden of rebuttal. **The same presumption applies to
every pattern in the working record's red-team reports, red-team ledger and pre-freeze
audits.** Where a working-record classification conflicts with this text, this text
governs.

| ID | Pattern (abstract) | Caught by | Outcome |
|---|---|---|---|
| CT-01 | An input asymmetry from which Π can be read cheaply (a weighted structure whose cut or community equals Π) | NR-5, NR-6, NR-7 | RELOCATED |
| CT-02 | Sorts or labels of Ξ's type coinciding with S/E | NR-1, NR-6 | RELOCATED, or NONGENERATIVE if declared |
| CT-03 | A clause asserting a bipartition with a persistence or decoupling property | NR-1 | NONGENERATIVE |
| CT-04 | A table of constants whose block or zero pattern is Π | NR-6, IP-3 | RELOCATED |
| CT-05 | A vanishing explicit seed in 𝒞 selects Π | NR-5 (λ at 0, 2^(−p★), 2^(−2p★)) | NONGENERATIVE |
| CT-06 | An extractor threshold tuned so Π appears only on Sol | NR-3, DIF-2, IP-5 | RELOCATED (pipeline) |
| CT-07 | Π depends on a chosen basis or coordinates | NR-8 | INVALID → NONGENERATIVE |
| CT-08 | Persistence obtained by pushing relata into ∂ | §1.3 | Not persistent |
| CT-09 | The carrier stated as an axiom, or Obs with one shared readout by construction | NR-1, NR-3, NR-10 | RELOCATED; NO RECIPROCITY VERDICT |
| CT-10 | The carrier declared to be the instantaneous E state by definition | NR-10(c), (i) | RELOCATED |
| CT-11 | Protocol-dependent readouts in disguise, used to obtain ε_R > 0 | NR-10(a), NR-11, B-NULL | MODE SELECTION; lock void |
| CT-12 | T_Π equal to the automorphism group of a supplied record structure | NR-10(f), (k) | NONGENERATIVE |
| CT-13 | T_Π picked from 𝒯 by a selector clause rather than constructed | NR-1, NR-10(f), IP-4 | NONGENERATIVE |
| CT-14 | A generated T_Π ⊇ J or T_univ | Q8, DIF-5, B-NULL | ε void by rule (§1.4); relations void; DIF-5 fails |
| CT-15 | R1 calibration data as law inputs | NR-10(g), NR-14 | RELOCATED |
| CT-16 | Admissible states restricted to Gibbs, KMS or detailed-balanced states, or a temperature among the inputs | NR-1, NR-12, PS-5 | SUPPLIED, dependent claims 0; RELOCATED if hidden or used by ℛ★ |
| CT-17 | Thermal structure through a weighting measure or a Gibbs or maximum-entropy prior | NR-9, NR-12 | RELOCATED (prior) |
| CT-18 | A known standard model, with its cut, readout and Gibbs ensemble, repackaged as a law | NR-1, NR-12, IP-7, OR-3, c_J(b) | NONGENERATIVE / RESTATED |
| CT-19 | The lock smuggled in as a clause, or as the objective, penalty or stationarity condition of an extremum principle | NR-2, NR-13, DEF-17 | RELOCATED |
| CT-20 | A tradeoff or sign imposed by an input, or a monotone identity–response tradeoff postulated | Q11, NR-13 | RELOCATED |
| CT-21 | A lock that is an identity of ε's definition or of R1's theorems | Q2, DEF-1 to DEF-17 | DEFINITIONAL |
| CT-22 | A lock following from KMS, FDT, a fluctuation theorem or Onsager, rewritten in (Π, T, ε) variables | Q3, STD-3, STD-4, NR-12, B-SRB | STANDARD |
| CT-23 | A lock equal to a D5 reverse-direction relation | Q3(f), §13.8 | STANDARD |
| CT-24 | A size-scaling law of ε_R or its witnesses | STD-9 | STANDARD |
| CT-25 | "An odd channel vanishes under a symmetric reference" | STD-5, Theorem C | STANDARD |
| CT-26 | Regime shopping: witnesses from another regime, or avoiding Gibbs structure to weaken the baseline | BP-3, BP-4, §13.5, §1.5 | Witness invalid; scored on the hostile fiber |
| CT-27 | Separate interface and response constraints presented as one relation | Q5, c_J | NONJOINT |
| CT-28 | A scope-Q relation on a realized set with ε_R ≡ 0 | Q9 | VACUOUS |
| CT-29 | Scope switching | §14 | Lock void / UNSCOPED |
| CT-30 | ε evaluated at a non-admissible, joined or universal T | Q8 | Void |
| CT-31 | A relation holding for one representative h but not the class | Q7 | NONINVARIANT |
| CT-32 | A relation using joint laws across protocols | Q7, FR3 | NONINVARIANT |
| CT-33 | A relation holding only because the repertoire has one protocol, or only for a listed repertoire | Q1, §1.7, B-NULL | UNFORCED |
| CT-34 | Predicting ε_R from the same Γ it is computed on, or a pin | MC-2, DEF-13 | DEFINITIONAL |
| CT-35 | Certifying Π or T_Π on the platform by using ℛ★ or a record functional | MC-2 | UNMEASURABLE |
| CT-36 | A lock needing more than N_max samples | MC-7 | UNMEASURABLE |
| CT-37 | Forcing claimed from numerics with a tolerance | Q1, DC-3 | UNFORCED |
| CT-38 | A truncation artifact | Ch-4, DC-4 | Zero |
| CT-39 | Inflation through grid, precision, instance copies or carrier size | Ch-1, Ch-3, Ch-5, per-instance minimum, N_dist, family cap (§2.5) | No gain |
| CT-40 | Freedom reduction by forbidding anchors or emptying Sol | §15.8, §2.5 | No credit; KU-5 |
| CT-41 | A real constant tuned to make the lock hold or flip one battery item | IP-5, IP-10 | Priced; distinction not credited |
| CT-42 | One symbol encoding a table; target vocabulary encoded as an isomorphic table or re-derived as a definition | IP-3, IP-6 closure, NR-6 | Priced in full; RELOCATED if Π decodable |
| CT-43 | Selectivity by lookup on scenario name, party or setting count, dimension or capacity | IP-9, SEL-11, §21.2 | RELOCATED or GRAVEYARD |
| CT-44 | A law built only from consistency conditions matching a B-CF member, with no weights | §15.2, DC-8 | D_sel = 0; UNMEASURABLE |
| CT-45 | Exactness claimed for a possibly undecidable target; membership over all extensions with no truncation | DC-4, DC-5 | UNDECIDABLE or OUTER |
| CT-46 | Many drafts, the best frozen, the search undisclosed | IP-12, BU-5, KU-10 | Tax charged; void if undisclosed |
| CT-47 | A repair variant of an earlier card | VAR-1 to VAR-6, BU-4(e) | VARIANT; slot consumed |
| CT-48 | Items, domain or scope declared out after results are seen | BU-3, DIF-7 | New card or VARIANT |
| CT-49 | Deferral: "ℛ follows once X is derived" | NR-15, §20 | SUPPLIED; no X campaign |
| CT-50 | A baseline, battery or chart edited after a card is seen | §19.2 | Forbidden |
| CT-51 | A pending item cited as checked | PV-3 | Hostile reading |
| CT-52 | Protocols chosen so that the relation happens to hold | Ch-2, §1.7, Q1 | No effect |
| CT-53 | Memory, viscoelastic or crystalline-order input | NR-14 | RELOCATED |
| CT-54 | A record-only statement offered as evidence of back-reaction | STD-12, B-NULL | No reciprocity credit |
| CT-55 | Holdouts selected before freeze, or by an agent that has seen the mechanism | §15.9 | Evaluation void; one disclosed reselection |
| CT-56 | A weak comparator set | OR-4 floor | Audit incomplete; no DISTINCTIVE |
| CT-57 | A "transfer" where a B-side fit absorbs the prediction, B data enter the fit, a standard bridge links A and B, or B replicates A | XS-2, XS-6, XS-7 | Not CROSS-SECTOR |
| CT-58 | Threshold, platform, tier, repertoire or estimator chosen after card freeze | MC-5, MC-8, G5-LOCK | LOCK-VOID = LOCK-FALSIFIED |
| CT-59 | A discriminator reducing to capacity or dimension, party count, a blanket ban on strong contextuality, maximal T, or a latent-dimension bound | §21.2 (behavioural) | CARD-GRAVEYARD |
| CT-60 | Circular extractor: a component reads records, ε or a record functional (directly or by simulating Obs), so ℛ★ is its defining condition | PC-6 | CARD-DEFINITIONAL |
| CT-61 | Pipeline identity gated by the preconditions: ℛ★ holds wherever the chain is defined, 𝒦 only makes the preconditions true | DEF-12, Q4, NR-3 (Dom_gate) | DEFINITIONAL |
| CT-62 | Off-slice extension: a pin on the realized set extended jointly where the law never goes | Q5 (realized coupling), Q2(b) | NONJOINT |
| CT-63 | Jointness manufactured by evaluating ε at different tiers | Q5, DEF-14 | NONJOINT |
| CT-64 | Conditional identity: 𝒦 forces Γ into a class on which ℛ★ is a DEF identity | DEF-15, Q2(c) | NONJOINT or uncredited |
| CT-65 | An unpublished identity of the card's own quotient | DEF-13 | DEFINITIONAL |
| CT-66 | Lossy canonical reduction (invariant but not maximal s_T) | §1.4 (ii)–(iii), Q8 | ε undefined; Q8 fails |
| CT-67 | Response absorbed into the interface class (protocol-induced maps in T_Π) | §1.3 T_Π, PC-6 | CARD-DEFINITIONAL |
| CT-68 | ε produced by a static readout nonlinearity or by Π-weighted readout | PC-7(b), (c); DIF-5(e) | CARD-DEFINITIONAL / SUPPLIED |
| CT-69 | Tautology appearing when standard models run through the card's pipeline | Q3(c) transplant; STD-9 | CARD-STANDARD |
| CT-70 | Generic baseline identity with an exotic witness; a starved or silent B-SRB | Q3(b); BP-5; §15.5 | STANDARD; RESTATED |
| CT-71 | Lock-side definitional wins: coordinate stretching, definitional observable splitting, sub-grid prediction, decorative interface input, platform cut selected by response | MC-4 frozen units, MC-9, DEF-13, MC-2 | DEFINITIONAL / UNMEASURABLE |
| CT-72 | Credit earned by leaving the baseline (non-standard realizations dropped) | §2.5 full Im | No gain |
| CT-73 | Dimension certified at a singular point | §2.5 certificates | Generic rank governs |
| CT-74 | Structural credit counted twice through a secondary relation | §3.1 (secondary earns nothing) | No gain |
| CT-75 | Generated-premise laundering: 𝒦 generates detailed balance or KMS (e.g. on an acyclic state graph) and ℛ★ is its FDT/Onsager consequence | NR-12(b), RH-DB (Kolmogorov) | STANDARD-IMPLIED |
| CT-76 | Differentiation laundered into credit (generated Π, T, carrier counted as compression) | §4.3(b): generated structure is a gate, never a credit | No gain |
| CT-77 | A cheap conjunct, or a cheap Ξ-level predicate R ⊇ Sol written in Ξ-variables, forces ℛ★ through the components | NR-17(b), NR-4 | RELOCATED |
| CT-78 | A pin carried by one constant shared across instances, multiplied by the instance count | §2.5 family cap | Credited once |
| CT-79 | A component evaluates a copy of a law clause to manufacture W-pipes or ⊥ off Sol | PC-6, NR-3, NR-4 | DEFINITIONAL / RELOCATED |
| CT-80 | Frozen-field persistence: Π read from variables the law makes exactly invariant | §1.3 non-vacuous, DIF-2 | Not persistent |
| CT-81 | A declared type that cannot express standard models, E2 or the product-latent twin | Q3(c), NR-10(n) | STANDARD / NONGENERATIVE |
| CT-82 | Two instance-indexed single-axis pins presented as a coupling | Q5 (split test) | NONJOINT |
| CT-83 | One non-standard realization used to disable the standard-class comparison | §2.5 c_J(b) on Im ∩ FB | No effect |
| CT-84 | Credit instances drawn where FDT is silent while the lock fiber is FDT-bound | §2.5 lock-fiber cap, Q6 | Capped |
| CT-85 | Isomorphic draws counted as distinct instances | §1.5 N_dist | No gain |
| CT-86 | Selectivity bits used to fill the compression margin | §4.4 ΔL₀ | No effect |
| CT-87 | Holdouts or seeds reused across sequential cards, or a Selector that has seen an earlier card | BU-6, §15.9, §23 | Evaluation void; items public |
| CT-88 | A reviewer offers a trivial superset (𝒦 ∨ X, or 𝒦 with points added) as a JN split | NR-17 (not a split) | No effect |
| CT-89 | Decorative-read persistence: X_Π reads a driven variable it ignores | §1.3 X_Π-relevant variables | Not persistent |
| CT-90 | Inert-relatum padding to pass the size test | §1.3 deletion of inert relata | No gain |
| CT-91 | A menu-branch T_Π: X_T chooses among named classes by a cheap condition | NR-10(f) | SUPPLIED → NONGENERATIVE |
| CT-92 | A transplant embedding that adds structure the draw lacks or fails the Q3(c) conditions, or selective ⊥ to shape the transplant denominator | Q3(c) | Auditor's substitute embedding and realized-structure substitution govern |
| CT-93 | A static nonlinearity applied per relatum before aggregation | PC-7(b), §15.3, DIF-5(e) | Tested by DIF-5(e): fails if it creates ε on an exogenous control (only the tail is calibrated out) |
| CT-94 | Decorated copies (ignored labels) inflating N_dist | §1.5 structural distinctness (i)–(iii); family-cap grouping | No gain |
| CT-95 | A trivial split (a part restating 𝒦, or containing it as a disjunct) offered to the Q5 split test | Q5 (parts strictly shorter than 𝒦) | No effect |
| CT-96 | Fragmented class fibers: T_Π instance-specific, joint on one pair, single-axis pins elsewhere | §2.5 N_fib (only instances in qualifying fibers count) | No gain |
| CT-97 | A cheap imposing predicate written to depend on one cheap clause of 𝒦, to escape JN | NR-17 (R may contain clauses of 𝒦; only Price_min(R) < Price_min(𝒦) is required) | RELOCATED |

### 24.2 Self-tests (known objects only; none is a candidate)
**Convention.** Each known object is completed into a card with the most favourable
well-formed content for every field it lacks (KP-1 to KP-5 met; the scope, lock register,
platform and transfer plan the object best supports), so S0 passes by construction. The
**terminal** follows T-1 (first failing screen; within a screen, the first listed
terminal; for S5, Q1 to Q12 in order). "Recorded" lists further clauses that must fire.
FZ-2 and CV-7 compare both the terminal and the recorded clauses.

| ID | Known object treated as a card | Required verdict |
|---|---|---|
| ST-1 | BRI1's Tier-1 ε_R relation (Duffing bath, Gibbs state, supplied partition and readout) | Terminal S3: CARD-RELOCATED (Gibbs state supplied and used in ℛ★'s derivation, §5.6). Recorded: NONGENERATIVE (partition, readout, bath supplied); STANDARD (STD-3 nonlinear FDR; B-SRB RESTATED, §13.6; STD-9 if ℛ★ includes the 1/N_B rate) |
| ST-2 | The harmonic R1-NULL | Terminal S3: CARD-RELOCATED (Gibbs reference supplied and used). Recorded: DEFINITIONAL (DEF-15); STANDARD (STD-3, STD-6, Ford–Kac–Mazur); VACUOUS for scope Q (Q9); RS-1 applies |
| ST-3 | ASP | Terminal S1: CARD-GRAVEYARD (GY-6). Recorded: S2 CARD-UNMEASURABLE (DC-8, no weight rule); S8 NON-SELECTIVE (SEL-10 admitted); B-CF collapse |
| ST-4 | NULL-ΠT (Ξ any SFP model of the declared type without PS-5 content used by ℛ★) | Terminal S3: CARD-NONGENERATIVE (Π, [h], T supplied). Recorded: S6 LOOKUP (Im = FB gives c_J = 0, so b_J = 0 and ΔL ≤ 0) |
| ST-5 | The product-latent E-B model | Terminal S3: CARD-NONGENERATIVE (protocol-indexed readouts, NR-10(a)). Recorded: carrier FAIL and MODE SELECTION (NR-11); no reciprocity credit (STD-12) |
| ST-6 | A textbook stochastic detailed-balance model: detailed balance arises only through Kolmogorov's criterion on state structure its dynamics generate; no PS-5 content in 𝒞, 𝒳, priors or Emb, and no clause flagged by NR-1; on a symmetric input Sol is a symmetry-broken orbit (NR-5); Π matches an SPS output of the realized dynamics, and no RB/SPS template or decoder within ℓ_dec applied to the inventory recovers Π (NR-6); lock fiber on a generic instance; ℛ := its FDT or Onsager-regression relation in (Π, T, ε) variables | Terminal S5: CARD-STANDARD (Q3: RH-DB; STD-3, STD-4(a); NR-12(b)). Recorded: STANDARD-MECHANISM (§15.7(viii)); JN recorded but not applied to the detailed-balance sub-conjunct (NR-17, last sentence). **ST-6′:** the same model with detailed balance carried by 𝒞 → terminal S3 CARD-RELOCATED (§5.6) |
| ST-7 | A known k-parameter standard model class with Π and T fixed by a standard rule | Terminal S3: CARD-RELOCATED (an RB/SPS decoder recovers Π from 𝒞, NR-6), or NONGENERATIVE (T picked by a selector, CT-13). Recorded: S5 CARD-STANDARD (Q3(e); Q3(c) where the class is a B-HB family); S6 c_J = 0 by §2.5(b) with M the class itself (an admissible comparison class), so ΔL ≤ 0 → LOOKUP |
| ST-8 | An order-2 Volterra predictor of a₊₊ from {a₀, a₊, a₋} on an HB-2 member of small coupling (RH-AN's surrogate holding at m = 2 at the frozen template amplitude) | Terminal S3: CARD-NONGENERATIVE (HB-2's partition, readout and bath supplied, §5.6). Recorded: S5 CARD-STANDARD (Q3: STD-14) |
| ST-9 | The Beenakker–Kindermann–Nazarov cascade correction on a standard P-2 model, the cascade relation derived without any thermal, Gibbs or FDT premise (zero environment temperature) | Terminal S3: CARD-NONGENERATIVE (the model's partition and detector readout supplied, §5.6). Recorded: S5 CARD-STANDARD (Q3: STD-7; SFP-5) |
| ST-10 | Credit feasibility on paper (Appendix A note) | SC2 reachable for a compact honest card at c_J = 1 and comfortably at c_J = 2; a law constant that ℛ★ pins identically on every instance is credited once (family cap); a tabulated card fails before SC2 (KU-1 CARD-EMPTY, or Q1 CARD-UNFORCED, on post-freeze draws) |
| ST-11 | A known definitional relation conjoined with an arbitrary non-standard restriction on Γ alone | Γ-restriction forced by Ξ-level clauses: terminal S3 CARD-RELOCATED (NR-17(b)) if the shortest L₀ statement of those clauses is ≤ L★ + c_dec, otherwise terminal S5 CARD-DEFINITIONAL (Q2 via DEF-15); in both cases Q2 (DEF-15) and Q5 are recorded as failing. Imposed by a target-level clause: terminal S3 CARD-RELOCATED (NR-2) |

---

## 25. Hard stop
- This charter is frozen alone (FZ-1); its `pending` CHECKS line is added after the push
  is verified on the remote.
- No 𝒦 card is generated, frozen, scored or optimized, and the evaluation kit is not
  built, until the owner has reviewed this charter and authorized the kit and Card 1.
- After the freeze the charter changes only under §19.2.

---
## Appendix A — Frozen numbers
No value changes after the first 𝒦 draft is logged, except by a tightening repair
(§19.2).

| Symbol | Value |
|---|---|
| p★ | 10 bits (sensitivity at 6 and 16) |
| r★ | k = 3 grid times; witness order m ≤ 4; A = {a₀, a₊, a₋}; record dimension per grid time d_rec = 1 |
| r★★ | k = 4; m ≤ 5; A ∪ {a₊₊}; d_rec = 2 |
| Protocol templates | a₀ null; a± linear ramps of amplitude ±α starting at t₁; a₊₊ amplitude 2α; α = 1 standard deviation, under a₀, of the driven S variable (never of a record); t₁ := H_hor/4, with H_hor the horizon the card declares in C7 (≥ the §1.3 bound); the template-to-Ξ map is part of Emb |
| Windows W | [−4, 4] for whitened cumulant coordinates; [0, 2] for ε; for scope G, the observable's range over B-HB at the standard reference parameters |
| Record alphabet q | 3, for HB-12 and for discretized continuous records only (B-SEL uses each scenario's own alphabet); tertiles of P_{a₀} from an independent calibration run; ε is always computed on continuous records |
| r_lock | max(2σ_pre, 2^(−p★)·abs(W)) per observable, frozen in C13 |
| δ_Π / η / δ_∂ | 0.05 / 0.05 / 0.10 |
| Horizon; robustness; scale window | H_hor ≥ max(window, 10·τ_int, 3·τ_slow); (2η, 2·H_hor); w = 2 |
| b_Π | 6 bits |
| AI-3 sizes; θ_gen | n_min = 8, so between 8 and 16 relata; coverage ≥ 0.9 of the AI-3 draws |
| N_AI3; N_AI5 | 160 AI-3 draws per card (N_AI3 in IP-13), seeds committed by the Selector after the card's freeze; 3 AI-5 instances per card |
| N_cred | 100 structurally distinct credit instances (AI-1 if eligible, plus Selector draws; redraws up to 10·N_cred attempts); N_dist ≤ N_cred is the number obtained |
| N_ch | 8 auditor chart coordinates |
| L₀ code | 64 tokens, 6 bits each; 4 reserved |
| Compression | COMPRESSIVE iff ΔL₀ = b_J − Price ≥ p★ at p = 10 and ΔL₀ > 0 at p = 16; LOOKUP iff ΔL = b_J + D_sel − Price ≤ 0 at p = 10 |
| Regime threshold δ_RH | max(2^(−p★), 3·r̂_lock), with r̂_lock = max over lock observables of r_lock/abs(W) (§13.2) |
| Scope-G chart | The response functionals of §1.5 up to order m at r★ and r★★; windows: each functional's range over B-HB at the standard reference parameters |
| D_sel | 1 bit per verified distinction, ≤ 10 bits |
| Q_min | 10 (3.32 bits) |
| σ_pre; LOCK-VOID | σ_pre ≤ abs(J_K)/4; realized systematics > 1.25·σ_pre |
| N_max; platform time | 10⁹ effective records per card; ≤ 30 days of platform time per card |
| α; power | 0.0027; 0.9 |
| Lock thresholds | falsified beyond z_obs·σ_eff, with z_obs := Φ⁻¹(1 − α_obs/2) and α_obs = α/(3·n_obs) (MC-9; z_obs ≈ 3.32, 3.51, 3.62 for n_obs = 1, 2, 3); confirmed within 2σ_eff with σ_eff ≤ abs(J_K)/4 |
| Lock observables; alternate platforms | ≤ 3 per card; 1 alternate |
| In-silico budget | ≤ 10¹⁰ effective samples (evidence grade only) |
| c_dec; ℓ_dec; p_dec | 60 bits; max(½·log₂ abs(𝒜_X), c_dec); 0.5 |
| ℓ_tr; b_patch | 32 bits; 4 bits |
| κ_res; R_item; R_card | 10; 48 core-hours per item; 5000 core-hours per card |
| DIF-6 perturbation | 2^(−p★), relative |
| Default constant range | [10⁻³, 10³], log scale |
| B-CF | Precomputed: (j,k)-consistency, k ≤ 4; SLAC; BLP; AIP; BLP+AIP; ASP; pairwise Boolean combinations. Collapse at Hamming distance ≤ 1, or auditor-exhibited refutations of width ≤ 6 or Sherali–Adams level ≤ 3 |
| FORBID truncation check | Levels n, n+1, 2n |
| Holdouts | ≥ 3 per Stage-3 pool; at Stage 5, ≥ max(2, n_obs) from ≥ 2·max(2, n_obs) candidate classes |
| N_pool (LOCK-H) | ≥ 5 eligible datasets |
| NR-16 test | one-sided binomial, α = 0.05 |
| Budget; relations | 3 cards for Stages 3–6; one credited relation ℛ★ and at most one uncredited secondary relation |
| Transfer | d_B = 0; TG ≥ p★; TG_A ≥ p★; band ≤ ¼ of range; bridge ≥ Q_min times wider |
| HB ranges | β ∈ [0.25, 4]; ω ∈ [0.5, 2]; couplings ∈ [0, 1]; N_B ≤ 8; quantum ≤ 4 sites; quartic λ ∈ [0, 2] |
| Clocks | T_kit 30 days; T_audit 60 days after the card's freeze; D_card 120 days from the owner checkpoint on card j to the freeze of card j+1; T_lock 365 days after G5-LOCK |

**Feasibility note (self-test ST-10; a paper estimate, not a theorem).** The sizes
below describe how large a compact card is. They describe no law. Prices follow
§4.1–§4.2 as frozen, itemized as in the pre-freeze audit
(`charter_workings/AUDIT_R1_C_selftests_feasibility.md` §2.2, with IP-6 as now frozen).

| Item (rule) | Bits |
|---|---|
| Law clauses, about 30 tokens with variable-index bits (IP-1) | ≈ 216 |
| 𝒞 and its FR11 meaning (IP-2) | ≈ 50–60 |
| Declaration of 𝒳 (IP-14, as max(declaration, log₂ m)) | ≈ 50–80 |
| The six components (IP-2, IP-8) | ≈ 300–600 |
| θ_dict, with its numeric content (IP-2, IP-5) | ≈ 45–90 |
| Two law constants (IP-5) | ≈ 24–38 |
| Thresholds, scales, truncation, enumeration bounds | ≈ 15–40 |
| Vocabulary, four canonical items (IP-6) | 16 |
| Selection tax (IP-12) | ≈ 3–10 |
| Domain restriction (IP-13) | ≈ 0–70 |
| **Total** | **≈ 720–1220** |

- **Credit** (§2.5) with N_fib = N_dist = 100: b_J = 1000 bits at c_J = 1; 2000 bits at
  c_J = 2. The family and lock-fiber caps can only lower it.
- **At c_J = 1** the margin ΔL₀ runs from about +280 to about −220. A compact card
  passes if its whole price stays below about 990 bits at p = 10 and below 1000 bits at
  p = 16, where each real literal costs 6 more bits; for a card with n real literals the
  bar is about 1000 − 6n bits (about 940 for ten), roughly 150 tokens, components
  included. A heavy card does not.
- **At c_J = 2** the margin is about +780 to +1280, so SC2 is reachable.
- **Tuning does not pay.** A tuned constant costs at least 12 bits at p = 10 (more at
  p = 16). It cannot create coupling credit, because Q1 is decided on post-freeze draws,
  and a law constant that ℛ★ pins identically on every instance is credited once (family
  cap, CT-78).
- **Tables fail first.** A tabulated card fails before SC2: on post-freeze draws its
  table either leaves Sol empty or equal to 𝒳 (KU-1, S4 CARD-EMPTY), or does not force
  ℛ★ (Q1, CARD-UNFORCED).
- **Scope.** This note checks SC2 only. SC1 and SC3 are certificate-level and cannot be
  reduced to arithmetic.
- **Contrast with v1.** v1's bar (ρ ≥ 2, b_J over 16 instances) was not reachable at
  these prices. The working draft's interim generated-structure credit G was withdrawn
  at pre-freeze audit, because it could be gamed (Appendix D, D-1).

---

## Appendix B — L₀ code and vocabulary schedule

**B.1 Alphabet (64 tokens, Polish notation, 6 bits each).**

| Group | Tokens | Count |
|---|---|---|
| Logic | ¬ ∧ ∨ → ↔ ∀ ∃ = ≠ ⊤ ⊥ ite | 12 |
| Sets | ∈ ⊆ ∅ singleton pair × 𝒫 card ∪ ∩ ∖ [n] | 12 |
| Maps | λ apply ∘ id image preimage inverse restrict | 8 |
| ℕ/ℚ arithmetic | 0 1 succ + − × ÷ ≤ < Σ-finite | 10 |
| Conditional response | kernel cond-prob E ⊗ marginal do law support | 8 |
| Process composition | sequential parallel contract wire | 4 |
| Structure | def var nat-literal rat-literal real-literal end | 6 |
| Reserved | (unavailable to cards) | 4 |

**B.2 Priced vocabulary** (IP-6; canonical definitions and axiom checklists encoded by
the kit before Card 1). VB-1 metric · VB-2 inner product / orthogonality · VB-3
finite-dimensional Hilbert space and tensor product · VB-4 tensor-product or subsystem
factorization, including block-splitting V_Ξ or 𝒳 · VB-5 quantum correlation set · VB-6
GPT cone with order unit · VB-7 Born rule · VB-8 continuum analysis (ℝ, limits, exp/log)
and continuous time or space beyond the declared resolution · VB-9 temporal order and
time unit, unless earned · VB-10 dimension, capacity or any dimension-like parameter,
including truncation levels · VB-11 energy function / Hamiltonian · VB-12 locality graph
of a generator · VB-13 probability measures, weights or priors on Ξ, unless generated ·
VB-14 a symmetry group and its action, when not generated · VB-15 conserved-quantity
declarations · VB-16 time-reversal parity / microscopic reversibility.
**Protected (paying for them never makes them generated or creditable; §5.1, §5.6):** VB-17 invariant measure, temperature, Gibbs
weight, detailed balance or KMS, and every PS-5 input · VB-18 group action on record
space · VB-19 readout map or class · VB-20 partition sorts · VB-21 target-level
coordinates in clauses. Supplying or matching VB-5, VB-6 or VB-7 makes every selectivity
result RELOCATED.

---

## Appendix D — Builder's choices relative to the working draft v1
These are frozen defaults. Until the first 𝒦 draft is logged, the owner may change any of
them in either direction (§19.2). "v1" is `charter_workings/CHARTER_V1_WITH_LEDGER.md`;
"OD-n" are its Appendix-C owner decision points.

| # | Topic | v1 | This charter | Reason |
|---|---|---|---|---|
| D-1 | Credit scale (OD-13) | b_J over 16 instances; ρ ≥ 2; scale left to the owner with ST-10 unresolved | b_J only, over up to N_cred = 100 structurally distinct post-freeze instances, with family and lock-fiber caps; COMPRESSIVE iff b_J − Price ≥ p★ (and > 0 at p = 16); D_sel only in the LOOKUP test | v1's bar was probably unreachable for an honest card (accounting report §0), which would make the charter a hidden kill. An interim credit for generated structure (G) was tried in the pre-freeze draft and withdrawn after audit: about ten distinct ways to game it (FREEZE_VERIFICATION.md). Generation stays a gate, as in v1's FC-3 |
| D-2 | Relations per card (OD-14) | Two, credited jointly | One credited ℛ★; at most one uncredited secondary | Removes double counting (CT-74) |
| D-3 | Evaluation order (OD-1, OD-15) | Batch freeze of all cards; intake at batch close | Sequential: freeze → score → owner checkpoint → next card; fresh Selector and fresh sealed draws per card; earlier items made public; earlier decoders and witnesses re-run; D_card clock | Uses the owner's review between cards. Learning is priced by the VARIANT rules and the selection tax. The intake-oracle trade-off is recorded for the owner (FREEZE_VERIFICATION.md) |
| D-4 | Freeze preconditions (OD-4) | Owner fixes constants and decision points before the freeze | Frozen defaults (Appendix A); owner review after the freeze, with repairs in either direction before the first draft | G2-11 orders "freeze, then STOP for owner review" |
| D-5 | Definitional lens | CT-D02 and CT-D05 missing (truncated report) | Dom_gate, DEF-12, Q4, NR-3 (CT-D02); DEF-15, Q2(c) (CT-D05); the full report is `REDTEAM_D_definitional.md` | Full report recovered from the agent transcript |
| D-6 | B-CF | k ≤ 6 and Sherali–Adams ≤ 3, all precomputed | k ≤ 4 precomputed; width ≤ 6 and Sherali–Adams ≤ 3 refutations count when an auditor exhibits them; collapse no longer fails G-SEL by itself | Kit cost; a B-CF vector near the all-correct vector would otherwise fail every exact card |
| D-7 | Regime surrogates | Separate v1 Appendix F | Merged into §13.2, with one threshold δ_RH | Length; one threshold instead of four |
| D-8 | v1 Appendix C decision points | Open (OD-1 to OD-15) | OD-2, OD-3 and OD-5 to OD-11 adopted as v1 proposed; OD-1, OD-4, OD-13, OD-14 and OD-15 as above; OD-12 (the kit) still needs owner authorization | A frozen charter has no open decision |
| D-9 | Length | ≈ 200 KB, ledger inline | Normative text here; drafts, reports, ledger and audits in the working record under the §24.1 presumption | Reviewability |
| D-10 | Interface catalogue | Four "frozen tiers" | R1 froze two tiers (T_R1, T_mono); E₂± and T_caus are charter catalogue classes with BL distances fixed here as a Stage-3 convention | R1 integrity (G2-10) |
| D-11 | 𝒜_Π | Reduced by standard selectors on the realized dynamics | 𝒜_Π^hand: every hand-designable partition, modulo the group generated by Aut(𝒞) and the realized symmetry, with only the §1.3 inert-relatum deletion; standard selectors give STANDARD-MECHANISM, never a smaller baseline | The reduction made every card fail either the witness requirement or the size test |
| D-12 | Vocabulary price | max(L_stmt(def), ΔF_tgt with axioms deleted) | 4 bits per canonical item; all card-specific content priced as statement or input | The axiom-deletion test priced any essential item at the whole credit |
| D-13 | Other v1 wording | — | Restored or kept: BP-5 correlators to order m★★ plus Θ_std; c_J in fixed-class fibers; v1's NULL-M guard (comparison classes published before the freeze and stated without reference to the card), now inside c_J(b) and the family cap; MC-4's log minimum; §15.5 closure under DEF; "ℛ★ need not separate the twin"; DEF-15 "or valid mathematics"; PC-6's ban on reading protocol identity; §21.2's absorbed-family list; DIF-5(e) binding at S4. Added: the §1.3 inert-relatum deletion (one template, the same on every lock fiber); the comparison-class guard (parameters are constants, not functions of u or ℛ★) applied in c_J(b), the family cap and Q3(b). Changed: the size test is log₂ abs(𝒜_Π^hand/G_ι) − log₂ M ≥ b_Π (b_Π 8 → 6, n_min 6 → 8); v1's comparison with the IP-14 ontology price is dropped, because it would exceed the 16-bit maximum at n ≤ 16. Replaced: v1's two-part NULL code by c_J(b) and the family cap | Coverage audits |

---

## Appendix E — Traceability to G2-11

| G2-11 requirement | Where |
|---|---|
| Item 1: baseline spaces 𝒜_Π, 𝒜_T, 𝒜_Γ, with 𝒜_ε as an image | §2, §12, §13.2 |
| Item 2: nontrivial freedom reduction + positive compression + measurable consequence | §2.5, §3, §4.4 |
| Item 3: compression accounting and information price | §4, Appendix A note, Appendix B |
| Item 4: nonrelocation of carrier, partition, interface class, readout class, Gibbs/FDT structure, target relation | §5 (PS-1 to PS-6, NR-0 to NR-17), PC-6, PC-7 |
| Item 5: at most three genuinely distinct cards | §6 |
| Item 6: card contents (exact law, price, generated structures, measurable target, hostile baseline comparison, kill condition) | §7, §17 |
| Item 7: originality at the assembled-law level | §8, NR-17 |
| Item 8: parameter transfer | §9 |
| Item 9: stopping rule; no deeper-prerequisite staircase | §10, §20 |
| Addition 1: merge = provenance | §11 |
| Addition 2: ε_R derived; definitional relations do not count; joint restriction beyond the definition | §12, Q2, Q5, §2.5 |
| Addition 3: baseline after causality, positivity, KMS/FDT, Onsager, conservation | §13, Q3, NR-12, BP-4, BP-5 |
| Addition 4: response scope | §14 |
| Central task: 𝒦 → Π → [h]_{T_Π} → T_Π → Γ_Π → ε_R forcing ℛ = 0 not independently imposed | §1.2, §3.1 |
| Carrier/readout derived, modulo representation; no unique h | §1.3, §1.6, NR-10, C17 |
| No presumed monotone identity–response tradeoff | CV-5, Q11, NR-13, C18 |
| R1's identifying assumption becomes a Stage-3 target | NR-10, DIF-5, DIF-9, MC-6 (generation is a gate, §4.3(b)) |
| Frozen alone; STOP before Card 1 | §19.1, §25 |
| VS Code review routine disabled, not replaced | Recorded in STATE (no charter rule needed) |

---

## Appendix G — Frozen carrier-certificate checklist (R1 post-result seed, adopted for MC-6)
1. The interface is deterministic, invertible and calibrated; residual uncalibrated
   curvature is below the witness: 3σ·abs(φ″_res/φ′) < abs(witness) at every operating point.
2. Readout noise is protocol-independent and calibrated; calibrated nonlinearities are
   removed on noise-free data or with a noise model (additive noise is a kernel, not a
   map).
3. No random run-to-run interface gains or offsets beyond a calibrated stationary model.
4. One fixed time base, sampling grid and trigger phase; no protocol-dependent clock
   jitter, latency, window, or phase of a nonstationary environment.
5. One readout channel with fixed weights; no push-pull reweighting of environmental
   sources.
6. Record completeness: the record contains the full support of every interface kernel,
   past and future, at driver resolution, with every kernel invertible on the record
   (injectivity into the observed record).
7. No outcome-dependent selection: no vetoes, cuts or lock-loss rejection.
8. Only invertible calibrated nonlinearities; saturation, clipping and quantization are
   excluded unless provably inactive.
9. The protocol acts on the environment only through the system; no actuator heating,
   EMI, vibration or other cross-talk.
10. Estimation is controlled: per-protocol sample sizes are equal or modelled.
