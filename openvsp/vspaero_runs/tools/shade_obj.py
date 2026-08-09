"""Painter's-algorithm shaded render of an OBJ, for eyeballing outer mould line. Usage: python shade_obj.py model.obj out.png [title]. Draws 4 views (side, top, front, 3/4) as depth-sorted Lambert-shaded polygons -- silhouette quality matters more than realism, since this is for judging whether the loft "looks right", which a point cloud can't show."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

path, out = sys.argv[1], sys.argv[2]
title = sys.argv[3] if len(sys.argv) > 3 else path

V, F = [], []
with open(path) as f:
    for line in f:
        if line.startswith("v "):
            V.append([float(x) for x in line.split()[1:4]])
        elif line.startswith("f "):
            idx = [int(t.split("/")[0]) - 1 for t in line.split()[1:]]
            for k in range(1, len(idx) - 1):          # fan-triangulate
                F.append([idx[0], idx[k], idx[k + 1]])
V = np.asarray(V)
F = np.asarray(F)
print(f"{len(V)} verts, {len(F)} tris")

tri = V[F]                                            # (n,3,3)
n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
ln = np.linalg.norm(n, axis=1, keepdims=True)
n = n / np.where(ln == 0, 1, ln)
ctr = tri.mean(axis=1)


def draw(ax, eye, up, ttl):
    eye = np.asarray(eye, float)
    eye /= np.linalg.norm(eye)
    right = np.cross(up, eye)
    right /= np.linalg.norm(right)
    trueup = np.cross(eye, right)

    depth = ctr @ eye
    order = np.argsort(depth)                         # far -> near
    P = np.stack([tri @ right, tri @ trueup], axis=-1)[order]

    facing = n[order] @ eye
    lightdir = np.array([0.35, 0.45, 0.82])
    lightdir /= np.linalg.norm(lightdir)
    lam = np.abs(n[order] @ lightdir)
    shade = 0.24 + 0.68 * lam
    shade[facing < 0] *= 0.55                          # back faces darker
    cols = np.stack([shade * 0.62, shade * 0.72, shade * 0.86], axis=1)
    cols = np.clip(cols, 0, 1)

    ax.add_collection(PolyCollection(P, facecolors=cols, edgecolors="none"))
    ax.set_xlim(P[..., 0].min() - 1, P[..., 0].max() + 1)
    ax.set_ylim(P[..., 1].min() - 1, P[..., 1].max() + 1)
    ax.set_aspect("equal")
    ax.set_title(ttl, fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


fig, axs = plt.subplots(2, 2, figsize=(15, 9), facecolor="white")
draw(axs[0, 0], (0, -1, 0), (0, 0, 1), "side (looking from -Y)")
draw(axs[0, 1], (0, 0, 1), (1, 0, 0), "top")
draw(axs[1, 0], (-1, 0, 0), (0, 0, 1), "front")
draw(axs[1, 1], (-0.62, -0.66, 0.42), (0, 0, 1), "three-quarter")
fig.suptitle(title, fontsize=13)
plt.tight_layout()
plt.savefig(out, dpi=115)
print("wrote", out)
