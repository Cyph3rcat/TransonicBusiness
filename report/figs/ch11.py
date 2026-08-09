"""Figures for Chapter 11: pricing and economics.

Numeric inputs come from report/economics.json, written by report/economics.py,
so these figures cannot drift from the tables in the text.
"""
import json
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from common import (use_style as _use_style, save, title, REPORT,
                    C1, C2, C3, C4, C5, C6,
                    INK, INK2, MUTED, CRITICAL, GOOD)


# Every label in this chapter is a dollar figure. Mathtext would swallow the
# "$...$" pairs, so parsing is off for the whole module.
def use_style():
    _use_style()
    plt.rcParams["text.parse_math"] = False


def _json(name):
    with open(os.path.join(REPORT, name)) as f:
        return json.load(f)


# ------------------------------------------- 11.1 programme cost buildup ----
def fig_11_1():
    e = _json("economics.json")
    use_style()
    el = e["elements_2012"]
    esc = e["escalation"]
    f = e["f_dapca"]           # the 1.2 x 0.9 adjustment, DAPCA terms only

    # The split that matters is not "which equation" but "did DAPCA estimate
    # this at all" -- the two purchased-equipment terms carry the model's
    # softest assumptions and together are a third of the total. The DAPCA
    # terms are shown post-adjustment so the shares sum to the programme total.
    ITEMS = [
        ("Manufacturing labour", el["manufacturing"] * f, "DAPCA-estimated"),
        ("Engines (Eq. 18.8)", el["engines"], "Purchased equipment"),
        ("Engineering labour", el["engineering"] * f, "DAPCA-estimated"),
        ("Manufacturing materials", el["materials"] * f, "DAPCA-estimated"),
        ("Avionics", el["avionics"], "Purchased equipment"),
        ("Tooling labour", el["tooling"] * f, "DAPCA-estimated"),
        ("Quality control", el["quality"] * f, "DAPCA-estimated"),
        ("Development support", el["dev_support"] * f, "DAPCA-estimated"),
        ("Flight test", el["flight_test"] * f, "DAPCA-estimated"),
        ("Interiors", el["interiors"], "Purchased equipment"),
    ]
    ITEMS.sort(key=lambda r: r[1])
    names = [r[0] for r in ITEMS]
    vals = np.array([r[1] for r in ITEMS]) * esc / 1e6      # 2026 $M
    kinds = [r[2] for r in ITEMS]
    KIND_COL = {"DAPCA-estimated": C1, "Purchased equipment": C2}
    total = e["total_2012"] * esc / 1e6

    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    b = ax.barh(names, vals, 0.68, color=[KIND_COL[k] for k in kinds],
                edgecolor="#fcfcfb", linewidth=2.0)
    ax.bar_label(b, labels=[f"${v:,.0f}M   ({v / total * 100:.1f}%)" for v in vals],
                 padding=4, fontsize=8, color=INK2)

    handles = []
    for kind, col in KIND_COL.items():
        share = sum(v for v, k in zip(vals, kinds) if k == kind)
        handles.append(Patch(
            facecolor=col,
            label=f"{kind}  —  ${share:,.0f}M ({share / total * 100:.0f}%)"))
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.22),
              fontsize=8.4)

    ax.set_xlabel("Programme cost over 200 aircraft (2026 $M)")
    ax.set_xlim(0, max(vals) * 1.42)
    ax.grid(axis="y", visible=False)
    labour = sum(v for v, n in zip(vals, names) if "labour" in n or "Quality" in n)
    purchased = sum(v for v, k in zip(vals, kinds) if k == "Purchased equipment")
    eng_lo = e["tit_sweep"][0]["c_eng_2026"] / 1e6
    eng_hi = e["tit_sweep"][-1]["c_eng_2026"] / 1e6
    ax.text(0.985, 0.03,
            f"Programme total  ${total:,.0f}M over {e['Q_base']} aircraft"
            "\n"
            f"Unit cost  ${e['unit_2026'] / 1e6:.2f}M   "
            f"→  price at ×1.2  ${e['price_dapca_2026'] / 1e6:.2f}M"
            "\n"
            f"Market anchor (§11.4)  ${e['price_market'] / 1e6:.2f}M   "
            f"→  DAPCA is {e['calibration']:.2f}× high",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8.8,
            color=INK, bbox=dict(boxstyle="round,pad=0.5", facecolor="#f1f0ec",
                                 edgecolor="#dedcd4"))
    title(ax, "Where the money goes: DAPCA IV programme cost buildup",
          f"Labour is {labour / total * 100:.0f}% of the total, but the "
          f"{purchased / total * 100:.0f}% that is purchased equipment carries\n"
          f"the softest assumptions — the engine price alone runs from "
          f"${eng_lo:.1f}M to ${eng_hi:.1f}M each" "\n"
          "across the plausible range of an unknown turbine inlet temperature.")
    return save(fig, "fig_11_1_cost_buildup.png")


# ------------------------------------------------ 11.2 price benchmarking ----
def fig_11_2():
    e = _json("economics.json")
    use_style()
    # (name, MTOW, price $M, label offset in points) -- the offsets keep the
    # CJ4 label off the trend line it sits almost exactly on.
    COMP = [("HondaJet Elite II", 11100.0, 5.5, (0, -32)),
            ("Phenom 300E", 18387.0, 10.5, (0, -32)),
            ("Citation CJ4 Gen3", 17110.0, 12.0, (0, 14))]
    mtow = 11660.0
    p_dapca = e["price_dapca_2026"] / 1e6
    p_lo, p_hi = e["price_bench_low"] / 1e6, e["price_bench_high"] / 1e6
    p_mkt = e["price_market"] / 1e6
    per_lb = e["per_lb_mtow"]

    fig, ax = plt.subplots(figsize=(7.8, 5.2))

    # The competitive-set trend line, drawn through the origin at the mean $/lb.
    x = np.linspace(9000, 20000, 50)
    ax.plot(x, per_lb * x / 1e6, "-", lw=1.6, color=MUTED, zorder=1,
            label=f"Competitive-set mean, ${per_lb:,.0f} per lb MTOW")

    for name, w, p, off in COMP:
        ax.plot(w, p, "o", ms=10, color=C1, mec="#fcfcfb", mew=2.0, zorder=3)
        ax.annotate(f"{name}\n${p:.1f}M", (w, p), textcoords="offset points",
                    xytext=off, ha="center", fontsize=8.3, color=INK2,
                    va="bottom" if off[1] > 0 else "top")

    # This design, priced three ways.
    ax.plot(mtow, p_dapca, "D", ms=11, color=CRITICAL, mec="#fcfcfb", mew=2.0,
            zorder=4)
    ax.annotate(f"DAPCA IV as written\n${p_dapca:.1f}M", (mtow, p_dapca),
                textcoords="offset points", xytext=(14, 4), ha="left",
                fontsize=8.6, color=INK, fontweight="bold")

    ax.vlines(mtow, p_lo, p_hi, color=C3, lw=3.0, zorder=2)
    ax.plot([mtow, mtow], [p_lo, p_hi], "o", ms=7, color=C3, mec="#fcfcfb",
            mew=1.8, zorder=3)
    ax.plot(mtow, p_mkt, "s", ms=10, color=C3, mec="#fcfcfb", mew=2.0, zorder=4)
    ax.annotate(f"Market-anchored\n${p_lo:.1f}–{p_hi:.1f}M\n(midpoint ${p_mkt:.1f}M)",
                (mtow, p_mkt), textcoords="offset points", xytext=(14, -6),
                ha="left", va="top", fontsize=8.6, color=INK)

    ax.annotate("", xy=(mtow - 380, p_mkt), xytext=(mtow - 380, p_dapca),
                arrowprops=dict(arrowstyle="<->", color=CRITICAL, lw=1.6))
    ax.text(mtow - 520, 0.5 * (p_mkt + p_dapca), f"{e['calibration']:.2f}×",
            ha="right", va="center", fontsize=10, color=CRITICAL,
            fontweight="bold")

    ax.set_xlabel("Maximum takeoff weight (lb)")
    ax.set_ylabel("Acquisition price (2026 $M)")
    ax.set_xlim(9000, 20000)
    ax.set_ylim(0, 26)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    ax.legend(loc="lower right", fontsize=8.4)
    title(ax, "The model prices this aeroplane out of its own market",
          "DAPCA IV returns $22.2M for an 11,660 lb light jet. The competitive set pays\n"
          "about $589 per pound of MTOW. The gap is the result, not a rounding error —\n"
          "and it is smaller than the ÷4 correction Raymer reports GA users applying.")
    return save(fig, "fig_11_2_price_benchmark.png")


# ------------------------------------ 11.3 operating cost vs. utilisation ----
def fig_11_3():
    e = _json("economics.json")
    use_style()
    rows = e["util_sweep"]
    base = e["doc"]

    # Six consolidated elements. Eight stacked segments would be unreadable and
    # the labour/materials and airframe/engine pairs move together anyway.
    def split(total_row, ref):
        """Scale the reference DOC composition to a row's total, holding the
        variable elements fixed and letting the ownership elements carry the
        utilisation effect."""
        return total_row

    SEGS = [("Fuel", "fuel", C1), ("Crew", "crew", C2),
            ("Maintenance", "maint", C3), ("Ownership", "own", C4),
            ("Insurance", "insurance", C5), ("Fees", "landing", C6)]

    utils = [r["util"] for r in rows]
    xs = np.arange(len(rows))
    # Rebuild each row's composition: variable elements are utilisation-
    # independent, so only the ownership block moves.
    comp = []
    for r in rows:
        own = r["fixed"] - base["insurance"]
        comp.append(dict(fuel=base["fuel"], crew=base["crew"],
                         maint=base["maint_labour"] + base["maint_materials"],
                         own=own, insurance=base["insurance"],
                         landing=r["total"] - (base["fuel"] + base["crew"]
                                               + base["maint_labour"]
                                               + base["maint_materials"] + own
                                               + base["insurance"])))

    fig, ax = plt.subplots(figsize=(7.8, 5.2))
    bottom = np.zeros(len(rows))
    handles = []
    for label, key, col in SEGS:
        vals = np.array([c[key] for c in comp])
        ax.bar(xs, vals, 0.58, bottom=bottom, color=col, edgecolor="#fcfcfb",
               linewidth=2.0)
        # Direct-label only the segments tall enough to hold text; the palette
        # carries a contrast WARN, so labels are the required relief.
        for i, (v, b0) in enumerate(zip(vals, bottom)):
            if v > 190:
                ax.text(xs[i], b0 + v / 2, f"${v:,.0f}", ha="center",
                        va="center", fontsize=8.0, color=INK)
        share = vals[1] / rows[1]["total"] * 100        # at the 500 FH/yr base
        handles.append(Patch(facecolor=col, label=f"{label}  —  {share:.0f}% at 500 h"))
        bottom += vals

    for i, r in enumerate(rows):
        ax.text(xs[i], r["total"] + 90, f"${r['total']:,.0f}/h",
                ha="center", fontsize=9.2, color=INK, fontweight="bold")
        ax.text(xs[i], r["total"] + 300, f"${r['seat_nm']:.2f}/seat-nm",
                ha="center", fontsize=8.2, color=MUTED)

    ax.set_xticks(xs)
    ax.set_xticklabels([f"{u:,.0f}" for u in utils])
    ax.set_xlabel("Annual utilisation (flight hours per year)")
    ax.set_ylabel("Direct operating cost (2026 $ per flight hour)")
    ax.set_ylim(0, max(r["total"] for r in rows) * 1.30)
    ax.grid(axis="x", visible=False)
    ax.legend(handles=handles, loc="upper right", fontsize=8.3, ncol=2)
    own_lo, own_hi = comp[-1]["own"], comp[0]["own"]
    drop = 1 - rows[-1]["total"] / rows[0]["total"]
    title(ax, "Utilisation is the dominant lever, and it moves only one block",
          "Fuel, crew and maintenance are flat per hour. Ownership — depreciation —\n"
          f"falls from ${own_hi:,.0f}/h to ${own_lo:,.0f}/h across the band, and that fall "
          f"is the whole\nof the {drop * 100:.0f}% reduction in cost per hour.")
    return save(fig, "fig_11_3_doc_utilisation.png")


if __name__ == "__main__":
    for f in (fig_11_1, fig_11_2, fig_11_3):
        f()
