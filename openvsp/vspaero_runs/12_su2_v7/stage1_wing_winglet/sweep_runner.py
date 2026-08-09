"""Stage 1 SU2 Euler Mach sweep runner: drag-divergence curve, fixed AoA.

Sweeps M = 0.60 -> 0.85 at AoA=3.7 deg (fixed -- NOT FIXED_CL_MODE, which
su2_screen/ENVIRONMENT.md documented as unstable on this SU2 build: it never
engaged an AoA update in 3 pilot attempts). Monotonic sweep direction with
restart chaining (solution continuation) between adjacent Mach points per
cfdinstructions.md sec.1 -- each point starts from the previous point's
converged flow instead of uniform freestream, which is both faster and
preserves shock-location continuity across the sweep.

Writes status.json after every completed Mach point (progress dashboard
reads this -- see dashboard.py, run separately in another terminal). Run
this itself in the background (nohup) since the full sweep is many
SU2_CFD invocations.

Usage (inside WSL, in this directory):
    python3 sweep_runner.py
"""
import json
import os
import re
import subprocess
import time

import gen_configs as gc

HERE = os.path.dirname(os.path.abspath(__file__))
# Written to the Windows-visible /mnt/c path (not the WSL-native run dir)
# so dashboard.py can be run directly from a normal Windows terminal with
# no WSL access needed.
STATUS = "/mnt/c/Users/cyphe/downloads/airplane/openvsp/vspaero_runs/12_su2_v7/stage1_wing_winglet/status.json"
SU2 = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"

MACH_POINTS = [0.60, 0.65, 0.70, 0.75, 0.78, 0.80, 0.82, 0.85]
AOA = 3.7
MESH_FILE = "wing_winglet_euler3.su2"   # refined mesh, make_mesh_euler3.py
ITER_CAP = 3000

# No coarse-mesh fallback any more, deliberately. The coarse mesh's results
# are not merely imprecise, they are invalid: it under-predicted CL by ~24%
# (0.340 vs 0.423 at M0.60) and returned NEGATIVE drag at M0.60/0.65. Falling
# back to it silently would reproduce exactly the numbers this rebuild exists
# to replace, so fail loudly instead.
if not os.path.exists(os.path.join(HERE, MESH_FILE)):
    raise SystemExit(f"{MESH_FILE} not found -- run make_mesh_euler3.py first")


def write_status(**kw):
    kw["updated"] = time.time()
    with open(STATUS, "w") as fh:
        json.dump(kw, fh, indent=2)


def tail_history(tag, last_n=1):
    """Parse the last N data rows of history_<tag>.csv -> dict of column:val."""
    path = os.path.join(HERE, f"history_{tag}.csv")
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        lines = [l.strip() for l in fh if l.strip()]
    if len(lines) < 2:
        return None
    header = [h.strip('"') for h in lines[0].split(",")]
    row = lines[-1].split(",")
    return dict(zip(header, row))


def run_point(idx, mach, restart_from):
    # "fine_" prefix keeps these separate from the superseded coarse-mesh
    # history_/surface_ files rather than overwriting them -- the old numbers
    # stay on disk so the before/after comparison remains checkable.
    tag = "fine_" + f"m{mach:.2f}".replace(".", "p")
    cfg_path = gc.write_config(tag, mach=mach, aoa=AOA, mesh_file=MESH_FILE,
                                iters=ITER_CAP, restart_from=restart_from)
    cfg_name = os.path.basename(cfg_path)
    log_path = os.path.join(HERE, f"log_{tag}.txt")

    write_status(stage="stage1_wing_winglet", solver="EULER",
                 mach_point_idx=idx, total_mach_points=len(MACH_POINTS),
                 current_mach=mach, status="running", tag=tag,
                 point_start_time=time.time())

    with open(log_path, "w") as logf:
        proc = subprocess.Popen([SU2, cfg_name], cwd=HERE, stdout=logf,
                                 stderr=subprocess.STDOUT)
        last_iter = -1
        while proc.poll() is None:
            time.sleep(3)
            row = tail_history(tag)
            if row:
                try:
                    it = int(float(row.get('"Inner_Iter"', row.get("Inner_Iter", -1))))
                except (ValueError, TypeError):
                    it = last_iter
                if it != last_iter:
                    last_iter = it
                    write_status(
                        stage="stage1_wing_winglet", solver="EULER",
                        mach_point_idx=idx, total_mach_points=len(MACH_POINTS),
                        current_mach=mach, status="running", tag=tag,
                        iteration=it, iter_cap=ITER_CAP,
                        cl=row.get('"CL"', row.get("CL")),
                        cd=row.get('"CD"', row.get("CD")),
                        point_start_time=time.time(),
                    )
        proc.wait()

    ok = proc.returncode == 0
    final_row = tail_history(tag) or {}
    return tag, ok, final_row


def main():
    write_status(stage="stage1_wing_winglet", solver="EULER",
                 total_mach_points=len(MACH_POINTS), status="starting",
                 sweep_start_time=time.time())

    results = []
    # Sweep monotonically from the design point outward isn't as simple as
    # one direction here (0.80 is mid-sweep) -- restart each point from
    # whichever adjacent point already converged, closest Mach first.
    order = sorted(range(len(MACH_POINTS)), key=lambda i: abs(MACH_POINTS[i] - 0.80))
    # Cold start. The previous version seeded this with "design_M080", whose
    # restart file belongs to the OLD coarse mesh -- a different node count
    # entirely, so SU2 would have either aborted or restarted from garbage.
    prev_tag = None
    for rank, idx in enumerate(order):
        mach = MACH_POINTS[idx]
        tag, ok, row = run_point(idx, mach, restart_from=prev_tag)
        results.append(dict(mach=mach, tag=tag, ok=ok, **row))
        print(f"[{rank+1}/{len(order)}] M={mach:.2f} tag={tag} ok={ok} "
              f"CL={row.get('CL')} CD={row.get('CD')}")
        if ok:
            prev_tag = tag
        with open(os.path.join(HERE, "sweep_results.json"), "w") as fh:
            json.dump(results, fh, indent=2)

    write_status(stage="stage1_wing_winglet", solver="EULER",
                 status="done", total_mach_points=len(MACH_POINTS),
                 sweep_start_time=time.time())
    print("SWEEP DONE")


if __name__ == "__main__":
    main()
