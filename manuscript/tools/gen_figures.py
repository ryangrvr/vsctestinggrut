#!/usr/bin/env python3
"""Generate the manuscript figures.

Fig. 1  model / protocol schematic with a minimal witness schematic (no data,
        no histograms): the clamped coordinate and the finite oscillator bath, the
        two protocol curves q(t) exactly as defined, and the witness logic.
Fig. 2  |gamma_1| versus N_B (log-log) at t_star, from the authoritative JSON,
        with the fitted power law (fit parameters from the same JSON) and a
        slope -1 reference line.
Fig. 3  normalised residual r(N_B) = N_B gamma_1(N_B) / N_B gamma_1(N_B max) - 1 at t_star = 0.5 and
        at t = 1.0, from the authoritative JSON only; two panels with their own vertical scales, because
        the effect sizes differ by orders of magnitude.

Each figure is written as PDF (for the LaTeX build) and PNG (for the HTML render);
data/figures.json records the provenance of every plotted quantity.
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from common import AUTH_JSON, AUTH_JSON_REL, DATA, FIG, dump_json, load_json

INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#d9d8d4"
SERIES1 = "#2a78d6"   # data
SERIES2 = "#eb6834"   # independent / reference overlays

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm", "font.size": 9,
    "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "axes.linewidth": 0.8, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "legend.frameon": False, "savefig.bbox": "tight", "savefig.dpi": 300,
})


def save(fig, name):
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, name + ".pdf"))
    fig.savefig(os.path.join(FIG, name + ".png"))
    plt.close(fig)


def s(u):
    return 10 * u ** 3 - 15 * u ** 4 + 6 * u ** 5     # protocol definition


def ramp(t):
    t = np.asarray(t, float)
    return np.where(t <= np.pi, s(np.clip(t / np.pi, 0, 1)), 1.0)


def fig1():
    fig = plt.figure(figsize=(7.0, 2.6))
    # (a) model
    ax = fig.add_axes([0.0, 0.0, 0.34, 1.0]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0.02, 0.95, "(a) model", fontsize=9, color=INK, va="top", weight="bold")
    ax.add_patch(FancyBboxPatch((0.04, 0.38), 0.30, 0.24, boxstyle="round,pad=0.02", fc="white", ec=INK2, lw=0.9))
    ax.text(0.19, 0.53, "clamped", ha="center", fontsize=7.5, color=INK)
    ax.text(0.19, 0.44, r"coordinate $q(t)$", ha="center", fontsize=7, color=INK)
    ys = [0.82, 0.64, 0.46, 0.28]
    for y in ys[:3] + ys[3:]:
        ax.add_patch(plt.Circle((0.80, y), 0.045, fc="white", ec=SERIES1, lw=1.0))
        ax.plot([0.34, 0.755], [0.5, y], color=GRID, lw=0.8, zorder=0)
    ax.text(0.80, 0.13, r"$\vdots\ N_B$ oscillators", ha="center", fontsize=8, color=INK)
    ax.text(0.80, 0.03, r"$\ddot x_j+x_j+x_j^3=q(t)/\sqrt{N_B}$", ha="center", fontsize=7.5, color=INK2)
    ax.add_patch(FancyArrowPatch((0.72, 0.30), (0.30, 0.37), arrowstyle="-|>", mutation_scale=9, color=SERIES2, lw=1.0,
                                 connectionstyle="arc3,rad=-0.3"))
    ax.text(0.30, 0.20, r"force $F_q(t)=N_B^{-1/2}\sum_j x_j(t)$", ha="center", fontsize=7.5, color=INK)

    # (b) protocols
    ax = fig.add_axes([0.42, 0.20, 0.26, 0.66])
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(t, np.zeros_like(t), color=INK2, lw=2, label="reference, $q\\equiv 0$")
    ax.plot(t, ramp(t), color=SERIES1, lw=2, label="ramp, $q=s(t/\\pi)$")
    ax.set_xticks([0, np.pi, 2 * np.pi]); ax.set_xticklabels(["0", r"$\pi$", r"$2\pi$"])
    ax.set_yticks([0, 1]); ax.set_ylim(-0.15, 1.3)
    ax.set_xlabel("$t$"); ax.set_ylabel("$q(t)$")
    ax.annotate(r"theorem: small $t\in(0,\delta)$" + "\n" + r"($\delta$ existential; not to scale)",
                xy=(0.05, 0.02), xytext=(2.6, 0.45), fontsize=6.5, color=INK2,
                arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.8))
    ax.legend(loc="upper left", fontsize=7, handlelength=1.5, bbox_to_anchor=(0.0, 1.02), ncol=1)
    ax.set_ylim(-0.15, 1.55)
    ax.set_title("(b) protocols", fontsize=9, loc="left", color=INK, weight="bold")

    # (c) witness logic (text schematic; no data)
    ax = fig.add_axes([0.72, 0.0, 0.28, 1.0]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0.0, 0.95, "(c) witness", fontsize=9, color=INK, va="top", weight="bold")
    box = dict(boxstyle="round,pad=0.35", fc="white", lw=0.9)
    ax.text(0.02, 0.70, "reference:\n" + r"$\kappa_3[F(t)]=0$" + "\nfor every $N_B$",
            fontsize=7.5, color=INK, va="center", bbox={**box, "ec": INK2})
    ax.text(0.02, 0.34, "ramp, small $t$:\n" + r"$\kappa_3[F(t)]\neq 0$" + "\nfor $N_B\\geq N_0(t)$",
            fontsize=7.5, color=INK, va="center", bbox={**box, "ec": SERIES1})
    ax.text(0.58, 0.52, r"$|\gamma_1|$ differs" + "\n" + r"$\Rightarrow$ no shared" + "\nsigned-affine\nrepresentation",
            fontsize=7.5, color=INK, va="center")
    ax.add_patch(FancyArrowPatch((0.42, 0.66), (0.56, 0.56), arrowstyle="-|>", mutation_scale=8, color=INK2, lw=0.8))
    ax.add_patch(FancyArrowPatch((0.42, 0.38), (0.56, 0.48), arrowstyle="-|>", mutation_scale=8, color=INK2, lw=0.8))
    save(fig, "fig1_schematic")
    return {"fig1_schematic": {"kind": "schematic", "data": "none",
                               "curves": "protocol definitions q = 0 and q = s(t/pi) on [0, pi], q = 1 on (pi, 2pi]",
                               "source": "protocol definition (record: BRI1_CANDIDATE_CHARTER.md §1)"}}


def fig2_fig3():
    d = load_json(AUTH_JSON)
    t7 = load_json(os.path.join(DATA, "t7_check.json"))
    const = load_json(os.path.join(DATA, "constants.json"))
    t_star = list(d["p1"].keys())[0]
    row = d["p1"][t_star]
    nb = np.array([int(k) for k in row], float)
    g1 = np.array([row[k]["gamma1_F"] for k in row])
    nbg = np.array([row[k]["NB_gamma1"] for k in row])
    sf = d["scaling_fit"]
    p, icpt = sf["global_p"], sf["intercept"]

    # Fig. 2
    fig, ax = plt.subplots(figsize=(3.4, 2.7))
    xx = np.geomspace(nb.min() / 1.3, nb.max() * 1.3, 50)
    ax.loglog(xx, np.exp(icpt) * xx ** (-p), color=SERIES1, lw=1.0, alpha=0.6,
              label=fr"fit, $|\gamma_1|\propto N_B^{{-p}}$, $p={p:.6f}$")
    ref = abs(g1[0]) * 3 * (xx / nb[0]) ** -1.0
    ax.loglog(xx, ref, color=SERIES2, lw=1.0, ls="--", label=r"slope $-1$ reference (offset)")
    ax.loglog(nb, np.abs(g1), "o", ms=4.5, mfc=SERIES1, mec="white", mew=0.8, color=SERIES1,
              label=fr"ramp protocol, $t_\star={t_star}$")
    ax.set_xlabel(r"bath size $N_B$"); ax.set_ylabel(r"$|\gamma_1[F(t_\star)]|$")
    ax.set_xticks(nb); ax.set_xticklabels([str(int(n)) for n in nb]); ax.minorticks_off()
    ax.legend(fontsize=7, loc="lower left")
    save(fig, "fig2_scaling")

    # Fig. 3: normalised residual of N_B*gamma_1 at t_star and at t = 1.0 (small multiples, own scales),
    # from the authoritative output only (the frozen evidence)
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.6))
    for ax, t, sc, lab in ((axes[0], t_star, 1e-10, "(a)"), (axes[1], "1.0", 1e-7, "(b)")):
        rr = d["p1"][t]
        keys = list(rr.keys())
        nbs = np.array([int(k) for k in keys], float)
        g = np.array([rr[k]["NB_gamma1"] for k in keys])
        ax.axhline(0, color=INK2, lw=0.8)
        ax.semilogx(nbs, (g / g[-1] - 1) / sc, "o", ms=5, mfc=SERIES1, mec="white", mew=0.8, color=SERIES1, zorder=4)
        ax.set_xticks(nbs); ax.set_xticklabels([str(int(n)) for n in nbs]); ax.minorticks_off()
        ax.set_xlabel(r"bath size $N_B$")
        e = int(round(np.log10(sc)))
        ax.set_ylabel(fr"$r(N_B)\ \ (\times 10^{{{e}}})$")
        ax.set_title(fr"{lab} $t = {t}$", fontsize=9, loc="left", color=INK)
    fig.tight_layout()
    save(fig, "fig3_residual")

    src = {"source": AUTH_JSON_REL, "json_paths": [f"p1.{t_star}.*.gamma1_F", f"p1.{t_star}.*.NB_gamma1",
                                                   "scaling_fit.global_p", "scaling_fit.intercept"]}
    return {
        "fig2_scaling": {**src, "reference_line": "slope -1 through 3x|gamma1(N_B min)| (display offset only)"},
        "fig3_residual": {"source": [AUTH_JSON_REL],
                          "quantity": "r(N_B) = N_B gamma1(N_B) / N_B gamma1(N_B max) - 1 at t_star and t = 1.0",
                          "json_paths": [f"p1.{t_star}.*.NB_gamma1", "p1.1.0.*.NB_gamma1"],
                          "scales": "panel (a) in units of 1e-10, panel (b) in units of 1e-7 (small multiples)"},
    }


def main():
    prov = {}
    prov.update(fig1())
    prov.update(fig2_fig3())
    dump_json(prov, os.path.join(DATA, "figures.json"))
    print("figures:", ", ".join(sorted(prov)))


if __name__ == "__main__":
    main()
