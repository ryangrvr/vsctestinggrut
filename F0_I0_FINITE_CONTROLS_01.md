# F0 I0 — FINITE CONTROLS 01
**Status:** campaign artifact. Results of `f0_i0_controls.py` (all exact; interface
semantics only). Each control instance declares its possibility facts as **model inputs**
(in a real campaign these would come from the subsidiary theory) and the complex is
**computed** from them via the declared interface definition.

## Results (all pass)

| control | setup | expected | result |
|---|---|---|---|
| **I0-K0 complete** | all three measurers share one joint measurer | complete simplex | ✅ all nonempty subsets present |
| **I0-K1 incompatible pair** | M1, M2 individually measurable, no joint measurer (complementary pair) | singletons only | ✅ exactly 3 singleton contexts |
| **I0-K2 Specker triangle** | three pair joint measurers, **no triple** | pairs + singletons, no triple | ✅ — the decisive control: the interface admits pairwise-without-triplewise **when the declared possibility facts come from a general (POVM-type) subsidiary theory** |
| **I0-K3 four-cycle** | four measurers, cycle pairs only | 4 cycle pairs + singletons; diagonals and higher sets absent | ✅ |
| **I0-K4 sharp control** | sharp-sector possibility facts: pairwise ⇒ triple | triple forced | ✅ — no Specker triangle in the sharp sector |
| **contrast** | same interface definition, different subsidiary facts | different complexes | ✅ — K2 and K4 both hold: the complex is determined by **subsidiary-theory possibility facts**, not by CT base principles alone |

## Downward-closure theorem: mechanically verified

The theorem proved in `F0_I0_Interface_Definition_01.md` (joint measurer for S + allowed
coarse-grainings ⇒ joint measurer for every nonempty S′ ⊂ S) was checked mechanically on
**every** control instance: no downward-closure violation occurs in any declared-consistent
model. The induced object is always an F0-A context complex — the interface lands in the
right kinematic carrier.

## What the controls establish (and do not)

- The interface definition is **coherent** and produces well-formed context complexes.
- The **Specker triangle is representable at the interface** — but only because the
  possibility facts (which joint measurers exist) were *declared as inputs* mimicking a
  general-POVM subsidiary theory. Base CT alone does not supply these facts (comparator
  audit: base CT has no higher-order hierarchy or unsharp calculus). **The controls
  therefore do not show that CT derives the Specker triangle; they show the interface can
  carry it once a subsidiary theory supplies the facts.**
- The K2/K4 contrast encodes the PVM-vs-POVM distinction at the interface level — the
  same finding as the quantum joint-measurability baseline, now transported through the
  CT-language interface.

## Not done (firewall)

No Γ coupling, no probabilities, no dynamics, no fitting, no Born rule, no access
evolution.
