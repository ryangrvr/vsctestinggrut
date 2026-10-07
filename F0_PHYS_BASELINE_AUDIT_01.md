# F0 — PHYS BASELINE AUDIT 01 (targeted)
**Status:** campaign artifact. Focused, **source-verified** comparison of the candidate
meanings of physical access (`F0_PHYSICALITY_OF_ACCESS_01.md`) against the nearest existing
formalisms. Objective: determine, for each comparator, *is the proposed notion of physical
access already exactly this object?* Known machinery is allowed; `RESTATED` applies only
if the complete proposed F0 structure adds nothing beyond it. **No novelty theater.**

Scope discipline: this is NOT a broad literature survey. Only comparators bearing directly
on "what makes two interventions jointly realizable" are included.

## Comparator table

| # | formalism | what "jointly realizable" means there | closest F0-PHYS meaning | verdict |
|---|-----------|----------------------------------------|--------------------------|---------|
| B1 | Operational probabilistic theories / GPTs (Hardy 2001; Barrett 2007, arXiv:quant-ph/0508211; Masanes–Müller 2011, arXiv:1009.1050) | compatibility is a theorem *inside* the theory (joint POVMs, joint measurements) given states+effects | Meaning 2 (operational joint measurability) | **RESTATED at the operational level:** F0's Meanings 1–2 coincide with theory-relative compatibility. F0 adds nothing at this level. `RESTATED` (operational layer only) |
| B2 | Joint measurability / measurement compatibility literature (Heinosaari–Ziman, *The Mathematical Language of Quantum Theory*, 2011; Gudder; Ali et al.) | POVMs jointly measurable iff a joint POVM exists; sharpness distinction is central (coexistence vs. joint measurability vs. compatibility — known non-equivalences) | Meaning 2, sharp scope | **RESTATED** at the sharp scope; F0's P7 requirement (sharpness loaded into interventions) mirrors this literature's known distinctions. `RESTATED` (concept), with F0's contribution being only the *physical-vs-operational* separation |
| B3 | Gonda et al., almost-quantum theories and Specker's principle (arXiv:1712.01225) | pairwise joint measurability of **sharp** measurements implies global joint measurability; for unsharp POVMs this fails; almost-quantum set satisfies consistent exclusivity but not Specker | Meaning 2 at two scopes | **RESTATED** as physics content (already frozen in `F0_CHARTER_02_REPAIRED.md` §3 and `F0_BASELINE_AUDIT_01.md` N2/N3). F0-PHYS adds the *interpretive* point (compatibility is theory-relative), which is new only at the interpretive level, not the mathematical one |
| B4 | Effect algebras / orthomodular posets / D-posets (Foulis–Bennett; Dvurečenskij–Pulmannová) | compatibility = algebraic joint measurability within the given effect structure | Meaning 2 (abstracted) | **RESTATED** — same object, algebraic presentation. No added relation in F0 |
| B5 | Sheaf-theoretic contextuality (Abramsky–Brandenburger 2011, arXiv:1006.0484; Vorob'ev 1962; Keller 2014) | **contexts = compatible measurement/intervention sets**; `E(C)` = local sections (outcome assignments on a context); compatibility = sheaf condition / gluing; global sections & no-signal as families | F0-A kinematics itself (presheaf, overlap compatibility, gluing) | **RESTATED at the kinematic level:** F0-A's `C`, `E`, overlap compatibility, and the K2 observation (compatibility without global section) are exactly the standard empirical-models setup with the family convention. F0-A is honest about this (Formulation §4.5/§6.2). The F0-A *additions* are the strict status bins (CONSTRUCTED vs DERIVED) and the explicit gluing≠access separation (Formulation §8) — governance, not new math |
| B6 | Process theories / categorical operational QM (Abramsky–Coecke; Selinger; Kissinger; Categorical Quantum Mechanics) | composition/margin: joint realizability = existence of a morphism into a common effect/process; monoidal structure supplied | Meaning 3 (process co-occurrence) | **PARTIALLY RELOCATED:** the categorical route supplies monoidal/subsystem structure (§8 of the physicality doc). F0 did not find a new relation here beyond it |
| B7 | Process tensors / quantum combs (Chiribella–D'Ariano–Perinotti 2009, arXiv:0908.0962; Pollock et al.; Milz–Strunberg) | joint realizability = existence of a higher-order instrument combining interventions | Meaning 2/3 | **RESTATED at the operational level** — again theory-relative; presupposes the quantum/process formalism |
| B8 | Quantum causal models (Leifer–Spekkens 2013, arXiv:1111.5084; Fritz; Allen et al.) | compatibility via conditional quantum states on given factorizations | Meaning 3/4 | **RELOCATED:** presupposes factorization + Hilbert space + (a fortiori) a causal formalism — precisely a supplied route (P5/P6 prices) |
| B9 | Algebraic QFT: compatible/local subalgebras (Haag, *Local Quantum Physics*; nets of algebras) | joint realizability = commutation of subalgebras (spacelike separation / net structure) | Meaning 3 | **RELOCATED:** presupposes spacetime + the AQFT net axioms — the P6 price exactly |
| B10 | Emergent subsystem / tensor-factorization work (Zanardi; Tibau Vidal et al.; Cotler et al.) | compatibility relative to an emergent or chosen factorization | P5 route | **RELOCATED** (the factorization is the supplied structure) — and the literature itself treats the factorization as dynamical/derived, i.e. it *postpones* the problem F0 faces rather than solving it |

## Findings

**R6 precision: this audit was deliberately targeted, not exhaustive. "Not found" here
means "not found in this targeted audit", not "does not exist".**

1. **No comparator providing an observer-independent, structure-supplying-free definition of
   joint realizability was found in this targeted audit (NOT FOUND, not DOES NOT EXIST).**
   Every formalism either (a) is operational/theory-relative
   (B1, B2, B4, B7, B3) or (b) buys precision with spacetime, factorization, or process
   algebra (B6, B8, B9, B10). This is the audit's central result and matches the
   physicality doc's §8 ledger.
2. **The F0-A kinematic layer is RESTATED from B5** (sheaf/empirical-models machinery) —
   with the deliberately added governance separation (gluing-of-descriptions ≠ physical
   joint accessibility; Formulation §8.2) and the finite/declared-data discipline. F0-A is
   not claimed as novel mathematics; the ledger marks it `CONSTRUCTED` (declared here),
   and its mathematical content is standard. **No novelty theater is performed.**
3. **The interpretive separation is F0's genuine addition so far** — not a new
   compatibility relation, but the explicit four-way split (menu / operational /
   co-instantiability / structural) and the demonstration (P1–P7) that these come apart.
   This is new *as a recorded discipline*, not as a theorem.
4. **`RESTATED` applies (per R9) only where claimed:** the operational layer of
   F0-PHYS is RESTATED (B1/B2/B4); the kinematic layer is RESTATED in content (B5); the
   *physicality question* as posed — primitive intervention, objective joint realizability
   — was **not answered by any comparator found in this targeted audit**, hence the
   campaign terminal `F0-PHYS-OPEN` (with the relocation pattern documented).

## Source verification

- arXiv:1712.01225 (Gonda et al.): sharp/projective Specker implication; unsharp failure;
  almost-quantum vs. Specker. — verified in campaign baseline (`F0_BASELINE_AUDIT_01.md` N2/N3).
- arXiv:1406.5656 (Cabello): exclusivity + two assumptions ⇒ Tsirelson. — verified (N1).
- arXiv:2305.07917 (Bacciagaluppi): Specker from maximal entanglement + non-maximal
  measurements + no-signalling. — verified (N4).
- arXiv:1006.0484 (Abramsky–Brandenburger); Vorob'ev 1962; Keller 2014: sheaf/empirical
  models, gluing, global sections. — standard; matches F0-A's structure (B5).
- arXiv:1009.1050 (Masanes–Müller); Barrett 2007: GPT reconstruction machinery (B1).
- arXiv:0908.0962 (CDP **quantum combs / quantum networks** — higher-order quantum maps;
  NOT Oreshkov-style "process matrices", which are a different formalism) (B7).
  arXiv:1111.5084 (Leifer–Spekkens causal conditionalization) (B8). Haag, *Local Quantum
  Physics* (B9).
- Textbooks (Heinosaari–Ziman 2011; Dvurečenskij–Pulmannová; Foulis–Bennett; Hardy 2001)
  verify B1/B2/B4 claims at the standard-result level.
