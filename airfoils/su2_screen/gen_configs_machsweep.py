"""Generate SU2 RANS Mach-sweep configs at (~)fixed CL for SC(2)-0412 vs SC(2)-0414 -- uses fixed AoA per run (PG-corrected estimate), not FIXED_CL_MODE, which piloted 3x and never engaged while the underlying flow showed genuine transonic buffet (CL cycling ~0.0-0.44), not a numerics artifact."""
import json
import math
import sys

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

ITER= {iters}
CONV_FIELD= DRAG
CONV_RESIDUAL_MINVAL= -10
CONV_STARTITER= {startiter}
CONV_CAUCHY_ELEMS= 300
CONV_CAUCHY_EPS= 5E-7

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

RE_REF = 7.3e6
M_REF = 0.80
N_POINTS = 7
BRACKET_LO = -0.10  # relative to each candidate's M_crit_PG
BRACKET_HI = 0.05
CL_TARGET = 0.248
A0_DEG = (2 * math.pi) / 57.29578  # thin-airfoil lift-curve slope, 1/deg (project default, config.md B.1)

with open("../results_critical_mach_pg.json") as f:
    pg = json.load(f)["candidates"]

candidates = {
    "sc20412": ("sc20412.su2", pg["NASA SC(2)-0412"]),
    "sc20414": ("sc20414.su2", pg["NASA SC(2)-0414"]),
}

pilot = "--pilot" in sys.argv


def aoa_guess(m, alpha_incomp_at_cl_target):
    """PG-corrected AoA estimate for CL=0.248 at Mach m -- linearized, close enough not exact."""
    cl_incomp_equiv = CL_TARGET * math.sqrt(max(1 - m**2, 1e-6))
    return alpha_incomp_at_cl_target + (cl_incomp_equiv - CL_TARGET) / A0_DEG


for cand, (mesh, pg_data) in candidates.items():
    mcrit_pg = pg_data["M_crit_PG"]
    alpha_incomp = pg_data["alpha @ Cl_target (deg)"]
    lo, hi = mcrit_pg + BRACKET_LO, mcrit_pg + BRACKET_HI
    machs = [round(lo + i * (hi - lo) / (N_POINTS - 1), 4) for i in range(N_POINTS)]

    if pilot:
        if cand != "sc20412":
            continue
        machs = [round(mcrit_pg, 4)]

    iters, startiter, tag_suffix = 4000, 500, "_pilot" if pilot else ""

    for m in machs:
        reynolds = RE_REF * (m / M_REF)  # Re scales with true airspeed at fixed FL410 temperature/altitude, hence with Mach
        aoa0 = round(aoa_guess(m, alpha_incomp), 3)
        tag = f"{cand}_M{m:.4f}".replace(".", "p") + tag_suffix
        cfg = TEMPLATE.format(mach=m, reynolds=reynolds, aoa_guess=aoa0, iters=iters, startiter=startiter, mesh=mesh, tag=tag)
        with open(f"cfg_{tag}.cfg", "w") as f:
            f.write(cfg)
        print(f"wrote cfg_{tag}.cfg  (M={m}, Re={reynolds:.0f}, AoA0={aoa0})")
