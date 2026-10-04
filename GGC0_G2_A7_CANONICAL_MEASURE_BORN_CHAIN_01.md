# GGC0 G2 A-7 CANONICAL MEASURE–BORN CHAIN 01
## Executed under `GGC0_G2_A7_CANONICAL_MEASURE_BORN_CHAIN_CHARTER_01.md` (frozen `1756e0c`, authorized by Owner Ruling 03 `346302e`)

**Sole target:** A-7. **Chain:** `F → μ_F → h_F → (h_F)_*μ_F → |α_i|²`,
audited arrow-by-arrow. **Condition-before-consequence ordering enforced:**
each route states its structural condition and its independent motivation
*before* any Born-consequence analysis. q-control genuinely hostile.
State-dependence attack mandatory. Exactly one label per route. No
retroactive relabeling of C1–C5 (untouched).

---

## Route S1 — Equivariance + locality/functional restriction

### 0. Frozen structural condition (stated before any Born analysis)

**Property imposed:** the ensemble distribution over Γ-space configurations
is *equivariant* under the Γ-dynamics — i.e., if ρ_t is the ensemble density
at time t, then the density propagated by the flow's transfer operator maps
solutions to solutions: ρ₀ equivariant ⇒ ρ_t stays in the admissible class.

**Why independently motivated:** equivariance is the requirement that the
statistical description be preserved by the dynamics — a
consistency-of-description condition, not a probability postulate. It is
the same kind of requirement as "the law is time-translation invariant":
imposing it does not presuppose any particular target measure. For a
*different* dynamics, the unique equivariant measure (if one exists) would
be different.

**Mathematical class defined:** admissible densities = local functionals of
the hierarchy data (the Γ^(n) generators and the accessible field), within
the declared functional/locality class of the influence hierarchy.

### Arrow A (F → μ_F)

- **Existence:** the Γ-space flow is *not* an established object in the
  record. The Level-0/SCOUT-era constructions define dynamics on accessible
  configurations with influence data as *parameters* of kernels, not as a
  state space with its own flow. No Liouville-type equation on Γ-space is
  on record. Existence of an invariant measure is therefore not
  established — not because it fails, but because the flow it would be
  invariant under is undefined at the required level.
- **Invariance:** undefined for the same reason.
- **Uniqueness:** cannot be assessed without the flow and the admissible
  density class. The Bohmian precedent (Goldstein–Struyve) shows uniqueness
  theorems of this type exist in a *different* structure (configuration
  space + Schrödinger-induced velocity field); transferability to Γ-space
  is not established and is explicitly forbidden as import.
- **Physical selection:** not established.
- **State dependence:** even if a unique equivariant density existed, the
  record contains no argument that it would depend on the initial quantum
  state in the required way (see Arrow D).

**Arrow A: UNRESOLVED** — the required objects (Γ-space flow, admissible
density class with a Liouville-type equation) are not defined on the record.
Per charter §6: "If the Γ-space flow or measure class has never been
derived, do not invent one to complete the proof."

### Arrow B (μ_F → h_F) — mooted by Arrow A (no μ_F to push). Formally UNRESOLVED.

### Arrow C — mooted. UNRESOLVED.

### Arrow D — mooted at this route's stage. UNRESOLVED.

### q-control

Cannot be run: no induced measure exists to test against the q-family. The
control's purpose (identify what excludes q≠2) is unachievable at this
stage. Recorded as NOT REACHED.

### State-dependence

Structural observation, recorded without deciding: a unique equivariant
measure of a *fixed* flow is state-independent by construction; for it to
encode Born weights, the state must be an argument of the flow itself (i.e.,
different ψ ⇒ different Γ-dynamics). The record's F[Γ, Φ, access, state]
form does allow ψ-dependence of F, so this is not automatically fatal — but
then equivariance-within-one-flow is the wrong uniqueness condition; one
would need uniqueness of the map ψ ↦ μ within a *family* of flows, which is
a different and stronger theorem never established here. **This is the
audit-predicted structural wall; it is recorded as an open difficulty, not
assumed fatal.**

### Hostile baseline

Nearest: Bohmian equivariance (hostile comparator only — not importable);
quantum trajectories (different structure: noise inserted, not selected).

### M-table

| Gate | Result | Reason |
|---|---|---|
| M1 | UNRESOLVED | F-class on Γ not defined at flow level on the record |
| M2 | UNRESOLVED | no flow ⇒ no invariant-measure question decidability |
| M3 | UNRESOLVED | h_F not derivable without the flow |
| M4 | UNRESOLVED | pushforward undefined |
| M5 | UNRESOLVED | cannot audit smuggling into undefined objects |

**GGC0-P: UNRESOLVED** (formulation on Γ intended, but the required
mathematical objects do not exist on the record). **GGC0-R: UNRESOLVED** (no
relation derivable).

### Route label: **UNRESOLVED**

(The chain fails for lack of established objects, not because a condition
was shown to select the wrong thing. STRUCTURAL-FAIL would assert the
condition does not select the required object — not shown. The honest
status is undecidable on the record without inventing new structure, which
the charter forbids.)

---

## Route S2 — Physical/SRB-type global measure

### 0. Frozen structural condition

**Property imposed:** the Γ-dynamics is such that a *global* physical
measure μ_phys exists — distinguished by time-average convergence for a
positive/full-measure set of initial conditions, defined across the entire
Γ-space (not per-attractor).

**Why independently motivated:** physicality is the standard
mathematical-physics criterion for "the statistics actually realized by
typical initial conditions." It is motivated without reference to Born
weights or outcomes.

**Mathematical class:** smooth deterministic flows on the Γ-state space
with attractor structure, satisfying the hypotheses of SRB-type theorems
(where they apply).

### Arrow A (F → μ_F)

- **Existence/invariance/uniqueness/physical selection:** for systems
  satisfying hyperbolicity-type hypotheses, SRB measures exist and are
  physically selected *within one attractor's basin*. This is established
  mathematics — but at the wrong granularity for outcomes (see below).
- **The global problem (charter §4-S2):** separate SRB measures on separate
  outcome attractors do not determine *relative* basin-entry probabilities.
  A global measure that weights the basins is required, and SRB theory does
  not supply one: the physical-measure machinery is per-basin.
- **Does the dynamics itself fix the weighting between outcome basins?**
  Only if the Γ-flow has a single global physical measure whose restriction
  to each basin is the basin's SRB measure AND whose inter-basin weights are
  dynamically determined. Such "global physical measures" exist in some
  classes (e.g., certain maps with a single attractor filling the space),
  but the record contains no Γ-flow with multiple outcome attractors and an
  established global physical measure weighting them. If an external
  initial ensemble is used to define basin weights, that ensemble is an
  inserted distribution — M5 smuggles.
- **State dependence:** no mechanism on record by which μ_phys depends on
  the initial quantum state; SRB measures are properties of the flow, not
  of initial conditions.

**Arrow A: FAIL (for the purpose of Born derivation) with the precise
reason:** per-basin physical measures exist in suitable classes, but the
global inter-basin weighting — the part that would have to become Born
weights — is not supplied by the physicality condition. Supplying it
externally = insertion (M5 FAIL). The route does not fail because "dynamics
can't select measures" (the N0 audit refuted that); it fails because the
*specific selection it provably provides* is per-basin, and the inter-basin
structure needed for outcome probabilities is exactly what remains
unselected.

### Arrow B (μ_F → h_F)

Even granting a hypothetical global μ_phys, h_F requires a dynamically
earned outcome map. Attractor labels are candidate outcome *identifiers*,
but "which attractor the trajectory enters" is not, by itself, a *realized
single outcome* for the quantum measurement problem — the record's own
hostile-review standard (decoherence/branch labels don't count) applies.
h_F would need additional structure linking attractors to pointer outcomes
dynamically. **FAIL as currently constructible.**

### Arrow C / D — mooted downstream of A/B. Not reached.

### q-control

NOT REACHED meaningfully: even granting a hypothetical global measure, the
route has no mechanism whose inter-basin weights could be compared against
the q-family — the missing object (dynamically fixed inter-basin weighting)
is the same object that would have to exclude q≠2. If an inserted ensemble
were used, the q-control could not exclude q≠2 either (any normalized
q-family could be produced by choice of ensemble) — which is the relocation
signature.

### State-dependence

SRB measures are state-independent (flow properties). For Born weights the
measure would need ψ-dependence; nothing in the SRB mechanism provides it.
If ψ-dependence were inserted into the flow's definition per-state, that is
a per-state supplied measure family — the relocation pattern the charter's
§7 flags. **Mandatory attack result: the route cannot satisfy
state-dependence without smuggling.**

### Composition

Not reached (upstream gates failed). Recorded: composition would have to
constrain inter-basin weights multiplicatively across independent systems —
a requirement that, if imposed, begins to look like Born-structure import
(flagged for M5 if the route were revived).

### Hostile baseline

Nearest: nonlinear amplify-and-collapse mechanisms (GRW/CSL-type) — where
the noise statistics ARE chosen to reproduce Born. This route is that
structure with "SRB statistics" replacing "chosen noise statistics," and the
q-control shows the replacement cannot be justified internally.

### M-table

| Gate | Result | Reason |
|---|---|---|
| M1 | PASS | Γ-dynamics class statable; acts on hierarchy at declared scope |
| M2 | FAIL | physicality selects per-basin measures; global inter-basin weighting not supplied by the condition |
| M3 | FAIL | attractor labels ≠ dynamically earned realized outcomes (record standard) |
| M4 | UNRESOLVED | downstream of M2/M3 failures |
| M5 | FAIL | any completion requires inserted initial ensemble (smuggling channel) |

**GGC0-P: PASS** (the formulation is genuinely on Γ). **GGC0-R: FAIL** (no
influence/response relation derivable from the route as it stands).

### Route label: **STRUCTURAL-FAIL**

(The structural condition — physicality — provably selects objects at the
wrong granularity: it does not select the required global outcome-weighting
object. This is a shown insufficiency, not an undecidability. The condition
was stated before the Born analysis; the failure is at the condition's own
reach.)

---

## Route S3 — Unique-ergodic / unique-invariant structure

### 0. Frozen structural condition

**Property imposed:** the Γ-dynamics is uniquely ergodic — exactly one
invariant probability measure exists on the Γ-state space.

**Why independently motivated:** uniqueness of the invariant statistics is a
structural determinacy condition — the theory's statistical predictions
would then be fixed by the dynamics alone, with no ensemble freedom. This is
motivated as "no extra statistical input" without reference to Born.

**Mathematical class:** continuous flows on compact Γ-state space with
trivial invariant-measure structure.

### Arrow A (F → μ_F)

- **Existence:** possible in principle (unique ergodicity is a real
  phenomenon), but no Γ-dynamics on the record is established to be uniquely
  ergodic; the Γ-flow itself is not an established object (same gap as S1).
- **Uniqueness:** would hold by hypothesis where the condition applies.
- **Physical selection:** unique ergodicity gives statistical determinacy
  for time averages of continuous observables — but (per the corrected
  audit, and charter §4-S3) this is time-average convergence, not arbitrary
  ensemble pushforward convergence. For outcome statistics from a single
  realized trajectory, time averages of an indicator of the outcome region
  would give the outcome's *frequency along that trajectory* — which is the
  right kind of object. This is the strongest form of the route: a single
  long trajectory samples the unique measure.
- **State dependence — the mandatory attack (charter §8 execution
  instruction):** the unique invariant measure is a property of the flow
  alone. A uniquely ergodic flow has *one* statistical structure, shared by
  all initial conditions. Born weights, however, vary with the initial
  quantum state (different ψ ⇒ different outcome distributions). Two
  possibilities:
  1. ψ enters as a *parameter of the flow*: for each ψ, a different
     Γ-dynamics, each with its own unique invariant measure μ_F[ψ]. Then
     state-dependence is possible in principle — but then the route must
     show the map ψ ↦ μ_F[ψ] is uniquely fixed by the *same* structural
     condition across the family, and that its outcome-pushforward is Born.
     No such family-level uniqueness theorem exists on the record or in
     standard ergodic theory; constructing one would be inventing new
     structure (forbidden).
  2. ψ does not enter the flow: then μ_F is state-independent, and its
     pushforward is one fixed distribution over outcomes — it cannot equal
     `|α_i|²` for all admissible α. **Derivation of the failure:** a fixed
     measure ν on outcome space satisfies `ν(i) = |α_i|²` for at most a
     measure-zero set of amplitude configurations; the Born rule is
     state-dependent by definition, so a state-independent pushforward
     cannot be Born for the full admissible class. **This failure is
     derived, not assumed.**

**Arrow A: the condition (unique ergodicity of a fixed flow) provably
cannot deliver state-dependent Born weights; the family version (μ_F[ψ])
requires an unestablished family-level uniqueness theorem.**

### Arrow B — attractor/region labels again face the realized-outcome standard; also downstream. UNRESOLVED/FAIL as above.

### Arrow C / D — mooted.

### q-control

The derived state-independence failure can be restated in q-family terms: a
state-independent ν cannot match *any* nontrivial q-family (all q-families
are state-dependent for q ≠ 0). So the route doesn't merely fail to force
q=2 — it fails to force *any* state-dependent rule. The q-control confirms
the failure is upstream of the exponent question.

### State-dependence (explicit disposition)

**Derived failure for the fixed-flow version** (state-independence provably
incompatible with Born for all states); **unestablished requirement for the
family version** (μ_F[ψ] canonical would need a new theorem). The charter's
§7 mandatory attack is thus answered concretely: for S3 the attack *succeeds*
as a derivation in the fixed-flow case.

### Composition

Not reached.

### Hostile baseline

Nearest: none standard — uniquely ergodic dynamics are not a known
measurement mechanism. (The route's interest is precisely that it is *not*
a restatement of an existing O/B mechanism; it fails for structural reasons
instead.)

### M-table

| Gate | Result | Reason |
|---|---|---|
| M1 | UNRESOLVED | Γ-flow not established on the record (compactness, continuity unverified) |
| M2 | PASS-in-principle/UNRESOLVED | unique ergodicity *would* satisfy M2's uniqueness requirement where it holds — but no Γ-flow established to have it |
| M3 | UNRESOLVED | h_F not constructible without the flow |
| M4 | FAIL (fixed-flow case, derived) / UNRESOLVED (family case) | state-independence provably incompatible with Born for all states; family uniqueness unestablished |
| M5 | UNRESOLVED | downstream |

**GGC0-P: UNRESOLVED. GGC0-R: UNRESOLVED.**

### Route label: **STRUCTURAL-FAIL**

(Adjudicated at the actually earned status under frozen assumptions: the
fixed-flow version of the route is *derivably* incompatible with Born
state-dependence — a shown structural failure, the strongest kind, obtained
without any Born information entering the derivation of the failure. The
family escape-hatch (μ_F[ψ]) is recorded as OUT-OF-SCOPE territory (it
would be a different, stronger structural condition), not executed.)

---

## Route S4 — Symmetry / covariance / conservation selection

### 0. Frozen structural conditions (stated before solving for q)

All assumptions declared first, per charter §14-execution instruction 9:

1. **Normalization:** Σ_i p_i = 1.
2. **Permutation symmetry:** p_i depends on the amplitudes only through
   permutation-invariant functions (in particular, p_i for outcome i depends
   on α_i and |{α_j}| symmetrically).
3. **Continuity:** p_i is continuous in the amplitudes.
4. **Composition:** for two independent systems with amplitudes α and β,
   the joint outcome probabilities are the products of the separate ones —
   p_{ij}(α⊗β) = p_i(α)·p_j(β).
5. **Coarse-graining consistency (additivity):** merging two outcomes into
   one adds their probabilities.
6. **Covariance/locality:** the rule is defined locally on the influence
   data, with no reference to global structure beyond the declared class.

No quantum-mechanical structure (inner product, Hilbert norm, unitarity) is
assumed in stating these.

### Solving for q

**The decisive analysis.** Work in the q-family `p_i(q) = |α_i|^q / Σ_j
|α_j|^q` (the charter's hostile control) and ask which conditions every
q≠2 fails and q=2 satisfies.

- Normalization: satisfied for all q (it's built into the family). Selects
  nothing.
- Permutation symmetry: satisfied for all q. Selects nothing.
- Continuity: satisfied for all q. Selects nothing.
- **Composition (the load-bearing condition).** For independent systems
  with amplitudes α_i, β_j: the joint amplitude is α_iβ_j (the record's
  quantum structure supplies tensor-product amplitudes — this is already
  Hilbert structure; flagged for M5 below). Composition demands:
  p_{ij}(α⊗β) = p_i(α)·p_j(β).
  For the q-family: p_{ij}(q) ∝ |α_iβ_j|^q = |α_i|^q|β_j|^q, and the
  normalization factors cancel *only for the product form*: p_{ij}(q) =
  |α_i|^q|β_j|^q / (Σ|α|^q)(Σ|β|^q) = p_i(q)·p_j(q). **Composition holds
  for ALL q.** The q-family is multiplicative for every q — composition
  does NOT select q=2.
- **Additivity/coarse-graining:** also satisfied for all q (normalized
  families are additive under outcome-merging by construction). Selects
  nothing.
- **Covariance/locality:** not a constraint on the exponent at this level.

**Result: none of the declared structural conditions, applied to the
q-family, excludes any q≠2.** The exponent is simply not determined by
normalization + symmetry + continuity + composition + additivity. To force
q=2 one must additionally import:

- the Born-specific step: identifying the amplitude-phase structure with a
  norm-squared (i.e., assuming the Hilbert-space inner product as the
  probability-relevant quantity), or
- a dynamical mechanism (attractor/noise/trajectory statistics) whose
  *measure* happens to push forward to |α|² — which is S1/S2/S3 territory,
  not a symmetry argument.

**The honest structural statement:** within this condition set, q is a free
parameter. The conditions select the *family* (power-law normalized rules),
not the exponent. This is itself a genuine finding: the q-control's purpose
was to identify what excludes q≠2, and the answer is *nothing in the
declared symmetry set* — the exclusion, where it exists in accepted physics,
comes from the Born postulate itself or from dynamical mechanisms outside
S4's scope.

### Arrow-by-arrow

- **Arrow A (F → μ_F):** S4 never constructs a measure on Γ-space at all —
  the route constrains *probability rules* directly, not measures on
  microscopic state space. There is no μ_F to select. **FAIL as a
  chain-route** (it operates at the wrong level of the chain: it is a rule
  on outcomes, not a measure selected by dynamics).
- **Arrow B/C/D:** not reached as chain objects.

### M-table

| Gate | Result | Reason |
|---|---|---|
| M1 | FAIL | no F on Γ; the conditions constrain outcome rules directly, not hierarchy dynamics |
| M2 | FAIL | no measure-class selection occurs at Γ level |
| M3 | FAIL | h_F not constructed (outcomes presupposed by the rule) |
| M4 | FAIL (as derivation) | q-family not excluded for any q≠2 by the declared conditions; q=2 forced only by importing Hilbert structure |
| M5 | **FAIL (relocation identified)** | the only step that selects q=2 is the identification of amplitudes' relevance via Hilbert inner product — i.e., quantum-measure structure is upstream, equivalent to Born weighting (charter §6: "if that assumption is equivalent to Born weighting, mark relocation") |

**GGC0-P: FAIL** (not a law on the full influence hierarchy — it is a
direct constraint on outcome probabilities). **GGC0-R: FAIL.**

### Route label: **RELOCATED**

(The relocation is precisely identified: the composition condition was
hoped to be the Born-selector, but it is q-independent; the only
q=2-forcing step is Hilbert-norm import, which is Born-equivalent structure
upstream. This is a *shown* relocation with the exact mathematical step
named, satisfying the charter's requirement to identify which assumption
does the work.)

**Recorded finding (non-negative content):** the declared symmetry set
admits the full q-family. Any future claim that symmetry alone derives Born
is refuted by this analysis at the declared conditions. That refutation is
itself a structural result worth recording — it is the S4 lesson.

---

## Out-of-scope successor note

During S3's analysis, the family-level condition — "uniqueness of the map
ψ ↦ μ_F[ψ] across a family of Γ-dynamics" — was identified as a genuinely
distinct structural condition, stronger than any of S1–S4. Recorded as:

**OUT-OF-SCOPE SUCCESSOR: family-level equivariance uniqueness
(ψ-parameterized flow families).** Not executed, per charter §4.

---

## Campaign-level summary tables

### M1–M5 across routes

| Gate | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| M1 | UNRESOLVED | PASS | UNRESOLVED | FAIL |
| M2 | UNRESOLVED | FAIL | UNRESOLVED (PASS-in-principle) | FAIL |
| M3 | UNRESOLVED | FAIL | UNRESOLVED | FAIL |
| M4 | UNRESOLVED | UNRESOLVED | FAIL (fixed-flow, derived) | FAIL |
| M5 | UNRESOLVED | FAIL | UNRESOLVED | **FAIL (relocation identified)** |

### q-control results

| Route | q-control status | Finding |
|---|---|---|
| S1 | NOT REACHED | no induced measure to test |
| S2 | NOT REACHED (meaningfully) | missing object (inter-basin weighting) is the same object that would exclude q≠2; with insertion, any q achievable — relocation signature |
| S3 | superceded by derived failure | state-independent pushforward incompatible with *every* nontrivial q — failure is upstream of exponent |
| S4 | **RUN — decisive** | no declared condition excludes any q≠2; q is free within the family; q=2 only via Hilbert import |

### State-dependence results

| Route | Result |
|---|---|
| S1 | open difficulty recorded (family-uniqueness needed; not established) |
| S2 | fails without smuggling (SRB measures state-independent) |
| S3 | **derived failure** for fixed-flow; family version needs new theorem |
| S4 | n/a (no measure constructed) |

### Composition results

| Route | Result |
|---|---|
| S1/S2/S3 | not reached |
| S4 | **decisive negative**: composition holds for all q — selects the family, not the exponent |

### GGC0-P/R

| Route | GGC0-P | GGC0-R |
|---|---|---|
| S1 | UNRESOLVED | UNRESOLVED |
| S2 | PASS | FAIL |
| S3 | UNRESOLVED | UNRESOLVED |
| S4 | FAIL | FAIL |

No concrete new influence/response relation was derived by any route.
Recorded plainly per charter §12.

### Genuine partial chains earned?

- **S2 earned M1 (PASS)** — the only gate passed by any route at the Γ level
  — but failed M2 (the gate that matters for canonical selection). This is
  not a "nontrivial portion of the chain" in the charter's sense (the chain
  requires *canonical selection*, which is exactly what failed).
- **S4 produced a genuine structural finding** (the q-family is not
  excluded by the declared symmetry set) — but as a *negative* result about
  symmetry-routes, not a positive chain segment.
- **No route earned a genuine nontrivial portion of the Born chain.**

---

## Final campaign terminal

Assessment against the four terminals:

- **G2-A7-CHAIN-PASS:** no route CHAIN-POSITIVE. No.
- **G2-A7-CHAIN-PARTIAL:** requires at least one route earning a genuine
  nontrivial portion of the chain. S2's M1 pass is a formulation-level
  pass, not a chain segment (the chain's first substantive link — canonical
  selection — failed). S3's derived state-dependence failure is a negative
  finding about that route, not a chain portion. S4's q-family result is a
  negative finding about symmetry routes. **No route earned a chain
  portion. Not this terminal.**
- **G2-A7-CHAIN-N0:** requires all four routes failed/relocated/
  baseline-restated **and** a route-specific exhaustion argument. S2 and S4
  are genuinely disposed (STRUCTURAL-FAIL, RELOCATED). But S1 and S3 are
  UNRESOLVED — not because their conditions were shown to fail, but because
  the required Γ-flow objects are not established on the record, and
  constructing them is forbidden. There is no exhaustion argument for S1/S3:
  their structural conditions (equivariance within a functional class;
  unique ergodicity) are *untested* against the Γ-dynamics because the
  Γ-dynamics as a flow does not exist on the record yet. **N0 is not
  available.**
- **G2-A7-CHAIN-OPEN:** no positive result earned; routes remain
  mathematically unresolved (S1, S3 undecidable on the current record
  without inventing new structure). **Matches.**

# **G2-A7-CHAIN-OPEN**

Per charter §12: this is a valid terminal and is not a failure of the
campaign. No positive claim follows. The two genuinely disposed routes
(S2, S4) are negative; the two unresolved routes (S1, S3) are undecidable
on the current record.

**The campaign's net structural finding, recorded for adjudication:** the
canonical-measure route to Born is blocked on the current record at a
point *upstream* of every mathematical question the routes pose — the
Γ-space flow itself is not an established object. S1/S3's undecidability
and S2's per-basin limitation and S4's q-freedom all live downstream of
that single gap. Whether the program should build the Γ-flow (a
Level-0-scale construction) is an owner decision outside this campaign's
scope.
