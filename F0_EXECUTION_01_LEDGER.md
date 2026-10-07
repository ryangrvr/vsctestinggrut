# F0 — EXECUTION 01 LEDGER
**Rule:** every load-bearing element of this campaign carries exactly one status. **Nothing
receives a stronger status silently** — upgrades are explicit entries with a reason and, for
`DERIVED`/`CONSTRUCTED`, an artifact pointer. Statuses are auditable against the artifacts.

## Status bins (definitions)

| bin | meaning |
|---|---|
| `DERIVED` | obtained by proof/argument from explicitly listed inputs (pointer required) |
| `CONSTRUCTED` | explicitly defined here, finite and checkable (validator-covered where applicable) |
| `SUPPLIED` | inserted as an input this campaign does not earn (each instance listed) |
| `POSTULATED` | assumed with a declared scope, weaker than SUPPLIED (no proof, but flagged) |
| `REPRESENTATIONAL` | a property of how things are written down, not of the object |
| `OPERATIONAL` | defined via procedures/experimenters; not observer-independent |
| `PHYSICAL-CANDIDATE` | observer-independent candidate; correctness not claimed |
| `UNRESOLVED` | question deliberately left open, with its reason |
| `STRUCTURAL-FAIL` | a proposed definition/property failed a check; recorded with reason |
| `RESTATED` | identified as an existing formalism with no added relation (R9) |

## Ledger

| # | element | status | artifact / reason |
|---|---------|--------|-------------------|
| L1 | Primitive intervention labels `X` (finite, uninterpreted) | `CONSTRUCTED` | `F0_A_KINEMATIC_FORMULATION_01.md` §2; validator covers instantiation |
| L2 | Outcome alphabets `O_x` (finite) | `CONSTRUCTED` | Formulation §3 |
| L3 | Context structure `C` = downward-closed family, canonical | `CONSTRUCTED` | Formulation §4; downward closure is validator-verified (K0–K3) |
| L4 | Hypergraph equivalent formulation | `CONSTRUCTED` | Formulation §4.4; equivalence `DERIVED` (Formulation §4.5) |
| L5 | Maximal contexts, overlaps | `CONSTRUCTED` | Formulation §4.6; validator-verified |
| L6 | Event presheaf `E` on `C` with restriction maps | `CONSTRUCTED` | Formulation §5 |
| L7 | Distinction "Γ is not the presheaf" | `DERIVED` | Formulation §5.3 (Γ = family of distributions; presheaf = event/value structure) |
| L8 | Γ = `{p_C}` with normalization, positivity, overlap compatibility | `CONSTRUCTED` | Formulation §6; validator checks normalization/positivity/compatibility on supplied instances |
| L9 | Naming "overlap compatibility / no-disturbance" (Bell specialization: no-signalling) | `CONSTRUCTED` (naming), `REPRESENTATIONAL` (status of the name) | Formulation §6.2 — explicitly NOT fundamental causality |
| L10 | Representation equivalence (4 declared moves) | `CONSTRUCTED` | Formulation §7; relabeling invariance validator-verified; deeper equivalences: `UNRESOLVED` (proof not given) |
| L11 | Composition/gluing of descriptions | `CONSTRUCTED` | Formulation §8; **composition ≠ physical joint accessibility** — see L13 |
| L12 | Statement: gluing never silently creates an accessible context | `DERIVED` | Formulation §8.2: glued set is added to `C` only by an explicit declared act, which is an F0-B matter — recorded as a future-law requirement, not a rule |
| L13 | The physical meaning of "jointly realizable" | `PHYSICAL-CANDIDATE` at best | `F0_PHYSICALITY_OF_ACCESS_01.md`: the strongest candidate (P6/P7-tested) does NOT reach `PHYSICAL-CANDIDATE` without supplied structure — see F0-PHYS result |
| L14 | Interpretations 1 (experimental availability) and 2 (operational joint measurability) | `OPERATIONAL` | Physicality doc §§2–3; apparatus- and class-dependent |
| L15 | Interpretation 3 (physical co-instantiability) | `UNRESOLVED` | Physicality doc §4: no observer-independent definition found that does not require supplied structure |
| L16 | Interpretation 4 (objective structural compatibility) | `UNRESOLVED` | Physicality doc §5 |
| L17 | P1 (apparatus dependence), P3 (coarse/fine), P5 (subsystem dependence), P7 (sharp/unsharp) | `STRUCTURAL-FAIL` for interpreting `C` as fundamental via those routes | Physicality doc §7 — with reasons recorded |
| L18 | P2 (relabeling), P4 (observer ignorance) | `DERIVED` (negative results: they do NOT rescue fundamental status) | Physicality doc §7 |
| L19 | P6 (temporal dependence) needs extra structure | `STRUCTURAL-FAIL` (as a definition route), `UNRESOLVED` (what structure suffices) | Physicality doc §7.6 |
| L20 | Validator: K0, K1, K2, K3 all pass | `CONSTRUCTED` + verified | `f0_kinematic_validator.py` test run log in RESULT |
| L21 | Baseline audit findings | see artifact | `F0_PHYS_BASELINE_AUDIT_01.md`; any `RESTATED` verdicts recorded there |
| L22 | Future-law requirements (no law) | `CONSTRUCTED` (as requirements only) | `F0_FUTURE_LAW_REQUIREMENTS_01.md`; **no `R_Gamma` formula, thresholds, searches** |
| L23 | Campaign terminal | `UNRESOLVED` at campaign start → resolved in RESULT | `F0_EXECUTION_01_RESULT.md` |

## Supplied / postulated inputs (complete list)

- Nothing structural is supplied for F0-A itself: labels, alphabets, and the family `C` are
  finite declared data (L1–L8), not derived from any theory.
- For F0-PHYS, candidate interpretations require SUPPLIED structure (recorded per test):
  spacetime locality (P6, L19), subsystem/tensor-factor decomposition (P5, L17),
  a measurement theory / Hilbert-space commutativity for operational routes (L14, L17).
  Each is `SUPPLIED`, never silently promoted.
- The classical-probability representation of Γ in §6 of the Formulation is a declared
  scope (`POSTULATED` as a scope restriction: first realization is probabilistic, classical
  distributions), not a claim that probability is fundamental.
