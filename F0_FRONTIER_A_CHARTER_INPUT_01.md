# F0 — FRONTIER A CHARTER INPUT 01 (support determination)
**Date:** 2026-10-06 · **Authorized by:** `F0_OWNER_RULING_02.md` §4 ("fold these
corrections into the charter input before the actual Frontier A charter is written").
**Narrow input repair IR1–IR2 applied 2026-10-06 per `F0_OWNER_RULING_03.md`** (two
sentences superseded by the dimension verification; marked [IR*]).
**Status:** charter *input* only — **the Frontier A charter is not written here, no
campaign is opened, no law is proposed, F0-B remains prohibited.** Binding context: the
governing requirements map `F0_REQUIREMENTS_CONSOLIDATION_01.md` @
`0a9a941c0951ffeb8f1cccafa12892057a62c884` (R1–R15, none discharged).

## 1. The question

**What determines which local events are possible/impossible?** — before asking what
determines the positive weights of the possible events. The campaign must decide, and
declare, which of G0's three exposed objects is the target physical object:
the declared possibility set · the derived p>0 support · the
zero-probability-but-not-forbidden events.

## 2. Target object (owner correction 1)

The law-level target is the **admissible support family** — CONSTRUCTED program
terminology (as is its synonym "support spectrum"); not a standard literature term —
**indexed by a physical realization, not a bare scenario**:

- 𝔖_T(R) = { Supp(p_s) : s ∈ States_T(R) }, where R is a declared
  physical/task/measurement realization of the scenario in theory T. A combinatorial
  scenario Σ = (X, 𝓒, O) does not itself say which measurements, task structures or
  dimensions realize its labels; support depends on both the state and the realization.
- **Envelope** P_T(R) = ⋃_{S ∈ 𝔖_T(R)} S — events possible in at least one admissible
  state (law/subsidiary-theory level).
- S_s ∈ 𝔖_T(R) — the actual state's positive-probability support (state-level).
- P_T(R) \ S_s — events structurally possible in the realization but zero-weight in
  that state. This recovers exactly the three-way distinction G0 exposed; the
  p=0-but-possible boundary (R15c) is treated as a **consequence to check**, not the
  first law target.
- A scenario-level object 𝔖_T(Σ) = ⋃_{R ∈ Real_T(Σ)} 𝔖_T(R) exists only secondarily,
  as a **comparator object** — the bare cover does not give it.

## 3. Structural closure properties (exact hostile controls, pre-amplitude)

- **Mixing-union.** For probability distributions p, q on a finite outcome set and
  0 < λ < 1: Supp(λp + (1−λ)q) = Supp(p) ∪ Supp(q) — proved directly (§7, 3a);
  **nonnegativity is essential** (for signed/quasi-probability objects cancellation
  breaks the ⊇ direction: p=(2,−1), q=(0,1), λ=1/2 gives r=(1,0)). Consequence, for a
  fixed realization with an affine state-to-behaviour map (true by definition in
  GPTs): the admissible-support family is **closed under contextwise unions of whole
  realized families** (S(ρ₁) ∪ S(ρ₂) ∈ 𝔖_T(R), simultaneously across all contexts,
  via any proper mixture). Exact limits (§7, 3b): **no downward closure** (a subset of
  a realized support family need not be realized — supports cannot in general be
  shrunk); **no intersection closure**; nothing beyond unions of *whole realized*
  families; and it does not say every union-closed family is realized.
- **Product realizations.** For an **independent product state** on a product
  realization, supports factor contextwise: Supp(p ⊗ q) = Supp(p) × Supp(q).
  **Correlated joint states are not covered** — and it is correlation, not
  entanglement per se, that breaks factorization: a classically correlated separable
  state (e.g. an equal mixture of |00⟩ and |11⟩ measured locally) already has
  non-product support {(0,0),(1,1)}. The product rule constrains only the independent
  sector (§7, 3c).

Any candidate law's admissible-support family must respect both, and both are checkable
exactly on finite scenarios before any weight is discussed.

## 4. The support-level quantum/post-quantum line (owner correction 2)

The key fact for the charter: **the quantum/post-quantum distinction already appears at
the support level**, so Frontier A can face the post-quantum control without weights.
Source grades below (§7). The control structure:

| Control | Pattern | Verdict required of the law |
|---|---|---|
| A-H | Hardy support, (2,2,2) — quantum-realizable, logically (possibilistically) contextual, not strongly contextual (explicit global section exists) | **ALLOW** |
| A-PR | PR-box support, (2,2,2) — strongly contextual; the only strongly contextual no-signalling (2,2,2) models are the 8 PR boxes (Lal, Prop 6.2 of arXiv:1102.0264), and PR boxes are not quantum-realizable | **FORBID** |
| A-GHZ | GHZ support, (n,2,2) for n ≥ 3 — quantum strong contextuality (the all-versus-nothing paradigm) | **ALLOW** |
| A-KS | A Kochen–Specker / Peres–Mermin strong-contextuality configuration (every quantum model on the cover strongly contextual) | **ALLOW** |

**The verified boundary (corrected post-ruling; §7 claim 1b).** The owner's removal of
the "bipartite ≥3-*settings* strong contextuality" positive control was right — more
settings alone are not the resource: **no two-qubit state, and no bipartite state with
a qubit on one side, admits strongly non-local behaviour with any finite number of
local measurements** (Brassard–Méthot–Tapp 2005, Thm 1; re-proved in arXiv:1705.09312).
But the blanket premise "no bipartite quantum-realizable behaviour is strongly
contextual" is **CONTRADICTED by the verified literature**: bipartite quantum strong
contextuality **exists at local dimension ≥ 3** — Heywood–Redhead's two-qutrit KS-EPR
construction (1983); bipartite pseudo-telepathy, whose minimum entangled dimension is
exactly 3×3 (BMT 2005); every bipartite perfect quantum strategy defines a KS set
(Cabello, arXiv:2311.17735). The CSL 2015 sentence asserting the blanket absence
out-proves its own citations (which cover (2,2,2) only) and conflicts with
Heywood–Redhead; the charter must use the verified scope. Overall, the minimum total
dimension for quantum strong non-locality is 2×2×2 = 8 (three qubits), below 3×3 = 9.

**The dividing line is therefore a dimension threshold, not a party count** — an even
harder-to-fake gate. The structural challenge stands in sharpened form: whatever rule
excludes the (2,2,2) PR supports cannot simply forbid strong contextuality (GHZ and KS
must survive), and cannot encode a party-count rule either (bipartite strong
contextuality is quantum-legal at 3×3).

**Stretch gate (restated to the verified boundary):** reproduce the absence of quantum
strong contextuality in (2,2,2) and in any bipartite qubit-on-one-side realization,
while permitting it for bipartite local dimension ≥ 3 and for n ≥ 3 qubits.

**Flagged for owner decision (this corrects a ruling premise, so it is not adopted
unilaterally):** an optional additional positive control **A-BQ** — a bipartite
dimension-≥3 strong-contextuality support (two-qutrit KS-EPR, or the magic-square
bipartite game support) → **ALLOW** — would pin the dimension threshold from both
sides. Owner to confirm A-BQ and the restated stretch gate.

## 5. Pass/fail gates (revised per owner)

- **A1 — Output.** The law produces an admissible-support family 𝔖(P) from a declared
  physical/task structure P, **without** inserting Hilbert orthogonality, GPT cones,
  exclusivity axioms, or quantum-lattice (orthomodular/Piron/Solèr) axioms.
- **A2 — Classical control.** Appropriate classical/global-section supports are
  recovered.
- **A3 — Quantum controls.** Hardy (2,2,2), GHZ strong contextuality (n ≥ 3), and at
  least one KS/Peres–Mermin strong-contextuality example are **included**.
- **A4 — Post-quantum control.** The PR support in (2,2,2) is **excluded**. Stretch
  (dimension-scoped per owner ruling 03 [IR1]): FORBID bipartite perfect/strong
  nonlocality when either local quantum system is only a qubit, even allowing
  generalized measurements (the BMT lower bound is proved for POVMs); ALLOW at least
  one bipartite 3×3 strong-contextual/perfect quantum support; ALLOW multipartite
  2×2×2 GHZ-type strong contextuality — **without encoding any of these as a
  scenario-name, party-count, or dimension lookup table.**
- **A5 — Discipline.** Representation invariance, restriction/coarse-graining,
  composition (incl. §3's closure properties), and R1–R15.

**Kill conditions.** If A3 + A4 are achieved only by inserting Hilbert orthogonality, a
hand-written "no bipartite strong contextuality" exception, or scenario-specific
labels/exceptions → **RELOCATED**. If the law collapses onto Local Orthogonality, a
lattice reconstruction, or another existing principle without an extra relation →
**RESTATED** (possibly a useful sector, but not a new law).

## 6. Baselines for the comparator audit

- **Abramsky–Brandenburger possibilistic hierarchy** (probabilistic ⊂ logical ⊂ strong
  contextuality) and all-versus-nothing arguments — the exact language for support
  patterns. arXiv:1102.0264.
- **Kochen–Specker sets** (Peres–Mermin square; Cabello's 18-vector set) —
  state-independent, support-level no-goes.
- **Local Orthogonality** (Fritz et al.) — **classified per owner correction 3 as an
  event-orthogonality/composition comparator adjacent to Frontier A, not a support-only
  null theory**: LO is fundamentally a probability inequality (Σ_{e∈C} p(e) ≤ 1 over
  pairwise-exclusive events), not a Boolean rule for supports; a single PR box passes
  it while two copies violate it, so the comparison must be done at the declared copy
  number. This classification prevents smuggling quantitative information into the
  qualitative campaign.
- **Quantum-logic reconstructions** (orthomodular lattices, Piron, Solèr) — generate
  quantum possibility structure by positing lattice axioms; a GRUT support law that
  reduces to them is RESTATED.

## 7. Source grades for the load-bearing literature claims

Graded per program discipline (the campaign may lean only on claims at their verified
scope; anything PARTIAL or weaker is owner-reviewable before charter freeze).

Verification run 2026-10-06, three independent agents reading primary texts (arXiv
full texts, LIPIcs PDF, publisher pages) from this environment; every quote below was
read, not recalled.

| # | Claim | Grade | Verified scope / caveats |
|---|---|---|---|
| 1a | Only strongly contextual no-signalling (2,2,2) models are the PR boxes | **VERIFIED** | arXiv:1102.0264 §6, Prop 6.2 (Lal), read verbatim. Cite **the Proposition, not the paper's Introduction** (the intro drops the (2,2,2) qualifier and overstates). Provenance caveat: Lal's result traces everywhere to *private communication*; the first published proof is constructive, in Mansfield's Oxford thesis (Prop 2.6.4) and PRA 95, 022122 (2017) = arXiv:1608.07299 (Prop IV.1). |
| 1b | "No bipartite quantum-realizable behaviour is strongly contextual" (blanket) | **CONTRADICTED** | The sentence exists in print (CSL 2015, LIPIcs 41 §2.1 = arXiv:1502.03097) but out-proves its own citations (Lal: (2,2,2) only; Mansfield 2014: Hardy completeness families). Proven absences: (2,2,2) (Lal + PR not quantum-realizable); **two-qubit states, and any bipartite state with a qubit on one side, admit no strongly non-local behaviour** (Brassard–Méthot–Tapp, QIC 5(4):275, 2005, Thm 1; re-proved as Thm 1 of arXiv:1705.09312, which also notes the Schmidt-decomposition extension). Proven presence: **bipartite quantum strong contextuality exists at local dimension ≥ 3** — Heywood–Redhead, Found. Phys. 13:481 (1983) (two-qutrit KS-EPR; cited as such by arXiv:1705.09312 fn. 1); bipartite pseudo-telepathy needs entangled dimension ≥ 3×3 and this is optimal (BMT 2005); every bipartite perfect quantum strategy defines a KS set (Cabello, arXiv:2311.17735). Minimum total dimension for quantum strong non-locality: 2×2×2 = 8 (three qubits). |
| 1c | Hardy (2,2,2): quantum-realizable, possibilistically non-local, **not** strongly contextual | **VERIFIED** | arXiv:1102.0264 §6, witnessed constructively (the global assignment {a↦1, a′↦0, b↦1, b′↦0} lies in S_e). Terminology: AB 2011 "possibilistically non-local" = CSL 2015 "logically contextual". Hardy's PRL 71:1665 itself APS-paywalled from here; realizability confirmed via the secondary sources. |
| 1d | GHZ (n,2,2), n ≥ 3: quantum strong contextuality | **VERIFIED** | arXiv:1102.0264 §6, Prop 6.1 ("strict hierarchy Bell < Hardy < GHZ"). The term "all-versus-nothing" is from CSL 2015 §4 (attributed to Mermin), not 1102.0264. |
| 2a | Hardy-type structure complete for possibilistic nonlocality in (2,2,ℓ) and (2,k,2) | **VERIFIED** | Mansfield–Fritz arXiv:1105.1819 = Found. Phys. 42(5):709 (2012), abstract + §V read. Precision: in (2,2,ℓ), ℓ>2, completeness needs **coarse-grained** Hardy paradoxes; plain Hardy suffices in (2,k,2). Completeness **fails** beyond these families — explicit (2,3,3) counterexample in the paper; (3,2,2) also known to fail (GHZ). |
| 2b | LO: single PR box passes; two copies violate | **VERIFIED** | arXiv:1210.3018 = Nat. Commun. 4:2263: "LO¹ = NS, in the present **bipartite** setting" (proved for bipartite only; for ≥3 parties LO¹ is already strictly stronger than NS); 2 PR copies violate LO². Single-copy PR satisfaction is immediate from LO¹=NS, not a standalone sentence in the paper. |
| 2c | LO is a probability inequality, not a support-level rule | **VERIFIED** | The paper's own formulation: orthogonality relation is combinatorial, but the principle is Σ p(eᵢ) ≤ 1 over pairwise-exclusive event sets (maximal cliques). The "not purely possibilistic" gloss is ours (accurate to the formulation; the paper never discusses the contrast). |
| 2d | KS / Peres–Mermin: state-independent, support-level strong contextuality; Cabello 18-vector set exists | **VERIFIED** | arXiv:1102.0264 §6 defines strong contextuality at support level (S_e = ∅) and §7 factors KS-type results through it ("every quantum model for this set of observables … is strongly contextual" — the literal phrase "state-independent" is Cabello's, not §7's). |
| 3a | Supp(λp+(1−λ)q) = Supp(p) ∪ Supp(q), 0<λ<1 | **VERIFIED (proved)** | Elementary; **nonnegativity essential** (signed counterexample above). Per-context in an empirical model. |
| 3b | Mixing-closure of the admissible-support family | **VERIFIED (proved)** | Requires an affine state→behaviour map (definitional in GPTs). Closure under contextwise unions of **whole realized families** only; no downward closure; no intersection closure. |
| 3c | Product-support rule | **VERIFIED (proved)** | Independent products only; **correlation (not entanglement per se) breaks factorization** — classically correlated separable states already fail it. |
| 3d | Citation identities (1102.0264 / 1105.1819 / 1210.3018 = NComms 4:2263) | **VERIFIED** | All three title/author/journal pairings confirmed against the arXiv pages. |

## 8. Reconnaissance computation (staged; before any law — owner-weakened form)

For the (2,2,2) scenario:
1. Enumerate all Boolean support tables satisfying possibilistic no-signalling.
2. Classify each as global-section/noncontextual, logically contextual, or strongly
   contextual (exact, combinatorial).
3. Identify the known anchor classes: deterministic/classical supports; quantum Hardy
   supports; strongly contextual PR supports.
4. **Only then**, as a separate question, ask which remaining Boolean patterns have
   quantum realizations — "possibilistically nonlocal" and "quantum-realizable" are
   different classifications and are not preregistered as one. (Combinatorial
   leverage: Hardy-completeness for possibilistic nonlocality holds exactly in the
   (2,2,ℓ) — via coarse-grained Hardy paradoxes — and (2,k,2) families, and **fails**
   beyond them ((2,3,3) counterexample; (3,2,2)); §7 row 2a. So the leverage applies to
   the (2,2,2) reconnaissance and its two nearest families, and must not be assumed for
   wider scenarios.)

This yields the exact target set a support law must reproduce in the smallest scenario.

## 9. Judgment standard (phase change — binding)

Per `F0_OWNER_RULING_02.md` §3: Frontier A must **attempt an actual generative
principle or prove that such a principle cannot be obtained from the surviving
primitives**. A campaign whose only result is "known framework X needs input Y" is not
permitted; that job is done. The gates above are finite, exact, and cannot be passed by
a filter: a law passing A3+A4 must encode *why* the quantum-admissible support classes
change across the verified local-resource boundary — without inserting Hilbert
dimension, party count, setting count, or scenario labels by hand [IR2] — real
structure. Expected difficulty is acknowledged: quantum possibility
structure normally comes from Hilbert-space geometry; generating it without that
geometry is exactly where GRUT would have to invent something. Success would be a
genuine result; failure at these gates sharply narrows the search — both are
publishable outcomes under the program's standards.

## 10. STOP

Charter input only. The Frontier A charter (scope, terminals menu, firewalls, hard
stop) is written separately, on owner authorization, building on this document and
subject to R1–R15.
