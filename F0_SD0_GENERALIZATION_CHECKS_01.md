# F0 SD0 — PREREGISTERED GENERALIZATION CHECKS 01 (Stage 2; frozen before any candidate)
**Date:** 2026-10-06 · **Per:** Owner Ruling 05 C2. These three cases were exposed in
the scientific discussion before freezing and are therefore **NOT blind holdouts** —
they are preregistered extension/generalization checks. The candidate's verdict on
each is recorded **before** the sealed section is consulted. Performance is reported
separately from SD-K1–K10 and does not alter the charter's terminal menu.

## G1 — Larger GHZ extension (outside finite gate SD-K4, per CR1)

**Instance (fully explicit; (4,2,2)):** parties 1–4, measurements X_i, Y_i, outcomes
{0,1}. Eight contexts with supports defined by parity constraints (⊕ = XOR over the
section's four bits):
- C_XXXX = {X1X2X3X4}: sections with ⊕ = 0;
- the six two-Y contexts {X X Y Y} and permutations (X1X2Y3Y4, X1Y2X3Y4, X1Y2Y3X4,
  Y1X2X3Y4, Y1X2Y3X4, Y1Y2X3X4): sections with ⊕ = 1;
- C_YYYY = {Y1Y2Y3Y4}: sections with ⊕ = 0.
(Each context's support = 8 of its 16 sections.) Verification at evaluation: the
candidate's verdict is computed from its frozen statement; the instance's own
properties are machine-checked from the table alone (possibilistic no-signalling;
global-section search over 2^8 assignments).

## G2 — Coarse-grained Hardy extension ((2,2,3), within the verified Mansfield–Fritz scope)

**Instance (fully explicit):** Alice a0, a1; Bob b0, b1; outcomes {0,1,2}. Supports:
- S(a0,b0) = {(0,0), (1,1), (1,2)}
- S(a0,b1) = {(0,1), (1,0), (1,1)}
- S(a1,b0) = {(0,1), (1,0), (2,2)}
- S(a1,b1) = {(0,1), (1,0), (2,0)}
Possibilistic no-signalling holds (marginal sets: a0:{0,1}; a1:{0,1,2}; b0:{0,1,2};
b1:{0,1} — consistent across contexts). Under the coarse-graining that merges
outcomes {1,2} into one block on every measurement, the table becomes the plain Hardy
pattern ((0,0) possible in (a0,b0); the merged-(0,0) cell impossible in (a0,b1) and
(a1,b0); the merged-(1,1) cell impossible in (a1,b1)). Verification at evaluation:
pNS, the coarse-graining property, logical contextuality (the section (0,0) ∈
S(a0,b0) does not extend; a global section exists), and exact-support probabilistic
realizability (3-outcome extension of the Stage-1 rational LP) are all machine-checked.

## G3 — Beyond-Hardy-completeness control ((2,3,3))

**Instance (by stable literature reference):** the empirical model of **Table 8(b) of
arXiv:1105.1819** (Mansfield–Fritz) — their explicit (2,3,3) model that is
possibilistically non-local while containing **no coarse-grained Hardy paradox**
("By direct inspection, we find that no coarse-grained Hardy paradox occurs for this
empirical model. Nevertheless, it displays possibilistic (and hence probabilistic)
non-locality" — read from the full text this session; the table's exact entries are
to be extracted verbatim from the paper at evaluation and machine-verified for the
two defining properties before the candidate's verdict is recorded). If extraction
fails to verify both properties, that failure is reported and G3 is marked
UNEVALUABLE rather than replaced.

## SEALED — expected literature classifications (consult only at evaluation, after the candidate's verdicts on G1–G3 are recorded)

> G1: strongly contextual (the GHZ (n,2,2) family is strongly contextual for all
> n ≥ 3, AB Prop 6.1; an explicit inconsistent Z2-subset for n = 4 is
> {XXXX=0, XXYY=1, XYXY=1, XYYX=1}: summing gives 0 = 1); quantum-realizable
> (four-qubit GHZ state with X/Y measurements).
> G2: logically contextual (not strongly); its coarse-graining is a plain Hardy
> pattern; expected exact-support realizable; quantum-realizability of this specific
> table is NOT asserted (not needed for the check).
> G3: possibilistically non-local with no coarse-grained Hardy paradox (the
> completeness-failure witness); probabilistic model given explicitly in the paper.

These cases must never be described as blind or out-of-sample; the genuine holdouts
are governed by `F0_SD0_HOLDOUT_PROTOCOL_01.md`.
