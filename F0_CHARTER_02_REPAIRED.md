# F0 — CHARTER 02 (REPAIRED; SELF-CONTAINED)
**Status:** OWNER-DIRECTED REPAIR (`F0_OWNER_RULING_01.md`), transplanted into
`vsctestinggrut` per the owner integration ruling (`F0_REPAIR_IMPORT_PROVENANCE_01.md`)
and made self-contained: this is now the **authoritative standalone F0 charter**.
R1–R10 from the reviewer handoff applied exactly; R11 added; the whole-law originality
firewall (**R9**) is now encoded explicitly (§7).
**Date:** 2026-10-05 · **No computation. No candidate-law search. No implementation of
`R_Gamma`, `Cl_Gamma`, `S`, or `U` in this charter.**

## 1. The question (owner, verbatim, prominent)

> Can presently realized influence data constrain and positively generate future physical
> accessibility without secretly assuming response data for inaccessible contexts?

## 2. Hierarchy (F0-A / F0-PHYS / F0-B / F0-C / F0-D)

### F0-A — KINEMATICS
Define `(C, Γ)` plus representation equivalence and composition.
- **Primitive finite objects.** `C` = a finite access structure: a finite set of contexts
  together with the compatibility relation declaring which subsets can be jointly
  co-instantiated / jointly accessed. `Γ` = the finite contextual influence data
  legitimately available in the current structure (measured correlations, response data,
  veto witnesses). Everything F0 consumes at this level is finite and explicitly enumerated.
- **Representation equivalence.** Two presentations of `C` (or of `Γ`) are the **same
  object** if they agree up to declared representation moves — relabeling of contexts,
  reindexing of outcomes, and declared redundancy in the influence data. No equivalence
  beyond these declared moves is assumed; equivalences must be listed, not inherited.
- **Composition.** Gluing: contexts may be combined along shared sub-contexts to form
  larger contexts, with the influence data composed along the same seams. Composition is a
  declared operation on `(C, Γ)`, not an automatic closure of the compatibility relation —
  whether a composite context is *accessible* is an F0-B/F0-PHYS question, not a kinematic
  one.
- **Information price.** Every object F0 introduces carries a declared information price:
  which of its inputs are already contained in `(C, Γ)` and which are added. Anything
  priced outside `(C, Γ)` is flagged as inserted (see §7).

### F0-PHYS — PHYSICALITY OF ACCESS (gate; may be the hardest gate)
Establish whether `C` has an **observer-independent physical meaning** — e.g. physical
co-instantiability, simultaneous intervention compatibility, or jointly realizable
transformations — rather than merely encoding the measurement menu some apparatus happens
to permit. If only the latter, `C` is operational metadata, not proto-geometry.
**No locality/geometry language precedes this gate.**

### F0-B — ACCESS TRANSITION / ADMISSIBILITY (R11)
Construct the lawful access-transition relation
`R_Gamma(C, C') ∈ {0,1}`, or the correspondence
`A_Gamma(C) = { C' : R_Gamma(C, C') }`:
using only information legitimately contained in the current `(C, Γ)`, which successor
access structures are allowed? F0-B may **constrain or veto**; it need not positively
choose. A `Gamma`-dependent closure operator `Cl_Gamma` is **one special candidate**,
admissible only where monotone access growth (`C ⊆ Cl_Gamma(C)`) and idempotence are
independently justified — neither is assumed here.

### F0-C — POSITIVE ACCESS SELECTION (only if earned)
`C' = S(C, Γ)` or equivalent. **Constraint ≠ selection.**

### F0-D — COUPLED DYNAMICS (only if both access and influence evolve under a specified law)
`(C_{t+1}, Γ_{t+1}) = U(C_t, Γ_t)`. `Γ' ∈ Adm(C')` is not dynamics; an allowed-successor
set is not dynamics; a veto rule is not dynamics.

## 3. Specker baseline repair (frozen distinctions)

### 3.1 Structural Specker principle
Use only at an **explicitly declared compatibility scope**. The standard relevant
principle concerns **sharp measurements** (projective/PVM measurements in ordinary quantum
theory) — pairwise compatibility/joint measurability of the sharp objects implies joint
compatibility. "Sharp" is the broader GPT concept, and its general definition is itself
nontrivial (Gonda et al., arXiv:1712.01225); when the scope is ordinary quantum theory,
say "projective/PVM" explicitly.
Do **NOT** assert it for arbitrary POVMs/unsharp measurements: in quantum theory,
**pairwise joint measurability of unsharp measurements does not imply global joint
measurability** (cf. arXiv:1712.01225). Unsharp pairwise-but-not-globally-compatible
quantum examples are **mandatory hostile controls**: Specker's triangle is an especially
good control precisely because arbitrary unsharp quantum measurements exhibit
pairwise-without-triplewise joint measurability. Use it to test whether F0 knows which
physical compatibility notion it is talking about; the sharp/projective sector and the
unsharp operational sector remain **distinct**.

### 3.2 Statistical exclusivity principles
Event-level **consistent exclusivity / compatible orthogonality / local orthogonality**
stays distinct from the full **structural** Specker principle. Almost-quantum correlations
satisfy consistent-exclusivity-type principles while lying beyond the quantum set
(arXiv:1403.4621 establishes the almost-quantum set and the principles it satisfies) — a
derivation of one is not automatically a derivation of the other.

### 3.3 Quantum correlation set
Both of the above stay distinct from **exact quantum realizability**. Almost-quantum
correlations are a **mandatory hostile control**: Gonda et al. (arXiv:1712.01225) show a
theory yielding the almost-quantum set cannot satisfy the stronger Specker principle, and
they lie outside the quantum set.

### 3.4 CHSH precision
Any statement that an exclusivity principle yields the Tsirelson CHSH bound must list the
**additional assumptions** of the cited result (Cabello's GPT result is exclusivity **plus
two further assumptions**, arXiv:1406.5656). Never write "exclusivity alone derives
Tsirelson." Price every additional assumption.

### 3.5 Existing derivations as null comparators
A new F0 derivation of Specker-type structure earns credit only if the whole-law linkage
and **information price** differ materially from known routes — e.g. Bacciagaluppi's
derivation of Specker's principle from maximal entanglement + non-maximal measurements +
no-signalling (arXiv:2305.07917) is a **null comparator**, not a precedent to be beaten by
restatement.

## 4. Bell/Specker reconnaissance status
The completed Bell access-enlargement calculation is recorded as
**CALIBRATION / REPRODUCTION OF KNOWN LOCAL-TO-GLOBAL STRUCTURE**. It demonstrates
blocking/admissibility; it does **not** demonstrate positive selection. It lands as an
instance of **F0-B blocking**: given a proposed enlargement and a closure assumption, the
current `Γ` can veto the enlargement without assigning outcomes to the nonexistent joint
context. It does **not** supply `S`.

## 5. Specker as benchmark, not target law
"Do not make 'derive Specker' the definition of F0 success." Sharp-sector Specker behavior
is one benchmark consequence a deeper access-transition law may derive. If Specker closure
is inserted directly into `R_Gamma`, `S`, `Adm`, initial data, or a hidden global response
object, classify the result **SUPPLIED/RELOCATED at that point**.

## 6. Quantum classification firewall
Every finite result labels quantum status as exactly one of:
`EXACT` · `EXPLICIT-QUANTUM-REALIZATION` · `GRAPH-THETA-AT-DECLARED-SCOPE` ·
`NPA-k-OUTER` · `UNRESOLVED`.
**Never upgrade an outer approximation to exact quantum membership.**

## 7. Terminals
`F0-ACCESS-LAW-PASS` · `F0-CONSTRAINT-ONLY` · `F0-LATENT-RELOCATION` ·
`F0-OPERATIONAL-ONLY` · `F0-RESTATED` · `F0-OPEN` · `F0-CLOSURE-ONLY`
(a valid monotone closure/admissibility rule exists but no positive successor-selection
law is derived).

## 7. R9 — THE WHOLE-LAW ORIGINALITY FIREWALL (explicit)
Known theories and mathematics are **allowed and expected as components** — Hilbert spaces,
graphs, probability, quantum information results, the Bell/Specker literature, standard
mathematical structure of every kind. Using them is not restatement and not smuggling.
**`F0-RESTATED` applies only when the *assembled whole* imposes nothing beyond the ordinary
independent freedom of those components** — i.e. the F0-specific linkage (the way access,
influence, and transition are coupled into one law) adds no constraint and no content that
the components, taken separately and freely chosen, do not already impose.
- What **counts as earned**: a whole-law linkage with a materially different information
  price from the known routes (baseline `F0_BASELINE_AUDIT_01.md` N1–N4), or a consequence
  (Specker-type or otherwise) that the components do not jointly force without the F0
  linkage.
- What **counts as relocated/supplied**: any F0 load-bearing object (`R_Gamma` closure
  assumptions, `S`, `Adm`, initial data, or a hidden global response object) that carries
  the conclusion by construction.
- **Equivalence baselines.** Any F0 result is compared against the broader baseline set:
  classical joint distributions (Vorob'ev), the almost-quantum set, PR boxes, and the
  null comparators of the audit. An F0 "derivation" that reproduces a baseline for free is
  `F0-RESTATED`, not a pass.
- **Inaccessible-relations kill conditions.** A proposed law is killed if it (a) assumes a
  probability law or response data for a jointly **inaccessible** context (the
  nonexistent-joint-context move); (b) smuggles an access seed or a selection criterion
  whose choice performs the selection (the EA-0 failure mode, `EA0_OWNER_RULING_02.md`);
  (c) upgrades an outer approximation to exact quantum membership (violating §6); or (d)
  converts a veto (`R_Gamma`) into a positive selection (`S`) without an independent
  derivation. Each kill declares its terminal (`F0-LATENT-RELOCATION`,
  `F0-RESTATED`, `F0-OPERATIONAL-ONLY`, as applicable).

## 8. Hard stop
This charter repair, plus `F0_BASELINE_AUDIT_01.md`, are the **only** artifacts of this
cycle. No candidate-law implementation, no fixed-point search, no Born/geometry/gravity.
**STOP for owner review.**
