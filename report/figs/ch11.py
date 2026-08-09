"""Figure for Chapter 11: pricing and economics, built from report/economics.json so it cannot drift from the tables in the text."""
import json
import os

import numpy as np
import matplotlib.pyplot as plt

from common import (use_style as _use_style, save, title, REPORT,
                    C1, C3,
                    INK, INK2, MUTED, CRITICAL, GOOD)


# Every label here is a dollar figure; mathtext would swallow the "$...$" pairs, so parsing is off for the whole module.
def use_style():
    _use_style()
    plt.rcParams["text.parse_math"] = False


def _json(name):
    with open(os.path.join(REPORT, name)) as f:
        return json.load(f)


# ------------------------------------------------ 11.1 price benchmarking ----
def fig_11_1():
    e = _json("economics.json")
    use_style()
    # (name, MTOW, price $M, label offset in points) -- offsets keep the CJ4 label off the trend line it sits almost on.
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
    return save(fig, "fig_11_1_price_benchmark.png")


if __name__ == "__main__":
    fig_11_1()
