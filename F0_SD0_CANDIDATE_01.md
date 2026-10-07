# F0 SD0 — CANDIDATE 01 (preregistration): the Anchored-Support Principle (ASP)
**Date:** 2026-10-06 · **Stage 3 of Owner Ruling 05 C4.** On commit, this candidate is
**immutable for SD0-EXEC01**; any substantive modification is a new candidate
requiring later owner authorization. The commit SHA of this artifact is the candidate
SHA. Reference implementation: `f0_sd0_candidate_asp.py` (frozen with this artifact;
it implements the statement below — a later fix realigning code to this frozen
statement is evaluation-tooling repair, not candidate modification, and must be
logged as such).

## 1. Exact mathematical statement

**Setting** (all finite, all Boolean; no weights anywhere). A **task structure** is
Σ = (X, 𝒞, (E_x)_{x∈X}): a finite set of variables X, a cover 𝒞 of subsets of X (the
contexts — co-measurable sets), and a finite outcome set E_x per variable. A
**support table** on Σ is S = (S_C)_{C∈𝒞} with ∅ ≠ S_C ⊆ ∏_{x∈C} E_x, satisfying
possibilistic no-signalling (pNS): for every x and all C, C′ ∋ x,
proj_x S_C = proj_x S_{C′} =: P⁰_x.

- **D1 (event).** An *event* is a pair (U, s) with ∅ ≠ U ⊆ C for some C ∈ 𝒞 and
  s ∈ proj_U(S_C) for at least one such C.
- **D2 (steering closure).** Given an event (U, s), set P_x := {s(x)} for x ∈ U and
  P_x := P⁰_x otherwise, and iterate to the (unique, monotone-decreasing) fixpoint:
  for each C ∈ 𝒞, R_C := {t ∈ S_C : t(x) ∈ P_x ∀x ∈ C}, then P_x := proj_x R_C for
  each x ∈ C. The event is an **anchor** iff at the fixpoint every R_C ≠ ∅.
- **D3 (anchored).** S is *anchored* iff it has at least one anchor.
- **D4 (sub-realization).** For ∅ ≠ U ⊆ X: Σ|U has variables U, cover = the maximal
  elements of {C ∩ U : C ∈ 𝒞} \ {∅}, and support (S|U)_D := ⋃{proj_D S_C : C ∈ 𝒞,
  C ∩ U = D}. (Each S|U is again a pNS support table.)

**THE LAW (ASP): 𝔄(Σ) := { S : S|U is anchored for every ∅ ≠ U ⊆ X }.**

Reading: an admissible possibility pattern must, in every part, contain at least one
possible event whose complete chain of certainty-consequences (iterated possibilistic
steering across all contexts) closes without contradiction. A pattern all of whose
possible events refute themselves under their own forced consequences — a *totally
self-refuting* pattern — is forbidden; and no sub-realization of an admissible
composite may be totally self-refuting.

## 2. Input signature / output / invariances

Input: Σ only — no party labels, no dimension, no capacity, no weights; composition
is consumed through D4 and the product construction, both built from (X, 𝒞, E).
Output: 𝔄(Σ), decided table-by-table by a finite Boolean computation. Invariances:
variable/outcome relabellings, party exchange; no scenario names, no constants, no
probability appears anywhere. Closure (proved in the design record, mechanically
spot-checked): mixing-union over whole families; independent products; heredity
(S ∈ 𝔄 ⟹ S|U ∈ 𝔄).

## 3. Free choices and information price (R10; per `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`)

| # | Choice | Content |
|---|---|---|
| F1 | propagation operator = per-variable arc-consistency closure, from the ladder {unit propagation, per-variable AC, relational/path consistency, full extension} | ~2 bits |
| F2 | anchor quantifier = EXISTENTIAL over events | 1 bit |
| F3 | event domain = sections over nonempty co-measurable subsets, possible in ≥1 covering context | 1 bit |
| F4 | heredity scope = all nonempty variable subsets, union-projection onto maximal induced contexts | ~1.5 bits |
| F5 | domain = pNS support tables (inherited program convention; arguably a constraint) | — |

No continuous parameters, thresholds, per-control constants, case splits, or lookup
rows. ≈ 5–6 bits of selection against D = 8 counted distinctions. Full audit at
evaluation.

## 4. Provenance, motivation, and design disclosures

Produced by a five-angle independent design panel (composition / generation /
symmetry / extension / family-relational; full returns preserved in the session
record). Four of the five proposals (ASP; GEN-AT, transport-censorship; CCT,
transport holonomy; HR, hereditary refinability) **converge extensionally on
(2,2,2)** — forbidding exactly the 8 PR boxes — as any gate-passing law must (Lal);
they diverge beyond it. ASP was selected because: its full battery was independently
re-run and reproduced by the orchestrator; its statement is the cleanest with proved
closures; it catches the fine-grained-PR stress case *without* a merge quantifier
(cross-run, 0/28 anchors), removing GEN-AT's advantage while avoiding GEN-AT's
self-flagged top risk (merge-robustness over-forbidding at SD-K6); it admits the
Cabello-18-ray bipartite max-entangled support (quantum, strongly contextual, 4×4:
432/864 anchors, heredity spot-checked over 298 subsets), where OCC-style universal
seeding over-forbids 512 realizable (2,2,2) logical tables; and its restatement risk
is argued low (provably inequivalent to the AB hierarchy, AvN/cohomology, LO, and
solution-group criteria on computed instances; nearest CSP neighbors — failed-literal
/ singleton-consistency techniques — are algorithmic tools, not published
support-admissibility laws; audit to check AGK robust-CSP and SAT-preprocessing
literature).

**Disclosures.** (i) The designer read the worktree and therefore saw the SEALED
expected classifications of G1/G2 (they are preregistered-not-blind checks per C2;
verdicts were computed mechanically; blindness is not claimed — the genuine holdouts
of C3 remain the anti-fitting test and do not yet exist). (ii) The designer's
K7-soundness argument used a from-memory claim (no bipartite binary-outcome
pseudo-telepathy) — audited under K7(ii) via the verified BMT scope instead.
(iii) Four panel angles initially failed on session limits and were completed on a
resumed run; all five returned before this freeze.

## 5. Predicted behavior (structural; designer-computed + orchestrator-verified)

ALLOW and verified by computation: all 1721 local and all 1232 logical (2,2,2)
tables; canonical Hardy (its unique exploding event is exactly the Hardy-paradox
event); GHZ (3,2,2) (76/108); Peres–Mermin (114/114); bipartite magic-square game
(96/96); CEG-18 bipartite (432/864); G1 (432/432); G2 (15/22). FORBID and verified:
all 8 PR boxes (0 anchors); all 480 strong XOR-(2,3,2); 5,667/5,667 sampled strong
(2,3,2) tables; PR⊗PR (0/288); embedded-PR (2,3,2) via heredity; fine-grained PR
(0/28); Specker triangle (0/12); chained-PR 6-cycle (0/24). **Predicted, not yet
computed:** SD-K6 at minimum dimension 3×3 (ALLOW predicted; §7).

**Known boundaries (recorded now, before evaluation).** ASP generates a
**possibility-level outer approximation** of the quantum-admissible family, not a
realizability characterization: (a) it admits the 240 (2,2,2) pNS tables with no
exact-support probabilistic realization (its declared target object is the
declared-possibility family, per R11); (b) it admits padded-PR in (2,2,3) (PR cells
plus an extra possible outcome pair; 8/24 anchors) — quantum status of that pattern
unknown; (c) it admits the theta-graph parity system ({p,q,r} even, {p,q,s} even,
{r,s} odd; 10/38 anchors), which has **no quantum model** (J = e) — an identified
over-allowance, caught by the panel's CCT proposal and recorded as a comparator fact
and a post-SD0 question for the owner.

## 6. Kill conditions (any one → the stated terminal, no tuning)

- K-a: any SD-K FORBID gate instance admitted, or any SD-K ALLOW gate instance
  forbidden → gate failure; terminal per charter (OPEN or NO-GO reasoning recorded).
- K-b: the compactness audit finds the effective adjustable structure approaching the
  targets' information content → `RELOCATED` (lookup structure), regardless of gate
  passes.
- K-c: the comparator audit finds ASP equivalent to an existing principle (LO, a
  lattice reconstruction, AB-hierarchy class, solution-group criterion, or a
  published CSP-based admissibility law) → `RESTATED`.
- K-d: a genuine post-freeze holdout with literature-established quantum realizability
  is FORBIDDEN by ASP → unsoundness; reported as such, and `LAW-CANDIDATE` is
  unavailable (per C3, a badly-failing candidate cannot be treated as validated).
- K-e: SD-K10 answered NO by the evaluation as a whole → the preregistered
  `RELOCATED` statement fires.

## 7. Evaluation plan (binding declarations, made before evaluation)

- **SD-K7(i) declared finite family:** the 8 PR boxes (2,2,2); the 480 strongly
  contextual XOR-type (2,3,2) supports; embedded-PR (2,3,2); fine-grained-PR
  (Alice binary, Bob 4-outcome). All must be FORBIDDEN. K7(ii): audit against the
  POVM-inclusive BMT theorem scope (theorem-level, not finite computation).
- **SD-K6 instance (minimum dimension):** the CHTW Kochen–Specker game support —
  Alice: a triad T of a pure-triad ℝ³ KS set (output: which vector is colored 1);
  Bob: a vector v ∈ T (output: its color); support cells {(i, [T_i = v])}. The
  pure-triad set is constructed by cross-product completion of the Peres 33-ray set,
  in exact arithmetic over ℚ(√2), with uncolorability machine-verified (= strong
  contextuality of the support). Supplementary computed evidence at 4×4: CEG-18
  bipartite (already ADMITTED). The game support's quantum realization is the
  maximally entangled two-qutrit state (verified source: BMT full text; CHTW §3.4).
- **Order (C4 Stage 5):** SD-K1–K10 → comparator/null audit → G1–G3 → genuine
  holdouts. Failures recorded as failures; no tuning; one terminal; STOP.
