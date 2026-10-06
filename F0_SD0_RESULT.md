# F0 SD0 — RESULT (EXEC01)
**Date:** 2026-10-06 · **Charter:** `909eaf86c032f58628f2e63eead0f915e6d439dd` ·
**Candidate (frozen):** `aacbc5215f36ba3ccae4c9ca3dca87c30cc0e21b` (Anchored-Support
Principle, ASP) · **Holdouts (selected post-freeze):** `38332fb` · **Live evaluation:**
`49cdebd` (`F0_SD0_EVAL_RAW_OUTPUT_01.txt`). **Closed at owner direction** ("wrap up …
get back on course"); the comparator audit was stopped after 1 of 5 agents returned.

## Terminal: `F0-SD0-OPEN`

**Why this terminal and not the others.**
- **`LAW-CANDIDATE` — not earned.** It requires surviving the charter §5 comparator
  audit. The audit was not completed, and the one completed comparator returned
  **OVERLAPS-PARTIALLY**, locating ASP's forbid mechanism inside known theory (see
  below).
- **`RESTATED` — strongly indicated but not established.** The incomplete audit did
  not show that ASP's *physical, state-dependent* forbid claim is a corollary of
  existing results, which is what this terminal needs. **Recorded risk: HIGH.**
- **`RELOCATED` — not established.** No prohibited input was used. The compactness
  audit was not formally run (sketch in §4).
- **`NO-GO` — not applicable.** A finite rule passing all gates exists.

## 1. What was computed (exact, live, `DERIVED`)

Every SD-K gate, every G check, and every genuine holdout matched its expected
verdict:
- **(2,2,2):** forbids exactly the 8 PR boxes and admits all 2953 local + logical
  tables.
- **Allowed strongly contextual quantum supports:**
  - GHZ (3,2,2) and GHZ (4,2,2);
  - Peres–Mermin square;
  - Mermin pentagram (H2);
  - bipartite magic square;
  - CEG-18;
  - **SD-K6 at the 3×3 minimum dimension.** This is the CHTW Kochen–Specker game over
    a certified pure-triad ℝ³ KS core of 94 rays and 67 triads, obtained from a
    145-ray / 112-triad cross-product closure with uncolorability decided exactly in
    ℤ[√2].
- **Forbidden strongly contextual non-quantum supports:**
  - PR ×8;
  - 480/480 strong XOR-(2,3,2);
  - embedded PR and fine-grained PR;
  - PR⊗PR;
  - Specker triangle;
  - chained-PR 6-cycle;
  - **C7 odd-cycle box (H1, blind)**.
- **Admitted local/logical cases:** G2, G3 (G3's three defining properties verified
  from the arXiv:1105.1819 LaTeX source), H3, H4.

## 2. What the results mean (the honest reading)

- **T1 — admits everything not strongly contextual.** This is structural and holds in
  any scenario: a global section survives arc-consistency propagation in every
  sub-realization. So K1, K2, G2, G3, H3 and H4 test only that ASP does not
  over-forbid. They do not test its content.
- **T2 — in the pairwise-binary sector, ASP = "forbid strong contextuality".** When
  every context is a pair with binary outcomes, the problem is 2-SAT: arc
  consistency equals unit propagation, and an implication-graph component containing
  both x and ¬x makes every literal fail. This matches the CHTW binary-output theorem
  (no bipartite pseudo-telepathy with both outputs binary). It is the orchestrator's
  proof; the independent refuter was stopped before checking it, so it is
  `UNRESOLVED`-pending-review.
- **ASP's actual content.** It forbids strong contextuality that arc consistency
  refutes (hereditarily) and allows strong contextuality that arc consistency cannot
  see.
- **Known over-allowance.** ASP admits the theta parity system ({p,q,r} even,
  {p,q,s} even, {r,s} odd). That system is strongly contextual and has no operator
  model: in its solution group, J = e. So ASP is an **outer approximation**, not a
  characterization.

## 3. Comparator audit (partial; 1/5 returned) — Atserias–Kolaitis–Severini line

Verdict: **OVERLAPS-PARTIALLY.**

- **Atserias–Kolaitis–Severini** (arXiv:1704.01736): for 2-SAT, Horn and bijunctive
  instances there is no gap between operator and classical satisfiability, instance
  by instance. Unit-resolution and 2-clause implication chains are sound for operator
  assignments.
- **Bulatov–Živný** (arXiv:2404.11709):
  - bounded width means there is no gap;
  - Singleton Linear Arc-Consistency derivations are sound for operators (Lemma 16).
- **ASP's forbid direction in operator semantics.** The agent derived it as an
  extension of that Lemma 16 to non-linear arc consistency and to multi-variable
  events. This **forces** the ALLOW verdicts on the state-independent controls
  (Peres–Mermin, pentagram, KS game), so those verdicts **are not independent
  evidence**.
- **Not a corollary for state-dependent quantumness.** GHZ and magic-square Bell
  tables are quantum, but their operator-semantics instances have no operator
  solution. ASP's physical claim therefore does not follow from that literature.
- **Not run before the stop:**
  - the bounded-width / quantum-advantage literature (Ciardo; quantum monad; Ó
    Conghaile);
  - the contextuality-side comparators;
  - the decidability bound (Slofstra: whether exact quantum support families are
    undecidable, which would make *any* computable support law an approximation);
  - the independent refuter of T1, T2 and the evaluation code.

## 4. Unfinished audits (recorded, not run)

- **K7(ii).**
  - Binary-output bipartite sector: consistent with CHTW/BMT, via T2 (pending
    review).
  - Multi-outcome qubit-side POVM patterns: ASP is dimension-blind by firewall design
    and cannot certify the BMT boundary there. `UNRESOLVED`.
- **Compactness.**
  - Free choices: about 5.6 bits (F1–F4), plus about 2.3 bits for choosing among 5
    panel proposals.
  - Against: 8 counted gate distinctions.
  - F1, the consistency level, is effectively forced by K3 versus K4 (the strongest
    level that refutes PR but not GHZ). That is a tuning signal.
  - Generalization: 7/7 G + H verdicts correct, but only G1, H1 and H2 test content
    beyond T1/T2.
  - Not judged; owner's call if reopened.

## 5. Program-level takeaways

- **The support level separates quantum from post-quantum in the smallest scenario.**
  Possibilistic no-signalling alone forces (2,2,2) strong contextuality onto exactly
  the 8 PR boxes. There are 240 pNS tables with no exact-support probabilistic
  realization, all in the logical class.
- **A simple, uniform, dimension-blind support rule exists.** It meets every
  preregistered gate and the blind holdouts. Its mechanism, however, sits largely
  inside known bounded-width / operator-assignment CSP theory, and it over-allows.
- **Frontier A has not produced a new generative law.** It has produced a sharp
  structural map: "local-consistency-visible" strong contextuality is non-quantum;
  quantum strong contextuality lives where local consistency cannot see it.

## 6. STOP

STOP FOR OWNER REVIEW. The candidate is unmodified. No R16, no F0-B, no merge to
`main`. Reopening options, if ever wanted:
- finish the 4 stopped audit agents (workflow resumable);
- run the formal compactness judgment.
