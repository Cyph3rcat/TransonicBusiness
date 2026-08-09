"""Raymer-method parasite drag buildup and cruise drag polar for full_v6.

Method: Raymer Ch.12 Eq. (12.24),
    CD0 = sum_c ( Cf_c * FF_c * Q_c * Swet_c ) / Sref  +  CD_misc + CD_L&P

The per-component Cf, FF and Swet come from OpenVSP's ParasiteDrag module
(refs/raymer/ch12_aerodynamics.md documents the same equations), run at the
cruise point on the actual OML rather than off a planform estimate -- that is
the only part of this that is not hand-arithmetic, and it is the part where
using the real lofted geometry is worth something.

Two corrections are applied here because OpenVSP does not:
  Q  -- OpenVSP writes Q = 1.0 for every component. Raymer Ch.12 gives real
        interference factors; the one that matters here is the OTWEM nacelle,
        which sits 0.47 nacelle diameters above the wing, i.e. inside Raymer's
        "less than about one diameter -> Q = 1.3" case.
  L&P -- Raymer's leakage-and-protuberance allowance, 2-5% of CD0 for a jet.

Induced drag comes from the VSPAERO Trefftz-plane (wake) result, which is the
trustworthy induced-drag column for this mixed panel/VLM model -- the
surface-integration CDi column carries a body pressure residual (see the
campaign README's fidelity caveats).

Usage:  python drag_buildup.py
"""
import csv
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PD_CSV = os.path.join(HERE, "final_alpha", "final_alpha_ParasiteBuildUp.csv")
POLAR = os.path.join(HERE, "final_alpha", "final_alpha.polar")

SREF, BREF = 193.678, 41.5324
AR = BREF ** 2 / SREF
MTOW = 11660.0

# Raymer Ch.12 interference factors.
Q_RAYMER = {
    "Fuselage":     (1.00, "Raymer: fuselage Q = 1.0 by definition"),
    "BellyFairing": (1.00, "faired into the fuselage; treated as fuselage"),
    "MainWing":     (1.00, "low wing WITH a belly/root fairing -> Raymer 1.0"),
    "Nacelle":      (1.30, "OTWEM, gap 0.47 nacelle dia -> Raymer 'within ~1 dia' = 1.3"),
    "Pylon":        (1.30, "part of the nacelle installation, same interference field"),
    "VertTail":     (1.05, "Raymer: conventional tail surfaces 1.03-1.08"),
    "HorizTail":    (1.05, "Raymer: conventional tail surfaces 1.03-1.08"),
    "DorsalFin":    (1.05, "treated as a tail surface"),
}
LEAKAGE = 0.03   # Raymer: 2-5% of CD0 for leaks and protuberances on a jet


def read_buildup(path):
    """Top-level component rows only -- OpenVSP repeats each component once per
    symmetric surface (Nacelle, Nacelle_0, Nacelle_1) and the un-suffixed row is
    already the total."""
    rows = []
    with open(path) as fh:
        for line in fh:
            p = [x.strip() for x in line.split(",")]
            if len(p) < 12 or p[0] in ("Component Name", "") or "_" in p[0]:
                continue
            try:
                # cols: 0 name, 1 Swet, 2 Lref, 3 t/c, 4 FF, 5 FF eqn, 6 Re,
                #       7 %Lam, 8 Cf, 9 Q, 10 f, 11 Cd, 12 %total
                rows.append(dict(name=p[0], swet=float(p[1]), lref=float(p[2]),
                                 toc=float(p[3]), ff=float(p[4]),
                                 cf=float(p[8]), f=float(p[10])))
            except ValueError:
                continue
    return rows


def read_polar(path):
    hdr, rows = None, []
    for line in open(path):
        s = line.strip()
        if not s or s.startswith(("Surface", "Surf-")):
            continue
        if s.startswith("Beta "):
            hdr = s.split()
            continue
        rows.append([float(x) for x in s.split()])
    c = {n: i for i, n in enumerate(hdr)}
    return c, np.array(rows)


def main():
    rows = read_buildup(PD_CSV)
    print("Parasite drag buildup -- full_v6, FL410 / M0.80 / ISA, fully turbulent")
    print(f"  Sref = {SREF} ft^2 ; Cf: compressible Schlichting ; FF: Hoerner\n")
    print(f"{'component':14s} {'Swet':>8} {'Cf':>8} {'FF':>6} {'Q':>5} "
          f"{'f=CfFFQSwet':>12} {'CD0_c':>9} {'%':>6}")
    tot_f = 0.0
    parts = []
    for r in rows:
        q, _ = Q_RAYMER.get(r["name"], (1.0, "default"))
        f = r["cf"] * r["ff"] * q * r["swet"]
        tot_f += f
        parts.append((r["name"], r["swet"], f))
    for (name, swet, f), r in zip(parts, rows):
        q, _ = Q_RAYMER.get(name, (1.0, ""))
        print(f"{name:14s} {swet:8.1f} {r['cf']:8.5f} {r['ff']:6.3f} {q:5.2f} "
              f"{f:12.4f} {f / SREF:9.5f} {100 * f / tot_f:6.1f}")
    cd0_geom = tot_f / SREF
    cd0 = cd0_geom * (1 + LEAKAGE)
    swet_tot = sum(p[1] for p in parts)
    print(f"\n  sum f              = {tot_f:.4f} ft^2")
    print(f"  CD0 (geometry)     = {cd0_geom:.5f}   ({cd0_geom * 1e4:.1f} counts)")
    print(f"  + leakage/protub.  = {LEAKAGE * 100:.0f}%  -> "
          f"CD0 = {cd0:.5f}  ({cd0 * 1e4:.1f} counts)")
    print(f"  total wetted area  = {swet_tot:.1f} ft^2   "
          f"Swet/Sref = {swet_tot / SREF:.2f}")
    print(f"  wetted aspect ratio = b^2/Swet = {BREF ** 2 / swet_tot:.3f}")

    # ---- induced drag from the Trefftz plane ------------------------------
    # NORMALIZATION (fixed 2026-08-07): fit the Trefftz-plane induced drag
    # CDiw against the Trefftz-plane lift CLwtot, NOT against the
    # surface-integration lift CLtot. The two are different quantities: panel
    # BODIES carry pressure lift that never sheds a trailing wake sheet, so it
    # appears in CLtot but legitimately not in CLwtot (the gap is ~4% on v6 and
    # ~9% on v7, whose belly fairing is larger -- physical, not a defect).
    # Fitting wake drag against surface lift mixed the two and produced
    # nonsense: e = 1.03 (v6) / 1.16 (v7), and a spurious 30% "improvement"
    # from v6 to v7 that was pure normalization artifact. Fitted consistently,
    # e = 0.96 / 0.99 and is flat across the alpha sweep, as it should be.
    c, d = read_polar(POLAR)
    clw, cdiw = d[:, c["CLwtot"]], d[:, c["CDiw"]]
    m = clw > 0.05
    k = np.polyfit(clw[m] ** 2, cdiw[m], 1)[0]    # CDiw = k * CLw^2
    e_eff = 1.0 / (math.pi * AR * k)
    print(f"\n  induced: CDi = {k:.5f}*CL^2  ->  e = {e_eff:.3f} (AR {AR:.2f}, "
          f"winglets on, wake/Trefftz)")

    # ---- cruise polar --------------------------------------------------
    # config.md Part A: "Cruise altitude: FL410 initial, cruise-climb to
    # FL450" is already GROUNDED -- but this script previously held FL410
    # constant for the whole leg, silently ignoring that decision and
    # understating mid/end-cruise L/D. Fixed here: fly the documented
    # cruise-climb, MTOW at FL410 climbing to FL450 as fuel burns.
    # Above the 36,089 ft tropopause T is isothermal (216.65 K), so TAS is
    # flat with altitude at fixed Mach (V=774.5 ft/s throughout) and only
    # rho varies -- isothermal-layer barometric formula, scale height
    # H = RT/g = 20,805.8 ft, anchored at the tropopause (rho=7.065e-4).
    vinf = 774.5
    RHO_TROP, H_TROP, SCALE_H = 7.065e-4, 36089.0, 20805.8

    def isa_rho(h_ft):
        return RHO_TROP * math.exp(-(h_ft - H_TROP) / SCALE_H)

    print(f"\n  cruise-climb profile: FL410 -> FL450 (config.md Part A, GROUNDED), "
          f"M0.80 throughout (V={vinf:.1f} ft/s, const. above tropopause)")
    print(f"\n{'state':22s} {'FL':>5} {'W (lb)':>8} {'q (psf)':>8} {'CL':>7} "
          f"{'CD0':>8} {'CDi':>8} {'CD':>8} {'L/D':>7}")
    for tag, w, fl in (("MTOW, start cruise", MTOW, 410),
                        ("mid-cruise (0.93)", 0.93 * MTOW, 430),
                        ("end cruise (0.86)", 0.86 * MTOW, 450)):
        rho = isa_rho(fl * 100.0)
        q_dyn = 0.5 * rho * vinf ** 2
        cl_c = w / SREF / q_dyn
        cdi = k * cl_c ** 2
        cd = cd0 + cdi
        print(f"{tag:22s} {fl:5d} {w:8.0f} {q_dyn:8.1f} {cl_c:7.4f} {cd0:8.5f} "
              f"{cdi:8.5f} {cd:8.5f} {cl_c / cd:7.2f}")
    print(f"\n  NOTE: CL stays well below CL_opt (see below) even at FL450 -- "
          f"closing that gap needs either a smaller wing or a higher service\n"
          f"  ceiling, neither of which is checked against real engine thrust "
          f"data in this project. Flagged in doubts.md/limitations.md, not\n"
          f"  resolved here.")
    q_dyn = 0.5 * isa_rho(41000.0) * vinf ** 2  # FL410, for the L/D_max/K_LD print below
    # L/D_max and the CL that achieves it
    cl_opt = math.sqrt(cd0 / k)
    print(f"\n  L/D_max = {cl_opt / (2 * cd0):.2f} at CL = {cl_opt:.3f} "
          f"(= {cl_opt * q_dyn * SREF:.0f} lb at FL410/M0.80)")
    print(f"  Raymer L/D_max check: 'L/D_max = K_LD * sqrt(AR_wet)', "
          f"AR_wet = {BREF ** 2 / swet_tot:.2f} -> K_LD implied = "
          f"{(cl_opt / (2 * cd0)) / math.sqrt(BREF ** 2 / swet_tot):.2f} "
          f"(Raymer gives 15.5 for a civil jet)")
    print("\n  NOT included: wave drag. At M0.80 the design sits AT the 2-D "
          "M_dd=0.777 swept to 0.80 (config.md B.5.3), so a wave-drag increment "
          "of order 10-20 counts is expected and is exactly what the staged SU2 "
          "Euler pass is for. Treat the L/D above as the pre-wave-drag value.")


if __name__ == "__main__":
    main()
