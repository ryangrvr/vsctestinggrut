# F0 PHYS-02 — INFORMATION PRICE 01 (REVISED per R5)
**Status:** campaign artifact (interface repair). **Withdrawn claims (R5):** "arbitrary
n=3 context structure = 7 independent bits" (that counts an arbitrary Boolean table,
which is a *different object* from the F0-A downward-closed complex) and "composition
reduces the all-possible instance to 0 free decisions" (composition constrains composite
possibility *conditionally*; it does not force primitive singleton tasks to be
possible — the earlier count wrongly counted present singletons as "forced").

## 1. Price table (finite n=3) — objects kept DISTINCT, no cross-object comparison

| object | exact free decisions at n=3 | status |
|---|---|---|
| **arbitrary Boolean subset table** (one bit per nonempty subset, no closure) | **7 free bits** (2^7 = 128 tables, exact) | not the F0-A object; shown for contrast only |
| **F0-A context complex** (downward-closed family on 3 labeled vertices, **frozen F0-A convention**: nonempty contexts, closure through nonempty subcontexts, coverage not required) | **exactly 19 families if the empty family is allowed; 18 if a nonempty-family condition were imposed** (both enumerated exactly by the program). The earlier 'exactly 20' claim was the full-Boolean-lattice/Dedekind count (empty face included) imported without matching conventions — **withdrawn (FR1)**. Decisions remain coupled by closure: a present pair forces its singleton subcontexts | the actual F0-A object |
| **CT task-possibility structure** (possibility values on a declared task algebra with serial/parallel closure) | **3 genuinely free singleton decisions** (T1, T2, T3 possible or not — composition does not force them), plus conditional constraints on composites once the substrate model is fixed; further free decisions depend on which composite substrates are defined | composition constrains composites conditionally; does NOT fix singletons |
| **CT-PARALLEL with all composite substrates defined** (the strongest closure regime) | 3 free singleton bits + forced closure of all composites | this is the regime in which K2 cannot be represented (see interface control) |

## 2. The exact enumeration (R5, no artificial number)

The downward-closed families on 3 labeled vertices were **enumerated exactly by the
program** (`f0_phys02_toy.py::prices_n3`) **under the frozen F0-A convention** (nonempty
contexts, closure through nonempty subcontexts, coverage not required): the count is
computed, not asserted. **FR1 result:** 19 (empty family allowed — the frozen definition
does not explicitly exclude it) / 18 (if a nonempty-family condition were added). The
previously reported 20 was the Dedekind number for the *full* Boolean-lattice convention
(empty face included) and is withdrawn. Where a principled finite information measure for
the CT task algebra is not available (it depends on the declared task set and substrate
model), **partial counts are reported rather than an artificial exact number**, per the
ruling. The convention question (allow or exclude the empty family) is flagged for a
future numbered repair if desired.

## 3. What composition does and does not constrain (corrected)

- Composition **does** constrain: conditional on constituents being possible and their
  composite substrate being defined, the composite must be possible; serial closure
  likewise. Violations are exactly detectable (toy controls R4-1..R4-neg).
- Composition **does not** force: primitive singleton tasks to be possible (those remain
  free model inputs); which composite substrates exist (explicit model input,
  `substrate_ok` — not silently set-union).
- Therefore: composition supplies **nontrivial structure** (real constraint content),
  but the earlier claim that it determines the instance wholesale is retracted.

## 4. Law/state placement (R6-corrected)

| item | classification (revised) |
|---|---|
| possibility/impossibility of a task on a substrate type | **law / subsidiary-theory content** (CT's core claim: laws are expressed as possible/imposable task statements — NOT state data; the earlier "solution/state" classification was backwards and is withdrawn) |
| actual substrate state / attribute instantiation | state/solution data |
| task definition (the specification object T = {x→y}) | representational/specification object |
| actual occurrence of a task (a constructor performing it) | history/instance data |
| which composite substrates are defined in a model | model input (declared) |

## 5. Toy controls (exact, all passing)

`f0_phys02_toy.py`: R4-1 pair-from-singletons ✓; R4-2 triple-from-pair+singleton ✓;
R4-3 undefined-substrate (no closure conclusion) ✓; R4-neg missing-pair flagged ✓;
R3 K2 interface control: full CT closure violated — triple forced, embedding FAILS
(12 violations, all forcing the triple).

## 1. Price table (finite n interventions/tasks)

| candidate | object | arbitrary information required (exact) | law content | classification |
|---|---|---|---|---|
| M-1 binary compatibility relation `~` | symmetric relation on X | ⌈n(n−1)/2⌉ bits, **all arbitrary** | none | `PRIMITIVE-BUT-UNEXPLANATORY` (also strictly weaker than C: no higher-order jointness) |
| M-2 compatibility hypergraph = arbitrary C | family of subsets | up to 2^n − n − 1 bits (which subsets are jointly possible), **all arbitrary** | none | `PRIMITIVE-BUT-UNEXPLANATORY` (isomorphic to arbitrary C in new vocabulary) |
| M-2′ same, task-possibility reading | hypergraph constrained by composition | ≤ 2^n bits raw, but **composition reduces the admissible set** (see §2) | composition constraint | candidate |
| M-3 partial composition law | partial monoid structure on tasks | number of composites declared defined/undefined: for n generators, a composition table of size O(n²) at depth 1 (plus associativity constraints) | strong (constrains what can coexist) | `PHYSICAL-CANDIDATE` |
| M-4 possible/impossible predicate on tasks | predicate P(T) ∈ {0,1} over task space | unconstrained: 2^(#tasks) bits; **constrained by composition**: serial/parallel composition forces closure (if T₁,T₂ possible then T₁;T₂ and T₁∥T₂ possible) | strong | `PHYSICAL-CANDIDATE` |
| M-5 transformation algebra | full algebra (states/effects/combs) | the entire operational formalism | — | `UNRESOLVED` (price = everything Exec-01 flagged as supplied) |
| CT package (substrate, attribute, task, possibility, ×2 composition) | 5 primitives | finite per-model instance data + universal possibility facts | predicate = law; substrate/attribute instance choices = state | `PHYSICAL-CANDIDATE` (RESTATED at tested scope — constructor baseline) |

## 2. Non-arbitrariness: where composition bites

The decisive question: **does the structure constrain its own instance data?**

- **M-1/M-2:** no. Every bit is free. Any hypergraph is as good as any other; the object
  explains nothing — it *is* the phenomenon, restated as data. Hence
  `PRIMITIVE-BUT-UNEXPLANATORY`.
- **M-3/M-4 (task-possibility):** yes, partially. Closure under serial/parallel composition
  forces the possible-task set to be a **composition-closed** family — a genuine
  constraint that a random compatibility table will generally violate. Example (finite
  semantic check): declaring {T₁} possible, {T₂} possible, but T₁∥T₂ impossible is
  *inconsistent* with the parallel-composition law; a bare hypergraph has no such
  inconsistency notion. This is exactly what "composition constrains the primitive" means,
  and it is why M-3/M-4 are candidates while M-1/M-2 are not.
- **Cost of that constraint:** the 5 CT primitives (substrate, attribute, task,
  possibility, compositions) — paid explicitly, not hidden (constructor baseline).

## 3. The law/state split (charter §6) applied

| possible placement of an access structure | content | consequence |
|---|---|---|
| universal law | the possibility predicate + composition (same in every world) | small, constraining — the CT reading |
| solution/state | which tasks exist on which substrates; instance hypergraph | varies by world; NOT a failure to derive — a theory need not derive all state data |
| boundary/initial | selection of the realized instance | same principle as GR initial data |
| representational | the written hypergraph/pair-table forms | `REPRESENTATIONAL` (Exec-01 moves) |

**Principle recorded:** failure to derive the exact realized `C` is **not** a failure; the
burden is a small universal law constraining admissible `C` — and that law is F0-B, out of
scope. PHYS-02's finding: what the future law would act ON is (at the tested scope) a
task-possibility structure with instance data.

## 4. Legacy sections (superseded, retained for audit trail)

The following sections date from the pre-repair version. Where they conflict with the
revised sections above, **the revised sections govern**.

### 4a. Original candidate price table (superseded by the revised table above)

| candidate | object | arbitrary information required (exact) | law content | classification |
|---|---|---|---|---|
| M-1 binary compatibility relation `~` | symmetric relation on X | ⌈n(n−1)/2⌉ bits, **all arbitrary** | none | `PRIMITIVE-BUT-UNEXPLANATORY` (also strictly weaker than C: no higher-order jointness) |
| M-2 compatibility hypergraph = arbitrary C | family of subsets | 2^n − n − 1 nontrivial decisions **if only maximal subsets counted**; withdrawn as a count for the F0-A object (coupled by closure) | none | `PRIMITIVE-BUT-UNEXPLANATORY` |
| M-2′ same, task-possibility reading | hypergraph constrained by composition | conditional constraints only (see revised §1) | composition constraint | candidate |
| M-3 partial composition law | partial monoid structure on tasks | composition table O(n²) at depth 1 + associativity | strong | `PHYSICAL-CANDIDATE` |
| M-4 possible/impossible predicate on tasks | predicate over task space | constrained by composition, conditionally (revised) | strong | `PHYSICAL-CANDIDATE` |
| M-5 transformation algebra | full algebra | the entire operational formalism | — | `UNRESOLVED` |
| CT package | 5 primitives | see revised table | predicate = **law** (R6); substrate/attribute instantiation = state | see revised verdict |

### 4b. Original non-arbitrariness section (superseded; kept for the correct parts)

- **M-1/M-2:** every bit free — no explanatory power. `PRIMITIVE-BUT-UNEXPLANATORY`.
  (Still valid.)
- **M-3/M-4:** composition closes the possible-task set — genuine constraint
  (still valid), but **conditional**: it does not force singletons possible (corrected).
- Cost: the 5 CT primitives, paid explicitly.

### 4c. Original law/state split (REVISED — see revised §4; the original placed
"which tasks exist on which substrates" under solution/state, which conflated
possibility facts (law) with instantiation (state))

| placement | consequence |
|---|---|
| universal law | possibility predicate + composition (CT reading) |
| solution/state | actual substrate attribute instantiation; occurrence history |
| boundary/initial | selection of realized instance |
| representational | written forms |

**Principle (unchanged):** failure to derive the exact realized `C` is **not** a failure;
the burden is a small universal law constraining admissible `C` — and that law is F0-B,
out of scope.

### 4d. Original toy description (SUPERSEDED — the old toy's §4 claim 4, "the Exec-01
C-hypergraph embeds in the task-possibility reading via context = jointly possible task
set", is WITHDRAWN; the K2 control refutes the direct embedding. The repaired toy is the
interface version described in revised §5.)

Run: `python3 f0_phys02_toy.py`. **This is semantics only** — no evolution, no transition
law, no fitting.
