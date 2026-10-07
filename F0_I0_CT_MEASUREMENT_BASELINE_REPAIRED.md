# F0 I0 — CT MEASUREMENT BASELINE 01 (REPAIRED, SOURCE-FAITHFUL)
**Status:** campaign artifact, REBUILT per the owner/reviewer ruling (R1–R3, R7). Re-audit
of Deutsch & Marletto, *Constructor theory of information*, arXiv:1405.5563; **Proc. R.
Soc. A 471, 20140540 (2015); DOI 10.1098/rspa.2014.0540** (R7-corrected citation). The
previous version's misdefinitions are withdrawn (see §5). Targeted, not exhaustive.

## 1. Source-faithful CT measurement-layer definitions (R1)

| term | source-faithful definition |
|---|---|
| **physical variable** (R1 corrected) | a set of **mutually disjoint attributes** of a substrate. Nothing more — distinguishability, measurability, and computation are NOT built into the definition of variable. (The previous version's formulation — "at all times S has exactly one X_j; each task with output T(X_j) is possible; each pair of tasks is possible" — is withdrawn as over-strong.) |
| **distinguishability** (R1 corrected) | task-based, at variable level: a variable X = {X_j} is **distinguishable** when a possible task maps its alternatives X_j to distinguishable records (distinguishable attributes of an output information medium). Attribute-pair task possibility is the prerequisite notion, not the definition of variable distinguishability. |
| **measurable variable / measurer** (R1 corrected) | a variable X is **measurable** when a possible task transfers information about which attribute of X the substrate has onto an output information medium. A **measurer** is a constructor capable of performing that measurement task for a specified output variable, labelling, and receptive state (the paper's §5 / Eq. (5.2) structure). |
| **observable** (R1 corrected — prior definition WITHDRAWN) | NOT "an equivalence class under permutations/coarse-grainings." Source-native: via the **consistency-of-measurement principle (Principle VIII)**, for a measurable variable X there is a **unique variable Z associated with all measurers of X**; an **observable is that uniquely associated variable** (with the truthfulness property for sharp outputs). Observables are defined through measurers, not through an equivalence-class construction. |
| **information observable** (R1 corrected) | an **observable that is also an information variable** (attributes distinguishable by number of copies / by a task on disjoint unions). |
| **superinformation medium** (R1 corrected) | an **information medium with at least two information observables whose attributes are mutually disjoint and whose union is not an information observable** — the exact set-level definition. |
| **complementary observables** | observables such that every information observable that is a coarse-graining of (compatible with) one is incompatible with the other — the paper's terminology and scope; no quantum terminology silently imported. |
| **simultaneous measurement** | a single measurer/constructor that measures several observables at once. |

## 2. Non-sharp measurement (R2 — the withdrawn claim corrected)

**Withdrawn:** "base CT has no notion of unsharp/noisy measurement."

**Corrected:** the paper contains an explicit subsection **"Measurement of non-sharp
variables" (§6(a))**: the measurement task's **input variable need not be sharp** — the
input can be a non-sharp variable X̄ (the "bar" operation applied to sharp variables, e.g.
Boolean variables), and the consistency principle (Principle VIII) is introduced in
exactly this context, along with the emergence/definition of observables for non-sharp
inputs.

**Two distinct claims that must not be conflated:**

1. **CT NON-SHARP INPUT MEASUREMENT** — source-native: measurers can be defined for
   non-sharp input variables; Principle VIII constrains them; observables emerge for
   non-sharp inputs.
2. **QUANTUM UNSHARP / POVM MEASUREMENT** — effect-valued measurement with the
   parent-POVM joint-measurability calculus (effects, noise parameters, the full
   joint-measurability hypergraph hierarchy).

The audited paper establishes (1). **The audit has NOT established a CT-native analogue of
the full POVM joint-measurability hierarchy** — that remains open for the interface
(assessed in the interface repair artifact and result). Whether (1) already supplies
enough structure for generalized joint compatibility must be answered from sources, not
assumption.

## 3. Set-level structure (R3 — the "pairwise-only" claim withdrawn)

**Withdrawn:** "base CT encodes only pairwise incompatibility."

**Corrected:** CT contains genuinely **set-level (higher-arity) principles** — e.g.
**Principle IV**: if every pair of attributes in a variable is distinguishable, the
**whole variable** is distinguishable. Variables, information observables, and
superinformation structures are set-level objects.

**Narrower, defensible replacement question:** does the audited CT measurement framework
determine an arbitrary higher-order joint-measurability complex over several observables?
Possible answers: YES / NO / restricted scope / NOT FOUND. Assessed in the interface
repair artifact. It must not be answered "pairwise-only" merely because the
superinformation example is presented with two complementary observables.

## 4. CT-native coarse-graining (R4 — load-bearing for the interface)

The paper explicitly states that **a measurer of X automatically measures subsets of X and
coarse-grainings of X, by relabelling its outputs — and those relabellings are possible
classical computations**. Consequences:

- The previous classification of output coarse-graining as wholly `SUPPLIED` (imported
  from quantum parent measurement) was **wrong**: coarse-graining output recovery is
  **CT-native**.
- The strongest **source-native** interface candidate: a family {X_i} of measurable
  variables is **jointly CT-measurable iff there exists a single measurable variable /
  measurer structure Z such that each X_i is recovered as a legitimate CT
  coarse-graining/re-labelling of Z**. Construction, sufficiency, necessity, and price are
  assessed in the interface repair artifact — not assumed.

## 5. Withdrawn definitions (audit trail)

| withdrawn | reason |
|---|---|
| "variable = at all times exactly one X_j + possible tasks + pairwise tasks" | over-strong; the paper defines a variable as a set of mutually disjoint attributes |
| "distinguishability = the task x→y is possible" | attribute-level; variable distinguishability is the set-level task-to-records notion |
| "observable = equivalence class under permutations/coarse-grainings" | not the paper's definition; observables come from Principle VIII via the unique variable associated with all measurers of X |
| "base CT has no notion of unsharp/noisy measurement" | contradicted by §6(a), "Measurement of non-sharp variables" |
| "base CT encodes only pairwise incompatibility" | contradicted by Principle IV and the set-level definitions |

## 6. Sources (R7-corrected)

- arXiv:1405.5563 (Deutsch & Marletto, *Constructor theory of information*).
- **Proc. R. Soc. A 471, 20140540 (2015); DOI 10.1098/rspa.2014.0540** — the published
  version (the previous Phil. Trans. citation was incorrect; corrected per R7). PMC4309123.
- arXiv:1210.7439 (CT core: substrates/attributes/tasks/constructors — inherited unchanged).
