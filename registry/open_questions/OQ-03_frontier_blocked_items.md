# OQ-03 — Frontier-blocked and out-of-envelope items at the program freeze

Every status word below is quoted verbatim from the frozen record; nothing is assigned or changed here. Each item names its source capsule (`record/testinggrut/<capsule>/`) and the capsule's pinned 40-character SHA. Items appearing in files carried on several branches are cited at the branch that created them; the capsule READMEs record the lineage.

## A. Items the record itself marks FRONTIER-BLOCKED, blocked by category, or blocked by rule

| Item | Recorded status (verbatim) | Source | Pin |
|---|---|---|---|
| **Π0-0 — the Π₀ trace-channel probe** (the record's only literal "FRONTIER-BLOCKED" marker) | "Π0-0 = FRONTIER-BLOCKED (owner ruling, comment 5902971222)" (`CURRENT_STATE.json`); "Π0-0 = FRONTIER-BLOCKED, terminal at declared scope; no Π0-1 charter authorized" (`playground/SCOUT_0/BASELINE_MAP.md`, Table 4 row F-4; same wording in `GRUT_WORKING_THEORY_DEPOSIT_01.md`, `GRUT_SUCCESSOR_STATUS_01.md`); "(1) **rung3's Π₀** — external, frontier-blocked, dispatch-ready" (`GRUT_II_What_Survived.md`) | scout-0 (reference capsule; content byte-identical in `main` @ `7baf2f1`) | `ab2da47407bb670d94e2a52c87599fa13fd8ab99` |
| **The frontier object the open rungs converge on** | "**All converge on one frontier object:** the exact small-ω scaling exponent of the spectral density ρ_σ(ω) for the vacuum's stress-coupling on de Sitter — Im⟨T_TT T_TT⟩(ω→0, k→0) for a free field in Bunch–Davies, free-streaming-vs-freezing the explicit competition." (`GRUT_ToE.md`) | scout-0 (reference capsule) | `ab2da47407bb670d94e2a52c87599fa13fd8ab99` |
| **AC-08 — endogenous / state-dependent access (EA-0: P_ρ, Γ(ρ))** | "**BLOCKED AT LEVEL-0 (CATEGORY MISMATCH)**; auxiliary non-trivial branch = **RELOCATION INTO D**" — "requires a lift" (`bridge/B3_ACCESS_COMPONENT_LEDGER.md`; tally "BLOCKED \| 1 (AC-08 at Level-0)"); carried as row L3h "BLOCKED at Level-0" in `residual_synthesis/SUPPLIED_INPUT_MASTER_TABLE.md` | bridge-1 | `753b90a3e3976ed286f385ca1b455e04c92a2d26` |
| **BI-13 — quantum lift, ħ, Born rule, gravity + cosmology** | "**BLOCKED / NO MAPPING** by rule (not reopened)" (`bridge/BRIDGE_INFORMATION_LEDGER.md`); handoff: "Lift, ħ, outcome and gravity / cosmology remain outside the C5 Bridge attack." | bridge-1 | `753b90a3e3976ed286f385ca1b455e04c92a2d26` |

## B. Out-of-envelope at freeze (SCOUT-2 frontier queue)

| Item | Recorded status (verbatim) | Source | Pin |
|---|---|---|---|
| **S2-D-arrow-∞ — infinite / continuous-spectrum arrow loophole** | "**OUT-OF-ENVELOPE / FUTURE SCOPE EXTENSION** (not unfinished SCOUT-2 work)"; queue footer: "**No open finite-envelope items.** Every probe is DONE, RETIRED or OUT-OF-ENVELOPE. No \"next\" marker remains." (`ledgers/FRONTIER_QUEUE.md`); handoff §O calls it "a scope-extension appendix candidate" | scout-2 (file carried on every later slim-line branch) | `af0042fbf51a65e986f90ff6ff6263cd32fc23a6` |

## C. Open premises and consolidated open questions at freeze

| Item | Recorded status (verbatim) | Source | Pin |
|---|---|---|---|
| **L_all localization premise behind the d\* candidate** | "**L_all is unproved.** Localization is verified only for the minimum-energy Gaussian product state."; result "CONDITIONAL ON L_all — HEURISTIC"; future scope: "a proof or disproof of L_all (a localization theorem for d\*)" (`gravity_scout_1/GRAVITY_SCOUT_1_HANDOFF.md`, `…_STATUS.md`) | gravity-scout-1 | `df25f29bf217931b366c0ef676cb38b7b34ad115` |
| **Continuum α₃ check; Stoica theorem / full-commutant epoch question; further decomposition of A_res; independent review** | listed under "## 11. Open questions / future scope (consolidated, not exhaustive)" — "a proof or disproof of L_all; an independent continuum check of α₃ (G);" (`residual_synthesis/GRUT_RESIDUAL_SYNTHESIS_01.md`); A_res decomposition and the Stoica/full-commutant question originate in `review/REVIEW_STATUS.md` on scout-2-review @ `1f08ae156a346f6089ae3b3aab2be80b9ee4ef8f` | residual-synthesis-1 | `a36cff9643765a7ef6e39e2a04e03d566a455b54` |
| **Bridge-1 o-items (B1-o1, B1-o2, B3-o1, B3-o2, B2-o2, B2-o3, B4-o1) and "review"** | queue "CLOSED … **No item remains \"next\".**"; items listed under "## OUT-OF-CAMPAIGN / FUTURE SCOPE REFINEMENT", incl. "review \| independent human / second-model review of the numerics"; B3-o3 under "OWNER CONVENTION" (`bridge/BRIDGE_FRONTIER_QUEUE.md`) | bridge-1 | `753b90a3e3976ed286f385ca1b455e04c92a2d26` |
| **Independent review owed** | scout-2 terminal: "SCOUT-2 SCIENTIFICALLY SATURATED AT CURRENT PREMISE ENVELOPE — **INDEPENDENT REVIEW OWED**" (`STATUS.md`); scout-2-review Q7 still lists an independent human / second-model reviewer as owed ("Numerical reproductions are an independent code path, not an independent reviewer", `review/REVIEW_STATUS.md`) | scout-2 / scout-2-review | `af0042fbf51a65e986f90ff6ff6263cd32fc23a6` / `1f08ae156a346f6089ae3b3aab2be80b9ee4ef8f` |

## D. Access- and environment-blocked at freeze

| Item | Recorded status (verbatim) | Source | Pin |
|---|---|---|---|
| **Primary-source full-text verification of known-result imports** | "**KNOWN-RESULT IMPORT — SOURCE LOCATED, TEXT NOT RE-READ** … Direct fetches from this environment are blocked by the egress proxy (arxiv.org and link.springer.com returned EGRESS_BLOCKED on 2026-10-02)" (`qft_scout_1/QFT_SCOUT_1_CHARTER.md`); "full-text fetch is blocked in this environment. No GO verdict could rest on that grade, and none was needed." (`selector_screen_1/GRUT_SELECTOR_SCREEN_01.md`); "arXiv is blocked from this sandbox" (`ledgers/LITERATURE_LEDGER.md`, scout-2-review) | qft-scout-1 / selector-screen-1 / scout-2-review | `5b07573bf45650d332df14258554cc8428a0706c` / `a1194546c08d81c110a6ad8cc7583fddeedbebd1` / `1f08ae156a346f6089ae3b3aab2be80b9ee4ef8f` |
| **Planck + ACT DR6 lensing likelihood v1.2 (Card #1 data provenance)** | "**BLOCKED**: `CONNECT tunnel failed, response 403` … **FAILS ACCESS.** No collaboration-maintained distribution is reachable. A substitute is forbidden (O3; Charter §4B)" (`conjecture_mode/cards/CARD_01_DATA_PROVENANCE.md`) | conjecture-mode-1 | `6c58155a5e3e74a8533281defbf7e5ff0b6833dc` |
| **VER0 verification items V0-5 / V0-6** | "VER0 remains paused, with V0-5 / V0-6 outstanding and access-dependent." (`program_governance/PROGRAM_CAMPAIGN_GATE_01.md`); the VER0 branch's own recorded state: "PAUSED FOR OWNER PROGRAM-LEVEL DISCUSSION."; "Items 4 and 6 are **OUTSTANDING — PRIMARY-TEXT ACCESS DEPENDENT**. Every item is at most VER-I1." with table rows "V0-5 K1-H / K1-HS \| **outstanding — primary-text access dependent**" and "V0-6 secondary primary-text checks \| **outstanding — primary-text access dependent**" (`verification_0/VER0_STATUS.md`; owed-check items #4/#6 correspond to verification rows V0-5/V0-6) | program-governance-1 / independent-verification-0 | `5baa8afd83b8a2dbce31b8f3c4bd484417afbc11` / `bd287a88dc08ae54173a6c73368db0e250cc1c7f` |

## E. Gated reopenings and holds (closed terminals that carry an explicit reopening condition)

| Item | Recorded status (verbatim) | Source | Pin |
|---|---|---|---|
| **Selector campaign** | "**SELECTOR CAMPAIGN: NO-GO AT CURRENT SCREEN — REQUIRES A NEW NAMED CANDIDATE TO REOPEN**" (TERMINAL, `selector_screen_1/SELECTOR_SCREEN_STATUS.md`); scope note: "not an impossibility theorem" | selector-screen-1 | `a1194546c08d81c110a6ad8cc7583fddeedbebd1` |
| **DA0 C3 architecture track** | "C3 ARCHITECTURE TRACK — HOLD: OPERATIONAL DEFINITION UNRESOLVED"; "The architecture question is **not** closed permanently, but the current detector programme is stopped." | directed-autonomy-0 | `0b27b0e9c8de5aad389c3f436d1fb4459152340e` |
| **Conjecture Mode never-run extensions** | "**The supernova extensions, the ε > 0 control and the MCMC posterior were never run.**"; "Further optimizer campaigns \| **None (no v1R3).** Any further work needs a new owner ruling" (`CONJECTURE_MODE_FINAL_SYNTHESIS_01.md`) | conjecture-mode-1 | `6c58155a5e3e74a8533281defbf7e5ff0b6833dc` |
| **Retired probe S2-Σb** | "**RETIRED** (superseded by S2-ΣH ΣH-5 epoch prescriptions; reopen only in a future campaign)" (`ledgers/FRONTIER_QUEUE.md`) | scout-2 lineage (quoted at gravity-scout-1) | `df25f29bf217931b366c0ef676cb38b7b34ad115` |
| **DA0 / RA0 open items at freeze** | "The intrinsic K-growth threshold is **open**."; "CONJECTURE C2-B is **open**." (`directed_autonomy_0/DA0_STATUS.md`); RA0 terminal: "RA0 COMPLETE — CONDITIONAL DYNAMICAL PARTITION DERIVATION; CONSCIOUSNESS HYPOTHESIS SECTOR ELIGIBLE BUT UNOPENED"; "**Consciousness:** ELIGIBLE AS A NEW HYPOTHESIS SECTOR — NOT DERIVED; **not opened on RA0**." with an explicit "**Open:**" list (`reflexive_autonomy_0/RA0_STATUS.md`; entry ruling "MATHEMATICALLY ELIGIBLE AS A NEW HYPOTHESIS SECTOR — NOT DERIVED." in `RA0_FINAL_HANDOFF.md`) | directed-autonomy-0 / reflexive-autonomy-0 | `0b27b0e9c8de5aad389c3f436d1fb4459152340e` / `ab4fd860ebbc72a6a3c0c5dd1ff2cef52616b7f5` |

---

Note on the term "frontier-blocked": the record uses the literal compound for exactly one object — **Π0-0** ("Π0-0 = FRONTIER-BLOCKED", owner ruling; "rung3's Π₀ — external, frontier-blocked, dispatch-ready") — in the fat-lineage record (group A, first row). Everywhere else the recorded markers are **BLOCKED AT LEVEL-0**, **BLOCKED / NO MAPPING**, **OUT-OF-ENVELOPE / FUTURE SCOPE EXTENSION**, **FAILS ACCESS**, **paused / outstanding and access-dependent**, **HOLD**, and the gated-reopening terminals quoted above. This entry collects all of them; whether the owner intends "frontier-blocked items" to mean only Π0-0, group A, or this full set is left for owner confirmation.
