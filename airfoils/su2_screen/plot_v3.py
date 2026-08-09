"""Final v3 results figure: constant-CL drag rise with error bars, M_crit Cp-crossing, and implied sweep, with v1 (retracted) and literature anchors overlaid."""
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from critical_cp import cp_critical

v3 = json.loads((HERE / "mach_sweep_sc20412_v3" / "results_v3.json").read_text())
v1 = json.loads((HERE / "mach_sweep_sc20412" / "results_su2_sweep_sc20412.json").read_text())
pg = json.loads((HERE.parent / "results_critical_mach_pg.json").read_text())["candidates"]["NASA SC(2)-0412"]

machs = [s["mach"] for s in v3["stations"]]
cds = [s["cd"] * 1e4 for s in v3["stations"]]
cd_stds = [s["cd_std"] * 1e4 for s in v3["stations"]]
cp_mins = [s["cp_min"] for s in v3["stations"]]

m_crit = v3["M_crit_CFD"]
m_dd_b = v3["M_dd_boeing"]
m_dd_d = v3["M_dd_delta20"]
m_crit_pg = pg["M_crit_PG"]

M_CRUISE = 0.80
KORN_MDD = 0.95 - 0.12 - 0.248 / 10  # kappa_A=0.95 supercritical, t/c=0.12, cl=0.248
ARXIV_SHOCK_ONSET = 0.78  # Rezaei et al., first upper-surface shock at AoA=0

fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))
fig.suptitle("SC(2)-0412 v3 (JST, cold-start, constant $C_L$=0.248): defensible $M_{crit}$ / $M_{dd}$",
             fontsize=12.5)

ax = axes[0]
ax.errorbar(machs, cds, yerr=cd_stds, fmt="o-", color="#d62728", lw=1.8, ms=5,
            capsize=3, label="v3: $C_D(M)$ at $C_L$=0.248 (±1σ window)")
v1m = [p["mach"] for p in v1["points"]]
v1cd = [p["cd"] * 1e4 for p in v1["points"]]
ax.plot(v1m, v1cd, "x--", color="0.6", lw=1, ms=6, label="v1 (retracted: unconverged)")
ax.axhline(v3["baseline_cd"] * 1e4, color="0.75", ls=":", lw=1)
ax.axhline(v3["baseline_cd"] * 1e4 + 20, color="#9467bd", ls=":", lw=1,
           label="baseline + 20 counts")
ax.axvline(m_dd_b, color="#d62728", ls="--", lw=1.2)
ax.axvline(m_dd_d, color="#9467bd", ls="--", lw=1.2)
ax.annotate(f"$M_{{dd}}$(Boeing)={m_dd_b:.3f}", (m_dd_b, 240), rotation=90,
            fontsize=8, ha="right", color="#d62728")
ax.annotate(f"$M_{{dd}}$(Δ20ct)={m_dd_d:.3f}", (m_dd_d, 240), rotation=90,
            fontsize=8, ha="left", color="#9467bd")
ax.axvline(KORN_MDD, color="#2ca02c", ls="-.", lw=1)
ax.annotate(f"Korn $M_{{dd}}$={KORN_MDD:.3f}", (KORN_MDD, 150), rotation=90,
            fontsize=8, ha="right", color="#2ca02c")
ax.set_xlabel("Freestream Mach")
ax.set_ylabel("$C_D$ (counts)")
ax.set_title("Drag rise at constant $C_L$ — two $M_{dd}$ definitions agree")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
ax.set_ylim(0, 300)

ax = axes[1]
m_dense = np.linspace(0.55, 0.85, 300)
ax.plot(m_dense, cp_critical(m_dense), "k--", lw=1.3, label="$Cp_{cr}(M)$ (sonic)")
ax.plot(machs, cp_mins, "o-", color="#d62728", lw=1.8, ms=5,
        label="v3 CFD $Cp_{min}(M)$ at $C_L$=0.248")
ax.plot(m_dense, -0.5861 / np.sqrt(1 - m_dense**2), color="#ff7f0e", lw=1.3,
        label="Prandtl–Glauert extrapolation")
ax.axvline(m_crit, color="#d62728", ls="--", lw=1.2)
ax.axvline(m_crit_pg, color="#ff7f0e", ls=":", lw=1.2)
ax.annotate(f"CFD $M_{{crit}}$={m_crit:.3f}", (m_crit, -1.55), rotation=90, fontsize=8,
            ha="right", color="#d62728")
ax.annotate(f"PG $M_{{crit}}$={m_crit_pg:.3f}", (m_crit_pg, -1.55), rotation=90, fontsize=8,
            ha="left", color="#ff7f0e")
ax.set_xlabel("Freestream Mach")
ax.set_ylabel("$C_{p,min}$")
ax.set_title("$M_{crit}$: CFD and PG now agree within 0.02")
ax.legend(fontsize=8, loc="upper right")
ax.grid(alpha=0.3)
ax.invert_yaxis()

ax = axes[2]
entries = [
    ("v1 $M_{dd}$=0.712\n(RETRACTED)", np.degrees(np.arccos(0.7122 / M_CRUISE)), "0.7"),
    ("v3 Boeing\n$M_{dd}$=0.777", np.degrees(np.arccos(m_dd_b / M_CRUISE)), "#d62728"),
    ("v3 Δ20ct\n$M_{dd}$=0.784", np.degrees(np.arccos(m_dd_d / M_CRUISE)), "#9467bd"),
    ("Korn\n$M_{dd}$=0.805", 0.0, "#2ca02c"),
]
labels = [e[0] for e in entries]
sweeps = [e[1] for e in entries]
colors = [e[2] for e in entries]
bars = ax.bar(labels, sweeps, color=colors)
for b, s in zip(bars, sweeps):
    ax.text(b.get_x() + b.get_width() / 2, s + 0.4, f"{s:.1f}°", ha="center", fontsize=9)
ax.set_ylabel(r"required $\Lambda_{25}$ = arccos($M_{dd}$/0.80)  (deg)")
ax.set_title("Implied wing sweep — v1's 27.1° was ~2× too much")
ax.set_ylim(0, 32)
ax.grid(alpha=0.3, axis="y")

fig.tight_layout(rect=[0, 0, 1, 0.93])
out = HERE / "sc20412_v3_results.png"
fig.savefig(out, dpi=160)
print(f"Saved: {out}")
