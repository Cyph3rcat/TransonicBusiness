"""Extract M_crit (Cp-crossing) and M_dd (Cd hockey-stick) from the SC(2)-0412 adaptive sweep -- SU2's SURFACE_CSV has no Cp column for a MARKER_HEATFLUX wall, so Cp is recovered from the raw conservative variables via the ideal-gas relation."""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from critical_cp import cp_critical

GAMMA = 1.4
HERE = Path(__file__).parent / "mach_sweep_sc20412"


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
    """First Mach where CFD Cp_min(M) <= the isentropic critical Cp_cr(M)."""
    residuals = [cp_mins[i] - cp_critical(machs[i]) for i in range(len(machs))]
    for i in range(len(machs) - 1):
        if residuals[i] > 0 and residuals[i + 1] <= 0:
            frac = residuals[i] / (residuals[i] - residuals[i + 1])
            return machs[i] + frac * (machs[i + 1] - machs[i])
    return None


DCD_DM_THRESHOLD = 0.10  # "Boeing criterion" for drag-divergence Mach, absolute dCd/dM
CONSECUTIVE_NEEDED = 2  # must match adaptive_sweep.py's live stopping criterion exactly


def find_hockey_stick(machs, cds):
    """Mach at the start of the first run of CONSECUTIVE_NEEDED consecutive dCd/dM>=threshold intervals -- must match adaptive_sweep.py's live stop logic exactly, since single-interval blips (like the 0.6222->0.6522 jump here) can be false starts."""
    slopes = [(cds[i + 1] - cds[i]) / (machs[i + 1] - machs[i]) for i in range(len(machs) - 1)]
    run = 0
    for i, slope in enumerate(slopes):
        run = run + 1 if slope >= DCD_DM_THRESHOLD else 0
        if run >= CONSECUTIVE_NEEDED:
            return machs[i - CONSECUTIVE_NEEDED + 1]
    return None


def main():
    with open(HERE / "adaptive_sweep_results.json") as f:
        points = json.load(f)

    machs = [p["mach"] for p in points]
    cds = [p["cd"] for p in points]

    cp_mins = []
    for p in points:
        surf_path = HERE / f"surface_{p['tag']}.csv"
        cpmin = cp_min_from_surface_csv(surf_path, p["p_inf"], p["rho_inf"], p["v_inf"])
        cp_mins.append(cpmin)
        print(f"M={p['mach']:.4f}  CD={p['cd']:.5f}  Cp_min={cpmin:.4f}  Cp_cr={cp_critical(p['mach']):.4f}")

    m_crit_cfd = find_cp_crossing(machs, cp_mins)
    m_dd_cfd = find_hockey_stick(machs, cds)

    print(f"\nM_crit (Cp-crossing): {m_crit_cfd}")
    print(f"M_dd (Cd hockey-stick): {m_dd_cfd}")

    result = {
        "points": [{"mach": m, "cd": cd, "cp_min": cp} for m, cd, cp in zip(machs, cds, cp_mins)],
        "M_crit_CFD": m_crit_cfd,
        "M_dd_CFD": m_dd_cfd,
    }
    out_path = HERE / "results_su2_sweep_sc20412.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
