"""Transonic airfoil screen for the OTWEM business jet: NASA SC(2)-0410, NACA 64-209, NASA SC(2)-0610 (closest real SC(2) family member to the requested but nonexistent "SC(2)-0609"), and a custom CST 9%-thick section refit from SC(2)-0410."""

import json
from pathlib import Path

import numpy as np
import aerosandbox as asb

HERE = Path(__file__).parent
DAT_DIR = HERE / "dat"

CL_TARGET = 0.248  # C_li, 2-D cruise design lift coefficient (config.md B.2)
TC_MAX_PREFERRED = 0.09

RE_PRIMARY = 7.5e6  # FL410 initial cruise, M0.80, recomputed from current MAC (config.md B.1/B.2)
RE_ALTERNATE = 15.0e6  # as literally requested in the prompt, run for comparison
MACH = 0.80  # NeuralFoil's mach= arg layers approximate PG/Korn compressibility corrections -- not a real compressible solve


def load_dat_smart(path: Path) -> np.ndarray:
    """Parse a UIUC .dat file in Selig or Lednicer format -- Lednicer's leading "n_upper n_lower" line isn't a coordinate and would otherwise get parsed as a bogus point."""
    lines = [l.strip() for l in path.read_text().splitlines()]
    body = lines[1:]
    data_lines = [l for l in body if l.strip() != ""]
    first_tokens = data_lines[0].split()
    is_lednicer = len(first_tokens) == 2 and all(float(t) > 2.0 for t in first_tokens)

    if not is_lednicer:
        return np.array([[float(x) for x in l.split()] for l in data_lines])

    blocks, current, started = [], [], False
    for l in body:
        if l.strip() == "":
            if current:
                blocks.append(current)
                current = []
            continue
        toks = l.split()
        if len(toks) == 2 and not started:
            started = True
            continue
        current.append([float(x) for x in toks])
    if current:
        blocks.append(current)
    upper, lower = np.array(blocks[0]), np.array(blocks[1])
    # Lednicer blocks both run LE->TE; standard (Selig) order is TE(upper)->LE->TE(lower)
    return np.concatenate([upper[::-1], lower[1:]], axis=0)


def build_candidates() -> dict[str, asb.Airfoil]:
    candidates = {}

    for label, filename in [
        ("NASA SC(2)-0410", "sc20410.dat"),
        ("NACA 64-209", "naca64209.dat"),
        ("NASA SC(2)-0610", "sc20610.dat"),
    ]:
        coords = load_dat_smart(DAT_DIR / filename)
        candidates[label] = asb.Airfoil(name=label, coordinates=coords)

    # Custom CST 9%-thick section: SC(2)-0410 geometry, refit to CST, rescaled to exactly 9% t/c
    base_kulfan = candidates["NASA SC(2)-0410"].to_kulfan_airfoil(n_weights_per_side=8)
    scale_y = TC_MAX_PREFERRED / base_kulfan.max_thickness()
    custom = base_kulfan.scale(scale_x=1.0, scale_y=scale_y)
    custom.name = "Custom CST 9% (SC(2)-0410-derived)"
    candidates[custom.name] = custom

    return candidates


def export_clean_dats(candidates: dict[str, asb.Airfoil], out_dir: Path) -> None:
    """Write single-loop Selig .dat files -- XFOIL chokes on the raw Lednicer point-count header line otherwise."""
    out_dir.mkdir(exist_ok=True)
    slug = {
        "NASA SC(2)-0410": "sc20410",
        "NACA 64-209": "naca64209",
        "NASA SC(2)-0610": "sc20610",
        "Custom CST 9% (SC(2)-0410-derived)": "custom_cst_9pct",
    }
    for name, af in candidates.items():
        filename = slug.get(name, name.replace(" ", "_")) + "_selig.dat"
        af.write_dat(out_dir / filename)
        print(f"  wrote {out_dir / filename}")


def evaluate(airfoil, Re: float, mach: float, cl_target: float) -> dict:
    alphas = np.linspace(-4, 10, 281)  # 0.05 deg resolution
    aero = airfoil.get_aero_from_neuralfoil(alpha=alphas, Re=Re, mach=mach)
    CL, CD, CM = aero["CL"], aero["CD"], aero["CM"]
    mach_crit, mach_dd = aero["mach_crit"], aero["mach_dd"]

    # operating point at the cruise design Cl (interpolate CD/CM/alpha vs CL)
    order = np.argsort(CL)
    CL_s, CD_s, CM_s, alpha_s = CL[order], CD[order], CM[order], alphas[order]
    if not (CL_s[0] <= cl_target <= CL_s[-1]):
        raise ValueError(
            f"{airfoil.name}: Cl_target={cl_target} outside achieved range "
            f"[{CL_s[0]:.3f}, {CL_s[-1]:.3f}] over alpha in [-4, 10] deg"
        )
    alpha_at_target = np.interp(cl_target, CL_s, alpha_s)
    cd_at_target = np.interp(cl_target, CL_s, CD_s)
    cm_at_target = np.interp(cl_target, CL_s, CM_s)

    # drag-bucket floor, for context (may occur at a different Cl than the target)
    i_min_cd = np.argmin(CD)

    # unswept 2D section's own Mcrit/Mdd (NeuralFoil's Laitone/Korn-type estimate) at target-Cl alpha
    aero_at_target = airfoil.get_aero_from_neuralfoil(alpha=float(alpha_at_target), Re=Re, mach=mach)
    mc = float(np.asarray(aero_at_target["mach_crit"]).reshape(-1)[0])
    mdd = float(np.asarray(aero_at_target["mach_dd"]).reshape(-1)[0])
    # sweep needed so that effective Mach (M_inf * cos(sweep)) <= mach_dd, i.e. reach M0.80 unpenalized
    sweep_needed_deg = float(np.degrees(np.arccos(min(mdd / mach, 1.0)))) if mdd < mach else 0.0

    t_over_c = airfoil.max_thickness()

    return {
        "t/c (%)": round(t_over_c * 100, 2),
        "alpha @ Cl_target (deg)": round(float(alpha_at_target), 3),
        "Cd @ Cl_target (counts)": round(float(cd_at_target) * 1e4, 1),
        "Cm @ Cl_target": round(float(cm_at_target), 4),
        "L/D @ Cl_target": round(float(cl_target / cd_at_target), 2),
        "Cd_min (counts)": round(float(CD[i_min_cd]) * 1e4, 1),
        "Cl @ Cd_min": round(float(CL[i_min_cd]), 3),
        "mach_crit (unswept)": round(mc, 3),
        "mach_dd (unswept)": round(mdd, 3),
        "sweep for M_dd=0.80 (deg)": round(sweep_needed_deg, 1),
    }


def main():
    candidates = build_candidates()

    print("Exporting XFOIL-compatible (single-loop Selig format) .dat files:")
    export_clean_dats(candidates, HERE / "dat_clean")

    results = {"Re_primary": RE_PRIMARY, "Re_alternate": RE_ALTERNATE, "mach": MACH, "cl_target": CL_TARGET, "cases": {}}

    for re_label, Re in [("Re=7.5e6 (FL410, recomputed MAC)", RE_PRIMARY), ("Re=15e6 (as originally requested)", RE_ALTERNATE)]:
        print(f"\n=== {re_label}, Mach {MACH} ===")
        header = (
            f"{'Airfoil':32s} {'t/c%':>6s} {'alpha':>7s} {'Cd@Cli':>8s} {'Cm@Cli':>8s} "
            f"{'L/D@Cli':>8s} {'Cd_min':>8s} {'Mcrit':>7s} {'Mdd':>7s} {'sweep*':>7s}"
        )
        print(header)
        print("-" * len(header))
        case_results = {}
        for name, af in candidates.items():
            r = evaluate(af, Re=Re, mach=MACH, cl_target=CL_TARGET)
            case_results[name] = r
            print(
                f"{name:32s} {r['t/c (%)']:6.2f} {r['alpha @ Cl_target (deg)']:7.3f} "
                f"{r['Cd @ Cl_target (counts)']:8.1f} {r['Cm @ Cl_target']:8.4f} "
                f"{r['L/D @ Cl_target']:8.2f} {r['Cd_min (counts)']:8.1f} "
                f"{r['mach_crit (unswept)']:7.3f} {r['mach_dd (unswept)']:7.3f} "
                f"{r['sweep for M_dd=0.80 (deg)']:7.1f}"
            )
        print("* sweep needed (deg) so effective Mach = 0.80*cos(sweep) <= this section's unswept M_dd")
        results["cases"][re_label] = case_results

    out_path = HERE / "results_transonic_screen.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
