"""
Reconverged re-run of the SC(2)-0412 adaptive Mach sweep (2026-08-04, v2).

Why this exists: the v1 sweep (adaptive_sweep.py, results in
mach_sweep_sc20412/) produced a genuinely noisy, non-monotonic Cd(M) curve
(272 -> 52 -> 233 -> 155 -> 44 -> 126 -> 208 counts). Root-caused by comparing
against this project's OWN proven-stable baseline (the original SC(2)-0410 vs
NACA 64-209 screen, su2_screen/README.md round 2, which genuinely plateaued):
the v1 template loosened CONV_CAUCHY_EPS 100x (5E-7 -> 5E-5), CONV_CAUCHY_ELEMS
3x (300 -> 100), and cut ITER by a third (4500 -> 3000) relative to that
baseline. This script reverts those three to the baseline and adds
RESTART_SOL solution-continuation chaining between Mach points (each point
warm-starts from the previous point's converged flow instead of a cold start).

Explicitly NOT changed: AoA control. FIXED_CL_MODE was already piloted 3x for
this exact section/Re/Mach bracket and never engaged the AoA controller in
up to 2000 iterations, while the underlying fixed-AoA flow itself cycled CL
~0.0-0.44 with a ~1000-iteration period -- root-caused as genuine transonic
buffet (periodic shock-induced separation) on this 12%-thick section, not a
numerics artifact (lowering CFL 3.0->1.5 made no difference). A steady RANS
solve cannot converge a physically unsteady flow regardless of how AoA is
driven, so fixed-AoA-per-point (PG-corrected estimate) is kept, matching both
the v1 sweep and the original validated screen's methodology. See
ENVIRONMENT.md and gen_configs_machsweep.py's docstring for the full record.

Expectation going in: if the higher-Mach points (M >~ 0.65-0.70, where CL
cycling was previously observed) still fail to plateau even at ITER=4500 with
the tightened Cauchy tolerance, that is itself evidence of real buffet onset
near M_dd, not proof the fix failed -- worth reporting as such, not silently
discarded.

Runs in a fresh directory (mach_sweep_v2/ in WSL, mach_sweep_sc20412_v2/ once
copied back to the Windows repo) so v1's results are left untouched for the
historical record, same pattern as this repo's existing round-1/round-2 split.

Run from the mach_sweep_v2 working directory (has sc20412.su2 already):
    python3 adaptive_sweep_v2.py
"""
import json
import math
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent if "__file__" in dir() else Path(".")
SU2_BIN = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"

RE_REF = 7.3e6
M_REF = 0.80
CL_TARGET = 0.248
A0_DEG = (2 * math.pi) / 57.29578
GAMMA = 1.4

MACH_START = 0.5922
MACH_STEP = 0.03
MAX_POINTS = 7
DCD_DM_THRESHOLD = 0.10
CONSECUTIVE_NEEDED = 2

# TEMPLATE: convergence block reverted to the proven-stable baseline
# (su2_screen/README.md round 2 / gen_configs_machsweep.py), NOT the loosened
# v1 values. RESTART_SOL/SOLUTION_FILENAME are new -- chain each point off the
# previous point's converged solution.
TEMPLATE = """\
SOLVER= RANS
KIND_TURB_MODEL= SST
MATH_PROBLEM= DIRECT

MACH_NUMBER= {mach}
AOA= {aoa_guess}
FREESTREAM_TEMPERATURE= 216.65
REYNOLDS_NUMBER= {reynolds:.0f}
REYNOLDS_LENGTH= 1.0
INIT_OPTION= REYNOLDS
FREESTREAM_OPTION= TEMPERATURE_FS

REF_ORIGIN_MOMENT_X= 0.25
REF_ORIGIN_MOMENT_Y= 0.00
REF_ORIGIN_MOMENT_Z= 0.00
REF_LENGTH= 1.0
REF_AREA= 1.0

MARKER_HEATFLUX= ( airfoil, 0.0 )
MARKER_FAR= ( farfield )
MARKER_PLOTTING= ( airfoil )
MARKER_MONITORING= ( airfoil )

NUM_METHOD_GRAD= WEIGHTED_LEAST_SQUARES
CFL_NUMBER= 1.5
CFL_ADAPT= YES
CFL_ADAPT_PARAM= ( 0.1, 1.2, 1.0, 20.0 )

CONV_NUM_METHOD_FLOW= ROE
MUSCL_FLOW= YES
SLOPE_LIMITER_FLOW= VENKATAKRISHNAN
ENTROPY_FIX_COEFF= 0.1
TIME_DISCRE_FLOW= EULER_IMPLICIT

CONV_NUM_METHOD_TURB= SCALAR_UPWIND
MUSCL_TURB= NO
SLOPE_LIMITER_TURB= VENKATAKRISHNAN
TIME_DISCRE_TURB= EULER_IMPLICIT

LINEAR_SOLVER= FGMRES
LINEAR_SOLVER_PREC= LU_SGS
LINEAR_SOLVER_ERROR= 1E-6
LINEAR_SOLVER_ITER= 15

ITER= 4500
CONV_FIELD= DRAG
CONV_RESIDUAL_MINVAL= -3.0
CONV_STARTITER= 500
CONV_CAUCHY_ELEMS= 300
CONV_CAUCHY_EPS= 5E-7

RESTART_SOL= {restart_sol}
{solution_filename_line}MESH_FILENAME= {mesh}
MESH_FORMAT= SU2
TABULAR_FORMAT= CSV
CONV_FILENAME= history_{tag}
RESTART_FILENAME= restart_{tag}.dat
OUTPUT_FILES= (RESTART, SURFACE_CSV)
SURFACE_FILENAME= surface_{tag}
OUTPUT_WRT_FREQ= 500
SCREEN_OUTPUT= (INNER_ITER, RMS_DENSITY, RMS_ENERGY, LIFT, DRAG)
SCREEN_WRT_FREQ_INNER= 50
"""

ROW_RE = re.compile(r"^\|\s*(\d+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*(-?[\d.]+)\|\s*$", re.MULTILINE)
PSTATIC_RE = re.compile(r"\|\s*Static Pressure\|\s*([\d.eE+-]+)\|")
DENSITY_RE = re.compile(r"\|\s*Density\|\s*([\d.eE+-]+)\|")
VMAG_RE = re.compile(r"\|\s*Velocity Magnitude\|\s*([\d.eE+-]+)\|")


def aoa_guess(m: float, alpha_incomp: float) -> float:
    cl_incomp_equiv = CL_TARGET * math.sqrt(max(1 - m**2, 1e-6))
    return alpha_incomp + (cl_incomp_equiv - CL_TARGET) / A0_DEG


def run_su2(mach: float, alpha_incomp: float, restart_from: str | None,
            cand: str = "sc20412", mesh: str = "sc20412.su2") -> dict:
    reynolds = RE_REF * (mach / M_REF)
    aoa0 = round(aoa_guess(mach, alpha_incomp), 3)
    tag = f"{cand}_v2_M{mach:.4f}".replace(".", "p")
    cfg_path = HERE / f"cfg_{tag}.cfg"
    log_path = HERE / f"log_{tag}.txt"

    if not log_path.exists():
        restart_sol = "YES" if restart_from else "NO"
        sol_line = f"SOLUTION_FILENAME= {restart_from}\n" if restart_from else ""
        cfg = TEMPLATE.format(mach=mach, reynolds=reynolds, aoa_guess=aoa0, mesh=mesh, tag=tag,
                               restart_sol=restart_sol, solution_filename_line=sol_line)
        cfg_path.write_text(cfg)
        print(f"[{tag}] running: M={mach}, AoA0={aoa0}, Re={reynolds:.0f}, "
              f"warm-start-from={restart_from or 'cold'}", flush=True)
        with open(log_path, "w") as f:
            subprocess.run([SU2_BIN, str(cfg_path)], cwd=str(HERE), stdout=f, stderr=subprocess.STDOUT)
    else:
        print(f"[{tag}] reusing existing log", flush=True)

    text = log_path.read_text(errors="ignore")
    rows = ROW_RE.findall(text)
    if not rows:
        raise RuntimeError(f"{tag}: no iteration rows parsed from log -- run may have failed")
    it, rms_rho, rms_e, cl, cd = rows[-1]

    p_m = PSTATIC_RE.search(text)
    rho_m = DENSITY_RE.search(text)
    v_m = VMAG_RE.search(text)
    if not (p_m and rho_m and v_m):
        raise RuntimeError(f"{tag}: freestream table not found in log")

    result = {
        "tag": tag,
        "mach": mach,
        "aoa0": aoa0,
        "final_iter": int(it),
        "rms_rho": float(rms_rho),
        "cl": float(cl),
        "cd": float(cd),
        "p_inf": float(p_m.group(1)),
        "rho_inf": float(rho_m.group(1)),
        "v_inf": float(v_m.group(1)),
        "restart_from": restart_from,
    }
    print(f"[{tag}] DONE: iter={result['final_iter']} rms_rho={result['rms_rho']:.3f} "
          f"CL={result['cl']:.4f} CD={result['cd']:.5f}", flush=True)
    return result


def main():
    with open(HERE.parent / "results_critical_mach_pg.json") as f:
        pg = json.load(f)["candidates"]["NASA SC(2)-0412"]
    alpha_incomp = pg["alpha @ Cl_target (deg)"]

    points = []
    mach = MACH_START
    consecutive_hits = 0
    prev_restart_file = None

    while len(points) < MAX_POINTS:
        r = run_su2(mach, alpha_incomp, prev_restart_file)
        points.append(r)
        prev_restart_file = f"restart_{r['tag']}.dat"

        if len(points) >= 2:
            dM = points[-1]["mach"] - points[-2]["mach"]
            dCd = points[-1]["cd"] - points[-2]["cd"]
            slope = dCd / dM if dM != 0 else 0.0
            print(f"  dCd/dM (last interval) = {slope:.4f}  (Boeing threshold {DCD_DM_THRESHOLD})", flush=True)

            if slope >= DCD_DM_THRESHOLD:
                consecutive_hits += 1
                print(f"  hockey-stick hit #{consecutive_hits}/{CONSECUTIVE_NEEDED}", flush=True)
            else:
                consecutive_hits = 0

            if consecutive_hits >= CONSECUTIVE_NEEDED:
                print(f"HOCKEY STICK RESOLVED after {len(points)} points -- stopping adaptive sweep.", flush=True)
                break

        mach = round(mach + MACH_STEP, 4)

    out_path = HERE / "adaptive_sweep_results_v2.json"
    out_path.write_text(json.dumps(points, indent=2))
    print(f"\nWrote {out_path} ({len(points)} points)", flush=True)
    print("SWEEP_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
