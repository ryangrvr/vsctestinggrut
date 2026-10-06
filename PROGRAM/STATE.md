# STATE

**Updated:** 2026-10-06 · **Branch:** `grut2` (forked from the SD0 execution tip
`a25d1be`, so the full F0 record is in the tree).

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

**Stage 2 progress (2026-10-06).**
- **R1 definition v1 (E₂±):** `PROGRAM/RESULTS/R1/R1_DEFINITION.md`.
- **v2 interface ladder:** `R1_T_LADDER.md`.
  - BRI1 escapes every linear interface class, causal or not, at the path level too.
  - Per-time nonlinear interfaces absorb it at a single time.
  - The multi-time case is OPEN (WO-002).
  - Unrestricted T makes R1 trivial.
- **WO-001 (VS Code):** C1 ACCEPTED. C2 numbers reproduced, with process cleanup
  pending (Amendment A). Next are C3, then C4.
- **WO-002 (VS Code):** BRI1's multi-time leading-order channels under T_mono. OPEN.
- **Identifiability flag:** BRI1's witness at these parameters needs about 10¹¹ samples
  (Review 2).

## Stage definitions 3–6 (pointer)

- **Stage 3.** Ξ ≠ Γ, with Γ_Π = Obs_Π(Ξ). At most three 𝒦 cards. Each card states:
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

**Owner decision pending: freeze T for R1** (`R1_T_LADDER.md` §6).
- Recommended: protocol-dependent linear interfaces, with independently calibrated
  nonlinearities inverted, not fitted.
- This does not block WO-001 C3/C4 or WO-002.

## Branch map (read-only references)

| Branch | Contents |
|---|---|
| `record-integration-01` | Consolidated frozen TestingGRUT record: `record/`, `registry/`, `governance/` |
| `bri1-manuscript` | BRI1 manuscript plus its byte-exact record |
| `ggc0-f0-program-consolidation-0` | The governing requirements map |
| `ggc0-f0-sd0-exec01-0` | SD0 execution (this branch's parent) |
| `main` @ `7baf2f1` | Untouched; no merge without owner approval |
