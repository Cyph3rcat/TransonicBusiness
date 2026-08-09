"""v1 (cold-start) vs v2 (reconverged, RESTART_SOL-chained) comparison for the SC(2)-0412 sweep -- v2 didn't fix v1's noisy Cd(M); instead CL drifted monotonically 0.207->0.033 across the sweep, isolating RESTART_SOL chaining as the cause since everything else (mesh, AoA formula, Re schedule) was unchanged."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent

v1_results = json.loads((HERE / "mach_sweep_sc20412" / "results_su2_sweep_sc20412.json").read_text())
v1_points = json.loads((HERE / "mach_sweep_sc20412" / "adaptive_sweep_results.json").read_text())
v2_results = json.loads((HERE / "mach_sweep_sc20412_v2" / "results_su2_sweep_sc20412_v2.json").read_text())
v2_points = json.loads((HERE / "mach_sweep_sc20412_v2" / "adaptive_sweep_results_v2.json").read_text())

m1 = [p["mach"] for p in v1_points]
cl1 = [p["cl"] for p in v1_points]
cd1 = [p["cd"] * 1e4 for p in v1_points]
cp1 = [p["cp_min"] for p in v1_results["points"]]

m2 = [p["mach"] for p in v2_points]
cl2 = [p["cl"] for p in v2_points]
cd2 = [p["cd"] * 1e4 for p in v2_points]
cp2 = [p["cp_min"] for p in v2_results["points"]]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("SC(2)-0412: v1 (independent cold-start) vs v2 (reconverged, warm-start chained)", fontsize=12)

ax = axes[0]
ax.plot(m1, cl1, "o-", color="#1f77b4", label="v1 (cold-start each point)")
ax.plot(m2, cl2, "s-", color="#d62728", label="v2 (warm-start chained)")
ax.axhline(0.248, color="0.5", ls="--", lw=1, label="C_L target (0.248)")
ax.set_xlabel("Freestream Mach")
ax.set_ylabel("$C_L$ achieved")
ax.set_title("$C_L$ drift: v2 falls away from target, v1 doesn't")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(m1, cd1, "o-", color="#1f77b4", label="v1")
ax.plot(m2, cd2, "s-", color="#d62728", label="v2")
ax.set_xlabel("Freestream Mach")
ax.set_ylabel("$C_D$ (counts)")
ax.set_title("$C_D(M)$: v2 is flatter, but at a collapsing $C_L$")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

ax = axes[2]
ax.plot(m1, cp1, "o-", color="#1f77b4", label="v1")
ax.plot(m2, cp2, "s-", color="#d62728", label="v2")
m_dense = np.linspace(0.55, 0.8, 200)
from pathlib import Path as _P
import sys
sys.path.insert(0, str(HERE.parent))
from critical_cp import cp_critical
ax.plot(m_dense, cp_critical(m_dense), "k--", lw=1, label=r"$Cp_{cr}(M)$")
ax.set_xlabel("Freestream Mach")
ax.set_ylabel("$C_{p,min}$")
ax.set_title("$C_{p,min}(M)$: v2's weaker suction shifts $M_{crit}$ later")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
ax.invert_yaxis()

fig.tight_layout(rect=[0, 0, 1, 0.94])
out = HERE / "sc20412_v1_vs_v2.png"
fig.savefig(out, dpi=160)
print(f"Saved: {out}")

print("\n--- Summary ---")
print(f"v1: M_crit={v1_results['M_crit_CFD']:.3f}  M_dd(raw)={v1_results['M_dd_CFD']}")
print(f"v2: M_crit={v2_results['M_crit_CFD']:.3f}  M_dd(raw)={v2_results['M_dd_CFD_raw']}  M_dd(cubic fit)={v2_results['M_dd_CFD_fit']}")
print(f"v1 CL range: {min(cl1):.3f}-{max(cl1):.3f}   v2 CL range: {min(cl2):.3f}-{max(cl2):.3f} (target 0.248)")
