"""
Simple single-panel view: how CD changes with freestream Mach for SC(2)-0412,
straight from the SU2 adaptive Mach sweep (7 points, M=0.5922-0.7722).

Reads airfoils/su2_screen/mach_sweep_sc20412/results_su2_sweep_sc20412.json --
no new analysis, just a plainer version of the drag-rise panel from
plot_sc20412_results.py.

Run: python plot_cd_vs_mach.py
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
SWEEP_DIR = HERE / "su2_screen" / "mach_sweep_sc20412"


def main():
    su2 = json.loads((SWEEP_DIR / "results_su2_sweep_sc20412.json").read_text())
    machs = [p["mach"] for p in su2["points"]]
    cds_counts = [p["cd"] * 1e4 for p in su2["points"]]

    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.plot(machs, cds_counts, "o-", color="#d62728", lw=2, ms=7)
    for m, cd in zip(machs, cds_counts):
        ax.annotate(f"{cd:.0f}", (m, cd), xytext=(0, 8), textcoords="offset points",
                     ha="center", fontsize=9)

    ax.set_xlabel("Freestream Mach")
    ax.set_ylabel(r"$C_D$ (counts, $C_D \times 10^4$)")
    ax.set_title("SC(2)-0412: Drag vs Mach (SU2 CFD, 2D section, unswept)")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    out_path = HERE / "sc20412_cd_vs_mach.png"
    fig.savefig(out_path, dpi=160)
    print(f"Saved: {out_path}")
    plt.show()


if __name__ == "__main__":
    main()
