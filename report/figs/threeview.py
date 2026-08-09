"""Three-view general arrangement of full_v7.

Every line is computed from the same numbers gen_v7.py feeds to OpenVSP
(fuselage station table, wing/winglet/tail planform drivers, nacelle and pylon
placement), so the drawing and the analysed model cannot diverge.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

from common import (use_style, save, fuselage_outline, fairing_outline,
                    FUSE_L, WING, WINGLET, NACELLE, PYLON, VT, HT, DORSAL,
                    INK, INK2, MUTED, GRID, AXIS, C1, C2)

SKIN = "#dcdbd4"
LINE = "#3d3c39"
ACCENT = C2


def _le_sweep(cr, taper, span, sweep25):
    return np.arctan(np.tan(np.radians(sweep25)) + 0.25 * cr * (1 - taper) / span)


def wing_quad():
    """Plan-view corners of the main wing panel (starboard side)."""
    w = WING
    t25 = np.tan(np.radians(w["sweep25"]))
    x_c4_root = w["x_le"] + 0.25 * w["cr"]
    x_c4_tip = x_c4_root + w["semispan"] * t25
    x_le_tip = x_c4_tip - 0.25 * w["ct"]
    return dict(x_le_r=w["x_le"], x_te_r=w["x_le"] + w["cr"],
                x_le_t=x_le_tip, x_te_t=x_le_tip + w["ct"],
                y_t=w["semispan"])


def winglet_quad(wq):
    """Winglet corners: y and z extents follow from the 70° cant."""
    g = WINGLET
    cant = np.radians(g["cant"])
    dy, dz = g["span"] * np.cos(cant), g["span"] * np.sin(cant)
    t25 = np.tan(np.radians(g["sweep25"]))
    cr = WING["ct"]
    x_c4_r = wq["x_le_t"] + 0.25 * cr
    x_c4_t = x_c4_r + g["span"] * t25
    x_le_t = x_c4_t - 0.25 * g["ct"]
    return dict(x_le_r=wq["x_le_t"], x_te_r=wq["x_le_t"] + cr,
                x_le_t=x_le_t, x_te_t=x_le_t + g["ct"], dy=dy, dz=dz)


def vt_geom():
    le = _le_sweep(VT["cr"], VT["ct"] / VT["cr"], VT["span"], VT["sweep25"])
    x_tip_le = VT["x_root_le"] + VT["span"] * np.tan(le)
    return dict(x_r=VT["x_root_le"], z_r=VT["z_root"],
                x_t=x_tip_le, z_t=VT["z_root"] + VT["span"],
                cr=VT["cr"], ct=VT["ct"])


def ht_quad(v):
    le = _le_sweep(HT["cr"], HT["ct"] / HT["cr"], HT["span"] / 2, HT["sweep25"])
    x_le_t = v["x_t"] + (HT["span"] / 2) * np.tan(le)
    return dict(x_le_r=v["x_t"], x_te_r=v["x_t"] + HT["cr"],
                x_le_t=x_le_t, x_te_t=x_le_t + HT["ct"],
                y_t=HT["span"] / 2, z=v["z_t"])


def _nacelle_profile():
    s = np.array(NACELLE["stations"])
    from scipy.interpolate import PchipInterpolator
    xl = np.linspace(0, NACELLE["length"], 120)
    d = PchipInterpolator(s[:, 0], s[:, 1])(xl)
    return NACELLE["x"] + xl, d / 2.0


def three_view():
    use_style()
    fig, axes = plt.subplots(3, 1, figsize=(8.4, 10.4))
    axp, axs, axf = axes

    x, hw, hh, zc = fuselage_outline()
    fx, fhw, fhh, fz = fairing_outline()
    wq = wing_quad()
    gq = winglet_quad(wq)
    v = vt_geom()
    hq = ht_quad(v)
    nx, nr = _nacelle_profile()
    z_ground = -4.80

    def poly(ax, pts, fc=SKIN, ec=LINE, lw=1.3, z=3, alpha=1.0):
        ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor=ec,
                             linewidth=lw, zorder=z, alpha=alpha))

    # ================================================================= PLAN ==
    axp.fill_between(x, -hw, hw, color=SKIN, edgecolor=LINE, linewidth=1.3,
                     zorder=3)
    axp.fill_between(fx, -fhw, fhw, color=SKIN, edgecolor=MUTED, linewidth=0.9,
                     linestyle="--", zorder=2)

    for s in (1, -1):
        poly(axp, [(wq["x_le_r"], 0), (wq["x_le_t"], s * wq["y_t"]),
                   (wq["x_te_t"], s * wq["y_t"]), (wq["x_te_r"], 0)], z=2)
        poly(axp, [(gq["x_le_r"], s * wq["y_t"]),
                   (gq["x_le_t"], s * (wq["y_t"] + gq["dy"])),
                   (gq["x_te_t"], s * (wq["y_t"] + gq["dy"])),
                   (gq["x_te_r"], s * wq["y_t"])], fc="#c9c8c0", z=4)
        poly(axp, [(hq["x_le_r"], 0), (hq["x_le_t"], s * hq["y_t"]),
                   (hq["x_te_t"], s * hq["y_t"]), (hq["x_te_r"], 0)],
             fc="#cfcec6", z=4)
        axp.fill_between(nx, s * NACELLE["y"] - nr, s * NACELLE["y"] + nr,
                         color="#c2c1b9", edgecolor=LINE, linewidth=1.1, zorder=5)
        axp.plot([PYLON["x"], PYLON["x"] + PYLON["cr"]],
                 [s * PYLON["y"]] * 2, color=LINE, lw=2.0, zorder=4)
    axp.plot([v["x_r"], v["x_t"] + v["ct"]], [0, 0], color=LINE, lw=2.2, zorder=6)

    axp.annotate("", xy=(46.5, -(wq["y_t"] + gq["dy"])),
                 xytext=(46.5, wq["y_t"] + gq["dy"]),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    axp.text(47.2, 0, f"span\n{2 * (wq['y_t'] + gq['dy']):.1f} ft\n"
                      "tip to tip\n(41.53 ft\nreference)", fontsize=8.2,
             color=INK2, va="center")
    axp.annotate("nacelle at 33% semispan,\ninlet over ~75% local chord",
                 xy=(NACELLE["x"] + 3.0, -NACELLE["y"]), xytext=(1.0, -19.5),
                 fontsize=8.4, color=ACCENT,
                 arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2))
    axp.set_ylim(-25, 25)

    # ================================================================= SIDE ==
    axs.fill_between(x, zc - hh, zc + hh, color=SKIN, edgecolor=LINE,
                     linewidth=1.3, zorder=3)
    fbot, ftop = fz - fhh, fz + fhh
    m = fbot < np.interp(fx, x, zc - hh)
    axs.fill_between(fx[m], fbot[m], np.interp(fx[m], x, zc - hh),
                     color=SKIN, edgecolor=LINE, linewidth=1.1, zorder=2)

    # In side view the wing reads as its root-chord silhouette; the swept tip
    # chord is shown as a faint outline behind it rather than as a filled wedge,
    # which is how a general-arrangement drawing conventionally handles sweep.
    zw = WING["z"]
    z_tip_side = zw + wq["y_t"] * np.tan(np.radians(WING["dihedral"]))
    axs.plot([wq["x_le_t"], wq["x_te_t"]], [z_tip_side, z_tip_side],
             color=MUTED, lw=1.6, ls="--", zorder=3)
    xs_c = np.linspace(0, 1, 60)
    tc = 0.12 * WING["cr"]
    axs.fill(wq["x_le_r"] + xs_c * WING["cr"],
             zw + tc * 0.5 * np.sin(np.pi * xs_c ** 0.85),
             facecolor="#c9c8c0", edgecolor=LINE, lw=1.2, zorder=4)
    axs.fill(wq["x_le_r"] + xs_c * WING["cr"],
             zw - tc * 0.32 * np.sin(np.pi * xs_c ** 0.7),
             facecolor="#c9c8c0", edgecolor=LINE, lw=1.2, zorder=4)
    poly(axs, [(v["x_r"], v["z_r"]), (v["x_t"], v["z_t"]),
               (v["x_t"] + v["ct"], v["z_t"]), (v["x_r"] + v["cr"], v["z_r"])],
         fc="#cfcec6", z=4)
    poly(axs, [(DORSAL["x"], DORSAL["z"]),
               (DORSAL["x"] + DORSAL["span"] / np.tan(np.radians(90 - DORSAL["sweepLE"])), DORSAL["z"] + DORSAL["span"]),
               (DORSAL["x"] + DORSAL["cr"], DORSAL["z"] + DORSAL["span"]),
               (DORSAL["x"] + DORSAL["cr"], DORSAL["z"])], fc="#d6d5cd", z=3)
    axs.plot([hq["x_le_r"], hq["x_te_r"]], [hq["z"], hq["z"]], color=LINE,
             lw=3.0, zorder=6, solid_capstyle="butt")
    poly(axs, [(PYLON["x"], PYLON["z"]),
               (PYLON["x"] + PYLON["span"] * np.tan(np.radians(PYLON["sweepLE"])), PYLON["z"] + PYLON["span"]),
               (PYLON["x"] + PYLON["span"] * np.tan(np.radians(PYLON["sweepLE"])) + PYLON["ct"], PYLON["z"] + PYLON["span"]),
               (PYLON["x"] + PYLON["cr"], PYLON["z"])], fc="#c2c1b9", z=5)
    axs.fill_between(nx, NACELLE["z"] - nr, NACELLE["z"] + nr, color="#b8b7af",
                     edgecolor=LINE, linewidth=1.1, zorder=6)

    axs.axhline(z_ground, color=INK2, lw=1.6)
    for xw, r in ((21.0, 0.875), (6.5, 0.75)):
        axs.plot([xw, xw], [z_ground + r, -2.6], color=LINE, lw=2.4, zorder=5)
        axs.add_patch(Circle((xw, z_ground + r), r, facecolor=LINE, zorder=6))

    axs.annotate("", xy=(0, z_ground - 1.1), xytext=(FUSE_L, z_ground - 1.1),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    axs.text(FUSE_L / 2, z_ground - 1.5, f"length {FUSE_L:.1f} ft", ha="center",
             va="top", fontsize=8.4, color=INK2)
    axs.annotate("", xy=(45.6, z_ground), xytext=(45.6, v["z_t"]),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    axs.text(46.2, (z_ground + v["z_t"]) / 2, f"height\n{v['z_t'] - z_ground:.1f} ft",
             fontsize=8.4, color=INK2, va="center")
    axs.annotate("over-the-wing nacelle:\n1.37 ft gap = 0.47 nacelle diameters",
                 xy=(NACELLE["x"] + 2.4, NACELLE["z"] - 1.45),
                 xytext=(4.0, 7.4), fontsize=8.4, color=ACCENT,
                 arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.3))
    axs.set_ylim(-7.6, 11.0)

    # ================================================================ FRONT ==
    th = np.linspace(0, 2 * np.pi, 200)
    dih = np.radians(WING["dihedral"])
    z_tip = zw + wq["y_t"] * np.tan(dih)
    for s in (1, -1):
        poly(axf, [(0, zw - 0.25), (s * wq["y_t"], z_tip - 0.10),
                   (s * wq["y_t"], z_tip + 0.10), (0, zw + 0.45)], fc="#c9c8c0", z=3)
        poly(axf, [(s * wq["y_t"], z_tip - 0.10),
                   (s * (wq["y_t"] + gq["dy"]), z_tip + gq["dz"]),
                   (s * (wq["y_t"] + gq["dy"]) - s * 0.10, z_tip + gq["dz"]),
                   (s * wq["y_t"], z_tip + 0.30)], fc="#b8b7af", z=4)
        axf.add_patch(Circle((s * NACELLE["y"], NACELLE["z"]), 1.45,
                             facecolor="#c2c1b9", edgecolor=LINE, lw=1.2, zorder=5))
        axf.plot([s * NACELLE["y"]] * 2, [PYLON["z"], NACELLE["z"]], color=LINE,
                 lw=2.6, zorder=4)
        axf.plot([s * 4.0, s * 4.0], [z_ground + 0.875, -2.6], color=LINE,
                 lw=2.4, zorder=4)
        axf.add_patch(Circle((s * 4.0, z_ground + 0.875), 0.875, facecolor=LINE,
                             zorder=5))
    axf.fill(3.05 * np.cos(th), 3.05 * np.sin(th), facecolor=SKIN,
             edgecolor=LINE, linewidth=1.3, zorder=3)
    axf.plot([0, 0], [v["z_r"], v["z_t"]], color=LINE, lw=3.0, zorder=4)
    axf.plot([-hq["y_t"], hq["y_t"]], [hq["z"], hq["z"]], color=LINE, lw=3.4,
             zorder=5, solid_capstyle="round")
    axf.axhline(z_ground, color=INK2, lw=1.6)
    axf.annotate("", xy=(-4.0, z_ground - 1.1), xytext=(4.0, z_ground - 1.1),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.2))
    axf.text(0, z_ground - 1.5, "track 8.0 ft", ha="center", va="top",
             fontsize=8.4, color=INK2)
    axf.text(-24, 8.4, "T-tail on the fin tip,\nclear of the wing wake",
             fontsize=8.4, color=INK2)
    axf.set_ylim(-7.6, 11.0)

    for ax, lab, xr in ((axp, "PLAN", (-3, 54)), (axs, "SIDE", (-3, 54)),
                        (axf, "FRONT", (-28.5, 28.5))):
        ax.set_xlim(*xr)
        ax.set_aspect("equal")
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.text(0.0, 0.99, lab, transform=ax.transAxes, fontsize=9.5,
                weight="bold", color=MUTED, va="top", ha="left")

    fig.suptitle("General arrangement — configuration full_v7", x=0.06,
                 ha="left", fontsize=13, weight="bold", color=INK)
    fig.text(0.06, 0.955,
             "Mach 0.80 light business jet, over-the-wing engine mount.  "
             "MTOW 11,660 lb · wing 193.7 ft² · AR 8.91 · Λ₂₅ 18.5° · "
             "NASA SC(2)-0412\n"
             "Drawn from the geometry drivers in gen_v7.py — the same numbers "
             "OpenVSP lofted and VSPAERO solved.",
             fontsize=8.8, color=INK2, ha="left", va="top")
    return save(fig, "fig_0_0_three_view.png", tight_rect=[0, 0, 1, 0.945])


if __name__ == "__main__":
    three_view()
