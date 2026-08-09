"""
Transonic airfoil screen for the OTWEM business jet, re-run "from scratch" per
2026-08-03 request.

Candidates
----------
1. NASA SC(2)-0410   -- real UIUC coordinates. Current config.md B.1 pick (ASSUMPTION).
2. NACA 64-209        -- real UIUC coordinates. Documented fallback (config.md B.1/B.5).
3. NASA SC(2)-0610    -- real UIUC coordinates. Closest REAL published SC(2) family
                          member to the requested "SC(2)-0609" -- see note below.
4. Custom-CST-9pct    -- SC(2)-0410 refit to an 8-weight-per-side Kulfan/CST
                          parameterization, then scaled in y only to exactly 9.00% t/c.
                          This is a informed custom section, not a from-scratch
                          transonic optimization (no such optimizer is available here) --
                          tag as PLACEHOLDER-grade, same caveat as the prior session's
                          inverse_design.py attempt (see doubts.md #8/#35).

Two corrections vs. the literal request, both verified against the installed
libraries/tools before running (see chat for details):

* "SC(2)-0609" is not a real NASA supercritical airfoil designation. The SC(2)
  family only has t/c values 06/10/14 (etc.) at each camber station -- 09 does not
  exist. Confirmed by a 404 from the UIUC coordinate database. Substituted the real
  SC(2)-0610 (9.98% t/c) as the closest published analog, run alongside the
  already-real SC(2)-0410 (9.97% t/c, already the doc's working pick).

* Reynolds number: requested value was "~15 million based on MAC." Recomputed
  from this project's own current numbers (config.md B.1/B.2, using the
  doubts.md #5-recommended S=193.7 sq ft / AR=8.9 recompute, since the raw
  span/chords in config.md are CONFLICT-tagged):
      b = sqrt(AR*S) = 41.53 ft ; taper=0.35 -> MAC = 5.02 ft
      FL410, M0.80: Re ~= 7.5e6   (ISA, isothermal stratosphere, Sutherland mu)
      FL450, M0.80: Re ~= 6.2e6
  Neither matches 15e6 or the doc's older FL330 figure (10.3e6, now superseded
  per doubts.md #2). Script runs the corrected Re=7.5e6 (FL410, initial cruise)
  as the primary case, and also reports Re=15e6 as a sensitivity/as-requested
  comparison so the discrepancy is visible rather than silently swapped.

Mach handling: aerosandbox's high-level `Airfoil.get_aero_from_neuralfoil(mach=...)`
(NOT the bare `neuralfoil.get_aero_from_airfoil` function, which has no Mach input
at all -- verified by inspecting its NN feature vector) layers a Laitone/Korn-type
critical-Mach estimate, Prandtl-Glauert CL/CM correction, and an empirical wave-drag
CD term on top of the incompressible NeuralFoil network. That's a real, if
approximate, transonic capability, and is what this script uses. It is NOT a
substitute for a compressible panel/CFD method, and should still be treated as
an estimate.
"""

import json
from pathlib import Path

import numpy as np
import aerosandbox as asb

HERE = Path(__file__).parent
DAT_DIR = HERE / "dat"

# ---- design targets, from config.md B.2 ----
CL_TARGET = 0.248  # C_li, 2-D cruise design lift coefficient
TC_MAX_PREFERRED = 0.09

# ---- Reynolds cases ----
RE_PRIMARY = 7.5e6  # FL410 initial cruise, M0.80, recomputed from current MAC (see docstring)
RE_ALTERNATE = 15.0e6  # as literally requested in the prompt, run for comparison
MACH = 0.80


def load_dat_smart(path: Path) -> np.ndarray:
    """Parse a UIUC-style .dat file in either Selig or Lednicer (two-block) format.

    Lednicer files start with an "n_upper n_lower" point-count line, which is
    NOT itself a coordinate -- aerosandbox's raw line-parser doesn't know this and
    will silently ingest it as a bogus (103, 103) point, so this has to be handled
    explicitly rather than passed straight to `asb.Airfoil(coordinates=path)`.
    """
    lines = [l.strip() for l in path.read_text().splitlines()]
    body = lines[1:]  # drop title line
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
            started = True  # this is the point-count header; skip it
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
    """Write single-loop Selig-format .dat files XFOIL (and other tools) can read directly.

    The raw NASA SC(2) downloads in `dat/` are in Lednicer two-block format, with a
    point-count header line ("103. 103.") that isn't a coordinate. XFOIL doesn't
    recognize that format and reads the header as a bogus (103, 103) point, producing
    a spike in the geometry plot. These exports use the same parsed/re-ordered
    coordinates the evaluation already runs on, written out in plain Selig order
    (TE-upper -> LE -> TE-lower, one x y pair per line, no header).
    """
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

    # unswept 2D section's own critical/drag-divergence Mach at the target-Cl alpha
    # (NeuralFoil's internal Laitone/Korn-type estimate -- cross-check vs B.5's hand Korn calc)
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
