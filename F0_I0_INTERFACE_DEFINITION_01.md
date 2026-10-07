# F0 I0 — INTERFACE DEFINITION 01
**Status:** campaign artifact. Defines the candidate interface precisely, prices each
component, states what is CT-native vs constructed/supplied, and attempts the
downward-closure theorem. **No Γ coupling, no dynamics.**

## 1. The interface candidate

Given a finite family of candidate measurement tasks on a declared substrate/type:

```
M = {M_1, …, M_n}
```

(e.g. M_i = "measure the variable X_i of substrate S", each a CT-measurer task per the
baseline), define the candidate contextual complex:

```
C_CT(M) = { ∅ ≠ S ⊆ {1..n} : there exists an appropriate joint measurer for the
            variables indexed by S }
```

**This is a PROPOSED definition, not an established CT construction.** Its components,
priced:

| # | component | CT-native? | price/status |
|---|-----------|-----------|--------------|
| 1 | one physically possible measurement task | yes (CT task) | `CT-NATIVE` |
| 2 | a joint output variable | partially — CT has variables and coarse-graining of attributes; a *joint* variable over several measurer outputs is **constructed for I0** | `CONSTRUCTED` |
| 3 | allowed classical output processing / coarse-graining recovering each M_i outcome | CT has attribute coarse-graining and output information transfer; **recovery-of-measurement-outcomes as classical post-processing is imported from standard measurement theory** | `SUPPLIED` (imported; priced) |
| 4 | consistency under restriction to smaller subsets | imported structure of joint measurability (parent-measurement marginals) | `SUPPLIED` (imported; priced) |
| 5 | representation invariance under output relabeling | F0-A declared move; applies | `REPRESENTATIONAL` |

**Verdict:** the interface definition **mirrors the parent-measurement definition of
quantum joint measurability** (a joint POVM whose outcomes coarse-grain to the parents).
That fact is priced honestly: **if the mapping is standard joint measurability rewritten
in CT language, the terminal is `F0-I0-JOINT-MEASUREMENT-RESTATED`** — acceptable, and
informative (it locates where the GRUT burden does not live).

## 2. Downward-closure theorem (attempted, earned)

**Theorem (of the interface definition).** Let the interface definition (§1) hold for a
family M. If S ∈ C_CT(M) and ∅ ≠ S' ⊆ S, then S' ∈ C_CT(M).

*Proof (exact, from components 2–4).* Suppose S ∈ C_CT(M): a joint measurer J_S exists —
one possible measurement task with joint output variable Y, and for every i ∈ S an allowed
classical coarse-graining f_i of Y's outcome such that processing J_S's output by f_i
reproduces the outcome of measuring M_i. Fix i ∈ S'. Because S' ⊆ S, i ∈ S, so f_i is an
allowed processing of Y recovering M_i's outcome. The same task J_S, with output processed
by f_i for each i ∈ S', is then a single possible measurement task whose outputs recover
each M_i (i ∈ S') outcome — i.e. a joint measurer for the variables indexed by S'. (The
joint output variable Y is unchanged; the coarse-grainings f_i, i ∈ S', are a subset of
the allowed ones; consistency under restriction (component 4) is inherited.) Hence
S' ∈ C_CT(M). ∎

**Classification:** theorem **of the interface definition** (it follows from components
2–4 as declared). It is **not** a new physical prediction: it explains *why* the induced
object is a downward-closed complex — the same marginalization structure that makes joint
measurability complexes simplicial in quantum measurement theory. If the interface
definition were changed (e.g. no classical post-processing allowed), the theorem's
hypotheses would fail; that dependence is part of the price.

**Consequence:** `C_CT(M)` is a downward-closed family of nonempty subsets — an F0-A
context complex (with the empty-context convention of Exec-01/Formulation §4.2). The
interface lands in the right kinematic carrier.

## 3. The three interface levels (charter §5) — assessed

- **I0-A (CT alone):** base CT proves non-simultaneous-measurability for *complementary
  information observables* (baseline §1–2) and *possibility* of measuring fine-grainings.
  Whether these principles **alone** determine the full complex C_CT(M) — especially the
  Specker-type middle regime — is tested in the finite controls. Finding: **no**; base CT
  under-determines the middle regime (see `F0_I0_COMPARATOR_AUDIT_01.md`, level analysis).
- **I0-B (CT + subsidiary theory):** the joint measurer's existence for a given family is
  determined by possibility facts of a subsidiary theory (e.g. quantum measurement theory
  supplies which POVM families have joint parents). CT supplies the objective language
  (task/measurer/variable/observable) and the sharp complementary-impossibility theorem.
- **I0-C (imported operational compatibility):** the interface definition as declared is
  exactly the parent-measurement structure; used at face value the mapping is standard
  joint measurability in CT terms.

## 4. Q-tests on the interface candidate (summary)

Q1 observer independence: pass (constructors, objective). Q2 apparatus distinction: pass
(measurer = physical constructor; the complex is over variables, not menus). Q3
representation invariance: pass (component 5; F0-A moves). Q4 composition: serial output
processing is used (component 3); parallel composition is NOT invoked — the failed
PHYS-02 identification is not re-imported. Q5 counterfactual: possibility of the joint
measurer (CT-style). Q6 empirical bridge: direct (joint measurers are the objective
counterpart of joint measurements). Q7 price: components table §1 — one `SUPPLIED` layer
(classical processing + restriction consistency) is honest. Q8 law/state: which measurers
are possible = subsidiary-theory possibility facts (law-grade within the subsidiary theory;
see the audit artifact). Q9 current-Γ fit: Γ (empirical model) is downstream — untouched
per charter. Q10 forecast: recorded in the result (originality burden location).

## 5. What the interface definition does NOT do

- It does not decide I0-A vs I0-B vs I0-C alone — the comparator audit and finite controls
  do that.
- It does not translate CT statements into POVM language (charter prohibition) — the
  `SUPPLIED` component 3 is declared as imported, not as a CT theorem.
- It does not touch Γ.
