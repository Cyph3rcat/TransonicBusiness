"""Finds the AoA at M0.80 for the real cruise CL: VSPAERO's fixed AoA=3.7 deg reported CL=0.34, but the Euler solve gives CL=0.608 (69% more lift than the aircraft flies at), so the drag-divergence result was pessimistic at a non-existent operating point; target CL=0.360 from W_TO=11660 lb, Sref=193.678 ft^2, FL410/M0.80 q=8006.6 Pa (config.md A.3/B), cross-checked against config.md's own 0.34-0.375 cruise-CL band. Runs 3 restart-chained angles and linearly fits CL(alpha) -- 3 points, not 2, so the residual flags nonlinearity before trusting the interpolated angle. Usage: python3 aoa_finder.py"""
import csv
import os
import subprocess

import gen_configs as gc

HERE = os.path.dirname(os.path.abspath(__file__))
SU2 = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"
MESH = "wing_winglet_euler3.su2"
MACH = 0.80
AOAS = [2.0, 1.5, 1.0]      # descending: 2.0 is nearest the 3.7 restart
TARGET_CL = 0.360
ITERS = 3000


def read_final(tag):
    path = os.path.join(HERE, f"history_{tag}.csv")
    rows = list(csv.DictReader(open(path)))
    key = {c.strip().strip('"'): c for c in rows[0].keys()}
    last = rows[-1]
    return (float(last[key["CL"]]), float(last[key["CD"]]),
            float(last[key["CMz"]]), len(rows))


def main():
    prev = "fine_m0p80"          # converged M0.80 at AoA 3.7, same mesh
    out = []
    for aoa in AOAS:
        tag = "aoa" + f"{aoa:.1f}".replace(".", "p") + "_m0p80"
        cfg = gc.write_config(tag, mach=MACH, aoa=aoa, mesh_file=MESH,
                              iters=ITERS, restart_from=prev)
        print(f"--> M{MACH} AoA={aoa} (restart from {prev})", flush=True)
        with open(os.path.join(HERE, f"log_{tag}.txt"), "w") as lg:
            rc = subprocess.run([SU2, os.path.basename(cfg)], cwd=HERE,
                                stdout=lg, stderr=subprocess.STDOUT).returncode
        if rc != 0:
            print(f"    FAILED rc={rc}", flush=True)
            continue
        cl, cd, cmz, n = read_final(tag)
        print(f"    CL={cl:.4f}  CD={cd*1e4:.2f} counts  CMz={cmz:.4f} "
              f"({n} iters)", flush=True)
        out.append((aoa, cl, cd, cmz))
        prev = tag

    # Known anchor from the sweep: AoA 3.7 -> CL 0.6077
    out.append((3.7, 0.6077, 0.025881, -0.0003))
    out.sort()

    print("\n  AoA     CL        CD(counts)   CMz")
    for a, cl, cd, cm in out:
        print(f"  {a:4.1f}  {cl:.4f}   {cd*1e4:8.2f}   {cm:+.4f}")

    if len(out) >= 2:
        n = len(out)
        sa = sum(a for a, _, _, _ in out)
        sc = sum(c for _, c, _, _ in out)
        saa = sum(a * a for a, _, _, _ in out)
        sac = sum(a * c for a, c, _, _ in out)
        slope = (n * sac - sa * sc) / (n * saa - sa * sa)
        icept = (sc - slope * sa) / n
        resid = max(abs(c - (slope * a + icept)) for a, c, _, _ in out)
        print(f"\nfit: CL = {slope:.5f}*AoA + {icept:.5f}"
              f"   (CL_alpha = {slope*57.2958:.3f}/rad, max resid {resid:.4f})")
        print(f"AoA for CL={TARGET_CL:.3f}  ->  {(TARGET_CL-icept)/slope:.3f} deg")


if __name__ == "__main__":
    main()
