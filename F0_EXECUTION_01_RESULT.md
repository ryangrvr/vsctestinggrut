# F0 — EXECUTION 01 RESULT (REPAIRED)
**Campaign:** F0 execution 01 (kinematics + physicality), authorized by the owner from the
frozen pre-execution boundary `bef8b9480c9f7569c70837c6ee5c4776fc2e0f3c`.
**Repair:** owner/reviewer ruling on `f45fb901…` — `F0-PHYS-OPEN RATIFIED`, `F0-A REPAIR
REQUIRED BEFORE BANKING`, `F0-B NOT AUTHORIZED`. This is the repaired result
(branch `ggc0-f0-exec01-repair-0`; R1–R8 applied; `F0_REPAIR_EXEC01_PROVENANCE.md`).
**Machine-readable status:** `F0_EXECUTION_01_STATUS.json`.

## 1. F0-A result (repaired)

- **`(C, Γ)` mathematically well-defined: YES, and now repaired/validated.** Explicit
  finite object `K = (X, {O_x}, C, E, Γ, ≈)`. Downward-closed family (canonical) with the
  hypergraph equivalent proven bijective.
- **Representation invariance: VERIFIED for every declared move that is programmatically
  testable** — intervention relabeling (`test_relabel_invariance`), **outcome relabeling
  (`test_outcome_relabel`, added in the repair — previously claimed but not exercised)**,
  and the family↔antichain presentation swap (`test_hypergraph_roundtrip`). The former
  fourth "redundant presentation" move is **withdrawn as invalid (R3)**: adding a previously
  absent union context changes accessibility, and is not a representation change. `≈` is
  limited to the two label bijections and the presentation swap.
- **Composition status (R2 — corrected):** three distinct notions, never conflated:
  (1) **two compatible marginals always admit a joint extension** (explicit construction
  `p(a,b,c) = p_AB·p_BC/p_B`, verified exactly); (2) **an entire family may fail
  simultaneous extension on cyclic scenarios** — the repaired K2 anti-correlated triangle
  is overlap-compatible yet has NO global distribution, verified by an exact rational
  feasibility check (contextuality CALIBRATION, no novelty claim; the previous correlated
  K2 data was globally extendable and its "no global section" claims are withdrawn);
  (3) **physical accessibility of the union never follows from either mathematical fact.**
  Summary: *pairwise probabilistic gluing is easy; global cyclic compatibility is where
  the obstruction lives; physical accessibility follows from neither.*
- **Unresolved kinematic ambiguities (deliberate):** empty-context convention (excluded
  here); deeper equivalence moves; non-distributional event scopes; canonical
  maximal-context presentation. Formulation §10.
- **Validator (repaired, with negative controls):** positive controls **12/12 PASS**
  (downward closure; maximal contexts; overlaps; presheaf functoriality; Γ well-formedness;
  overlap compatibility; intervention relabel invariance; **outcome relabel invariance**;
  hypergraph roundtrip; gluing (two-marginal extension exists); global extension (K2 fails
  / K3 passes); suites K0–K3). Negative controls **5/5 PASS (all reject as required)**:
  malformed downward closure; non-normalized Γ; negative probability; overlap-incompatible
  Γ; contextual K2 passes local and FAILS global.
- **F0-A status (R8):** finite kinematics — **mathematically repaired/validated**;
  mathematical content — **RESTATED relative to standard empirical-model/sheaf machinery**
  where appropriate (baseline B5), with the added governance discipline. These two labels
  are distinct and are not to be reinterpreted as one another.

## 2. F0-PHYS result (terminal unchanged; wording repaired)

- **TERMINAL: `F0-PHYS-OPEN` — RATIFIED by owner/reviewer ruling; unchanged by the
  repair.**
- **Strongest observer-independent interpretation found:** Meaning 3, *physical
  co-instantiability* — right shape, but every current formulation buys precision with
  supplied structure: measurement theory, subsystem/tensor decomposition, spacetime, or
  process algebra (§8 table of the physicality doc).
- **Strongest hostile tests (R5-repaired wording):** P1/P3 establish that **operational
  `C` depends on the physically/operationally specified intervention, including apparatus,
  sharpness, noise and coarse-graining** (coarse-grained/noisy versions are generally
  different operational interventions/POVMs, not different presentations of one
  "same physical measurement"), and therefore operational compatibility cannot
  automatically be identified with a deeper structure-free access relation. P4 shows
  counterfactual "bracketing" is latent relocation, not elimination. P5/P6 block the
  subsystem and spacetime escape routes as supplied-structure relocations; P7 imposes the
  sharpness-into-interventions requirement. **These tests do NOT prove that one physical
  intervention acquires two incompatible fundamental `C`'s** — that stronger reading is
  withdrawn.
- **Structures it requires as input (complete ledger):** measurement theory; subsystem /
  tensor-factor decomposition; spacetime structure; process algebra / dynamics; a sharpness
  notion (P7). Physicality doc §8.
- **Information price:** all of the above are `SUPPLIED` at the current state of the
  program; nothing in this campaign derived any of them.
- **Comparison to existing formalisms (R6):** operational layer = **RESTATED** (GPTs,
  joint measurability, effect algebras); kinematic layer = **RESTATED in content** (sheaf /
  empirical-models machinery, with added governance discipline); the interpretive
  four-way separation and the hostile tests are the campaign's genuine additions. **No
  comparator providing an observer-independent, structure-free definition was found in
  this targeted audit — NOT FOUND, not DOES NOT EXIST.** See
  `F0_PHYS_BASELINE_AUDIT_01.md` B1–B10.

## 3. What has NOT been earned

- **No access-transition law** (`R_Gamma`/`A_Gamma`/`Cl_Gamma`): not implemented, not
  proposed; requirements only (`F0_FUTURE_LAW_REQUIREMENTS_01.md`).
- **No positive selection** (`S`); **no dynamics** (`U`).
- **No quantum-set derivation**; no Born rule; no geometry; no gravity.
- **No claim of a theory of reality.** No verdict value is a pass condition; nothing
  banked.
- The frozen charter was not modified by any campaign artifact; the frozen branch
  (`ggc0-f0-influence-access-0`) was not touched.

## 4. Supplied / postulated inputs (summary)

For F0-A: none structural (labels, alphabets, contexts, distributions are declared data;
classical-probabilistic scope is a `POSTULATED` scope restriction). For F0-PHYS: the five
supplied structures in §2 above, each priced and never silently promoted. Full detail:
ledger §"Supplied / postulated inputs".

## 5. Unresolved issues (deliberate)

1. Whether an observer-independent physical access notion exists at all (the gate itself).
2. What structure, if any, could distinguish simultaneous / sequential / commuting /
   jointly measurable / jointly realizable without spacetime presupposition (P6).
3. Whether sharpness can be defined for interventions without a measurement theory (P7
   requirement).
4. Deeper representation equivalences for `K` (Formulation §7/§10).
5. The empty-context and non-distributional-scope conventions (Formulation §4.2, §5.2).

## 6. Literature baseline findings

See `F0_PHYS_BASELINE_AUDIT_01.md` (R6-repaired): no comparator supplying an
observer-independent structure-free joint-realizability notion **was found in this
targeted audit** (NOT FOUND, not DOES NOT EXIST); the F0-A layer is the standard
sheaf/empirical setup restated (honestly, with governance additions); the interpretive
separation is the new discipline. Source-verified arXiv links recorded there.

## 7. Firewall confirmation

**No F0-B law was implemented.** The validator classifies no transition as allowed or
forbidden; no candidate `R_Gamma`, `A_Gamma`, `Cl_Gamma`, `S`, `U` exists in any campaign
file; no searches or optimizations were run. Requirements were recorded; candidate dynamics
were not.

## 8. Statuses (R8 — distinct, not to be reinterpreted)

| item | status |
|---|---|
| F0-A finite kinematics | mathematically repaired/validated (12/12 positive + 5/5 negative controls) |
| F0-A mathematical content | RESTATED relative to standard empirical-model/sheaf machinery where appropriate |
| F0-PHYS terminal | `F0-PHYS-OPEN` (RATIFIED) |
| Operational meanings of `C` (meanings 1–2) | `F0-OPERATIONAL-ONLY` |
| Attempted precision routes requiring supplied structure | documented `F0-PHYS-RELOCATED` failure modes |

## 9. STOP

**STOP FOR OWNER REVIEW.** No F0-B work, no second campaign, no merge into `main`.
Branch pushed and verified from the remote (see commit report in
`F0_EXECUTION_01_STATUS.json` and the final report to the owner).
