"""
v3 Mach sweep for SC(2)-0412 -- designed for a DEFENSIBLE M_crit / M_dd, fixing
the diagnosed failure modes of both prior attempts:

v1 failure: under-converged limit-cycle sampling. CD at subcritical Mach came
out 272/52/233 counts across M=0.59-0.65 where a clean solution is ~80-95
counts (proved by v2's own first cold-start point: 84.6 counts at M=0.5922).
Snapshotting an oscillating solve at whatever iteration the loop ended is not
a measurement.

v2 failure: RESTART_SOL warm-start chaining through this regime made the
operating point path-dependent -- CL decayed monotonically 0.244 -> 0.033
across the sweep at the same per-point AoA schedule v1 ran, so the curve no
longer represents the design condition at all.

v3 changes (each maps to a specific diagnosed cause):
1. JST central scheme (SU2's standard robust choice for transonic airfoil
   RANS) instead of ROE + MUSCL + Venkatakrishnan limiter -- limiter switching
   on a marginal mesh is a classic driver of exactly the residual limit cycle
   observed (rms_rho pinned at -3.0/-3.1 from iter 500 onward, CD cycling).
2. NO warm-start chaining. Every run is an independent cold start (v1/original
   -screen methodology, which v2's own clean early points validate).
3. No early-exit convergence gamble: fixed ITER=5000 every run, and CD/CL are
   reported as MEAN +/- STD over the last 1500 iterations (windowed statistics
   via HISTORY_OUTPUT=AERO_COEFF), not a single end-point sample. If a run
   still oscillates, the oscillation shows up honestly as an error bar.
4. Constant-CL curve done properly: 3 AoA per Mach point bracketing the
   CL=0.248 target, then CD/Cp_min interpolated to CL=0.248 in
   post-processing. No FIXED_CL_MODE (already proven unstable here 3x).
5. Mach range extended THROUGH cruise: 8 points, 0.60 -> 0.80, spacing tighter
   around the expected knee -- so the drag rise is resolved on both sides
   instead of the sweep ending right where it gets interesting.
6. CFL 4.0 (adapt to 50) with implicit Euler -- appropriate for JST implicit;
   the old CFL 1.5-20 with ROE never pushed residuals past -3.1.

Run from the mach_sweep_v3 working directory (needs sc20412.su2):
    python3 sweep_v3.py
"""
import csv
import json
import math
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent if "__file__" in dir() else Path(".")
SU2_BIN = "/home/cyph3r/mses_replacement/su2/bin/SU2_CFD"

RE_REF = 7.3e6
M_REF = 0.80
CL_TARGET = 0.248
A0_DEG = (2 * math.pi) / 57.29578

MACHS = [0.60, 0.64, 0.67, 0.70, 0.72, 0.74, 0.77, 0.80]
ALPHA_OFFSETS = [0.0, 0.8, 1.6]  # deg, relative to PG-corrected guess; biased
# upward because v1 consistently UNDERSHOT the CL target (0.16-0.21 vs 0.248)
# at offset 0, so the bracket needs to reach higher CL, not lower.
ITER_BUDGET = 5000
AVG_WINDOW = 1500  # iterations averaged for reported CL/CD stats

TEMPLATE = """\
SOLVER= RANS
KIND_TURB_MODEL= SST
MATH_PROBLEM= DIRECT

MACH_NUMBER= {mach}
AOA= {aoa}
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
CFL_NUMBER= 4.0
CFL_ADAPT= YES
CFL_ADAPT_PARAM= ( 0.1, 1.5, 1.0, 50.0 )

CONV_NUM_METHOD_FLOW= JST
JST_SENSOR_COEFF= ( 0.5, 0.02 )
TIME_DISCRE_FLOW= EULER_IMPLICIT

CONV_NUM_METHOD_TURB= SCALAR_UPWIND
MUSCL_TURB= NO
SLOPE_LIMITER_TURB= VENKATAKRISHNAN
TIME_DISCRE_TURB= EULER_IMPLICIT

LINEAR_SOLVER= FGMRES
LINEAR_SOLVER_PREC= LU_SGS
LINEAR_SOLVER_ERROR= 1E-6
LINEAR_SOLVER_ITER= 15

ITER= {iters}
CONV_FIELD= RMS_DENSITY
CONV_RESIDUAL_MINVAL= -12
CONV_STARTITER= {iters}

MESH_FILENAME= sc20412.su2
MESH_FORMAT= SU2
TABULAR_FORMAT= CSV
CONV_FILENAME= history_{tag}
RESTART_SOL= NO
RESTART_FILENAME= restart_{tag}.dat
OUTPUT_FILES= (RESTART, SURFACE_CSV)
SURFACE_FILENAME= surface_{tag}
OUTPUT_WRT_FREQ= 1000
HISTORY_OUTPUT= (ITER, RMS_RES, AERO_COEFF)
HISTORY_WRT_FREQ_INNER= 1
SCREEN_OUTPUT= (INNER_ITER, RMS_DENSITY, RMS_ENERGY, LIFT, DRAG)
SCREEN_WRT_FREQ_INNER= 250
"""

PSTATIC_RE = re.compile(r"\|\s*Static Pressure\|\s*([\d.eE+-]+)\|")
DENSITY_RE = re.compile(r"\|\s*Density\|\s*([\d.eE+-]+)\|")
VMAG_RE = re.compile(r"\|\s*Velocity Magnitude\|\s*([\d.eE+-]+)\|")


def aoa_guess(m: float, alpha_incomp: float) -> float:
    cl_incomp_equiv = CL_TARGET * math.sqrt(max(1 - m**2, 1e-6))
    return alpha_incomp + (cl_incomp_equiv - CL_TARGET) / A0_DEG


def window_stats(history_path: Path):
    """Mean/std of CL, CD and final rms_rho over the last AVG_WINDOW iterations,
    from the SU2 history CSV (column names arrive quoted and space-padded)."""
    with open(history_path) as f:
        reader = csv.reader(f)
        header = [h.strip().strip('"') for h in next(reader)]
        rows = [r for r in reader if r and len(r) == len(header)]
    idx = {name: i for i, name in enumerate(header)}
    cl_col = idx.get("CL")
    cd_col = idx.get("CD")
    rho_col = next((i for n, i in idx.items() if "rms[Rho]" in n and "Rho" == n[5:8]), None)
    if rho_col is None:
        rho_col = next((i for n, i in idx.items() if n.startswith("rms[Rho]")), None)
    tail = rows[-AVG_WINDOW:]
    cls = [float(r[cl_col]) for r in tail]
    cds = [float(r[cd_col]) for r in tail]
    n = len(cls)
    cl_mean = sum(cls) / n
    cd_mean = sum(cds) / n
    cl_std = (sum((x - cl_mean) ** 2 for x in cls) / n) ** 0.5
    cd_std = (sum((x - cd_mean) ** 2 for x in cds) / n) ** 0.5
    rms_final = float(rows[-1][rho_col]) if rho_col is not None else None
    return cl_mean, cl_std, cd_mean, cd_std, rms_final, len(rows)


def run_one(mach: float, aoa: float, alpha_idx: int) -> dict:
    reynolds = RE_REF * (mach / M_REF)
    tag = f"sc20412_v3_M{mach:.2f}_a{alpha_idx}".replace(".", "p")
    cfg_path = HERE / f"cfg_{tag}.cfg"
    log_path = HERE / f"log_{tag}.txt"

    if not log_path.exists():
        cfg_path.write_text(TEMPLATE.format(mach=mach, aoa=round(aoa, 3),
                                            reynolds=reynolds, iters=ITER_BUDGET, tag=tag))
        print(f"[{tag}] running: M={mach}, AoA={aoa:.3f}, Re={reynolds:.0f}", flush=True)
        with open(log_path, "w") as f:
            subprocess.run([SU2_BIN, str(cfg_path)], cwd=str(HERE), stdout=f, stderr=subprocess.STDOUT)
    else:
        print(f"[{tag}] reusing existing log", flush=True)

    text = log_path.read_text(errors="ignore")
    p_m, rho_m, v_m = PSTATIC_RE.search(text), DENSITY_RE.search(text), VMAG_RE.search(text)
    if not (p_m and rho_m and v_m):
        raise RuntimeError(f"{tag}: freestream table not found in log -- run failed?")

    cl_mean, cl_std, cd_mean, cd_std, rms_final, n_hist = window_stats(HERE / f"history_{tag}.csv")
    result = {
        "tag": tag, "mach": mach, "aoa": round(aoa, 3),
        "cl_mean": cl_mean, "cl_std": cl_std,
        "cd_mean": cd_mean, "cd_std": cd_std,
        "rms_rho_final": rms_final, "history_rows": n_hist,
        "p_inf": float(p_m.group(1)), "rho_inf": float(rho_m.group(1)), "v_inf": float(v_m.group(1)),
    }
    print(f"[{tag}] DONE: CL={cl_mean:.4f}+/-{cl_std:.4f}  CD={cd_mean:.5f}+/-{cd_std:.5f}  "
          f"rms_rho={rms_final}", flush=True)
    return result


def main():
    with open(HERE / "results_critical_mach_pg.json") as f:
        pg = json.load(f)["candidates"]["NASA SC(2)-0412"]
    alpha_incomp = pg["alpha @ Cl_target (deg)"]

    results = []
    out_path = HERE / "sweep_v3_raw.json"
    for mach in MACHS:
        base = aoa_guess(mach, alpha_incomp)
        for i, off in enumerate(ALPHA_OFFSETS):
            results.append(run_one(mach, base + off, i))
            out_path.write_text(json.dumps(results, indent=2))  # checkpoint after every run

    print(f"\nWrote {out_path} ({len(results)} runs)", flush=True)
    print("SWEEP_V3_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
