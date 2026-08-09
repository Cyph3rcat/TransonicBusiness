"""Summarize taper/twist variants: span efficiency + stall-onset character.

Run from openvsp/vspaero_runs/:  python tools/compare_sweep.py
"""
import glob
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from vspaero_post import read_polar, read_lod, strip_data

S, B, CREF = 193.678, 41.5324, 5.0236
CLMAX2D = 2.11

print(f"{'variant':>14} {'e@CL.34':>8} {'e@CL.60':>8} {'CDi@.34':>9} "
      f"{'stallCL':>8} {'stall_eta':>9} {'a(CL1.27)':>9}")
rows = []
for d in sorted(glob.glob(os.path.join("02_taper_twist", "*"))):
    name = os.path.basename(d)
    base = os.path.join(d, name)
    if not os.path.exists(base + ".polar"):
        continue
    polar, pc = read_polar(base + ".polar")
    aoa = polar[:, pc["AoA"]]
    CL = polar[:, pc["CLtot"]]
    CDi = polar[:, pc["CDi"]]
    Ew = polar[:, pc["Ew"]]
    e34 = np.interp(0.34, CL, Ew)
    e60 = np.interp(0.60, CL, Ew)
    cdi34 = np.interp(0.34, CL, CDi)
    lod, cols = read_lod(base + ".lod")
    aoas = sorted(lod.keys())
    maxcl = []
    for a in aoas:
        eta, chord, cl, load = strip_data(lod[a], cols, B, CREF)
        maxcl.append((a, cl.max(), eta[np.argmax(cl)]))
    maxcl = np.array(maxcl)
    sel = maxcl[:, 0] >= np.median(maxcl[:, 0])
    p = np.polyfit(maxcl[sel, 0], maxcl[sel, 1], 1)
    a_stall = (CLMAX2D - p[1]) / p[0]
    # linear CL fit for extrapolation
    q = np.polyfit(aoa, CL, 1)
    CL_stall = q[0] * a_stall + q[1]
    eta_stall = np.interp(a_stall, maxcl[:, 0], maxcl[:, 2])
    a_127 = (1.27 - q[1]) / q[0]
    print(f"{name:>14} {e34:8.3f} {e60:8.3f} {cdi34:9.5f} "
          f"{CL_stall:8.2f} {eta_stall:9.2f} {a_127:9.1f}")
