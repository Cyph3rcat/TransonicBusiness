"""Re-extracts converged CL/CD/CMz per Mach point: the sweep converged all 8 points but the history CSV only had RMS_RES (HISTORY_OUTPUT wasn't set, so SCREEN_OUTPUT showed CL/CD/CMz but it was never captured to file); fixed in gen_configs.py (HISTORY_OUTPUT=(ITER,RMS_RES,AERO_COEFF)), so this cheaply re-runs each already-converged point for 2 iterations from its restart file just to get a CSV with the coefficients."""
import csv
import glob
import os
import re
import subprocess

import gen_configs as gc

HERE = os.path.dirname(os.path.abspath(__file__))
SU2 = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"
MESH_FILE = "coarse_euler2.su2"

results = []
for f in sorted(glob.glob(os.path.join(HERE, "restart_m0p*.dat"))):
    tag = os.path.basename(f).replace("restart_", "").replace(".dat", "")
    m = re.search(r"m0p(\d+)", tag)
    mach = float("0." + m.group(1))
    extag = f"{tag}_reext"
    cfg_path = gc.write_config(extag, mach=mach, aoa=3.7,
                                mesh_file=MESH_FILE, iters=150, restart_from=tag)
    with open(os.path.join(HERE, f"log_{extag}.txt"), "w") as logf:
        subprocess.run([SU2, os.path.basename(cfg_path)], cwd=HERE,
                        stdout=logf, stderr=subprocess.STDOUT)
    hist = os.path.join(HERE, f"history_{extag}.csv")
    with open(hist) as fh:
        rows = list(csv.reader(fh))
    header = [h.strip().strip('"') for h in rows[0]]
    last = dict(zip(header, rows[-1]))
    results.append((mach, float(last["CL"]), float(last["CD"]), float(last["CMz"])))

results.sort()
print(f"{'Mach':>6} {'CL':>10} {'CD':>10} {'CD_counts':>10} {'CMz':>10}")
for mach, cl, cd, cmz in results:
    print(f"{mach:6.2f} {cl:10.5f} {cd:10.5f} {cd*1e4:10.2f} {cmz:10.5f}")

with open(os.path.join(HERE, "sweep_final.csv"), "w") as fh:
    fh.write("Mach,CL,CD,CMz\n")
    for mach, cl, cd, cmz in results:
        fh.write(f"{mach},{cl},{cd},{cmz}\n")
