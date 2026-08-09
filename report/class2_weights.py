"""Chapter 8 -- Class-II weight estimate (Raymer GA set, Eqs 15.46-15.59, used because this aircraft is below the transport-equation fit population) and loading-sequence CG envelope."""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ============================================================ design condition
MTOW = 11660.0                 # lb, config.md A.3
MLW = 0.93 * MTOW              # lb, config.md B.2
W_FUEL = 0.2634 * MTOW         # lb, config.md A.3
MACH = 0.80
Q_CRUISE = 167.3               # psf, FL410 M0.80 (report/drag summary, ISA)

# FAR 25.337 limit manoeuvring load factor
n_lim = min(max(2.1 + 24000.0 / (MTOW + 10000.0), 2.5), 3.8)
NZ = 1.5 * n_lim               # ultimate load factor
N_GEAR = 3.0                   # Raymer Table 11.5, commercial
NL = 1.5 * N_GEAR              # ultimate landing load factor

# ================================================================== geometry
# Wing (config.md B.1/B.2, full_v7)
SW, AR_W, SWEEP_W, TAPER_W, TC_W, BW = 193.678, 8.9095, 18.5, 0.35, 0.12, 41.5324
# Horizontal tail (config.md D.7 / full_v7 final)
SHT, AR_HT, SWEEP_HT, TAPER_HT, TC_HT = 29.10, 4.4706, 20.0, 0.4783, 0.10
# Vertical tail (T-tail, so Ht/Hv = 1.0)
SVT, AR_VT, SWEEP_VT, TAPER_VT, TC_VT, HT_HV = 43.20, 1.0659, 35.0, 0.6052, 0.10, 1.0
# Fuselage: wetted areas from final_alpha_ParasiteBuildUp.csv; belly fairing included as primary structure (carries wing centre section & gear bays), not a bolted-on fairing.
S_FUSE, S_FAIRING = 534.556, 121.717
SF = S_FUSE + S_FAIRING
L_STRUCT = 39.0                # ft, 42.2 total less radome and tail cap
D_FUSE = 6.10                  # ft, structural depth
LT = 19.923                    # ft, wing quarter-MAC to HT quarter-MAC (v7_results)
V_PRESS = 380.0                # ft^3, pressurised cabin volume (fuselage.md 4/5)
P_DELTA = 8.6                  # psi, cabin differential for a FL450 ceiling

# Gear (Chapter 7)
L_M, L_N = 30.0, 32.0          # in, extended gear lengths (ASSUMPTION)
# Propulsion
N_EN, W_EN = 2, 520.0          # FJ44-3A-24 dry weight, EASA TCDS IM.E.016
V_T, V_I, N_TANK = 488.0, 460.0, 3      # gal total / integral, tank count (fuselage.md 10)
W_FW = 0.95 * W_FUEL           # lb of fuel carried in the wing
# Systems
N_FUNC, K_H, W_UAV, N_PERS = 5, 0.11, 300.0, 8

print("=" * 78)
print("CHAPTER 8  REFINED (CLASS-II) WEIGHT ESTIMATE -- Raymer Eqs. (15.46)-(15.59)")
print("=" * 78)
print(f"  design gross weight W_dg = {MTOW:.0f} lb")
print(f"  FAR 25.337: n_limit = 2.1 + 24000/(W+10000) = {n_lim:.3f}"
      f"  ->  N_z = 1.5 n = {NZ:.3f}")
print(f"  N_l = 1.5 N_gear = {NL:.2f} ; landing weight W_l = {MLW:.0f} lb")
print(f"  cruise dynamic pressure q = {Q_CRUISE:.1f} psf, M = {MACH}")


def cosd(x):
    return math.cos(math.radians(x))


NZW = NZ * MTOW

# ------------------------------------------------------------ (15.46) wing
W_wing = (0.036 * SW ** 0.758 * W_FW ** 0.0035
          * (AR_W / cosd(SWEEP_W) ** 2) ** 0.6
          * Q_CRUISE ** 0.006 * TAPER_W ** 0.04
          * (100 * TC_W / cosd(SWEEP_W)) ** -0.3
          * (NZW) ** 0.49)

# ------------------------------------------------- (15.47) horizontal tail
W_ht = (0.016 * (NZW) ** 0.414 * Q_CRUISE ** 0.168 * SHT ** 0.896
        * (100 * TC_HT / cosd(SWEEP_HT)) ** -0.12
        * (AR_HT / cosd(SWEEP_HT) ** 2) ** 0.043 * TAPER_HT ** -0.02)

# --------------------------------------------------- (15.48) vertical tail
tvt = max(TAPER_VT, 0.2)       # Raymer: if lambda_vt < 0.2 use 0.2
W_vt = (0.073 * (1 + 0.2 * HT_HV) * (NZW) ** 0.376 * Q_CRUISE ** 0.122
        * SVT ** 0.873 * (100 * TC_VT / cosd(SWEEP_VT)) ** -0.49
        * (AR_VT / cosd(SWEEP_VT) ** 2) ** 0.357 * tvt ** 0.039)

# -------------------------------------------------------- (15.49) fuselage
W_press = 11.9 * (V_PRESS * P_DELTA) ** 0.271
W_fuse = (0.052 * SF ** 1.086 * (NZW) ** 0.177 * LT ** -0.051
          * (L_STRUCT / D_FUSE) ** -0.072 * Q_CRUISE ** 0.241 + W_press)

# ---------------------------------------------------- (15.50/51) landing gear
W_mlg = 0.095 * (NL * MLW) ** 0.768 * (L_M / 12.0) ** 0.409
W_nlg = 0.125 * (NL * MLW) ** 0.566 * (L_N / 12.0) ** 0.845

# ------------------------------------------------ (15.52) installed engines
W_eng_inst = 2.575 * W_EN ** 0.922 * N_EN

# ----------------------------------------------------- (15.53) fuel system
W_fuelsys = (2.49 * V_T ** 0.726 * (1.0 / (1.0 + V_I / V_T)) ** 0.363
             * N_TANK ** 0.242 * N_EN ** 0.157)

# -------------------------------------------------- (15.54) flight controls
W_fc = 0.053 * L_STRUCT ** 1.536 * BW ** 0.371 * (NZW * 1e-4) ** 0.80

# ------------------------------------------------------- (15.55) hydraulics
W_hyd = K_H * MTOW ** 0.8 * MACH ** 0.5

# --------------------------------------------------- (15.57) avionics first
W_avionics = 2.117 * W_UAV ** 0.933
# -------------------------------------------------------- (15.56) electrical
W_elec = 12.57 * (W_fuelsys + W_avionics) ** 0.51
# ------------------------------------------------------- (15.58) ECS/anti-ice
W_ac = 0.265 * MTOW ** 0.52 * N_PERS ** 0.68 * W_avionics ** 0.17 * MACH ** 0.08
# ----------------------------------------------------- (15.59) furnishings
W_furn = 0.0582 * MTOW - 65.0

# Arms, ft aft of the nose; wing/fuel arms use the 40% MAC convention carried from weight.md 3.
X_LEMAC, MAC = 17.734, 5.0237
groups = [
    ("Wing",                 W_wing,     X_LEMAC + 0.40 * MAC, "15.46"),
    ("Horizontal tail",      W_ht,       39.60 - 1.40,         "15.47"),
    ("Vertical tail",        W_vt,       36.84 - 0.76,         "15.48"),
    ("Fuselage",             W_fuse,     0.45 * 42.2,          "15.49"),
    ("Main landing gear",    W_mlg,      20.40,                "15.50"),
    ("Nose landing gear",    W_nlg,       6.50,                "15.51"),
    ("Engines installed",    W_eng_inst, 28.40 - 4.6536,       "15.52"),
    ("Fuel system",          W_fuelsys,  X_LEMAC + 0.40 * MAC, "15.53"),
    ("Flight controls",      W_fc,       24.00,                "15.54"),
    ("Hydraulics",           W_hyd,      22.00,                "15.55"),
    ("Electrical",           W_elec,     18.00,                "15.56"),
    ("Avionics",             W_avionics,  5.50,                "15.57"),
    ("Air cond. + anti-ice", W_ac,       21.50,                "15.58"),
    ("Furnishings",          W_furn,     16.90,                "15.59"),
]

print(f"\n{'group':<24}{'W (lb)':>9}{'% MTOW':>9}{'arm (ft)':>10}  Raymer Eq.")
print("-" * 78)
for name, w, x, eq in groups:
    print(f"{name:<24}{w:9.1f}{w / MTOW * 100:8.2f}%{x:10.2f}  ({eq})")
W_E_II = sum(g[1] for g in groups)
print("-" * 78)
print(f"{'EMPTY WEIGHT (Class-II)':<24}{W_E_II:9.1f}{W_E_II / MTOW * 100:8.2f}%")

W_E_I = 0.59 * MTOW
print(f"\n  Class-I anchor (config.md A.3): W_E = 0.59 x MTOW = {W_E_I:.0f} lb "
      f"({W_E_I / MTOW * 100:.1f}%)")
print(f"  Class-II statistical buildup   : W_E = {W_E_II:.0f} lb "
      f"({W_E_II / MTOW * 100:.1f}%)   delta = {W_E_II - W_E_I:+.0f} lb "
      f"({(W_E_II - W_E_I) / W_E_I * 100:+.1f}%)")

# Does the aircraft still close on its mission?
W_useful = MTOW - W_E_II
W_payload = 1720.0
print(f"\n  Mission closure check at the Class-II empty weight:")
print(f"    useful load = MTOW - W_E = {W_useful:.0f} lb")
print(f"    payload + crew                = {W_payload:.0f} lb")
print(f"    fuel required (W_F/W_TO=0.2634) = {W_FUEL:.0f} lb")
print(f"    sum = {W_payload + W_FUEL:.0f} lb  ->  margin = {W_useful - W_payload - W_FUEL:+.0f} lb")

# ==================================================== CG envelope, sequenced
print("\n" + "=" * 78)
print("8.x  CG ENVELOPE -- loading sequence, not just corner states")
print("=" * 78)


def cg(items):
    w = sum(i[1] for i in items)
    return w, sum(i[1] * i[2] for i in items) / w


def pct(x):
    return (x - X_LEMAC) / MAC * 100


X_FUEL = X_LEMAC + 0.40 * MAC
LOAD = {"crew": (400.0, 7.50), "pax_fwd": (540.0, 14.50), "pax_aft": (540.0, 19.50),
        "bag_nose": (60.0, 5.00), "bag_aft": (180.0, 27.00), "fuel": (W_FUEL, X_FUEL)}

# Two loading orders bracket the envelope: payload-first and fuel-first.
sequences = {
    "fwd-critical: crew, nose bag, fwd pax, fuel, aft pax, aft bag":
        ["crew", "bag_nose", "pax_fwd", "fuel", "pax_aft", "bag_aft"],
    "aft-critical: crew, aft bag, aft pax, fuel, fwd pax, nose bag":
        ["crew", "bag_aft", "pax_aft", "fuel", "pax_fwd", "bag_nose"],
}
extremes = []
for label, seq in sequences.items():
    print(f"\n  {label}")
    print(f"    {'after adding':<12}{'W (lb)':>9}{'Xcg (ft)':>10}{'% MAC':>8}")
    items = list(groups)
    w, x = cg(items)
    print(f"    {'(empty)':<12}{w:9.0f}{x:10.3f}{pct(x):8.1f}")
    extremes.append(("empty", w, x))
    for k in seq:
        items = items + [(k, LOAD[k][0], LOAD[k][1])]
        w, x = cg(items)
        print(f"    {k:<12}{w:9.0f}{x:10.3f}{pct(x):8.1f}")
        extremes.append((k, w, x))

flight = [e for e in extremes if e[1] > W_E_II + 300]     # exclude near-empty
fwd = min(flight, key=lambda e: e[2])
aft = max(flight, key=lambda e: e[2])
print(f"\n  FORWARD limit  {fwd[2]:.3f} ft = {pct(fwd[2]):.1f}% MAC  at W = {fwd[1]:.0f} lb")
print(f"  AFT limit      {aft[2]:.3f} ft = {pct(aft[2]):.1f}% MAC  at W = {aft[1]:.0f} lb")
print(f"  band width = {pct(aft[2]) - pct(fwd[2]):.1f}% MAC")

X_NP = json.load(open(os.path.join(HERE, "v7_results.json")))["x_np"]
print(f"\n  measured neutral point x_np = {X_NP:.3f} ft = {pct(X_NP):.1f}% MAC")
print(f"  static margin at forward CG = {(X_NP - fwd[2]) / MAC * 100:.1f}% MAC")
print(f"  static margin at aft CG     = {(X_NP - aft[2]) / MAC * 100:.1f}% MAC")

# The tail was sized in Chapter 6 against the Class-I point CG; re-solve S_HT against the real aft CG limit found above, feeding the changed tail weight back into the CG.
SM_FLOOR = 0.10                 # MAC fraction, conventional civil-jet minimum
DNP_DSHT = 0.05912              # ft per ft^2, measured slope (report/v7_results.py)
X_HT_ARM = 38.20                # ft, HT group arm

sm_aft_now = (X_NP - aft[2]) / MAC
print(f"\n  --- horizontal tail re-check against the aft CG limit ---")
print(f"  static margin at the aft limit is {100 * sm_aft_now:.1f}% MAC against a "
      f"{100 * SM_FLOOR:.0f}% floor")
if sm_aft_now < SM_FLOOR:
    # Weight and moment of the aft-limit loading with the tail group removed, frozen once.
    w_rest = aft[1] - W_ht
    m_rest = aft[1] * aft[2] - W_ht * X_HT_ARM
    s_ht = SHT
    for _ in range(50):
        w_ht_new = W_ht * (s_ht / SHT) ** 0.896      # Raymer 15.47 exponent on S_ht
        x_aft_new = (m_rest + w_ht_new * X_HT_ARM) / (w_rest + w_ht_new)
        x_np_new = X_NP + DNP_DSHT * (s_ht - SHT)
        resid = (x_np_new - x_aft_new) / MAC - SM_FLOOR
        s_next = s_ht - resid * MAC / DNP_DSHT       # Newton step, dSM/dS_HT ~ DNP/MAC
        if abs(s_next - s_ht) < 1e-5:
            s_ht = s_next
            break
        s_ht = s_next
    w_ht_new = W_ht * (s_ht / SHT) ** 0.896
    x_aft_new = (m_rest + w_ht_new * X_HT_ARM) / (w_rest + w_ht_new)
    x_np_new = X_NP + DNP_DSHT * (s_ht - SHT)
    print(f"  converged: aft CG moves {aft[2]:.3f} -> {x_aft_new:.3f} ft as the tail grows;"
          f" x_np {X_NP:.3f} -> {x_np_new:.3f} ft")
    print(f"  check: SM at the aft limit = {(x_np_new - x_aft_new) / MAC * 100:.1f}% MAC")
    print(f"  required S_HT for SM = {100 * SM_FLOOR:.0f}% at the aft limit: "
          f"{s_ht:.1f} ft^2  (vs {SHT:.1f} ft^2 built)  -> +{s_ht - SHT:.1f} ft^2, "
          f"+{(s_ht / SHT - 1) * 100:.0f}%")
    print(f"  tail weight would rise {W_ht:.0f} -> {w_ht_new:.0f} lb; "
          f"c_HT rises {SHT * LT / (SW * MAC):.3f} -> {s_ht * LT / (SW * MAC):.3f}")
    print(f"  RECOMMENDED as the full_v8 change. Not applied to the built model in this")
    print(f"  pass -- it invalidates the measured polar, so it needs a VSPAERO re-run.")
    S_HT_REQ = s_ht
else:
    S_HT_REQ = SHT
    print("  no change required")

env = [dict(state="Empty (not a flight state)", W=W_E_II, xcg=cg(groups)[1],
            pct_mac=pct(cg(groups)[1]))]
for lbl, w, x in [("Forward limit", fwd[1], fwd[2]), ("Aft limit", aft[1], aft[2])]:
    env.append(dict(state=lbl, W=w, xcg=x, pct_mac=pct(x)))
mt = cg(list(groups) + [(k, *LOAD[k]) for k in LOAD])
env.append(dict(state="MTOW (all items)", W=mt[0], xcg=mt[1], pct_mac=pct(mt[1])))
print(f"\n  fully loaded: W = {mt[0]:.0f} lb, Xcg = {mt[1]:.3f} ft = {pct(mt[1]):.1f}% MAC"
      f"  (vs MTOW {MTOW:.0f} lb)")

json.dump(dict(W_E_classII=W_E_II, W_E_classI=W_E_I, n_limit=n_lim, Nz=NZ,
               groups=[dict(name=n, W=w, arm=x, eq=e) for n, w, x, e in groups],
               envelope=env, x_np=X_NP, S_HT_built=SHT, S_HT_required=S_HT_REQ,
               sm_fwd=(X_NP - fwd[2]) / MAC * 100, sm_aft=(X_NP - aft[2]) / MAC * 100),
          open(os.path.join(HERE, "class2_weights.json"), "w"), indent=2)
print(f"\nwritten: {os.path.join(HERE, 'class2_weights.json')}")
