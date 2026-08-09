"""Quantify loft ripple: extract the fuselage centerline top/bottom lines from
the OBJ mesh and plot the residual against the analytic design lines.
Ripple = deviation from a smooth curve; faceting = chordal error, always
negative (mesh inside the true surface) and smoothly varying."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

L, D, R = 42.2, 6.10, 3.05
L_nc, X_te, Ztipn, Ztipt = 10.4, 23.4, -1.30, 1.75
P_H, P_Z, S_BLEND = 0.85, 1.6, 0.35
L_t = L - X_te

def top_bot(x):
    x = np.asarray(x, float)
    h = np.where(x <= L_nc, D * np.sin(0.5 * np.pi * (np.clip(x, 0, L_nc) / L_nc) ** P_H), D)
    zc = np.where(x <= L_nc, Ztipn * (1 - np.clip(x, 0, L_nc) / L_nc) ** P_Z, 0.0)
    s = np.clip((x - X_te) / L_t, 0, 1)
    sb = np.clip(s / S_BLEND, 0, 1)
    f = (S_BLEND * (sb**3 - 0.5 * sb**4) + np.where(s > S_BLEND, s - S_BLEND, 0)) / (S_BLEND * 0.5 + 1 - S_BLEND)
    tt = R - (R - Ztipt) * s ** 1.8
    bb = -R + (R + Ztipt) * f
    top = np.where(x <= X_te, zc + h / 2, tt)
    bot = np.where(x <= X_te, zc - h / 2, bb)
    return top, bot

import sys
path = sys.argv[1] if len(sys.argv) > 1 else "body_only.obj"
V = []
with open(path) as fh:
    for line in fh:
        if line.startswith("v "):
            V.append([float(t) for t in line.split()[1:4]])
V = np.asarray(V)
# fuselage centerline points only: |y| tiny and exclude belly fairing verts
# (fairing z < -2.0 in its own band x=16..30.5 near centerline bottom)
sel = np.abs(V[:, 1]) < 1e-3
pts = V[sel]
x, z = pts[:, 0], pts[:, 2]
tt, bb = top_bot(x)
is_top = np.abs(z - tt) < np.abs(z - bb)
# drop fairing points: they sit below the fuselage bottom line
fair = (~is_top) & (x > 15.9) & (x < 30.6) & (z < bb - 0.05)
fig, axs = plt.subplots(2, 1, figsize=(13, 6), sharex=True)
for ax, mask, ref, name in [(axs[0], is_top & ~fair, tt, "top line"),
                            (axs[1], ~is_top & ~fair, bb, "bottom line")]:
    xx, res = x[mask], (z - ref)[mask]
    o = np.argsort(xx)
    ax.plot(xx[o], res[o], ".-", ms=3, lw=0.7)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_ylabel(f"{name}\nmesh - analytic (ft)")
    ax.grid(alpha=0.3)
    rr = res[o]
    d2 = np.diff(rr, 2)
    print(f"{name}: max|res| = {np.abs(res).max():.4f} ft, ripple (max|2nd diff|) = {np.abs(d2).max():.4f} ft")
axs[1].set_xlabel("x (ft)")
plt.tight_layout()
plt.savefig("ripple_metric.png", dpi=115)
print("wrote ripple_metric.png")
