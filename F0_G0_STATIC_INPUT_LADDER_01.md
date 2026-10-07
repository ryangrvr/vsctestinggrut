# F0 G0 — STATIC INPUT LADDER 01
**Status:** campaign artifact. Results per level, computed exactly (`f0_g0_solver.py`,
rational arithmetic, no floats). Scenarios: K0 complete classical, K1 path, K2 Specker
triangle, K3 Bell four-cycle (re-instantiated Exec-01 objects; historical artifacts
unmodified).

## G0-A — C only

The bare compatibility complex contains **no event data**: no outcome alphabets, no
sections, nothing for weights to attach to. The identifiability question is degenerate —
there are no probability variables at all. **Result: C alone determines nothing about
weights (structurally).**

## G0-B — C + E (normalization + no-disturbance only)

Exact computation of the admissible affine space (variables = one probability per
context-section):

| scenario | variables | rank | free parameters (affine dim) | classification |
|---|---|---|---|---|
| K0 complete classical | 8 | 5 | **3** | polytope |
| K1 path/acyclic | 14 | 9 | **5** | polytope |
| K2 Specker triangle | 18 | 12 | **6** | polytope |
| K3 Bell four-cycle | 24 | 16 | **8** | polytope |

In every case a continuum of admissible models. The empirical-model consistency constraints
(normalization + no-disturbance) remove only the "obvious" freedom; substantial statistical
freedom remains. **Result: C + E does not identify Γ.**

## G0-C — C + E + SUPPORT

- **Full support** (all sections allowed): identical dimensions as G0-B — full support
  adds nothing, as expected. Support ≠ weights at the trivial end.
- **Restricted support (the interesting case):** support zeros act as additional equality
  constraints:
  - K2 with **correlated-pair support** (each pair context allows only same-value
    sections): affine dim drops 6 → **1**. Support *does* remove freedom.
  - K2 with **anti-correlated support** (pairs only allow different-value sections):
    affine dim drops 6 → **0** — **UNIQUE**. The anti-correlated K2 empirical model is
    forced entirely by support plus consistency. (Note: this is exactly the nonextendable
    K2 configuration from Phys-02's calibration — unique up to its single distribution.)

**Result: the support layer can remove arbitrary amounts of freedom — down to uniqueness
in special cases — but which support obtains is itself unforced data.** This is C1-class
behavior in general, C4 in special instances.

## G0-D — C + E + SUPPORT + EVENT RELATIONS

Where declared relations exist (exclusivity among distinct sections of one context;
normalization partitions already present), they constrain *regions* of the polytope
(e.g. sum rules over exclusive events reduce dimensions further) but the campaign did not
find — without importing an external theory — any principle that would fix which
exclusive-algebra structure a given scenario "really" has beyond what the support and
alphabets declare. **Result: relations constrain but do not identify, unless imported with
a theory attached (G0-E).**

## G0-E — richer structure (comparator only)

What the richer frameworks add, exactly (detailed in baseline audit):

- **Hilbert/projective lattice + additivity (Gleason-type):** the entire geometric +
  measure-theoretic apparatus; produces the Born measure class. The added structure is the
  whole content.
- **GPT state/effect cones:** likewise — probability rules come from the cone geometry
  supplied.
- **CT probability (Marletto):** decision-supporting weights derived only under
  superinformation-theory conditions — additional structure again.

**Common thread: in every comparator, the step from possibility/compatibility to
statistics is bought with substantial extra structure. None of them derives statistics
from a bare compatibility complex.**

## Ladder conclusion

Freedom removed by static structure, per level: G0-A none (degenerate) → G0-B only
consistency → G0-C support-dependent (arbitrary; up to uniqueness in special cases) →
G0-D relations constrain regions → G0-E full theories derive statistics by importing
geometry. The identifiability question thus has a sharp answer: **static possibility
structure does not, in general, identify Γ — except when a special (and itself unforced)
support happens to be strong enough.**
