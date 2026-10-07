# HANDOFF — Claude Code → VS Code (2026-10-07, rest of the week)

**Why:** Claude Code's weekly limit is at 99% (owner, 2026-10-07). VS Code is reactivated as builder until
the owner says otherwise; Claude Code is paused. `DIVISION_OF_LABOR.md` status block records this.

## 1. Session start (every session)
```
git fetch origin && git checkout grut2-stage3 && git pull origin grut2-stage3
```
Then read, in order: `PROGRAM/NORTH_STAR.md`, `PROGRAM/DIVISION_OF_LABOR.md`, `PROGRAM/RULES.md`,
`PROGRAM/STATE.md`, this file, and the open work order `PROGRAM/WORK_ORDERS/WO-003_STAGE3_KIT_SUPPORT.md`.
Run the VS Code task **"Kit: run tests"** (`.vscode/tasks.json`); expect `test_l0_code.py` 10 ok and `test_kit.py` 11 ok.

## 2. Where things stand (branch `grut2-stage3`, head at handoff: see `git log`)
- **Stage 1 (SD0):** complete. **Stage 2 (R1):** TERMINAL, accepted (G2-11; boundary `dbfd64b`).
- **Stage 3:** charter `PROGRAM/STAGE3/STAGE3_CHARTER.md` frozen alone (`0bc125a`), re-frozen with CR-1
  (`0b414e6`, G2-12); repairs CR-3 (`5aef9a4`, kit hostile defaults) and CR-4 (`c1275a8`, G2-13).
- **Kit** `PROGRAM/STAGE3/kit/` (`f6ba47f`, NR-4 fix `608d72f`): price coder, NR-4 harness, partial HB
  controls, SEL reproduction. Unfinished items take CR-3 hostile defaults KD-1…KD-5. **No extension.**
- **External checks** (`PROGRAM/CHECKS.md`): SEL and kit tests checked by the owner; NR-4 issue found and
  fixed. **Pending:** price coder vs Appendix B, HB controls, the NR-4 fix (`608d72f`), CR-4.
- **Open owner questions:** `charter_workings/FREEZE_VERIFICATION.md` §13 (undefined K-image at
  decoupling; NR-17(b) cross-reference). CV-1 (hostile default) governs until ruled.
- **Card 1 is NOT open** (G2-13 item 5). The owner is working out the card concept with ChatGPT.
- `r1-terminal` tag: the owner pushes it from their machine (`git tag r1-terminal dbfd64b && git push origin r1-terminal`).

## 3. What VS Code does this week
Only work order **WO-003** (computational support for the pending external checks). Nothing else unless the
owner issues a ruling or a new work order.

## 4. Hard rules (unchanged; RULES.md and OWNER_RULINGS.md govern)
1. **Never generate, propose, sketch, freeze, score or optimize a 𝒦 candidate.** Card authors are the owner
   (with ChatGPT). Fixtures are abstract and carry no physics.
2. **The charter is frozen.** Change it only by a charter repair (CR) that the owner has ruled. Do not apply
   CR-2 queue items (Q-1…Q-7); if a card's verdict comes to depend on one, STOP and flag it for the owner.
3. **The kit is closed** (G2-12 item 3: no extension). Do not build KD-1…KD-5 items outside a card's audit.
4. **DRAFT rule:** any proof, theorem statement, verdict or comparator judgment you write is marked
   `DRAFT — pending Claude Code review` and is never entered on `SCOREBOARD.md` or `GRAVEYARD.md`.
5. **Nothing is banked until externally checked** (`CHECKS.md`, RULES 8). You may add CHECKS lines (after the
   push is verified on the remote); only the owner or a checker sets a status.
6. **Git:** never rewrite history (no rebase, amend, force-push); no tag pushes; push at the end of every
   session and verify with `git fetch origin grut2-stage3 && git rev-parse HEAD origin/grut2-stage3`.
   Commit trailer: `Claude-Session: …` only if the session has one; no AI co-author trailers, no model names.
7. **TestingGRUT is frozen and read-only.**
8. **Blocked → stop that item,** note it under "Blockers" in `STATE.md`, continue other items.

## 5. If the owner opens Card 1 this week
Follow the owner's ruling and charter §§17–19 exactly. VS Code may run the **computational** Evaluator steps
(the kit, charter code built for that card inside R_card per CR-3). Every verdict, stage outcome and ruling-like
judgment is `DRAFT — pending Claude Code review`; nothing is logged as a card verdict until reviewed and
externally checked. When unsure, CV-1: resolve against the card and flag for the owner.

## 6. Handing back to Claude Code
Leave `STATE.md` current, push, and list in `STATE.md` → "Last results" what is DRAFT and awaiting review.
