# R1 — THE OPERATIONAL RECIPROCITY OBJECT ε_R: WORKING NOTES 01

**DRAFT — pending Claude Code review.** The T-hierarchy (T₀–T₃) and the distance choice
are **definition decisions owned by Claude Code** under PROGRAM/DIVISION_OF_LABOR.md;
they are recorded here as a proposal only. All proof-shaped statements (in particular the
BRI1-as-special-case embedding) are claimed by this file only as items to be verified;
see the explicit unverified-claims flags below.
**Stage 2 · prove or kill.** Definition (STATE.md, verbatim):

```
ε_R^(T)(S:E) = inf over P★ and {t_a ∈ T} of max_a d_op(P_a, (t_a)#P★)
```

- `P_a` is the full intervention-conditioned multi-time process law (the process for
  intervention settings `a`, including temporal order, environment state, and all
  higher-time correlations).
- `T` is the maximal independently calibrated, environment-preserving interface class:
  **frozen before testing**, closed under composition, with no unrestricted per-protocol
  maps.
- `(t_a)#P★` is the pullback of a shared "clean" process P★ through the calibrated
  transformations t_a (one per protocol a).
- `d_op` is the operational distance on process laws (to be fixed as part of the object,
  priced).
- ε_R = 0 means: every protocol's full conditional process law is the calibrated
  transformation of one shared process — the *only* asymmetry between protocols is the
  independently calibrated interface. ε_R > 0 isolates genuine protocol-relative physical
  content.

## 1. What R1 must earn (deliverables, from STATE.md)

1. **ε_R = 0 for every exogenous process whose protocol dependence factors through T**
   (including colored and non-Markovian noise) — i.e. the vanishing class is nontrivial
   and noise-robust.
2. **BRI1 as a special case:** signed-affine T; skewness is one witness; scaling ∝ 1/N_B.
   (BRI1 = backreaction identifiability: a finite Duffing bath escapes the shared
   signed-affine class E₂±; record on `bri1-manuscript` @ `92dc6bb`.)
3. **Invariance** on equivalence classes, and behavior under legitimate coarse-graining.
4. **Identifiability from finite intervention data.**
5. **Comparator audit:** non-Markovianity measures; generic nonlinear response;
   Janzing–Schölkopf; independent causal mechanisms; MDL causal discovery; invariant
   causal prediction; Blackwell–Le Cam deficiency; process tensors.

**Kill condition:** R1 is killed only if ε_R is trivial (always 0 or always ∞),
unidentifiable, or reduces to non-Markovianity / generic nonlinear response. ε_R is an
*observable*, not the law — overlap with known machinery is acceptable here (but must be
priced and recorded).

## 2. Design decisions to fix first (frozen before testing)

### 2.1 The process-law object

Take a finite setting: interventions `a ∈ A` (discrete settings), a state space for the
environment, and a multi-time process law = the joint distribution over
(intervention outcomes, environment trajectory) conditioned on the setting:

```
P_a(outcomes_1..n, env trajectory | setting a)
```

For the first finite model: discrete time, finite state space E (the "environment" /
bath), finite system S, interventions as stochastic matrices on S together with
environment coupling operations.

### 2.2 The interface class T (frozen before testing)

Requirements: independently calibrated (each t_a is measurable/known from calibration
experiments *before* the protocol is run); environment-preserving (t_a acts on the
environment/process side, not introducing uncontrolled new degrees of freedom); closed
under composition; no unrestricted per-protocol maps (this is what would trivialize ε_R —
if T contains arbitrary per-protocol process maps, any P_a can be pulled back to any P★).

Candidate T hierarchy (to be tested):
- **T₀ = {id}**: the trivial interface; ε_R^{T₀} measures raw process inequality.
- **T₁ = signed-affine maps on the environment response** (the BRI1 class; skewness
  witness; ∝ 1/N_B scaling).
- **T₂ = all invertible affine maps on the environment response** (larger, still
  calibrated).
- **T₃ = all invertible maps on the environment's operation statistics** — check whether
  this already trivializes; if yes, the maximal T is smaller and the boundary is itself a
  finding.

### 2.3 The distance d_op

Candidate: total variation distance on the joint outcome distributions (finite setting);
alternatively an operational distinguishability (multiple statistical tests, trace
distance analogue). TV on the full joint law is the most conservative and clearly
operational: two processes are ε-close iff every measurement statistics differ by ≤ ε.

### 2.4 P★ and the infimum

P★ ranges over all process laws of the same type; the inf over (P★, {t_a}) makes ε_R a
projection distance: how close the protocol-conditional family {P_a} is to the orbit of a
single process under T.

## 3. Deliverable 2 check — BRI1 embedding

BRI1's statement: for a finite Duffing bath, backreaction (the protocol-conditioned
difference) is *identifiable* — it does not vanish within the signed-affine class E₂±.
In R1 terms: there is a protocol family whose ε_R^{T₁} > 0 but ε_R^{T₂} = 0 (or whose
scaling with bath size N_B is the BRI1 ∝ 1/N_B witness). **UNVERIFIED — flagged.** BRI1's theorem, quantifiers and the frozen bath belong to the
record (`bri1-manuscript` @ `92dc6bb`); the embedding argument is Claude Code's proof
deliverable, not mine (WO-001: "Do not restate BRI1's theorem"). What I will compute:
the skewness-witness lower bound along the N_B ladder and its scaling. Precisely: pull the
BRI1 construction from `bri1-manuscript` @ `92dc6bb` and translate: the two Duffing bath
states ↔ two protocols a; the signed-affine class ↔ T₁; the "analytic escape" ↔ the
positive lower bound on d_op.**

## 4. Deliverable 5 — comparator audit table (to fill as the work proceeds)

| comparator | what it measures | relation to ε_R | verdict slot |
|---|---|---|---|
| non-Markovianity measures (LP, BLP) | deviation of intermediate dynamics from CP-divisibility | orthogonal axis: Markovian processes can still have protocol dependence | TBD |
| generic nonlinear response | response functions of a fixed dynamics | ε_R compares across *protocols*, not orders of response | TBD |
| Janzing–Schölkopf / independent causal mechanisms | mechanism independence across contexts | closest relative: ε_R = 0 says mechanisms are T-calibrated across protocols | TBD |
| invariant causal prediction | invariance of conditional laws across environments | ε_R = 0 is a *quantitative* version with calibrated maps; ICP is accept/reject | TBD |
| MDL causal discovery | compression of mechanism descriptions | priced cousin; ε_R is a distance not a codelength | TBD |
| Blackwell–Le Cam deficiency | comparability of experiments (existence of a Markov kernel making one experiment simulate another) | **structurally closest**: (t_a)#P★ = P_a with a single kernel class T; ε_R is a quantitative deficiency when exact simulation fails | TBD |
| process tensors / multi-time operational formalism | the object P_a lives in this framework | framework, not a measure | TBD |

**Key early observation (to develop):** Blackwell–Le Cam deficiency / *comparability of
experiments* is the exact qualitative skeleton of ε_R — (t)#P is the "simulate P via
randomization t" construction, and ε_R^{T} = 0 iff all P_a are in the T-orbit of one
process (exact mutual simulability). The R1 content beyond BL is: (i) the *restriction of
the kernel class to independently calibrated, environment-preserving T* (BL allows arbitrary
kernels; that freedom is what would trivialize the comparison), (ii) the *quantitative*
distance when exact simulation fails, (iii) the multi-protocol (n > 2) simultaneous
version, (iv) the physics identification: T = calibrated interface = "what a protocol
change is allowed to do to the environment record." This is the comparator-audit crux and
must be priced, not hidden.

## 5. Finite pilot model (to implement next)

- Bath: N two-level systems (or a Duffing-type continuous model reduced to a response
  functional), initial state ρ_B.
- System: qubit, protocol a ∈ {weak, strong} measurement settings.
- Process law P_a: joint distribution of (system outcomes over k rounds, bath final
  coarse observable).
- Interface classes: T₀ = {id}; T₁ = signed-affine on the bath record distribution;
  T₂ = invertible affine; T₃ = invertible maps on the record.
- Compute ε_R^{T_i} exactly (finite distributions) for the standard protocol pair and
  check: ε_R^{T₁} > 0 for a genuinely backreacting bath; scaling with N_B; and whether
  T₃ collapses ε_R to 0 (boundary-of-maximal-T finding).

## 6. Status

Design fixed (frozen before testing): P_a = full conditional joint law; T-hierarchy
T₀ ⊂ T₁ ⊂ T₂ ⊂ T₃ with T₁ = signed-affine (BRI1 class); d_op = TV on the joint law.
Next: implement the pilot, compute ε_R^{T_i}, verify deliverable 1 (vanishing class) and
deliverable 2 (BRI1 embedding), then invariance/identifiability, then the audit.
