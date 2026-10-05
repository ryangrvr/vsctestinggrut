#!/usr/bin/env python3
"""Build checks; writes BUILD_MANIFEST.json and build/BUILD_REPORT.{json,md}. Exit 1 on any failure.

Checks (all blocking unless marked informational):
  C1  record import: every imported record file is byte-exact (git blob ids)
  C2  placeholders: none unresolved in the rendered Markdown; every {{key}} in src exists
  C3  numeric literals: src/*.md carry no scientific number outside the allowlist
  C4  provenance: every value in data/values.json has a provenance entry; every used value too
  C5  numeric-zone rule: numeric Gibbs moments appear only in Section 6 and Supplement S5
  C6  vocabulary firewall on the rendered manuscript and on src/
  C7  trace: every marker has a trace item and vice versa; every quoted source passage
      occurs verbatim in the cited record file
  C8  disclosure placeholders present at the two reserved locations; page header present
  C9  generated artefacts present (figures, tables, data files)
  info: [CITATION NEEDED] placeholders listed; PDF page count
"""
import json
import os
import re
import subprocess
import sys
import unicodedata

from common import (AUTH_JSON_REL, BUILD, DATA, FIG, MS, ROOT, RECORD_DIR, SOURCE_BRANCH, SOURCE_COMMIT,
                    SOURCE_REPO, SRC, dump_json, load_json)
import record_import
import render

BANNED = ["GRUT", "ontology", "quotient", "X1", "P0", "P1", "V1", "V2", "V3", "owner", "ruling", "charter",
          "tier", "gate"]
BANNED_EXTRA = ["BRI", "BRI0", "BRI1", "PF4Q", "SCOUT", "Candidate"]      # internal labels, added by this build
VOCAB_EXCEPTIONS = {}                                                     # term -> reason (none needed)

NUMERIC_ALLOW = [
    (r"t_\\star\s*=\s*0\.5", "t_star = 0.5 (prompt allowlist)"),
    (r"\\beta\s*=\s*1\b", "beta = 1 (prompt allowlist)"),
    (r"s\(u\)\s*=\s*10u\^3\s*-\s*15u\^4\s*\+\s*6u\^5", "protocol definition (prompt allowlist)"),
]
NB_VALUES = {"4", "8", "16", "32", "64", "128"}                           # integer N_B values (prompt allowlist)
DISCLOSURES = {
    "[AI-USE DISCLOSURE — research: proof development, code, numerical verification]": "S6_methods_and_provenance.md",
    "[AI-USE DISCLOSURE — manuscript preparation]": "08_back_matter.md",
}


def norm(s):
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\s+", " ", s).strip()


def src_files():
    out = []
    for dp, _, fns in os.walk(SRC):
        for fn in sorted(fns):
            if fn.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dp, fn), SRC))
    return sorted(out)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def numeric_scan(rel, text):
    hits = []
    text = re.sub(r"<!--\s*refs:begin\s*-->.*?<!--\s*refs:end\s*-->", "", text, flags=re.S)  # bibliography
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\[CITATION NEEDED:[^\]]*\]", "", text)
    text = render.PH.sub("", text)
    for i, line in enumerate(text.split("\n"), 1):
        l = line
        for pat, _ in NUMERIC_ALLOW:
            l = re.sub(pat, " ", l)
        l = re.sub(r"\{#[^}]*\}", " ", l)                       # anchors
        l = re.sub(r"^#+\s*S?\d+(\.\d+)*\.?", " ", l)          # heading numbers
        l = re.sub(r"\b(Supplements?|Section|Table|Lemma|Theorem|Proposition|Definition|Fig\.)\s+S?\d+(\.\d+)*", " ", l)
        l = re.sub(r"\bS\d+(\.\d+)*\b", " ", l)                # supplement labels
        l = re.sub(r"[\^_]\{?\s*[-+]?\s*\d+\s*\}?", " ", l)    # exponents, subscripts, indices
        for mo in re.finditer(r"(?<![A-Za-z\\])(\d+\.\d+|\d+)(?![A-Za-z]*\()", l):
            tok = mo.group(1)
            if "." in tok:
                hits.append((rel, i, tok, line.strip()[:120]))
            elif len(tok) >= 2 and tok not in NB_VALUES:
                hits.append((rel, i, tok, line.strip()[:120]))
    return hits


def vocab_scan(name, text):
    hits = []
    for term in BANNED + BANNED_EXTRA:
        for mo in re.finditer(r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])", text, flags=re.I):
            line = text.count("\n", 0, mo.start()) + 1
            hits.append((name, line, term, text[max(0, mo.start() - 40): mo.end() + 40].replace("\n", " ")))
    return [h for h in hits if h[2] not in VOCAB_EXCEPTIONS]


def git_head():
    try:
        return subprocess.check_output(["git", "-C", ROOT, "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return None


def main():
    fails, report = [], {}

    # C1
    bad, n = record_import.verify()
    report["C1_record_import"] = {"files": n, "problems": bad}
    fails += [f"C1 {b}" for b in bad]

    # render log
    rlog = load_json(os.path.join(BUILD, "render_log.json"))
    manuscript = read(os.path.join(BUILD, "BRI1_manuscript.md"))

    # C2
    leftover = re.findall(r"\{\{[^}]*\}\}", manuscript)
    report["C2_placeholders"] = {"unresolved_in_render": rlog["unresolved"], "leftover_in_output": leftover}
    if rlog["unresolved"] or leftover:
        fails.append(f"C2 unresolved placeholders: {rlog['unresolved'] or leftover}")
    for unresolved in re.findall(r"\?\?(eq|fig):[A-Za-z0-9_\-]+", manuscript):
        fails.append(f"C2 unresolved cross-reference {unresolved}")

    # C3
    hits = []
    for rel in src_files():
        hits += numeric_scan(rel, read(os.path.join(SRC, rel)))
    report["C3_numeric_literals"] = {"violations": hits, "allowlist": [r for _, r in NUMERIC_ALLOW] +
                                     ["integer N_B values " + ", ".join(sorted(NB_VALUES, key=int)),
                                      "single-digit structural integers (exponents, orders, combinatorial factors)",
                                      "section, table, figure, lemma and equation numbers",
                                      "bibliographic entries inside the references block"]}
    fails += [f"C3 numeric literal {t!r} in {f}:{i}: {ctx}" for f, i, t, ctx in hits]

    # C4
    values = load_json(os.path.join(DATA, "values.json"))
    noprov = [k for k, v in values.items() if not v.get("provenance")]
    report["C4_provenance"] = {"values": len(values), "without_provenance": noprov,
                               "used": sorted(rlog["used_values"])}
    fails += [f"C4 value without provenance: {k}" for k in noprov]

    # C5
    zone_bad = []
    for k, files in rlog["used_values"].items():
        allowed = values[k].get("allowed_in")
        if allowed:
            for f in files:
                if os.path.basename(f) not in allowed:
                    zone_bad.append((k, f))
    report["C5_numeric_zone"] = {"violations": zone_bad}
    fails += [f"C5 numeric Gibbs value {k} used outside Section 6/S5 in {f}" for k, f in zone_bad]

    # C6
    vhits = vocab_scan("build/BRI1_manuscript.md", manuscript)
    for rel in src_files():
        vhits += vocab_scan("src/" + rel, read(os.path.join(SRC, rel)))
    report["C6_vocabulary"] = {"banned": BANNED, "added_by_build": BANNED_EXTRA, "exceptions": VOCAB_EXCEPTIONS,
                               "violations": vhits}
    fails += [f"C6 banned term {t!r} at {f}:{l}: …{c}…" for f, l, t, c in vhits]

    # C7
    trace = load_json(os.path.join(MS, "tools", "trace_items.json"))
    files = trace["_files"]
    markers = {}
    for item, f, line in rlog["markers"]:
        markers.setdefault(item, []).append(f"src/{f}:{line}")
    missing_items = sorted(set(markers) - set(trace["items"]))
    unused_items = sorted(set(trace["items"]) - set(markers))
    quote_fail = []
    manifest_items = {}
    for iid, it in trace["items"].items():
        srcs = []
        for s in it["sources"]:
            path = os.path.join(ROOT, RECORD_DIR, files[s["file"]])
            ok = norm(s["quote"]) in norm(read(path))
            if not ok:
                quote_fail.append((iid, files[s["file"]], s["quote"][:80]))
            srcs.append({"repo": SOURCE_REPO, "commit": SOURCE_COMMIT, "path": f"{RECORD_DIR}/{files[s['file']]}",
                         "section": s["section"], "quote": s["quote"], "quote_verified_verbatim": ok})
        manifest_items[iid] = {"kind": it["kind"], "label": it["label"], "manuscript_locations": markers.get(iid, []),
                               "sources": srcs, "blueprint": it["blueprint"], "notes": it["notes"]}
    report["C7_trace"] = {"markers": len(markers), "items": len(trace["items"]), "missing_items": missing_items,
                          "unused_items": unused_items, "quote_failures": quote_fail}
    fails += [f"C7 marker without trace item: {m}" for m in missing_items]
    fails += [f"C7 trace item never placed in src: {m}" for m in unused_items]
    fails += [f"C7 quote not found verbatim: {q}" for q in quote_fail]

    # C8
    dis = {}
    for text, fname in DISCLOSURES.items():
        ok = text in read(os.path.join(SRC, fname)) and text in manuscript
        dis[text] = {"file": fname, "present": ok}
        if not ok:
            fails.append(f"C8 disclosure placeholder missing: {text}")
    header_ok = render.HEADER in manuscript and "\\fancyhead[C]" in manuscript and "fancypagestyle{plain}" in manuscript
    report["C8_disclosure_and_header"] = {"disclosures": dis, "header": render.HEADER, "header_on_every_page": header_ok}
    if not header_ok:
        fails.append("C8 page header missing")

    # C9
    need = [os.path.join(FIG, f"{n}.{e}") for n in ("fig1_schematic", "fig2_scaling", "fig3_flat") for e in ("pdf", "png")]
    need += [os.path.join(DATA, f) for f in ("values.json", "constants.json", "t7_check.json", "figures.json", "tables.json")]
    tables = load_json(os.path.join(DATA, "tables.json"))
    need += [os.path.join(DATA, "tables", t + ".md") for t in tables]
    missing = [os.path.relpath(p, MS) for p in need if not os.path.exists(p)]
    report["C9_artefacts"] = {"missing": missing}
    fails += [f"C9 missing artefact {m}" for m in missing]

    # informational
    cites = sorted(set(re.findall(r"\[CITATION NEEDED:[^\]]*\]", manuscript)))
    report["citation_placeholders"] = cites
    pdf = os.path.join(BUILD, "BRI1_manuscript.pdf")
    pages = None
    if os.path.exists(pdf):
        info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        mo = re.search(r"Pages:\s+(\d+)", info)
        pages = int(mo.group(1)) if mo else None
    s1pdf = os.path.join(BUILD, "S1_theorem_and_notation.pdf")
    s1pages = None
    if os.path.exists(s1pdf):
        mo = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", s1pdf], capture_output=True, text=True).stdout)
        s1pages = int(mo.group(1)) if mo else None
    report["pdf"] = {"manuscript_pages": pages, "s1_pages": s1pages, "outputs": rlog["outputs"]}
    t7 = load_json(os.path.join(DATA, "t7_check.json"))
    report["t7_check"] = [{"t": r["t"], "ratio": r["ratio"], "ratio_method_B": r["ratio_method_B"],
                           "ratio_series": r["ratio_series_t7_to_t14"]} for r in t7["rows"]]
    report["findings"] = trace.get("_findings", [])
    report["result"] = "PASS" if not fails else "FAIL"
    report["failures"] = fails

    manifest = {
        "build": {"tool": "manuscript/Makefile", "repo_head_at_check": git_head(),
                  "header": render.HEADER, "section_order": rlog["section_order"]},
        "record": {"repo": SOURCE_REPO, "branch": SOURCE_BRANCH, "commit": SOURCE_COMMIT,
                   "imported_as": RECORD_DIR, "ledger": "manuscript/RECORD_IMPORT.json",
                   "authoritative_numerics": AUTH_JSON_REL,
                   "blueprint": "Blueprint v1.1 not present in this repository or in the source repository; "
                                "binding constraints taken from the build prompt. Items marked BLUEPRINT-UNVERIFIED "
                                "await a conformance pass against the full blueprint."},
        "findings": trace.get("_findings", []),
        "items": manifest_items,
        "values": {k: {"text": v["text"], "fmt": v["fmt"], "provenance": v["provenance"],
                       "used_in": sorted(set(rlog["used_values"].get(k, [])))} for k, v in values.items()},
        "equations": rlog["equations"],
        "figures": load_json(os.path.join(DATA, "figures.json")),
        "tables": tables,
        "check": {"result": report["result"], "failures": fails},
    }
    dump_json(manifest, os.path.join(MS, "BUILD_MANIFEST.json"))
    dump_json(report, os.path.join(BUILD, "BUILD_REPORT.json"))
    write_md_report(report)
    print(f"CHECK {report['result']}: {len(fails)} failure(s)")
    for f in fails[:60]:
        print("  -", f)
    sys.exit(0 if not fails else 1)


def write_md_report(r):
    L = ["# Build report", "", f"**Result: {r['result']}**", ""]
    L += ["## Failures", ""] + ([f"- {f}" for f in r["failures"]] or ["- none"]) + [""]
    L += ["## Record import", "", f"{r['C1_record_import']['files']} files verified byte-exact.", ""]
    L += ["## Vocabulary firewall", "", "Banned: " + ", ".join(r["C6_vocabulary"]["banned"]),
          "", "Added by this build: " + ", ".join(r["C6_vocabulary"]["added_by_build"]),
          "", f"Exceptions: {r['C6_vocabulary']['exceptions'] or 'none'}",
          "", f"Violations: {len(r['C6_vocabulary']['violations'])}", ""]
    L += ["## Numeric-literal check", "", "Allowlist:"] + [f"- {a}" for a in r["C3_numeric_literals"]["allowlist"]]
    L += ["", f"Violations: {len(r['C3_numeric_literals']['violations'])}", ""]
    L += ["## Trace", "", f"{r['C7_trace']['markers']} marked statements; {r['C7_trace']['items']} trace items; "
          f"quote failures: {len(r['C7_trace']['quote_failures'])}", ""]
    L += ["## Findings (record, blueprint, notation)", ""] + [f"- **{f['id']} {f['type']}.** {f['finding']}" for f in r.get("findings", [])] + [""]
    L += ["## Citation placeholders", ""] + [f"- {c}" for c in r["citation_placeholders"]] + [""]
    L += ["## S2 small-time check (computed by this build)", "", "| t | ratio | method B | series |", "|---|---|---|---|"]
    L += [f"| {x['t']:g} | {x['ratio']:.6f} | {x['ratio_method_B']:.6f} | {x['ratio_series']:.6f} |" for x in r["t7_check"]]
    L += ["", "## PDF", "", f"Manuscript pages: {r['pdf']['manuscript_pages']}; S1 sheet pages: {r['pdf']['s1_pages']}", ""]
    with open(os.path.join(BUILD, "BUILD_REPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
