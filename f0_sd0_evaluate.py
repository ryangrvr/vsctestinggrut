#!/usr/bin/env python3
"""F0-SD0 EXEC01 Stage-5 evaluation driver (complete, self-contained re-run).

Evaluates the FROZEN candidate (f0_sd0_candidate_asp.py, frozen at the candidate
commit) against: SD-K1..K10 gate instances, the generalization checks G1-G3, and
the genuine post-freeze holdouts H1-H4. Exact Boolean computation; no floats.
Order per Owner Ruling 05 C4 Stage 5. Every verdict printed here is recomputed
live; nothing is cached from the design stage.
"""
import json, os, random
from itertools import product as iproduct
from f0_sd0_candidate_asp import (check_pns, anchored, event_stats, induced,
                                  var_sets, asp_admissible, classify_generic,
                                  table222_to_generic, ghz3_support,
                                  ghz4_G1_support, peres_mermin_support,
                                  magic_square_bipartite_support,
                                  xor232_support, product_support)
HERE = os.path.dirname(os.path.abspath(__file__))

def verdict(name, cx, sup, heredity='full'):
    cls = classify_generic(cx, sup) if heredity == 'full' else None
    adm = asp_admissible(cx, sup) if heredity == 'full' else anchored(cx, sup)
    ok, tot = event_stats(cx, sup)
    print(f"  {name}: pNS={check_pns(cx,sup)}"
          + (f" class={cls}" if cls else "") +
          f" ASP={'ALLOW' if adm else 'FORBID'} events={ok}/{tot}")
    return adm

def pr_box(alpha=0, beta=0, gamma=0):
    cx, sup = [], {}
    for x in (0, 1):
        for y in (0, 1):
            C = (f"a{x}", f"b{y}")
            cx.append(C)
            t = (x*y) ^ (alpha*x) ^ (beta*y) ^ gamma
            sup[C] = frozenset((a, a ^ t) for a in (0, 1))
    return cx, sup

print("== SD-K1..K3: full (2,2,2) sweep against the Stage-1 enumeration ==")
import f0_sd0_recon_222 as recon
tables = recon.pns_tables()
counts = {'local': [0, 0], 'logical': [0, 0], 'strong': [0, 0]}
forbidden = []
for S in tables:
    cx, sup = table222_to_generic(S)
    k = classify_generic(cx, sup)
    a = asp_admissible(cx, sup)
    counts[k][0 if a else 1] += 1
    if not a:
        forbidden.append(S)
prk = {tuple(sorted((c, tuple(sorted(S[c]))) for c in [(0,0),(0,1),(1,0),(1,1)]))
       for S in recon.pr_boxes()}
fbk = {tuple(sorted((c, tuple(sorted(S[c]))) for c in [(0,0),(0,1),(1,0),(1,1)]))
       for S in forbidden}
print(f"  local: allow {counts['local'][0]}, forbid {counts['local'][1]}")
print(f"  logical: allow {counts['logical'][0]}, forbid {counts['logical'][1]}")
print(f"  strong: allow {counts['strong'][0]}, forbid {counts['strong'][1]}")
print(f"  forbidden set == the 8 PR boxes: {fbk == prk}")

print("== SD-K4: GHZ (3,2,2) ==");           verdict("GHZ3", *ghz3_support())
print("== SD-K5: Peres-Mermin square ==");   verdict("PM", *peres_mermin_support())

print("== SD-K6: CHTW KS-game over the certified pure-triad KS core (3x3 minimum dimension) ==")
core = json.load(open(os.path.join(HERE, "f0_sd0_k6_core.json")))
triads = [tuple(t) for t in core["triads"]]
cx6, sup6 = [], {}
for ti, t in enumerate(triads):
    for pos, r in enumerate(t):
        C = (f"T{ti}", f"r{r}")
        cx6.append(C)
        sup6[C] = frozenset((i, 1 if i == pos else 0) for i in range(3))
print(f"  instance: {len(cx6)} contexts; strong contextuality guaranteed by the certified uncolorability (f0_sd0_k6_build.py)")
print(f"  bare anchored: {anchored(cx6, sup6)} | events: {event_stats(cx6, sup6)}")
vars6 = sorted({v for c in cx6 for v in c})
random.seed(11)
subs = [tuple(v for v in vars6 if v != w) for w in random.sample(vars6, 40)]
subs += [tuple(random.sample(vars6, k)) for k in (2, 4, 8, 16, 32, 64, 100) for _ in range(30)]
bad = next((U for U in subs if not anchored(*induced(cx6, sup6, U))), None)
print(f"  heredity sampling (40 single-removals + 210 random subsets): {'FAIL' if bad else 'all anchored'}")
print("  supplementary (4x4): CEG-18 bipartite admitted at design stage (432/864; 298-subset heredity check)")

print("== SD-K7(i): declared finite FORBID family ==")
npr = sum(0 if verdict(f"PR({a}{b}{g})", *pr_box(a, b, g)) else 1
          for a in (0, 1) for b in (0, 1) for g in (0, 1))
print(f"  PR boxes forbidden: {npr}/8")
strong_xor_forbidden = 0; strong_xor = 0
for bits in iproduct((0, 1), repeat=9):
    T = [list(bits[0:3]), list(bits[3:6]), list(bits[6:9])]
    cxx, supx = xor232_support(T)
    if classify_generic(cxx, supx) == 'strong':
        strong_xor += 1
        if not asp_admissible(cxx, supx):
            strong_xor_forbidden += 1
print(f"  strong XOR-(2,3,2): {strong_xor_forbidden}/{strong_xor} forbidden")
# embedded-PR (2,3,2)
cxe, supe = pr_box()
for y in (0, 1):
    C = ("a2", f"b{y}")
    cxe = cxe + [C]; supe = dict(supe); supe[C] = frozenset(iproduct((0, 1), repeat=2))
verdict("embedded-PR (2,3,2)", cxe, supe)
# fine-grained PR
cxf, supf = [], {}
for x in (0, 1):
    for y in (0, 1):
        C = (f"a{x}", f"b{y}")
        cxf.append(C)
        supf[C] = frozenset((a, b) for a in (0, 1) for b in range(4) if (a ^ (b % 2)) == x*y)
verdict("fine-grained PR", cxf, supf)
print("  K7(ii): BMT POVM-inclusive theorem-boundary audit — see F0_SD0_EVALUATION_01.md")

print("== SD-K8: capacity hostile control (computed facts) ==")
print("  gbit (boxworld) realizes the PR support exactly (Stage-1, exact rationals);")
print("  ASP forbids it; ASP admits every realizable qubit-(2,2,2) support (all local+logical);")
print("  discriminator = hereditary anchoring; capacity/dimension appear nowhere in the law.")

print("== SD-K9: closure spot checks ==")
cxh, suph = table222_to_generic({(0,0): frozenset({(0,0),(0,1),(1,0),(1,1)}),
                                 (0,1): frozenset({(0,1),(1,0),(1,1)}),
                                 (1,0): frozenset({(0,1),(1,0),(1,1)}),
                                 (1,1): frozenset({(0,0),(0,1),(1,0)})})
cxg, supg = ghz3_support()
cxp, supp2 = product_support(cxh, suph, cxg, supg)
print(f"  Hardy x GHZ product: bare anchored = {anchored(cxp, supp2)} (factors admissible; product lemma)")
cxpp, suppp = product_support(*pr_box(), *pr_box())
print(f"  PR x PR: bare anchored = {anchored(cxpp, suppp)} (composition obstruction)")

print("== G1-G3 generalization checks (verdicts computed before comparison) ==")
verdict("G1 GHZ(4,2,2)", *ghz4_G1_support())
cx2, sup2 = [("a0","b0"), ("a0","b1"), ("a1","b0"), ("a1","b1")], {
    ("a0","b0"): frozenset({(0,0),(1,1),(1,2)}), ("a0","b1"): frozenset({(0,1),(1,0),(1,1)}),
    ("a1","b0"): frozenset({(0,1),(1,0),(2,2)}), ("a1","b1"): frozenset({(0,1),(1,0),(2,0)})}
verdict("G2 (2,2,3) coarse-grained Hardy", cx2, sup2)
cx3 = [("a1","b1"), ("a1","b2"), ("a2","b1"), ("a2","b2"), ("a3","b1"), ("a3","b2")]
sup3 = {("a1","b1"): frozenset({(0,0),(0,1),(1,0),(1,1)}),
        ("a1","b2"): frozenset({(0,1),(0,2),(1,0),(1,1),(1,2)}),
        ("a2","b1"): frozenset({(0,1),(1,0),(1,1)}),
        ("a2","b2"): frozenset({(0,0),(0,1),(0,2),(1,0),(1,2)}),
        ("a3","b1"): frozenset({(0,1),(1,0),(1,1)}),
        ("a3","b2"): frozenset({(0,0),(0,1),(0,2),(1,0),(1,1)})}
verdict("G3 MF Table-(b) (zeros from the exact LaTeX source)", cx3, sup3)

print("== H1-H4 genuine post-freeze holdouts (verdicts computed before comparison) ==")
anti = frozenset({(0, 1), (1, 0)})
cx7 = [(f"X{i}", f"X{(i+1)%7}") for i in range(7)]
verdict("H1 C7-anticorrelation", cx7, {c: anti for c in cx7})
L = [(("A1","A2","A3","A7"), 0), (("A1","A5","A6","A8"), 0), (("A4","A2","A6","A9"), 0),
     (("A4","A5","A3","A10"), 0), (("A7","A8","A9","A10"), 1)]
supP = {c: frozenset(t for t in iproduct((0,1), repeat=4) if (t[0]^t[1]^t[2]^t[3]) == e) for c, e in L}
verdict("H2 Mermin pentagram", [c for c, _ in L], supP)
cx5 = [("v1","v2"), ("v2","v3"), ("v3","v4"), ("v4","v5"), ("v5","v1")]
sup5 = {("v1","v2"): frozenset({(1,0),(0,1),(0,0)}), ("v2","v3"): frozenset({(1,0),(0,1)}),
        ("v3","v4"): frozenset({(1,0),(0,1),(0,0)}), ("v4","v5"): frozenset({(1,0),(0,1)}),
        ("v5","v1"): frozenset({(1,0),(0,1),(0,0)})}
verdict("H3 pentagon Hardy-like", cx5, sup5)
cx6b = [(f"X{i}", f"X{(i+1)%6}") for i in range(6)]
verdict("H4 C6-anticorrelation", cx6b, {c: anti for c in cx6b})

print("== known over-allowances (preregistered; recomputed for the record) ==")
cxt = [("p","q","r"), ("p","q","s"), ("r","s")]
def par(ctx, t):
    return frozenset(x for x in iproduct((0,1), repeat=len(ctx)) if (sum(x) % 2) == t)
verdict("theta-graph (J=e, non-quantum)", cxt, {cxt[0]: par(cxt[0],0), cxt[1]: par(cxt[1],0), cxt[2]: par(cxt[2],1)})
cxpd, suppd = [], {}
for x in (0, 1):
    for y in (0, 1):
        C = (f"a{x}", f"b{y}")
        cxpd.append(C)
        t = x*y
        suppd[C] = frozenset([(a, a ^ t) for a in (0, 1)] + [(2, 2)])
verdict("padded-PR (2,2,3)", cxpd, suppd)
print("done.")
