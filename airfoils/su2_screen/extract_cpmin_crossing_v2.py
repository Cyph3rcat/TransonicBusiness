"""
Extract M_crit/M_dd from the v2 (reconverged, warm-started) SC(2)-0412 sweep,
and compare against v1. Adds a curve-fit fallback for M_dd since the raw
2-consecutive-interval Boeing-criterion check (same as v1's method) does not
find a crossing in v2's data either -- see adaptive_sweep_v2.log: only one
isolated hit (M=0.6522, dCd/dM=+0.162), never followed by a second, so the
loop ran through all 7 points without triggering the adaptive stop.

This applies the fallback method discussed before re-running: fit a smooth
curve through the (still noisy) Cd(M) points and read M_dd off the fit's
slope, rather than off two adjacent raw samples -- reported alongside the
raw-threshold result (which is None), not in place of disclosing it.
"""
import csv
import json
from pathlib import Path

import numpy as np

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from critical_cp import cp_critical

GAMMA = 1.4
HERE = Path(__file__).parent / "mach_sweep_sc20412_v2"
DCD_DM_THRESHOLD = 0.10
CONSECUTIVE_NEEDED = 2


def cp_min_from_surface_csv(path: Path, p_inf: float, rho_inf: float, v_inf: float) -> float:
    q_inf = 0.5 * rho_inf * v_inf**2
    cp_vals = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rho = float(row["Density"])
            mx = float(row["Momentum_x"])
            my = float(row["Momentum_y"])
            e = float(row["Energy"])
            p = (GAMMA - 1) * (e - 0.5 * (mx**2 + my**2) / rho)
            cp_vals.append((p - p_inf) / q_inf)
    return min(cp_vals)


def find_cp_crossing(machs, cp_mins):
    residuals = [cp_mins[i] - cp_critical(machs[i]) for i in range(len(machs))]
    for i in range(len(machs) - 1):
        if residuals[i] > 0 and residuals[i + 1] <= 0:
            frac = residuals[i] / (residuals[i] - residuals[i + 1])
            return machs[i] + frac * (machs[i + 1] - machs[i])
    return None


def find_hockey_stick_raw(machs, cds):
    slopes = [(cds[i + 1] - cds[i]) / (machs[i + 1] - machs[i]) for i in range(len(machs) - 1)]
    run = 0
    for i, slope in enumerate(slopes):
        run = run + 1 if slope >= DCD_DM_THRESHOLD else 0
        if run >= CONSECUTIVE_NEEDED:
            return machs[i - CONSECUTIVE_NEEDED + 1]
    return None


def find_mdd_fit(machs, cds, degree=3):
    """Fallback: least-squares fit Cd(M), read M_dd off where the FIT's slope
    first sustains >= DCD_DM_THRESHOLD, evaluated on a dense grid (not just the
    7 raw points) so a single noisy sample can't flip the answer."""
    coeffs = np.polyfit(machs, cds, degree)
    deriv = np.polyder(coeffs)
    m_dense = np.linspace(min(machs), max(machs), 400)
    slope_dense = np.polyval(deriv, m_dense)
    cd_fit_dense = np.polyval(coeffs, m_dense)
    for i, s in enumerate(slope_dense):
        if s >= DCD_DM_THRESHOLD:
            return float(m_dense[i]), coeffs, m_dense, cd_fit_dense
    return None, coeffs, m_dense, cd_fit_dense


def main():
    with open(HERE / "adaptive_sweep_results_v2.json") as f:
        points = json.load(f)

    machs = [p["mach"] for p in points]
    cds = [p["cd"] for p in points]

    cp_mins = []
    for p in points:
        surf_path = HERE / f"surface_{p['tag']}.csv"
        cpmin = cp_min_from_surface_csv(surf_path, p["p_inf"], p["rho_inf"], p["v_inf"])
        cp_mins.append(cpmin)
        print(f"M={p['mach']:.4f}  CD={p['cd']:.5f}  CL={p['cl']:.4f}  Cp_min={cpmin:.4f}  "
              f"Cp_cr={cp_critical(p['mach']):.4f}  rms_rho={p['rms_rho']:.3f}")

    m_crit_cfd = find_cp_crossing(machs, cp_mins)
    m_dd_raw = find_hockey_stick_raw(machs, cds)
    m_dd_fit, coeffs, m_dense, cd_fit_dense = find_mdd_fit(machs, cds)

    print(f"\nM_crit (Cp-crossing): {m_crit_cfd}")
    print(f"M_dd (raw 2-consecutive-interval Boeing criterion): {m_dd_raw}  <-- same method as v1, finds nothing here")
    print(f"M_dd (cubic-fit slope crossing, fallback method): {m_dd_fit}")

    result = {
        "points": [{"mach": m, "cd": cd, "cp_min": cp} for m, cd, cp in zip(machs, cds, cp_mins)],
        "M_crit_CFD": m_crit_cfd,
        "M_dd_CFD_raw": m_dd_raw,
        "M_dd_CFD_fit": m_dd_fit,
        "fit_coeffs_desc_order": list(coeffs),
        "fit_curve_for_plot": {"mach": list(m_dense), "cd": list(cd_fit_dense)},
    }
    out_path = HERE / "results_su2_sweep_sc20412_v2.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
