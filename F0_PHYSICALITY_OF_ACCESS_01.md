# F0-PHYS — PHYSICALITY OF ACCESS 01
**Status:** the central scientific artifact of the F0 execution 01 campaign
(`F0_EXECUTION_01_CHARTER.md`). It asks one question:

> What exactly is a primitive intervention, and what physical fact makes two interventions
> objectively jointly realizable?

**How access changes is out of scope.** No `R_Gamma`, `A_Gamma`, `Cl_Gamma`, `S`, `U` is
proposed here. Nothing in this document may modify the frozen charter.

---

## 0. The F0-PHYS gate

The gate: does `C` (the context structure of `F0_A_KINEMATIC_FORMULA01`/`_01`) have an
**observer-independent physical meaning**, or is it merely an **experimenter's measurement
menu** — a record of what apparatus happens to exist? Four candidate meanings are
distinguished (§2–§5), hostile tests P1–P7 (§7) separate them, and a terminal is reached
(§8). The gate is stated here explicitly because it has a *negative* form: **no
locality/geometry language may be used downstream of F0 until this gate passes.**

## 1. What a "primitive intervention" is (candidate definition)

At the kinematic level (F0-A) an intervention is a **primitive label** `x` with an outcome
alphabet `O_x` — uninterpreted. The F0-PHYS question is what, physically, `x` should be
*taken to be*. Candidates:

| candidate | content | status in this campaign |
|---|---|---|
| I-1 | an apparatus setting someone built | OPERATIONAL (§2) |
| I-2 | an input of an operational procedure with joint readout | OPERATIONAL (§3) |
| I-3 | a physically performable process/event | candidate (§4) |
| I-4 | a primitive of the physical structure itself | candidate (§5) |

**No interpretation is assigned in F0-A.** The formalism works for any of them; that
neutrality is a feature, and it is why the gate must be settled separately.

## 2. Meaning 1 — experimental availability

- **Definition.** `C` = the family of measurement combinations the experimenter's current
  laboratory permits. Two interventions are "jointly realizable" iff the apparatus can be
  physically arranged to run both in one experimental session.
- **Apparatus dependence:** total. The same physics with a bigger budget or a new device
  changes `C` without any change in the physical content being described.
- **Observer dependence:** total — it is an agent's menu.
- **Changes when a device is redesigned:** yes, trivially.
- **Exists without a measurement theory:** yes, but precisely because it *is* a menu.
- **Presupposes:** no Hilbert space, but does presuppose apparatus, agents, economics.
- **Fundamental primitive?** **No.** It cannot ground proto-geometry: geometry would then
  depend on funding. **Verdict: `OPERATIONAL`** (ledger L14).

## 3. Meaning 2 — operational joint measurability

- **Definition.** Interventions `x, y` are jointly realizable iff there exists a single
  **procedure** `p_{xy}` with readout such that running `p_{xy}` reproduces the statistics
  of running `x` and of running `y` (in a stated sense of marginal agreement).
- **Apparatus dependence:** substantial — joint measurability in quantum theory depends on
  the noise/sharpness of the specific POVMs, not only on what is being measured.
- **Observer dependence:** moderate (procedure-language is observer-framed).
- **Changes when a device is redesigned:** **yes** — the canonical fact: unsharp versions
  of the same observables become jointly measurable while sharp versions are not
  (baseline audit B3, arXiv:1712.01225). If the *same underlying physics* yields different
  `C` under re-sharpening, `C` is not tracking the physics; it is tracking the instruments.
- **Presupposes:** a measurement theory (states + effects + at least a statistical
  formalism). That is a huge presupposition to place *under* the foundation.
- **Fundamental primitive?** **No** — it is a theorem-level notion *within* an already
  given theory. **Verdict: `OPERATIONAL`** (ledger L14).

## 4. Meaning 3 — physical co-instantiability (the strongest candidate)

- **Definition (candidate).** Interventions `x, y` are jointly realizable iff the physical
  processes they denote can **occur together in one world**, as processes, with no
  reference to any observer, menu, or measurement procedure: there is a physically possible
  single situation in which both processes take place.
- **Apparatus dependence:** none *if the processes are identified physically*. This is the
  whole difficulty: without a theory of what the processes are, the identification is
  informal.
- **Observer dependence:** aimed at none; but every concrete realization below re-imports
  either spacetime structure or subsystem structure (both are **supplied** inputs, ledger
  list §8).
- **Changes when a device is redesigned:** no — that is the point of the candidate.
- **Exists without a measurement theory:** this is exactly what fails. Every way of making
  "can occur together" precise that this campaign found requires one of:
  (a) **spatiotemporal separation/coexistence** — presupposes spacetime (P6);
  (b) **independence of sub-systems** — presupposes a tensor-factor or subsystem
  decomposition (P5);
  (c) **commutation of transformations** — presupposes an algebra of processes, i.e. a
  dynamics/theory (P4-analysis);
  (d) **joint realizability of preparations and readouts** — collapses into Meaning 2
  (operational), which is observer-framed.
- **Presupposes:** spacetime, or subsystem structure, or process algebra — one of them.
- **Fundamental primitive?** **Not yet earned.** The candidate is the *right shape* — it is
  the only one of the four that is even attempting to be observer-independent — but every
  current formulation buys its precision with **supplied structure**. **Verdict:
  `UNRESOLVED`** (ledger L15); the structural reasons are the failed routes P5/P6/P7
  (ledger L17, L19).

## 5. Meaning 4 — objective structural compatibility

- **Definition (candidate).** There is a fundamental relation `≈` among physical processes
  such that compatibility facts are facts *about the physical structure*, from which
  operational joint measurability would be a **derived, theory-relative shadow**.
- **Status.** This is a *research target*, not a definition: no candidate relation with
  known extensional behavior was found that (i) does not presuppose spacetime, subsystems,
  or a process algebra, and (ii) recovers the operational relation in the regime where the
  operational notion is well-defined. Without (ii) it is not even wrong; with (ii) it
  currently duplicates one of the supplied routes of §4.
- **Verdict: `UNRESOLVED`** (ledger L16).

## 6. The asymmetry that motivates the gate (why this is not pedantry)

The same physical world supports, simultaneously and consistently:
- pairwise joint measurability without triplewise joint measurability for **unsharp**
  measurements (B3);
- pairwise joint measurability implying triplewise joint measurability for **sharp**
  measurements (B2/B3, the Specker structure at the sharp scope);
- different `C` for the same observables under different instruments (P1/P3).

So `C` as a *fact about the world* and `C` as a *fact about the laboratory* demonstrably
come apart. F0 must know which one it is holding before anything is built on it. That is
the gate.

## 7. Hostile physicality tests

Each test is a thought experiment / finite counterexample. Status labels are from the
ledger; **fails are recorded as `STRUCTURAL-FAIL` with reasons** — they are results, not
embarrassments.

### P1 — apparatus dependence (`STRUCTURAL-FAIL` for fundamental status)
*Same physics, different apparatus.* Take the same physical system and two instrument
families: coarse jointly-measurable POVMs vs. sharp individual measurements. Meaning 1 and
Meaning 2 give **different** `C` for the **same** underlying world. If `C` changed solely
because equipment changed, then either `C` is the menu (and not physical), or there are
*two different* `C`-facts and the fundamental one is not the operational one. **Reason
recorded:** the operational `C` is demonstrably not invariant under instrumentation;
therefore the fundamental relation, if any, is not the operational one.

### P2 — relabeling invariance (`DERIVED`, negative)
Could the dependence on apparatus be a mere relabeling artifact? **No**: the F0-A
representation equivalence (Formulation §7) already quotients relabeling, and P1 survives
the quotient — the two `C`'s are inequivalent objects, related by no declared move. The
dependence is *substantive*, not notational.

### P3 — coarse vs. fine graining (`STRUCTURAL-FAIL` for fundamental status)
The same physical measurement can be presented coarse (jointly measurable) or fine
(paired but not jointly measurable). Under Meaning 2 the two presentations give different
compatibility facts for the *same* physical measurement. A fundamental notion cannot vary
under a change of presentation. **Reason:** Meaning 2 conflates presentation with content;
only a meaning that fixes a canonical physical presentation could survive — and no such
canon was found without a supplied theory.

### P4 — observer-ignorance probe (`DERIVED`, negative)
Can we rescue observer-independence by "bracketing" the observer — defining joint
realizability as *"two interventions that WOULD be jointly performable by any
suitably-equipped observer"*? The counterfactual modalizes the menu, but the modality is
still indexed to observers and their equipment class; it relocates the menu into the
counterfactual rather than eliminating it. **Reason:** modal relocation is not elimination;
this is exactly the F0 `LATENT-RELOCATION` pattern applied at the definition level.

### P5 — subsystem decomposition dependence (`STRUCTURAL-FAIL`)
Physical co-instantiability via "independent sub-processes" presupposes a decomposition of
the world into sub-systems (tensor factors in quantum theory; spatial regions classically).
That decomposition is **supplied structure**, not derived at F0 — and different decompositions
(algebraic vs. tensor-factor; with/without superselection sectors) yield different
compatibility facts. **Reason:** a candidate fundamental relation that varies with the
supplied decomposition is not fundamental *yet*; it inherits the decomposition's arbitrariness.

### P6 — temporal/spacetime dependence (`STRUCTURAL-FAIL` as a definition route; `UNRESOLVED` for the deeper question)
"Can occur together" is often glossed as "can be arranged in one spacetime region" or
"simultaneously performable." Both glosses presuppose spacetime, which F0 must not do
(the frozen charter's F0-PHYS rule: no locality/geometry language *before* the gate).
Moreover, temporal glosses make joint realizability depend on a direction of time, which
the F0 program has not earned. **Reason:** presupposition of spacetime violates the
F0-PHYS precondition; the route is *blocked*, not disproven — what structure would suffice
in its place is `UNRESOLVED` (ledger L19).

### P7 — sharp/unsharp scope test (`STRUCTURAL-FAIL` for any single-relation reading)
Within the best-established physical theory: pairwise-without-triplewise for unsharp,
pairwise-implies-triplewise for sharp (B2/B3). If a single relation "jointly realizable"
covered both, one of these theorems would be violated by construction. Hence: **if `C` is
fundamental, the sharp/unsharp distinction must be *physically loaded into the
interventions themselves*** — sharpness is not a presentation detail but a difference in
what the interventions are. That is a substantive requirement imported into any future
physical reading of `C`, and it is recorded as such (see §9).

## 8. Ledger of supplied structure (complete, per the no-silent-strengthening rule)

Every precision source for "can occur together" identified in §§4–7, with its price:

| supplied structure | used by | price |
|---|---|---|
| measurement theory (states/effects) | Meanings 1–2 | observer-framed; theory-relative |
| subsystem/tensor decomposition | P5 route | decomposition is arbitrary; supplied |
| spacetime structure | P6 route | violates F0-PHYS precondition; supplied |
| process algebra / dynamics | commutation route | presupposes a theory of change; supplied |
| sharpness notion | P7 requirement | presupposes measurement theory; supplied |

**No observer-independent definition of "jointly realizable" was found that costs nothing.**
This is the central result of the campaign, and it is negative.

## 9. Consequences recorded for the F0 program (requirements, not conclusions)

1. The operational readings of `C` are legitimate **as operational readings** — they
   support the kinematics and all future *calibration* work — but they cannot be promoted
   to proto-geometry without the supplied-structure prices listed in §8.
2. If a later F0 level derives geometry from `C` while `C` is Meaning 1/2, the derivation
   is `F0-OPERATIONAL-ONLY` or, if the menu is treated as physical, `F0-LATENT-RELOCATION`.
3. Any future physical candidate must state, up front, which of the §8 prices it pays —
   and pay them explicitly, not silently.
4. P7's requirement (sharpness loaded into the interventions) is a mandatory design
   constraint for any future candidate relation.

## 10. Terminal

Applying the charter's F0-PHYS terminals:

- `F0-PHYS-PASS` — an earned observer-independent physical meaning for `C`: **not reached.**
- `F0-OPERATIONAL-ONLY` — `C` is (for now) an operational notion: **fits, but is
  incomplete as a terminal because the physicality question is genuinely open, not closed.**
- `F0-PHYS-RELOCATED` — the candidates relocate supplied structure into `C`: **true of
  each current formulation of Meaning 3/4, as documented in §8.**
- `F0-PHYS-RESTATED` — some candidate is an existing formalism restated: **partially true**
  (see baseline audit, B1/B4) but not the whole story.
- `F0-PHYS-OPEN` — the physicality question remains open with the failure modes
  documented: **this is the terminal reached.** It is *not* `F0-PHYS-PASS`; it is not
  claimed that no physical meaning exists; it is recorded precisely what was tried, why
  each route failed, and what structure any future candidate must supply or derive.

**F0-PHYS terminal: `F0-PHYS-OPEN`** (with `F0-PHYS-RELOCATED` as the documented failure
mode of every current candidate, and `F0-OPERATIONAL-ONLY` as the status of `C` under
meanings 1–2). Full statement and machine-readable fields: `F0_EXECUTION_01_RESULT.md`.
