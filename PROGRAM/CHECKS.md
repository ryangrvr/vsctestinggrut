# CHECKS — commits awaiting external review

The rule is RULES rule 8.
- **Lines.** One line per pushed commit that contains a result, a proof or a status
  change. A line is added only after the commit is verified on the remote
  (`origin/grut2`).
- **Status.** One of: `pending` · `checked: ChatGPT` · `checked: Claude` ·
  `issue found` (with what, and the fixing SHA when there is one).
- **Gate.** Nothing is banked, killed or status-changed on `SCOREBOARD.md` or
  `GRAVEYARD.md` until the line shows at least one external check with no open issue.
- **Who edits.** Claude Code adds lines; the owner or checker updates the status.

| SHA (grut2) | Claims | Status |
|---|---|---|
| `2eda8fb` | R1 definition v1 (`RESULTS/R1/R1_DEFINITION.md`): d_op = W₃ on per-time-standardized laws, T = E₂±. Prop 1: ε_R is the Chebyshev radius in the T-quotient, = 0 iff one orbit. Prop 2: skewness and correlation witnesses with data-computed constants. Prop 3: TV/W₁/W₂ admit no skewness bound. Cor 4: BRI1 ⇒ ε_R^(E₂±) > 0 under BRI1's quantifiers. | pending |
| `edd274c` | (VS Code) WO-001 C1 redo: γ₁ from finite-N_B dynamics with ε = N_B^(−1/2); N_B·γ₁ flat (relative spread 1.4e−7), √N_B·γ₁ not flat; faithful transfer of BRI1's archived V3-R2 numbers. | pending |
| `bc113f3` | (VS Code) WO-001 C2 exogenous controls: C2-G witness 0; C2-NG ε_R = 0 (exact control, 4.4e−16); C2-F witness 0.294556 under E₂±, 0 with calibrated filters. | pending |
| `34230e1` | Review 2 (status change): C1 redo ACCEPTED; C2 numbers reproduced, process REVISE; C2-F reframed (E₂± not closed under calibrated linear filters); identifiability flag (~10¹¹ samples). | pending |
| `1892ca0` | R1 v2 interface ladder (`RESULTS/R1/R1_T_LADDER.md`): Theorem A quotient form for E₂± / T_caus / T_lin; Prop B Mardia and innovation witnesses; Theorem C (BRI1 escapes every linear interface class); Prop D (T_mono absorbs a single time, multi-time OPEN); Prop E (unrestricted T trivial); WO-002 issued. | issue found — owner review (Ruling G2-01): Theorem C confirmed as stated; its mode-preservation (latent-dimension) hypothesis was implicit and must be an explicit, priced part of T. Fix: `82d311e` (common carrier, §10). |
| `82d311e` | R1 freeze v3 (`RESULTS/R1/R1_T_LADDER.md` §0, §§8–10; rulings G2-01…G2-08). Claims: Theorem A-BL (BL quotient after center + whiten, min over O(k)). Theorem F (dist_BL(P, sym) = ½ d_BL(P, −P) = sup_odd |E f|, constant 1, sharp; two protocols: ε_R = ½ d_q exactly; so ε_R ≥ ½|E f_odd|/‖f‖_BL). M1 (T_mono: ε_R = 0 ⇔ all copulas in one reflection orbit). M2 (radial-symmetry certificate). M3 (Gaussian tangent: rank J = k, C(k+2,3) − k). Theorem C under the common carrier. E1 (protocol-dependent carriers make linear T trivial). E2 (two-mode counterexample). BRI1 Tier 1 R1-PASS (Theorem C + carrier certificate) — banked by G2-08, SCOREBOARD entry gated here. Also: C2 results + report, noise-floor correction, Review 2 erratum; WO-002 preregistration (script, before results). | pending |
