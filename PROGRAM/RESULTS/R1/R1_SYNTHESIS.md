# R1 SYNTHESIS — the operational reciprocity observable (Claude Code) · 2026-10-07

**Status:** DRAFT for the R1 terminal. The structure is required by ruling G2-09
item 3.
- §5 (D5) is filled in from the comparator audit, `D5_COMPARATOR_AUDIT.md`.
- Every claim cites the governing note and its CHECKS status.
- Nothing here is new beyond `R1_T_LADDER.md` v3.1, `R1_DEFINITION.md` and the WO-001
  / WO-002 results. This is the synthesis, not a new derivation.

---

## 1. The observable: failure of protocol separability modulo a declared interface class

**Data.**
- A finite set A of intervention protocols. Each prescribes the system path, which is
  clamped.
- For each protocol a, a finite observed time grid and P_a, the law of the
  environment-force record Y_a ∈ ℝ^k under that protocol. It is the full multi-time
  law.

**Interface class.**
- T is declared and calibrated in advance. It contains the transformations of the
  readout that are explained by the interface, not by the environment.
- Frozen (rulings G2-01 … G2-08):
  - **Tier 1, T_R1** = GL(k) with translations, on the observed record. Independently
    calibrated nonlinearities are removed by their known maps, not fitted.
  - **Tier 2, T_mono** = coordinatewise strictly monotone maps, with residual group the
    coordinate reflections. This is the declared top of R1.

**Protocol separability modulo T.** The family {P_a} is *T-separable* if there are one
shared law P★ and maps t_a ∈ T with P_a = t_a#P★ for every a.

**The observable.**

  **ε_R^(T)(S:E) := inf over P★ of max over a ∈ A of d_op^T(P_a, T·P★).**

- d_op^T is the T-adapted quotient distance.
  - For Tier 1 it is the bounded-Lipschitz distance between centred and whitened laws,
    minimized over O(k) (`R1_T_LADDER.md` §0, §8).
  - For Tier 2 it is the bounded-Lipschitz distance between normal-score (copula) laws,
    minimized over reflections (§9).
- **ε_R^(T) = 0 if and only if the family is T-separable** (Theorems A, A-BL and M1).
- ε_R > 0 is the operational statement: no single environment law, read through
  interface maps in T, reproduces every protocol's record.

**Constants** (`R1_T_LADDER.md` §8, Theorem F; checked in `82d311e`).
- For any odd bounded-Lipschitz witness f: the distance from the driven law to the
  symmetric null orbit is ≥ |E f|/‖f‖_BL, with constant 1, sharp.
- For two protocols, ε_R = ½·d_q exactly, so ε_R ≥ ½·|E_{P1} f|/‖f‖_BL.
- Normalization: ‖f‖_BL = max(‖f‖_∞, Lip f).

**What ε_R is not.** It is an observable, not a law. It measures a failure of
separability; it does not by itself say why separability fails. That is §2–§3.

## 2. The identification limit

**Statement** (`R1_T_LADDER.md` §10 E1; Prop. E; checked in `82d311e`).
- Suppose protocol-dependent readouts h_a are allowed without restriction, even
  **linear** maps from a latent environment of unrestricted dimension.
- Then **every** intervention family admits an exact exogenous representation:
  - take Z with independent coordinates Z_a ~ P_a;
  - take h_a := the projection onto coordinate a;
  - then h_a#Law(Z) = P_a exactly.
- On BRI0's admissible (non-anticipating) domain, the zero set is exactly grid-level
  E_univ. A causal version uses 0/1 selections from a latent indexed by the protocols'
  prefix tree.

**Consequence.**
- **From the records alone, reciprocity (a responding environment, C) is not
  identifiable against protocol-dependent mode selection (B).**
- Any family of records, however asymmetric, is consistent with an unchanged
  environment read through protocol-dependent channels.
- Example (E2): a symmetric mode S read alone versus S + U read together reproduces
  BRI1's "symmetric reference, skewed driven" signature with no back-reaction.

**Closest established results** are named in D5 (§5): universal exogenous /
functional-causal-model representations and latent-variable non-identifiability. The
R1 statement is an instance of that general fact, specialized to interface classes. It
is not claimed as new.

## 3. Conditional inference: what an R1-PASS requires

**Two independent conditions** (ruling G2-08, verdict table in `R1_T_LADDER.md` §0).

**(a) Carrier / readout invariance, established independently of the records.**
- **Common carrier:** one fixed readout channel h, applied to the environment's
  **instantaneous** state on one time base, for every protocol. A calibrated fixed
  filter of it also counts.
- This is the dynamical analog of **measurement invariance**: the same construct is
  measured by the same instrument across groups (here, protocols). Without it, a
  difference between groups cannot be attributed to the construct. D5 records the
  precise correspondence and its limits.
- **The mode-stability certificate** must cover the ten applicability items:
  1. the interface is deterministic, invertible and calibrated, within a curvature
     tolerance;
  2. readout noise is calibrated and protocol-independent;
  3. there are no random gains;
  4. there is one time base, grid and trigger phase;
  5. there is one channel with fixed weights;
  6. the record is complete;
  7. there is no outcome-dependent selection;
  8. nonlinearities are invertible only;
  9. there is no actuator–environment cross-talk;
  10. estimation is controlled.

**(b) Quotient separation.** ε_R^(T) > 0, i.e. the protocols lie in different T-orbits.

**Verdicts.**

| Carrier | T-orbits | Verdict |
|---|---|---|
| PASS | different | **R1-PASS** |
| PASS | same | R1-NULL |
| UNRESOLVED | different | NO RECIPROCITY VERDICT |
| FAIL | different | MODE SELECTION (not reciprocity) |
| FAIL or UNRESOLVED | same | R1-NULL |

**What C is separated from.**
- **From A (calibrated interface):** by the quotient. Any T-explained difference gives
  ε_R = 0.
- **From B (mode selection):** only by the certificate. By §2, no statistic of the
  records can do it.

## 4. The BRI1 calibration: tiers and grades

**Model.** A finite Duffing bath of N_B clamped oscillators (H₀ = p²/2 + x²/2 + x⁴/4,
Gibbs initial ensemble). The force record is F = N_B^(−1/2)·Σ_j x_j(t). There are three
protocols:
- P0, undriven: the force law is exactly centrally symmetric;
- P1 and P2, the frozen drives.

Record: `bri1-manuscript` @ `92dc6bb`.

**Carrier certificate: PASS by construction.** The bath degrees of freedom, Hamiltonian
class, equilibrium ensemble and readout are the same for every protocol; only the
forcing changes (`OWNER_RULING_R1_BOUNDARY.md`).

| Tier | Class | BRI1 X1 | Grade | Scoreboard |
|---|---|---|---|---|
| — | E₂± (BRI1's own class) | escapes; witness O(1/N_B) | DERIVED (BRI1 theorem, quantifiers ∃δ ∀t∈(0,δ) ∃N₀(t) ∀N_B ≥ N₀(t)) | #1 |
| **1** | T_R1 = GL(k) + common carrier | **R1-PASS** (Theorem C: symmetric P0; injective linear maps cannot create odd cumulants) | DERIVED, owner-banked | #10 |
| **2** | T_mono (copula modulo reflections) | **R1-PASS** — odd channel (7/7 A_abc ≠ 0) is a dual-branch escape (T_lin and T_mono separately); even channel (3/3 Δρ ≠ 0) is T_mono-only; invariants scale as 1/N_B | **Evidence grade** (formal leading order, numerically cross-checked). Theorem grade pending M5. No claim about the join of T_lin and T_mono | #11 |
| — | single time under T_mono | absorbed (ε_R = 0) | DERIVED (D1) | — |
| — | unrestricted / protocol-dependent carriers | everything absorbed | DERIVED (Prop. E, E1) | GRAVEYARD |

**Zero-side calibration** (exogenous controls give ε_R = 0 where they should).
- C2-G: Gaussian colored noise.
- C2-NG: an affine-entry exact control.
- C2-F: protocol-dependent calibrated filters of a shared skewed driver. It is nonzero
  under E₂±, the correct value for that class, and **0 under T_lin**.
- The harmonic bath gives K ≡ 0 and C2 ≡ 0. The escape is carried entirely by the bath
  nonlinearity.

**Identifiability (D4, C4: laboratory preparation; not an exit-gate item).** At BRI1's
parameters (t* = 0.5, N_B = 4) the single-time witness is about 5×10⁻⁶. Resolving it
needs about 10¹¹ samples.

**Bounded-Lipschitz rate (Prop. G, DERIVED; `R1_T_LADDER.md` §8.1).**
- Under BRI1's quantifiers, plus a new threshold N₁(t*, f):
  liminf N_B·ε_R^(T_R1) ≥ |K(t*,t*,t*)|·V*/(12·m₂^(3/2)), with V* = 0.943578.
- Source: Barbour (1986) smooth-function expansion, with no Cramér condition, plus
  uniformity over the triangular array.
- The bound transfers to any grid containing t*.

**Open proof obligation (rigour; not an exit-gate item unless the owner rules
otherwise).** M5: a uniform multivariate Edgeworth expansion in normal-score
coordinates, which would make Tier 2 a theorem.

## 5. Comparator audit (D5)

*Filled in from `D5_COMPARATOR_AUDIT.md`.*

## 6. What R1 hands to Stage 3

- **A defensible operational object.** ε_R^(T) has a frozen T, a frozen d_op with
  derived constants, a stated identification limit, and a conditional-inference rule.
- **A calibration.** One known physical environment, the BRI1 bath, passes Tier 1
  (DERIVED) and Tier 2 (evidence grade) under a certified common carrier.
- **The environmental-identity requirement** (NORTH_STAR, G2-02 item 6).
  - "Environment responds" is meaningful only relative to a specified environmental
    identity across interventions.
  - Stage 3 should aim to **derive an objective equivalence class of readouts, [h]_T**,
    rather than a unique formula: 𝒦 → stable subsystem identity → stable interface
    carrier → T → ε_R.
- **Honest scope.** This is not new fundamental physics. It is the observable that a
  reciprocity law would have to predict.
