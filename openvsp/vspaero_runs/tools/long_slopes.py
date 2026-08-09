"""CL_alpha, dCM/dCL, static margin and neutral point from a real alpha sweep.

Usage: python long_slopes.py xcg cref label1=path1.polar [label2=...]

Preferred over VSPAERO's -stab 0.01-deg finite difference, which for this model
differences moment coefficients at the 1e-4 level - the same order as the
solve's own residual noise.
"""
import sys
import numpy as np


def read_polar(path):
    hdr, rows = None, []
    for line in open(path):
        s = line.strip()
        if not s or s.startswith(("Surface", "Surf-")):
            continue
        if s.startswith("Beta "):
            hdr = s.split()
            continue
        rows.append([float(x) for x in s.split()])
    return hdr, np.array(rows)


xcg, cref = float(sys.argv[1]), float(sys.argv[2])
print(f"{'model':10s} {'CL_a 1/rad':>11s} {'CM_a 1/rad':>11s} {'dCM/dCL':>9s} "
      f"{'SM %':>7s} {'x_np ft':>9s} {'CL@a=3.7':>9s} {'L/D@CL0.35':>11s}")
for arg in sys.argv[3:]:
    label, path = arg.split("=", 1)
    hdr, d = read_polar(path)
    c = {n: i for i, n in enumerate(hdr)}
    a = np.deg2rad(d[:, c["AoA"]])
    cl, cm, cd = d[:, c["CLtot"]], d[:, c["CMytot"]], d[:, c["CDtot"]]
    cla = np.polyfit(a, cl, 1)[0]
    cma = np.polyfit(a, cm, 1)[0]
    dcmdcl = cma / cla
    sm = -dcmdcl
    xnp = xcg + sm * cref
    cl37 = np.polyval(np.polyfit(a, cl, 1), np.deg2rad(3.7))
    lod = np.interp(0.35, cl, cl / cd)
    print(f"{label:10s} {cla:11.3f} {cma:11.3f} {dcmdcl:9.4f} "
          f"{100 * sm:7.1f} {xnp:9.2f} {cl37:9.3f} {lod:11.2f}")
