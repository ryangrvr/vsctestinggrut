#!/usr/bin/env python3
"""Generate data/values.json — every number and generated expression the
manuscript may print, each with its formatting (declared once, here) and a
provenance entry.

Sources:
  * the authoritative numerical output of the record,
    backreaction_identifiability_0/publication_verification/v3_r2/v3_r2_results.json;
  * data/constants.json (gen_constants.py: Gibbs moments, exact series);
  * data/t7_check.json (check_t7.py: fresh small-time check).
"""
import math
import os

from common import AUTH_JSON, AUTH_JSON_REL, DATA, RECORD_DIR, SOURCE_COMMIT, SOURCE_REPO, dump_json, load_json

V = {}


def auth(json_path):
    return {"repo": SOURCE_REPO, "commit": SOURCE_COMMIT, "path": AUTH_JSON_REL,
            "json_path": json_path, "section": "authoritative numerical output (reference resolution)"}


def derived(script, method, inputs):
    return {"computed_by": "manuscript/tools/" + script, "method": method, "inputs": inputs}


def put(key, value, fmt, prov, allowed_in=None):
    """Register a value. fmt: ('sig', n) | ('fixed', n) | ('int',) | ('latex',) | ('text',)."""
    assert key not in V, key
    V[key] = {"value": value, "fmt": list(fmt), "text": fmt_value(value, fmt), "provenance": prov}
    if allowed_in:
        V[key]["allowed_in"] = allowed_in


def fmt_value(v, fmt):
    kind = fmt[0]
    if kind == "int":
        return str(int(v))
    if kind in ("latex", "text"):
        return str(v)
    if kind == "fixed":
        return f"{v:.{fmt[1]}f}"
    if kind == "sig":
        n = fmt[1]
        if v == 0:
            return "0"
        e = math.floor(math.log10(abs(v)))
        if -3 <= e <= 3:
            return f"{v:.{max(n - 1 - e, 0)}f}"
        m = v / 10 ** e
        ms = f"{m:.{n - 1}f}"
        if ms.lstrip("-").startswith("10"):           # rounding carried to 10.0
            e += 1
            ms = f"{v / 10 ** e:.{n - 1}f}"
        return rf"{ms}\times 10^{{{e}}}"
    raise ValueError(fmt)


# Numeric Gibbs moments may appear only in the numerical section and its tables
# (m2 is kept symbolic elsewhere).
NUMERIC_ZONE = ["06_numerical_illustration.md", "S5_numerical_tables.md"]


def main():
    d = load_json(AUTH_JSON)
    c = load_json(os.path.join(DATA, "constants.json"))
    t7 = load_json(os.path.join(DATA, "t7_check.json"))

    # ---------------- settings of the authoritative run
    put("num.nx", d["settings"]["nx"], ("int",), auth("settings.nx"))
    put("num.dt", d["settings"]["dt"], ("sig", 1), auth("settings.dt"))
    times = list(d["p1"].keys())                 # ["0.5", "0.25", "0.75", "1.0"]
    t_star = times[0]
    put("num.t_star", float(t_star), ("text",), auth("p1 (first key)"))
    V["num.t_star"]["text"] = t_star
    diag = times[1:]
    for i, t in enumerate(diag, 1):
        put(f"num.t_diag_{i}", float(t), ("text",), auth(f"p1 key #{i + 1}"))
        V[f"num.t_diag_{i}"]["text"] = t
    nbs = list(d["p1"][t_star].keys())
    put("num.nb_min", int(nbs[0]), ("int",), auth(f"p1.{t_star} keys"))
    put("num.nb_max", int(nbs[-1]), ("int",), auth(f"p1.{t_star} keys"))
    put("num.nb_count", len(nbs), ("int",), auth(f"p1.{t_star} keys"))

    # ---------------- numerical settings read from the record script that wrote the JSON
    import re
    rel = "publication_verification/v3_r2/extract_data.py"
    with open(os.path.join(os.path.dirname(AUTH_JSON), "extract_data.py"), encoding="utf-8") as f:
        code = f.read()
    sref = lambda what: {"repo": SOURCE_REPO, "commit": SOURCE_COMMIT, "path": RECORD_DIR + "/" + rel,
                         "section": what, "note": "script whose output schema matches the authoritative JSON"}
    L = float(re.search(r"\bL=([0-9.]+)", code).group(1))
    put("num.L", L, ("int",), sref("L= (quadrature half-width)"))
    gl = int(re.search(r"leggauss\((\d+)\)\n", code[code.index("Independent 1-D"):]).group(1))
    put("num.gl_1d", gl, ("int",), sref("independent 1-D check: leggauss(n)"))

    # ---------------- reference-protocol controls
    p0 = d["p0"]
    v0 = p0["0.0"]["var"]
    put("num.ref_var_t0", v0, ("sig", 10), auth("p0.0.0.var"), NUMERIC_ZONE)
    drift = max(abs(p0[t]["var"] - v0) for t in p0)
    put("num.ref_var_drift", drift, ("sig", 2), derived("gen_values.py", "max_t |Var x(t) - Var x(0)| over p0 times", [AUTH_JSON_REL + ":p0.*.var"]))
    put("num.ref_k3_max", max(abs(p0[t]["k3"]) for t in p0), ("sig", 2),
        derived("gen_values.py", "max_t |kappa3| over p0 times", [AUTH_JSON_REL + ":p0.*.k3"]))
    put("num.ref_mean_max", max(abs(p0[t]["mean"]) for t in p0), ("sig", 2),
        derived("gen_values.py", "max_t |mean| over p0 times", [AUTH_JSON_REL + ":p0.*.mean"]))
    put("num.gibbs_residual", d["gibbs_identity_residual"], ("sig", 2), auth("gibbs_identity_residual"))
    ind = d["independent_1d"]
    put("num.ind1d_m2", ind["m2"], ("sig", 10), auth("independent_1d.m2"), NUMERIC_ZONE)
    put("num.ind1d_m4", ind["m4"], ("sig", 10), auth("independent_1d.m4"), NUMERIC_ZONE)
    put("num.ref_rel_disc", abs(v0 - ind["m2"]) / ind["m2"], ("sig", 2),
        derived("gen_values.py", "|Var x(0) - m2(1-D)| / m2(1-D)", [AUTH_JSON_REL + ":p0.0.0.var", AUTH_JSON_REL + ":independent_1d.m2"]))

    # ---------------- ramp protocol at t_star and diagnostics
    row = d["p1"][t_star]
    put("num.g1_tstar_nbmin", row[nbs[0]]["gamma1_F"], ("sig", 4), auth(f"p1.{t_star}.{nbs[0]}.gamma1_F"))
    put("num.g1_tstar_nbmax", row[nbs[-1]]["gamma1_F"], ("sig", 4), auth(f"p1.{t_star}.{nbs[-1]}.gamma1_F"))
    nbg = [row[n]["NB_gamma1"] for n in nbs]
    put("num.nbg1_tstar", nbg[0], ("sig", 6), auth(f"p1.{t_star}.{nbs[0]}.NB_gamma1"))
    spread = (max(nbg) - min(nbg)) / abs(sum(nbg) / len(nbg))
    put("num.nbg1_tstar_relspread", spread, ("sig", 2),
        derived("gen_values.py", "(max - min)/|mean| of N_B*gamma1 over the N_B grid", [AUTH_JSON_REL + f":p1.{t_star}.*.NB_gamma1"]))
    for i, t in enumerate(diag, 1):
        r = d["p1"][t]
        put(f"num.g1_diag_{i}_nbmin", r[nbs[0]]["gamma1_F"], ("sig", 4), auth(f"p1.{t}.{nbs[0]}.gamma1_F"))
        g = [r[n]["NB_gamma1"] for n in nbs]
        put(f"num.nbg1_diag_{i}_relspread", (max(g) - min(g)) / abs(sum(g) / len(g)), ("sig", 2),
            derived("gen_values.py", "(max - min)/|mean| of N_B*gamma1 over the N_B grid", [AUTH_JSON_REL + f":p1.{t}.*.NB_gamma1"]))
        put(f"num.nbg1_diag_{i}_drift", abs(g[0] - g[-1]) / abs(g[-1]), ("sig", 2),
            derived("gen_values.py", "|NBg1(N_B min) - NBg1(N_B max)| / |NBg1(N_B max)|", [AUTH_JSON_REL + f":p1.{t}.*.NB_gamma1"]))
    sf = d["scaling_fit"]
    put("num.global_p", sf["global_p"], ("fixed", 6), auth("scaling_fit.global_p"))
    put("num.local_p_min", min(sf["local_p"]), ("fixed", 6), auth("scaling_fit.local_p (min)"))
    put("num.local_p_max", max(sf["local_p"]), ("fixed", 6), auth("scaling_fit.local_p (max)"))
    odd = d["odd_epsilon"]
    worst = max(abs(odd[k]["ratio"] + 1) for k in odd)
    put("num.odd_ratio_dev", worst, ("sig", 2), derived("gen_values.py", "max |ratio + 1| over odd_epsilon", [AUTH_JSON_REL + ":odd_epsilon.*.ratio"]))
    put("num.odd_sum_max", max(abs(odd[k]["sum"]) for k in odd), ("sig", 2),
        derived("gen_values.py", "max |kappa3(+eps) + kappa3(-eps)|", [AUTH_JSON_REL + ":odd_epsilon.*.sum"]))
    put("num.odd_nbs", ", ".join(odd.keys()), ("text",), auth("odd_epsilon keys"))

    # ---------------- high-precision constants (computed here)
    g = c["gibbs"]
    put("const.m2", float(g["m2"]), ("sig", 12), g["method"], NUMERIC_ZONE)
    put("const.m4", float(g["m4"]), ("sig", 12), g["method"], NUMERIC_ZONE)
    put("const.var_x0sq", float(g["var_x0sq"]), ("sig", 12), g["method"], NUMERIC_ZONE)
    put("const.identity_residual", float(g["identity_m2_plus_m4_minus_1"]), ("sig", 1), g["method"])
    put("const.var_cert_mid", g["record_certified_var"]["midpoint"], ("text",), g["record_certified_var"]["source"], NUMERIC_ZONE)
    put("const.C7", c["series"]["C_numeric"]["7"], ("sig", 6), c["series"]["method"], NUMERIC_ZONE)

    # ---------------- exact symbolic expressions (computed here; cross-checked against the record log)
    s = c["series"]
    sym_prov = {**s["method"], "record_cross_check": s["record_source"], "agreement_t7_to_t14": s["all_record_terms_agree"]}
    for k, latex in s["latex"].items():
        put(f"sym.{k}", latex, ("latex",), sym_prov)
    put("sym.C7_den", s["C7_denominator_coefficient"], ("int",), sym_prov)
    put("sym.order_max", s["order"], ("int",), sym_prov)

    # ---------------- S2 small-time check (computed here)
    tp = t7["method"]
    for i, r in enumerate(t7["rows"], 1):
        put(f"t7.t_{i}", r["t"], ("text",), tp)
        V[f"t7.t_{i}"]["text"] = f"{r['t']:g}"
        put(f"t7.K_{i}", r["K_numerical"], ("sig", 6), tp)
        put(f"t7.Klead_{i}", r["K_leading"], ("sig", 6), tp)
        put(f"t7.ratio_{i}", r["ratio"], ("fixed", 4), tp)
        put(f"t7.ratioB_{i}", r["ratio_method_B"], ("fixed", 4), tp)
        put(f"t7.ratioS_{i}", r["ratio_series_t7_to_t14"], ("fixed", 4), tp)
        put(f"t7.spread_{i}", r["relative_spread"], ("sig", 1), tp)

    # ---------------- cross-check: leading-order prediction N_B*gamma1 -> K(t)/m2^{3/2}
    m2 = float(g["m2"])
    for i, r in enumerate(t7["rows"], 1):
        key = f"{r['t']:g}"
        if key in d["p1"]:
            pred = r["K_numerical"] / m2 ** 1.5
            obs = d["p1"][key][nbs[-1]]["NB_gamma1"]
            tag = "tstar" if key == t_star else "t" + key.replace(".", "")
            put(f"x.pred_{tag}", pred, ("sig", 6),
                derived("gen_values.py", "K(t)/m2^{3/2} with K from check_t7.py and m2 from gen_constants.py",
                        ["data/t7_check.json", "data/constants.json"]), NUMERIC_ZONE)
            put(f"x.obs_{tag}", obs, ("sig", 6), auth(f"p1.{key}.{nbs[-1]}.NB_gamma1"), NUMERIC_ZONE)
            put(f"x.reldiff_{tag}", abs(pred - obs) / abs(obs), ("sig", 2),
                derived("gen_values.py", "|pred - obs| / |obs|", ["x.pred", "x.obs"]))

    dump_json(V, os.path.join(DATA, "values.json"))
    print(f"values.json: {len(V)} keys")
    for k in ("num.global_p", "num.nbg1_tstar_relspread", "num.nbg1_diag_3_drift", "x.reldiff_tstar", "x.reldiff_t025"):
        if k in V:
            print(f"  {k} = {V[k]['text']}")


if __name__ == "__main__":
    main()
