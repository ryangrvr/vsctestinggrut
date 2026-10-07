# F0 SD0 — HOLDOUT PROTOCOL 01 (Stage 2; frozen before any candidate)
**Date:** 2026-10-06 · **Per:** Owner Ruling 05 C3. This protocol deliberately names
**no holdout instances**. Selection happens only after the candidate principle's
commit SHA exists and the candidate is immutable.

## 1. Admissible pool (category, not instances)

Support-level cases from the published contextuality/non-locality literature with an
established classification, in finite measurement scenarios. A case is an explicit
finite support table (or a construction from which one is mechanically derivable)
together with a literature-backed expected status in at least one of these respects:
possibilistic-locality class (local / logically contextual / strongly contextual);
exact-support probabilistic realizability; quantum-realizability at the support level
(where the literature establishes it).

## 2. Eligibility rules

E1. The scenario is small enough for the campaign's exact tooling (global-section
search and, where needed, the rational-LP realizability check) to verify the case's
possibilistic properties mechanically.
E2. The expected status is backed by a citable published source (paper + location);
private-communication-only results are admissible only with a published proof also
cited.
E3. The support table must be constructible from the source without discretion; any
ambiguity in extraction disqualifies the case.
E4. Cases spanning at least two different scenario shapes are preferred; at most one
case per scenario shape.

## 3. Exclusions (no duplication)

X1. Nothing equal, up to the declared representation-equivalence moves (measurement
and outcome relabellings, party exchange), to any SD-K1–K10 gate instance: the
(2,2,2) classical/Hardy/PR classes, the (3,2,2) GHZ support, the Peres–Mermin /
KS configurations named in SD-K5, the specific bipartite 3×3 construction of SD-K6,
the SD-K7(i) representative family, the qubit/gbit SD-K8 pair.
X2. Nothing equal, in the same sense, to G1, G2, or G3 of
`F0_SD0_GENERALIZATION_CHECKS_01.md` (the (4,2,2) GHZ table; the stated (2,2,3)
table; Table 8(b) of arXiv:1105.1819).
X3. Nothing from the (2,2,2) scenario (its full support landscape is already in the
Stage-1 enumeration and hence visible to the designer).

## 4. Number of cases

At least **three**.

## 5. Independent-selector procedure

S1. The selector is a fresh, independent evaluator (a separately spawned agent with
its own context), invoked only after the candidate's commit SHA is recorded.
S2. The selector receives: this protocol; the exclusion list of §3 (including the G
instances); the campaign's scenario conventions — and **not** the candidate artifact,
its motivation, or any discussion of the candidate's mechanism. (The selector may be
given the candidate's bare input/output signature if needed to ensure evaluability,
and nothing more.)
S3. The selector returns, per case: the explicit support table (or mechanical
construction); the literature-supported expected status with provenance (paper,
location); why the case is not excluded under §3; which eligibility rules it meets.
S4. The selection is committed as `F0_SD0_HOLDOUT_SELECTION_01.md` **before** the
candidate is evaluated on any selected case.

## 6. Immutability rule

The candidate cannot be changed after selection (it is already immutable from its
commit under Ruling 05 Stage 3; this rule re-binds it across Stages 4–5). Holdout
performance is an independent generalization audit: it does not change the charter's
terminal menu, and a `LAW-CANDIDATE` that fails badly on the genuine holdouts must be
reported to the owner as such and cannot be treated as externally validated.
