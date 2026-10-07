# R1 TERMINAL SYNTHESIS — the operational reciprocity observable · 2026-10-07

**Status: R1 TERMINAL SYNTHESIS — STOP FOR OWNER REVIEW** (ruling G2-10).
- No Stage-3 card is opened, frozen, scored or optimized before review.
- `grut2` is not merged into `main`.
- Every item carries its grade and its provenance:
  - **PRE-RESULT** means frozen at `82d311e`, before the WO-002 numbers were opened.
  - **POST-RESULT SYNTHESIS / STAGE-3 SEED** means not part of the frozen definition.
  - **D5 ANALYSIS** means derived during the comparator audit, evidence grade, not
    externally checked.

**Governing documents.**
- `R1_T_LADDER.md`: the definition and the theorems.
- `R1_DEFINITION.md`: v1.
- `WO-002/REPORT.md`, plus the independent cross-check in `xcheck/`.
- `D5_PREREGISTRATION.md` (committed at `891193a`, before the audit).
- `D5_COMPARATOR_AUDIT.md` and `D5_IDENTIFICATION.md`.
- `OWNER_RULINGS.md` (G2-01 … G2-10) and `OWNER_RULING_R1_BOUNDARY.md`.

---

## 1. Exact definition (PRE-RESULT)

**Data.**
- A finite set A of intervention protocols. Each prescribes, i.e. clamps, the system
  path.
- A finite observed time grid.
- For each protocol a, P_a: the law of the environment-force record Y_a ∈ ℝ^k. It is the
  full multi-time law.

**Interface class (frozen; two tiers).**
- **Tier 1: T_R1 = GL(k) with translations,** on the observed record. Independently
  calibrated nonlinearities and filters are removed with their known maps, not fitted.
  - Canonical reduction: centering and whitening, P ↦ P̃. This leaves an O(k)
    quotient.
  - Standing assumption: finite, nonsingular covariance. Otherwise work on the support
    subspace; the rank is an invariant.
- **Tier 2: T_mono = coordinatewise strictly monotone continuous bijections** of the
  margins' support intervals. The residual group is the coordinate reflections ℛ only,
  with no permutations across time coordinates.
  - Margins are continuous and atomless, with interval supports.
  - **T_mono is the declared top of R1. The ladder is closed** (G2-08, G2-10).

**Distance (frozen).**
- d_op is the bounded-Lipschitz quotient distance:
  - Tier 1: d_q^BL(P, Q) = min over O ∈ O(k) of d_BL(P̃, O#Q̃).
  - Tier 2: the same on normal-score (copula) laws, minimized over ℛ.
- Here d_BL(P, Q) = sup{ |E_P f − E_Q f| : ‖f‖_∞ ≤ 1, Lip f ≤ 1 }.
- Normalization: ‖f‖_BL = max(‖f‖_∞, Lip f). Dudley's β satisfies β ≤ d_BL ≤ 2β.

**The observable.**

  **ε_R^(T)(S:E) := inf over P★ of max over a ∈ A of d_op^T(P_a, T·P★).**

- It measures the **failure of protocol separability modulo a declared calibrated
  interface class**.
- ε_R^(T) = 0 if and only if the family is T-separable, i.e. some shared law P★ and some
  t_a ∈ T give P_a = t_a#P★ for every a (Theorems A, A-BL and M1).

**Derived constants.** For two protocols with P0 centrally symmetric:
- ε_R = ½·d_q exactly;
- the distance from P1 to the symmetric orbit is ≥ |E f_odd|/‖f‖_BL, with constant 1,
  sharp;
- hence ε_R ≥ ½·|E_{P1} f_odd|/‖f‖_BL (Theorem F).

**Verdict table** (PRE-RESULT; G2-08):

| Carrier | T-orbits | Verdict |
|---|---|---|
| PASS | different | **R1-PASS** |
| PASS | same | R1-NULL |
| UNRESOLVED | different | NO RECIPROCITY VERDICT |
| FAIL | different | MODE SELECTION (not reciprocity) |
| FAIL or UNRESOLVED | same | R1-NULL |

## 2. Identifying assumptions

**The common-carrier / readout certificate (PRE-RESULT form).**
- One latent-to-record map h is used for all protocols; there is no h_a. Then
  Y_a = t_a(h(Z)) with t_a ∈ T. The latent may have any dimension.
- Without a certificate the verdict is **NO RECIPROCITY VERDICT**.

**BRI1's certificate (PRE-RESULT, G2-08): PASS by construction.**
- The bath degrees of freedom, the Hamiltonian class, the Gibbs initial ensemble and the
  readout F = N_B^(−1/2)·Σ_j x_j(t) are the same for every protocol.
- Only the forcing changes.

**Standing regularity assumptions.**
- Nonsingular covariance (Tier 1).
- Continuous margins with interval supports (Tier 2).
- Calibrated interface maps applied exactly.

**POST-RESULT SYNTHESIS / STAGE-3 SEED.** These clarify the carrier; they do not change
it.
- The precise form: one fixed readout of the environment's **instantaneous** state on
  one time base.
- The 10-item certificate checklist in `R1_T_LADDER.md` §0.
- The measurement-invariance framing. D5 finds it RESTATED; credit it as **"an instance
  of measurement invariance (Mellenbergh 1989; Meredith 1993) with the intervention
  protocol as grouping variable,"** at the full distributional level, which is stronger
  than strict factorial invariance.

**D5 ANALYSIS (evidence grade; not externally checked).**
- **Theorem C1.** Among assumptions that restrict only the readouts, the common carrier
  modulo T_R1 is the **unique weakest** one under which ε_R^(T_R1) > 0 soundly implies
  "not exogenous". It is proved for affine readouts with environment laws that have
  densities, and for measurable readouts with finitely supported laws.
- **Tier-2 necessity is OPEN.**
- **Prop. C6.** An environment-side alternative — global central symmetry of the whole
  environment law, plus affine (or monotone∘affine) readouts — is incomparable with the
  carrier.
  - The disjunction "carrier OR global symmetry" is strictly weaker than the carrier.
  - It still certifies BRI1's Tier 1 and its Tier-2 odd channel.
  - **Only the Tier-2 even channel needs the carrier itself.**
- This is recorded for the owner. It is not a definition change.

## 3. No-go: non-identifiability (PRE-RESULT; Prop. E, §10 E1, G2-10 item 1)

**Statement.**
- If protocol-dependent readouts h_a are unrestricted — even **linear** ones — then
  every intervention family has an exact exogenous representation.
- Take Z = (Z_a)_a with independent coordinates Z_a ~ P_a, and h_a = the projection
  onto coordinate a. Then h_a#Law(Z) = P_a exactly.
- This holds for any index set, at path level, and for every d_op vanishing on equal
  laws.

**Consequence.**
- Explanations E-B (mode selection) and E-C (responding environment) have **identical
  observational images at every family**.
- So no record statistic separates them. Any level-α test of E-B has power ≤ α at every
  E-C alternative (D5 Corollary D1′).
- **Every R1 reciprocity claim is therefore conditional on an independently certified
  common carrier / readout class.**

**Causal version.** With **causal** linear readouts: {families with a causal linear
representation} = {non-anticipating families} = grid-level E_univ (D5 Theorem D2).

**Which state is "the environment" must be declared.**
- BRI1 itself has an exact E-B representation with the *initial* bath state as the
  latent (BRI-UPPER).
- It has an exact E-C representation with the *instantaneous* state (D5 Remark D3).

**Not new mathematics.** This is an instance of:
- response-function / potential-outcome representations (Balke–Pearl 1994; Pearl
  2009);
- Kallenberg's randomization and transfer theorems;
- PJS Prop. 4.1;
- BRI0's E_univ.

R1's only specialization is that the readouts may be linear.

## 4. Tier 1 result — calibrated-readout reciprocity: BRI1 R1-PASS (DERIVED; owner-banked; SCOREBOARD #10)

**Theorem C.**
- P0 (undriven) is exactly centrally symmetric.
- An injective linear interface cannot create an odd cumulant.
- κ₃(F_{P1}(t*)) ≠ 0 for N_B ≥ N₀(t*), under BRI1's quantifiers ∃δ ∀t* ∈ (0, δ)
  ∃N₀(t*) ∀N_B ≥ N₀(t*).
- So X1 = {P0, P1} is not T_R1-separable, and the carrier is PASS.

**Rate (Prop. G, DERIVED; pending external check).**
- liminf N_B·ε_R^(T_R1) ≥ |K(t*,t*,t*)|·V*/(12·m₂^(3/2)), with V* = 0.943578.
- Source: Barbour 1986, with uniformity over the triangular array proved.
- The bound transfers to any grid containing t*.
- **D5 evidence:** the bound appears asymptotically sharp at k = 1,
  ε_R = (V*/12)·|γ₁|·(1 + 0.235/N_B + …).

**Regime restatement (D5, recorded honestly).**
- K is a classical Kubo/FDT third-cumulant response, fixed by P0's connected 4-point
  function.
- So BRI1's Tier-1 single-time calibration value is standard physics, read through
  R1's quotient.

## 5. Tier 2 result — readout-robust reciprocity: BRI1 R1-PASS at EVIDENCE GRADE (SCOREBOARD #11)

**Exact theory (DERIVED).**
- **M1:** ε_R^(T_mono) = 0 if and only if all protocols' copulas lie in one
  reflection orbit.
- **M2:** a radially symmetric C₀ and a radially asymmetric C₁ give ε_R > 0.
- **M3:** the Gaussian tangent structure; rank J = k, leaving C(k+2, 3) − k leading
  third-order directions.

**WO-002** (preregistered outcome 1; checked: Claude, `cb81a3b`).
- **Odd channel.** 7/7 off-diagonal A_abc are nonzero, at ≥ 2×10⁶ × the quadrature
  spread, for P1 and P2.
- **Even channel.** 3/3 normal-score Δρ are nonzero, at ≥ 3×10⁶ × the spread.
- They scale as 1/N_B.
- An independent re-implementation agrees to ≤ 2×10⁻¹⁴.

**Grading.**
- **The odd channel is a dual-branch escape:** against T_lin (Theorem C) and against
  T_mono (M2), separately.
- **The even channel is a T_mono-only escape:** linear time-mixing absorbs correlation
  change. Per D5 C6, it is also the only channel that needs the carrier itself.

## 6. Evidence grade vs theorem grade

| Claim | Grade |
|---|---|
| ε_R definition; Theorems A, A-BL, C, F; M1, M2, M3; Prop. E / E1; E2 | DERIVED (A-BL, F, M1–M3: v3/v3.1, external check pending) |
| BRI1 Tier 1 R1-PASS | DERIVED (BRI1 quantifiers), owner-banked |
| Prop. G (Tier-1 rate) | DERIVED; external check pending |
| Prop. G sharpness at k = 1 | D5 evidence only |
| BRI1 Tier 2 R1-PASS | **EVIDENCE GRADE**: formal leading order, numerically cross-checked |
| Tier 2 theorem grade | **OPEN — M5** (§10) |
| D5 C1–C6, D1–D3 | D5 ANALYSIS: evidence grade, not externally checked |

## 7. Portability limits

1. **The identification is conditional and cannot be tested from records.** The
   carrier certificate must come from outside the records: calibration and physics
   (§3). It must also declare which state variable counts as the environment.
2. **Calibration burden.** Tier 1's power to discriminate back-reaction rests entirely
   on independent interface calibration. An uncalibrated nonlinear detector fires
   Tier 1 on an exogenous environment. The post-result checklist lists the apparatus
   mechanisms a certificate must exclude:
   - protocol-dependent readout noise;
   - gain jitter;
   - trigger and clock jitter;
   - outcome-dependent vetoes;
   - non-invertible saturation;
   - actuator cross-talk.
3. **Narrow by design: R1-NULL does not mean "no response".**
   - ε_R annihilates every T-explainable response: mean response of every order,
     linear back-reaction, and affine or Gaussian latent change.
   - The harmonic bath responds (friction) and is R1-NULL.
   - R1-PASS is a one-sided, quotiented certificate of a total causal effect.
4. **Estimation (D4 OPEN).**
   - BRI1's single-time witness at N_B = 4 needs about 10¹¹ samples.
   - d_q^BL is not weakly continuous in the raw laws, because whitening uses second
     moments.
   - Plug-in d_BL converges as n^(−1/k) for k ≥ 3, so use the per-witness form.
5. **Scope of the calibration.** The calibration is one supplied model environment: the
   finite Duffing bath, on the frozen grid and protocols. Nothing is claimed for other
   environments.
6. **Control coverage (D5 erratum).**
   - C2-F is colored (exact AR(1)), not non-Markovian.
   - D1 is a theorem with no Markov assumption, but no genuinely non-Markov record
     control has been run. C2-F′ is proposed.

## 8. Common-carrier requirement (summary)

- **Required for every R1-PASS:** a certified common readout of the environment's
  declared state, with the same channel, weights, time base and grid for every
  protocol, and calibrated interfaces removed by their known maps.
- **Unavoidable in kind.** By §3, some assumption from outside the records is needed.
- **Minimal among readout-only assumptions at Tier 1** (D5 C1, evidence grade).
- **Not the only route** for the odd channel (D5 C6). It is needed for the Tier-2 even
  channel.

## 9. No claim about the join

- **No claim is made** about the group generated by T_lin and T_mono, i.e. compositions
  of linear time-mixing and per-time nonlinearities.
- It is expected, but not proved, to trivialize ε_R.
- Tier 2 escapes are relative to T_mono alone. The odd channel's dual-branch escape
  holds against each class **separately**.

## 10. M5 status and open items

**M5 — OPEN.** A uniform multivariate Edgeworth (Cramér-type) expansion in normal-score
coordinates for BRI1's triangular array. It would upgrade Tier 2 to theorem grade.
- Barbour 1986 and Lemma A do not apply: normal scores are law-dependent nonlinear
  transforms.
- M5 does not alter the banked evidence-grade result unless it uncovers a contradiction
  (G2-10).

**Other open items.**
- Tier-2 necessity of the carrier (D5).
- D4: a finite-sample test of ε_R = 0.
- Trivialization of the join (expected).
- The external check of A-BL, F, M1–M3, Prop. G and the D5 analysis.

## 11. D5 verdict (governing audit; preregistered categories)

**Verdict.**
- **(M) Mathematics: STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION.**
- **(P) Physical interpretation / identification rule: STANDARD MATHEMATICS, NEW
  OPERATIONAL DEFINITION.**
- This was the preregistered expectation, recorded in advance as acceptable.

**Per comparator.** All 10 comparators come out MID/MID:
- generic nonlinear response;
- non-Markovianity;
- process tensors;
- ICP;
- ICM;
- Janzing–Schölkopf;
- MDL;
- Blackwell–Le Cam;
- measurement invariance;
- ε-transducers.

**Robustness.**
- No skeptic's RESTATED case succeeded.
- **DISTINCTIVE was not awarded:** no candidate relation survives every comparator.

**Kill condition (STATE.md): does not fire.**
- ε_R ≡ 0 on single-protocol families, and all four cells of (Markov or not) × (ε_R zero
  or not) are occupied.
- Mean and linear responses give ε_R = 0, and E2 gives ε_R > 0 with no response.
- The zero set is nontrivial.
- Identification is conditional within the frozen scope.

**Answers.**
- **A.** No: ε_R is not a renamed response or process-distance quantity. The
  qualifications are recorded (FDT regime restatement; signalling-distance core;
  invariant-OT instance).
- **B.** Yes: the quotient is known mathematics, and the identification rule is new
  only operationally.
- **C.** Yes, in a qualified sense (§2, §8).
- **D.** Yes (§3).

**Post-result items.**
- Z_A is **RESTATED** by ε-transducer causal states restricted to a repertoire.
- The measurement-invariance framing is **RESTATED** by measurement invariance.
- [h]_T is **known in nearby form** (Stevens scale types + MI; IRT linking; the
  interventional-CRL identifiability class). It is not adjudicable as RESTATED, because
  it has no frozen definition.

**Not R1's own:** any new mathematics; any new physical relation, constraint or
prediction.

**Its own:** one physical observable assembled from standard parts, with an explicit
identifying assumption and a verdict table, calibrated on one known environment.

## 12. What Stage 3 must derive rather than assume

R1 supplies the observable a law must explain. A 𝒦 card must **derive**, not supply, the
following:

1. **The environmental identity: the carrier and its readout class [h]_T.** This means
   which state variable is "the environment" across interventions, and why one readout
   class is common. Remark D3 shows the B/C label depends on it. Any novelty claim for
   [h]_T must be positioned against IRT linking, Stevens scale types and interventional
   CRL classes (D5 comparators 5 and 9).
2. **The interface class.** T_Π should be generated by 𝒦's differentiation (Stage 4),
   not declared. R1 used a declared T; this is the supplied-T versus generated-T_Π
   tension, and Stage 3 must resolve it.
3. **ε_R values, not just ε_R > 0.**
   - BRI1's Tier-1 value is already predicted by Kubo/FDT from equilibrium
     correlations.
   - So a 𝒦 card earns credit only for a relation that standard response theory does
     **not** supply: for example, a forced relation between ε_R and other sectors
     (CROSS-SECTOR), or a prediction for an environment where FDT is silent.
4. **Why the null is conservative.** R1 deliberately discards T-explainable
   (linear/Gaussian) response. A law should say whether reciprocity lives in that
   quotient-irreducible part or not.
5. **Not to be assumed in Stage 3:**
   - the carrier;
   - the instantaneous-state choice;
   - the calibration of T;
   - the Gibbs/FDT structure of the environment.

   Each was an input to R1's calibration.

---

**STOP — R1 terminal synthesis submitted for owner review** (G2-10). No Stage-3 card,
no merge, and no change to WO-002 or the frozen definition.
