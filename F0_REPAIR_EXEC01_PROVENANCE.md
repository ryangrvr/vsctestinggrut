# F0 — EXEC 01 REPAIR PROVENANCE
**Date:** 2026-10-05 · **Status:** narrow repair only, per owner/reviewer ruling on the
execution-01 commit. **No new science; no F0-B; frozen charter untouched.**

## Ruling recorded

- **F0 EXECUTION 01 — REPAIR REQUIRED BEFORE BANKING** (F0-A defects below)
- **F0-PHYS-OPEN — RATIFIED** (terminal unchanged)
- **F0-B — NOT AUTHORIZED**

## Source

| field | value |
|---|---|
| base branch | `ggc0-f0-kinematics-physicality-0` |
| base SHA | `f45fb901746c76beb9cce7a7a1003a6a1aba97ec` |
| repair branch | `ggc0-f0-exec01-repair-0` (created directly from the base SHA) |
| frozen parent (unchanged) | `bef8b9480c9f7569c70837c6ee5c4776fc2e0f3c` |

## Repairs applied

- **R1 — K2 contextual calibration.** The previous perfectly-correlated K2 pair data
  (a=b, b=c, a=c) was globally extendable (p(000)=p(111)=1/2); all "compatible without
  global section / NO global section exists" claims about it are **withdrawn**. K2 now uses
  uniformly **anti-correlated** pairs ((0,1)/(1,0) at 1/2 each; uniform singleton
  marginals): overlap-compatible, and an **exact rational feasibility check** over the
  8-assignment simplex (Gaussian elimination + null-space interval intersection, no
  floating point) verifies **no global distribution on {a,b,c} reproduces all three pair
  marginals**. Recorded only as a **known contextuality calibration — no F0 novelty
  claim**. Nonextendability is verified exactly, not inferred from the absence of the
  triple context.
- **R2 — two-context gluing corrected.** The claim that two compatible finite marginals
  "may or may not" extend was a probability-theory mistake and is **withdrawn**: two
  compatible marginals always admit a joint extension (explicit construction
  `p(a,b,c) = p_AB(a,b)·p_BC(b,c)/p_B(b)`, implemented and verified exactly). The
  obstruction belongs to whole-family (cyclic) extension (Vorob'ev / global-extension
  domain). Formulation §8 now states the three-way distinction: (1) pair gluing — always
  extends; (2) whole-family extension — may fail on cyclic scenarios; (3) physical
  accessibility of the union — never follows from either.
- **R3 — invalid representation move removed.** The draft "redundant presentation" move
  `C ≈ C ∪ {m}` (m = m₁∪m₂) is **withdrawn**: adding a previously absent union context
  changes joint accessibility and is not a representational change. Representation
  equivalence now: intervention-label bijections; outcome-label bijections; family ↔
  maximal-context-antichain presentation swap. No new physical equivalences introduced.
- **R4 — outcome relabeling actually tested; negative controls added.** `relabel()` was
  repaired (outcome-permutation path) and a dedicated `test_outcome_relabel` now exercises
  it; the old "same test" claim covered only intervention permutations. Five negative
  controls added, all passing (i.e. all rejecting malformed input): malformed downward
  closure; non-normalized Γ; negative probability; overlap-incompatible Γ; and the
  calibration check that contextual K2 passes local compatibility while failing global
  extendability. Validator results now reported **separately for positive (12/12) and
  negative (5/5) controls**.
- **R5 — physicality wording precision (terminal unchanged).** P1/P3 no longer claim that
  coarse/noisy/sharp versions are "presentations of the same physical measurement": they
  are generally **different operational interventions/POVMs** (joint measurability is
  defined via coarse-grainings of a common POVM). Earned statement: operational access
  depends on the physically/operationally specified intervention and cannot automatically
  be identified with a deeper structure-free access relation. The terminal remains
  **`F0-PHYS-OPEN`**: NOT FOUND / OPEN, not an impossibility theorem.
- **R6 — baseline search precision.** All categorical "No comparator provides …"
  statements replaced with "No comparator providing … **was found in this targeted
  audit**" (NOT FOUND, not DOES NOT EXIST).
- **R7 — terminology.** The probabilistic Γ scope is now called the **finite ordinary
  probability-valued empirical-model scope** (not "classical"), since a contextual
  empirical model uses ordinary per-context probability distributions.
- **R8 — statuses distinguished** in `F0_EXECUTION_01_RESULT.md` §8: F0-A finite
  kinematics (repaired/validated) ≠ F0-A mathematical content (RESTATED) ≠ F0-PHYS
  terminal (`F0-PHYS-OPEN`) ≠ operational meanings (`F0-OPERATIONAL-ONLY`) ≠ relocated
  failure modes (`F0-PHYS-RELOCATED`).

## Final verification repair (V1–V5, branch `ggc0-f0-exec01-validator-final-0` from
## `003ffcdd35822513be5f6e5aeeaa004331760b2b`)

- **V1 — intervention relabeling corrected.** `relabel()` kept tuples in source-coordinate
  order; now it maps old-coordinate values to renamed labels and emits the target tuple in
  sorted target-context order. Verified on a deliberately **asymmetric calibration object**
  (`p_ab = (1/10, 2/10, 3/10, 4/10)` with exactly derived singleton marginals): under
  `a↔b` the probability table must **transpose** — the previous symmetric Bell
  distributions could not expose the bug.
- **V2 — non-vacuous outcome/combined tests.** Outcome-flip now flips **only b's**
  alphabet on the asymmetric table (the old all-flip on p(00)=p(11)=½ was invariant, so a
  broken implementation passed vacuously); exact table checks, not just
  normalization/compatibility. A **combined** intervention+outcome test added, with its
  exact derived semantics (`p'_ab(s1,s2) = p_ab(s2, 1−s1)`).
- **V3 — positivity isolated.** The negative-probability control now sums **exactly to 1**
  while containing a negative entry, so rejection exercises the positivity branch
  specifically; the separate non-normalization control is retained.
- **V4 — terminology:** status JSON scope renamed "finite ordinary probability-valued
  empirical-model scope"; baseline B5 corrected (contexts = compatible
  measurement/intervention sets; `E(C)` = local sections/outcome assignments); B7 source
  corrected to CDP **quantum combs / quantum networks** (not Oreshkov-style process
  matrices).
- **V5 — verification standard:** all three relabel tests (intervention, outcome,
  combined) are asymmetric and each carries an explicit **non-vacuity check**: each test
  verifies that replacing the transform with the identity would fail it. Retained all
  prior positive/negative controls. Full suite: **13 positive + 5 negative, all PASS.**

No terminal change: **`F0-PHYS-OPEN` stands.** No F0-B; no F0-PHYS-02 authorization
implied; frozen charter untouched.

## Firewall confirmation

No `R_Gamma`, `A_Gamma`, `Cl_Gamma`, `S`, or `U` implemented; no access-law or fixed-point
searches; frozen charter unmodified; no merge to main. Repair-only commit(s).
