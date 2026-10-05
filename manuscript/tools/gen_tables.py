#!/usr/bin/env python3
"""Generate the manuscript tables (Markdown pipe tables) from machine-readable output.

  main_tstar   §6   ramp-protocol skewness at t_star across the bath-size grid
  s5_full      S5   full finite-epsilon record at t_star
  s5_diag      S5   diagnostic times
  s5_ref       S5   reference-protocol stationarity control
  s5_odd       S5   odd-epsilon symmetry control
  s5_cross     S5   leading-order prediction (independent code) vs finite-N_B values
  s2_t7        S2   small-time consistency check (computed by check_t7.py)

Written to data/tables/<name>.md; provenance in data/tables.json.
"""
import os

from common import AUTH_JSON, AUTH_JSON_REL, DATA, dump_json, load_json
from gen_values import fmt_value

TDIR = os.path.join(DATA, "tables")


def m(v, fmt):
    return "$" + fmt_value(v, fmt) + "$"


def table(header, rows, align=None):
    align = align or ["r"] * len(header)
    sep = ["---:" if a == "r" else ":---" for a in align]
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def main():
    os.makedirs(TDIR, exist_ok=True)
    d = load_json(AUTH_JSON)
    t7 = load_json(os.path.join(DATA, "t7_check.json"))
    const = load_json(os.path.join(DATA, "constants.json"))
    times = list(d["p1"].keys())
    ts, diag = times[0], times[1:]
    nbs = list(d["p1"][ts].keys())
    prov = {}
    T = {}

    r = d["p1"][ts]
    T["main_tstar"] = table(
        ["$N_B$", r"$\gamma_1[F(t_\star)]$", r"$N_B\,\gamma_1[F(t_\star)]$"],
        [[n, m(r[n]["gamma1_F"], ("sig", 6)), m(r[n]["NB_gamma1"], ("sig", 10))] for n in nbs])
    prov["main_tstar"] = {"source": AUTH_JSON_REL, "json_paths": [f"p1.{ts}.*.gamma1_F", f"p1.{ts}.*.NB_gamma1"]}

    T["s5_full"] = table(
        ["$N_B$", r"$\varepsilon$", r"$\kappa_3(X^\varepsilon)$", r"$\mathrm{Var}\,X^\varepsilon$",
         r"$\kappa_3(F)$", r"$\gamma_1(F)$", r"$N_B\,\gamma_1$"],
        [[n, m(r[n]["epsilon"], ("fixed", 4)), m(r[n]["kappa3_X"], ("sig", 7)), m(r[n]["var_X"], ("sig", 10)),
          m(r[n]["kappa3_F"], ("sig", 7)), m(r[n]["gamma1_F"], ("sig", 7)), m(r[n]["NB_gamma1"], ("sig", 10))]
         for n in nbs])
    prov["s5_full"] = {"source": AUTH_JSON_REL, "json_paths": [f"p1.{ts}.*"]}

    rows = []
    for t in [ts] + diag:
        rr = d["p1"][t]
        g = [rr[n]["NB_gamma1"] for n in nbs]
        rows.append([f"${t}$", m(rr[nbs[0]]["gamma1_F"], ("sig", 6)), m(rr[nbs[-1]]["gamma1_F"], ("sig", 6)),
                     m(g[0], ("sig", 8)), m((max(g) - min(g)) / abs(sum(g) / len(g)), ("sig", 2))])
    T["s5_diag"] = table(
        ["$t$", fr"$\gamma_1$, $N_B={nbs[0]}$", fr"$\gamma_1$, $N_B={nbs[-1]}$", fr"$N_B\gamma_1$, $N_B={nbs[0]}$",
         r"rel. spread of $N_B\gamma_1$"], rows)
    prov["s5_diag"] = {"source": AUTH_JSON_REL, "json_paths": ["p1.*.*.gamma1_F", "p1.*.*.NB_gamma1"],
                       "derived": "relative spread = (max - min)/|mean| over the N_B grid (gen_tables.py)"}

    p0 = d["p0"]
    T["s5_ref"] = table(
        ["$t$", r"$\mathbb{E}\,x(t)$", r"$\mathrm{Var}\,x(t)$", r"$\kappa_3[x(t)]$"],
        [[f"${t}$", m(p0[t]["mean"], ("sig", 2)), m(p0[t]["var"], ("sig", 10)), m(p0[t]["k3"], ("sig", 2))] for t in p0])
    prov["s5_ref"] = {"source": AUTH_JSON_REL, "json_paths": ["p0.*"]}

    odd = d["odd_epsilon"]
    T["s5_odd"] = table(
        ["$N_B$", r"$\kappa_3(X^{+\varepsilon})$", r"$\kappa_3(X^{-\varepsilon})$", "sum", "ratio"],
        [[n, m(o["k3_plus"], ("sig", 9)), m(o["k3_minus"], ("sig", 9)), m(o["sum"], ("sig", 2)),
          m(o["ratio"], ("fixed", 12))] for n, o in odd.items()])
    prov["s5_odd"] = {"source": AUTH_JSON_REL, "json_paths": ["odd_epsilon.*"]}

    m2 = float(const["gibbs"]["m2"])
    rows = []
    for row in t7["rows"]:
        key = f"{row['t']:g}"
        if key in d["p1"]:
            pred = row["K_numerical"] / m2 ** 1.5
            obs = d["p1"][key][nbs[-1]]["NB_gamma1"]
            rows.append([f"${key}$", m(obs, ("sig", 9)), m(pred, ("sig", 9)), m(abs(pred - obs) / abs(obs), ("sig", 2))])
    T["s5_cross"] = table(
        ["$t$", fr"$N_B\gamma_1$ at $N_B={nbs[-1]}$", r"$K(t)/m_2^{3/2}$ (independent)", "rel. difference"], rows)
    prov["s5_cross"] = {"source": [AUTH_JSON_REL, "manuscript/data/t7_check.json", "manuscript/data/constants.json"],
                        "json_paths": [f"p1.*.{nbs[-1]}.NB_gamma1", "rows.*.K_numerical", "gibbs.m2"]}

    T["s2_t7"] = table(
        ["$t$", r"$K(t)$ numerical", r"$3C_7t^7$", "ratio", "ratio (method B)", r"ratio (series to $t^{14}$)",
         "rel. spread"],
        [[f"${row['t']:g}$", m(row["K_numerical"], ("sig", 6)), m(row["K_leading"], ("sig", 6)),
          m(row["ratio"], ("fixed", 6)), m(row["ratio_method_B"], ("fixed", 6)),
          m(row["ratio_series_t7_to_t14"], ("fixed", 6)), m(row["relative_spread"], ("sig", 1))] for row in t7["rows"]])
    prov["s2_t7"] = {"source": "manuscript/data/t7_check.json", "computed_by": "manuscript/tools/check_t7.py"}

    for name, txt in T.items():
        with open(os.path.join(TDIR, name + ".md"), "w", encoding="utf-8") as f:
            f.write(txt)
    dump_json(prov, os.path.join(DATA, "tables.json"))
    print("tables:", ", ".join(T))


if __name__ == "__main__":
    main()
