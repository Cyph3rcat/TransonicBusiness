"""Fuselage/fairing outline, v3 vs v4, from the OpenVSP loft station tables (diagnostic for the 'plastic surgery' pass). Usage: python plot_outline_v3_v4.py out.png"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- v3 (07_full_v3/build_full_v3.vspscript) ----
x3 = np.array([0.0, 1.0, 2.5, 5.0, 7.5, 10.4, 14.0, 17.0, 20.0, 23.0, 26.0, 29.0, 33.0, 38.0, 42.2])
d3 = np.array([0.0, 1.50, 2.59, 3.93, 5.01, 6.10, 6.10, 6.10, 5.85, 5.50, 5.05, 5.05, 3.90, 2.50, 0.0])
z3 = np.array([-0.85, -0.70, -0.50, -0.25, -0.10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.85, 1.75, 2.40])

# v3 belly fairing: L=10.5 at x=17.5, z=-2.7, no z-ramp
b3x = np.array([0.0, 1.5, 4.5, 8.0, 10.5]) + 17.5
b3w = np.array([0.0, 4.6, 5.8, 5.2, 0.0])
b3h = np.array([0.0, 1.0, 1.3, 1.15, 0.0])
b3z = np.full_like(b3x, -2.7)

# ---- v4 (this directory) ----
x4 = np.array([0.00, 0.55, 1.40, 2.70, 4.30, 6.10, 8.10, 10.40, 14.00,
               18.50, 23.40, 26.50, 29.50, 32.00, 35.00, 38.00, 40.50, 42.20])
d4 = np.array([0.000, 1.216, 2.296, 3.500, 4.569, 5.384, 5.907, 6.100, 6.100,
               6.100, 6.100, 5.780, 5.140, 4.450, 3.500, 2.480, 1.500, 0.000])
z4 = np.array([-0.600, -0.538, -0.449, -0.329, -0.206, -0.103, -0.029, 0.000, 0.000,
               0.000, 0.000, 0.060, 0.260, 0.480, 0.850, 1.290, 1.680, 1.980])

b4x = np.array([0.0, 1.6, 3.6, 6.0, 8.6, 11.0, 13.0, 14.5]) + 16.0
b4w = np.array([0.00, 4.20, 6.30, 7.00, 7.00, 5.90, 3.80, 0.00])
b4h = np.array([0.00, 2.00, 2.90, 3.20, 3.20, 2.80, 1.80, 0.00])
b4z = np.array([0.25, 0.08, 0.00, 0.00, 0.05, 0.30, 0.60, 1.05]) - 2.20

fig, axs = plt.subplots(2, 1, figsize=(14, 9), sharex=True)

for ax, (x, d, z, bx, bw, bh, bz, c, lab) in zip(
    [axs[0], axs[1]],
    [(x3, d3, z3, b3x, b3w, b3h, b3z, "tab:blue", "full_v3"),
     (x4, d4, z4, b4x, b4w, b4h, b4z, "tab:orange", "full_v4")],
):
    ax.plot(x, z + d / 2, "-o", color=c, ms=3, label=f"{lab} fuselage upper")
    ax.plot(x, z - d / 2, "-o", color=c, ms=3, label=f"{lab} fuselage lower")
    ax.plot(x, z, ":", color=c, lw=1, alpha=0.7, label="centreline")
    ax.plot(bx, bz + bh / 2, "--", color="tab:red", lw=1.2)
    ax.plot(bx, bz - bh / 2, "--", color="tab:red", lw=1.6, label="belly fairing (side)")
    ax.plot(x, d / 2, "-", color=c, alpha=0.35, lw=1)
    ax.plot(x, -d / 2, "-", color=c, alpha=0.35, lw=1, label="half-width (plan)")
    ax.plot(bx, bw / 2, "--", color="tab:red", alpha=0.45, lw=1)
    ax.plot(bx, -bw / 2, "--", color="tab:red", alpha=0.45, lw=1)
    ax.axvspan(19.0, 25.9, color="k", alpha=0.05)
    ax.text(22.4, -4.6, "wing root chord", ha="center", fontsize=8, color="0.35")
    ax.axvline(10.4, color="0.7", ls=":", lw=1)
    ax.axvline(23.4, color="0.7", ls=":", lw=1)
    ax.text(16.9, 3.6, "cabin 10.4 - 23.4 ft", ha="center", fontsize=8, color="0.35")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_ylabel("z / y  (ft)")
    ax.legend(fontsize=8, loc="upper right", ncol=2)
    ax.set_title(lab, fontsize=11)

axs[1].set_xlabel("x (ft, nose tip origin)")
fig.suptitle("Fuselage + belly fairing outline: v3 (waisted) vs v4 (constant barrel)", fontsize=13)
plt.tight_layout()
plt.savefig(sys.argv[1], dpi=115)
print("wrote", sys.argv[1])
