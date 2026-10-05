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
S3_FORBIDDEN = [r"assuming", r"plausib", r"not proved here", r"all[- ]orders", r"every order",
                r"conjectur", r"heuristic", r"presumabl", r"it is expected"]
S6_FORBIDDEN = [r"Monte Carlo", r"fail", r"invalid", r"defect", r"broken", r"wrong set", r"earlier attempt",
                r"supersed", r"discrepan", r"corrected", r"\bbug\b", r"previous attempt"]
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


def _near_negation(s, idx, window=70):
    """A negator within `window` characters before position idx."""
    return bool(NEG.search(s[max(0, idx - window):idx]))


def semantic(text, label):
    v = []
    num_eq = r"\s*(=|\\approx|\\simeq|\\sim|\\lesssim|\\gtrsim)\s*[-+]?\d"
    num_ineq = r"\s*(<|>|\\leq?|\\geq?)\s*[-+]?(?!0(?![.\d]))(?!1\]|1\b)\d"
    delta_pat = r"(\\delta|δ)"
    n0_pat = r"N_\{?0\}?(\(t\))?"
    for s in sentences(text):
        # (b) numerical value asserted for delta or N_0 (equality/approx with any number;
        #     inequality with a number other than the existential 0 / (0,1] forms; value-on-left; worded values)
        hit_b = False
        for tgt in (delta_pat, n0_pat):
            if re.search(tgt + num_eq, s) or re.search(tgt + num_ineq, s):
                hit_b = True
            if re.search(r"\d(\.\d+)?\s*(<|>|\\leq?|\\geq?|\\lesssim|\\gtrsim)\s*\$?" + tgt, s):
                hit_b = True
        if re.search(r"(approximately|about|roughly|of order)\s+\$?\d", s) and re.search(delta_pat + "|" + n0_pat, s):
            hit_b = True
        if hit_b:
            v.append((label, "(b) numerical value asserted for delta or N_0", s[:160]))
        # (c) uniform / t-independent threshold, unless the negation is of the claim itself
        topic_c = (re.search(r"uniform", s, re.I) and re.search(r"N_0|threshold", s)) \
            or re.search(r"(single|one)\s+(threshold|\$?N_0\b)[^.]*\b(all|every)\b", s, re.I) \
            or re.search(r"(threshold|N_0(\(t\))?\$?)[^.]{0,60}does not depend on\s*\$?t\b", s, re.I)
        if topic_c:
            allowed = re.search(r"no uniform|non-?uniform|not a uniform statement|"
                                r"not? (?:claimed|asserted|established)(?: to be)?[^.]{0,40}uniform", s, re.I) \
                and not re.search(r"does not depend on\s*\$?t\b", s, re.I)
            if not allowed:
                v.append((label, "(c) uniform threshold asserted", s[:160]))
        # (d) a numerical time placed inside the theorem's window, or the window-restricted
        #     Proposition 1 applied at a numerical time
        topic_d = (re.search(r"t_\\star[^.]*\\delta|\\delta[^.]*t_\\star", s) or
                   (re.search(r"t_\\star|t\s*=\s*0\.(5|25|75)|t\s*=\s*1\.0", s) and
                    re.search(r"window|\(0, ?\\delta\)|Theorem 1 applies|theorem applies", s, re.I)) or
                   (re.search(r"Proposition 1", s) and re.search(r"t_\\star|0\.5|0\.25|0\.75|1\.0", s)))
        if topic_d:
            allowed = re.search(r"not (?:claimed|proven|proved|certified|shown|asserted)[^.]{0,80}"
                                r"(lie|inside|window|\(0, ?\\delta\))|none of [^.]{0,30}is claimed|is not claimed|"
                                r"no statement that.{0,140}?(lie|inside)", s, re.I) \
                or re.search(r"not only in the theorem'?s window|not only in \(0, ?\\delta\)", s, re.I)
            if not allowed:
                v.append((label, "(d) numerical time tied to the theorem's window, or Proposition 1 applied at one", s[:160]))
        # (e) reservoir/large-bath limit tied to the harmonic class: negation must govern the harmonic phrase
        if re.search(r"limit|N_B\s*\\to\s*\\infty|reservoir|large[- ]bath|macroscopic", s, re.I):
            allowed_f = re.search(r"\bwhether\b|not addressed|open (question|connection|problem)|not (?:constructed|claimed|established)", s, re.I)
            for mo in re.finditer(r"\\mathcal\{H\}|(?<![A-Za-z])harmonic", s, re.I):
                ctx = s[max(0, mo.start() - 30):mo.start()]
                if re.search(r"anharmonic", s[mo.start():mo.start() + 12], re.I):
                    continue
                if re.search(r"effective(ly)?[- ]?$|effective(ly)?[- ][a-z]*$", ctx, re.I) and allowed_f:
                    continue   # the effective-harmonic firewall (f) owns this token
                if re.search(r"(not|;\s*not)\s*\$?\\?math?cal\{H\}?\s*$|not the harmonic\s*$|not\s*\$?$", ctx, re.I):
                    continue   # explicit 'not H' / 'not the harmonic' immediately before the token
                governed = _near_negation(s, mo.start(), 90) and re.search(
                    r"not a statement|no harmonic|nor is it|not (?:enter|become|reach|realised|realized|constructed|addressed|claimed)|"
                    r"remains anharmonic|never (?:enters|becomes)|does not (?:enter|become)", s, re.I)
                if not governed:
                    v.append((label, "(e) reservoir limit tied to the harmonic class without governing negation", s[:160]))
                    break
        # (f) effective-harmonic: only as an open, cited connection
        if re.search(r"effective(ly)?[- ]harmonic|effective oscillator bath|harmonic mapping", s, re.I):
            allowed = re.search(r"\bwhether\b", s, re.I) or \
                re.search(r"not addressed|open (question|connection|problem)|not (?:constructed|claimed|established)", s, re.I)
            if not allowed:
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
    full, s1 = ws(rendered_full), ws(rendered_s1)
    if full.count(stmt) < 2:
        v.append(("manuscript", "(a) theorem statement not present verbatim (whole statement) in both Section 4 and S1", stmt[:80]))
    if s1.count(stmt) < 1:
        v.append(("S1 sheet", "(a) theorem statement not present verbatim (whole statement)", stmt[:80]))
    # the full chain must also occur, in order, inside each rendered occurrence
    for name, body, need in (("rendered manuscript", full, 2), ("rendered S1 sheet", s1, 1)):
        start, found = 0, 0
        while True:
            i = body.find(ws(QUANTIFIER_CHAIN[0]), start)
            if i < 0:
                break
            pos2, ok = i, True
            for q in QUANTIFIER_CHAIN[1:]:
                j = body.find(ws(q), pos2)
                if j < 0:
                    ok = False
                    break
                pos2 = j
            if ok:
                found += 1
            start = i + 1
        if found < need:
            v.append((name, f"(a) quantifier chain found {found} time(s), need {need}", ""))
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
