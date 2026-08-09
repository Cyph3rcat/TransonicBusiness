"""Figures for Chapters 1-3: market, weights, fuselage."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon

from common import (use_style, save, title, read_wavedrag_area, VSP,
                    fuselage_outline, fairing_outline,
                    C1, C2, C3, C4, C5, C8, INK, INK2, MUTED, GRID, AXIS,
                    CRITICAL, GOOD, BLUES)

# Competitive set. Range and cruise Mach as tabulated in report section 1.3;
# MTOW sets the marker area.
FLEET = [
    # name,                 range nm, Mach,  MTOW lb, colour
    ("HondaJet Elite II",       1547, 0.72, 11100, C3),
    ("Citation CJ4 Gen3",       2165, 0.77, 17110, C4),
    ("Phenom 300E",             2010, 0.80, 18344, C5),
]
DESIGN = ("This design", 1675, 0.80, 11660, C2)
REQUIREMENT = 1750


def fig_1_1():
    use_style()
    fig, ax = plt.subplots(figsize=(7.4, 4.6))

    ax.axvspan(1500, 2200, color=BLUES[0], alpha=0.5, zorder=0)
    ax.text(1850, 0.837, "light-jet segment, 1,500-2,200 nm",
            ha="center", fontsize=8, color=INK2)

    ax.axvline(REQUIREMENT, color=MUTED, ls="--", lw=1.2, zorder=1)
    ax.text(REQUIREMENT - 25, 0.705, "1,750 nm design requirement", rotation=90,
            va="bottom", ha="right", fontsize=8, color=INK2)

    def area(w):
        # Marker AREA linear in MTOW -- the honest encoding for a size channel.
        return w / 11660.0 * 430.0

    for name, rng, mach, mtow, col in FLEET:
        ax.scatter(rng, mach, s=area(mtow), color=col, alpha=0.85,
                   edgecolor="white", linewidth=1.6, zorder=3)
        ax.annotate(f"{name}\n{mtow:,} lb", (rng, mach),
                    textcoords="offset points", xytext=(0, -14 - np.sqrt(area(mtow)) / 2),
                    ha="center", va="top", fontsize=8.2, color=INK2)

    name, rng, mach, mtow, col = DESIGN
    ax.scatter(rng, mach, s=area(mtow) * 0.85, color=col, marker="D", alpha=0.95,
               edgecolor="white", linewidth=1.8, zorder=4)
    ax.annotate(f"{name}\n{mtow:,} lb", (rng, mach),
                textcoords="offset points", xytext=(0, 22),
                ha="center", va="bottom", fontsize=8.6, color=C2, weight="bold")

    ax.set_xlabel("Range (nm)")
    ax.set_ylabel("Cruise Mach number")
    ax.set_xlim(1350, 2350)
    ax.set_ylim(0.695, 0.845)
    title(ax, "The competitive set, and the gap this design targets",
          "Marker area is proportional to MTOW. The gap is the empty upper-left: "
          "Phenom speed at HondaJet weight.")
    return save(fig, "fig_1_1_market.png")


def fig_2_1():
    """MTOW and empty weight against the competitive set.

    Only the quantities §1.3 and §2.4 actually tabulate are plotted. The
    HondaJet empty weight is a published figure that did not enter the sizing
    (§2.4 blends the CJ4 and Phenom ratios only) and is drawn hollow to say so.
    """
    use_style()
    names = ["This design", "HondaJet\nElite II", "Phenom 300E", "Citation CJ4"]
    mtow = [11660, 11100, 18344, 17110]
    empty = [6879, 7203, 10461, 10300]
    sourced = [True, False, True, True]

    x = np.arange(len(names))
    w = 0.34
    fig, ax = plt.subplots(figsize=(7.6, 4.8))

    b1 = ax.bar(x - w / 2, mtow, w * 0.9, label="Maximum takeoff weight",
                color=C1, edgecolor="#fcfcfb", linewidth=2.0)
    ax.bar_label(b1, labels=[f"{v:,.0f}" for v in mtow], padding=3,
                 fontsize=8.2, color=INK2)
    b2 = ax.bar(x + w / 2, empty, w * 0.9, label="Empty weight",
                color=[C2 if s else "none" for s in sourced],
                edgecolor=[("#fcfcfb" if s else C2) for s in sourced],
                linewidth=2.0, hatch=[None, "//", None, None])
    ax.bar_label(b2, labels=[f"{v:,.0f}" for v in empty], padding=3,
                 fontsize=8.2, color=INK2)

    for i, (m_, e_) in enumerate(zip(mtow, empty)):
        ax.text(i, -1250, f"$W_E/W_0$ = {e_ / m_:.2f}", ha="center",
                fontsize=8.4, color=INK2)

    ax.set_xticks(x, names)
    ax.set_ylabel("Weight (lb)")
    ax.set_ylim(0, 20800)
    ax.legend(loc="upper left", ncols=2)
    ax.tick_params(axis="x", pad=22)
    title(ax, "This design sits in the HondaJet weight class, not the CJ4/Phenom class",
          "The CJ4 and Phenom carry the same eight occupants in a far heavier "
          "airframe.\n§2.4 adopted $W_E/W_0$ = 0.59 from the CJ4 and Phenom "
          "ratios, overriding a 0.497 statistical regression; Chapter 8's\n"
          "independent buildup returns 0.5899. Hatched bar: a published figure "
          "that was not an input to the sizing.")
    return save(fig, "fig_2_1_weight_comparison.png")


L_NC = 10.4       # nose-cone length, ft
R_BARREL = 3.05   # barrel radius, ft


def fig_3_1():
    use_style()
    x = np.linspace(0, L_NC, 400)
    xi = x / L_NC
    r_pow = R_BARREL * xi ** 0.6                       # first loft, rejected
    r_sin = R_BARREL * np.sin(0.5 * np.pi * xi ** 0.7)  # adopted
    droop = -0.60 * (1 - xi) ** 2

    fig, (ax, axz) = plt.subplots(1, 2, figsize=(8.6, 4.0),
                                  gridspec_kw=dict(width_ratios=[1.75, 1.0]))
    xb = np.linspace(L_NC, L_NC + 3.4, 30)

    for a in (ax, axz):
        a.plot(x, r_pow, color=C8, lw=1.9, ls="--")
        a.plot(x, -r_pow, color=C8, lw=1.9, ls="--")
        a.plot(x, droop + r_sin, color=C1, lw=2.2)
        a.plot(x, droop - r_sin, color=C1, lw=2.2)
        a.plot(xb, np.full_like(xb, R_BARREL), color=MUTED, lw=1.8)
        a.plot(xb, np.full_like(xb, -R_BARREL), color=MUTED, lw=1.8)
        a.axvline(L_NC, color=AXIS, lw=1.0)
        a.set_aspect("equal")

    ax.plot([], [], color=C8, lw=1.9, ls="--",
            label=r"rejected: $r/R=(x/L_{nc})^{0.6}$")
    ax.plot([], [], color=C1, lw=2.2,
            label=r"adopted: $r/R=\sin[\frac{\pi}{2}(x/L_{nc})^{0.7}]$")
    ax.plot([], [], color=MUTED, lw=1.8, label="constant 6.10 ft barrel")
    ax.plot(x, droop, color=C1, lw=0.9, ls=":", alpha=0.7)
    ax.text(L_NC + 0.15, -4.0, "barrel joint\nx = 10.4 ft", fontsize=8, color=INK2)
    ax.annotate("blunt tip: dr/dx → ∞\nso a radome fits", xy=(0.06, -0.35),
                xytext=(2.4, -2.9), fontsize=8.2, color=C1, ha="center",
                arrowprops=dict(arrowstyle="->", color=C1, lw=1.2))
    ax.set_xlabel("Fuselage station x (ft)")
    ax.set_ylabel("Radius (ft)")
    ax.set_xlim(-0.5, 13.8)
    ax.set_ylim(-4.8, 4.8)
    ax.legend(loc="upper left", fontsize=8.0)
    title(ax, "Nose profile: the continuity fix")

    # ------------------------------------------- zoom on the barrel joint ---
    slope = 0.6 * R_BARREL / L_NC          # dr/dx of the power law at x = L_nc
    ang = np.degrees(np.arctan(slope))
    xt = np.linspace(L_NC - 1.3, L_NC + 1.0, 20)
    axz.plot(xt, R_BARREL + slope * (xt - L_NC), color=C8, lw=1.0, ls=":")
    axz.annotate(f"{ang:.0f}° slope break",
                 xy=(L_NC, R_BARREL), xytext=(L_NC - 1.35, R_BARREL + 0.62),
                 fontsize=8.4, color=C8, ha="center",
                 arrowprops=dict(arrowstyle="->", color=C8, lw=1.2))
    axz.annotate("tangent, $C^1$ continuous",
                 xy=(L_NC - 0.35, R_BARREL - 0.02), xytext=(L_NC - 2.4, R_BARREL - 0.75),
                 fontsize=8.4, color=C1, ha="center",
                 arrowprops=dict(arrowstyle="->", color=C1, lw=1.2))
    axz.set_xlim(L_NC - 2.9, L_NC + 0.9)
    axz.set_ylim(R_BARREL - 1.1, R_BARREL + 0.9)
    axz.set_xlabel("x (ft)")
    axz.set_yticks([2.5, 3.0])
    title(axz, "Zoom: where the nose meets the barrel")
    return save(fig, "fig_3_1_nose_profile.png")


def fig_3_2():
    use_style()
    xw, aw = read_wavedrag_area(f"{VSP}/08_full_v4/wavedrag_full_v3.csv")
    xc, ac = read_wavedrag_area(f"{VSP}/08_full_v4/wavedrag_full_v4.csv")

    # Sears-Haack of the same length and volume as the adopted (constant-barrel)
    # body, i.e. the minimum-wave-drag distribution this body could aim at.
    L = xc[-1] - xc[0]
    V = np.trapezoid(ac, xc)
    t = (xc - xc[0]) / L
    sh = (16.0 * V) / (3.0 * np.pi * L) * (4.0 * t * (1.0 - t)) ** 1.5

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.fill_between(xc, 0, ac, color=C1, alpha=0.10, zorder=1)
    ax.plot(xc, ac, color=C1, lw=2.3, label="constant 6.10 ft barrel (adopted), D/q = 1.49 ft²")
    ax.plot(xw, aw, color=C2, lw=2.0, ls="--", label="waisted barrel, D/q = 1.53 ft²")
    ax.plot(xc, sh, color=MUTED, lw=1.6, ls=":",
            label="Sears–Haack ideal at the same length and volume")

    i = int(np.argmax(ac))
    ax.annotate("crest is made by wing, nacelle\nand belly fairing, not by the barrel",
                xy=(xc[i], ac[i]), xytext=(xc[i] + 1.0, ac[i] + 11),
                fontsize=8.3, color=INK2, ha="left",
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    ax.axvspan(21, 27, color=GRID, alpha=0.6, zorder=0)

    ax.set_xlabel("Fuselage station x (ft)")
    ax.set_ylabel("Cross-sectional area A(x)  (ft²)")
    ax.set_xlim(0, 43)
    ax.set_ylim(0, 74)
    ax.legend(loc="upper left")
    title(ax, "Cross-sectional area distribution: why there is no coke bottle",
          "The un-waisted body is smoother in dA/dx and carries 17% more volume, "
          "even though its peak is higher.")
    return save(fig, "fig_3_2_area_distribution.png")


def fig_3_3():
    """Cabin layout: plan and side elevation on the real full_v7 loft."""
    use_style()
    fig, (axp, axs) = plt.subplots(2, 1, figsize=(8.4, 6.4), sharex=True)

    x, hw, hh, zc = fuselage_outline()
    PBF, PBA = 8.2, 26.5              # pressure bulkheads
    CAB0 = 12.6                       # passenger section start
    pitch, sw, aw = 40 / 12, 25 / 12, 16 / 12
    LAV0 = CAB0 + 3 * pitch

    # ---------------------------------------------------------------- plan ---
    axp.fill_between(x, -hw, hw, color=GRID, alpha=0.55, zorder=1)
    axp.plot(x, hw, color=INK2, lw=1.4, zorder=2)
    axp.plot(x, -hw, color=INK2, lw=1.4, zorder=2)
    axp.axhline(0, color=AXIS, lw=0.8, ls="-.", zorder=2)

    for r in range(3):
        x0 = CAB0 + r * pitch
        for side in (+1, -1):
            y0 = aw / 2 if side > 0 else -(aw / 2) - sw
            axp.add_patch(FancyBboxPatch((x0 + 0.18, y0), pitch - 0.55, sw,
                                         boxstyle="round,pad=0,rounding_size=0.18",
                                         facecolor=C1, alpha=0.8,
                                         edgecolor="white", lw=1.6, zorder=3))
    axp.text(CAB0 + 1.5 * pitch, 0, "aisle 16 in", ha="center", va="center",
             fontsize=7.4, color=INK2, zorder=4)

    axp.add_patch(Rectangle((8.4, -2.0), 3.8, 4.0, facecolor="#c8c7c0",
                            alpha=0.55, edgecolor=INK2, lw=1.0, zorder=2))
    axp.text(10.3, 0, "flight deck\n2 crew", ha="center", va="center",
             fontsize=7.4, color=INK2, zorder=4)
    axp.add_patch(Rectangle((LAV0, -2.9), 3.0, 5.8, facecolor=C3, alpha=0.32,
                            edgecolor=C3, lw=1.3, zorder=2))
    axp.text(LAV0 + 1.5, 0, "enclosed\nlavatory\n3.0 ft", ha="center", va="center",
             fontsize=7.2, color=INK2, zorder=4)
    axp.add_patch(Rectangle((3.7, -1.4), 4.0, 2.8, facecolor=C4, alpha=0.32,
                            edgecolor=C4, lw=1.3, zorder=2))
    axp.text(5.7, 0, "nose bay\n10 ft³", ha="center", va="center",
             fontsize=7.2, color=INK2, zorder=4)
    axp.add_patch(Rectangle((LAV0 + 3.3, -2.6), 4.6, 5.2, facecolor=C4, alpha=0.32,
                            edgecolor=C4, lw=1.3, zorder=2))
    axp.text(LAV0 + 5.6, 0, "aft baggage\n50 ft³", ha="center", va="center",
             fontsize=7.2, color=INK2, zorder=4)

    axp.annotate("", xy=(CAB0, -4.3), xytext=(LAV0 + 3.0, -4.3),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.1))
    axp.text((CAB0 + LAV0 + 3.0) / 2, -4.7,
             "cabin 13.0 ft = 3 rows × 40 in pitch + 3.0 ft lavatory",
             ha="center", va="top", fontsize=8, color=INK2)
    axp.annotate("", xy=(22.4, -3.05), xytext=(22.4, 3.05),
                 arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.1), zorder=5)
    axp.text(22.4, 3.5, "6.10 ft external / 5.50 ft cabin width",
             fontsize=7.8, color=INK2, va="bottom", ha="center")

    axp.set_ylim(-6.4, 5.4)
    axp.set_ylabel("y (ft)")
    axp.set_aspect("equal")
    axp.grid(False)
    axp.set_yticks([-3, 0, 3])
    title(axp, "Cabin layout — plan",
          "Sized inside-out: 2 × 25 in seats + 16 in aisle sets the 5.50 ft cabin width.")

    # ---------------------------------------------------------------- side ---
    axs.fill_between(x, zc - hh, zc + hh, color=GRID, alpha=0.55, zorder=1)
    axs.plot(x, zc + hh, color=INK2, lw=1.4)
    axs.plot(x, zc - hh, color=INK2, lw=1.4)
    fx, fhw, fhh, fz = fairing_outline()
    fbot = fz - fhh
    body_bot = np.interp(fx, x, zc - hh)
    m = fbot < body_bot                       # only where it protrudes below
    axs.plot(fx[m], fbot[m], color=MUTED, lw=1.4, ls="--")
    axs.text(23.5, -4.6, "belly fairing (main gear bay)", fontsize=7.4,
             color=MUTED, ha="center")

    axs.add_patch(Rectangle((CAB0, -2.55), 3 * pitch, 4.55, facecolor=C1,
                            alpha=0.16, edgecolor=C1, lw=1.2, zorder=2))
    for r in range(3):
        x0 = CAB0 + r * pitch + 0.35
        axs.add_patch(Rectangle((x0, -2.55), 1.75, 1.35, facecolor=C1, alpha=0.75,
                                edgecolor="white", lw=1.3, zorder=3))
        axs.add_patch(Rectangle((x0 + 1.40, -2.55), 0.35, 2.55, facecolor=C1,
                                alpha=0.75, edgecolor="white", lw=1.3, zorder=3))
    axs.text(CAB0 + 1.5 * pitch, 2.5, "passenger section", ha="center",
             fontsize=7.8, color=INK2)

    for xs, lab, side in ((PBF, "forward pressure\nbulkhead, x = 8.2", -1),
                          (PBA, "aft pressure\nbulkhead, x = 26.5", 1)):
        i = int(np.argmin(abs(x - xs)))
        axs.plot([xs, xs], [zc[i] - hh[i] + 0.1, zc[i] + hh[i] - 0.1],
                 color=CRITICAL, lw=1.8, ls="--", zorder=4)
        axs.text(xs + 0.4 * side, 3.6, lab, ha="center", va="bottom",
                 fontsize=7.4, color=CRITICAL)

    axs.set_xlim(-1.5, 44.5)
    axs.set_ylim(-6.4, 5.4)
    axs.set_xlabel("Fuselage station x (ft)")
    axs.set_ylabel("z (ft)")
    axs.set_aspect("equal")
    axs.grid(False)
    axs.set_yticks([-3, 0, 3])
    title(axs, "Cabin layout — side elevation",
          "Outline is the as-lofted full_v7 body (7 stations, gen_v7.py), not a sketch.")

    return save(fig, "fig_3_3_cabin_layout.png")


if __name__ == "__main__":
    fig_1_1()
    fig_2_1()
    fig_3_1()
    fig_3_2()
    fig_3_3()
