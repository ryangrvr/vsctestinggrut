#!/usr/bin/env python3
"""Generate data/constants.json: Gibbs-marginal moments and the exact small-time
series of c(t), both computed here with fresh code.

1. Moments of the beta = 1 Gibbs marginal  rho(x) ~ exp(-x^2/2 - x^4/4):
   m2 = <x^2>, m4 = <x^4>, Var(x0^2) = m4 - m2^2, by mpmath quadrature at 40
   digits. Cross-checked against (i) the exact identity m2 + m4 = 1 and
   (ii) the certified enclosure quoted in the record.

2. Exact Taylor coefficients of
       c(t) = Cov(x0(t)^2, y1(t)),   y1'' + (1 + 3 x0^2) y1 = q(t),  q(t) = s(t/pi),
   by an order-by-order recursion in sympy, with Gibbs expectations reduced by
   the integration-by-parts identity m_{k+1} + m_{k+3} = k m_{k-1}. The output is
   compared term by term with the record's symbolic log.
"""
import os
import re

import mpmath as mp
import sympy as sp

from common import DATA, dump_json, record_path, src_ref, tool_ref

ORDER = 14  # the record's symbolic log runs through t^14


# ---------------------------------------------------------------- 1. moments
def gibbs_moments(dps=40):
    mp.mp.dps = dps
    w = lambda x: mp.e ** (-x ** 2 / 2 - x ** 4 / 4)
    Z = mp.quad(w, [-mp.inf, 0, mp.inf])
    m = {k: mp.quad(lambda x: x ** k * w(x), [-mp.inf, 0, mp.inf]) / Z for k in (2, 4, 6)}
    return m


# ------------------------------------------------------- 2. symbolic series
a, b, m2s = sp.symbols("a b m2", real=True)
PI = sp.pi


def q_coeffs(n):
    """Taylor coefficients of q(t) = s(t/pi), s(u) = 10u^3 - 15u^4 + 6u^5 (protocol definition)."""
    u = sp.Symbol("u")
    s = 10 * u ** 3 - 15 * u ** 4 + 6 * u ** 5
    poly = sp.Poly(sp.expand(s.subs(u, sp.Symbol("t") / PI)), sp.Symbol("t"))
    c = [sp.Integer(0)] * (n + 1)
    for (k,), v in poly.terms():
        if k <= n:
            c[k] = v
    return c


def cauchy(f, g, k):
    return sum(f[i] * g[k - i] for i in range(k + 1))


def series_coeffs(n):
    """Return (x0 coeffs, y1 coeffs) as polynomials in (a, b) through t^n."""
    x = [a, b] + [None] * (n - 1)
    y = [sp.Integer(0), sp.Integer(0)] + [None] * (n - 1)
    q = q_coeffs(n)
    x2 = []
    x3 = []
    for k in range(n - 1):
        # coefficients of x^2 and x^3 at order k need x_0..x_k only
        x2.append(sp.expand(cauchy(x, x, k)))
        x3.append(sp.expand(cauchy(x, x2, k)))
        x[k + 2] = sp.expand((-x[k] - x3[k]) / ((k + 2) * (k + 1)))
        x2y = sp.expand(cauchy(x2, y, k))
        y[k + 2] = sp.expand((-y[k] - 3 * x2y + q[k]) / ((k + 2) * (k + 1)))
    return x, y


def a_moment(j, cache={}):
    """E[a^j] under exp(-a^2/2 - a^4/4), reduced to m2 via m_{k+1} + m_{k+3} = k m_{k-1}."""
    if j % 2:
        return sp.Integer(0)
    if j == 0:
        return sp.Integer(1)
    if j == 2:
        return m2s
    if j not in cache:
        k = j - 3                      # m_{k+3} = k m_{k-1} - m_{k+1}
        cache[j] = sp.expand(k * a_moment(k - 1) - a_moment(k + 1))
    return cache[j]


def b_moment(j):
    return sp.Integer(0) if j % 2 else sp.factorial2(j - 1) if j else sp.Integer(1)


def expect(poly_ab):
    p = sp.Poly(sp.expand(poly_ab), a, b)
    return sp.expand(sum(c * a_moment(i) * b_moment(j) for (i, j), c in p.terms()))


def c_coeffs(n):
    x, y = series_coeffs(n)
    x2 = [sp.expand(cauchy(x, x, k)) for k in range(n + 1)]
    C = []
    for k in range(n + 1):
        cross = expect(sum(x2[i] * y[k - i] for i in range(k + 1)))
        C.append(sp.factor(sp.simplify(cross - m2s * expect(y[k]))))
    return C, x, y


def parse_record_log():
    """Coefficient strings printed by the record's symbolic preflight."""
    out = {}
    with open(record_path("preflight/bri1_preflight_symbolic.log"), encoding="utf-8") as f:
        for line in f:
            mo = re.match(r"\(2\) X1/P1: c\(t\) coefficient of t\^(\d+): (.*)$", line.strip())
            if mo:
                out[int(mo.group(1))] = mo.group(2)
    return out


def record_certified_var():
    with open(record_path("BRI1_ANALYTIC_ESCAPE_THEOREM.md"), encoding="utf-8") as f:
        txt = f.read()
    mo = re.search(r"Var\(x₀²\) ∈ ([0-9.]+)… ± ([0-9]+)·10⁻([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", txt)
    sup = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    return mo.group(1), int(mo.group(2)), -int(mo.group(3).translate(sup))


def y7_latex(y7):
    """b7 written as -(1 + 3a^2)/(K pi^3) + 1/(J pi^5), with K, J read off the exact coefficient."""
    pa2 = sp.Poly(sp.expand(y7), a)
    c_a2, c_a0 = pa2.coeff_monomial(a ** 2), pa2.coeff_monomial(1)
    k = sp.nsimplify(-1 / (c_a2 / 3 * PI ** 3))               # c_a2 = -3/(K pi^3)
    rest = sp.simplify(c_a0 + 1 / (k * PI ** 3))              # = 1/(J pi^5)
    j = sp.nsimplify(1 / (rest * PI ** 5))
    assert sp.simplify(y7 - (-(1 + 3 * a ** 2) / (k * PI ** 3) + 1 / (j * PI ** 5))) == 0
    return rf"-\frac{{1 + 3a^{{2}}}}{{{k}\pi^{{3}}}} + \frac{{1}}{{{j}\pi^{{5}}}}"


def main():
    m = gibbs_moments()
    m2, m4, m6 = m[2], m[4], m[6]
    var = m4 - m2 ** 2
    cert_str, cert_k, cert_e = record_certified_var()
    cert_mid = mp.mpf(cert_str)
    cert_tol = cert_k * mp.mpf(10) ** cert_e + mp.mpf(10) ** (-(len(cert_str.split(".")[1])))
    var_in_cert = abs(var - cert_mid) <= cert_tol

    C, x, y = c_coeffs(ORDER)
    rec = parse_record_log()
    agree = {}
    for k, s in rec.items():
        r = sp.sympify(s, locals={"m2": m2s, "pi": PI})
        agree[k] = sp.simplify(r - C[k]) == 0
    assert all(C[k] == 0 for k in range(7)), "C0..C6 must vanish"
    VarS = sp.Symbol("V")  # Var(x0^2) = 1 - m2 - m2^2
    C7 = sp.simplify(C[7])
    # express C7, C8 in terms of Var(x0^2) = 1 - m2 - m2^2
    C7_over_var = sp.simplify(C7 / (1 - m2s - m2s ** 2))
    C8_over_var = sp.simplify(C[8] / (1 - m2s - m2s ** 2))
    ratio_8_7 = sp.simplify(C[8] / C7)
    den7 = sp.fraction(sp.together(-C7_over_var * PI ** 3))[1]

    var_sym = sp.Symbol(r"\operatorname{Var}(x_0^2)")
    t = sp.Symbol("t")
    latex = {
        "C7": sp.latex(C7_over_var * var_sym),
        "C8": sp.latex(C8_over_var * var_sym),
        "ratio_C8_C7": sp.latex(ratio_8_7),
        "y1_b5": sp.latex(sp.simplify(y[5])),
        "y1_b6": sp.latex(sp.simplify(y[6])),
        "y1_b7": y7_latex(y[7]),
        "x0_a2": sp.latex(sp.expand(x[2])),
        "x0sq_d2": sp.latex(sp.expand(cauchy(x, x, 2)), order="lex"),
        "y1_b7_a2coef": sp.latex(sp.Poly(sp.expand(y[7]), a).coeff_monomial(a ** 2)),
        "C7_in_m2": sp.latex(C7),
        "q3": sp.latex(q_coeffs(5)[3]), "q4": sp.latex(q_coeffs(5)[4]), "q5": sp.latex(q_coeffs(5)[5]),
    }

    # numeric series coefficients at the high-precision m2 (for the S2 secondary check)
    Cnum = [float(sp.N(C[k].subs(m2s, sp.Float(str(m2), 40)), 30)) for k in range(ORDER + 1)]

    out = {
        "gibbs": {
            "m2": mp.nstr(m2, 30), "m4": mp.nstr(m4, 30), "m6": mp.nstr(m6, 30),
            "var_x0sq": mp.nstr(var, 30),
            "identity_m2_plus_m4_minus_1": mp.nstr(m2 + m4 - 1, 5),
            "var_from_identity_1_minus_m2_minus_m2sq": mp.nstr(1 - m2 - m2 ** 2, 30),
            "record_certified_var": {"midpoint": cert_str, "radius": f"{cert_k}e{cert_e}",
                                     "contains_computed": bool(var_in_cert),
                                     "source": src_ref("BRI1_ANALYTIC_ESCAPE_THEOREM.md", "T1 step 6")},
            "method": tool_ref("gen_constants.py", "mpmath.quad on (-inf,0,inf), 40 digits"),
        },
        "series": {
            "order": ORDER,
            "C_latex_in_m2": {str(k): sp.latex(C[k]) for k in range(ORDER + 1)},
            "C_numeric": {str(k): Cnum[k] for k in range(ORDER + 1)},
            "C7_denominator_coefficient": int(den7),
            "latex": latex,
            "record_log_agreement": {str(k): bool(v) for k, v in sorted(agree.items())},
            "all_record_terms_agree": bool(all(agree.values())) and len(agree) == ORDER - 6,
            "C0_to_C6_vanish": True,
            "method": tool_ref("gen_constants.py", "sympy order-by-order Taylor recursion; Gibbs moments reduced by m_{k+1}+m_{k+3}=k m_{k-1}"),
            "record_source": src_ref("preflight/bri1_preflight_symbolic.log", "lines (2)"),
        },
    }
    dump_json(out, os.path.join(DATA, "constants.json"))
    print("m2 =", mp.nstr(m2, 20), " Var(x0^2) =", mp.nstr(var, 20), " in record enclosure:", var_in_cert)
    print("C7 =", C7, " denominator coefficient:", out["series"]["C7_denominator_coefficient"])
    print("record log agreement t^7..t^14:", out["series"]["record_log_agreement"])


if __name__ == "__main__":
    main()
