# F0 G0 — OWNER RULING 01
**Date:** 2026-10-06. **Context:** issued after an independent adversarial audit of the
full F0 chain (13-agent review: four program-level questions, each adversarially
refuted, plus a dedicated G0 inspection; all four campaign scripts re-run; audit record
outside the repository). This artifact records the ruling; the repair executing it is
`F0_G0_REPAIR_PROVENANCE_01.md` on branch `ggc0-f0-g0-repair-0`.

## Confirmed factual findings the ruling rests on

1. **Supports are supplied inputs, not derived.** Every support in G0 is a hand-supplied
   generator set (`f0_g0_solver.py`, support generators); no artifact derives a
   possibility→support relation from upstream structure.
2. **The solver enforces zero probability only *outside* the declared set.** p>0 inside
   the declared support is permitted, never enforced, so zero-weight-but-possible events
   are structurally admitted. G0's "support" is therefore a *declared possibility input*,
   distinct from the standard empirical-model (derived, p>0) support.
3. **The pre-repair K4 witness pair did not have identical standard supports.** The
   correlated and anti-correlated Bell models have disjoint p>0 supports on every pair
   context; they share only the externally declared possible-event set.

## Ruling

- **PROGRAM AUDIT — PASS WITH GOVERNANCE WARNINGS.** The campaign sequence has remained
  scientifically coherent; repeated repairs have generally weakened or corrected claims
  rather than preserving preferred conclusions. Warnings: the additive-repair style
  leaves obsolete claims in live-looking files (architectural fix required before
  publication); terminal-adjacent wording must not outrun earned content.
- **G0 TERMINAL — RETAIN `F0-G0-SUPPORT-COUPLING`, STRICTLY AS THE PREREGISTERED C1
  CLASS.** C1 survives as a preregistered *input-level classification*: the frozen G0
  charter defines G0-C as C+E+SUPPORT, defines `C1 — SUPPORT ONLY` as a classification
  (not a candidate equation), and its success criterion asks whether the supplied
  possibility structure removes statistical freedom. Under that preregistered design the
  computation genuinely shows support-zero constraints can reduce the admissible
  statistical space, sometimes to a singleton. The primary terminal is **not** replaced
  by `F0-G0-NONIDENTIFIABLE` (which stands, correctly scoped, as the bare-level
  sub-finding).
- **EXPLICIT QUALIFICATION — NO POSSIBILITY→SUPPORT LAW WAS DERIVED.** The pre-repair
  sentence "A principled possibility→support relation is the only earned coupling
  channel" was too strong: no such relation was earned. What G0 earned is narrower:
  **given supplied support information, support zeros constrain Γ; bare compatibility
  does not identify Γ.** Standing prose descriptor from now on: the **C1
  supplied-support constraint**.
- **K4 WITNESS — REPAIR REQUIRED.** Replace the witness with two different strictly
  positive distributions satisfying the same no-disturbance constraints: genuinely
  identical full p>0 support, different weights. Note that the basic nonidentifiability
  point is more basic than cycles — a single ordinary finite context with at least two
  outcomes already admits many full-support distributions; cyclic covers matter for
  contextual structure, not for the basic statement that possibility does not determine
  weights.
- **PHYSICALITY WORDING.** G0 must say "declared possibility/support structure" or
  "compatibility/event-possibility input" rather than "physical possibility" unless a
  physicality assumption is explicitly priced: PHYS-02 ended OPEN, and no fundamental
  physical interpretation of `C` is possessed. This is not cosmetic; it prevents quietly
  upgrading an unresolved operational/static object into ontology.
- **NEXT SCIENTIFIC FRONTIER — SUPPORT DETERMINATION (A), AFTER CONSOLIDATION.** No new
  campaign immediately. The highest-value next action is a program consolidation
  decision: consolidate the live requirements into one authoritative map and choose one
  frontier. Exactly two real candidate frontiers exist: **A. SUPPORT DETERMINATION**
  (what makes an event possible/impossible: physical/task structure → Supp — the
  qualitative law G0 explicitly did not derive) and **B. WITHIN-SUPPORT WEIGHT
  SELECTION** (Supp → Γ — closer to the Born/statistical problem, likely harder).
  Preference: **A first** — not because G0 proved support coupling (it did not), but
  because G0 showed support is the first level at which qualitative possibility can
  materially reduce statistical freedom, some supports even forcing a unique empirical
  model. If the theory cannot generate the zero structure at all, there is no reason to
  expect it to generate precise positive weights.

## Scope

This ruling authorizes the numbered repair R1–R6 on G0's campaign artifacts and the
program consolidation artifact. It does not authorize F0-B, any Γ-coupling equation, or
any new campaign.
