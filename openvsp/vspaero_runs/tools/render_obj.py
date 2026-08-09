"""Render top/side/front views of an OBJ wireframe. Usage: python render_obj.py file.obj out.png"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

verts = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith("v "):
            verts.append([float(x) for x in line.split()[1:4]])
v = np.array(verts)
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
for a, (i, j, t) in zip(ax, [(0, 1, "top (x-y)"), (0, 2, "side (x-z)"), (1, 2, "front (y-z)")]):
    a.plot(v[:, i], v[:, j], ",", ms=0.5)
    a.set_aspect("equal")
    a.set_title(t)
    a.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(sys.argv[2], dpi=110)
print("wrote", sys.argv[2])
