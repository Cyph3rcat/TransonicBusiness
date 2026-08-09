"""Plots A(x) area distributions from WaveDrag CSVs vs Sears-Haack ideal. Usage: python plot_area_dist.py out.png csv1 [csv2 ...]"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def read_wavedrag_csv(path):
    cdwave = None
    area = None
    length = None
    with open(path) as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "CDWave":
                cdwave = float(parts[1])
            elif parts[0] == "Slice_Area" and area is None:
                area = np.array([float(x) for x in parts[1:]])
            elif parts[0] == "Length" and length is None:
                length = float(parts[1])
    x = np.linspace(0, length, len(area))
    return x, area, cdwave, length


fig, ax = plt.subplots(figsize=(11, 5.5))
for path in sys.argv[2:]:
    x, a, cd, L = read_wavedrag_csv(path)
    name = path.split("\\")[-1].replace("wavedrag_", "").replace(".csv", "")
    ax.plot(x, a, "-o", ms=3, label=f"{name} (CDwave metric {cd:.2f})")
    # Sears-Haack with same volume and length
    vol = np.trapezoid(a, x)
    sh = (16 * vol) / (3 * np.pi * L) * (4 * (x / L) * (1 - x / L)) ** 1.5
    ax.plot(x, sh, "--", alpha=0.6, color=ax.lines[-1].get_color(),
            label=f"Sears-Haack (same V={vol:.0f} ft3)")
ax.set_xlabel("x (ft)")
ax.set_ylabel("cross-section area A(x), ft^2")
ax.set_title("Whole-aircraft area distribution (Mach-1 normal slices) vs Sears-Haack")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig(sys.argv[1], dpi=110)
print("wrote", sys.argv[1])
