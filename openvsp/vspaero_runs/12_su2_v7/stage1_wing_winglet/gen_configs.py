"""SU2 Euler config generator for the Stage 1 (wing+winglet) Mach sweep: mesh is in METERS (Mesh.ScalingFactor 0.3048 in make_mesh_euler2.py) so freestream state below is plain SI; Sref is HALF the full-aircraft area (half-model + symmetry BC) while bref/cref stay full, matching VSPAERO convention (193.678/41.5324/5.0236 ft); moment reference is the wing ROOT LE in this stage's own local frame (NOT the true x=14.346 ft full-aircraft position, gen_v7.py) -- fine for a stage-1 pitching-moment TREND but needs reconciling once stage 2 (+fuselage) is compared directly; freestream is FL410 ISA (T=216.65K, p=17872 Pa, matching drag_buildup.py/VSPAERO Re_Cref=8e6)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

FT2M = 0.3048
SREF_FULL_FT2, BREF_FT, CREF_FT = 193.678, 41.5324, 5.0236
SREF_HALF_M2 = (SREF_FULL_FT2 / 2.0) * FT2M ** 2
BREF_M = BREF_FT * FT2M
CREF_M = CREF_FT * FT2M

T_FL410, P_FL410 = 216.65, 17872.0   # K, Pa

BASE = """SOLVER= EULER
MATH_PROBLEM= DIRECT
RESTART_SOL= {restart}

MACH_NUMBER= {mach:.4f}
AOA= {aoa:.3f}
SIDESLIP_ANGLE= 0.0
FREESTREAM_TEMPERATURE= {t_fs:.2f}
FREESTREAM_PRESSURE= {p_fs:.1f}
FREESTREAM_OPTION= TEMPERATURE_FS

REF_ORIGIN_MOMENT_X= 0.0
REF_ORIGIN_MOMENT_Y= 0.0
REF_ORIGIN_MOMENT_Z= 0.0
REF_LENGTH= {cref:.5f}
REF_AREA= {sref:.5f}

MARKER_EULER= ( wing_wall )
MARKER_SYM= ( symmetry )
MARKER_FAR= ( farfield )
MARKER_PLOTTING= ( wing_wall )
MARKER_MONITORING= ( wing_wall )

% -- numerics: JST for fast initial convergence (cfdinstructions.md); smooth
% limiter to avoid limit-cycle oscillation near shocks
NUM_METHOD_GRAD= GREEN_GAUSS
CONV_NUM_METHOD_FLOW= JST
MUSCL_FLOW= NO
JST_SENSOR_COEFF= ( 0.5, 0.02 )
TIME_DISCRE_FLOW= EULER_IMPLICIT

% -- CFL ramping: conservative start, adapt up as the solve settles
CFL_NUMBER= 5.0
CFL_ADAPT= YES
CFL_ADAPT_PARAM= ( 0.5, 1.2, 1.0, 100.0 )

LINEAR_SOLVER= FGMRES
LINEAR_SOLVER_PREC= ILU
LINEAR_SOLVER_ERROR= 1E-2
LINEAR_SOLVER_ITER= 10

% -- mesh sequencing / multigrid (cfdinstructions.md sec.5)
MGLEVEL= 2
MGCYCLE= V_CYCLE
MG_PRE_SMOOTH= ( 1, 2, 1 )
MG_POST_SMOOTH= ( 0, 0, 0 )

ITER= {iters}
CONV_FIELD= DRAG
CONV_RESIDUAL_MINVAL= -10
CONV_STARTITER= 50
CONV_CAUCHY_ELEMS= 100
CONV_CAUCHY_EPS= 1E-5

MESH_FILENAME= {mesh_file}
MESH_FORMAT= SU2
TABULAR_FORMAT= CSV
HISTORY_OUTPUT= ( ITER, RMS_RES, AERO_COEFF )
CONV_FILENAME= history_{tag}
SOLUTION_FILENAME= {sol_in}
RESTART_FILENAME= restart_{tag}.dat
OUTPUT_FILES= ( RESTART, SURFACE_CSV, PARAVIEW )
SURFACE_FILENAME= surface_{tag}
VOLUME_FILENAME= volume_{tag}
OUTPUT_WRT_FREQ= 200
SCREEN_OUTPUT= ( INNER_ITER, RMS_DENSITY, RMS_ENERGY, LIFT, DRAG, MOMENT_Z )
SCREEN_WRT_FREQ_INNER= 25
"""


def write_config(tag, mach, aoa, mesh_file, iters=3000, restart_from=None):
    """restart_from: tag of the previous sweep point to chain from, or None for a cold start (uniform freestream)."""
    restart = "YES" if restart_from else "NO"
    sol_in = f"restart_{restart_from}.dat" if restart_from else "solution_flow.dat"
    body = BASE.format(
        restart=restart, mach=mach, aoa=aoa, t_fs=T_FL410, p_fs=P_FL410,
        cref=CREF_M, sref=SREF_HALF_M2, iters=iters, mesh_file=mesh_file,
        tag=tag, sol_in=sol_in,
    )
    path = os.path.join(HERE, f"cfg_{tag}.cfg")
    with open(path, "w") as fh:
        fh.write(body)
    return path


if __name__ == "__main__":
    # quick single-point sanity config: design condition, coarse mesh, low iteration cap -- just confirms SU2 accepts the mesh and runs
    write_config("sanity_M080", mach=0.80, aoa=3.7,
                 mesh_file="coarse_euler2.su2", iters=200)
    print("wrote cfg_sanity_M080.cfg")
