# GGC0 G2 A-7 N0 EXHAUSTION AUDIT 01
## Executed under `GGC0_G2_A7_N0_EXHAUSTION_AUDIT_CHARTER_01.md` (frozen `fa6fa70`)

**Audit target:** the structural no-go/exhaustion claim in
`GGC0_G2_A7_GENERATIVE_SEARCH_01.md` at `9ea0ed8`. No sixth candidate; C1–C5
unaltered; G1 not reopened; G3 not opened.

**Preregistered prior (on record, not part of the decision rule):** T2
expected FALSE, T3 expected UNPROVED, T4 expected to be the decisive
question. The dispositions below were reached by working through each
theorem independently as required.

---

## Part 1 — Theorem audit (T1–T4, independently)

### N0-T1 — "A deterministic outcome map alone does not automatically specify ensemble probabilities."

**Analysis.** A map h_F from initial conditions to outcomes determines, for
each individual initial condition, a definite outcome. It says nothing about
how *ensembles* of initial conditions are distributed. That distribution is
extra information. This is standard and uncontroversial: the map `x → h(x)`
carries no measure.

**Hostile check:** Could one argue the map *induces* a measure via counting
preimages? Only relative to a measure on the domain — which is exactly the
extra information. No escape.

**Disposition: TRUE.** The 9ea0ed8 execution established this correctly.

### N0-T2 — "No deterministic F can dynamically determine or uniquely select a probability measure."

**Analysis.** This is the claim the original execution relied on implicitly,
and it is **false as a universal statement**. Established mathematics:

- **Unique ergodicity.** In a uniquely ergodic topological dynamical system
  there is a unique invariant probability measure (e.g., irrational
  rotations on the circle; more generally, systems with trivial
  invariant-measure structure). Under the standard compact/continuous
  hypotheses, empirical measures — equivalently, time averages of continuous
  observables — converge to that measure **for every initial point**. This
  does **not** imply that the ordinary pushforward of every arbitrary
  initial ensemble converges weakly to the invariant measure. The hostile
  value of the comparator stands: deterministic dynamics can possess a
  uniquely distinguished invariant statistical structure. The dynamics has
  selected the measure — not inserted it.
- **Physical (SRB) measures.** For a uniformly hyperbolic attractor of an
  appropriate smooth deterministic system, there is a distinguished SRB/
  physical invariant measure such that time averages for
  Lebesgue-almost-every initial point **in the attractor's basin** converge
  to averages under that measure (Pesin; Young; Ledrappier–Young). For more
  general dynamical systems, uniqueness and full-basin convergence are not
  implied unless the relevant class establishes them. The point retained:
  deterministic dynamics can select physically distinguished invariant
  statistics for positive/full-measure sets of initial conditions in
  suitable classes. The measure is selected by the dynamics plus a
  structural requirement on the physical ensemble (spread over states rather
  than concentrated on zero-measure sets) — generic rather than tuned, and
  motivated independently.
- **Equivariant uniqueness (the Bohmian precedent).** For standard Bohmian
  dynamics, `|ψ|²` is equivariant. Goldstein–Struyve establish its
  uniqueness **within the class of equivariant distributions that are local
  functionals of the wavefunction**. This is sufficient as a hostile
  counterexample to the unrestricted assertion that deterministic dynamics
  plus independently stated structural restrictions can never single out a
  distinguished measure. It does not establish uniqueness among all
  conceivable equivariant distributions and does not furnish a GRUT
  mechanism. No measure was
  inserted; the measure follows from the dynamics plus the requirement that
  the ensemble distribution be preserved by the dynamics.

These three mechanisms share a structure: **dynamics + an independently
motivated structural condition (unique ergodicity / physicality /
equivariance) → unique measure.** The measure is not in the equations as a
primitive; it is a consequence of the dynamics' interaction with a generic
structural requirement.

The original execution's no-go — "the measure must be either inserted with
exactly the right structure or F must be fine-tuned" — never considered this
third option, and the Bohmian case is a direct counterexample to it *as a
universal claim*: there, the "right structure" (`|ψ|²`) follows from
equivariance, and equivariance is arguably not "tuning to Born" but a
generic conservation-of-ensemble-structure condition.

**Disposition: FALSE as an unrestricted universal statement about
deterministic dynamical systems; UNPROVED at the declared Γ-space/F-class
scope.** Established deterministic counterexamples (unique ergodicity; SRB
measures; equivariant uniqueness within the Goldstein–Struyve class) show
that "deterministic dynamics can never select a measure" is false generally.
But the audit has not constructed or proved the existence of such a
measure-selecting dynamics on GRUT's actual full influence hierarchy. This
distinction does not rescue N0: exhaustion requires ruling out that
possibility, which `9ea0ed8` did not do.

### N0-T3 — "Any F whose natural/invariant measure pushes forward to Born is necessarily fine-tuned relocation."

**Analysis.** The original execution treated "measure pushes forward to
Born" as either (a) insertion or (b) fine-tuning. The Bohmian counterexample
shows a third possibility: (c) the pushforward follows from a structural
uniqueness condition (equivariance) that is not itself about Born weights.
In Bohmian mechanics, no parameter was tuned to make the pushforward `|ψ|²`;
the pushforward is *forced* by the requirement of equivariance, which would
be a natural condition to impose on any measure-dynamics pair regardless of
what the resulting measure turned out to be.

Is the distinction between (b) and (c) rigorous, or is "imposing
equivariance" already a disguised Born-importation? Honest assessment:

- Equivariance is *not* specific to Born: it is the requirement that the
  ensemble measure be invariant under the dynamics. Imposing it does not
  presuppose the answer; for a different dynamics, the unique equivariant
  measure would be something else.
- However, in the Bohmian case, the dynamics itself was *constructed*
  (historically) as the velocity field that makes `|ψ|²` equivariant. So
  for the actual Bohmian dynamics, the pair (dynamics, measure) was
  co-designed. The uniqueness theorem is real, but the dynamics was not
  independent of the target measure. This is the strongest form of the
  "fine-tuned relocation" reading: not that equivariance implies Born
  generally, but that the specific F for which equivariance yields Born was
  selected with Born in mind.
- **The critical question for N0:** does the declared F-class contain
  dynamics for which a structural condition yields Born *without* the
  dynamics having been designed around Born? The original execution provided
  no argument for this. The existence proof (Bohmian) shows such pairs
  exist in nature of mathematics; whether they exist in the declared class
  is unresolved.

**Disposition: UNPROVED as a universal claim.** "Necessarily fine-tuned" was
asserted, not established. The Bohmian comparator demonstrates a logical
route of `dynamics + structural restriction → distinguished |ψ|²
distribution` within a specific theory/class — it defeats "necessarily
relocation" as an established theorem. It does not prove that this route was
independently discovered without Born motivating the dynamics (the
historical co-design caveat stands), nor that an analogous GRUT F exists.
Thus it furnishes no positive candidate — but it removes the universal
presumption the original execution relied on.

### N0-T4 — "There exists no admissible structural condition on F that singles out a Born-compatible measure without importing A-7."

**Analysis.** This is the actual exhaustion burden. The audit must determine
whether the original execution established it. It did not: the execution
never enumerated or analyzed candidate structural conditions. The candidate
conditions suggested by the mathematical material above:

1. **Equivariance** (invariance of the ensemble measure under the dynamics):
   selects, when unique, a measure determined by F. Whether the unique
   equivariant measure of any F in the declared Γ-class can be Born on
   outcomes is completely unexamined. The Bohmian precedent shows the
   mechanism is not vacuous.
2. **Physicality/SRB** (measure selected for a full basin of absolutely
   continuous initial ensembles): for chaotic Γ-dynamics, a physical measure
   exists and is dynamically selected. Whether `(h_F)_* μ_phys` can be Born
   is unexamined. Note: for it to yield *exactly* `|α_i|²` for arbitrary
   initial states would require an extraordinary coincidence — but the
   audit's burden is to establish impossibility, not improbability.
   "Improbable for generic F" is not "impossible for all admissible F,"
   unless a structural argument (e.g., a no-go theorem connecting the
   symmetries of h_F to the form of the pushforward) is supplied.
3. **Unique ergodicity:** same structure; unexamined.
4. **Locality/local structure on Γ:** the declared class may impose
   locality. Whether locality + any of the above forces or forbids Born
   pushforward is unexamined.

The original execution's argument — "the measure must be inserted or
fine-tuned" — amounts to assuming T4 without proof. The honest statement:

**Disposition: UNPROVED.** The burden for class exhaustion was not met. No
admissible-structural-condition analysis was performed. The loophole
identified in the charter (deterministic F selecting its own measure via
structural requirements) is genuine and unaddressed by the original
execution.

**However** — and this must be recorded with equal clarity — the unproved
status of T4 does not make T4 *false*. No candidate structural condition has
been shown to yield Born within the declared class either. The correct
status is: **exhaustion not established; loophole open; no positive result
either.** The audit cannot convert "N0 not earned" into "a candidate
exists" — that would be the mirror-image error.

---

## Part 2 — Hostile-control families

### Control 1: Natural/physical measures of deterministic attractors

Physical measures (Sinai–Ruelle–Bowen) exist for broad chaotic classes and
are selected by the dynamics for full-measure basins of absolutely
continuous initial conditions. This is measure-selection-by-dynamics in the
charter's type-(4) sense — a serious counterexample category to the
original no-go. **Does not by itself invalidate N0** (nothing here shows
Born pushforward), but it invalidates the *premise* that deterministic
dynamics cannot select ensemble measures. The original execution's universal
statement is false; the N0 exhaustion claim, which rests on it, is
undermined at its foundation.

### Control 2: SRB-type measure selection

As above: type-(4). The selection mechanism (full basin + absolute
continuity of physical ensembles) is generic, not tuned to any particular
target measure. Whether it can produce Born in the declared class:
unexamined by 9ea0ed8. **Invalidates the universal premise; does not
establish Born.**

### Control 3: Unique ergodicity

Type-(3): dynamics + uniqueness requirement → unique measure. Rare but real
(irrational rotations, certain interval exchange transformations, some
horocycle flows). Where unique ergodicity holds, the dynamics fully
determines the ensemble statistics of every orbit (uniform convergence of
empirical measures). **Same verdict: invalidates the universal premise,
does not establish Born.**

### Control 4: Invariant/equivariant distributions

Type-(5): equivariance within a declared functional class. The Bohmian
precedent lives here. Uniqueness of the equivariant measure is a real
theorem in that case — with the scope qualification recorded in Control 5:
uniqueness holds within the class of equivariant distributions that are
local functionals of the wavefunction (Goldstein–Struyve), not among every
conceivable equivariant probability distribution. Whether any F in the
declared Γ-class has a unique equivariant measure whose outcome-pushforward
is Born: unexamined. **Invalidates the universal premise; does not establish
Born.**

### Control 5: The Bohmian `|ψ|²` equivariance example (hostile comparator only)

Strictly as a comparator. The precise result: for standard Bohmian
dynamics, `|ψ|²` is equivariant, and Goldstein–Struyve establish uniqueness
**within the class of equivariant distributions that are local functionals
of the wavefunction**. The comparator therefore demonstrates that:

> deterministic dynamics plus an independently stated structural
> restriction can, in at least some mathematical frameworks, single out a
> distinguished measure.

It does **NOT** establish:
- uniqueness among every conceivable equivariant probability distribution;
- that equivariance alone derives Born (the derivation relies on the
  specific structure of the Schrödinger flow and the configuration-space
  representation);
- that GRUT has such a mechanism.

With those qualifications, the comparator refutes the universal form of
T2/T3: no insertion of a probability postulate is involved — the
distinguished measure follows from the dynamics plus the structural
restriction. **But** it does not show that GRUT's declared F-class contains
such a mechanism: Bohmian dynamics is not of the form
`F[Γ, Φ, access, state]` (it is a velocity field on configuration space
defined directly from the wavefunction, with the outcome map the identity on
positions), and its equivariance relies on the specific structure of the
Schrödinger flow. Importing it as a GRUT candidate would violate the audit's
charter; using it to refute the *universal* claim is exactly its proper
role. **Verdict: refutes the universal no-go premise; does not provide a
GRUT mechanism.**

---

## Part 3 — Born pushforward-chain analysis

Chain: `F → μ_F → h_F → (h_F)_*μ_F → |α_i|²`

What 9ea0ed8 actually established:

| Arrow | Established impossible? | Status |
|---|---|---|
| F → μ_F (dynamics selects a canonical measure) | **No.** The execution asserted measures must be inserted; ergodic theory contradicts this for broad classes. | **Merely unsupported (and contradicted in general)** |
| μ_F → h_F (outcome map well-defined given F) | Not in dispute; h_F was arguably well-defined for C4/C5. | **Not an obstacle** |
| (h_F)_*μ_F well-defined | Follows if μ_F and h_F are. | **Not an obstacle** |
| (h_F)_*μ_F = \|α_i\|² for arbitrary admissible α | **No argument given.** The execution never analyzed whether any admissible structural condition forces this; it assumed any Born pushforward implies tuning. | **Open; the decisive arrow** |
| Uniqueness/naturalness of the whole chain within the declared class | Not addressed. | **Open** |

**Chain verdict:** the original no-go ruled out *no arrow*. It asserted,
without proof, that the first and fourth arrows cannot be traversed without
insertion or tuning. The first assertion is contradicted by ergodic theory
(T2 FALSE); the fourth is the genuine open question (T4 UNPROVED). The
exhaustion claim fails at exactly the point the remand anticipated.

---

## Part 4 — C4/C5 exhaustion analysis

The original execution's C4/C5 objection was: "the probability of reaching
attractor i is the measure of the basin of attraction i; what measure?
Natural measures don't in general induce Born; making them do so requires
tuning." The audit question (charter §6) is the stronger one: **has the
record ruled out every admissible structurally selected physical measure in
those families?**

**Analysis.** No. The original argument considered only:

- the uniform/Lebesgue measure on initial conditions (found: doesn't push
  to Born in general);
- tuned measures (found: relocation).

It did not consider:

- **SRB/physical measures in systems with suitable hyperbolic structure** —
  such measures demonstrate that deterministic dynamics can select
  distinguished statistics for typical initial states. **However, in a
  multiple-attractor outcome model, separate SRB measures on separate
  attractors do not by themselves determine relative probabilities of
  entering their basins.** A global initial-distribution or additional
  global physical-measure structure may still be required. The audit does
  NOT establish that SRB dynamics actually provides such a measure.
- **equivariant measures within the declared functional class** —
  unexamined.
- **structural conditions tying h_F to F** (e.g., if the outcome map is
  definable from the same structural data as the dynamics, the pair may
  admit a uniquely selected measure whose pushforward is constrained by the
  same structure) — unexamined, and this is the class of mechanism the
  Bohmian comparator instantiates (within its recorded scope limits).

**C4/C5 exhaustion verdict: NOT ESTABLISHED.** The measure objection
presented in 9ea0ed8 suffices to show that *naive* measure choices fail, not
that the families are exhausted. The legitimate remaining loophole is the
narrower one: **9ea0ed8 did not establish that no admissible Γ-dynamics can
possess a canonical global physical/equivariant measure whose pushforward
through its outcome map is Born.** C4 and C5's substantive status is
unchanged by this audit (they remain unproven candidates, not positive
results), but the *family-level exhaustion* claimed on their basis is not
earned.

---

## Part 5 — C1–C5 disposition-compliance audit (charter §7)

Charter §8 of the G2 execution required each candidate to receive exactly
one of: A7-POSITIVE / A7-PARTIAL-O / A7-PARTIAL-B / A7-RELOCATED /
RESTATED / GGC0-R-FAIL / UNFORMULABLE / NO-CANDIDATE.

What 9ea0ed8 actually recorded:

| Candidate | Recorded disposition | Charter-permitted? |
|---|---|---|
| C1 | "fails specification" + "nearest structure is RESTATED" | **NO** — "fails specification" is not a permitted label; the parenthetical gestures at RESTATED but does not assign it |
| C2 | "fails specification" with conditional "A7-RELOCATED (if noise inserted)" | **NO** — conditional label; the candidate's actual specification (no inserted noise) leaves it unlabeled |
| C3 | "fails specification" with conditional "A7-RELOCATED (if access given Born properties)" | **NO** — same conditional structure |
| C4 | "fails specification" + "A7-RELOCATED (measure)" | **Ambiguous** — two labels given, one permitted (A7-RELOCATED) and one not |
| C5 | "fails specification" + "A7-RELOCATED (joint measure)" | **Ambiguous** — same structure as C4 |

**Compliance finding: NON-COMPLIANT.** No candidate received exactly one
permitted disposition. Three candidates (C1, C2, C3) received no permitted
label at all; two (C4, C5) received a permitted label *plus* an
unpermitted one. The failure mode is systematic and traces to a single
conception in the execution: candidates were terminated at specification
("fails at item k") rather than being assigned terminal dispositions.

Can the labels be assigned now without scientific judgment after results
were seen? Assessment:

- C1: its failure (no outcome mechanism at all, structure equivalent to
  2PI-type self-consistency) maps cleanly to **RESTATED** — but wait: the
  candidate never produced O or B, so RESTATED (which implies O/B
  equivalence at scope) is too strong; NO-CANDIDATE is a class-level label,
  not candidate-level. The honest assignment requires judging whether a
  candidate that "fails at specification" is RELOCATED, UNFORMULABLE, or
  something else — and that judgment depends on *why* it failed, which is
  exactly the scientific judgment the audit is told to flag rather than
  make.
- C2/C3: conditional RELOCATED labels depend on a design choice (insert
  noise? give access Born properties?) that was not made and should not be
  made post hoc.
- C4/C5: A7-RELOCATED was arguably earned on the *measure-insertion
  branch*, but the audit's Part 4 shows that branch is not the only branch —
  the families are not exhausted, so even the RELOCATED label may be
  premature.

**Disposition-compliance verdict: PROCEDURAL DEFECT confirmed.** Relabeling
now would require post-hoc scientific judgment; per charter §7, the defect
is flagged for owner adjudication rather than repaired.

---

## Part 6 — Audit terminal

Substantive component: T2 FALSE (universal premise contradicted by
ergodic theory); T3 UNPROVED; T4 UNPROVED (exhaustion burden not met); the
Born-chain's decisive arrows open; C4/C5 family exhaustion not established.
**A genuine deterministic-measure loophole remains inside the declared
F-class** — specifically the possibility, unexcluded by anything in 9ea0ed8,
that some admissible F in the class admits a uniquely selected physical or
equivariant measure whose outcome-pushforward is Born.

Procedural component: candidate dispositions non-compliant with charter §8;
repair requires post-hoc judgment; flagged, not fixed.

Both are present.

# **N0-AUDIT-MIXED**

Per charter §8: this is not a positive A-7 result. `G2-A7-N0` is not earned.
G2 remains unresolved pending owner adjudication.

---

## Summary for adjudication

1. **T1: TRUE** (correctly established by the original execution).
2. **T2: FALSE** as a universal claim — deterministic dynamics can uniquely
   select ensemble measures (unique ergodicity; SRB/physical measures;
   equivariant uniqueness per the Bohmian comparator, used strictly as a
   hostile comparator).
3. **T3: UNPROVED** — "necessarily fine-tuned" was asserted, not shown; the
   distinction between fitting-to-Born and Born-from-independent-structural-
   condition was not made.
4. **T4: UNPROVED** — the actual exhaustion burden; no structural-condition
   analysis was performed by 9ea0ed8.
5. **Born chain:** no arrow ruled out; the execution's argument assumed its
   conclusion at the decisive arrows.
6. **C4/C5:** family exhaustion not established (naive-measure analysis
   only).
7. **Dispositions:** procedurally non-compliant; defect flagged for owner
   adjudication, not repaired.
8. **Terminal:** N0-AUDIT-MIXED. `G2-A7-N0` is not earned; no positive
   A-7 result follows either. G2 unresolved; no successor opened.
