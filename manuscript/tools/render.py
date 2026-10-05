#!/usr/bin/env python3
"""Assemble the manuscript from src/ and generated data, then convert with pandoc.

  python3 render.py            -> build/BRI1_manuscript.md, build/S1_theorem_and_notation.md
  python3 render.py --pdf      -> also the PDFs (pandoc + xelatex) and the HTML render

Source conventions (src/*.md):
  {{key}}                 value from data/values.json (formatting declared there)
  {{include:name}}        src/_include/name.md (shared statement text)
  {{table:name}}          data/tables/name.md
  ![caption](figure:name){#fig:label}   generated figure figures/name.{pdf,png}
  $$ ... $$ {#eq:label}   numbered display equation; cite as @eq:label
  @fig:label              figure reference
  <!-- M:item.id -->      trace marker: the next statement is traced in the manifest
Nothing else may carry a scientific number (enforced by check.py).
"""
import json
import os
import re
import shutil
import subprocess
import sys

from common import BUILD, DATA, FIG, MS, SRC, dump_json, load_json

HEADER = "Working draft — not for submission. AI-assisted; disclosure statements pending."
TITLE = ("Finite-bath escape of reciprocal anharmonic back-reaction from shared "
         "signed-affine exogenous forcing")

MAIN = ["00_front.md", "01_introduction.md", "02_model.md", "03_classes.md", "04_main_result.md",
        "05_reservoir_limit.md", "06_numerical_illustration.md", "07_discussion.md", "08_back_matter.md"]
SUPP = ["S0_supplement_front.md", "S1_theorem_and_notation.md", "S2_t7_check.md",
        "S3_class_hierarchy_and_mechanism_map.md", "S4_reservoir_limit_proof.md",
        "S5_numerical_methods_and_convergence.md", "S6_second_code_path_and_reproducibility.md"]

PH = re.compile(r"\{\{\s*([A-Za-z0-9_.:\-]+)\s*\}\}")
MARK = re.compile(r"<!--\s*M:([A-Za-z0-9_.\-]+)\s*-->\n?")
EQ = re.compile(r"\$\$\n(.*?)\n\$\$\s*\{#(eq:[A-Za-z0-9_\-]+)\}", re.S)
FIGRE = re.compile(r"!\[(.*?)\]\(figure:([A-Za-z0-9_\-]+)\)\{#(fig:[A-Za-z0-9_\-]+)\}", re.S)


class Ctx:
    def __init__(self):
        self.values = load_json(os.path.join(DATA, "values.json"))
        self.used = {}          # key -> [files]
        self.unresolved = []    # (file, token)
        self.markers = []       # (item id, file, line)
        self.includes_used = []


def expand(text, fname, ctx, depth=0):
    def inc(mo):
        name = mo.group(1)
        ctx.includes_used.append((name, fname))
        with open(os.path.join(SRC, "_include", name + ".md"), encoding="utf-8") as f:
            raw = strip_markers(f.read().rstrip("\n"), f"_include/{name}.md", ctx)
            return expand(raw, f"_include/{name}.md", ctx, depth + 1)

    text = re.sub(r"\{\{\s*include:([A-Za-z0-9_\-]+)\s*\}\}", inc, text)

    def tab(mo):
        p = os.path.join(DATA, "tables", mo.group(1) + ".md")
        if not os.path.exists(p):
            ctx.unresolved.append((fname, mo.group(0)))
            return mo.group(0)
        with open(p, encoding="utf-8") as f:
            return f.read().rstrip("\n")

    text = re.sub(r"\{\{\s*table:([A-Za-z0-9_\-]+)\s*\}\}", tab, text)

    def val(mo):
        key = mo.group(1)
        if key not in ctx.values:
            ctx.unresolved.append((fname, mo.group(0)))
            return mo.group(0)
        ctx.used.setdefault(key, []).append(fname)
        return ctx.values[key]["text"]

    text = PH.sub(val, text)
    return text


def strip_markers(text, fname, ctx):
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        mo = MARK.fullmatch(line.strip() + "\n") if line.strip().startswith("<!-- M:") else None
        if mo:
            ctx.markers.append((mo.group(1), fname, i))
            continue
        out.append(line)
    return "\n".join(out)


def number(text, supp_prefix=None):
    """Tag display equations and figures; resolve @eq/@fig references."""
    eqs, figs = {}, {}
    counter = {"main": 0}

    def eq(mo):
        label = mo.group(2)
        sec = re.match(r"eq:(S\d)-", label)
        if sec:
            counter[sec.group(1)] = counter.get(sec.group(1), 0) + 1
            tag = f"{sec.group(1)}.{counter[sec.group(1)]}"
        else:
            counter["main"] += 1
            tag = str(counter["main"])
        eqs[label] = tag
        return f"$$\n{mo.group(1)}\n\\tag{{{tag}}}\n$$"

    text = EQ.sub(eq, text)

    def fig(mo):
        figs[mo.group(3)] = str(len(figs) + 1)
        return mo.group(0)

    FIGRE.sub(fig, text)
    text = re.sub(r"@(eq:[A-Za-z0-9_\-]+)", lambda m: f"({eqs.get(m.group(1), '??' + m.group(1))})", text)
    text = re.sub(r"@(fig:[A-Za-z0-9_\-]+)", lambda m: f"Fig. {figs.get(m.group(1), '??' + m.group(1))}", text)
    return text, eqs, figs


def figures(text, ext):
    rel = os.path.relpath(FIG, BUILD)
    return FIGRE.sub(lambda m: f"![{m.group(1)}]({rel}/{m.group(2)}.{ext}){{#{m.group(3)}}}", text)


def front_matter(title):
    hdr = HEADER.replace("—", "---")
    return "\n".join([
        "---",
        f"title: \"{title}\"",
        "author: \"[AUTHOR — to be completed by the author]\"",
        "date: \"Working draft\"",
        "geometry: margin=1in",
        "fontsize: 11pt",
        "colorlinks: true",
        "header-includes:",
        "  - \\usepackage{fancyhdr}",
        "  - \\usepackage{amsmath}",
        "  - \\pagestyle{fancy}",
        "  - \\fancyhf{}",
        f"  - \\fancyhead[C]{{\\footnotesize {hdr}}}",
        "  - \\fancyfoot[C]{\\thepage}",
        "  - \\renewcommand{\\headrulewidth}{0.4pt}",
        f"  - \\fancypagestyle{{plain}}{{\\fancyhf{{}}\\fancyhead[C]{{\\footnotesize {hdr}}}\\fancyfoot[C]{{\\thepage}}}}",
        "---",
        "",
        f"**{HEADER}**",
        "",
        "",
    ])


def assemble(files, title, ctx):
    parts = []
    for fn in files:
        with open(os.path.join(SRC, fn), encoding="utf-8") as f:
            raw = f.read()
        raw = strip_markers(raw, fn, ctx)
        parts.append(expand(raw, fn, ctx))
    body = "\n\n".join(p.strip("\n") for p in parts) + "\n"
    body, eqs, figs = number(body)
    return front_matter(title) + body, eqs, figs


def pandoc(md, out, fmt):
    args = ["pandoc", md, "-o", out, "--resource-path", BUILD, "--columns=300"]
    if fmt == "pdf":
        args += ["--pdf-engine=xelatex"]
    else:
        args += ["-s", "--mathjax", "--metadata", "pagetitle=working draft"]
    r = subprocess.run(args, capture_output=True, text=True)
    return r.returncode, (r.stderr or "")[-3000:]


def main():
    os.makedirs(BUILD, exist_ok=True)
    ctx = Ctx()
    full, eqs, figs = assemble(MAIN + SUPP, TITLE, ctx)
    s1, _, _ = assemble(["S1_theorem_and_notation.md"], "Theorem and notation sheet (Supplement S1)", Ctx())
    outputs = {}
    for name, txt in (("BRI1_manuscript", full), ("S1_theorem_and_notation", s1)):
        md = os.path.join(BUILD, name + ".md")
        with open(md, "w", encoding="utf-8") as f:
            f.write(figures(txt, "pdf"))
        outputs[name] = {"md": os.path.relpath(md, MS)}
        if "--pdf" in sys.argv:
            rc, err = pandoc(md, os.path.join(BUILD, name + ".pdf"), "pdf")
            outputs[name]["pdf_rc"] = rc
            if rc:
                outputs[name]["pdf_error"] = err
            hmd = os.path.join(BUILD, name + ".html.md")
            with open(hmd, "w", encoding="utf-8") as f:
                f.write(figures(txt, "png"))
            rc, err = pandoc(hmd, os.path.join(BUILD, name + ".html"), "html")
            os.remove(hmd)
            outputs[name]["html_rc"] = rc
            if rc:
                outputs[name]["html_error"] = err
    dump_json({"used_values": ctx.used, "unresolved": ctx.unresolved, "markers": ctx.markers,
               "includes": ctx.includes_used, "equations": eqs, "figures": figs, "outputs": outputs,
               "section_order": MAIN + SUPP, "header": HEADER}, os.path.join(BUILD, "render_log.json"))
    print(json.dumps(outputs, indent=1))
    if ctx.unresolved:
        print("UNRESOLVED:", ctx.unresolved)
        sys.exit(1)


if __name__ == "__main__":
    main()
