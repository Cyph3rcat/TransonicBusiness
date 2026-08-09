"""Cn_beta / Cl_beta / CY_beta by least-squares slope over a real sideslip sweep.

Usage: python lat_slopes.py label1=path1.polar [label2=path2.polar ...]

VSPAERO sign convention (see any .stab file): CMl = -CMx, CMn = -CMz. The
noise floor is reported explicitly as |CMz| at beta=0, which must be zero by
symmetry - if the slope*beta_max is not comfortably above it, the derivative
is not resolved.
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


print(f"{'model':10s} {'CY_beta':>10s} {'Cl_beta':>10s} {'Cn_beta':>10s}   "
      f"{'|CMz| @b=0':>11s} {'|dCMz| 0-6deg':>14s}  {'S/N':>5s}")
for arg in sys.argv[1:]:
    label, path = arg.split("=", 1)
    hdr, d = read_polar(path)
    col = {n: i for i, n in enumerate(hdr)}
    b = np.deg2rad(d[:, col["Beta"]])
    cmx, cmz, cs = d[:, col["CMxtot"]], d[:, col["CMztot"]], d[:, col["CStot"]]

    def slope(y):
        return np.polyfit(b, y, 1)[0]

    noise = abs(cmz[0])
    span = abs(cmz[-1] - cmz[0])
    print(f"{label:10s} {slope(cs):10.4f} {-slope(cmx):10.4f} {-slope(cmz):10.4f}   "
          f"{noise:11.2e} {span:14.2e}  {span / noise:5.1f}")
