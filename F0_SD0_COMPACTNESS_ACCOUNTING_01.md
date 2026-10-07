# F0 SD0 — COMPACTNESS ACCOUNTING PROCEDURE 01 (Stage 2; frozen before any candidate)
**Date:** 2026-10-06 · **Per:** Owner Ruling 05 C1. Committed before candidate
drafting; the procedure may not be changed after the candidate SHA exists.

## 1. What is counted — free choices (F)

Every freely chosen ingredient of the candidate, each listed as its own row with a
plain-language description of its information content: continuous parameters ·
discrete parameters · thresholds · selected invariants (which invariant, out of what
space of alternatives) · categorical branches · supplied algebraic objects ·
basis/graph/table data · external structures carrying equivalent information. **A
single symbol that encodes a table counts as the table** (its rows are counted,
not the symbol). Choices forced by R1–R15 or by the charter's firewalls are not
"free" and are listed separately as constraints.

## 2. What is counted — independent target distinctions (D)

One distinction per SD-K gate verdict the candidate reproduces: SD-K1, K2, K3, K4,
K5, K6, K7(i) — seven; SD-K8 counts as one further distinction (the qubit/gbit
separation at equal capacity); SD-K9's two closure properties are structural
requirements, not distinctions, and earn no credit. A distinction is **not** counted
if, given candidate-independent background facts recorded in the frozen record
(e.g. the Stage-1 enumeration), it is logically implied by other counted
distinctions; implications must be argued explicitly in the audit. Correct
predictions on G1–G3 and on the genuine holdouts are reported in the same table but
**tallied separately** (they are generalization evidence, not design targets).

## 3. The test

Report the full table `free choices / imported information / distinctions
reproduced`. The requirement (C1.5): the number **and information content** of F must
be clearly smaller than D. No numerical description-length threshold is imposed in
advance; the complete accounting is exposed for hostile review, and the owner judges.
If the effective adjustable structure of the candidate approaches the information
content of the targets, the classification is **lookup structure → `F0-SD0-RELOCATED`,
regardless of whether the controls pass.**

## 4. Known hazards (preregistered reading guidance for the hostile review)

- A "selected invariant" chosen from a large family of candidate invariants carries
  log-of-family-size information even if stated in one line.
- A rule quantifying over "all contexts/sections" is scenario-uniform; a rule
  quantifying over a hand-listed set of configurations is a table.
- Any constant whose value matters only on one control is a per-control fitted
  constant (C1.3 violation), however it is phrased.
