"""Close-up smoothness check: shaded side/three-quarter views of the nose,
tail cap and belly regions, plus the exact mesh silhouette (y~0 section curve)
so loft ripples show up as wiggles in a line, not just shading."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

path = sys.argv[1] if len(sys.argv) > 1 else "body_only.obj"
out = sys.argv[2] if len(sys.argv) > 2 else "zoom_check.png"

V, F = [], []
with open(path) as f:
    for line in f:
        if line.startswith("v "):
            V.append([float(x) for x in line.split()[1:4]])
        elif line.startswith("f "):
            idx = [int(t.split("/")[0]) - 1 for t in line.split()[1:]]
            for k in range(1, len(idx) - 1):
                F.append([idx[0], idx[k], idx[k + 1]])
V = np.asarray(V); F = np.asarray(F)
tri = V[F]
n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
ln = np.linalg.norm(n, axis=1, keepdims=True)
n = n / np.where(ln == 0, 1, ln)
ctr = tri.mean(axis=1)


def draw(ax, eye, up, xlim, zlim, ttl):
    eye = np.asarray(eye, float); eye /= np.linalg.norm(eye)
    right = np.cross(up, eye); right /= np.linalg.norm(right)
    trueup = np.cross(eye, right)
    depth = ctr @ eye
    order = np.argsort(depth)
    P = np.stack([tri @ right, tri @ trueup], axis=-1)[order]
    lightdir = np.array([0.35, 0.45, 0.82]); lightdir /= np.linalg.norm(lightdir)
    lam = np.abs(n[order] @ lightdir)
    shade = 0.24 + 0.68 * lam
    shade[(n[order] @ eye) < 0] *= 0.55
    cols = np.clip(np.stack([shade * 0.62, shade * 0.72, shade * 0.86], axis=1), 0, 1)
    ax.add_collection(PolyCollection(P, facecolors=cols, edgecolors="none"))
    ax.set_xlim(*xlim); ax.set_ylim(*zlim)
    ax.set_aspect("equal"); ax.set_title(ttl, fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])


# mesh silhouette at |y| < 0.02 (centerline section): top and bottom lines
sel = np.abs(V[:, 1]) < 0.02
pts = V[sel]
fig, axs = plt.subplots(2, 2, figsize=(15, 8), facecolor="white")
draw(axs[0, 0], (0, -1, 0), (0, 0, 1), (-1, 14), (-4.5, 4.0), "nose close-up (side)")
draw(axs[0, 1], (0, -1, 0), (0, 0, 1), (30, 43.5), (-3.5, 4.0), "tail cap close-up (side)")
draw(axs[1, 0], (0, -1, 0), (0, 0, 1), (13, 33), (-5.0, 1.0), "belly fairing close-up (side)")
ax = axs[1, 1]
o = np.argsort(pts[:, 0])
ax.plot(pts[o, 0], pts[o, 2], ".", ms=2)
ax.set_aspect("equal"); ax.grid(alpha=0.3)
ax.set_title("centerline mesh points (ripples show as scatter off a smooth curve)")
plt.tight_layout()
plt.savefig(out, dpi=115)
print("wrote", out)
