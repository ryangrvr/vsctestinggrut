# D5 PREREGISTRATION — comparator / identification audit for R1 · 2026-10-07

**Ruling.** G2-10 (`PROGRAM/OWNER_RULINGS.md`).

**Committed before the governing D5 audit begins.** The audit runs only after this file
is verified on the remote. The audit itself (`D5_COMPARATOR_AUDIT.md`) is bound by
everything below.

**Disclosure.**
- An earlier D5 run was launched before ruling G2-10 arrived. It was a workflow with a
  different verdict vocabulary (RESTATES / SPECIAL-CASE-OF / GENERALIZES / OVERLAPS /
  DISTINCT), and it lacked comparator 10.
- Claude Code stopped it on receipt of G2-10. **None of its outputs were opened, and it
  is not used.**
- The governing audit is a fresh run against this preregistration.

## 1. Verdict categories (fixed in advance; G2-10)

| Category | Criterion |
|---|---|
| **RESTATED** | ε_R, together with its quotient, distance and identification rule, is an existing quantity or test under renamed variables, **with no added structure**. That is, some established object already contains both the declared interface quotient and the common-readout condition, and ε_R is a known function of it. |
| **STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION** | The mathematics is known: maximal invariants, copulas, integral probability metrics, group quotients, comparison of statistical experiments, measurement invariance, universal exogenous representations. But the combination — a **certified common readout** plus a **quotient-irreducible process change** — defines a useful physical observable with an explicit identifying assumption that no comparator states in this form. |
| **DISTINCTIVE** | R1 yields a relation, constraint or prediction that the comparators do not yield. A concrete statement must be exhibited and checked against each comparator. |

**Two separate classifications.**
- **(M) The mathematics:** the quotient construction, the distance, Theorems A, A-BL,
  C, F and M1–M3, and Prop. G.
- **(P) The physical interpretation and identification rule:** common carrier, the
  mode-stability certificate, the verdict table, and the separation of E-C from E-A
  and E-B.

**Recorded expectation.** The middle category is expected for (M), and plausibly for
(P). It is an **acceptable** outcome and does not block the R1 terminal or Stage 3.
R1's job was to supply a well-defined observable that a future law must explain, not
to be new physics by itself.

**Kill linkage.**
- The STATE.md kill condition fires if D5 finds ε_R RESTATED as a generic
  nonlinear-response or non-Markovianity quantity, or finds it trivial or
  unidentifiable within its declared scope. That is recorded honestly; no rescue
  class.
- RESTATED relative to any other comparator is recorded as such. Its kill consequence
  is the owner's call.

**Decision rules.**
- **Per comparator,** the verdict is the more conservative of the analyst's and the
  adversarial skeptic's. The order is RESTATED (most conservative) <
  STANDARD/NEW-OPERATIONAL < DISTINCTIVE.
- **Overall (M) and (P):**
  - RESTATED if any single comparator restates it, under the criterion above;
  - otherwise DISTINCTIVE only if a concrete distinctive relation survives every
    comparator;
  - otherwise STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION.

## 2. Comparators (G2-10 list, verbatim order)

1. generic nonlinear-response diagnostics;
2. non-Markovianity measures;
3. process tensors / quantum combs;
4. invariant causal prediction;
5. independent causal mechanisms;
6. Janzing–Schölkopf algorithmic causal inference;
7. MDL causal discovery;
8. Blackwell–Le Cam / statistical-experiment comparison;
9. measurement-invariance / latent-measurement identification analogues;
10. input-output predictive-state / ε-transducer formalisms.

## 3. Questions D5 must answer (G2-10, verbatim)

- **A.** Is epsilon_R merely an existing generic nonlinear-response or process-distance
  quantity under renamed variables?
- **B.** Is the quotient construction itself known mathematics but the physical
  identification rule new only in application?
- **C.** Is the common-carrier/readout certificate an unavoidable identifying
  assumption?
- **D.** Does the product-latent construction prove non-identifiability when
  protocol-dependent readouts h_a are unrestricted?

The three explanations of protocol dependence are renamed to avoid a clash with
questions A–D:
- **E-A:** an unchanged environment plus a calibrated interface transformation;
- **E-B:** an unchanged environment plus protocol-dependent mode selection;
- **E-C:** a responding environment.

## 4. Method (fixed)

**Per comparator:**
1. its definition, verified against a primary source (DOI or URL plus the exact
   statement), or marked UNVERIFIED;
2. its formal relation to ε_R:
   - implications in both directions;
   - explicit counterexamples wherever an implication fails, using the program's
     controls (C2-G, C2-NG, C2-F, BRI1 X1, the two-mode example E2, the harmonic bath);
3. which of E-A / E-B / E-C it separates;
4. a category for (M) and a category for (P).

**Adversarial check.** Each comparator analysis gets an independent skeptic instructed
to argue for **RESTATED**.

**Answers to A–D** are given with their decisive arguments.

**Post-result labeling (G2-10 item 1).**
- The non-identifiability under unrestricted protocol-dependent readouts is **frozen
  pre-result** (`82d311e`: Prop. E; the h ↦ h_a exclusion; D5's mode-selection
  mandate).
- Z_A, [h]_T and the measurement-invariance framing are **POST-RESULT SYNTHESIS /
  STAGE-3 SEED**. They may be discussed but are not used to change any verdict
  criterion.

**No change** to WO-002, the interface ladder (closed at T_mono), or the frozen
pre-result R1 definition.
