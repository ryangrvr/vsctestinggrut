# CR-2 queue — loopholes found after the freeze (UNAPPLIED)

**Status (G2-13 item 3, binding):** not applied now, and preregistered as a binding
design constraint. Card authors design as if all seven items apply. An item is
skeptic-verified and applied (tightening only, rescoring toward failure) the first time a
card's verdict depends on it. Recorded originally under owner ruling G2-12 ("Record
loopholes in a CR-2 queue, unapplied (tightening stays available under §19.2)"). Each item tightens a
rule, so it can be applied at any time, including after Card 1 (rescoring moves only
toward failure). Every pattern below is an abstract CHARTER TEST; none is a candidate
law. The §24.1 presumption already covers them as working-record patterns.

## From round A, loopholes lens (workflow run `wf_959efb57-3b2`; the only lens that completed)

| # | Severity (as reported) | Clause | Pattern | Proposed tightening (reporter's wording, unverified) |
|---|---|---|---|---|
| Q-1 | BLOCKER | §2.5 b_J | **Thin-band pin.** Near-regime fibers (BP-4, §13.5) make FB a thin band; a pin inside it earns p★ = 10 bits per instance although the real reduction is about log₂(band/cell) | A codimension is worth p_w := min(p★, ⌊log₂(w/ρ)⌋) bits, w being the certified width of the baseline across Z(ℛ★) |
| Q-2 | BLOCKER | Q5 split; NR-17(b); Q3(c) | **Sheltered exception.** Universal tests are evaluated on card-chosen instances (AI-1, lock fibers), so a rare input feature shelters the law | Credit instances on which the Q5 or NR-17(b) condition holds are removed from N_fib; Q3(c) also runs on AI-5 instances |
| Q-3 | MAJOR | §1.4 decision semantics (Q3(b), Q3(c), NR-12(c), NR-17(b)) | **Loose-enclosure shield.** Undecided ε enclosures count as "ℛ★ does not hold" in tests that fire against the card | Where ℛ★ holding fails the card, ℛ★ counts as holding wherever it is not certified to fail |
| Q-4 | MAJOR | Q3(c) realized-structure substitution | **⊥-guarded extractor.** A ⊥ branch keyed to a feature standard draws lack forces substitution and guaranteed non-hits | The auditor may also run the component with its ⊥ branches replaced by their alternatives |
| Q-5 | MAJOR | Q5, §2.5 (u) | **Relabelled statistic.** "Declared interface statistic" is undefined, so an environment-internal quantity can be declared as interface | An interface statistic is a functional of the block-membership process only, computed by a priced component under PC-6 |
| Q-6 | MAJOR | §2.2 θ_dict; §2.5(b) | **Blind dictionary.** A θ_dict that passes no inputs prices every comparison class out | M may receive inputs through any dictionary an auditor exhibits with L_stmt ≤ L_stmt(θ_dict) + c_dec |
| Q-7 | MINOR | §13.2 RH-KMS, RH-MR; STD-4(a) | **Parity mislabel.** Declared time-reversal parities decide the surrogates | Parities chosen by the auditor |

Further loopholes found by the CR-1 round are appended below.
