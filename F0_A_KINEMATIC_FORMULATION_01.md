# F0-A — KINEMATIC FORMULATION 01 (the finite object, made precise)
**Status:** campaign artifact (`F0_EXECUTION_01_CHARTER.md`). All objects here are finite,
explicitly declared, and validator-checked where indicated. No physical interpretation is
assigned to any object at this level; no transition is classified as allowed or forbidden.
**Parent:** frozen charter `F0_CHARTER_02_REPAIRED.md` @ `bef8b9480c9f7569c70837c6ee5c4776fc2e0f3c`.

## 1. Overview

The kinematic object is the tuple

```
K = (X, {O_x}, C, E, Γ, ≈)
```

defined in §§2–7 below. Section 8 defines composition/gluing. Everything is finite in the
declared scope. **The validator (`f0_kinematic_validator.py`) is the executable check of
this document**: every testable clause cites a validator test.

## 2. Primitive intervention labels

- A finite set `X = {x_1, …, x_n}`, `n ≥ 1`.
- The `x_i` are **labels only**: no outcome structure, no physical meaning, no
  compositional structure, no temporal order. Two interventions are equal iff their labels
  are equal.
- No physical meaning is assigned yet (owner authorization: this is an F0-PHYS question,
  answered — negatively or positively — in `F0_PHYSICALITY_OF_ACCESS_01.md`).

## 3. Outcome alphabets

- For each `x ∈ X`, a finite set `O_x` with `|O_x| ≥ 1`. (The trivial one-point alphabet is
  permitted: an intervention with no discriminating outcome.)
- The joint outcome space of a context `C ⊆ X` is `O_C = ∏_{x∈C} O_x` (finite, since each
  factor is finite and `C` is finite).

## 4. Context structure

### 4.1 Definition (canonical)

`C` is a **finite downward-closed family of subsets of `X`**: if `C ∈ C` and
`C' ⊆ C` then `C' ∈ C`. Equivalently, `C` is an abstract simplicial complex on vertex set
`X`, where simplices = contexts.

**Convention note (required by the authorization):** the family-of-subsets presentation is
canonical in this campaign. The hypergraph presentation (§4.4) is the equivalent dual used
for maximum contexts; where a source in the baseline audit uses the hypergraph convention,
the audit states which convention it uses.

### 4.2 What is NOT required

`C` need not cover `X` (a label may appear in no context); `C` need not be connected; the
empty set MAY be included by convention — we **exclude** it (contexts are nonempty) and
record this as a declared choice: with the empty context excluded, downward closure starts
from singletons. (Validator test `test_downward_closure` asserts exactly this convention.)

### 4.3 Vocabulary (distinct roles)

- **primitive intervention label:** an element of `X`. Not a context.
- **context:** an element of `C` (any jointly-admissible set). Declared data.
- **maximal context:** an element `C ∈ C` such that no `C' ∈ C` with `C ⊊ C'`.
- **overlap:** for contexts `C, C' ∈ C`, the intersection `C ∩ C'` **when it is itself a
  context** (which downward closure guarantees if both are contexts and `C ∩ C'` is
  nonempty; overlaps are `⊥` (none) when the intersection is empty). Overlap of a family
  `F ⊆ C` is defined analogously. Only nonempty intersections are usable overlaps, since
  the empty set is not a context (§4.2).

### 4.4 Hypergraph formulation

A **compatibility hypergraph** `H = (X, M)` with edge set `M` = the set of maximal contexts.
The induced family is `↓M = { C ⊆ m : m ∈ M, C ≠ ∅ }`. The two presentations are equivalent:

### 4.5 Equivalence of the two presentations (derived)

- From `C` (downward-closed): take `M = Max(C)`; then `C = ↓M` (every element of `C` is
  contained in some maximal element, by finiteness).
- From `H`: `↓M` is downward-closed by construction, and `Max(↓M) = M` provided `M` is
  an **antichain** (no edge contains another) — so the hypergraph data must satisfy the
  antichain condition to represent the same objects. The correspondence
  `C ↦ (X, Max(C))` and `(X, antichain M) ↦ ↓M` is a bijection between downward-closed
  nonempty families on `X` and antichains on `X`. This is standard and elementary; the
  validator confirms it on all four test suites (`test_hypergraph_roundtrip`).

### 4.6 Maximal contexts and overlaps, operationally

`Max(C)` is extracted by inclusion test (validator: `test_maximal_contexts`); overlaps are
computed by intersection + membership check (validator: `test_overlaps`). Maximal contexts
are **not** additional data — they are a function of `C`.

## 5. Event presheaf

### 5.1 Events

For each context `C ∈ C`, an **event set** `E(C)` — the jointly admissible
outcome-structure over that context. In the first (classical, distributional) scope
declared in §6, we take the **global-section presentation**:

```
E(C) = ∏_{x∈C} O_x   (the joint outcome space of §3)
```

and for `C' ⊆ C` the **restriction map** `E(C) → E(C')` is coordinate projection
`r_{C,C'}` (delete the coordinates outside `C'`). Then `r_{C',C''} ∘ r_{C,C'} =
r_{C,C''}` and `r_{C,C} = id`: the family `{E(C), r}` is a presheaf on the poset
`C` (ordered by inclusion). This is the standard event presheaf of the sheaf-theoretic
contextuality machinery; here it is **defined, with the projection restriction maps
declared**, and the functoriality identity is validator-checked
(`test_presheaf_functoriality`).

### 5.2 Generality note (declared scope)

The projection restriction map is the classical/reproducible scope. Other scopes (e.g.
events carrying only marginal *existence* data, or quantum events where the restriction
forgets measurement statistics of non-reproducible observables) are **not** defined here;
they would be a separate declared extension. This is recorded in
`F0_FUTURE_LAW_REQUIREMENTS_01.md` as a scope condition any future law must state.

### 5.3 **Γ is not the presheaf.**

- `E` (the presheaf) says **what the outcomes of a jointly admissible intervention set
  are**: the value/variable structure.
- `Γ` says **what influence data the current structure carries**: in the declared
  probabilistic scope, a family of distributions on the `E(C)`.
- They are different mathematical types: `E` is a (pre)sheaf of sets on `C`; `Γ` (next
  section) is an element of a convex product of probability simplices over `C`. Confusing
  them would smuggle statistics into kinematics; the distinction is therefore stated here
  and enforced in the validator's type checks (distributions are validated against `E`,
  never identified with it).

## 6. Influence model (first probabilistic realization)

### 6.1 Definition

```
Γ = { p_C }_{C ∈ C},    p_C ∈ Δ(E(C)) = probability distributions on E(C)
```

subject to exactly three conditions:

1. **normalization:** `Σ_{s ∈ E(C)} p_C(s) = 1` for all `C ∈ C`;
2. **positivity:** `p_C(s) ≥ 0` for all `C, s`;
3. **restriction/overlap compatibility (canonical name: overlap compatibility /
   no-disturbance):** for `C' ⊆ C`,
   `p_C ↓ E(C') = p_{C'}`, i.e. `p_{C'}(t) = Σ_{s ∈ E(C): s|C' = t} p_C(s)`.

### 6.2 Naming and status

The name for condition 3 is **overlap compatibility**, equivalently **no-disturbance**. In
a Bell-type scenario (the four-cycle K1) where contexts overlap in a single intervention,
condition 3 reduces to the usual **no-signalling** condition; that is a specialization of
the same condition, stated where the overlap structure has singleton intersections.
**Neither name is fundamental causality**: this is a consistency condition on declared
distribution data inside the kinematic object, a `REPRESENTATIONAL` naming choice
(ledger L9). Nothing here asserts a causal mechanism.

### 6.3 Γ as declared data

`Γ` is an **input** to the kinematic object, not derived from `C`. Whether a proposed `Γ`
satisfies the three conditions is mechanically checkable (validator:
`test_gamma_wellformed`, `test_overlap_compatibility`); whether the influences *could have
been otherwise* is not an F0-A question.

## 7. Representation equivalence

`≈` is generated by the following four declared moves (and nothing else — no deeper
equivalence is assumed without proof):

1. **relabelling interventions:** a bijection `σ: X → X` applied consistently to `X`, `C`,
   `E`, `Γ` (validator: `test_relabel_invariance`);
2. **relabelling outcomes:** for each `x`, a bijection `τ_x: O_x → O_x`, applied
   consistently to `E` and `Γ` (validator: same test);
3. **hypergraph isomorphism:** the relabelling moves restricted to the dual presentation
   (§4.4–4.5) — nothing additional beyond 1–2 (the two coincide on antichain data;
   validator: `test_hypergraph_roundtrip`);
4. **redundant presentation:** a context or outcome that duplicates an existing one and
   adds no distinct restriction data may be removed without changing the equivalence class.
   Formally: `C ≈ C ∪ {m}` if `m = m_1 ∪ m_2` (composition, §8) — this is the only
   redundancy rule declared here, and it is stated at the level of *presentations*, not
   *objects*: it changes the written family, not the object up to `≈`.

Anything else (e.g. identification of interventions believed to be "physically the same",
coarse-graining of alphabets, splitting of an intervention into two) is **not** an
equivalence: it changes the object. That asymmetry is deliberate and is the subject of
hostile test P3 (`F0_PHYSICALITY_OF_ACCESS_01.md`).

## 8. Composition / gluing

### 8.1 Mathematical gluing of descriptions

Given `C_1, C_2 ∈ C` with a shared **context** `O = C_1 ∩ C_2` (a genuine overlap per
§4.3), the **glued set** is `C_1 ∪ C_2`. `C_1 ∪ C_2` is a set; it is a **new context** of
the family only if it is already in `C` or is explicitly added by a declared act of
extension. Given compatible distributions `p_{C_1}, p_{C_2}` (they agree on the overlap by
condition 3) with **exact** overlap data (they determine the same marginal on `O`), a glued
distribution `p_{C_1 ∪ C_2}` may or may not exist extending both — this is the classical
gluing/extension problem (known: Vorob'ev / Keller theorems in the sheaf literature; see
`F0_PHYS_BASELINE_AUDIT_01.md`). F0-A only records when extension data was given and
whether extension is possible; it does **not** assert that a glued context or glued
distribution exists by default. (Validator: `test_gluing` checks agreement-on-overlap and
reports extension as data, not as permission.)

### 8.2 Gluing ≠ physical joint accessibility

The separation is explicit: **mathematical gluing is an operation on descriptions; physical
joint accessibility would be the fact that the glued set of interventions can be jointly
realized.** F0-A never grants the latter. Adding `C_1 ∪ C_2` to `C` — or declaring that
agreement on an overlap makes the union jointly realizable — is an **access-transition
matter (`R_Gamma`), explicitly prohibited in this campaign**; it is recorded as a future-law
requirement in `F0_FUTURE_LAW_REQUIREMENTS_01.md` (requirement: gluing compatibility; see
ledger L12). Within this campaign, a glued set added to `C` appears only as declared
*test data*, and the validator treats such additions as ordinary declared context data.

## 9. Validator coverage map

| Formulation clause | validator test |
|---|---|
| §4.1 downward closure (with the §4.2 empty-set convention) | `test_downward_closure` |
| §4.5 family ↔ antichain bijection | `test_hypergraph_roundtrip` |
| §4.6 maximal contexts, overlaps | `test_maximal_contexts`, `test_overlaps` |
| §5.1 presheaf functoriality | `test_presheaf_functoriality` |
| §6.1 normalization, positivity, overlap compatibility | `test_gamma_wellformed`, `test_overlap_compatibility` |
| §7 moves 1–2 (and 3 via §4.5) | `test_relabel_invariance`, `test_hypergraph_roundtrip` |
| §8.1 agreement-on-overlap / extension reporting | `test_gluing` |
| §4 suites K0–K3 | `test_suites_k0_k3` |

## 10. Unresolved kinematic ambiguities (deliberate, recorded)

- Whether the empty context should be included (declared excluded here; a future law must
  state its convention).
- Whether further equivalence moves (coarse-graining, intervention-identification) should
  ever be admissible — deferred to F0-PHYS/hostile tests and left `UNRESOLVED`.
- Non-distributional scopes for `E` (§5.2) — deferred, not defined.
- Whether a *canonical* maximal-context presentation exists for all purposes (we use the
  family convention canonically; the dual is equivalent data, §4.5).
