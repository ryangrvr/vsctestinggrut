# STATE

**Updated:** 2026-10-07 · **Branch:** `grut2` (forked from the SD0 execution tip
`a25d1be`, so the full F0 record is in the tree).
**Builder:** Claude Code. VS Code is paused (role kept, inactive; `DIVISION_OF_LABOR.md`).
**External checking:** `PROGRAM/CHECKS.md` (RULES rule 8). Nothing is banked until it is
checked.

## Where we are

**Stage 1 is COMPLETE. The next stage is Stage 2 (R1).**

## Last result — Stage 1, SD0 referendum: FAILED as a law → old F0 BANKED

SD0 ended with terminal `F0-SD0-OPEN`. Record: `F0_SD0_RESULT.md`,
`F0_SD0_STATUS.json`.
- **The candidate passed every test.** The frozen candidate ASP (anchored-support
  principle) passed every preregistered gate. It also passed all four blind
  post-freeze holdouts.
- **No new law was earned.**
  - Its mechanism largely overlaps known operator-assignment / bounded-width CSP
    theory (Atserias–Kolaitis–Severini; Bulatov–Živný).
  - It over-allows the non-quantum theta parity system, so it is an outer
    approximation.
  - The comparator audit was stopped at 1/5, at owner direction.
- **Per the build prompt, old F0 is now a banked library of constraints and no-gos.**
  - Governing requirements map: `F0_REQUIREMENTS_CONSOLIDATION_01.md`, R1–R15, none
    discharged.
  - There is no follow-on access, factorization, or interface campaign.

## Next action — Stage 2: R1, the operational reciprocity object (prove or kill)

Definition:

ε_R^(T)(S:E) = inf over P★ and {t_a ∈ T} of max_a d_op(P_a, (t_a)#P★)

- P_a is the full intervention-conditioned multi-time process law.
- T is the maximal independently calibrated, environment-preserving interface class:
  frozen before testing, closed under composition, with no unrestricted per-protocol
  maps.

Deliverables:
1. ε_R = 0 for every exogenous process whose protocol dependence factors through T
   (including colored and non-Markovian noise).
2. BRI1 is a special case (signed-affine T; skewness is one witness; ∝ 1/N_B). BRI1's
   record is on branch `bri1-manuscript` @ `92dc6bb`.
3. Invariance on equivalence classes, and behavior under legitimate coarse-graining.
4. Identifiability from finite intervention data.
5. Comparator audit: non-Markovianity measures; generic nonlinear response;
   Janzing–Schölkopf; independent causal mechanisms; MDL causal discovery; invariant
   causal prediction; Blackwell–Le Cam deficiency; process tensors.

Kill condition: R1 is killed only if the object is trivial, unidentifiable, or reduces
to non-Markovianity or to generic nonlinear response. ε_R is an observable, not the
law, so overlap with known machinery is acceptable here.

**Stage 2 progress (2026-10-07).** Rulings G2-01 … G2-07 are in
`PROGRAM/OWNER_RULINGS.md`.
- **R1 definition, FROZEN** (`PROGRAM/RESULTS/R1/R1_T_LADDER.md` §0).
  - **T:** T_R1 = GL(k) with translations, plus calibrated nonlinearities removed by
    known maps.
  - **Common-carrier / mode-stability commitment:** arbitrary latent dimension, one
    latent-to-record map h, no h_a.
  - **d_op:** the bounded-Lipschitz quotient (center, whiten, then O(k)).
  - **Empirical rule:** a mode-stability certificate is required; otherwise NO
    RECIPROCITY VERDICT.
  - **D5 must separate:** (A) calibrated interface, (B) mode selection, (C) a
    responding environment.
- **Derived in v3** (pending external check):
  - Theorem A-BL.
  - Theorem F: the distance to the symmetric orbit is ≥ |E f_odd|/‖f‖_BL (constant 1,
    sharp). For two protocols ε_R = ½·d_q exactly, so ε_R ≥ ½·|E f_odd|/‖f‖_BL.
  - The copula theorem M1 (exact quotient) and M2 (symmetry certificate).
  - M3: rank J = k.
  - Mode-selection trivialization E1 and counterexample E2.
- **WO-001 (Claude Code builds):** C1 ACCEPTED; C2 done, including the process fixes;
  C3 next. C4 is laboratory preparation and does not block Stage 3.
- **WO-002 (Claude Code builds; frozen by G2-07):**
  - **The question:** does BRI1 change its copula class modulo reflections?
  - **Status:** computation running, with an independent re-implementation as a
    cross-check.
  - **Preregistered outcomes:**
    1. leading-order nonzero → escape at leading order;
    2. zero → exact finite-N_B radial asymmetry before any verdict;
    3. exactly one orbit → this branch KILLED.
- **R1 boundary (G2-08):**
  - Tier 1, calibrated-readout (GL(k) plus common carrier): BRI1 is **R1-PASS**,
    banked by ruling; its SCOREBOARD entry waits for the external check.
  - Tier 2, T_mono with reflections only, is the declared top of R1.
  - Stopping rule: if BRI1 lies in one copula reflection orbit, the spine ends and Tier 1
    stays banked.
- **R1 exit gate:**
  - (i) T fixed — done;
  - (ii) WO-002 yes/no;
  - (iii) d_op frozen with the proved inequality — derived, awaiting check;
  - (iv) D5, including mode selection — not started.
  - Then R1 is terminal and Stage 3 opens.
  - **No Stage-3 candidate is frozen, scored or optimized before then.**
- **Identifiability flag:** about 10¹¹ samples for BRI1's witness at these parameters
  (Review 2 and its erratum).

## Stage definitions 3–6 (pointer)

- **Stage 3** (limits per ruling G2-08 item 8).
  - **Success criterion:** freedom reduction relative to baseline spaces frozen before
    any card, plus positive compression, plus a measurable relation.
  - **Cross-sector** means parameter transfer.
- Ξ ≠ Γ, with Γ_Π = Obs_Π(Ξ). At most three 𝒦 cards. Each card states:
  - the law;
  - its price in L₀;
  - what it is meant to generate;
  - its kill condition.

  The owner chooses which card goes forward.
- **Stage 4 gates.**
  - Selectivity: the solution set is strictly smaller than the unconstrained space,
    and does not admit classical, quantum, and super-quantum structures
    indiscriminately.
  - Differentiation: a stable approximate partition Π and its T_Π are generated, not
    supplied.
  - Nonrelocation: neither Π nor T_Π is encoded in the inputs.
- **Stage 5.** 𝒦 forces ℛ(Π, T_Π, ε_R, Γ_Π) = 0, a measurable loss of freedom not
  independently imposed by existing frameworks; then a sealed holdout or experiment.
- **Stage 6.** The same 𝒦, unmodified, gives quantum, thermodynamic, and gravitational
  regimes. The same ε_R (same quotient, same distance) is exported to a gravitational
  ensemble, with local backreaction used as calibration only.
- **Not inputs to 𝒦:** memory, viscoelasticity, and crystalline order. Check for them
  as effective regimes after Stage 4.

## Blockers

None blocking.
- **"Owner decision pending: freeze T" is CLOSED** by rulings G2-01 … G2-08.
  - The two-tier T, the verdict logic and the stopping rule are in
    `PROGRAM/OWNER_RULING_R1_BOUNDARY.md`.
  - `grut2` is not merged into `main` until the R1 terminal.
- Open proof obligations, all Claude Code's:
  - M5: the theorem-grade BRI1 copula expansion;
  - the theorem-grade BRI1 rate for a bounded odd surrogate (`R1_T_LADDER.md` §8.1).

## Branch map (read-only references)

| Branch | Contents |
|---|---|
| `record-integration-01` | Consolidated frozen TestingGRUT record: `record/`, `registry/`, `governance/` |
| `bri1-manuscript` | BRI1 manuscript plus its byte-exact record |
| `ggc0-f0-program-consolidation-0` | The governing requirements map |
| `ggc0-f0-sd0-exec01-0` | SD0 execution (this branch's parent) |
| `main` @ `7baf2f1` | Untouched; no merge without owner approval |
