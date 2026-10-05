# F0 PHYS-02 — INFORMATION PRICE 01
**Status:** campaign artifact. Exact counts for the candidate structures of
`F0_PHYS02_PRIMITIVE_CANDIDATES_01.md`, finite n. Purpose: make `primitive` vs
`arbitrary` quantitative. A candidate whose entire content is arbitrary state data is
marked `PRIMITIVE-BUT-UNEXPLANATORY`.

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

## 4. Finite semantic toy (exact arithmetic)

`f0_phys02_toy.py` demonstrates, on 3 tasks {T₁, T₂, T₃}:

1. a **composition-consistent** possibility table (parallel composites of possible tasks
   are possible; the table is forced to close under declared composition);
2. a **composition-inconsistent** table (declares T₁, T₂ possible but T₁∥T₂ impossible) —
   flagged by an exact checker;
3. the information-price count for each representation (pair table: 3 bits; hypergraph:
   4 nontrivial subset decisions; composition-closed tables: fewer free bits than raw —
   counted exactly);
4. the observation that the Exec-01 `C`-hypergraph embeds in the task-possibility reading
   via "context = jointly possible task set" (semantic bridge, no law).

Run: `python3 f0_phys02_toy.py`. **This is semantics only** — no evolution, no transition
law, no fitting.
