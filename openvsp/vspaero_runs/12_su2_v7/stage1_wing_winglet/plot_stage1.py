"""Stage 1 figures (drag rise, polars, lift curves, CD0/e split) from dragrise_analysis.json + raw history CSVs; deliberately plots the fit residual alongside the results since past M0.80 the polar model (CD=CD0+k*CL^2) stops describing the flow, and showing CD0/e out there without that context would be lying by omission."""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_CL = 0.360
CRUISE_M = 0.80
MDD = 0.809

BLUE, RED, GREY = "#2b6cb0", "#c53030", "#718096"


def load():
    with open(os.path.join(HERE, "dragrise_analysis.json")) as fh:
        return json.load(fh)


def fig_dragrise(rows):
    m = [r["mach"] for r in rows]
    cd = [r["cd_at_target"] * 1e4 for r in rows]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(m, cd, "o-", color=BLUE, lw=2, ms=7, label=f"CD at CL={TARGET_CL}")
    ax.axvline(CRUISE_M, color=GREY, ls="--", lw=1.4)
    ax.axvline(MDD, color=RED, ls=":", lw=1.8)
    ax.annotate(f"cruise\nM{CRUISE_M}", (CRUISE_M, max(cd) * 0.62),
                ha="right", fontsize=9, color=GREY)
    ax.annotate(f"drag divergence\nM{MDD}", (MDD, max(cd) * 0.82),
                ha="left", fontsize=9, color=RED)
    ax.set_xlabel("Mach")
    ax.set_ylabel("CD (counts)")
    ax.set_title("Drag rise at constant cruise lift (wing+winglet, inviscid)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_dragrise.png"), dpi=130)
    plt.close(fig)


def fig_polars(rows):
    fig, ax = plt.subplots(figsize=(8, 5))
    cmap = plt.get_cmap("viridis")
    n = len(rows)
    for i, r in enumerate(rows):
        pts = sorted(r["points"], key=lambda p: p["cl"])
        cl = [p["cl"] for p in pts]
        cd = [p["cd"] * 1e4 for p in pts]
        ax.plot(cd, cl, "o-", color=cmap(i / max(1, n - 1)), ms=5,
                label=f"M{r['mach']:.2f}")
    ax.axhline(TARGET_CL, color=RED, ls="--", lw=1.4)
    ax.annotate(f"cruise CL={TARGET_CL}", (ax.get_xlim()[1] * 0.62, TARGET_CL),
                fontsize=9, color=RED, va="bottom")
    ax.set_xlabel("CD (counts)")
    ax.set_ylabel("CL")
    ax.set_title("Drag polars by Mach -- the spread at fixed CL is the drag rise")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_polars.png"), dpi=130)
    plt.close(fig)


def fig_split(rows):
    m = [r["mach"] for r in rows]
    cd0 = [r["cd0"] * 1e4 for r in rows]
    e = [r["e"] for r in rows]
    res = [r["resid"] * 1e4 for r in rows]

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    a1.plot(m, cd0, "s-", color=BLUE, lw=2, ms=7)
    a1.set_ylabel("CD0 (counts)")
    a1.set_title("Where the drag rise comes from")
    a1.grid(alpha=0.3)
    a1.axvspan(0.805, max(m), color=RED, alpha=0.07)
    a1.annotate("polar fit unreliable here\n(see residual below)",
                (0.822, max(cd0) * 0.55), fontsize=8, color=RED)

    a2.plot(m, e, "o-", color=BLUE, lw=2, ms=7, label="span efficiency e")
    a2.set_ylabel("e")
    a2.set_xlabel("Mach")
    a2.grid(alpha=0.3)
    a2.axvspan(0.805, max(m), color=RED, alpha=0.07)
    a2b = a2.twinx()
    a2b.bar(m, res, width=0.008, color=GREY, alpha=0.5)
    a2b.set_ylabel("polar fit residual (counts)", color=GREY)
    a2.legend(loc="lower left", fontsize=9)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_split.png"), dpi=130)
    plt.close(fig)


def fig_liftcurves(rows):
    fig, ax = plt.subplots(figsize=(8, 5))
    cmap = plt.get_cmap("viridis")
    n = len(rows)
    for i, r in enumerate(rows):
        pts = sorted(r["points"], key=lambda p: p["aoa"])
        ax.plot([p["aoa"] for p in pts], [p["cl"] for p in pts], "o-",
                color=cmap(i / max(1, n - 1)), ms=5, label=f"M{r['mach']:.2f}")
    ax.axhline(TARGET_CL, color=RED, ls="--", lw=1.4)
    ax.set_xlabel("angle of attack (deg)")
    ax.set_ylabel("CL")
    ax.set_title("Lift curves -- steeper with Mach (compressibility)")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_liftcurves.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    rows = load()
    fig_dragrise(rows)
    fig_polars(rows)
    fig_split(rows)
    fig_liftcurves(rows)
    print("wrote fig_dragrise.png fig_polars.png fig_split.png fig_liftcurves.png")
