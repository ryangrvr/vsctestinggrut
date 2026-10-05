"""Semantic and architectural firewalls for the manuscript (used by check.py; unit-tested by test_firewalls.py).

C10  architecture: frozen section/supplement titles and order; the displayed ladder includes H;
     Introduction carries the contribution list (exactly three items), the established-vs-added
     table and the dictionary table; S3 contains no unproved-assumption language; S6 contains no
     verification-history narrative; AI_USE_LOG.md present and linked to both disclosure slots.
C11  semantic firewalls on rendered text:
     (a) the theorem's quantifier chain appears verbatim, in order, in the shared statement;
     (b) no numerical value is asserted for delta or N_0;
     (c) no uniform-in-t threshold is asserted;
     (d) t_star = 0.5 is never asserted to lie in (0, delta);
     (e) the reservoir limit is never asserted to be the harmonic class H;
     (f) effective-harmonic statements appear only as cited, unclaimed literature connections.
"""
import re

MAIN_TITLES = [
    ("01_introduction.md", "# 1. Introduction"),
    ("02_model.md", "# 2. Model and protocols"),
    ("03_classes.md", "# 3. Shared exogenous descriptions"),
    ("04_main_result.md", "# 4. Main result"),
    ("05_reservoir_limit.md", "# 5. Reservoir limit"),
    ("06_numerical_illustration.md", "# 6. Numerical illustration"),
    ("07_discussion.md", "# 7. Discussion"),
]
SUPP_TITLES = [
    ("S1_theorem_and_notation.md", "# S1. Theorem and notation sheet"),
    ("S2_t7_check.md", "# S2. Small-time consistency check"),
    ("S3_class_hierarchy_and_mechanism_map.md", "# S3. Class hierarchy and mechanism map"),
    ("S4_reservoir_limit_proof.md", "# S4. Reservoir-limit proof"),
    ("S5_numerical_methods_and_convergence.md", "# S5. Numerical methods and convergence"),
    ("S6_second_code_path_and_reproducibility.md", "# S6. Second numerical code path and reproducibility"),
]
LADDER = r"\mathcal{H} \subset \mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}"
QUANTIFIER_CHAIN = [
    r"There exists $\delta \in (0, 1]$",
    r"for each fixed $t \in (0, \delta)$",
    r"there is a finite integer $N_0(t)$",
    r"for every bath size $N_B \geq N_0(t)$",
    r"admit no common representation in the class $\mathcal{E}_2^{\pm}$",
    r"The numbers $\delta$ and $N_0(t)$ are existential",
    r"$N_0(t)$ is not claimed to be uniform in $t$",
]
S3_FORBIDDEN = ["assuming", "plausible", "not proved here", "all orders", "heuristic"]
S6_FORBIDDEN = ["Monte Carlo", "failed", "invalid", "defect", "broken", "wrong set", "earlier attempt"]
NEG = re.compile(r"\b(no|not|nor|never|neither|none|cannot|without)\b", re.I)
CITE = re.compile(r"\[\d\]|CITATION NEEDED")


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


def sentences(text):
    """Split prose into sentences; table rows and list items are their own units."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    out = []
    for block in re.split(r"\n\s*\n|\n(?=\s*[-|*\d])", text):
        block = ws(block)
        if not block:
            continue
        out += [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\[\*\$(])", block) if s]
    return out


def semantic(text, label):
    v = []
    for s in sentences(text):
        # (b) numerical delta / N_0
        # equalities/approximations with any number; inequalities only with a non-zero number
        # (the existential statements "delta > 0", "N_0(t) < infinity" are allowed)
        num_eq = r"\s*(=|\\approx|\\simeq|\\sim)\s*[-+]?\d"
        num_ineq = r"\s*(<|>|\\leq?|\\geq?)\s*[-+]?(?!0(?![.\d]))\d"
        if re.search(r"\\delta" + num_eq, s) or re.search(r"\\delta" + num_ineq, s) or \
           re.search(r"N_0(\(t\))?" + num_eq, s) or re.search(r"N_0(\(t\))?" + num_ineq, s):
            v.append((label, "(b) numerical value asserted for delta or N_0", s[:160]))
        # (c) uniform threshold
        if re.search(r"uniform", s, re.I) and re.search(r"N_0|threshold", s) and not NEG.search(s):
            v.append((label, "(c) uniform threshold asserted", s[:160]))
        # (d) t_star inside (0, delta)
        if re.search(r"t_\\star\s*\\in\s*\(0,\s*\\delta\)", s) or \
           (("t_\\star" in s or "0.5" in s) and "\\delta" in s and not NEG.search(s)):
            v.append((label, "(d) t_star asserted inside (0, delta)", s[:160]))
        # (e) reservoir limit asserted to be H
        if re.search(r"limit", s, re.I) and re.search(r"\\mathcal\{H\}|(?<![A-Za-z])harmonic", s, re.I) and not NEG.search(s):
            v.append((label, "(e) reservoir limit tied to the harmonic class without negation", s[:160]))
        # (f) effective-harmonic firewall
        if re.search(r"effective[- ]harmonic", s, re.I) and not (CITE.search(s) and NEG.search(s)):
            v.append((label, "(f) effective-harmonic statement not framed as cited, unclaimed connection", s[:160]))
    return v


def quantifiers(include_text, rendered_full, rendered_s1):
    v = []
    pos = -1
    t = ws(include_text)
    for q in QUANTIFIER_CHAIN:
        i = t.find(q)
        if i < 0:
            v.append(("thm_main", "(a) quantifier phrase missing", q))
        elif i < pos:
            v.append(("thm_main", "(a) quantifier phrase out of order", q))
        pos = max(pos, i)
    stmt = ws(re.sub(r"<!--.*?-->", "", include_text))
    if ws(rendered_full).count(stmt[:200]) < 2:
        v.append(("manuscript", "(a) theorem statement not present verbatim in both Section 4 and S1", stmt[:80]))
    if ws(rendered_s1).count(stmt[:200]) < 1:
        v.append(("S1 sheet", "(a) theorem statement not present verbatim", stmt[:80]))
    return v


def architecture(read_src, order, ai_log_text, disclosures):
    v = []
    expected = [f for f, _ in MAIN_TITLES] + [f for f, _ in SUPP_TITLES]
    present = [f for f in order if f in expected]
    if present != expected:
        v.append(("render order", "section/supplement files missing or out of order", str(present)))
    for f, title in MAIN_TITLES + SUPP_TITLES:
        try:
            first = read_src(f).lstrip().split("\n", 1)[0]
        except FileNotFoundError:
            v.append((f, "missing file", title))
            continue
        if not first.startswith(title):
            v.append((f, "title does not match the frozen architecture", f"{first!r} != {title!r}"))
    if LADDER not in ws(read_src("03_classes.md")):
        v.append(("03_classes.md", "displayed ladder does not include H", LADDER))
    intro = read_src("01_introduction.md")
    m = re.search(r"<!-- M:intro.contributions -->(.*?)(?=<!-- M:|\Z)", intro, re.S)
    items = re.findall(r"^\s*\d\.\s", m.group(1), re.M) if m else []
    if len(items) != 3:
        v.append(("01_introduction.md", "contribution list must have exactly three items", str(len(items))))
    if "| Established ingredients | Contribution here |" not in intro:
        v.append(("01_introduction.md", "established-ingredients table missing", ""))
    if "<!-- M:intro.dictionary -->" not in intro or "| causal modelling | this paper |" not in intro:
        v.append(("01_introduction.md", "causal/physics dictionary table missing", ""))
    s3 = read_src("S3_class_hierarchy_and_mechanism_map.md")
    for w in S3_FORBIDDEN:
        if re.search(re.escape(w), s3, re.I):
            v.append(("S3", "unproved-assumption language", w))
    s6 = read_src("S6_second_code_path_and_reproducibility.md")
    for w in S6_FORBIDDEN:
        if re.search(re.escape(w), s6, re.I):
            v.append(("S6", "verification-history narrative", w))
    if ai_log_text is None:
        v.append(("AI_USE_LOG.md", "missing", ""))
    else:
        for d in disclosures:
            if d not in ai_log_text:
                v.append(("AI_USE_LOG.md", "does not reference disclosure slot", d))
    return v
