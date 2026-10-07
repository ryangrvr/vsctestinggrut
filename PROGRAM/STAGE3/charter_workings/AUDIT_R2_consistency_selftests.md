# Pre-freeze audit, round 2: dispositions, consistency, self-tests, feasibility, freezability

**Audited:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (2648 lines, untracked) in `/tmp/claude-0/mainwt`, branch `grut2-stage3` at `86bf5a0` (= `main` = `origin/main`).
**Against:** `charter_workings/FREEZE_VERIFICATION.md` (§3 dispositions), the four `AUDIT_R1_*.md` reports, G2-11 (`OWNER_RULINGS.md`), R1_SYNTHESIS §1/§6/§9/§12, R1_T_LADDER §1–§2, CHECKS, SCOREBOARD, GRAVEYARD, F0_SD0_RESULT, and v1 (`CHARTER_V1_WITH_LEDGER.md`) where the charter cites it.
**Mode:** read-only. No repository file was edited. Scratch arithmetic: `scratchpad/s3/r2_arith.py`, `scratchpad/s3/xref.py`.
**Constraint kept:** no candidate law is proposed, sketched or exemplified. Every pattern below is the charter's own abstract pattern or a known object the charter names.
**Line numbers** ("L###") refer to the current charter file.

Severity: **BLOCKER** = must fix before freezing · **MAJOR** · **MINOR**.

---

## Part 1. Task 1: BLOCKER and MAJOR dispositions marked Applied

**Confirmed in the text** (clause cited):

| Finding | Where the fix is |
|---|---|
| B-B1 | Header L16–17; FZ-1 L2144–2148; §18.1 step 2 L2106–2107; §25 L2455–2456; FREEZE_VERIFICATION.md exists (but see F-6: its §7 is a placeholder) |
| B-B2 | §1.4 L303–315 ("R1's frozen tiers are T_R1 = T_lin … and T_mono"; "charter catalogue classes, not R1 tiers"; BL convention for E₂±, T_caus). "frozen tier" now occurs only at L303 and in D-10 |
| B-M3 | DEF-4 L1539–1542 |
| B-M4 | §1.4 L317–320 (J, T_univ defined; "R1 makes no claim"); §15.6 L1929–1932; CT-14 L2355 |
| B-M5/M6 | §2.3 L477–486 (no branch; 𝒜_Π^hand never reduced) |
| B-M7 | δ_RH defined once, §13.2 L1597–1602; used in BP-4, BP-6, §1.5, §13.5 |
| B-M8 | XS-7 L1434–1437 |
| B-M9 | Q9 L684–687 |
| B-M10 | MC-9 L794–797; BU-7′ L1259–1261 (Appendix A row not updated: F-7) |
| B-M11 | BU-6 L1241–1245; §15.9 L1967–1971 |
| B-M12 / C-B3 | §1.5 L358; IP-13 L918–920; App. A L2479 (N_AI3 = 160) |
| B-M13 | §1.5 L380–383; App. A L2485 |
| B-M14 | MC-4 L751–753 |
| B-M15 | BU-8 L1264–1266 |
| B-M16 | T-1 L1458–1464; §24.2 convention L2431–2436 (rows ST-8/ST-9 inconsistent with it: F-2) |
| A1-1 / A2 F-5 | BP-5 L436–450; C13 L2088 (Θ_std) |
| A1-2 | NR-17(a)/(b) L1148–1159; NR-4 "appears" L1039–1041; CT-77 L2418 |
| A1-4 | §2.5 fixed-T fibers L537–540 |
| A1-5 | Q4 L655–658 |
| A1-6 | §15.3 L1852–1855; §5.5 L1180–1181; DIF-5(e) L1986–1988 (S4 terminal unnamed: F-15) |
| A1-7 | §15.5 L1906–1909; MC-9 L798–800 |
| A1-8 | App. D D-10 to D-13 (D-13 misdescribes the size test: F-13) |
| A1-11 | Q3(c) L639–643; NR-10(n) L1117–1119; C12 L2087 |
| A1-12 | Q5 L669–672 |
| A1-13 | §1.3 L276–281 (provenance test) |
| A1-14 | §1.4 (iv) and coverage L330–338 |
| A1-15 | PC-7(b) L206–211 |
| A1-16 | NR-7 L1067–1073 |
| A2 F-1 / C-B1 | §2.3 L481–486; NR-6 L1060–1062; §15.7(viii) L1942–1944; §21.2 L2291–2292 |
| A2 F-2(b) | NR-5 L1052–1054 (but the IP-7 price it invokes is undefined: F-4) |
| A2 F-6 / C-B2 | IP-6 L875–882 (4 bits per canonical item). New closure wording creates F-5; the old ΔF_tgt survives orphaned in IP-7 (F-4) |
| A2 F-7 | §4.3 L945–947; §4.4 L951–955; KU-11 L1303 |
| A2 F-8 | §2.5 L561–563; Q6 L676–677 |
| A2 F-9 | §1.5 L362–369; §2.5 L571 |
| A2 F-10 / C-M1 | IP-4 L863–867; IP-14 L921–924; IP-1 L853–854 |
| A2 F-11 | BU-6 L1251–1253; App. A L2507 |
| A2 F-12 | §15.2 L1838–1844 |
| A2 F-13 | PC-6 L186–188; NR-4 L1041–1042 |
| A2 F-14 | §1.3 L245–254 |
| A2 F-15 | §2.5 L556–560 |
| C-M2 | IP-12 L908–917 |
| C-M3 | §1.5 L362 |
| C-M6 | Q3(a) L623–631 |
| C-M7 | OR-6 L1382–1388 |
| C-M8 | §15.1 L1828–1830; §15.2 L1845–1846 |
| C-M9 | NR-10(f) L1093–1100 |
| C-A1/A2 | BU-6 L1241–1247; §15.9 L1967–1971; §23 L2321–2322; §18.1 step 3 L2108–2111 |

**Not applied as recorded, or applied inconsistently:**
- **A2 F-4 (round-1 BLOCKER), A1-10, C-M5.** The family cap and c_J(b) are in the text, but the Price(M) definition makes them inoperative for every card whose Π no RB/SPS template returns. The same definition admits a hostile reading that zeroes b_J for every card. C-M5's "any L₀ rule priced as a component" was not adopted, and v1's NULL-M guard ("published before the freeze and stated without reference to the card") was dropped without an Appendix-D row. → **F-1 (BLOCKER).**
- **C-B5 / B-M16.** The convention is applied, but ST-8 and ST-9 now name terminal S5, which T-1 contradicts (→ **F-2, BLOCKER**). ST-6 and ST-11 are underdetermined because NR-17 runs at S3 (→ **F-3, MAJOR**).
- **C-B4.** The arithmetic is right. "Tuning never pays" depends on F-1, and "below about 990" ignores the binding p = 16 test (F-9).
- **A1-3.** Applied in A2 F-1(c)'s form; A1-3's "beyond the IP-14 price of the ontology choice" was dropped. The drop is correct, since it would exceed the 16-bit maximum. The record should say "modified", and D-13 should not say "restored" (F-6, F-13).

---

## Part 2. Task 2: consistency after the edits

**Leftover search** (whole file):

| Term | Result |
|---|---|
| G (generated-structure credit), g(ι), "G caps", "G term" | None left. G appears only historically at L2541 and in D-1 |
| "Credited" | Only the §4.3 heading and CT-78's outcome "Credited once"; no formula uses it |
| "N_cred ·", "N_cred·" | None. b_J uses N_dist (L571) |
| 48 / 47 instances | None (the "48" at L2496 is R_item core-hours) |
| "frozen tier(s)" | Only L303 (R1's two tiers, correct) and D-10 (history). "tier" is still used loosely for catalogue classes (F-10) |
| batch / batch freeze | Only D-3 (v1 history) |
| Appendix C / F | Only as "v1 Appendix C/F" in D-7, D-8 (legitimate) |
| H vs H_hor | Two leftovers: C7 L2082 "H", and App. A L2471 "t₁ := H/4" (F-8) |
| κ vs κ_res | Clean: κ_res at L2034, L2053, L2496; κ_J/κ_ι/κ_f/κ_lock/κ_fam elsewhere |
| ΔF_tgt | Orphaned: used in IP-7 L892, defined nowhere (F-4) |
| ΔL vs ΔL₀ | Consistent in §4.3/§4.4/KU-11/§0.6/App. A/D-1; §15.9 L1972 mentions only ΔL (F-18) |

**Cross-references.** Scripted check: every § number resolves; Appendix references other than "v1 Appendix C/F" resolve (A, B, D, E, G); every ID family is gap-free (Q1–12, NR-0–17, DEF-1–17, STD-1–15, MC-1–11, BU-1–9, KU-1–13, IP-1–14, CT-01–87, ST-1–11, DIF-1–10, SEL-0–16, HB-1–12, D-1–13, …). Semantic spot-checks of about 120 pointers found no wrong target. The defects are: the undefined ΔF_tgt (F-4); C7's "NR-10(h)–(l)", which predates (m) and (n) (F-18); and the App. A note's pointer to FREEZE_VERIFICATION.md for an itemization that lives in AUDIT_R1_C §2.2 (F-9).

**Numbers against Appendix A.** Every "[A]" symbol in the text has a row. These agree: p★, r★/r★★ (m★★ = 5), δ_Π/η/δ_∂, w, b_Π, n_min, θ_gen, N_AI3, N_AI5, N_cred, N_ch, L₀ code (B.1 counts sum to 64), compression row (= §4.4 = KU-11), δ_RH, Q_min, N_max, platform time, α, power, c_dec/ℓ_dec/p_dec, ℓ_tr/b_patch, κ_res/R_item/R_card, B-CF (k ≤ 4), HB ranges, clocks, §2.4 counts (2961 = 1721 + 1232 + 8; 2721 = 1721 + 992 + 8). **One mismatch:** App. A "Lock thresholds | falsified beyond 3σ_eff; confirmed within 2σ_eff" against MC-9, which replaces 3 and 2 by z_obs = 3.32–3.62 and z_obs − 1 (F-7). The "In-silico budget" row is referenced nowhere (F-18).

---

## Part 3. Task 3: self-tests under T-1 and the §24.2 convention

| ST | Mark | Reason |
|---|---|---|
| ST-1 | **HOLDS** | S0–S2 pass by convention. In S3, both "Π, [h] supplied → NONGENERATIVE" and "Gibbs supplied and used by ℛ★ → RELOCATED" fire (§5.6). RELOCATED is listed first in §18.2 S3, so the terminal is S3 CARD-RELOCATED; NONGENERATIVE is recorded. In S5, Q3 fails (STD-3 BRI1 clause, §13.6, B-SRB RESTATED). Caveat: the recorded "STD-9" fires only if ℛ★ includes the 1/N_B rate, which the row does not say (F-12) |
| ST-2 | **HOLDS** | Terminal S3 RELOCATED: the Gaussian/Gibbs reference is used in deriving ε = 0. Recorded: S5 Q2 fails through DEF-15 (its own example: Gaussian families are T_caus/T_lin-separable); Q3 (STD-3 "harmonic baths are R1-NULL", STD-6); Q9 for scope Q (RS-4 forces scope Q for an ε-only relation). RS-1 is illustrative |
| ST-3 | **HOLDS**, one sub-clause FAILS | Terminal S1 CARD-GRAVEYARD (GY-6 by behavioural equivalence; no earlier card, so no VARIANT). S2 UNMEASURABLE (DC-8, ASP is a B-CF member, no weight rule) ✓. S8 NON-SELECTIVE through SEL-10 ✓. B-CF collapse at Hamming 0 ✓. But "SEL-4 admitted" cannot fire: SEL-4 is "FORBID all (as record-law supports) … automatic", and a completed card whose record laws obey STD-1 cannot realize those 240 supports. ASP admits them only as possibilistic tables (F-11) |
| ST-4 | **HOLDS** | Terminal S3 NONGENERATIVE (Π, [h], T declared supplied). Recorded S6 LOOKUP: Im = FB, so 𝓗 = FB ⊆ Z(ℛ★), c_J(a) = 0, b_J = 0, D_sel = 0, ΔL = −Price ≤ 0. This does not depend on c_J(b). Caveat: "any SFP model" could carry a PS-5 premise used by ℛ★, which would make the terminal RELOCATED (F-12) |
| ST-5 | **HOLDS** | Terminal S3 NONGENERATIVE: protocol-indexed readouts are PS-3 (NR-10(a), PC-6), and the record laws supplied in the latent are FR13 SUPPLIED. Recorded: carrier FAIL, MODE SELECTION (NR-11; HB-9), STD-12 |
| ST-6 | **UNDERDETERMINED** | The S5 path (RH-DB ⇒ STD-3/STD-4(a); Q3(e) STANDARD) is sound once reached. But NR-17 runs at S3: a reviewer may offer 𝒦₂ := "the generator satisfies detailed balance" (an R ⊇ Sol), on which the FDT/Onsager relation holds everywhere. JN therefore fires, giving S3 CARD-RELOCATED, whenever that predicate's L₀ statement is within c_dec of "Price(ℛ★ stated directly)". Neither length is fixed, and the latter is undefined. The row also does not exclude an NR-6 RB/SPS template recovering Π from 𝒞 on the generic lock fiber (S3 RELOCATED). CT-75 states STANDARD-IMPLIED for the same pattern, which conflicts with NR-17 → F-3 |
| ST-6′ | **HOLDS** | Detailed balance in 𝒞 is PS-5 used by ℛ★ → §5.6 RELOCATED (declared), or NR-12(b) RELOCATED (hidden) |
| ST-7 | Terminal **HOLDS**; recorded S6 clause **FAILS** | Terminal: an NR-6 SPS template on 𝒞 (RELOCATED), else CT-13 (NONGENERATIVE). Recorded "c_J = 0 by §2.5(b) with M the class itself and its uniform rule" fails. Price(M) admits only RB/SPS selectors, else a per-instance hand price, and no RB/SPS template returns T. So M, which is the card, is priced above the card and does not qualify (F-1). The recorded "(Q3(c))" is not guaranteed either: B-HB draws need not satisfy a class-specific relation, while Q3(e) fires for certain (F-12) |
| ST-8 | **FAILS** | The required terminal is S5 CARD-STANDARD. HB-2's partition, readout and bath are supplied by the model (NR-1, §5.6 "SUPPLIED, even when declared → CARD-NONGENERATIVE"), so S3 fails first. ST-1, on the same Duffing/BRI1 object, is correctly given terminal S3. Also, "at small amplitude" conflicts with the frozen template amplitude α = 1 SD (App. A L2471) → F-2 |
| ST-9 | **FAILS** | Same defect: the P-2 model's partition and detector readout are supplied, so the terminal is S3 CARD-NONGENERATIVE, not S5 → F-2 |
| ST-10 | **UNDERDETERMINED** | "Reachable at c_J = 1 for a compact card": arithmetic HOLDS, but the binding test is p = 16 (about 940–990 bits, not 990). "Comfortably at c_J = 2": HOLDS. "A tuned constant never recovers its price": not supported while F-1 stands, because a constant that ℛ★ pins on every instance is policed only by the family cap. "Tabulated card fails Q1 (UNFORCED)": it fails before SC2, but not necessarily at Q1. A table whose default is Sol = ∅ on uncovered post-freeze draws passes Q1 vacuously and fails KU-1 (S4 CARD-EMPTY) instead (F-9) |
| ST-11 | Target-level branch **HOLDS**; Ξ-level branch **UNDERDETERMINED** | Target-level: NR-2 → S3 RELOCATED ✓. Ξ-level: Q2 (DEF-15; Q2(c)) precedes Q5 in S5 order, so DEFINITIONAL is right if S5 is reached. But NR-17(b) at S3 fires with 𝒦₂ := the Ξ-level clauses forcing the Γ-restriction (D is definitional, so ℛ★ = D ∧ G holds on all of Dom_gate ∩ Sol(𝒦₂)), whenever those clauses are within c_dec of Price(ℛ★) → F-3 |

Tally: 6 hold (ST-1, 2, 4, 5, 6′ and the terminal of ST-3); ST-7 holds at its terminal; 2 fail (ST-8, ST-9); 3 are underdetermined (ST-6, ST-10, the Ξ-level branch of ST-11). In addition, recorded sub-clauses of ST-3 and ST-7 fail.

---

## Part 4. Task 4: feasibility (Appendix A note)

**Arithmetic.**
- Price range 216 + 50…60 + 50…80 + 300…600 + 45…90 + 24…38 + 15…40 + 16 + 3…10 + 0…70 = 719…1220 ✓.
- b_J = N_dist·p★·c_J = 1000 bits (c_J = 1) and 2000 bits (c_J = 2) ✓.
- Margins +280 to −220 and +780 to +1280 ✓.
- IP-6: 4 items × ⌈log₂ 16⌉ = 16 ✓.
- IP-13: log₂ C(160, k_ex) with k_ex ≤ 16 (θ_gen = 0.9) gives ≤ 71.8 bits, so "≈ 0–70" ✓.
- IP-14 as max(declaration, log₂ m) replaces the declaration ✓ (IP-1 L853–854).
- Minimum real literal at p = 10 is 12 bits ✓.

**Conclusions.**
1. "Reachable at c_J = 1 below about 990 bits" is supported at p = 10 only. b_J does not reprice ("p★ bits per codimension at every p"), but every real literal costs 6 more bits at p = 16. So with n real literals the p = 16 test, ΔL₀ > 0, requires Price(p = 10) < 1000 − 6n: 988 for n = 2, 940 for n = 10, 916 for n = 14. The p = 16 test binds for any card with at least 2 real literals (F-9).
2. "Comfortably at c_J = 2" is supported.
3. "Tuning never pays" is **not supported as written**. The stated reason (Q1 on post-freeze draws) defeats instance-specific tuning only. A single law constant that ℛ★ pins identically on all instances is the CT-78 pattern, and it is credited once only if the family cap binds. Under F-1 the cap does not bind for compact cards whose Π no RB/SPS template returns.
4. "Tables fail Q1 first" is supported as "fail before SC2", but the label may be KU-1 at S4 (F-9).

**Disguised kills (requirements impossible by construction, or under the CV-1 reading).**
- **F-1 (BLOCKER).** Two hostile readings of the c_J(b)/family-cap clause each zero b_J for almost every card:
  - c_fam is a minimum over an empty set, read as zero under CV-1 with §2.3's "contributes zero credit";
  - an auditor-built class "SFP class restricted to Z(ℛ★)", priced through "a priced rule".
- **F-4 (MAJOR).** The undefined ΔF_tgt in IP-7, read in its old axiom-deletion sense, prices the NR-5 asymmetry of any card whose 𝒞 type cannot be symmetric at the whole credit.
- **F-5 (MAJOR).** IP-6's closure-by-definability makes the classical record-law simplex "match" VB-6, so every selectivity result is RELOCATED and G-SEL fails for every card.

**Not kills.** The 4-bit IP-6 price, IP-13 at N_AI3 = 160 (≤ 72 bits), IP-14, N_dist ≤ 100 with family and lock-fiber caps, and the size test (≤ 16 bits available against b_Π = 6) are all reachable. One resource dimension the note does not check: about 160 AI-3 draws × 2 levels + 100 credit certificates + B-SEL × 3 levels + NR harnesses within R_card = 5000 core-hours averages about 10 core-hours per item. That is tight but not impossible.

---

## Part 5. Task 5: freezability and factual claims

- **Open decisions.** None blocks the freeze. App. A fixes every [A] symbol. D-8 leaves only OD-12 (kit authorization), which correctly follows owner review. FREEZE_VERIFICATION §5's four residual items are owner review items, not open rules.
- **Freeze preconditions still unmet.** FREEZE_VERIFICATION §6 says "See §7, appended after the round-2 audits", and no §7 exists. FZ-2 ("independent audits checked this text") is true only once round 2 is recorded (F-6).
- **Claims about the repository: verified.** `86bf5a0` = main = origin/main; `dbfd64b`, `0a9a941` (F0 requirements R1–R15), `82d311e`, `cb81a3b`, `aacbc52` exist; GY-1…GY-12 match GRAVEYARD order; SCOREBOARD #6/#9–#11 match PV-5; v1 is about 200 KB (203 684 bytes).
- **Claims about R1: verified.**
  - Two frozen tiers and their BL distances (R1_SYNTHESIS §1).
  - E₂± ⊂ T_caus ⊂ T_lin, E₂± ⊂ T_mono and T_lin ∩ T_mono = E₂±, with canonical forms and sign groups (R1_T_LADDER §1).
  - Zero-set-only monotonicity (§2).
  - No claim about the join (§9).
  - The §12 items, and the pending list A-BL, F, M1–M3, Prop. G and the D5 analyses (G2-11 addition 1).
- **Minor inaccuracies.**
  - PV-5 says "Theorems A and C … checked". Theorem C is checked (owner G2-01; `82d311e`). Theorem A's own CHECKS line (`1892ca0`) reads "issue found" (the issue is Theorem C's hypothesis), and A-BL is pending; R1_SYNTHESIS §6 says only "DERIVED" (F-14).
  - D-13 says the size test was "restored"; v1's test was different (F-13).
  - FREEZE_VERIFICATION §3 marks A2 F-4, C-M5, A1-3 and C-B5 "Applied" (F-1, F-2, F-6).
- **Candidate check: PASS.** No 𝒦 is proposed, sketched, named or exemplified. The self-tests use known objects, and the feasibility note counts sizes only.

---

## Part 6. Findings with replacement wording

### BLOCKER

**F-1. BLOCKER. §2.5 c_J(b), Price(M) and the family cap: inoperative for generated-Π cards under one reading, and a universal kill under the hostile reading. A2 F-4 (round-1 BLOCKER) is therefore not effectively applied.**
- **Location:** §2.5 L543–549: "(b) for every standard model class M that realizes Im ∩ FB … with constants fitted, Π, [h] and T fixed by hand or by a priced rule, and Price(M) ≤ Price(𝒦) … Price(M) := the IP-4 framework choice + L_stmt(M) + the IP-5 price of M's fitted constants + the price of the rule fixing Π, [h] and T (the cheapest RB/SPS selector returning them, else log₂|𝒜_Π^hand/G_ι| + log₂ 5 per instance)". §2.5 L564–569: "Family cap: c_fam := the minimum, over every standard class M with Price(M) ≤ Price(𝒦) that realizes Im ∩ FB on all of I_𝒦, …".
- **Problem.**
  - (a) No RB or SPS template returns T: §5.4 lists only partition selectors and, for [h], readout selectors. So the per-instance "else" term always applies to T, and to Π whenever no template returns the card's Π. Summed over the lock family or I_𝒦 (about 100 instances of 8–16 relata), it is 1031–1832 bits, T alone 232. That exceeds every card price in App. A (720–1220). For every card whose Π no RB/SPS template returns, which are the generated-Π cards the charter exists for, no M qualifies. Neither c_J(b) nor the family cap ever binds, so:
    - CT-78 (one shared constant × 100 instances) reopens;
    - App. A's "tuning never pays" loses its support;
    - ST-7's recorded "c_J = 0 by §2.5(b) with M the class itself and its uniform rule" fails, because the class's own uniform T rule is not an RB/SPS selector, so M is priced above the card that is M.
  - (b) Charging M per instance for the card's Π re-credits generation through the comparator. That contradicts §4.0 ("counting it would credit the card for compressing what it produced itself") and CT-76. c_ι already conditions on the card's (Π, [h], T_Π) at no price.
  - (c) When no class qualifies, c_fam is a minimum over an empty set. Under CV-1 together with §2.3 ("contributes zero credit on its axis"), b_J = 0 for every such card: a disguised kill.
  - (d) "fixed by hand or by a priced rule" contradicts the parenthetical price. Under CV-1 an auditor may use any priced rule. v1's NULL-M guard ("published before the freeze and stated without reference to the card", v1 §4.4) was dropped, and Appendix D does not record the drop. So an auditor-built class "SFP class restricted to Z(ℛ★)" gives c_J(b) = c_fam = 0 for every card whose ℛ★ is short: a second disguised kill.
- **Replacement wording.**
  - §2.5 (b): "(b) for every standard model class M that is a B-HB family, a composition of B-HB families within the frozen ranges, or a model class of an SFP framework published before the card's freeze, stated without reference to the card, to ℛ★ or to any lock observable, and that realizes Im ∩ FB (non-standard realizations are scored by their own kill conditions and never disable this clause), with its constants fitted, with the card's realized Π, carrier class, [h] and T_Π given to it on every instance at zero price (as in FB(u); generation is a gate, never a credit, §4.0), and with Price(M) ≤ Price(𝒦) at p = 10: the codimension of Z(ℛ★) ∩ Obs(M) in Obs(M). Here Price(M) := the IP-4 framework choice + L_stmt(M) + the IP-5 price of M's fitted constants, a constant shared across instances being priced once. If no class qualifies, (b) does not bind."
  - Family cap: "**Family cap:** c_fam := the minimum, over every class M admissible in (b) that realizes Im ∩ FB on all of I_𝒦, of the codimension of Z(ℛ★) ∩ Obs_fam(M) in Obs_fam(M), … (κ_fam likewise). A freedom that M carries in one shared constant is credited once, not once per instance. If no class qualifies, the family cap does not bind."
  - ST-7 recorded: "S6: c_J = 0 by §2.5(b) with M the class itself, so ΔL ≤ 0 → LOOKUP".
  - App. A, "Tuning never pays" bullet, append: "A law constant that ℛ★ pins identically on every instance is credited once (family cap, CT-78)."
  - D-13, append: "Kept from v1's NULL-M: comparator classes are published or B-HB and stated without reference to the card (§2.5(b))."
  - FREEZE_VERIFICATION §3: A2 F-4, A1-10 and C-M5 → "Applied in round 2 (§7)".

**F-2. BLOCKER. §24.2 ST-8 and ST-9 name terminal S5, but T-1 gives S3. This contradicts ST-1, which is the same object class.**
- **Location:** L2447 "ST-8 | An order-2 Volterra predictor … on HB-2 at small amplitude | Terminal S5: CARD-STANDARD (STD-14)"; L2448 "ST-9 | The Beenakker–Kindermann–Nazarov cascade correction on a standard P-2 model | Terminal S5: CARD-STANDARD (STD-7)".
- **Problem.**
  - The convention says "The terminal follows T-1 (first failing screen …)". Both objects are standard models whose partition and readout are supplied (NR-1 flags typed sorts and readout maps), and HB-2's bath and Gibbs state are supplied too. §5.6 gives "SUPPLIED, even when declared → CARD-NONGENERATIVE" at S3, before S5. The convention completes missing fields; it cannot make a supplied partition generated.
  - ST-1 (Duffing/BRI1 bath, the HB-2 class) is correctly given terminal S3.
  - Round-1 audit C recorded both as "Terminal S3 NONGENERATIVE … HOLDS as a finding". The revision turned that finding into a wrong terminal.
  - §19.3 requires the kit to compute ST-6 to ST-9, so the computed terminals will contradict the frozen ones, and CV-7 voids any interpretation that changes a self-test verdict.
  - "At small amplitude" conflicts with the frozen template amplitude α = 1 SD (App. A L2471; Ch-2).
- **Replacement wording.**
  - ST-8 object: "An order-2 Volterra predictor of a₊₊ from {a₀, a₊, a₋} on an HB-2 member of small coupling (RH-AN's surrogate holding at m = 2 at the frozen template amplitude)".
  - ST-8 verdict: "Terminal S3: CARD-NONGENERATIVE (HB-2's partition, readout and bath supplied, §5.6). Recorded: S5 CARD-STANDARD (Q3: STD-14)".
  - ST-9 verdict: "Terminal S3: CARD-NONGENERATIVE (the P-2 model's partition and detector readout supplied, §5.6). Recorded: S5 CARD-STANDARD (Q3: STD-7; SFP-5 lists Beenakker–Kindermann–Nazarov)".

### MAJOR

**F-3. MAJOR. NR-17 (joint necessity) runs at S3 and can pre-empt the S5 terminals stated for ST-6 and ST-11. CT-75's stated outcome conflicts with it, and "Price(ℛ★ stated directly)" is undefined.**
- **Location:**
  - NR-17 L1148–1159: "Any Ξ-level predicate R ⊇ Sol may be offered as 𝒦₂ … If Price_min(𝒦₂) ≤ Price(ℛ★ stated directly) + c_dec, and … (b) … then ℛ★ is imposed, not forced: RELOCATED".
  - ST-6 L2445: "Terminal S5: CARD-STANDARD".
  - ST-11 L2450: "terminal S5 CARD-DEFINITIONAL".
  - CT-75 L2416: "STANDARD-IMPLIED".
- **Problem.**
  - ST-6: 𝒦₂ := "the generator satisfies detailed balance" is an R ⊇ Sol, and the FDT/Onsager relation holds on all of Dom_gate ∩ Sol(𝒦₂). JN therefore fires at S3 (§5.6 → CARD-RELOCATED) whenever that predicate's L₀ statement is within 60 bits of Price(ℛ★ stated directly). Neither quantity is fixed.
  - ST-11's Ξ-level branch is the same: with 𝒦₂ := the clauses forcing the Γ-restriction, ℛ★ = D ∧ G holds throughout.
  - ST-6 also does not exclude an NR-6 RB/SPS template that recovers Π from 𝒞 on the generic lock fiber.
  - Both terminals are therefore underdetermined, and the CT-75 presumption contradicts NR-17.
- **Replacement wording.**
  - NR-17, append: "A 𝒦₂ that is, or is L₀-equivalent within c_dec bits to, a PS-5 structure generated by 𝒦 is assessed under NR-12(b) (STANDARD-IMPLIED; CT-75); JN is recorded for it, not applied. Price(ℛ★ stated directly) is the L_stmt of ℛ★ with ε, d_op, the chart coordinates and the card's components as defined symbols, at ⌈log₂(#definitions + 1)⌉ bits per use (§4.1)."
  - ST-6 construction, append: "; no RB/SPS template or decoder within ℓ_dec applied to the inventory recovers Π (NR-6)".
  - ST-11: "Γ-restriction forced by Ξ-level clauses: terminal S3 CARD-RELOCATED (NR-17(b)) if the shortest L₀ statement of those clauses is ≤ Price(ℛ★ stated directly) + c_dec; otherwise terminal S5 CARD-DEFINITIONAL (Q2 via DEF-15). In both cases Q2 (DEF-15) and Q5 are recorded as failing. Imposed by a target-level clause: terminal S3 CARD-RELOCATED (NR-2)."

**F-4. MAJOR. IP-7 prices with ΔF_tgt, which the revision left undefined. Its old meaning reinstates the IP-6 kill for asymmetric types.**
- **Location:** IP-7 L891–893: "a declared PS-5 structure costs P_X := max(L_stmt(X), ΔF_tgt(X)), computed against 𝒟(ι)". NR-5 L1052–1053: "its asymmetry is priced under IP-7 as a supplied commitment".
- **Problem.**
  - ΔF_tgt was defined only in the old IP-6 (v1 L556: "Credited(𝒦) − Credited(𝒦[v ↦ v̄]) … with v's axioms deleted"). Both that definition and "Credited" are gone.
  - Under CV-1 an auditor may restore the deletion reading. That prices the NR-5 asymmetry of every card whose 𝒞 type cannot be symmetric, and every declared PS-5 commitment, at the whole of b_J. This is the C-B2/F-6 kill that the IP-6 rewrite removed.
- **Replacement wording:** "**IP-7 Supplied commitments:** a declared PS-5 structure, or the asymmetry priced under NR-5, costs P_X := max(L_stmt(X), ΔF_tgt(X)), where ΔF_tgt(X) := b_J − b_J with X replaced by an independent draw of its type from the charter reference measure (the larger loss over two post-freeze seeds), computed against 𝒟(ι). Deleting X is not a test. **Pricing never substitutes for generation** (§5.1)."

**F-5. MAJOR. The IP-6 closure-by-definability reaches the base language and classical probability. Read literally, every card "matches" VB-6, so every selectivity result is RELOCATED.**
- **Location:** IP-6 L883–889: "a defined symbol whose interpretation satisfies an item's frozen axiom checklist …, or any structure from which such an item is L₀-definable within c_dec bits, *is* that item; an undeclared match → RELOCATED … Supplying or matching VB-5, VB-6 or VB-7 makes every selectivity result RELOCATED".
- **Problem.**
  - The simplex of record laws, with total mass as the order unit, is a GPT state cone with order unit (VB-6), and it is L₀-definable from the base `law` token in well under c_dec = 60 bits.
  - Base ℚ arithmetic likewise defines a metric (VB-1) and an inner product (VB-2).
  - Under CV-1, every card matches VB-6, so G-SEL (S8) fails for every card. This is a disguised kill, introduced with the definability clause (A1 minor 26). Nothing in the charter tells the kit's VB-6 checklist to exclude classical structure.
- **Replacement wording**, appended to the IP-6 closure: "Base L₀ tokens (Appendix B.1) and charter objects used unchanged (record laws as probability measures, the charter reference measure, the chart) match no item. For VB-5, VB-6 and VB-7 a match requires non-classical structure (a non-simplicial state cone, a Hilbert-space representation, or the Born rule); the kit's axiom checklists encode this."

**F-6. MAJOR. Freeze precondition: the round-2 record is a placeholder, so FZ-2 is not yet true. Several §3 dispositions are mislabelled "Applied".**
- **Location:**
  - FREEZE_VERIFICATION §6: "See §7, appended after the round-2 audits." (no §7 exists).
  - FZ-2 L2149–2154: "Before the freeze, independent audits checked this text …".
  - FREEZE_VERIFICATION §3 rows A2 F-4, A1-10, C-M5, A1-3 and C-B5 marked "Applied".
- **Problem.** Round 1 audited the pre-freeze draft, not this text. B-B1 (round-1 BLOCKER) required the record to exist before the freeze commit. The labels misstate F-1, F-2 and the A1-3 modification.
- **Replacement wording.**
  - Before the freeze commit, write FREEZE_VERIFICATION §7, listing every round-2 finding with its disposition and where it was applied.
  - FZ-2, first sentence: "Before the freeze, two rounds of independent read-only audits checked this text (round 2) and its predecessor (round 1): …".
  - §3 rows:
    - A1-3 → "Applied, modified: v1's comparison with the IP-14 ontology price is dropped (it would exceed the 16-bit maximum at n ≤ 16; the ontology is priced in Price)";
    - C-M5 → "Applied in round 2 (§7)";
    - A2 F-4 → "Applied in round 2 (§7)";
    - C-B5 → "Applied; ST-6, ST-8, ST-9 and ST-11 corrected in round 2 (§7)".

### MINOR

- **F-7. App. A L2491 "Lock thresholds"** contradicts MC-9 L796–797. Replace with: "falsified beyond z_obs·σ_eff; confirmed within (z_obs − 1)·σ_eff with σ_eff ≤ abs(J_K)/4; z_obs := Φ⁻¹(1 − α_obs/2), α_obs = α/(3·n_obs) (MC-9; z_obs ≈ 3.32, 3.51, 3.62 for n_obs = 1, 2, 3)".
- **F-8. Horizon leftovers.**
  - C7 L2082 "Π (δ_Π, η, δ_∂, H, …" → "H_hor".
  - App. A L2471 "t₁ := H/4": H_hor is only bounded below, so t₁ is undefined. Replace with "t₁ := H_hor/4, with H_hor the horizon the card declares in C7 (≥ the §1.3 bound)".
- **F-9. Feasibility note and ST-10 wording.**
  - L2511 "itemized as in the pre-freeze audit (FREEZE_VERIFICATION.md)" → "(AUDIT_R1_C_selftests_feasibility.md §2.2)".
  - L2530: "A compact card passes if its whole price stays below about 990 bits at p = 10 and below 1000 bits at p = 16, where each real literal costs 6 more bits; for a card with n real literals the bar is about 1000 − 6n bits (about 940 for ten)."
  - L2536–2537 and ST-10: "A tabulated card fails before SC2: on post-freeze draws its table either leaves Sol empty or equal to 𝒳 (KU-1, S4 CARD-EMPTY) or does not force ℛ★ (Q1, CARD-UNFORCED)."
  - FREEZE_VERIFICATION §5 item 1: apply the same p = 16 caveat.
- **F-10. "tier" for catalogue classes** (L104, L384, L663, L666, L716, L1569, L2189, L2404). Read narrowly, the chart's "T-tier verdicts" would cover only R1's two tiers. Add to §1.4: "Elsewhere in this charter, 'tier' means any class of 𝒯 or T_Π, and a 'T-tier verdict' is the R1 verdict-table outcome at that class; only T_R1 and T_mono are R1 tiers."
- **F-11. ST-3 recorded clause** L2442 "S8 NON-SELECTIVE (SEL-10 and SEL-4 admitted)": SEL-4 is "automatic" for record-law supports and cannot be admitted by a completed card whose record laws obey STD-1. Replace with "S8 NON-SELECTIVE (SEL-10 admitted)".
- **F-12. Self-test row precision.**
  - ST-1: "STD-9 (if ℛ★ includes the 1/N_B rate)".
  - ST-4: "Ξ is any SFP model of the declared type without PS-5 content used by ℛ★".
  - ST-7: "S5 CARD-STANDARD (Q3(e); Q3(c) where the class is a B-HB family)".
- **F-13. D-13 L2599** "Restored or kept: … the size test's 'selection beyond hand choice' (b_Π 8 → 6 with n_min 6 → 8)" misdescribes v1, whose test was "beyond the IP-14 price of the ontology choice" (v1 L135). Replace with: "Changed: the size test is log₂|𝒜_Π^hand/G_ι| − log₂ M ≥ b_Π (b_Π 8 → 6, n_min 6 → 8); v1's comparison with the IP-14 ontology price is dropped because it exceeds the 16-bit maximum at n ≤ 16."
- **F-14. PV-5 L1509** "Theorems A and C | … | DERIVED; checked" → "DERIVED (R1_SYNTHESIS §6); Theorem C checked (G2-01; `82d311e`)".
- **F-15. §15.3 L1852–1855** says the exogenous-zero checks "run at S4", but no S4 terminal is named. Add: "A failure is recorded at S4 and takes effect at S5 (Q8); it is not an S4 terminal."
- **F-16. NR-4 L1037–1041.** Two thresholds apply to ℛ★ (p_dec and 1/Q_min). Add: "For X = ℛ★, the threshold p_dec is replaced by 1/Q_min."
- **F-17. §1.5 L366** "the Selector draws further seeds, up to 10·N_cred attempts". It is not stated whether these redraws count as AI-3 draws for Q1, IP-13 and DIF-7. Add: "Further draws are AI-3 draws for Q1, NR-4, NR-6, IP-13 and DIF-7."
- **F-18. Small loose ends.**
  - C7 L2082: "NR-10(h)–(l)" → "NR-10(h)–(n)".
  - §15.9 L1972: "never enter ΔL" → "never enter ΔL or ΔL₀".
  - App. A L2479: "(the N of IP-13)" → "(N_AI3 in IP-13)".
  - The B-HB regime codes (G-cl, X, N, G-q, "X / 0", "N / G") are undefined: add a key.
  - App. A "In-silico budget" is referenced nowhere: cite it in MC-8 or delete it.

---

## Part 7. Five-line summary

1. **Dispositions.** About 50 of 56 BLOCKER/MAJOR rows are in the text as recorded. Three are not effectively applied: A2 F-4 (family cap), A1-10/C-M5 (Price(M)) and C-B5 (ST-8/ST-9 rows). A1-3 was applied in modified form but is labelled "Applied".
2. **Consistency.** The G removal is clean: no G, g(ι), Credited, "N_cred ·", 48 instances, batch or Appendix C/F leftovers, and all IDs resolve. Remaining defects: ΔF_tgt is orphaned in IP-7, "H" survives in C7 and App. A t₁, the App. A lock thresholds disagree with MC-9, and "tier" is used loosely.
3. **Self-tests.** ST-1, 2, 4, 5 and 6′ hold, as do the terminals of ST-3 and ST-7. ST-8 and ST-9 fail (S3, not S5; ST-1 is the same object class). ST-6, ST-10 and ST-11's Ξ-level branch are underdetermined, because NR-17 (S3) can pre-empt S5 and "tuning" depends on F-1. Recorded sub-clauses of ST-3 (SEL-4) and ST-7 (c_J(b)) fail.
4. **Feasibility.** The arithmetic checks (720–1220 against 1000/2000; IP-13 ≤ 72; IP-6 16 bits). "About 990" should be about 940–990 because p = 16 binds. "Tuning never pays" is unsupported while the family cap cannot bind. Three disguised kills exist under hostile readings: F-1 (empty or auditor-built comparator), F-4 (ΔF_tgt) and F-5 (VB-6 closure).
5. **Freezability.** No open owner decision blocks the freeze, and no false claim about R1 or the repository was found beyond minor labels (PV-5 Theorem A, D-13). Do not freeze until F-1 and F-2 are fixed, F-3 to F-5 are applied, and FREEZE_VERIFICATION §7 records round 2. Candidate check: PASS.
