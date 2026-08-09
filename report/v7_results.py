"""Consolidate the full_v7 VSPAERO results into the numbers the report quotes.

Everything here is read out of the run directories in
`openvsp/vspaero_runs/11_full_v7/`; nothing is retyped by hand. Run from
anywhere:

    python report/v7_results.py

Outputs, in order:
  1. the neutral-point-vs-S_HT parametric fit (four alpha sweeps at fixed wing
     position), which is what sizes the horizontal tail,
  2. longitudinal slopes for the final configuration,
  3. lateral/directional slopes for the final configuration, with the symmetry
     noise floor reported so the reader can see Cn_beta is actually resolved,
  4. the Class-I CG envelope at the final geometry.

Sign conventions follow VSPAERO's .stab files: CMl = -CMx, CMn = -CMz.
"""
import json
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "..", "openvsp", "vspaero_runs", "11_full_v7")

# ---------------------------------------------------------------- v7 geometry
SREF, BREF, CREF = 193.678, 41.5324, 5.0236
S_HT, S_VT = 29.10, 43.20           # final_alpha/build_run.vspscript header
X_WING_LE = 14.3464                 # ditto
XCG_SOLVE = 18.911                  # moment reference used in the final run
XCG_SWEEP = 19.900                  # moment reference used in the S_HT sweep


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
    return {n: i for i, n in enumerate(hdr)}, np.array(rows)


def longitudinal(path, xcg):
    """CL_alpha, dCm/dCL, neutral point from a real alpha sweep.

    Preferred over VSPAERO's `-stab` finite difference, which perturbs by
    0.01 deg and so differences the moment coefficients at the same order as
    the solve's own residual noise (config.md D.5b).
    """
    c, d = read_polar(path)
    a = np.deg2rad(d[:, c["AoA"]])
    cl, cm, cd = d[:, c["CLtot"]], d[:, c["CMytot"]], d[:, c["CDtot"]]
    (cla, _), (cma, _) = np.polyfit(a, cl, 1), np.polyfit(a, cm, 1)
    fit = np.polyfit(cl, cm, 1)
    r2 = 1 - np.sum((cm - np.polyval(fit, cl)) ** 2) / np.sum((cm - cm.mean()) ** 2)
    sm = -fit[0]
    return dict(cla=cla, cma=cma, dcmdcl=fit[0], sm=sm, r2=r2,
                x_np=xcg + sm * CREF, cl=cl, cd=cd, aoa=d[:, c["AoA"]])


def lateral(path):
    c, d = read_polar(path)
    b = np.deg2rad(d[:, c["Beta"]])
    cmx, cmz, cy = d[:, c["CMxtot"]], d[:, c["CMztot"]], d[:, c["CStot"]]
    noise = abs(cmz[0])                      # must be 0 by symmetry at beta=0
    span = abs(cmz[-1] - cmz[0])
    return dict(cyb=np.polyfit(b, cy, 1)[0],
                clb=-np.polyfit(b, cmx, 1)[0],
                cnb=-np.polyfit(b, cmz, 1)[0],
                noise=noise, span=span, snr=span / noise)


# ------------------------------------------------------- 1. the NP parametric
print("=" * 74)
print("1. Neutral point vs horizontal tail area  (alpha sweeps, wing pinned)")
print("=" * 74)
print(f"{'S_HT ft2':>9} {'CL_alpha':>9} {'dCm/dCL':>9} {'x_np ft':>9} {'R^2':>7}")
areas, nps = [], []
for s in (30.0, 38.0, 46.0, 54.0):
    p = os.path.join(RUNS, f"ht{s}", f"ht{s}.polar")
    r = longitudinal(p, XCG_SWEEP)
    areas.append(s)
    nps.append(r["x_np"])
    print(f"{s:9.1f} {r['cla']:9.3f} {r['dcmdcl']:9.4f} {r['x_np']:9.3f} {r['r2']:7.4f}")

A, B = np.polyfit(areas, nps, 1)[::-1]       # x_np = A + B * S_HT
pred = A + B * np.array(areas)
fit_r2 = 1 - np.sum((np.array(nps) - pred) ** 2) / np.sum((np.array(nps) - np.mean(nps)) ** 2)
print(f"\n  fit: x_np = {A:.4f} + {B:.5f} * S_HT   (ft, R^2 = {fit_r2:.5f})")
print(f"  tail-off intercept x_np(S_HT=0) = {A:.3f} ft")

# ------------------------------------------------------ 2/3. final config
print("\n" + "=" * 74)
print(f"2. Final configuration  (S_HT={S_HT} ft2, S_VT={S_VT} ft2, wing LE={X_WING_LE} ft)")
print("=" * 74)
fa = longitudinal(os.path.join(RUNS, "final_alpha", "final_alpha.polar"), XCG_SOLVE)
print(f"  CL_alpha        = {fa['cla']:.3f} /rad  ({fa['cla'] * math.pi / 180:.4f} /deg)")
print(f"  dCm/dCL         = {fa['dcmdcl']:+.4f}   (R^2 = {fa['r2']:.4f})")
print(f"  static margin   = {100 * fa['sm']:.1f} % MAC at the solve CG x={XCG_SOLVE} ft")
print(f"  neutral point   = {fa['x_np']:.3f} ft")

lb = lateral(os.path.join(RUNS, "final_beta", "final_beta.polar"))
print(f"\n  CY_beta         = {lb['cyb']:+.4f} /rad")
print(f"  Cl_beta         = {lb['clb']:+.4f} /rad   (normal band -0.05 .. -0.20)")
print(f"  Cn_beta         = {lb['cnb']:+.4f} /rad   (must be > 0)")
print(f"  symmetry noise  = {lb['noise']:.2e} (|CMz| at beta=0), signal {lb['span']:.2e}"
      f"  ->  S/N = {lb['snr']:.1f}")

# ------------------------------------------------------------- 4. CG envelope
print("\n" + "=" * 74)
print("4. Class-I CG envelope at the final geometry")
print("=" * 74)
MTOW, W_E_FRAC, W_F_FRAC = 11660.0, 0.59, 0.2634
W_E, W_FUEL = W_E_FRAC * MTOW, W_F_FRAC * MTOW
S_HT_REF, S_VT_REF, X_WING_REF = 51.68, 59.00, 19.00
AR_HT, TAPER_HT, SWEEP25_HT = 4.4706, 0.4783, 20.0
AR_VT, TAPER_VT, SWEEP25_VT = 1.0659, 0.6052, 35.0
X_VT_ROOT, Z_VT_ROOT = 31.6, 2.0
CR_W, CT_W, SEMISPAN_W, SWEEP25_W = 6.9086, 2.4180, 20.7662, 18.5


def panel(area, ar, taper, one_sided):
    b = math.sqrt(ar * area)
    cr = 2.0 * area / (b * (1.0 + taper))
    mac = (2.0 / 3.0) * cr * (1 + taper + taper ** 2) / (1 + taper)
    span_to_root = b if one_sided else b / 2.0
    y_mac = (span_to_root / 3.0) * (1 + 2 * taper) / (1 + taper)
    return dict(S=area, b=b, cr=cr, ct=taper * cr, mac=mac, y_mac=y_mac,
                span_to_root=span_to_root)


def le_sweep(cr, taper, span_to_root, sweep25):
    return math.atan(math.tan(math.radians(sweep25))
                     + 0.25 * cr * (1 - taper) / span_to_root)


taper_w = CT_W / CR_W
MAC_W = (2.0 / 3.0) * CR_W * (1 + taper_w + taper_w ** 2) / (1 + taper_w)
YMAC_W = (SEMISPAN_W / 3.0) * (1 + 2 * taper_w) / (1 + taper_w)
X_C4_W = X_WING_LE + 0.25 * CR_W + YMAC_W * math.tan(math.radians(SWEEP25_W))
X_LEMAC = X_C4_W - 0.25 * MAC_W

vt = panel(S_VT, AR_VT, TAPER_VT, True)
vt_le = le_sweep(vt["cr"], TAPER_VT, vt["b"], SWEEP25_VT)
vt["x_lemac"] = X_VT_ROOT + vt["y_mac"] * math.tan(vt_le)
ht = panel(S_HT, AR_HT, TAPER_HT, False)
ht["x_root_le"] = X_VT_ROOT + vt["b"] * math.tan(vt_le)
ht_le = le_sweep(ht["cr"], TAPER_HT, ht["b"] / 2.0, SWEEP25_HT)
ht["x_lemac"] = ht["x_root_le"] + ht["y_mac"] * math.tan(ht_le)
ht["x_c4"] = ht["x_root_le"] + 0.25 * ht["cr"] + ht["y_mac"] * math.tan(math.radians(SWEEP25_HT))
vt["x_c4"] = X_VT_ROOT + 0.25 * vt["cr"] + vt["y_mac"] * math.tan(math.radians(SWEEP25_VT))

L_HT, L_VT = ht["x_c4"] - X_C4_W, vt["x_c4"] - X_C4_W
print(f"  MAC = {MAC_W:.4f} ft, X_LEMAC = {X_LEMAC:.3f} ft, quarter-MAC = {X_C4_W:.3f} ft")
print(f"  L_HT = {L_HT:.3f} ft -> c_HT = {S_HT * L_HT / (SREF * MAC_W):.4f}")
print(f"  L_VT = {L_VT:.3f} ft -> c_VT = {S_VT * L_VT / (SREF * BREF):.4f}")

dx = X_WING_LE - X_WING_REF
groups = [("Wing", 0.095 * MTOW, 23.62 + dx),
          ("Horizontal tail", 0.009 * MTOW * S_HT / S_HT_REF, ht["x_lemac"] + 0.40 * ht["mac"]),
          ("Vertical tail+dorsal", 0.012 * MTOW * S_VT / S_VT_REF, vt["x_lemac"] + 0.40 * vt["mac"]),
          ("Fuselage", 0.102 * MTOW, 19.00),
          ("Nacelles+pylons", 0.016 * MTOW, 28.50 + dx),
          ("Nose gear", 0.009 * MTOW, 6.50),
          ("Main gear", 0.035 * MTOW, 24.80 + dx),
          ("Engines installed", 2 * 520 * 1.25, 28.40 + dx)]
w_fixed = W_E - sum(g[1] for g in groups)
groups += [("Avionics (nose)", 0.16 * w_fixed, 5.50),
           ("Furnishings", 0.42 * w_fixed, 16.90),
           ("Systems (aft-mid)", 0.42 * w_fixed, 21.50)]
crew, pax, bag = ("Crew", 400.0, 7.50), ("Pax", 1080.0, 17.00), ("Baggage", 240.0, 25.00)
fuel = ("Fuel", W_FUEL, 23.62 + dx)


def cg(items):
    w = sum(i[1] for i in items)
    return w, sum(i[1] * i[2] for i in items) / w


states = [("Empty (not a flight state)", groups),
          ("OEW (empty + crew)", groups + [crew]),
          ("Zero-fuel (crew+payload)", groups + [crew, pax, bag]),
          ("MTOW", groups + [crew, pax, bag, fuel]),
          ("OEW + full fuel (ferry)", groups + [crew, fuel])]
x_np = fa["x_np"]
print(f"\n{'state':28} {'W lb':>8} {'Xcg ft':>8} {'%MAC':>7} {'SM %':>7}")
env = []
for name, items in states:
    w, x = cg(items)
    pct = (x - X_LEMAC) / MAC_W * 100
    sm = (x_np - x) / MAC_W * 100
    env.append((name, w, x, pct, sm))
    print(f"{name:28} {w:8.0f} {x:8.3f} {pct:7.1f} {sm:7.1f}")

flight = [e for e in env if not e[0].startswith("Empty")]
print(f"\n  flight CG band {min(e[3] for e in flight):.1f} - {max(e[3] for e in flight):.1f} % MAC"
      f"  ({max(e[3] for e in flight) - min(e[3] for e in flight):.1f} % MAC wide)")
print(f"  neutral point  {x_np:.3f} ft = {(x_np - X_LEMAC) / MAC_W * 100:.1f} % MAC")

json.dump(dict(np_fit=[A, B], np_fit_r2=fit_r2, S_HT=S_HT, S_VT=S_VT,
               c_HT=S_HT * L_HT / (SREF * MAC_W), c_VT=S_VT * L_VT / (SREF * BREF),
               L_HT=L_HT, L_VT=L_VT, MAC=MAC_W, X_LEMAC=X_LEMAC, x_np=x_np,
               CL_alpha=fa["cla"], SM_mtow=None,
               Cn_beta=lb["cnb"], Cl_beta=lb["clb"], CY_beta=lb["cyb"], snr=lb["snr"],
               envelope=[dict(state=e[0], W=e[1], xcg=e[2], pct_mac=e[3], sm=e[4]) for e in env]),
          open(os.path.join(HERE, "v7_results.json"), "w"), indent=2)
print(f"\nwritten: {os.path.join(HERE, 'v7_results.json')}")
