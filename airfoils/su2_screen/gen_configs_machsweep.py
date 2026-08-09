"""Generate SU2 RANS config files for a Mach sweep at (approximately) fixed
C_L, for the SC(2)-0412 vs SC(2)-0414 critical-Mach determination.

Pilot testing (2026-08-04) showed FIXED_CL_MODE never actually engaged within
1500-2000 iterations across three attempts (no AoA-update diagnostic ever
printed), while the underlying fixed-AoA flow itself showed genuine periodic
oscillation (CL cycling ~0.0-0.44 with a ~1000-iteration period, residuals
stuck around rms_rho~-1.8 to -2.5, well short of the ~-2.86 the validated
baseline reached) at the bracket's higher Mach points -- consistent with real
transonic buffet/periodic shock-induced separation on this 12%-thick section,
not a numerics/CFL artifact (lowering CFL_NUMBER 3.0->1.5 and the adaptation
cap 100->20 made no qualitative difference). A steady RANS solve cannot
converge a genuinely unsteady flow regardless of AoA-driver tuning.

Switched to the SAME proven-stable methodology as the original SC(2)-0410 vs
NACA 64-209 screen (su2_screen/gen_configs.py): FIXED AoA per run, no
FIXED_CL_MODE. AoA is set via a Prandtl-Glauert-corrected estimate
(aoa_guess()) so each run lands close to but not exactly at C_L=0.248 --
matching how the original screen also didn't hit an exact target C_L, and
accepted as adequate for a conceptual-design-level screen. ITER=4500,
CONV_STARTITER=500 match the original validated baseline exactly (no
FIXED_CL overhead to budget for anymore).

Re is NOT held fixed across the sweep: at fixed FL410 temperature/altitude,
Re is proportional to true airspeed, hence to Mach. Re(M) = Re_ref * (M/M_ref).

Usage: python3 gen_configs_machsweep.py [--pilot]
  --pilot: only emit the single mid-bracket calibration run (sc20412 at its
  own M_crit_PG estimate) to sanity-check convergence before committing the
  full ~14-run matrix.
"""
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
    """PG-corrected AoA estimate for C_L=0.248 at Mach m (linearized -- good
    enough to land close to the target, not exact)."""
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
        reynolds = RE_REF * (m / M_REF)
        aoa0 = round(aoa_guess(m, alpha_incomp), 3)
        tag = f"{cand}_M{m:.4f}".replace(".", "p") + tag_suffix
        cfg = TEMPLATE.format(mach=m, reynolds=reynolds, aoa_guess=aoa0, iters=iters, startiter=startiter, mesh=mesh, tag=tag)
        with open(f"cfg_{tag}.cfg", "w") as f:
            f.write(cfg)
        print(f"wrote cfg_{tag}.cfg  (M={m}, Re={reynolds:.0f}, AoA0={aoa0})")
