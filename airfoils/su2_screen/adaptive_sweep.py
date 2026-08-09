"""Adaptive Mach sweep for SC(2)-0412 only (2026-08-04 plan revision).

Runs SU2 sequentially at increasing Mach, fixed AoA per point (Prandtl-Glauert
-corrected estimate, no FIXED_CL_MODE -- see gen_configs_machsweep.py's
docstring for why FIXED_CL_MODE was dropped), and stops adaptively once the
Cd(M) "hockey stick" (drag-divergence knee) is clearly resolved, instead of
committing to a fixed point count upfront.

Retuned convergence tolerance (real observed plateau is rms_rho~-3.0 to -3.1,
not the old CONV_RESIDUAL_MINVAL=-10; CD was still slowly drifting at
iteration 4000 under the old CONV_CAUCHY_EPS=5E-7, which never triggered
early exit) -- see plan file status update for the full rationale.

Run from the mach_sweep working directory (has sc20412.su2 already):
    python3 adaptive_sweep.py
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

MACH_START = 0.5922  # already have this point from the first (over-converged) run
MACH_STEP = 0.03
MAX_POINTS = 7
# "Boeing criterion" for drag-divergence Mach: dCd/dM = 0.1 (standard, absolute --
# NOT relative to a "baseline" slope. A relative/ratio criterion breaks down here
# because CD does not monotonically rise from the first point -- observed CD
# actually DROPPED between the first two points (0.0272 -> 0.0052, slope -0.73),
# so any ratio-to-baseline test is undefined/misleading whenever the baseline
# itself is negative or near zero. An absolute threshold has no such failure mode.
DCD_DM_THRESHOLD = 0.10
CONSECUTIVE_NEEDED = 2  # how many intervals in a row must exceed threshold before stopping

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

ITER= 3000
CONV_FIELD= DRAG
CONV_RESIDUAL_MINVAL= -3.0
CONV_STARTITER= 800
CONV_CAUCHY_ELEMS= 100
CONV_CAUCHY_EPS= 5E-5

MESH_FILENAME= {mesh}
MESH_FORMAT= SU2
TABULAR_FORMAT= CSV
CONV_FILENAME= history_{tag}
RESTART_SOL= NO
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


def run_su2(mach: float, alpha_incomp: float, cand: str = "sc20412", mesh: str = "sc20412.su2") -> dict:
    reynolds = RE_REF * (mach / M_REF)
    aoa0 = round(aoa_guess(mach, alpha_incomp), 3)
    tag = f"{cand}_M{mach:.4f}".replace(".", "p")
    cfg_path = HERE / f"cfg_{tag}.cfg"
    log_path = HERE / f"log_{tag}.txt"

    if not log_path.exists():
        cfg = TEMPLATE.format(mach=mach, reynolds=reynolds, aoa_guess=aoa0, mesh=mesh, tag=tag)
        cfg_path.write_text(cfg)
        print(f"[{tag}] running: M={mach}, AoA0={aoa0}, Re={reynolds:.0f}", flush=True)
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

    while len(points) < MAX_POINTS:
        r = run_su2(mach, alpha_incomp)
        points.append(r)

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

    out_path = HERE / "adaptive_sweep_results.json"
    out_path.write_text(json.dumps(points, indent=2))
    print(f"\nWrote {out_path} ({len(points)} points)", flush=True)
    print("SWEEP_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
