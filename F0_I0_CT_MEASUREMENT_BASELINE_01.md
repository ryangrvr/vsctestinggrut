# F0 I0 — CT MEASUREMENT BASELINE 01
**Status:** campaign artifact, source-faithful audit of Deutsch & Marletto, *Constructor
Theory of Information*, arXiv:1405.5563 (also Phil. Trans. R. Soc. A 373, 20140226 (2015);
PMC4309123). Definitions reproduced from the paper's own terms; no premature POVM
translation. Targeted, not exhaustive (NOT FOUND ≠ DOES NOT EXIST).

## 1. CT measurement-layer definitions (source-faithful)

| term | CT definition (source-verified) |
|---|---|
| **variable** | a set of attributes {X_j} of a substrate S such that: at all times, S has exactly one of the X_j; each task with T(X_j) as output is possible; and for each pair (j, j'), the tasks {X_j→X_j, X_j'→X_j'} are possible. A variable is the CT analogue of a "measurable quantity." |
| **distinguishability** | attributes x, y are distinguishable if the task x→y (or the reverse) is possible — a substrate property, defined without observers. |
| **measurable variable** | a variable whose attributes are pairwise distinguishable (that is all; measurability is grounded in possible tasks on the substrate). |
| **measurer** | a constructor that, when presented with a substrate S in any attribute X_j of a variable X = {X_j}, outputs another substrate that reliably carries the information "S had X_j" — the task {X_j → X'_j} over all j is possible, where the X'_j are distinguishable attributes of the output substrate. |
| **observable** | the equivalence class of a measurable variable under (i) permutations of the attribute set and (ii) coarse-graining (lumping attributes together). An observable is what multiple measurable variables share. |
| **information observable** | an observable whose attributes X_j are distinguishable by the number of copies of S with X_j: two substrates are distinguishable by a task possible on their disjoint union — bit-likeness defined without classicality assumptions. |
| **superinformation medium** | a medium that has **two or more incompatible information observables** — the CT home of nonclassical information media (quantum media are the canonical instance). |
| **complementary observables** | two observables of a medium are complementary if every information observable compatible with (i.e., fine-graining of) one is incompatible with the other. |
| **simultaneous measurement** | a single measurer that measures all the observables in a set — equivalently, the observables' variables must be jointly measurable by one task. |
| **coarsening / relabeling** | observables are coarse-grainings/permutations of measurable variables; "measurement" of a coarse-grained observable is achieved by measuring a finer variable and processing the output. |

**Key CT theorem used in PHYS-02/here (source-verified):** *in a superinformation medium,
complementary observables cannot be simultaneously measured* — i.e. for complementary
information observables O₁, O₂, no measurer exists that measures both. This is an
impossibility statement about **constructors** (objective), not about observers' knowledge.

## 2. The two distinct "cannot" statements (kept separate per charter §3)

| statement | status in CT |
|---|---|
| **cannot simultaneously have sharp values** | expressible via attributes/variables of one substrate (the substrate has exactly one attribute at a time); CT does not, at base, assign "sharp values" to non-instantiated variables of a substrate — there is no hidden-variable postulate. Not a proven CT impossibility theorem in the same form. |
| **cannot be simultaneously measured** | **proven** for complementary information observables in superinformation media (existence of a joint measurer would contradict the superinformation incompatibility structure). |

**Scope warning:** the proven theorem concerns *complementary information observables in
superinformation media*. It does NOT establish the general joint-measurability hierarchy
of quantum measurement theory (arbitrary POVMs, partial compatibility, noise-dependence).
What CT says about non-complementary, partially-compatible pairs — and about triples — is
**not** fixed by that theorem.

## 3. What CT does NOT supply at base (gaps relevant to I0)

- **No notion of "unsharp" or "noisy" measurement:** CT measurers are characterized by
  reliability (possible/error-free at the attribute level); there is no base-CT calculus of
  partial joint measurability, measurement strength, or disturbance. Whether generalized
  measurements enter CT only through a subsidiary theory's possibility facts is exactly
  I0's subsidiary-theory question.
- **No general theory of partial compatibility:** base CT proves impossibility for
  complementary observables and possibility for compatible (fine-graining-related)
  observables; the *intermediate* regime (pairwise but not triplewise) is not addressed by
  the information-paper theorems audited here.
- **Joint measurer:** the concept is *implicit* in "simultaneous measurement" (a single
  measurer measuring several observables) but the paper does not define a joint-measurer
  calculus with the classical-processing/coarse-graining structure standard in quantum
  joint measurability. Whether it is already present in CT or must be constructed for I0
  is recorded in the interface definition artifact.

## 4. Sources

- arXiv:1405.5563 (Deutsch & Marletto, *Constructor theory of information*) — verified:
  variables, measurers, observables, information observables, superinformation media,
  complementary observables, the non-simultaneous-measurement impossibility, coarse-graining.
- PMC4309123 (published version, Phil. Trans. R. Soc. A 373, 20140226) — same content,
  published text.
- The PHYS-02 baseline (CT core, arXiv:1210.7439) for substrate/attribute/task/constructor
  definitions — inherited, unchanged.
