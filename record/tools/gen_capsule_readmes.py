#!/usr/bin/env python3
"""Generate CAPSULE_README.md for each content capsule from the import plan + the extraction data.

Inputs:  import_plan.json (pins, statuses from the archive index, parentage, file lists)
         extracts.json    (per-campaign: verbatim status source, grounded summary sentences,
                           key quotes, classification + recorded basis)
The README quotes statuses verbatim and never assigns a scientific status. Reference-only
capsules (scout-0, bri1, oldgrut) are hand-written and skipped here.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.dirname(HERE)
ROOT = os.path.dirname(REC)
SKIP = {"scout-0", "bri1", "oldgrut", "archive-index"}

ROLE_NOTE = {
    "program-governance-1": "The three files of this capsule are imported under `governance/program_governance/` (the active-rules area) and are referenced from here rather than duplicated; see `governance/GOVERNANCE_README.md`.",
    "conjecture-mode-1": "Archived downstream empirical campaign — non-load-bearing for generative theory. Governance available for future empirical prediction campaigns (see `governance/`). Card #1: POSTULATED; COMPUTATIONALLY UNRESOLVED.",
}


def main():
    plan = json.load(open(os.path.join(HERE, "import_plan.json")))
    ext = json.load(open(os.path.join(HERE, "extracts.json")))
    for name, cap in plan.items():
        if name.startswith("_") or name in SKIP:
            continue
        e = ext.get(name, {})
        lines = [f"# Capsule: {name}", ""]
        lines += ["| Field | Value |", "|---|---|",
                  "| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |",
                  f"| Branch | `{cap['branch']}` |",
                  f"| Pin (authoritative) | `{cap['pin']}` |",
                  f"| Proposed tag | `{cap['proposed_tag_label']}` (label — pending, not pushed; tags do not exist on the remote) |"]
        if cap.get("terminal_is_recorded_state"):
            lines.append(f"| Recorded state (verbatim; **not a terminal**) | {cap['terminal_verbatim']} |")
        else:
            lines.append(f"| Terminal status (verbatim) | **\"{cap['terminal_verbatim'].strip(chr(34))}\"** |")
        if cap.get("parent_capsule"):
            lines.append(f"| Parent | `{cap['parent_capsule']}` (this capsule holds only the files this campaign added over it) |")
        lines.append(f"| Files imported (byte-exact) | {len(cap['files'])} — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |")
        cls = e.get("classification", [])
        if cls:
            lines.append(f"| Classification | {' **and** '.join(cls)} |")
        lines.append("")
        if e.get("classification_basis"):
            lines += [f"**Classification basis (recorded wording):** {e['classification_basis']}", ""]
        if name in ROLE_NOTE:
            lines += [f"**Role.** {ROLE_NOTE[name]}", ""]
        if e.get("summary"):
            lines += ["## What this campaign is (from its own documents)", ""]
            lines += [f"- {s}" for s in e["summary"]]
            lines.append("")
        if e.get("key_quotes"):
            lines += ["## Key recorded statements", ""]
            for q in e["key_quotes"][:6]:
                lines.append(f"- `{q['path']}`: “{q['quote']}”")
            lines.append("")
        if e.get("extra"):
            lines += [e["extra"], ""]
        lines += ["---", "",
                  "Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` "
                  "(IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).", ""]
        dst = os.path.join(ROOT, "record", "testinggrut", name, "CAPSULE_README.md")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("wrote", name)


if __name__ == "__main__":
    main()
