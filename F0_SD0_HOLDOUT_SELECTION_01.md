# F0 SD0 — HOLDOUT SELECTION 01 (Stage 4; selected AFTER the candidate freeze)
**Date:** 2026-10-06 · **Candidate SHA (frozen before selection):**
`aacbc5215f36ba3ccae4c9ca3dca87c30cc0e21b`. **Selector:** an independent agent run
under `F0_SD0_HOLDOUT_PROTOCOL_01.md` §5: it received the protocol, the exclusion
list, the scenario conventions, and the candidate's bare input/output signature only —
**not** the candidate artifact, its mechanism, or any design discussion. **Blindness
attestation (selector's, recorded verbatim in substance):** no file under the
worktree, scratchpads, or the repository was read or fetched; no search for this
program; work from the task prompt and external published literature only; local
computation limited to self-contained inline verification of pNS and classifications.
The candidate is unmodified (its SHA predates this artifact). Per C3, the selected
cases' expected statuses are recorded openly here; the anti-fitting protection is the
freeze order, not evaluator ignorance.

## H1 — C7 anticorrelation box (7-cycle)
**Scenario:** variables X0..X6, binary; contexts {Xi, Xi+1 mod 7}, i = 0..6.
**Support (every context):** (0,1) and (1,0) possible; (0,0) and (1,1) forbidden.
**Expected status (literature):** STRONGLY CONTEXTUAL (inconsistent Z2 system
xi⊕xi+1 = 1 summed over an odd cycle; AvN_Z2 per arXiv:1502.03097 Prop. 7);
exact-support ND-realizable (no-disturbance polytope vertex: Araújo–Quintino–Budroni–
Terra Cunha–Cabello, PRA 88, 022118 (2013) / arXiv:1206.3212, Thm 2, odd number of
negative correlators); **NOT quantum-realizable** (its support forces Ω = 7 > the
odd-n Tsirelson bound Ω_QM(7) = (21cos(π/7)−7)/(1+cos(π/7)) ≈ 6.27; Thm 3, Eq. 7).
**Non-duplication:** Specker triangle is the 3-cycle (3 variables); the (2,3,2)
XOR exclusions are bipartite on 6 variables; a 7-cycle admits no party bipartition.
**Catches:** over-allowing (a quantum-sound law must reject it).

## H2 — Mermin pentagram parity support (10₂–5₄ configuration)
**Scenario:** 10 variables A1..A10, outcomes {+1,−1}; 5 four-variable contexts
L1 = {A1,A2,A3,A7} (ε=+1), L2 = {A1,A5,A6,A8} (+1), L3 = {A4,A2,A6,A9} (+1),
L4 = {A4,A5,A3,A10} (+1), L5 = {A7,A8,A9,A10} (−1); each variable in exactly 2
contexts. **Support:** in Lk, exactly the cells with product of entries = εk
(8 possible / 8 forbidden per context). **Expected status:** STRONGLY CONTEXTUAL
(parity proof: product of all five constraints gives +1 = −1; Mermin, RMP 65, 803
(1993); Waegell–Aravind, J. Phys. A 45, 405301 (2012) / arXiv:1205.5015, Fig. 3;
Loveridge–Dridi arXiv:1511.00950 §3.1); **quantum-realizable, state-independent**
(three-qubit Pauli realization: X1X2X3 etc.; with ρ = I/8 every allowed parity cell
has p = 1/8, forbidden cells 0 — exact support). **Non-duplication:** Peres–Mermin
square is 9 variables / 6 ternary contexts; GHZ gates are Bell scenarios; this is a
single-system 10-variable / 5 quaternary-context configuration. **Catches:**
over-forbidding (must be admitted).

## H3 — Pentagon Hardy-like support (Cabello–Badziąg–Terra Cunha–Bourennane)
**Scenario:** variables v1..v5, binary; contexts {v1,v2},{v2,v3},{v3,v4},{v4,v5},
{v5,v1} (KCBS 5-cycle). **Support:** {v1,v2}: (1,0),(0,1),(0,0) possible, (1,1)
forbidden · {v2,v3}: (1,0),(0,1) possible, (0,0),(1,1) forbidden · {v3,v4}:
(1,0),(0,1),(0,0) possible, (1,1) forbidden · {v4,v5}: (1,0),(0,1) possible,
(0,0),(1,1) forbidden · {v5,v1}: (1,0),(0,1),(0,0) possible, (1,1) forbidden.
**Expected status:** LOGICALLY CONTEXTUAL, not strong (PRL 111, 180404 (2013) /
arXiv:1310.8330, Eqs. (2)–(8): zeros P(1,1|1,2) = P(0,0|2,3) = P(1,1|3,4) =
P(0,0|4,5) = 0 force the noncontextual prediction P(0,1|5,1) = 0 while quantum gives
1/9; selector re-derived: exactly 3 global sections; the non-extending possible
sections are exactly the v1 = 1 ones); **quantum-realizable** — the exact support of
the published qutrit model |η⟩ = (1,1,1)/√3 with rays (1,−1,1)/√3, (1,1,0)/√2,
(0,0,1), (1,0,0), (0,1,1)/√2 (exact rational probabilities; adjacent rays exactly
orthogonal). **Non-duplication:** no 5-cycle appears in the exclusions; not a Bell
scenario; not the (2,2,3) coarse-grained-Hardy table. **Catches:** over-forbidding
on a state-dependent logical-contextual quantum support.

## H4 — C6 anticorrelation (even cycle; local baseline)
**Scenario:** X0..X5 binary; contexts {Xi, Xi+1 mod 6}. **Support (every context):**
(0,1),(1,0) possible; (0,0),(1,1) forbidden. **Expected status:** possibilistically
LOCAL (the two alternating deterministic assignments realize all 12 possible cells;
selector re-verified exactly 2 global sections); exact-support classically realizable
(uniform mixture), hence quantum-realizable. Anchors: PRA 88, 022118 Thm 1–2 (the
all-negative direction on an even cycle is deterministically attainable);
Braunstein–Caves Ann. Phys. 202, 22 (1990). **Non-duplication:** the (2,3,2) XOR
exclusion row covers strongly contextual tables; this table is local (class is
relabelling-invariant); even-parity chained cycle, not relabelling-equivalent to any
odd-twist variant. **Catches:** baseline sanity (must be admitted).

## Coverage
Four distinct shapes (7-cycle, pentagram, 5-cycle, 6-cycle); expected classes
strong/strong/logical/local; quantum statuses NO/YES/YES/YES — both failure
directions covered. All four tables pNS (selector-verified; to be re-verified by the
evaluation). Per C3: the candidate may not be modified; holdout performance is an
independent generalization audit reported separately from SD-K1–K10.
