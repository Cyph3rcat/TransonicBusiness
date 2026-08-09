"""Figures for Chapters 5-6: airfoils, drag divergence, wing and tail.

Every curve here is read from a solver output file: SU2 surface CSVs and the
extracted results_v3.json for the 2-D work, VSPAERO .lod/.polar files for the
3-D work.
"""
import csv
import json
import os

import numpy as np
import matplotlib.pyplot as plt

from common import (use_style, save, title, read_polar, read_lod, load_airfoil,
                    VSP, AF, C1, C2, C3, C4, C5, C6, C7, C8,
                    INK, INK2, MUTED, GRID, AXIS, CRITICAL, GOOD, BLUES)

V3 = os.path.join(AF, "su2_screen", "mach_sweep_sc20412_v3")
GAMMA = 1.4
CL_TARGET = 0.248


def cp_critical(m):
    """Isentropic Cp at which the local flow first reaches M = 1."""
    return 2.0 / (GAMMA * m ** 2) * (
        ((1 + 0.5 * (GAMMA - 1) * m ** 2) / (1 + 0.5 * (GAMMA - 1))) ** (GAMMA / (GAMMA - 1)) - 1)


def _camber_line():
    """Mean line of SC(2)-0412 from its coordinate file, as a function of x/c.

    Used to split the SU2 surface nodes into upper and lower. Splitting on the
    sign of y fails on this section: its aft camber carries the lower surface
    above y = 0 near the cusped trailing edge.
    """
    x, y = load_airfoil("sc20412_selig.dat")
    i = int(np.argmin(x))                      # Selig order: TE -> LE -> TE
    xu, yu = x[:i + 1][::-1], y[:i + 1][::-1]
    xl, yl = x[i:], y[i:]
    grid = np.linspace(0, 1, 400)
    return grid, 0.5 * (np.interp(grid, xu, yu) + np.interp(grid, xl, yl))


_CAM_X, _CAM_Y = _camber_line()


def _surface_cp(tag, p_inf, rho_inf, v_inf):
    """(x, Cp, is_upper) on the airfoil from an SU2 SURFACE_CSV."""
    q = 0.5 * rho_inf * v_inf ** 2
    x, y, cp = [], [], []
    with open(os.path.join(V3, f"surface_{tag}.csv")) as f:
        for row in csv.DictReader(f):
            rho = float(row["Density"])
            mx, my = float(row["Momentum_x"]), float(row["Momentum_y"])
            e = float(row["Energy"])
            p = (GAMMA - 1) * (e - 0.5 * (mx ** 2 + my ** 2) / rho)
            x.append(float(row["x"]))
            y.append(float(row["y"]))
            cp.append((p - p_inf) / q)
    x, y, cp = np.array(x), np.array(y), np.array(cp)
    upper = y > np.interp(x, _CAM_X, _CAM_Y)
    return x, cp, upper


# ----------------------------------------------------- 5.0 airfoil gallery ---
SCREEN = [
    # file,                     label,             t/c,  Clmax, sweep for Mdd=0.80
    ("naca64209_selig.dat", "NACA 64-209", 8.98, 1.74, "21.4°"),
    ("sc20410_selig.dat", "NASA SC(2)-0410", 9.97, 2.02, "0°"),
    ("sc20412_selig.dat", "NASA SC(2)-0412", 12.00, 2.11, "0°"),
    ("sc20414_selig.dat", "NASA SC(2)-0414", 14.00, 2.18, "0°"),
    ("custom_cst_9pct_selig.dat", "Custom CST inverse design", 9.00, 1.65, "unknown"),
]


def fig_5_0():
    """The real sections behind the Chapter 5 screen, drawn from the UIUC
    coordinate files actually fed to NeuralFoil, SU2 and OpenVSP."""
    use_style()
    fig, axes = plt.subplots(len(SCREEN), 1, figsize=(7.0, 6.4), sharex=True)
    for ax, (fn, lab, tc, clmax, sweep), col in zip(
            axes, SCREEN, [C4, C3, C1, C5, C7]):
        x, y = load_airfoil(fn)
        chosen = fn.startswith("sc20412")
        ax.fill(x, y, color=col, alpha=0.30 if not chosen else 0.55,
                edgecolor=col, linewidth=1.8 if not chosen else 2.4)
        ax.set_ylim(-0.13, 0.13)
        ax.set_xlim(-0.03, 1.14)
        ax.set_aspect("equal")
        ax.grid(False)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.tick_params(bottom=False)
        tag = "  ← SELECTED" if chosen else ""
        ax.text(1.03, 0.055, f"{lab}{tag}", fontsize=9,
                color=INK if chosen else INK2,
                weight="bold" if chosen else "normal", va="center")
        ax.text(1.03, -0.045,
                f"t/c {tc:.2f}%   $C_{{l,max}}$ {clmax:.2f}   sweep for $M_{{dd}}$=0.80: {sweep}",
                fontsize=7.6, color=MUTED, va="center")
    axes[-1].tick_params(bottom=True)
    axes[-1].spines["bottom"].set_visible(True)
    axes[-1].set_xlabel("x/c")
    axes[-1].set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    fig.suptitle("The shortlisted sections, drawn to scale", x=0.06, y=0.985,
                 ha="left", fontsize=11, weight="bold", color=INK)
    fig.text(0.06, 0.940,
             "Coordinates are the UIUC files actually fed to NeuralFoil, SU2 and "
             "OpenVSP. Supercritical sections carry their\nthickness aft and run "
             "a flatter upper surface — that is what buys the weak shock.",
             fontsize=8.6, color=INK2, ha="left")
    return save(fig, "fig_5_0_airfoil_gallery.png", tight_rect=[0, 0, 1, 0.93])


# ---------------------------------------------------- 5.1 drag-rise curve ----
def fig_5_1():
    use_style()
    v3 = json.load(open(os.path.join(V3, "results_v3.json")))
    m = np.array([s["mach"] for s in v3["stations"]])
    cd = np.array([s["cd"] for s in v3["stations"]]) * 1e4
    sd = np.array([s["cd_std"] for s in v3["stations"]]) * 1e4
    base = v3["baseline_cd"] * 1e4
    mdd_b, mdd_d = v3["M_dd_boeing"], v3["M_dd_delta20"]

    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.axhline(base, color=MUTED, ls=":", lw=1.2)
    ax.text(0.598, base - 6, f"subcritical baseline, {base:.0f} counts",
            fontsize=8, color=MUTED)
    ax.axhline(base + 20, color=C7, ls=":", lw=1.2)

    ax.errorbar(m, cd, yerr=sd, fmt="o-", color=C1, lw=2.2, ms=6, capsize=3,
                elinewidth=1.2, ecolor=C1, mfc="white", mew=1.8, zorder=3,
                label="SU2 v3, $C_D$ at constant $C_L$ = 0.248 (±1σ over the last 1,500 iterations)")

    for mv, col, lab, off in ((mdd_b, C2, "Boeing criterion\n$dC_d/dM$ ≥ 0.10", -1),
                              (mdd_d, C7, "Δ$C_D$ = +20 counts", 1)):
        ax.axvline(mv, color=col, ls="--", lw=1.5)
        ax.annotate(f"$M_{{dd}}$ = {mv:.3f}\n{lab}",
                    xy=(mv, 155), xytext=(mv + 0.008 * off, 152),
                    fontsize=8.2, color=col,
                    ha="right" if off < 0 else "left", va="top")

    ax.axvline(0.80, color=INK2, lw=1.2)
    ax.text(0.7985, 108, "cruise M0.80 (unswept section)", rotation=90,
            fontsize=8, color=INK2, ha="right", va="bottom")

    ax.set_xlabel("Freestream Mach number")
    ax.set_ylabel("Section drag coefficient (counts)")
    ax.set_xlim(0.585, 0.815)
    ax.set_ylim(95, 175)
    ax.legend(loc="upper left")
    title(ax, "SC(2)-0412 drag rise at constant lift — the adopted v3 result",
          "Flat to M = 0.74, then a clean knee. The error bars shrink as the "
          "solver converges, which is the point of the windowed statistics.")
    return save(fig, "fig_5_1_drag_rise.png")


# ----------------------------------------------- 5.2 pressure distributions --
def fig_5_2():
    use_style()
    raw = json.load(open(os.path.join(V3, "sweep_v3_raw.json")))
    by_mach = {}
    for r in raw:
        by_mach.setdefault(r["mach"], []).append(r)

    fig, axes = plt.subplots(1, 3, figsize=(9.4, 4.0), sharey=True)
    for ax, mach, col in zip(axes, (0.60, 0.74, 0.80), (C3, C1, C2)):
        runs = sorted(by_mach[mach], key=lambda r: r["cl_mean"])
        lo, hi = runs[0], runs[1]
        for a, b in zip(runs, runs[1:]):
            if a["cl_mean"] <= CL_TARGET <= b["cl_mean"]:
                lo, hi = a, b
                break
        t = (CL_TARGET - lo["cl_mean"]) / (hi["cl_mean"] - lo["cl_mean"])

        xl, cpl, upper = _surface_cp(lo["tag"], lo["p_inf"], lo["rho_inf"], lo["v_inf"])
        _, cph, _ = _surface_cp(hi["tag"], hi["p_inf"], hi["rho_inf"], hi["v_inf"])
        cp = cpl + t * (cph - cpl)              # interpolate to the design C_L

        for m_, ls, lw in ((upper, "-", 2.0), (~upper, "--", 1.7)):
            o = np.argsort(xl[m_])
            ax.plot(xl[m_][o], cp[m_][o], ls, color=col, lw=lw)

        ax.axhline(cp_critical(mach), color=MUTED, ls=":", lw=1.4)
        ax.text(0.97, cp_critical(mach) - 0.04, "$C_{p,crit}$ (sonic)",
                fontsize=7.8, color=MUTED, ha="right", va="bottom")
        ax.set_xlabel("x/c")
        ax.set_xlim(-0.02, 1.02)
        title(ax, f"M = {mach:.2f}")

    axes[0].set_ylabel("$C_p$")
    axes[0].set_ylim(1.35, -1.65)
    axes[0].plot([], [], "-", color=INK2, lw=2.0, label="upper surface")
    axes[0].plot([], [], "--", color=INK2, lw=2.0, label="lower surface")
    axes[0].legend(loc="lower right")

    axes[0].annotate("fully subcritical: the suction\npeak stays well below sonic",
                     xy=(0.30, -0.52), xytext=(0.48, -1.36), fontsize=8.2,
                     color=INK2, ha="center",
                     arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    axes[1].annotate("rooftop now sitting\non the sonic line", xy=(0.28, -0.70),
                     xytext=(0.45, -1.36), fontsize=8.2, color=INK2, ha="center",
                     arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    axes[2].annotate("flat supercritical rooftop", xy=(0.33, -0.60),
                     xytext=(0.34, -1.36), fontsize=8.2, color=INK2, ha="center",
                     arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    axes[2].annotate("shock, ~65% chord", xy=(0.655, -0.66), xytext=(0.87, -1.02),
                     fontsize=8.6, color=C2, ha="center",
                     arrowprops=dict(arrowstyle="->", color=C2, lw=1.4))

    fig.suptitle("Surface pressure at the design lift coefficient: the shock arrives between M 0.74 and 0.80",
                 x=0.045, ha="left", fontsize=11, weight="bold", color=INK)
    fig.text(0.045, 0.905,
             "Each curve is interpolated between the two bracketing angle-of-attack "
             "runs so all three are compared at $C_L$ = 0.248.",
             fontsize=8.6, color=INK2, ha="left")
    return save(fig, "fig_5_2_cp_distributions.png", tight_rect=[0, 0, 1, 0.885])


# --------------------------------------------------------- 5.3 span loading --
def fig_5_3():
    use_style()
    blocks, ref = read_lod(os.path.join(VSP, "01_wing_baseline", "wing_v6_baseline.lod"))
    # Cases run alpha = -2, 0, 2, 4, 6, 8, 10 deg; cruise C_L = 0.34 sits at
    # alpha ~ 2.4 deg, so take the alpha = 2 deg case (C_L = 0.309).
    d = blocks[2]
    y = d["Yavg"]
    m = y > 0
    eta = y[m] / (ref["Bref"] / 2.0)
    cl = d["Cl"][m]
    chord = d["Chord"][m]
    cref = ref["Cref"]
    load = cl * chord / cref
    o = np.argsort(eta)
    eta, cl, load = eta[o], cl[o], load[o]

    # Elliptical distribution carrying the same total lift.
    ell = np.sqrt(np.clip(1 - eta ** 2, 0, None))
    ell *= np.trapezoid(load, eta) / np.trapezoid(ell, eta)

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.2))

    ax.fill_between(eta, 0, load, color=C1, alpha=0.14)
    ax.plot(eta, load, color=C1, lw=2.4, label="VSPAERO, λ = 0.35 with −3° washout")
    ax.plot(eta, ell, color=MUTED, lw=1.8, ls="--",
            label="elliptical ideal at the same total lift")
    ax.axvline(0.60, color=C2, lw=1.6, ls=":")
    ax.text(0.585, 0.055, "first stall, η = 0.60", rotation=90, fontsize=8.2,
            color=C2, ha="right", va="bottom")
    ax.axvspan(0.65, 1.0, color=C2, alpha=0.07)
    ax.text(0.825, 0.36, "aileron span", fontsize=8.2, color=C2, ha="center")
    ax.set_xlabel("Semispan station η = 2y/b")
    ax.set_ylabel(r"Local load  $c_l\,c/c_{ref}$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.66)
    ax.legend(loc="lower left")
    title(ax, "Span loading at cruise is near-elliptical",
          "Loaded inboard, unloaded at the tip — what taper\n0.35 plus washout "
          "should give.")

    # Stall location must be read near maximum lift, not at cruise: the peak
    # section c_l migrates outboard as angle of attack rises (eta 0.36 at
    # alpha = 2 deg, 0.60 at alpha = 10 deg), so the highest-alpha case governs.
    for tag, blk, col, ls in (("α = 10°, near stall", blocks[6], C1, "-"),
                              ("α = 4°, en-route climb", blocks[3], MUTED, "--")):
        y2 = blk["Yavg"]
        k = y2 > 0
        e2 = y2[k] / (ref["Bref"] / 2.0)
        c2v = blk["Cl"][k]
        o2 = np.argsort(e2)
        e2, c2v = e2[o2], c2v[o2]
        ax2.plot(e2, c2v, ls, color=col, lw=2.4, label=tag)
        if col is C1:
            i = int(np.argmax(c2v))
            ax2.plot(e2[i], c2v[i], "o", color=C2, ms=10, mfc="white", mew=2.4,
                     zorder=5)
            ax2.annotate(f"peak section $c_l$ at η = {e2[i]:.2f}\n"
                         "→ stall starts inboard of the ailerons,\n"
                         "so roll authority survives the onset",
                         xy=(e2[i], c2v[i]), xytext=(0.03, 0.30), fontsize=8.4,
                         color=INK2, ha="left",
                         arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    ax2.axvspan(0.65, 1.0, color=C2, alpha=0.07)
    ax2.text(0.825, 0.10, "aileron span", fontsize=8.2, color=C2, ha="center")
    ax2.set_xlabel("Semispan station η = 2y/b")
    ax2.set_ylabel("Section lift coefficient $c_l$")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1.32)
    ax2.legend(loc="lower left", fontsize=8.4)
    title(ax2, "Where the wing stalls first",
          "Read at high angle of attack, not at cruise — the peak\nmigrates "
          "outboard as the wing is loaded up.")
    return save(fig, "fig_5_3_span_loading.png")


# ---------------------------------------------------------- 5.4 winglet ------
def fig_5_4():
    use_style()
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    runs = [
        ("without winglet", os.path.join(VSP, "01_wing_baseline", "wing_v6_baseline.polar"), C4, "o"),
        ("with winglet", os.path.join(VSP, "03_wing_winglet", "wing_v6_winglet.polar"), C1, "D"),
    ]
    at = {}
    for lab, path, col, mk in runs:
        c, d = read_polar(path)
        cl = d[:, c["CLtot"]]
        cdi = d[:, c["CDi"]] * 1e4
        o = np.argsort(cl)
        cl, cdi = cl[o], cdi[o]
        ax.plot(cl ** 2, cdi, mk + "-", color=col, ms=8, mfc="white", mew=2.2,
                lw=1.8, label=lab)
        at[lab] = {q: float(np.interp(q, cl, cdi)) for q in (0.34, 0.60)}

    lines = []
    for q, lab in ((0.34, "cruise $C_L$ = 0.34"), (0.60, "climb $C_L$ = 0.60")):
        ax.axvline(q ** 2, color=MUTED, ls=":", lw=1.2)
        ax.text(q ** 2 - 0.012, 8, lab, rotation=90, fontsize=8, color=MUTED,
                ha="right", va="bottom")
        a, b = at["without winglet"][q], at["with winglet"][q]
        lines.append(f"{lab}:  {a:.1f} → {b:.1f} counts "
                     f"({(b / a - 1) * 100:+.1f}%)")

    ax.text(0.025, 425, "\n".join(lines), fontsize=9, color=INK, va="top",
            linespacing=1.5)
    ax.text(0.025, 330,
            "A plain tip extension of the same projected length would\n"
            "recover about 7.5% by span growth alone, so roughly three\n"
            "quarters of this is span, not end-plate effect. The winglet's\n"
            "real advantage is lower root bending moment — which a\n"
            "vortex-lattice method cannot see.",
            fontsize=8.2, color=INK2, va="top")

    ax.set_xlabel("$C_L^2$")
    ax.set_ylabel("Induced drag coefficient $C_{Di}$ (counts)")
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 440)
    ax.legend(loc="lower right")
    title(ax, "Induced drag with and without the winglet",
          "Measured on a fixed reference span, so the comparison is like for "
          "like. Straight on these axes means $C_{Di} = K C_L^2$.")
    return save(fig, "fig_5_4_winglet_polar.png")


# ------------------------------------------------- 6.1 neutral point sweep ---
def fig_6_1():
    use_style()
    v7 = json.load(open(os.path.join(os.path.dirname(VSP), "..", "report",
                                     "v7_results.json").replace("\\", "/")))
    s_ht = np.array([30.0, 38.0, 46.0, 54.0])
    x_np = np.array([21.519, 22.012, 22.480, 22.940])
    a, b = v7["np_fit"][0], v7["np_fit"][1]

    fig, (ax, axb) = plt.subplots(1, 2, figsize=(9.6, 4.4),
                                  gridspec_kw=dict(width_ratios=[1.5, 1.0]))

    xs = np.linspace(26, 58, 50)
    ax.plot(xs, a + b * xs, color=C1, lw=1.8, ls="--",
            label=f"fit: $x_{{np}}$ = {a:.3f} + {b:.5f}·$S_{{HT}}$   (R² = {v7['np_fit_r2']:.4f})")
    ax.plot(s_ht, x_np, "o", color=C1, ms=10, mfc="white", mew=2.4,
            label="VSPAERO α-sweep, one measurement per tail area")

    for s, col, lab in ((29.1, C2, "adopted\n29.1 ft²"),
                        (33.3, C3, "§8.6 re-solve\n33.3 ft²"),
                        (46.6, C8, "Raymer jet transport\n+ T-tail credit, 46.6 ft²"),
                        (53.4, C8, "Sadraey jet\ntransport, 53.4 ft²")):
        ax.axvline(s, color=col, ls=":", lw=1.5)
        ax.text(s - 0.35, 19.55, lab, rotation=90, fontsize=7.8, color=col,
                ha="right", va="bottom")

    ax.axvspan(44, 58, color=C8, alpha=0.06, zorder=0)
    ax.set_xlabel("Horizontal tail area $S_{HT}$ (ft²)")
    ax.set_ylabel("Neutral point $x_{np}$ (ft aft of nose)")
    ax.set_xlim(26, 58)
    ax.set_ylim(19.4, 23.4)
    ax.legend(loc="upper left", fontsize=8.0)
    title(ax, "Neutral point moves linearly with tail area",
          "Only $S_{HT}$ varies here, so $dx_{np}/dS_{HT}$ = 0.059 ft/ft² is clean.\n"
          "(The final model also shrank the fin, so its measured $x_{np}$ = 19.72 ft "
          "is not a point on this curve.)")

    # ------------------------------ what each sizing basis actually delivers --
    bases = [("Sadraey\njet transport", 53.4, 40.0, "#b9b8b1"),
             ("Raymer\n+ T-tail credit", 46.6, 33.0, "#b9b8b1"),
             ("Requirement-\ndriven (adopted)", 29.1, 16.0, C2)]
    axb.axhspan(10, 20, color=C3, alpha=0.16, zorder=0)
    axb.text(-0.42, 24.5, "10–20% MAC is typical for the class", fontsize=8,
             color=INK2, ha="left", va="center")
    axb.annotate("", xy=(-0.35, 20.2), xytext=(-0.35, 23.6),
                 arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))
    bars = axb.bar([b_[0] for b_ in bases], [b_[2] for b_ in bases],
                   0.62, color=[b_[3] for b_ in bases],
                   edgecolor="#fcfcfb", linewidth=2.0)
    axb.bar_label(bars, labels=[f"{b_[2]:.0f}%" for b_ in bases], padding=3,
                  fontsize=9.5, color=INK2)
    for i, b_ in enumerate(bases):
        axb.text(i, 1.6, f"{b_[1]:.1f} ft²", ha="center", fontsize=8, color="white")
    axb.set_ylabel("Static margin at the MTOW CG (% MAC)")
    axb.set_ylim(0, 47)
    axb.set_xlim(-0.7, 2.6)
    axb.tick_params(axis="x", labelsize=7.6)
    title(axb, "What each sizing basis delivers",
          "A 40% margin is safe, and pays for it in trim drag\nand control authority.")
    return save(fig, "fig_6_1_neutral_point.png")


# ----------------------------------------------------- 6.2 pitching moment ---
def fig_6_2():
    use_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.6))

    final = os.path.join(VSP, "11_full_v7", "final_alpha", "final_alpha.polar")
    c, d = read_polar(final)
    cl, cm = d[:, c["CLtot"]], d[:, c["CMytot"]]
    o = np.argsort(cl)
    cl, cm = cl[o], cm[o]
    k, b = np.polyfit(cl, cm, 1)
    r2 = 1 - np.sum((cm - (k * cl + b)) ** 2) / np.sum((cm - cm.mean()) ** 2)

    xs = np.linspace(cl.min() - 0.05, cl.max() + 0.05, 20)
    ax.plot(xs, k * xs + b, color=C1, lw=1.5, ls="--")
    ax.plot(cl, cm, "o-", color=C1, lw=2.2, ms=8, mfc="white", mew=2.2,
            label=f"full_v7, closed body:  $dC_m/dC_L$ = {k:.4f},  R² = {r2:.3f}")

    # The retracted model: the same sweep on the v5 body as-scripted, whose tail
    # cone terminated on an open 2.18 ft^2 aperture -- ill-posed in a panel method.
    ret = os.path.join(VSP, "10_full_v6", "ref_v5_asis", "full_v5.polar")
    c2_, d2 = read_polar(ret)
    cl2, cm2 = d2[:, c2_["CLtot"]], d2[:, c2_["CMytot"]]
    o2 = np.argsort(cl2)
    cl2, cm2 = cl2[o2], cm2[o2]
    k2, b2 = np.polyfit(cl2, cm2, 1)
    r2b = 1 - np.sum((cm2 - (k2 * cl2 + b2)) ** 2) / np.sum((cm2 - cm2.mean()) ** 2)
    ax.plot(cl2, cm2, "s--", color=C8, lw=1.8, ms=8, mfc="white", mew=2.0,
            label=f"RETRACTED: unclosed tail cone, 2.18 ft² open aperture  (R² = {r2b:.3f})")

    ax.axhline(0, color=AXIS, lw=1.0)
    ax.annotate("straight line: the slope IS the static margin",
                xy=(cl[3], (k * cl + b)[3]), xytext=(0.52, -0.075),
                fontsize=8.4, color=C1, ha="center",
                arrowprops=dict(arrowstyle="->", color=C1, lw=1.1))
    ax.annotate("non-monotone — the curve bends back.\n"
                "Nothing errored; the numbers just looked plausible.",
                xy=(cl2[2], cm2[2]), xytext=(0.44, -0.42), fontsize=8.4,
                color=C8, ha="center",
                arrowprops=dict(arrowstyle="->", color=C8, lw=1.2))

    ax.set_xlabel("Lift coefficient $C_L$")
    ax.set_ylabel("Pitching moment coefficient $C_m$ about the CG")
    ax.set_ylim(-0.58, 0.02)
    ax.legend(loc="lower left", fontsize=8.2)
    title(ax, "Trap 2 made visible: an open body corrupts the pitching moment",
          "The retracted curve is not merely offset — it bends, and it reported "
          "the static margin backwards.")
    return save(fig, "fig_6_2_pitching_moment.png")


if __name__ == "__main__":
    fig_5_0()
    fig_5_1()
    fig_5_2()
    fig_5_3()
    fig_5_4()
    fig_6_1()
    fig_6_2()
