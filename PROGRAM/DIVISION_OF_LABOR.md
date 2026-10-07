# DIVISION OF LABOR (read at every session start, after NORTH_STAR.md)

**Added 2026-10-06 at the owner's direction.** Where this file and the Stage-2 task
list in `STATE.md` differ, this file governs.

> **STATUS 2026-10-07 (owner): VS Code is PAUSED. Its role is kept but inactive.**
> - Claude Code builds: it executes the open work orders itself, as well as the
>   definitions, proofs and audits.
> - The gate for the scoreboard is now external checking via `PROGRAM/CHECKS.md`
>   (RULES rule 8), not Claude Code's own review.
> - Everything below applies again if VS Code is reactivated.

## Who does what

| | **VS Code** (long autonomous runs) | **Claude Code** (reasoning and review) |
|---|---|---|
| Owns | computation: simulations, enumerations, numerics, reproductions, data-generating controls, estimator studies | definitions, proofs, theorem statements, comparator audits, literature verdicts, adversarial review |
| Takes work from | `PROGRAM/WORK_ORDERS/` (status `OPEN`) | `PROGRAM/RESULTS/` (status `DONE — PENDING REVIEW`), and the owner |
| Writes to | `PROGRAM/RESULTS/<WO-id>/` (machine-readable output + a generated report) | `PROGRAM/WORK_ORDERS/`, reviews, the scoreboard after review |

## The DRAFT rule

Any proof, theorem statement, or comparator verdict written by VS Code is marked
**`DRAFT — pending Claude Code review`**. It is **not entered on `SCOREBOARD.md`**
until Claude Code has reviewed it. This applies retroactively to anything already
written for R1.

Computed results (numbers, tables, plots from committed code) go on the scoreboard
only after Claude Code has re-run the code and reproduced them.

## Work-order protocol

1. A work order is one file, `PROGRAM/WORK_ORDERS/WO-NNN_<name>.md`. It contains the
   task, the exact definitions to use, the controls, the output format, and a status
   line.
2. VS Code takes `OPEN` orders, sets them `IN PROGRESS`, writes results to
   `PROGRAM/RESULTS/WO-NNN/`, and sets the order to `DONE — PENDING REVIEW`.
3. Claude Code reviews: it re-runs the code, checks the numbers, and checks claims.
   It then sets `REVIEWED — ACCEPTED`, `REVIEWED — REVISE (reasons)`, or
   `REVIEWED — KILLED (→ GRAVEYARD)`.
4. If VS Code needs a definition or a proof that doesn't exist yet, it stops that
   item and notes it under "Blockers" in `STATE.md`. It does not write the proof
   itself as if it were final. Other items continue.
5. Push at the end of every session. Claude Code reviews what reaches the remote
   every 2 hours. Unpushed work cannot be reviewed.

## Stage 2 (R1) split

- **VS Code — `WO-001` (computational deliverables):**
  - reproduce BRI1 under the ε_R^(T) definition (signed-affine T, 1/N_B scaling);
  - exogenous colored and non-Markovian controls, which must give ε_R = 0 when
    protocol dependence factors through T;
  - nonlinear-interface controls;
  - finite-data identifiability simulations.
- **Claude Code:**
  - the definition of ε_R^(T), including T, d_op, and the process law P_a;
  - the proofs: deliverables 1–4 (zero on T-factoring exogenous processes; BRI1 as
    a special case; invariance and coarse-graining; identifiability);
  - the comparator audit: deliverable 5.
