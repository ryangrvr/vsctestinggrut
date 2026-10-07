# F0 — OWNER RULING 03 (Frontier A: boundary corrections confirmed; charter authorized)
**Date:** 2026-10-06. **Context:** issued after the owner reviewed the primary-source
verification recorded in `F0_FRONTIER_A_CHARTER_INPUT_01.md` §7 (claim 1b CONTRADICTED)
and the flagged items of `F0_OWNER_RULING_02.md` §4. The owner independently re-checked
the key source (BMT, quant-ph/0412136); this session additionally verified the
POVM-inclusive scope of the BMT lower bound, the CHTW attribution of the 3×3-attaining
game, and the Aravind magic-square 4×4 example against the BMT full text, and the JGBB
polygon-paper claims against its abstract (quotes in the SD0 charter's source table).

## 1. Boundary decisions

- **A-BQ — CONFIRMED**, defined concretely: ALLOW **at least one** bipartite 3×3
  perfect/strongly-contextual quantum support, e.g. the CHTW/Heywood–Redhead-derived
  construction. The gate is **not** phrased as "all bipartite d ≥ 3 cases are allowed":
  what is established is **existence beginning at 3×3**, not that every
  higher-dimensional realization yields strong contextuality. The magic-square game
  remains a useful additional positive control, but it uses 4×4 and must not be the
  witness for the minimum-dimension boundary (BMT records both the 3×3 construction
  and the 4×4 magic-square-type examples).
- **RESTATED DIMENSION GATE — CONFIRMED**, exact scope:
  - FORBID PR support in (2,2,2);
  - FORBID bipartite perfect/strong nonlocality when either local quantum system is
    only a qubit, **even allowing generalized measurements** (BMT explicitly include
    POVMs in proving the lower bound — verified: the proof invokes Naimark's theorem,
    "truly the most general form of quantum strategy");
  - ALLOW at least one bipartite 3×3 strong-contextual/perfect quantum support;
  - ALLOW multipartite 2×2×2 GHZ-type strong contextuality;
  - **none of these encoded as a scenario-name, party-count, or dimension lookup
    table.**
  Cabello's result that every bipartite perfect quantum strategy defines a
  Kochen–Specker set (arXiv:2311.17735) reinforces that the bipartite perfect-strategy
  sector is genuinely tied to contextual structure, not a quirk of one historical game.

## 2. Comparator decisions

- **LOCAL GEOMETRY — REQUIRED COMPARATOR, NOT YET R16.** Janotta–Gogolin–Barrett–
  Brunner (arXiv:1012.1215, New J. Phys. 13 (2011) 063024) establish that varying only
  local state-space geometry (regular-polygon models) changes attainable bipartite
  correlation strength, that Tsirelson-bound behaviour of the maximally-entangled
  analogue "depends crucially on … strong self-duality", and that "there exist models
  which are locally almost indistinguishable from quantum mechanics, but can
  nevertheless generate maximally nonlocal correlations." That strongly motivates
  geometry as a **hostile comparator**; it does **not** yet prove geometry is the
  indispensable missing object for Frontier A's support-level separation. A successful
  law could conceivably generate the distinction through another equivalent structure
  (event algebra, transformation structure, distinguishability relation, compositional
  invariant). **R16 is not adopted.** The campaign may promote a new requirement only
  if the hostile test shows that none of the surviving F0 primitives can distinguish
  the quantum/legal and post-quantum support families without adding new local-system
  structure. Preregistered failure statement:
  > If no invariant definable from the surviving F0 primitives can distinguish the
  > qubit/gbit/3×3-quantum controls, Frontier A terminates **RELOCATED** and must
  > identify the minimal missing local-system structure.
  Only then does the consolidation receive R16; the missing object is **not**
  pre-decided to be "geometry".
- **CAPACITY-ONLY EXPLANATION — HOSTILE CONTROL (confirmed).** Capacity alone is too
  weak as a prospective selector: theories can share the same maximal number of
  perfectly distinguishable local states while having very different convex state
  spaces and bipartite correlations (polygon family). Frontier A must explicitly
  hostile-test **same local capacity + different admissible correlation/support
  behavior**. "Dimension" is not a fundamental variable GRUT is allowed to see.
- **POLYGON FAMILY — RECONNAISSANCE ONLY**, not yet a pass/fail gate, until their
  possibilistic/strong-contextual support behavior is computed or sourced. The JGBB
  results are probabilistic (correlation strengths, Tsirelson/macroscopic-locality
  behaviour), not an enumeration of support spectra; using polygon models immediately
  as an A3/A4 support gate would silently cross from probability back into
  possibility. Reconnaissance question: **at fixed local capacity, do different
  polygon geometries produce different admissible zero-pattern/support families, or
  only different weights inside the same supports?**
- **QUANTUM RECONSTRUCTIONS — REQUIRED NULL COMPARATOR.** Add Hardy,
  Chiribella–D'Ariano–Perinotti, Masanes–Müller and related operational
  reconstructions. Firewall: if Frontier A reproduces quantum support structure only
  after adopting reconstruction axioms sufficient to recover the same local
  state/effect structure, classify the sector **RESTATED** (axioms merely renamed) or
  **RELOCATED** (axioms explicitly supplied). Known machinery can be contained; it
  cannot be counted as GRUT's distinctive law.

## 3. Stale-sentence corrections (executed as narrow input repair IR1–IR2)

Two sentences in `F0_FRONTIER_A_CHARTER_INPUT_01.md` @ `9290a1d`, inherited from the
superseded blanket premise, were ordered corrected before charter freeze:
- §5 A4 "stretch: reproduce the absence of bipartite quantum strong contextuality…" —
  false generally → replaced with the dimension-scoped boundary of §1 (**IR1**).
- §9 "why strong contextuality needs more parties or settings" — now exactly the wrong
  conclusion → replaced with "why the quantum-admissible support classes change across
  the verified local-resource boundary without inserting Hilbert dimension, party
  count, setting count, or scenario labels by hand" (**IR2**).

## 4. Authorization

$$\boxed{\textbf{FRONTIER A CHARTER — AUTHORIZED TO BE WRITTEN}}$$

The campaign enters with **no preferred generative mechanism and no preferred failure
object. It is allowed to invent a law now.** The question has changed from "what known
framework supplies the missing structure" to: **can a compact invariant principle
generate the admissible support family itself?** Its first serious discriminator:
PR₍₂ₓ₂₎ forbidden while quantum strong contextuality at 3×3 is allowed — and simple
capacity counting may not explain the difference by fiat.

Charter freeze and campaign execution remain separate: the charter is frozen alone for
owner review; **execution requires a further owner authorization.** F0-B (access-law
dynamics) remains prohibited.
