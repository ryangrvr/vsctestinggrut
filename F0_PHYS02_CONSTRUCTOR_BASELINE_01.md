# F0 PHYS-02 — CONSTRUCTOR BASELINE 01
**Status:** campaign artifact. Constructor theory studied **first**, as primary null
comparator, fairly: its purpose is to formulate physical laws through **objective
possible/impossible transformations**, not experimenter menus. Source-verified. Targeted,
not exhaustive (NOT FOUND ≠ DOES NOT EXIST).

## 1. Constructor theory in brief (source-verified)

- Deutsch, *Constructor Theory* (arXiv:1210.7439, 2013): fundamental laws expressed as
  **statements of which tasks are possible and which are impossible**, rather than as
  trajectories evolving from spacetime initial conditions. Intended as exact,
  scalable, and **counterfactual** (a task is possible if a *constructor* — any physical
  system that would perform it — can exist), covering ideal measurements as a special case.
- Deutsch & Marletto, *Constructor theory of information* (arXiv:1405.5563): information
  defined via tasks on substrates (distinctness, copyability, interoperability) — media
  characterized by their possible/impossible tasks.
- Constructor theory of time (Marletto): time emerges as an approximately-required
  substrate concept; the fundamental specifications are **timeless**.
- Constructortheory.org FAQs: possible/impossible statements are **objective physical
  facts**, not statements about what an experimenter can build; constructors are idealized
  physical systems; approximate constructors suffice for physical content.

## 2. CT primitives (as used here; R1-corrected definitions)

| CT primitive | definition (source-faithful, R1) |
|---|---|
| **substrate** | a physical system, characterized by the set of its **attributes** |
| **attribute** | a distinguishable set of physical states of a substrate |
| **task** (R1 corrected) | an abstract specification of a physical transformation as a **finite set of ordered input/output attribute pairs** T = {x₁→y₁, …, xₙ→yₙ} on one or more substrates — NOT the earlier "outputs to produce / outputs to forbid" wording, which is withdrawn |
| **possible task** | ∃ constructor (physical system) that performs T with arbitrarily high accuracy, arbitrarily many times |
| **constructor** | anything that can cause tasks on substrates and remains unchanged on the attribute-level after each cycle (idealized) |
| **serial composition** | perform T₁ then T₂ (defined where substrates chain appropriately) |
| **parallel composition** | perform T₁ and T₂ on the composite substrate M⊕N — **defined only when the composite substrate conditions hold** (see §5, R2) |
| **time** | emergent, not primitive |

## 3. Comparison table (charter §8)

| issue | Constructor theory | F0 candidate (task-possibility access) |
|---|---|---|
| fundamental object | task + possibility predicate on substrates | compatibility/possibility structure over interventions — **candidate: same predicate, projective reading** |
| physical substrate | explicit primitive | **not yet defined in F0** — F0's "context" would need to be re-based on substrates to compare exactly |
| transformation/task | explicit primitive | the F0 "intervention," re-proposed as a task (I-3) |
| possible/impossible predicate | explicit, law-grade | M-4 — proposed primitive |
| counterfactual status | explicit: possibility = existence of a constructor | borrowed wholesale at this scope |
| serial composition | defined | defined (same) |
| parallel composition | defined (independence of substrates) | defined (same) |
| time required? | no (timeless formulation) | no |
| observer dependence | explicitly none | aimed at none |
| state/law distinction | possibility facts are law-like; substrate attribute choices in models are state data | same split available (charter §6) |
| probability required? | no — CT handles probability via information theory on substrates, not as a primitive of the base formalism | F0's current Γ **is** probabilistic (empirical model) — a genuine scope difference, see §4 |
| information price | substrate + attribute + task + predicate + 2 compositions (5 primitives) | at least the same 5 if re-based on CT |
| empirical accessibility | via approximate constructors on lab substrates | via the same route |

## 4. Verdict on F0's task-possibility candidate (M-3/M-4 + I-3) — REVISED BY R2/R3

The original PHYS-02 reduction claimed: "context = set of tasks whose parallel composite
is possible." **That equivalence has not been established and, after the R3 hostile
control, is REFUTED as a general identification.** Two distinct relations must be kept
apart (R2):

- **CT-PARALLEL:** T₁ ∥ T₂ is a well-defined parallel composite task on the composite
  substrate M⊕N, subject to CT's composition law — possible tasks compose, so if T₁ and
  T₂ are possible and the composite substrate exists, the composite is possible.
- **CONTEXT-COMPATIBLE:** {x₁,…,xₙ} ∈ C means the corresponding interventions/tasks
  possess the F0 contextual joint-realizability relation — which may involve alternative
  measurements/transformations on the **same** underlying substrate (exactly the K2
  situation).

These are not automatically the same notion: CT parallel composition is about tasks on
composite substrates; contextual compatibility is about jointly implementable
interventions, possibly on one system.

### R3 — the K2 interface control (decisive, computed exactly)

K2/Specker triangle: three singleton contexts, three pair contexts, **no triple
context**. Under the naive mapping (contexts = possible parallel task-sets, composite
substrates defined as K2's pair contexts presuppose them), **full CT closure forces the
triple**: {T1,T2} possible + {T3} possible + defined composite ⇒ {T1,T2,T3} possible.
K2 has no triple. The exact computation (`f0_phys02_toy.py`, `k2_interface_control`)
finds **12 closure violations, all forcing the triple**.

**Verdict: the direct embedding FAILS.** Escape routes examined and rejected:
1. declare the triple substrate undefined — unavailable, since K2's pair substrates are
   defined and coexist on the same underlying scenario;
2. weaken composition — forbidden (would modify CT to save the reduction);
3. restrict to independent-substrate scope — yields at most a restricted **one-way
   implication** (independent-substrate contexts correspond to possible parallel
   composites), not the general reduction.

**Answer to R2's question "under what conditions does CT-PARALLEL induce
CONTEXT-COMPATIBLE?":** at most a **restricted one-way implication under an explicit
independent-substrate assumption**; no general reduction; the general relation is
**unresolved**. No answer was favored; this one is forced by the control.

### Consequences for the earlier claims (withdrawn)

- "the Exec-01 C-hypergraph, including K2, embeds directly as jointly-possible task
  sets" — **withdrawn**; K2 is exactly the counterexample.
- The prior `F0-PHYS-CONSTRUCTOR-RESTATED` verdict is **withdrawn** (see result doc).

## 4c. What survives

- CT remains the **nearest primitive-possibility framework** found: objective,
  compositional, counterfactual, timeless, with a law-grade possibility predicate.
- The failure is informative: it exposes a **previously hidden interface** —
  CT task possibility and F0 contextual compatibility are related, but not by
  identification. Characterizing that interface is a distinct open problem (recorded as
  the likely next scientific question, R9 — not executed here).

## 5. The stronger CT interface target (FR4 — source-verified)

The Deutsch–Marletto **Constructor Theory of Information** (arXiv:1405.5563; also
published, Phil. Trans. R. Soc. A 2015) already defines, in constructor-theoretic terms:

- **measurable variables / observables** — attributes of a substrate with associated
  **measurers** (constructor tasks that reproduce the attribute with high accuracy); the
  **observable** is the equivalence class of such attributes;
- **information observables** — observables whose attributes are distinguishable by the
  number of distinct copies (bit-like); foundational to CT information theory;
- **superinformation media** — sets of incompatible information observables on a common
  substrate (the CT home of nonclassical information);
- **complementary observables** — and the **derived impossibility theorem**: in a
  superinformation medium, complementary observables **cannot be simultaneously
  measured** (the paper's explicit impossibility proof).

**Consequence for F0-I0 (recorded, not executed):** the right interface target is NOT
`context = CT parallel-composite possibility` (refuted by the K2 control), but rather

> contextual joint compatibility ⟷ existence of a **constructor-theoretic joint
> measurer / compatible-observable structure** on the relevant substrate,

i.e. CT already contains a same-substrate objective measurability/incompatibility notion
(superinformation media, complementary observables) that is a far closer neighbor to F0's
CONTEXT-COMPATIBLE than parallel composition is. **Do NOT claim equivalence** — CT's
impossibility theorem (complementaries never jointly measurable) may be stronger or weaker
than F0's contextual compatibility; that comparison is exactly the I0 campaign's work.

The prior claim that "the only visible non-CT content is the Γ↔C coupling because CT
supplies no possibility/statistics bridge" was **too strong and is withdrawn**.

### R7 — Constructor Theory of Probability (Marletto, arXiv:1507.03287 / Proc. R. Soc. A 472, 20150883) — audited

What it **does** establish (source-verified):
- **Unpredictability** as a theoretical property of substrates/attributes: a substrate is
  unpredictable with respect to an attribute if no possible task can force a particular
  outcome on every execution — i.e. unpredictability is defined through possible/impossible
  tasks, not through probability postulates.
- **Repeated measurements / apparent stochasticity**: deterministic-looking and
  apparently-stochastic behaviors are both modeled via constructors and possible/impossible
  tasks across multiple instances; a formal connection between unpredictability and
  **entropy/information theory** is derived inside CT.
- **Decision-supporting superinformation theories**: a class of theories (including
  quantum and higher theories) characterized abstractly by how unpredictability behaves;
  probabilities emerge as **derived quantities** (decision-supporting weights) within such
  theories, not primitives.

What it **does not** (as far as this audit found):
- It does not provide a bridge from **contextual empirical models** (F0's Γ: context-indexed
  compatible distributions with no-signalling-type constraints) to task-possibility
  structure; its probability notion is defined over **repeated executions of tasks on
  substrates**, not over context families.
- It does not derive Born-type structure for arbitrary contexts, nor the specific
  compatibility/statistics coupling F0 would need.

### Permissible statement (revised novelty forecast)

> **No F0-specific relation between the contextual empirical-model layer and objective
> task-possibility structure has yet been established.** Existing constructor-theoretic
> work on probability (Marletto) defines unpredictability and derived probabilities via
> task possibility, and must be included before deciding whether such a coupling lies
> beyond CT. Additionally, the **upstream interface** — what maps CT task possibility to
> contextual joint compatibility — is itself unresolved (R3: not identity).

Two distinct open relations, in order:
1. **Interface (upstream):** CT task possibility ↔ contextual joint compatibility.
   (R9: likely next scientific question, not executed.)
2. **Coupling (downstream):** that combined structure ↔ contextual statistics Γ.
   (Original Γ↔C question; must wait for the interface.)

No formula for either is authorized.

## 6. F0-I0 null comparators (FR5 — baseline list for the next campaign, NOT executed)

F0-I0 (TASK/CONTEXT INTERFACE) must compare against, at minimum:

- **constructor-theoretic measurers / information observables / superinformation media**
  (Deutsch–Marletto, arXiv:1405.5563) — including the derived impossibility theorem that
  complementary observables cannot be simultaneously measured;
- **quantum joint measurability** (compatibility of POVMs; noise/sharpness dependence);
- **compatibility hypergraphs** — general POVMs can realize genuinely higher-order joint
  measurability structures (beyond pairwise graphs), while projective measurements realize
  a more restricted class (cf. Phys. Rev. Research 2, 043147 — baseline information,
  source: journals.aps.org);
- **effect algebras / compatibility-support mappings**;
- **partial Boolean algebras / commeasurability**;
- **sheaf/contextuality scenarios** (Empirical models; Exec-01 B5).

The Specker triangle (pairwise jointly measurable, not triplewise) is the first hostile
target: I0 asks whether CT's measurer/observable principles reproduce such compatibility
structures, forbid some, or require subsidiary-theory input.

**This is baseline information only. No new interface law or mapping is authorized
here.**

## 8. What this verdict does NOT establish

- That F0 *should* adopt CT; that the interface (relation 1) is impossible or is
  identity; that the Γ-coupling (relation 2) is impossible; that no smaller primitive
  exists (targeted audit: NOT FOUND ≠ DOES NOT EXIST).
- No RESTATED-by-renaming is hidden: the direct reduction was **tested and failed**,
  which is a stronger (and more useful) result than an assumed restatement.

## 9. Sources

- arXiv:1210.7439 (Deutsch, *Constructor Theory*) — verified: tasks, possible/impossible,
  constructors, counterfactual laws, ideal measurements, scalable formulation.
- arXiv:1405.5563 (Deutsch–Marletto, *Constructor theory of information*) — verified
  (also FR4): substrates/attributes; information via possible tasks; **measurers,
  observables, information observables, superinformation media, complementary
  observables, and the impossibility of simultaneous measurement of complementaries**;
- arXiv:1507.03287 / Proc. R. Soc. A 472, 20150883 (Marletto, *Constructor theory of
  probability*) — verified (R7): unpredictability via possible/impossible tasks;
  repeated measurements; apparent stochasticity; decision-supporting superinformation
  theories; probabilities as derived decision weights;
- Phys. Rev. Research 2, 043147 (FR5 baseline): general POVMs realize arbitrary
  joint-measurability structures; projective measurements are more restricted.
- arXiv:1507.03287 / Proc. R. Soc. A 472, 20150883 (Marletto, *Constructor theory of
  probability*) — verified (R7): unpredictability via possible/impossible tasks;
  repeated measurements; apparent stochasticity; decision-supporting superinformation
  theories; probabilities as derived decision weights.
- constructortheory.org and /faqs, and the CT papers (e.g. constructortheory.org PDFs,
  arXiv:1210.7439 §2, ct-life.pdf) — verified (R1): task = finite set of ordered
  input/output attribute pairs; constructors as physical, idealized; approximate
  constructors; parallel composition on composite substrates.
- Marletto, constructor theory of time — timeless fundamental specifications.
