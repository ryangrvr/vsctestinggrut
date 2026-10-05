# F0 I0 — INTERFACE DEFINITION 01 (REPAIRED, CT-NATIVE FIRST)
**Status:** campaign artifact, rebuilt per R4/R5. The source-native interface is now
defined and tested **before** any imported parent-POVM mathematics. **No Γ coupling, no
dynamics.**

## 1. The strongest source-native interface candidate (R4)

A family `{X_i}` of measurable variables (on a declared substrate/type) is
**jointly CT-measurable** iff there exists a **single measurable variable / measurer
structure Z** such that each `X_i` is recovered as a legitimate **CT
coarse-graining/re-labelling of Z** — where coarse-grainings and re-labellings are the
CT-native operations the paper explicitly grants (a measurer of X automatically measures
subsets and coarse-grainings of X via output re-labellings, which are possible classical
computations).

Call the induced complex:

```
C_CT(M) = { ∅ ≠ S ⊆ {1..n} : the variables indexed by S have a common CT
            fine-graining Z (single measurable variable/measurer structure)
            with each X_i a CT coarse-graining of Z }
```

### Component pricing (corrected per R4)

| component | status |
|---|---|
| measurement task (possible task) | CT-NATIVE |
| joint/fine-grained variable Z | CT-NATIVE (variables and their unions are CT objects; whether a *specific* union is a variable/measurable is a possibility fact) |
| coarse-graining/re-labelling recovering each X_i | **CT-NATIVE** (the previous wholesale `SUPPLIED` classification is withdrawn — the paper grants exactly this) |
| consistency under restriction | **CT-NATIVE consequence** of coarse-grainings being actual coarse-grainings of a single variable Z |
| representation invariance | F0-A declared move; applies |

**This corrects the previous claim:** the interface is more CT-native than the original
I0 realized. What remains genuinely open is whether this native construction is
*sufficient* for the generalized joint-measurement hierarchy — see §3.

## 2. The four source questions (R4) — answered from sources

1. **Is the construction explicitly CT-native?** Yes in its building blocks: the paper
   grants that a measurer of X measures subsets and coarse-grainings of X by re-labelling,
   and that those re-labellings are possible classical computations. The *composite*
   definition (common fine-graining Z for a whole family) is a natural assembly of these
   granted operations — its components are native; the assembly is `CONSTRUCTED` (defined
   for I0 from native operations), not a quoted CT theorem.
2. **Is it sufficient for simultaneous measurement in the paper's sense?** Yes at the
   sharp/fine-graining scope: if all X_i are coarse-grainings of one variable Z and Z is
   measurable, then measuring Z and re-labelling gives a single measurer measuring all
   X_i — which is exactly the paper's notion of simultaneous measurement.
3. **Is it necessary?** **Not established.** The paper does not state that every
   simultaneous measurement must arise via a common fine-graining variable; a joint
   measurer could conceivably exist without the family being coarse-grainings of one
   variable. This necessity question is left `UNRESOLVED` — deciding it would require
   either a CT theorem or a counterexample construction, neither of which is in the
   audited paper.
4. **What additional assumptions are needed?** To get from the native construction to the
   full generalized joint-measurement hierarchy (unsharp/partial compatibility, the
   K2/Specker middle regime), the paper's native machinery (sharp variables,
   coarse-grainings, Principle VIII consistency) is **not obviously enough** — see §3.

## 3. Sharp common refinement vs generalized joint measurement (R5) — the decisive test

**The sharp/information-observable sector:** the native common-fine-graining construction
lives naturally in the sharp/fine-graining scope — variables that are coarse-grainings of
one another share one underlying variable. In this sector the interface behaves like the
known restricted structures: **pairwise compatibility via common refinements extends
strongly** (if X_1,X_2 share a refinement Z_12 and X_1,X_3 share Z_13, nothing in base CT
guarantees a *common* Z for all three — but neither does base CT obviously forbid it; what
base CT provably gives is: a common fine-graining *when it exists* yields simultaneous
measurement, and coarse-grainings of a measurable variable are simultaneously measurable).

**The generalized/Specker question in source-native terms:**

> Can CT's own measurement-of-non-sharp-variables machinery (§6(a), Principle VIII)
> support pairwise joint measurability of non-sharp variables **without** a global joint
> measurer?

**Answer from sources: `UNRESOLVED` — the audited paper does not decide it.** What the
paper provides: measurers for non-sharp inputs; the consistency principle (Principle VIII)
constraining them; observables for non-sharp inputs. What it does **not** provide (as far
as this audit found): an analysis of *families* of non-sharp variables with partial
(pairwise but not global) simultaneous measurability. Neither a CT prohibition nor a CT
construction of the K2/Specker pattern is found. **We do not import the POVM parent object
as the answer.**

**If a quantum subsidiary theory is ultimately required to decide these facts, the
dependency is classified `SUBSIDIARY-THEORY-REQUIRED`** (for that sector) — with the
explicit caveat that this is a *classification of where the facts come from*, not a proof
that CT forbids them (R8: no novelty claim).

## 4. Comparison with the imported (parent-POVM) definition — precise overlap

- The CT-native construction and the quantum parent-measurement definition **overlap in
  the sharp/fine-graining scope**: a common fine-graining variable with allowed
  re-labellings is the exact analogue of a parent measurement whose outcomes coarse-grain
  to the parents.
- They may **diverge in the generalized scope**: quantum parent POVMs support partial/
  unsharp joint measurability with no common underlying sharp variable; whether the CT
  non-sharp machinery supports an analogue is exactly the §3 unresolved question.
- Therefore the previous wholesale "the interface is standard parent-measurement
  mathematics translated into CT language" claim is **withdrawn as too broad**: the sharp
  scope is RESTATED (overlap precise as above); the generalized scope is **UNRESOLVED**
  pending either CT-internal analysis or subsidiary input.

## 5. Downward closure — re-derived for the native construction

**Theorem (of the native construction).** If the variables indexed by S share a common CT
fine-graining Z (each X_i a coarse-graining of Z), then every nonempty S′ ⊆ S does too —
the same Z works, since coarse-graining is transitive (a coarse-graining of a
coarse-graining of Z is a coarse-graining of Z).

*Classification:* theorem of the **native** construction — grounded directly in the
paper's granted coarse-graining/re-labelling operations, not in imported structure. It
explains why the induced object is a downward-closed complex, and mechanically it is the
same closure structure as before, now with native justification.

## 6. Q-tests (summary)

Q1 pass (constructors). Q2 pass (measurers are physical; variables, not menus). Q3 pass
(re-labelling invariance is native). Q4 composition: re-labelling chain used; parallel
composition not invoked. Q5 counterfactual: possibility of the measurer/fine-graining
variable. Q6 bridge: direct. Q7 price: components are now largely native (corrected);
remaining price: the possibility facts about which fine-grainings/variables exist. Q8
law/state: which variables are measurable — possibility facts (subsidiary or CT-theorem
level); the coarse-graining operations — native. Q9 Γ: untouched. Q10: forecast in result.
