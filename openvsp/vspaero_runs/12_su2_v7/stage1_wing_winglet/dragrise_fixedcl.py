"""Drag-divergence curve at CONSTANT lift -- the honest version.

Why not just sweep Mach at fixed AoA: an aircraft in cruise holds lift
(weight) constant and lets angle of attack fall as it speeds up. A fixed-AoA
sweep instead lets CL climb with Mach (0.42 -> 0.66 in the first attempt),
and since wave drag is strongly CL-dependent, that manufactures a drag rise
that has as much to do with the lift climbing as with the Mach number. It
put apparent drag divergence at ~M0.74 and made the wing look far worse than
it is.

So at each Mach: run three angles bracketing the cruise lift, fit the polar
CD = CD0 + k*CL^2, and read drag off at CL = 0.360 (MTOW at FL410, M0.80 --
derivation in aoa_finder.py). That also yields CD0(M) and span efficiency
e(M) as a free by-product, which is what actually shows WHERE the drag rise
comes from: CD0 climbing is wave drag, k climbing is the shock interfering
with the lift distribution.

SU2's own FIXED_CL_MODE would do this directly but is documented unstable on
this build (su2_screen/ENVIRONMENT.md: never engaged an AoA update in 3
pilot attempts), hence bracketing by hand.

Usage:  python3 dragrise_fixedcl.py
"""
import csv
import json
import math
import os
import subprocess

import gen_configs as gc

HERE = os.path.dirname(os.path.abspath(__file__))
SU2 = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"
MESH = "wing_winglet_euler3.su2"
TARGET_CL = 0.360
AR = 41.5324 ** 2 / 193.678
ITERS = 3000

# Nearest-to-0.80 first so each solve restarts from a similar flow field.
MACHS = [0.80, 0.78, 0.82, 0.75, 0.85, 0.70]

# Measured at M0.80 by aoa_finder.py: CL = 0.16075*AoA + 0.01258 (deg).
SLOPE_080, ICEPT_080 = 0.16075, 0.01258
BETA_080 = math.sqrt(1.0 - 0.80 ** 2)

# M0.80 originally reused aoa_finder.py's 1.0/1.5/2.0 deg points. That was a
# false economy: those angles top out at CL=0.334, BELOW the CL=0.360 target,
# so the design point -- the single most important number here -- came out
# EXTRAPOLATED while every other Mach was interpolated. It also fitted a
# different CL range than its neighbours, which is why CD0 came out
# non-monotonic across Mach (14.3 -> 24.2 -> 13.1 counts, physically
# impossible). M0.80 now gets the same bracket_angles() treatment as
# everything else; the old points remain on disk and analyze_dragrise.py
# still picks them up as extra samples.


def read_final(tag):
    rows = list(csv.DictReader(open(os.path.join(HERE, f"history_{tag}.csv"))))
    k = {c.strip().strip('"'): c for c in rows[0].keys()}
    last = rows[-1]
    return float(last[k["CL"]]), float(last[k["CD"]]), float(last[k["CMz"]])


def bracket_angles(mach):
    """Prandtl-Glauert-scale the M0.80 lift curve to guess the cruise angle,
    then bracket it. Only a starting guess -- the polar fit is what decides."""
    beta = math.sqrt(1.0 - mach ** 2)
    slope = SLOPE_080 * BETA_080 / beta
    icept = ICEPT_080 * BETA_080 / beta
    a = (TARGET_CL - icept) / slope
    return [round(a - 0.4, 2), round(a, 2), round(a + 0.4, 2)]


def fit_polar(pts):
    """Least squares CD = CD0 + k*CL^2 over (CL, CD) pairs."""
    n = len(pts)
    x = [cl ** 2 for cl, _ in pts]
    y = [cd for _, cd in pts]
    sx, sy = sum(x), sum(y)
    sxx = sum(v * v for v in x)
    sxy = sum(a * b for a, b in zip(x, y))
    k = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    cd0 = (sy - k * sx) / n
    resid = max(abs(b - (k * a + cd0)) for a, b in zip(x, y))
    return cd0, k, resid


def main():
    prev = "aoa2p0_m0p80"
    out = []

    for mach in MACHS:
        mtag = f"m{mach:.2f}".replace(".", "p")
        pts = []

        for aoa in bracket_angles(mach):
            tag = f"cl_a{aoa:.2f}".replace(".", "p") + f"_{mtag}"
            # Resumable: this loop has already been killed once mid-campaign
            # (harness stopped the wrapper). Skip anything already solved so
            # a re-run fills gaps instead of repeating ~40 min of work.
            if os.path.exists(os.path.join(HERE, f"history_{tag}.csv")):
                cl, cd, cmz = read_final(tag)
                print(f"  [have] M{mach} AoA={aoa}  CL={cl:.4f} "
                      f"CD={cd*1e4:.2f}", flush=True)
                pts.append((cl, cd))
                prev = tag
                continue
            cfg = gc.write_config(tag, mach=mach, aoa=aoa, mesh_file=MESH,
                                  iters=ITERS, restart_from=prev)
            print(f"--> M{mach} AoA={aoa} (from {prev})", flush=True)
            with open(os.path.join(HERE, f"log_{tag}.txt"), "w") as lg:
                rc = subprocess.run([SU2, os.path.basename(cfg)], cwd=HERE,
                                    stdout=lg,
                                    stderr=subprocess.STDOUT).returncode
            if rc != 0:
                print(f"    FAILED rc={rc}", flush=True)
                continue
            cl, cd, cmz = read_final(tag)
            print(f"    CL={cl:.4f}  CD={cd*1e4:.2f} counts", flush=True)
            pts.append((cl, cd))
            prev = tag

        if len(pts) < 2:
            print(f"  M{mach}: too few points to fit, skipping", flush=True)
            continue

        cd0, k, resid = fit_polar(pts)
        cd_at = cd0 + k * TARGET_CL ** 2
        e = 1.0 / (math.pi * k * AR) if k > 0 else float("nan")
        cls = [c for c, _ in pts]
        extrap = not (min(cls) <= TARGET_CL <= max(cls))
        out.append(dict(mach=mach, cd0=cd0, k=k, e=e, cd_at_target=cd_at,
                        resid=resid, cl_range=[min(cls), max(cls)],
                        extrapolated=extrap))
        print(f"  M{mach}: CD0={cd0*1e4:.2f}  e={e:.3f}  "
              f"CD@CL{TARGET_CL}={cd_at*1e4:.2f} counts"
              f"{'  [EXTRAPOLATED]' if extrap else ''}", flush=True)

    out.sort(key=lambda r: r["mach"])
    with open(os.path.join(HERE, "dragrise_fixedcl.json"), "w") as fh:
        json.dump(out, fh, indent=2)

    print(f"\n=== DRAG RISE AT CONSTANT CL = {TARGET_CL} ===")
    print(f"{'Mach':>6} {'CD (counts)':>12} {'CD0':>8} {'e':>7} {'fit resid':>11}")
    for r in out:
        flag = " *extrap" if r["extrapolated"] else ""
        print(f"{r['mach']:>6.2f} {r['cd_at_target']*1e4:>12.2f} "
              f"{r['cd0']*1e4:>8.2f} {r['e']:>7.3f} "
              f"{r['resid']*1e4:>10.2f}c{flag}")


if __name__ == "__main__":
    main()
