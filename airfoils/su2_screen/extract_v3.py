"""
Constant-CL extraction of M_crit / M_dd from the v3 sweep (24 runs: 8 Mach
stations x 3 AoA, JST, cold starts, windowed CD/CL statistics).

Per Mach station: linearly interpolate CD, CD_std, and Cp_min to the design
CL = 0.248 between the two bracketing AoA runs. Then:
  - M_crit: first crossing of the constant-CL Cp_min(M) curve with the
    isentropic critical Cp_cr(M) curve.
  - M_dd, two independent standard definitions (agreement = defensibility):
      (a) "Boeing criterion": dCD/dM >= 0.10 on the constant-CL curve.
      (b) delta-CD criterion: CD rises 20 counts above the subcritical
          baseline (mean of the M <= 0.70 stations).
Both are evaluated on a monotone piecewise-linear interpolation of the
station values; error bars come from the windowed std of each run,
interpolated the same way as the means.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from critical_cp import cp_critical

GAMMA = 1.4
HERE = Path(__file__).parent / "mach_sweep_sc20412_v3"
CL_TARGET = 0.248
DCD_DM_THRESHOLD = 0.10
DELTA_CD_COUNTS = 20.0
BASELINE_MACH_MAX = 0.70


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


def interp_at_cl(runs, key):
    """Linear interpolation of runs[i][key] to CL_TARGET using cl_mean as the
    abscissa. Picks the bracketing pair; falls back to the nearest two."""
    pts = sorted(runs, key=lambda r: r["cl_mean"])
    lo, hi = None, None
    for a, b in zip(pts, pts[1:]):
        if a["cl_mean"] <= CL_TARGET <= b["cl_mean"]:
            lo, hi = a, b
            break
    if lo is None:
        lo, hi = (pts[0], pts[1]) if CL_TARGET < pts[0]["cl_mean"] else (pts[-2], pts[-1])
    t = (CL_TARGET - lo["cl_mean"]) / (hi["cl_mean"] - lo["cl_mean"])
    return lo[key] + t * (hi[key] - lo[key]), (lo["cl_mean"], hi["cl_mean"])


def find_crossing(machs, values, thresholds):
    """First M where values[i] <= thresholds[i] (linear interp inside interval)."""
    res = [v - t for v, t in zip(values, thresholds)]
    for i in range(len(machs) - 1):
        if res[i] > 0 and res[i + 1] <= 0:
            frac = res[i] / (res[i] - res[i + 1])
            return machs[i] + frac * (machs[i + 1] - machs[i])
    return None


def main():
    with open(HERE / "sweep_v3_raw.json") as f:
        runs = json.load(f)

    for r in runs:
        r["cp_min"] = cp_min_from_surface_csv(
            HERE / f"surface_{r['tag']}.csv", r["p_inf"], r["rho_inf"], r["v_inf"])

    by_mach = {}
    for r in runs:
        by_mach.setdefault(r["mach"], []).append(r)

    stations = []
    print(f"{'M':>6} {'CD@CL=.248':>12} {'+/-':>8} {'Cp_min@CL':>10} {'Cp_cr(M)':>9} {'CL bracket':>18}")
    for mach in sorted(by_mach):
        cd, bracket = interp_at_cl(by_mach[mach], "cd_mean")
        cd_std, _ = interp_at_cl(by_mach[mach], "cd_std")
        cpmin, _ = interp_at_cl(by_mach[mach], "cp_min")
        stations.append({"mach": mach, "cd": cd, "cd_std": cd_std, "cp_min": cpmin,
                          "cl_bracket": bracket})
        print(f"{mach:6.2f} {cd*1e4:10.1f} ct {cd_std*1e4:6.1f} ct {cpmin:10.4f} "
              f"{cp_critical(mach):9.4f}  [{bracket[0]:.3f}, {bracket[1]:.3f}]")

    machs = [s["mach"] for s in stations]
    cds = [s["cd"] for s in stations]
    cp_mins = [s["cp_min"] for s in stations]

    # M_crit: Cp_min crosses Cp_cr. find_crossing wants res = value - threshold
    # to start positive and go negative: cp_min - cp_cr is positive while still
    # subcritical (cp_min less negative than cp_cr) and negative once critical.
    m_crit = find_crossing(machs, cp_mins, [cp_critical(m) for m in machs])

    # M_dd (a): Boeing dCD/dM >= 0.10 -- slope on successive intervals, linear
    # interpolation in slope to the threshold inside the first qualifying interval
    m_dd_boeing = None
    slopes = [(cds[i + 1] - cds[i]) / (machs[i + 1] - machs[i]) for i in range(len(machs) - 1)]
    for i, s in enumerate(slopes):
        if s >= DCD_DM_THRESHOLD:
            if i == 0:
                m_dd_boeing = machs[0]
            else:
                prev = slopes[i - 1]
                frac = (DCD_DM_THRESHOLD - prev) / (s - prev)
                # slope belongs to interval midpoints; interpolate between midpoints
                mid_prev = 0.5 * (machs[i - 1] + machs[i])
                mid_this = 0.5 * (machs[i] + machs[i + 1])
                m_dd_boeing = mid_prev + frac * (mid_this - mid_prev)
            break

    # M_dd (b): CD exceeds subcritical baseline + 20 counts
    baseline = sum(c for m, c in zip(machs, cds) if m <= BASELINE_MACH_MAX) / \
        sum(1 for m in machs if m <= BASELINE_MACH_MAX)
    thresh = baseline + DELTA_CD_COUNTS / 1e4
    m_dd_delta = find_crossing(machs, [-c for c in cds], [-thresh] * len(machs))

    print(f"\nSubcritical baseline CD (M<= {BASELINE_MACH_MAX}): {baseline*1e4:.1f} counts")
    print(f"M_crit (Cp-crossing, constant CL): {m_crit}")
    print(f"M_dd (Boeing dCd/dM>=0.10):        {m_dd_boeing}")
    print(f"M_dd (baseline + 20 counts):       {m_dd_delta}")

    out = {
        "cl_target": CL_TARGET,
        "stations": stations,
        "baseline_cd": baseline,
        "M_crit_CFD": m_crit,
        "M_dd_boeing": m_dd_boeing,
        "M_dd_delta20": m_dd_delta,
    }
    out_path = HERE / "results_v3.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
