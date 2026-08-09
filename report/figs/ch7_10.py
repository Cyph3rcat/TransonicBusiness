"""Figures for Chapters 7-10: landing gear, weights and CG, drag, performance; inputs come from the JSON written by the report scripts so figures cannot drift from the text."""
import json
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, Polygon, Patch

from common import (use_style, save, title, fuselage_outline, fairing_outline,
                    wing_planform, REPORT, WING,
                    C1, C2, C3, C4, C5, C6, C7, C8,
                    INK, INK2, MUTED, GRID, AXIS, CRITICAL, WARNING, GOOD, BLUES)


def _json(name):
    with open(os.path.join(REPORT, name)) as f:
        return json.load(f)


# ------------------------------------------------------- 7.1 landing gear ----
def fig_7_1():
    g = _json("landing_gear.json")
    use_style()
    fig, (ax, axf) = plt.subplots(2, 1, figsize=(8.2, 7.4))

    x, hw, hh, zc = fuselage_outline()
    zg = g["z_ground"]
    x_mg, x_ng, Hcg = g["x_mg"], g["x_ng"], g["H_cg"]
    x_cg_aft = 19.449                          # Chapter 8 aft limit
    z_cg = zg + Hcg

    # ------------------------------------------------------ side elevation ---
    ax.fill_between(x, zc - hh, zc + hh, color=GRID, alpha=0.6, zorder=1)
    ax.plot(x, zc + hh, color=INK2, lw=1.3)
    ax.plot(x, zc - hh, color=INK2, lw=1.3)
    fx, fhw, fhh, fz = fairing_outline()
    fbot = fz - fhh
    m = fbot < np.interp(fx, x, zc - hh)
    ax.plot(fx[m], fbot[m], color=MUTED, lw=1.3, ls="--")

    ax.axhline(zg, color=INK2, lw=2.0)
    ax.fill_between([-2, 46], zg, zg - 1.2, color=GRID, alpha=0.9, zorder=0)

    for xw, r, lab in ((x_mg, 0.875, "main"), (x_ng, 0.75, "nose")):
        ax.plot([xw, xw], [zg + r, -2.6], color=INK2, lw=2.6, solid_capstyle="round")
        ax.add_patch(Circle((xw, zg + r), r, facecolor=INK2, edgecolor=INK2, zorder=4))
        ax.add_patch(Circle((xw, zg + r), r * 0.42, facecolor="#fcfcfb", zorder=5))

    ax.plot(x_cg_aft, z_cg, "o", color=C2, ms=11, zorder=6)
    ax.annotate(f"aft CG limit, x = {x_cg_aft:.2f} ft\n"
                f"tipback {g['tipback_deg']:.1f}° (≥ 15° required)",
                xy=(x_cg_aft, z_cg), xytext=(13.0, 5.6), fontsize=8.4, color=C2,
                ha="center", arrowprops=dict(arrowstyle="->", color=C2, lw=1.2))

    # Tipback: main-wheel contact to the aft CG, measured off vertical.
    ax.plot([x_mg, x_cg_aft], [zg, z_cg], color=C2, lw=1.6, ls="--")
    ax.plot([x_mg, x_mg], [zg, z_cg + 1.2], color=MUTED, lw=1.0, ls=":")
    ax.add_patch(Wedge((x_mg, zg), 4.5, 90.0,
                       90.0 + g["tipback_deg"], facecolor=C2, alpha=0.22, zorder=2))

    # Tail strike: rotation about the main-wheel contact point.
    a = np.radians(g["alpha_c_deg"])
    ax.plot([x_mg, x_mg + 21 * np.cos(a)], [zg, zg + 21 * np.sin(a)],
            color=C3, lw=1.6, ls="--")
    ax.add_patch(Wedge((x_mg, zg), 8.0, 0.0, g["alpha_c_deg"],
                       facecolor=C3, alpha=0.18, zorder=2))
    ax.text(x_mg + 8.8, zg + 1.0, f"tail-strike {g['alpha_c_deg']:.1f}°",
            fontsize=8.4, color=C3)

    ax.annotate("", xy=(x_ng, zg - 0.85), xytext=(x_mg, zg - 0.85),
                arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    ax.text((x_ng + x_mg) / 2, zg - 1.15,
            f"wheelbase B = {g['B']:.1f} ft", ha="center", va="top",
            fontsize=8.4, color=INK2)

    ax.set_xlim(-2, 46.5)
    ax.set_ylim(zg - 2.6, 7.6)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_xlabel("Fuselage station x (ft)")
    ax.set_ylabel("z (ft)")
    title(ax, "Side elevation: tipback and tail-strike clearance")

    # ------------------------------------------------------ front elevation --
    p = wing_planform()
    dih = np.radians(WING["dihedral"])
    y_tip = p["y_tip"]
    z_root = WING["z"]
    z_tip = z_root + y_tip * np.tan(dih)
    track = g["track"]

    axf.axhline(zg, color=INK2, lw=2.0)
    axf.fill_between([-25, 25], zg, zg - 1.2, color=GRID, alpha=0.9, zorder=0)
    th = np.linspace(0, 2 * np.pi, 120)
    axf.fill(3.05 * np.cos(th), 3.05 * np.sin(th), color=GRID, alpha=0.7,
             zorder=1)
    axf.plot(3.05 * np.cos(th), 3.05 * np.sin(th), color=INK2, lw=1.3, zorder=2)
    for s in (1, -1):
        axf.plot([0, s * y_tip], [z_root, z_tip], color=INK2, lw=2.2, zorder=3)
        axf.plot([s * track / 2, s * track / 2], [zg + 0.875, -2.6],
                 color=INK2, lw=2.6, zorder=3)
        axf.add_patch(Circle((s * track / 2, zg + 0.875), 0.875,
                             facecolor=INK2, zorder=4))

    # Roll to wing-tip strike, about the outer main wheel contact.
    roll = g["roll_clearance_deg"]
    axf.add_patch(Wedge((track / 2, zg), 7.0, 0.0, roll, facecolor=CRITICAL,
                        alpha=0.28, zorder=2))
    axf.plot([track / 2, y_tip], [zg, z_tip], color=CRITICAL, lw=1.8, ls="--",
             zorder=5)
    axf.annotate(f"roll to wing-tip strike: only {roll:.1f}°\n"
                 "landing attitudes run 10–15°  — FLAGGED (§7.3)",
                 xy=(14.0, zg + 1.85), xytext=(11.0, 5.6), fontsize=8.6,
                 color=CRITICAL, ha="center", weight="bold",
                 arrowprops=dict(arrowstyle="->", color=CRITICAL, lw=1.3))

    axf.add_patch(Wedge((track / 2, zg), 3.2, 0.0, g["phi_ot_deg"],
                        facecolor=C3, alpha=0.20, zorder=1))
    axf.annotate(f"overturn {g['phi_ot_deg']:.1f}° (≥ 25° required,\nso not the "
                 "binding constraint)", xy=(6.0, zg + 1.2), xytext=(-9.0, 5.2),
                 fontsize=8.2, color=C3, ha="center",
                 arrowprops=dict(arrowstyle="->", color=C3, lw=1.1))
    axf.plot([track / 2, track / 2 + 3.0 * np.cos(np.radians(g["phi_ot_deg"]))],
             [zg, zg + 3.0 * np.sin(np.radians(g["phi_ot_deg"]))],
             color=C3, lw=1.5, ls="--", zorder=5)

    axf.annotate("", xy=(-track / 2, zg - 0.85), xytext=(track / 2, zg - 0.85),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    axf.text(0, zg - 1.15, f"track {track:.1f} ft", ha="center", va="top",
             fontsize=8.4, color=INK2)

    axf.set_xlim(-24.2, 24.2)
    axf.set_ylim(zg - 2.6, 7.6)
    axf.set_aspect("equal")
    axf.grid(False)
    axf.set_xlabel("y (ft)")
    title(axf, "Front elevation: the clearance that is thin")

    return save(fig, "fig_7_1_landing_gear.png")


# ------------------------------------------------------- 8.1 CG envelope -----
FWD_SEQ = [("empty", 6879, 41.3), ("+ crew", 7279, 27.9), ("+ nose bag.", 7339, 25.6),
           ("+ fwd pax", 7879, 19.4), ("+ fuel", 10950, 25.2), ("+ aft pax", 11490, 25.7),
           ("+ aft bag.", 11670, 28.1)]
AFT_SEQ = [("empty", 6879, 41.3), ("+ crew", 7279, 27.9), ("+ aft bag.", 7459, 31.7),
           ("+ aft pax", 7999, 31.9), ("+ fuel", 11070, 34.1), ("+ fwd pax", 11610, 29.6),
           ("+ nose bag.", 11670, 28.1)]
NP_PCT = 39.5


def fig_8_1():
    use_style()
    fig, ax = plt.subplots(figsize=(7.6, 5.2))

    ax.axvspan(NP_PCT - 10, NP_PCT, color=CRITICAL, alpha=0.10, zorder=0)
    ax.axvspan(0, NP_PCT - 10, color=GOOD, alpha=0.07, zorder=0)
    ax.axvline(NP_PCT, color=INK2, lw=2.0, zorder=2)
    ax.text(NP_PCT - 0.5, 12250, "neutral point 39.5% MAC", rotation=90,
            fontsize=8.4, color=INK2, ha="right", va="top")
    ax.axvline(NP_PCT - 10, color=CRITICAL, lw=1.6, ls="--", zorder=2)
    ax.text(NP_PCT - 10.5, 12250, "10% static-margin floor", rotation=90,
            fontsize=8.4, color=CRITICAL, ha="right", va="top")

    for seq, col, lab, mk in ((FWD_SEQ, C1, "forward-critical loading sequence", "o"),
                              (AFT_SEQ, C2, "aft-critical loading sequence", "s")):
        w = [s[1] for s in seq]
        p = [s[2] for s in seq]
        ax.plot(p, w, mk + "-", color=col, lw=2.0, ms=6.5, mfc="white", mew=1.8,
                label=lab, zorder=4)

    ax.plot(19.4, 7879, "D", color=C1, ms=12, zorder=6)
    ax.annotate("forward limit\n19.4% MAC, 7,879 lb\nstatic margin 20.1%",
                xy=(19.4, 7879), xytext=(10.6, 9700), fontsize=8.4, color=C1,
                ha="left", arrowprops=dict(arrowstyle="->", color=C1, lw=1.2))
    ax.plot(34.1, 11070, "D", color=C2, ms=12, zorder=6)
    ax.annotate("aft limit\n34.1% MAC, 11,070 lb\nstatic margin 5.3%\n"
                "— BELOW THE FLOOR",
                xy=(34.1, 11070), xytext=(23.6, 9250), fontsize=8.4, color=C2,
                ha="left", weight="bold",
                arrowprops=dict(arrowstyle="->", color=C2, lw=1.4))

    ax.text(29.0, 6480, "static margin ≥ 10%", fontsize=8, color=INK2,
            ha="right")
    ax.text(30.0, 6480, "< 10%", fontsize=8, color=CRITICAL, ha="left")

    ax.axhline(11660, color=MUTED, ls=":", lw=1.2)
    ax.text(10.6, 11760, "MTOW 11,660 lb", fontsize=8, color=MUTED)
    ax.axhline(6879, color=MUTED, ls=":", lw=1.2)
    ax.text(10.6, 6960, "empty 6,879 lb", fontsize=8, color=MUTED)

    ax.set_xlabel("Centre of gravity (% mean aerodynamic chord)")
    ax.set_ylabel("Weight (lb)")
    ax.set_xlim(10, 44)
    ax.set_ylim(6250, 12600)
    ax.legend(loc="upper left", fontsize=8.4)
    title(ax, "Centre-of-gravity envelope from real loading sequences",
          "The four-corner method reported a 1.6% MAC band. Loading the aircraft "
          "in a plausible order gives 14.7%, and the aft end breaks the floor.")
    return save(fig, "fig_8_1_cg_envelope.png")


def fig_8_2():
    w = _json("class2_weights.json")
    use_style()
    groups = sorted(w["groups"], key=lambda g: g["W"])
    names = [g["name"] for g in groups]
    vals = [g["W"] for g in groups]
    mtow = 11660.0

    # Colour encodes group family (the only categorical structure here), not magnitude -- the bar length already says that.
    FAMILY = {
        "Wing": "Structure", "Horizontal tail": "Structure",
        "Vertical tail": "Structure", "Fuselage": "Structure",
        "Main landing gear": "Structure", "Nose landing gear": "Structure",
        "Engines installed": "Propulsion", "Fuel system": "Propulsion",
        "Flight controls": "Systems", "Hydraulics": "Systems",
        "Electrical": "Systems", "Avionics": "Systems",
        "Air cond. + anti-ice": "Systems", "Furnishings": "Interior",
    }
    FAM_COL = {"Structure": C1, "Propulsion": C2, "Systems": C3, "Interior": C4}

    fig, ax = plt.subplots(figsize=(7.8, 5.4))
    cols = [FAM_COL[FAMILY[n]] for n in names]
    b = ax.barh(names, vals, 0.68, color=cols, edgecolor="#fcfcfb", linewidth=2.0)
    handles = []
    for fam, col in FAM_COL.items():
        share = sum(g["W"] for g in groups if FAMILY[g["name"]] == fam)
        pct = share / sum(g["W"] for g in groups) * 100
        handles.append(Patch(facecolor=col,
                             label=f"{fam}  —  {share:,.0f} lb ({pct:.0f}%)"))
    ax.bar_label(b, labels=[f"{v:,.0f} lb   ({v / mtow * 100:.1f}% MTOW)" for v in vals],
                 padding=4, fontsize=8, color=INK2)

    ax.set_xlabel("Group weight (lb)")
    ax.set_xlim(0, 2450)
    ax.grid(axis="y", visible=False)
    ax.legend(handles=handles, loc="lower right",
              bbox_to_anchor=(1.0, 0.30), fontsize=8.2)

    total = w["W_E_classII"]
    ax.text(0.985, 0.03,
            f"Class-II total  {total:,.0f} lb   ({total / mtow * 100:.2f}% MTOW)\n"
            f"Class-I anchor  {w['W_E_classI']:,.0f} lb   (0.5900 × MTOW)\n"
            f"difference  {abs(total - w['W_E_classI']):.1f} lb",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=9,
            color=INK, bbox=dict(boxstyle="round,pad=0.5", facecolor="#f1f0ec",
                                 edgecolor=AXIS, linewidth=0.8))

    title(ax, "Class-II group weight statement (Raymer Eqs. 15.46–15.59)",
          "Installed engines are the single largest item at 14.1% of MTOW, which "
          "is characteristic of this weight class.")
    return save(fig, "fig_8_2_group_weights.png")


# --------------------------------------------------------------- 9. drag -----
DRAG = [  # component, CD0, interference-affected
    ("Main wing", 0.00706, False),
    ("Fuselage", 0.00694, False),
    ("Nacelles", 0.00395, True),
    ("Belly fairing", 0.00223, False),
    ("Vertical tail", 0.00159, False),
    ("Horizontal tail", 0.00133, False),
    ("Pylons", 0.00068, True),
    ("Dorsal fin", 0.00015, False),
    ("Leakage & protuberance (+3%)", 0.00072, False),
]
CD0 = 0.02465
K = 0.03617


def fig_9_1():
    use_style()
    fig, ax = plt.subplots(figsize=(7.8, 4.8))

    geom = [d for d in DRAG if not d[0].startswith("Leakage")]
    subtotal = sum(d[1] for d in geom)
    order = sorted(DRAG, key=lambda d: d[1])
    names = [d[0] for d in order]
    vals = [d[1] * 1e4 for d in order]
    cols = [C2 if d[2] else (MUTED if d[0].startswith("Leakage") else C1)
            for d in order]

    b = ax.barh(names, vals, 0.66, color=cols, edgecolor="#fcfcfb", linewidth=2.0,
                hatch=["//" if d[2] else None for d in order])
    labels = []
    for d in order:
        if d[0].startswith("Leakage"):
            labels.append(f"{d[1]*1e4:.1f} ct")
        else:
            labels.append(f"{d[1]*1e4:.1f} ct   ({d[1] / subtotal * 100:.1f}% of geometry)")
    ax.bar_label(b, labels=labels, padding=4, fontsize=8.2, color=INK2)

    ax.plot([], [], "s", color=C2, ms=10,
            label="carries the OTWEM interference factor Q = 1.30")
    ax.set_xlabel("Parasite drag contribution (counts)")
    ax.set_xlim(0, 112)
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right", fontsize=8.4)

    title(ax, f"Parasite drag buildup: total $C_{{D0}}$ = {CD0:.5f} "
              f"({CD0*1e4:.1f} counts)",
          f"Geometry subtotal {subtotal*1e4:.1f} counts, plus a 3% leakage and "
          "protuberance allowance.\nThe OTWEM penalty is about 10.5 counts — "
          "≈9 on the nacelle, ≈1.5 on the pylon — and it is not recoverable.")
    return save(fig, "fig_9_1_drag_breakdown.png")


CRUISE = [("Start of cruise, FL410", 0.3598, 12.27),
          ("Mid-cruise, FL430", 0.3683, 12.46),
          ("End of cruise, FL450", 0.3750, 12.61)]


def fig_9_2():
    use_style()
    cl = np.linspace(0, 1.2, 300)
    cd = CD0 + K * cl ** 2

    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    ax.fill_between(cd * 1e4, 0, cl, where=cd > 0, color="none")
    ax.plot(np.full_like(cl, CD0) * 1e4, cl, color=MUTED, ls=":", lw=1.6,
            label=f"parasite only, $C_{{D0}}$ = {CD0*1e4:.1f} counts")
    ax.plot(cd * 1e4, cl, color=C1, lw=2.4,
            label=f"$C_D$ = {CD0:.5f} + {K:.5f}·$C_L^2$")
    ax.fill_betweenx(cl, np.full_like(cl, CD0) * 1e4, cd * 1e4, color=C1,
                     alpha=0.10)
    ax.text(430, 0.72, "induced", fontsize=8.6, color=C1)
    ax.text(212, 0.72, "parasite", fontsize=8.6, color=MUTED)

    for (lab, clv, ld), col in zip(CRUISE, (C2, C3, C5)):
        cdv = CD0 + K * clv ** 2
        ax.plot(cdv * 1e4, clv, "o", color=col, ms=9, mfc="white", mew=2.2,
                zorder=5)
    lo, hi = CRUISE[0], CRUISE[-1]
    ax.annotate("the three cruise states\n"
                f"$C_L$ {lo[1]:.3f} → {hi[1]:.3f},  L/D {lo[2]:.2f} → {hi[2]:.2f}",
                xy=(CD0 * 1e4 + K * 0.368 ** 2 * 1e4 + 4, 0.368),
                xytext=(430, 0.30), fontsize=8.4, color=INK2, ha="left",
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))

    cl_ldmax = np.sqrt(CD0 / K)
    cl_range = np.sqrt(CD0 / (3 * K))
    for clv, col, lab in ((cl_ldmax, C7, f"$L/D_{{max}}$ at $C_L$ = {cl_ldmax:.3f}\n"
                                         "— the glider optimum, not this aircraft's"),
                          (cl_range, C4, "jet range optimum, max "
                                         f"$C_L^{{1/2}}/C_D$, at $C_L$ = {cl_range:.3f}")):
        ax.axhline(clv, color=col, ls="--", lw=1.3)
        ax.text(770, clv + 0.025, lab, fontsize=8.2, color=col, ha="right")

    ax.set_xlabel("Drag coefficient $C_D$ (counts)")
    ax.set_ylabel("Lift coefficient $C_L$")
    ax.set_xlim(190, 790)
    ax.set_ylim(0, 1.18)
    ax.legend(loc="lower right", fontsize=8.4)
    title(ax, "Cruise drag polar, measured rather than assumed",
          "Parasite drag from a component buildup on the real outer mould line; "
          "induced drag from the VSPAERO wake integration.")
    return save(fig, "fig_9_2_drag_polar.png")


def fig_9_3():
    use_style()
    cl = np.linspace(0.05, 1.2, 400)
    cd = CD0 + K * cl ** 2
    ld = cl / cd
    rf = np.sqrt(cl) / cd

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.3), sharex=True)

    cl_ldmax = np.sqrt(CD0 / K)
    cl_range = np.sqrt(CD0 / (3 * K))

    for a, y, opt, col, ylab, name in (
            (ax, ld, cl_ldmax, C1, "$L/D$", "$L/D$ — the glider optimum"),
            (ax2, rf, cl_range, C4, "$C_L^{1/2}/C_D$", "$C_L^{1/2}/C_D$ — the jet range optimum")):
        a.plot(cl, y, color=col, lw=2.4)
        a.axvline(opt, color=col, ls="--", lw=1.4)
        yi = np.interp(opt, cl, y)
        a.plot(opt, yi, "o", color=col, ms=9, mfc="white", mew=2.2)
        a.text(opt + 0.04, yi * 0.62, f"optimum at\n$C_L$ = {opt:.3f}",
               fontsize=8.4, color=col)
        for (lab, clv, _), c2 in zip(CRUISE, (C2, C3, C5)):
            a.plot(clv, np.interp(clv, cl, y), "o", color=c2, ms=7, zorder=5)
        a.axvspan(0.355, 0.380, color=C2, alpha=0.16, zorder=0)
        a.set_xlabel("Lift coefficient $C_L$")
        a.set_ylabel(ylab)
        a.set_xlim(0, 1.2)
        a.set_ylim(0, max(y) * 1.18)
        title(a, name)

    ax.annotate("the three cruise states\nsit here, at $C_L$ ≈ 0.36–0.38",
                xy=(0.368, 12.6), xytext=(0.44, 6.4), fontsize=8.4, color=C2,
                ha="left", arrowprops=dict(arrowstyle="->", color=C2, lw=1.1))
    frac = np.interp(0.3598, cl, rf) / rf.max() * 100
    ax2.annotate(f"cruise already sits at {frac:.0f}% of the\njet range optimum — "
                 "there is no\nlarge unused lever here",
                 xy=(0.368, 20.4), xytext=(0.50, 8.0), fontsize=8.4, color=C2,
                 ha="left", arrowprops=dict(arrowstyle="->", color=C2, lw=1.1))

    fig.suptitle("Why the two optima differ, and which one matters",
                 x=0.045, ha="left", fontsize=11, weight="bold", color=INK)
    fig.text(0.045, 0.905,
             "A jet maximises range at maximum $C_L^{1/2}/C_D$, not at $L/D_{max}$. "
             "Judged against the correct optimum, this aircraft is already near it.",
             fontsize=8.6, color=INK2, ha="left")
    return save(fig, "fig_9_3_ld_optima.png", tight_rect=[0, 0, 1, 0.885])


# ------------------------------------------------------- 10. performance -----
CLIMB = [(0, 8338, 2984), (10000, 7208, 2273), (20000, 5592, 1613),
         (30000, 4159, 983), (41000, 2624, 225), (45000, 2074, -78)]


def fig_10_1():
    p = _json("performance.json")
    use_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.8))

    h = np.array([c[0] for c in CLIMB]) / 1000.0
    aeo = np.array([c[1] for c in CLIMB])
    oei = np.array([c[2] for c in CLIMB])

    ax.axhspan(41, 45, color=C1, alpha=0.10, zorder=0)
    ax.text(8900, 43, "FL410–450\ncruise band", fontsize=8.4, color=C1,
            va="center", ha="right")

    ax.plot(aeo, h, "o-", color=C1, lw=2.4, ms=7, mfc="white", mew=2.0,
            label="all engines operating")
    ax.plot(oei, h, "s-", color=C2, lw=2.4, ms=7, mfc="white", mew=2.0,
            label="one engine inoperative")
    ax.axvline(100, color=CRITICAL, ls="--", lw=1.4)
    ax.text(230, 8, "100 fpm service-ceiling criterion", rotation=90,
            fontsize=8, color=CRITICAL, va="bottom")

    ceil = p["oei_ceiling"] / 1000.0
    ax.plot(100, ceil, "*", color=C2, ms=17, zorder=6)
    ax.annotate(f"one-engine-inoperative ceiling {p['oei_ceiling']:,.0f} ft\n"
                "→ an engine failure at FL450 needs a drift-down;\n"
                "at FL410 it does not",
                xy=(180, ceil), xytext=(5000, 35.0), fontsize=8.4, color=C2,
                ha="left", arrowprops=dict(arrowstyle="->", color=C2, lw=1.2))

    ax.set_xlabel("Rate of climb (ft/min)")
    ax.set_ylabel("Pressure altitude (thousands of ft)")
    ax.set_xlim(-500, 10200)
    ax.set_ylim(0, 50)
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.34), fontsize=8.6)
    title(ax, "Rate of climb on a realistic climb schedule",
          "250 KIAS below 10,000 ft, then 300 KEAS, then M0.80. Without that "
          "constraint the model returns speeds no operator would fly.")
    return save(fig, "fig_10_1_climb.png")


def fig_10_2():
    p = _json("performance.json")
    use_style()
    fig, ax = plt.subplots(figsize=(7.4, 4.8))

    pts = p["payload_range"]
    r = [0.0] + [q["range"] for q in pts]
    pl = [pts[0]["payload"]] + [q["payload"] for q in pts]
    ax.plot(r, pl, "-", color=C1, lw=2.6, zorder=4)
    ax.fill_between(r, 0, pl, color=C1, alpha=0.12, zorder=1)

    for q, lab, tx, ty, ha in zip(pts, "ABC",
                                  (1290, 2060, 2130), (1465, 1345, 300),
                                  ("center", "center", "center")):
        ax.plot(q["range"], q["payload"], "o", color=C1, ms=10, mfc="white",
                mew=2.4, zorder=5)
        ax.annotate(f"{lab}  {q['range']:,.0f} nm\n{q['payload']:,.0f} lb payload",
                    xy=(q["range"], q["payload"]), xytext=(tx, ty),
                    fontsize=8.4, color=INK2, ha=ha,
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))

    # What closing the SFC gap would buy: range scales as 1/SFC on Breguet.
    scale = 0.70 / 0.65
    ax.plot([v * scale for v in r], pl, "--", color=C3, lw=2.0, zorder=3,
            label="same aircraft at SFC = 0.65 lb/(lbf·hr)")
    ax.plot(r, pl, "-", color=C1, lw=2.6, zorder=4,
            label="as analysed, SFC = 0.70 lb/(lbf·hr) (assumed)")

    ax.axvline(1750, color=CRITICAL, lw=1.8, ls="--", zorder=6)
    ax.text(1738, 940, "1,750 nm design requirement", rotation=90, fontsize=8.4,
            color=CRITICAL, ha="right", va="bottom")

    ax.annotate("Only 208 lb of payload — barely one passenger —\n"
                "buys 157 nm. That steep A→B trade is what an aircraft\n"
                "whose tanks are nearly full at maximum payload\nlooks like.",
                xy=(1756, 1214), xytext=(120, 480), fontsize=8.4, color=INK2,
                ha="left", arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))

    ax.set_xlabel("Range (nm)")
    ax.set_ylabel("Payload (lb)")
    ax.set_xlim(0, 2320)
    ax.set_ylim(0, 1650)
    ax.legend(loc="lower right", fontsize=8.4)
    title(ax, "Payload–range: the requirement is missed by 4%, and by how much depends on one unknown",
          "Range is inversely proportional to specific fuel consumption, which is "
          "the softest input in the study.")
    return save(fig, "fig_10_2_payload_range.png")


def fig_10_3():
    p = _json("performance.json")
    use_style()
    n_pos, n_neg = p["n_pos"], -1.0
    VA, VC, VD = p["V_A_kt"], p["V_C_kt"], p["V_D_kt"]
    VS1 = 112.7                      # clean stall, EAS, MTOW
    a_slope = 4.316                  # measured C_L_alpha, /rad
    WS = 11660.0 / 193.678

    fig, ax = plt.subplots(figsize=(7.4, 5.0))

    # Manoeuvre envelope: stall parabolas out to V_A, then the load-factor caps.
    v = np.linspace(0, VA, 200)
    ax.plot(v, (v / VS1) ** 2, color=C1, lw=2.2)
    v_neg = np.linspace(0, VS1 * np.sqrt(abs(n_neg)), 200)
    ax.plot(v_neg, -(v_neg / VS1) ** 2, color=C1, lw=2.2)
    ax.plot([VA, VD], [n_pos, n_pos], color=C1, lw=2.2)
    ax.plot([VS1 * np.sqrt(abs(n_neg)), VC], [n_neg, n_neg], color=C1, lw=2.2)
    ax.plot([VC, VD], [n_neg, 0], color=C1, lw=2.2)
    ax.plot([VD, VD], [0, n_pos], color=C1, lw=2.2, label="manoeuvre envelope (FAR 25.333–337)")
    ax.fill_between(v, (v / VS1) ** 2, 0, color=C1, alpha=0.07)
    ax.fill_between([VA, VD], [n_pos, n_pos], 0, color=C1, alpha=0.07)

    # Gust lines: FAR 25.341 sharp-edged gust with the alleviation factor.
    mu_g = 2 * WS / (0.0023769 * 5.0236 * a_slope * 32.174)
    Kg = 0.88 * mu_g / (5.3 + mu_g)
    for Ude, Vg, col, lab in ((56.0, VC, C2, "56 ft/s gust at $V_C$"),
                              (25.0, VD, C7, "25 ft/s gust at $V_D$")):
        dn = Kg * Ude * Vg * a_slope / (498.0 * WS)
        for s in (1, -1):
            ax.plot([0, Vg], [1, 1 + s * dn], color=col, lw=1.6, ls="--",
                    label=lab if s > 0 else None)
        ax.plot(Vg, 1 + dn, "o", color=col, ms=7, mfc="white", mew=2.0)
        ax.text(Vg + 6, 1 + dn, f"+{1 + dn:.2f}", fontsize=8.2, color=col,
                va="center")

    for vx, lab in ((VS1, "$V_{S1}$"), (VA, "$V_A$"), (VC, "$V_C$"), (VD, "$V_D$")):
        ax.axvline(vx, color=MUTED, ls=":", lw=1.0)
        ax.text(vx, 4.28, f"{lab}\n{vx:.0f} kt", ha="center", va="top",
                fontsize=8.2, color=MUTED)

    ax.axhline(n_pos, color=INK2, lw=1.0, ls=":")
    ax.text(6, n_pos + 0.09, f"manoeuvre limit n = +{n_pos:.2f}  — GOVERNS",
            fontsize=8.6, color=INK, weight="bold")
    ax.axhline(0, color=AXIS, lw=1.0)

    ax.set_xlabel("Equivalent airspeed (kt)")
    ax.set_ylabel("Load factor n")
    ax.set_xlim(0, 410)
    ax.set_ylim(-1.7, 4.3)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.70), fontsize=8.4)
    title(ax, "V–n diagram: manoeuvre governs, but only by 7%",
          "For a wing loading of 60.2 lb/ft² that was not a foregone conclusion — "
          "lightly loaded wings are often gust-critical.")
    return save(fig, "fig_10_3_vn_diagram.png")


if __name__ == "__main__":
    fig_7_1()
    fig_8_1()
    fig_8_2()
    fig_9_1()
    fig_9_2()
    fig_9_3()
    fig_10_1()
    fig_10_2()
    fig_10_3()
