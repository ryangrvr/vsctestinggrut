# F0 SD0 — RECONNAISSANCE 01 (Stage 1 of Owner Ruling 05 C4)
**Date:** 2026-10-06 · **Code:** `f0_sd0_recon_222.py` (exact: Fractions, rational
two-phase simplex, no floats), `f0_sd0_recon_polygon.py` (Part A floats as
confirmation of an analytic statement; Part B exact rationals). **No law is proposed
in this artifact.**

## 1. (2,2,2) Boolean-support enumeration (exact) — `DERIVED`

All support tables (nonempty support per context) satisfying **possibilistic
no-signalling** (pNS: each party's locally possible outcomes agree across the two
contexts containing the measurement), classified by global-section structure, then by
**probabilistic exact-support realizability** (there is a no-disturbance probability
model whose p>0 support is exactly the table; checked cell-by-cell by exact rational
LP, assembled by the proved mixing-union lemma):

| class | pNS tables | exact-support realizable | gap |
|---|---|---|---|
| possibilistically local (every possible section extends) | 1721 | 1721 | 0 |
| logically contextual (globals exist; some section does not extend) | 1232 | 992 | **240** |
| strongly contextual (no global section) | **8** | **8** | 0 |
| total | 2961 | 2721 | 240 |

**Findings (all machine-checked, exact):**

1. **Lal's proposition reproduced and sharpened at the possibilistic level.** The
   strongly contextual class contains exactly 8 tables, and they are exactly the 8 PR
   boxes (a ⊕ b = x·y ⊕ αx ⊕ βy ⊕ γ) — **already before the realizability filter**:
   in (2,2,2), possibilistic no-signalling alone forces strong contextuality onto the
   PR patterns. All 8 are realizable (SD-K3's FORBID target set is therefore exactly
   the strongly-contextual realizable class of the smallest scenario).
2. **Mansfield–Fritz completeness reproduced.** Every one of the 1000 realizable
   possibilistically-nonlocal tables (992 logical + 8 strong) contains a plain Hardy
   configuration under the 128-element relabelling symmetry group: 1000/1000.
3. **New exact datum — the possibilistic/probabilistic gap is nonempty and sits
   entirely in the logical class:** 240 pNS tables admit *no* no-disturbance
   probability model with exactly that support (local: 0; strong: 0). A support law
   defined purely at the possibilistic level would admit 240 patterns in the smallest
   scenario that no probabilistic theory realizes exactly — any candidate must say
   which object (pNS tables, or realizable supports) it generates. This sharpens the
   charter's target-object question with an exact count.

## 2. Polygon zero-pattern reconnaissance at fixed capacity

**Part A — single-system zero structure (analytic statement, numerically confirmed
n = 3..8) — `DERIVED` (combinatorial) + confirmation.** All regular-polygon systems
have capacity 2 (JGBB; `SUPPLIED` source fact). For the binary facet measurement
(e_F, u−e_F): outcome 1 is impossible on exactly 2 extremal states for every n; but
outcome 2 is impossible on exactly **2** extremal states when n is even (antipodal
facet) and exactly **1** when n is odd (opposite vertex). **At fixed capacity, local
geometries already differ at the single-system support level** — the first exact
affirmative answer to the reconnaissance question "different zero-pattern families,
or only different weights?": different zero patterns, visible before any composite is
chosen.

**Part B — PR-forcing lemma and the capacity-2 contrast (exact) — `DERIVED`.**
Lemma (weights-free): a model whose support is the PR zero-pattern has every
correlator ±1 exactly, hence CHSH = 4, for any weights on the support. Consequence:
any composite with attainable CHSH < 4 cannot realize the PR support. And, exactly in
rationals: on square ⊗ square (gbit/boxworld, maximal tensor), the PR functional is a
valid state (16/16 product-extremal-effect probabilities ≥ 0; context sums 1; support
exactly the PR pattern, 8 cells at 1/2 and 8 at 0). Combined with §1: **qubit and
gbit, both capacity 2 — the gbit realizes the PR support, the qubit cannot** (the
strongly-contextual (2,2,2) class = PR only, and PR is not quantum-realizable). This
is SD-K8's canonical instance, now machine-grounded on the gbit side.

**Part C — recorded `UNRESOLVED`.** Attainable-CHSH values / support families for
polygon composites with n ≠ 4 (including JGBB's maximally-entangled analogues) are not
computed here. Via the forcing lemma, CHSH < 4 ⟹ PR support unrealizable for that
(n, composite, state family); the per-n values are comparator inputs for a later
stage or the JGBB full text.

## 3. Status summary

`DERIVED`: §1 table and findings 1–3; §2 Part A combinatorial statement and Part B
lemma + n=4 realization. `SUPPLIED`: polygon capacity-2 (JGBB), the JGBB
parametrization context. `UNRESOLVED`: §2 Part C. Reconnaissance complete per Stage 1;
no candidate content anywhere above.
