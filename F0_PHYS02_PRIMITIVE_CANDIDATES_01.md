# F0 PHYS-02 — PRIMITIVE CANDIDATES 01
**Status:** campaign artifact (`F0_PHYS02_CHARTER.md`). Both nouns challenged; every
candidate carries the nine required fields; Q1–Q10 applied. **No law, no transition
dynamics.**

## Part I — What is an intervention?

### I-1. Operational measurement/input  — `OPERATIONAL`
- **Definition.** A procedure an experimenter can perform, with outcome readout (Exec-01
  Meaning 1/2). **Price:** measurement theory (states/effects) + apparatus.
- **Q1 observer independence:** fails (Exec-01 P1/P4). **Q2:** conflates apparatus with
  menu. **Q4:** composition only via ad hoc procedure concatenation. **Q6:** direct
  empirical bridge. **Q7:** high (full operational formalism). **Q9:** matches current Γ
  trivially (same scope). **Verdict:** retained as **control**; not fundamental.

### I-2. Physical transformation  — `UNRESOLVED`
- **Definition.** A physically performable change of state of some substrate.
- **Failure condition found:** "physical transformation" is definable only relative to a
  supplied state/process formalism (Exec-01 P6 price: process algebra or dynamics). Without
  the formalism it is a word, not an object. **Q4:** composition needs the formalism too.
- **Verdict:** the *intent* is right (objective, observer-independent) but the object is
  not yet defined; this is precisely the gap constructor theory fills — see I-3.

### I-3. Constructor-theoretic task  — `PHYSICAL-CANDIDATE`
- **Definition (CT, source-verified):** a task is a finite specification of a subset of
  attributes of a substrate: T = {possible outputs} ↢ {impossible outputs}; a task is
  **possible** iff there exists a constructor that can perform it with arbitrarily high
  accuracy over arbitrarily many instances. Substrates carry **attributes** ( distinguishable
  sets of physical states). **Price (paid explicitly by CT):** substrate notion; attribute
  notion; task (specification pair); possibility predicate; constructor (idealized);
  serial and parallel composition. **No time in the definitions** (time is an emergent
  approximately-required substrate concept in CT, not a primitive).
- **Q1:** yes — CT's possibility statements are explicitly non-anthropocentric (source:
  constructortheory.org FAQs; Deutsch arXiv:1210.7439). **Q2:** yes — apparatus is a
  *constructor*, an approximate physical object; the task is defined over substrate
  attributes, not over the menu. **Q3:** yes — task identity is attribute-relative,
  presentation-independent by construction. **Q4:** yes — serial and parallel composition
  are defined and exact. **Q5:** yes — possibility *is* the counterfactual, defined
  physically (existence of a constructor), not sociologically. **Q6:** bridge — operational
  measurements are approximations to tasks on lab substrates (CT's own intended reading).
  **Q7:** the five CT primitives (see price doc). **Q8:** possibility predicate is law-like;
  which tasks are possible on which substrates is physical fact; substrate/attribute choices
  in a model are state data. **Q9:** mismatch noted — CT objects are categorical/compositional,
  Γ is a flat empirical model; the bridge is exactly the future Γ↔C requirement.
- **Verdict:** strongest candidate found. **But:** its status for F0 is decided by the
  constructor baseline (RESTATED risk) — see below.

### I-4. Event / relation / state-transition specification  — `UNRESOLVED`
- Events presuppose spacetime or process structure; "relation" is too weak to carry
  outcome structure; state-transition specs presuppose states. All collapse into I-1–I-3
  with prices already counted. **Verdict:** no independent candidate.

**Noun verdict:** "intervention" is misleading — it suggests agency and menu. The
physically defensible candidate notion is **task/possible-transformation** (I-3) at the
constructor-theoretic scope. The word may be replaced; the object is what matters.

## Part II — What is influence?

Current Γ is **context-indexed compatible probability data — an empirical model**. The
name "influence" is **not earned**: nothing in the object encodes physical influence,
force, signal, or transformation; it is statistics. Candidates for a deeper object:

### B-1. Transformation/task data  — `UNRESOLVED`
Influence as *which task outcomes can be brought about jointly* — i.e. replacing
probability tables with possible/impossible + probabilistic task data. Price: the CT
primitives plus a statistics layer. **Not built here** (would be a law-adjacent move);
recorded as a future requirement.

### B-2. Response maps on tasks  — `UNRESOLVED`
Probability as a *response functional* on possible tasks (as in operational-realist
readings). Requires a task algebra + response notion; not built.

### B-3. Keep the empirical-model scope, renamed  — `CONSTRUCTED` (declared)
Honest option: Γ stays what it is — an empirical model in the finite ordinary
probability-valued scope — and the name is corrected to match (e.g. "empirical model,"
"contextual influence data" → "context statistics"). The mismatch with compositional
primitives (Q9) is then recorded rather than repaired by fiat.

**Noun verdict:** "influence" is **retracted as a physics claim** and retained only as a
label for context statistics; the deep question (what should Γ be if tasks are primitive)
is a FUTURE REQUIREMENT, not solved here.

## Part III — Access structures: the three ontological options

### PHYS02-A — operational (control)  — `OPERATIONAL`
Exec-01's conclusion stands: specification-relative, cannot be fundamental as-is.

### PHYS02-B — derived `C = Access(P)`  — `UNRESOLVED`
Candidate P's examined: spacetime region structure (Exec-01 P6 price); subsystem
factorization (P5 price); process algebra (supplied); **task-possibility structure
(I-3)** — see constructor baseline. No candidate P survived Q1–Q10 *without* paying one of
the known prices; the honest statement is that the best current `P` is task-possibility
structure, and whether `C = Access(P)` adds anything beyond it is exactly the RESTATED
question.

### PHYS02-C — access/possibility is PRIMITIVE  — the fair hostile test
Candidates M-1..M-5 (see price doc). Headline results:

- **M-1 binary compatibility relation** — `PRIMITIVE-BUT-UNEXPLANATORY`: n(n−1)/2
  arbitrary bits; cannot express higher-order jointness (a pairwise table cannot
  distinguish "a,b,c pairwise compatible with a triple context" from "without"); strictly
  weaker than `C`.
- **M-2 hypergraph of jointly possible sets** — `PRIMITIVE-BUT-UNEXPLANATORY` as bare
  state data: up to 2^n−1 arbitrary bits; isomorphic to arbitrary `C` in new vocabulary.
  **However**, if the hypergraph is *task-possibility data on a substrate* (CT scope), the
  arbitrariness is constrained by composition — the combination is candidate M-3/M-4.
- **M-3 partial composition + M-4 possible/impossible predicate** — `PHYSICAL-CANDIDATE`:
  the only structures found where composition constrains the primitive (not every
  combinatorially-writable table is composition-consistent), giving non-arbitrariness a
  handle. Full assessment in the constructor baseline.
- **M-5 transformation algebra** — `UNRESOLVED`: presupposes state/effect formalism.

## Q-tests summary (applied to survivors)

| test | I-3/M-3/M-4 (task-possibility) | M-1/M-2 (bare tables) |
|---|---|---|
| Q1 observer independence | pass (CT scope) | vacuous (no semantics) |
| Q2 apparatus distinction | pass (constructors ≈ apparatus, tasks over attributes) | fail |
| Q3 representation invariance | pass | pass |
| Q4 composition | defined (serial/parallel) | unavailable |
| Q5 counterfactual | defined (constructor existence) | unavailable |
| Q6 empirical bridge | plausible (approximate constructors) | none beyond restating C |
| Q7 price | 5 CT primitives | 2^n−1 bits |
| Q8 law/state | predicate law-like; substrate/task instance data = state | all state |
| Q9 current-Γ fit | mismatch (compositional vs flat) — recorded | matches trivially |
| Q10 whole-law forecast | Γ↔C linkage is where GRUT content could live | none |

## Terminal-relevant conclusions

1. The only surviving observer-independent candidates are (i) constructor-theoretic
   task-possibility structure, or (ii) bare compatibility tables that are
   `PRIMITIVE-BUT-UNEXPLANATORY`.
2. Whether (i) is new or is exactly constructor theory at this scope is decided in
   `F0_PHYS02_CONSTRUCTOR_BASELINE_01.md`.
3. The Γ↔C coupling requirement is recorded, not built.
