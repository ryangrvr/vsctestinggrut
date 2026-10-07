# STATE

**Updated:** 2026-10-07.
- **Branch:** `grut2`, forked from the SD0 execution tip `a25d1be`, so the full F0 record
  is in the tree. Per ruling G2-11 it is merged into `main` with history preserved, and
  `grut2` is kept as a historical branch.
- **R1 terminal boundary:** `dbfd64b`.
- **Builder:** Claude Code. VS Code is paused (role kept, inactive; see
  `DIVISION_OF_LABOR.md`). The two-hourly VS Code review routine is disabled (G2-11).
- **External checking:** `PROGRAM/CHECKS.md` (RULES rule 8). Nothing is banked until it
  is checked. A merge is provenance, not endorsement: items marked "external check
  pending" stay pending.

## Where we are

**Stage 1 (SD0): COMPLETE.** **Stage 2 (R1): TERMINAL, ACCEPTED** (G2-11, at `dbfd64b`).

**Stage 3: AUTHORIZED TO OPEN — charter phase.**
- The Stage-3 charter is written and frozen **alone**, before any 𝒦 candidate exists.
- Then STOP for owner review before Card 1.
- No 𝒦 card is generated, frozen, scored or optimized before that review.

## Last results

**Stage 1 — SD0 referendum: failed as a law; old F0 banked.**
- Terminal: `F0-SD0-OPEN`. Record: `F0_SD0_RESULT.md`, `F0_SD0_STATUS.json`.
- The ASP candidate passed every preregistered gate and four blind holdouts, but earned
  no new law:
  - its mechanism overlaps operator-assignment / bounded-width CSP theory;
  - it over-allows the theta parity system;
  - the comparator audit was stopped at 1/5.
- Old F0 is now a banked library: `F0_REQUIREMENTS_CONSOLIDATION_01.md`, R1–R15, none
  discharged.

**Stage 2 — R1: TERMINAL, ACCEPTED** (G2-11; `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md`).

R1 **earns** a conditional operational reciprocity observable,
ε_R^(T)(S:E) := inf over P★ of max over a of d_op^T(P_a, T·P★):
- built from standard mathematics;
- with an explicit identifying assumption, the common carrier / readout certificate;
- with a calibrated BRI1 realization:
  - Tier 1 R1-PASS, DERIVED (SCOREBOARD #10);
  - Tier 2 R1-PASS, evidence grade (SCOREBOARD #11).

R1 does **not** earn:
- new mathematics;
- a fundamental law;
- a distinctive physical relation;
- a confirmed prediction;
- CROSS-SECTOR status.

D5 (governing audit; `D5_COMPARATOR_AUDIT.md`):
- (M) and (P) are both STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION.
- DISTINCTIVE was not earned.
- The kill condition does not fire.

## R1 open upgrades (non-blocking unless one uncovers a contradiction; G2-11)

- **M5:** a theorem-grade Tier-2 expansion (uniform multivariate Edgeworth in
  normal-score coordinates).
- **D4:** finite-sample testing. BRI1's single-time witness needs about 10¹¹ samples at
  the frozen parameters.
- **Tier-2 carrier-necessity question** (D5).
- **Remaining external theorem checks:** A-BL, F, M1–M3, Prop. G, and the D5 analyses
  C1–C6. Their CHECKS lines stay pending.
- **WO-001 C3 and C4:** laboratory preparation.

## Next action — Stage 3 charter (G2-11)

**Central task.** Find a compact selective law 𝒦 that generates persistent
differentiation and makes interface/response structure non-independent:
𝒦 → Π → [h]_{T_Π} → T_Π → Γ_Π → ε_R. The law must force at least one measurable relation
ℛ(Π, T_Π, ε_R, Γ_Π) = 0 that existing frameworks do not independently impose.

**What the charter must fix before any candidate exists:**
1. **Baseline freedom spaces** 𝒜_Π, 𝒜_T and 𝒜_Γ.
   - ε_R is derived, ε_R = ε[Γ_Π, T_Π]. 𝒜_ε is the image of 𝒜_Γ × 𝒜_T, not a free axis.
   - The spaces are computed after imposing causality, positivity, KMS/FDT, Onsager
     reciprocity and conservation laws.
2. **Success criterion:** nontrivial freedom reduction + positive compression + a
   measurable consequence. Definitional relations do not count.
3. **Compression accounting** and information-price rules.
4. **Nonrelocation:** the carrier, partition, interface class, readout class, Gibbs/FDT
   structure and target relation may not be hidden in the inputs.
5. **Budget:** at most three genuinely distinct 𝒦 cards.
6. **Required contents of every card:**
   - the exact law;
   - its information price;
   - the structures it generates;
   - a measurable target;
   - a hostile baseline comparison;
   - a kill condition;
   - the declared response scope (quotient-irreducible back-reaction vs response in
     general).
7. **Originality:** novelty is judged only at the assembled-law level.
8. **Cross-sector gold standard:** parameter transfer.
9. **Stopping rule:** if the budget fails, this generative route terminates. No new
   prerequisite staircase.

**Also:**
- Derive carrier/readout structure modulo representation. Do not assume a unique
  formula for h.
- Do not presume any monotonic identity–response tradeoff.

## Stage definitions 4–6 (pointer)

- **Stage 4 gates.**
  - **Selectivity:** the solution set is strictly smaller than the unconstrained space,
    and does not admit classical, quantum and super-quantum structures
    indiscriminately.
  - **Differentiation:** a stable approximate partition Π and its T_Π are generated,
    not supplied.
  - **Nonrelocation:** neither Π nor T_Π is encoded in the inputs.
- **Stage 5.** 𝒦 forces ℛ(Π, T_Π, ε_R, Γ_Π) = 0, a measurable loss of freedom not
  independently imposed by existing frameworks. Then a sealed holdout or experiment.
- **Stage 6.** The same 𝒦, unmodified, gives quantum, thermodynamic and gravitational
  regimes. The same ε_R (same quotient, same distance) is exported to a gravitational
  ensemble, with local back-reaction used as calibration only.
- **Not inputs to 𝒦:** memory, viscoelasticity and crystalline order. Check for them as
  effective regimes after Stage 4.

## Blockers

None. The owner reviews the Stage-3 charter before Card 1.

## Branch map

| Branch / ref | Contents |
|---|---|
| `main` | Canonical after the G2-11 merge of `grut2`: an explicit merge commit, history preserved |
| `grut2` | Historical working branch (Stage 1 close, R1). Kept after the merge |
| `r1-terminal` (tag) | R1 terminal boundary `dbfd64b`. If a tag push is blocked, it is recorded here and in the merge commit message, for the owner to tag locally |
| `record-integration-01` | Consolidated frozen TestingGRUT record: `record/`, `registry/`, `governance/` |
| `bri1-manuscript` | BRI1 manuscript plus its byte-exact record (`92dc6bb`) |
| `ggc0-f0-program-consolidation-0` | The governing requirements map |
| `ggc0-f0-sd0-exec01-0` | SD0 execution (`grut2`'s parent) |
