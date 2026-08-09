"""Classical Prandtl-Glauert + critical-Cp method for M_crit.

Candidates: NASA SC(2)-0412 (12% t/c), NASA SC(2)-0414 (14% t/c) -- the two
thicker supercritical sections adopted 2026-08-04 after SC(2)-0410 (9.97%)
was retired for insufficient wing fuel volume (doubts.md #15).

Method (replaces Korn's equation per 2026-08-04 request -- Korn's own
regression already contradicted itself across methods for the SC(2)-0410
screen, see config.md B.5.1):
  1. Get the low-speed (incompressible) Cp_min at the design C_li=0.248
     from NeuralFoil (aerosandbox's `Cpmin_0` field -- valid regime, no
     compressibility extrapolation baked in yet).
  2. Apply the Prandtl-Glauert rule: Cp(M) = Cpmin_0 / sqrt(1 - M^2).
  3. Find M where Cp(M) equals the isentropic critical-Cp curve Cp_cr(M)
     (critical_cp.py) -- that crossing is M_crit.

This is a linearized/low-speed-extrapolated estimate. It is expected to be
LESS accurate than the real SU2 Mach-sweep result (su2_screen/) in exactly
the M~0.7-0.8 regime being probed, since Prandtl-Glauert's 1/sqrt(1-M^2)
term is known to degrade near there -- kept as the SU2 sweep's Mach-bracket
prior and as an ASSUMPTION-tier comparison point, not the canonical number.
"""

import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
import aerosandbox as asb

from evaluate_transonic import load_dat_smart
from critical_cp import cp_critical

HERE = Path(__file__).parent
CL_TARGET = 0.248
RE = 7.3e6  # canonical FL410 cruise-start bracket, matches su2_screen's configs

CANDIDATES = {
    "NASA SC(2)-0412": "sc20412.dat",
    "NASA SC(2)-0414": "sc20414.dat",
}


def find_alpha_for_cl(af: asb.Airfoil, cl_target: float, re: float) -> float:
    alphas = np.linspace(-4, 6, 401)
    aero = af.get_aero_from_neuralfoil(alpha=alphas, Re=re, mach=0.0)
    order = np.argsort(aero["CL"])
    return float(np.interp(cl_target, aero["CL"][order], alphas[order]))


def find_mcrit_pg(cpmin_0: float) -> float:
    def residual(M):
        return cpmin_0 / np.sqrt(1 - M**2) - cp_critical(M)

    Ms = np.linspace(0.3, 0.95, 400)
    res = [residual(m) for m in Ms]
    for i in range(len(Ms) - 1):
        if res[i] == 0:
            return Ms[i]
        if res[i] * res[i + 1] < 0:
            return brentq(residual, Ms[i], Ms[i + 1])
    raise ValueError(f"No crossing found for Cpmin_0={cpmin_0}")


def main():
    results = {}
    for name, filename in CANDIDATES.items():
        coords = load_dat_smart(HERE / "dat" / filename)
        af = asb.Airfoil(name=name, coordinates=coords)

        alpha_cl = find_alpha_for_cl(af, CL_TARGET, RE)
        aero0 = af.get_aero_from_neuralfoil(alpha=alpha_cl, Re=RE, mach=0.0)
        cpmin_0 = float(np.asarray(aero0["Cpmin_0"]).reshape(-1)[0])
        m_crit_pg = find_mcrit_pg(cpmin_0)

        results[name] = {
            "t/c (%)": round(af.max_thickness() * 100, 2),
            "alpha @ Cl_target (deg)": round(alpha_cl, 3),
            "Cpmin_0 (incompressible)": round(cpmin_0, 4),
            "M_crit_PG": round(m_crit_pg, 4),
        }
        print(
            f"{name}: t/c={results[name]['t/c (%)']}%, "
            f"alpha@Cl={CL_TARGET}={alpha_cl:.3f} deg, "
            f"Cpmin_0={cpmin_0:.4f}, M_crit_PG={m_crit_pg:.4f}"
        )

    out_path = HERE / "results_critical_mach_pg.json"
    out_path.write_text(json.dumps({"Re": RE, "cl_target": CL_TARGET, "candidates": results}, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
