# F0 G0 — IDENTIFIABILITY 01
**Status:** campaign artifact. Exact results (`f0_g0_solver.py`, rational arithmetic).
Summary of the identifiability computation per level and per control.
**Repaired 2026-10-06 under owner ruling (R1, R4, R5):** `F0_G0_REPAIR_PROVENANCE_01.md`.

## 1. Setup

Admissible set: `Adm_Γ(input)` = all probability-valued empirical models satisfying the
declared constraints (normalization per context; no-disturbance/overlap compatibility;
support zeros where a support is supplied; declared event relations where justified).
Computation: exact RREF over Fractions; affine dimension = variables − rank; explicit
distinct models exhibited when non-unique.

## 2. Results by level

### G0-B (C + E)

| scenario | variables | affine dim | verdict |
|---|---|---|---|
| K0 complete classical | 8 | 3 | non-unique |
| K1 path | 14 | 5 | non-unique |
| K2 triangle | 18 | 6 | non-unique |
| K3 Bell four-cycle | 24 | 8 | non-unique |

A polytope in every case. The consistency constraints remove only normalization and
marginal-determination freedom.

### G0-C (C + E + support)

- Full support: dimensions unchanged (support ⊇ sections adds nothing).
- K2 + correlated-pair support: dim 6 → **1**.
- K2 + anti-correlated support: dim 6 → **0** — **unique** (the model is forced: uniform
  anti-correlated pair distributions, the nonextendable K2 configuration).

### G0-D (C + E + support + relations)

Declared exclusivity/normalization-partition relations constrain regions (further
dimension reduction where supplied) but no principle *within the static ladder* selects
which relations a scenario has. Relations identify only when imported with a theory
attached (G0-E).

### G0-E (comparators)

Gleason-type, GPT-cone, CT-probability: all derive statistics only after supplying rich
additional structure (geometry/cones/superinformation conditions). Details: baseline
audit.

## 3. The hostile no-go control (G0-K4) — witness repaired [R1]

**Semantics declaration (previously stated only in §5, now binding at this site):** in
this campaign "support" is a **declared possibility input** — zeros are imposed *off*
the declared set, while p>0 *on* the set is permitted, not enforced. A model's
**derived support** (the standard empirical-model meaning) is its set of p>0 sections.

**Primary witnesses** (Bell four-cycle, binary outcomes; machine-checked by the solver:
0/24 constraint violations each, strictly positive on all 24 sections):

- Γ_U: singletons uniform; all four pair contexts uniform — p = 1/4 on each section;
- Γ_T: singletons uniform; all four pair contexts tilted — p(00) = p(11) = 3/8,
  p(01) = p(10) = 1/8.

Identical X, alphabets, C; **identical full support under BOTH the declared and the
derived reading**; both normalized and no-disturbing; Γ_U ≠ Γ_T. **Therefore
C + E + full support does not identify Γ.**

**Remark (owner ruling, 2026-10-06).** The basic statement needs no cycle: a single
context with ≥2 outcomes already admits many full-support distributions.
Cyclic covers matter for *contextual structure* — the cyclic exhibit shows the freedom
persists under the full no-disturbance coupling of a contextual cover — not for the
basic statement that possibility does not determine weights.

**Secondary exhibit (the pre-repair pair, relabeled).** Γ₁ (all pair contexts uniformly
correlated — p(00) = p(11) = 1/2) vs Γ₂ (uniformly anti-correlated — p(01) = p(10) =
1/2): both admissible under **declared**-full support (0/24 violations each,
machine-checked), but their **derived** supports are disjoint on every pair context
(16/24 sections each). This pair therefore witnesses a different fact: **the declared
possibility set does not even pin the derived support.** Its pre-repair description
("identical X, alphabets, C, **full support**") was true only in the declared sense, which was not stated at
this site; it does not witness same-*derived*-support/different-weights (the primary
pair above does).

The K2 anti-correlated case still shows the *limit*: uniqueness can occur, but only when
the supplied support is so restrictive that it forces the model.

## 4. Coupling classification (charter §7) [R4]

| class | reached? | evidence |
|---|---|---|
| C0 NONE | reached at G0-B/G0-C-full-support | dims > 0 everywhere without special support |
| C1 SUPPORT ONLY | **earned as the general behavior** | support zeros remove freedom; which support obtains is unforced data |
| C2 INEQUALITY | reachable only with supplied event relations (G0-D) or theory import (G0-E) | exclusivity-style bounds require the exclusive structure as input |
| C3 MEASURE CLASS | only via G0-E structures (Gleason geometry, cones, CT superinformation conditions) | comparator audit |
| C4 UNIQUE | reached locally in special support cases (K2 anti-correlated) | exact computation |

**Primary classification: C1 — SUPPORT ONLY**, with C4 reachable locally by special
supports and C2/C3 only via supplied richer structure.

## 5. Possibility vs zero probability

- In G0's own setup: support zeros are imposed as constraints (impossible ⇒ p = 0,
  **definitional at the support level**); the converse is **not** assumed — a section may
  lie in the support yet receive weight 0 in a particular admissible model. Concrete
  instance: K2 with full support — the anti-correlated model assigns weight 0 to
  correlated sections, which remain in the declared support (declared-possible) [R5]. This gap is
  recorded as potentially load-bearing for a future GRUT relation (it is exactly where a
  possibility→weights principle could bite, and where standard frameworks are silent or
  definitional).

## 6. Symmetry

Uniform Γ is derivable from scenario automorphisms **only after a state-invariance
postulate** ("the model must be invariant under every automorphism"). That postulate is
priced, not assumed: scenario symmetry and state symmetry are different claims. No
state-invariance principle is available in the static structure. (Recorded; `UNRESOLVED`
as to whether a future law could justify such a postulate.)

## 7. Critical whole-law question (charter §8) [R4]

> Is there room for a genuinely F0-specific possibility/statistics relation?

**Yes — narrowly but precisely.** All known nontrivial constraints enter by supplying
extra structure (event relations, geometry, cones, superinformation conditions); at the
bare static level the possibility structure is **C1-class**. The room for a GRUT-specific
relation is therefore exactly:

- the **support-determination problem**: what fixes Supp_C (and, more finely, the
  zero-weight-but-possible boundary) from the declared possibility/support structure's physical origin — no physicality assumption is priced here (F0-PHYS gate OPEN) [R5]; the standard frameworks
  either assume it as data or derive it from geometry;
- and, downstream of that, any principle that selects *within* the support polytope
  without importing Hilbert geometry, GPT cones, exclusivity axioms, or decision-weight
  structures.

If neither exists, GRUT's possibility/statistics layer is C1: possibility says which
events can occur; statistics is additional supplied data. That would be a decisive,
sharp negative — telling us exactly what the missing primitive must contain.
