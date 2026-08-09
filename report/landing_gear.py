"""Chapter 7 -- landing gear design (Raymer Ch.11 loads/tyres/shock absorber + Sadraey Ch.9 clearance/overturn geometry); CG envelope prefers report/class2_weights.py, falling back to the Class-I envelope in v7_results.json if it hasn't been run."""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------- inputs
MTOW = 11660.0                  # lb, config.md A.3
MLW = 0.93 * MTOW               # lb, config.md B.2 ASSUMPTION
G = 32.174                      # ft/s^2
VS_LAND = 91.0 * 1.68781        # ft/s, config.md B.2 stall speed at MLW

# Airframe stations, full_v7 (wing root LE 14.3464 -> wing_dx = -4.6536 ft)
WING_DX = 14.3464 - 19.0
X_LEMAC, MAC = 17.734, 5.0237   # report/v7_results.py
FUSE_R = 3.05                   # ft, barrel radius (fuselage.md 5)
Z_FAIRING_BOTTOM = -3.80        # ft, belly fairing lower surface (config.md D.5b)
X_FAIRING = (16.0 + WING_DX, 16.0 + WING_DX + 17.07)
WING_ROOT_Z, DIHEDRAL, SEMISPAN = -2.60, 2.3, 20.7662
WING_ROOT_LE, CR_W = 14.3464, 6.9086
# Aft-body lower line, from the 7-station loft in gen_v7.py: (x, z_bottom)
AFT_LOWER = [(30.5, 0.4769 - 4.696 / 2), (42.2, 1.7956 - 0.60 / 2)]

# CG envelope -- prefer the Class-II result, fall back to Class-I
def load_cg():
    for f, key in (("class2_weights.json", "envelope"), ("v7_results.json", "envelope")):
        p = os.path.join(HERE, f)
        if os.path.exists(p):
            env = json.load(open(p))[key]
            flight = [e for e in env if "not a flight state" not in e["state"]]
            return (min(e["xcg"] for e in flight), max(e["xcg"] for e in flight),
                    f, [(e["state"], e["W"], e["xcg"]) for e in flight])
    raise SystemExit("run report/v7_results.py first")


X_CG_FWD, X_CG_AFT, CG_SRC, CG_STATES = load_cg()

print("=" * 78)
print("CHAPTER 7  LANDING GEAR DESIGN")
print("=" * 78)
print(f"CG envelope source: {CG_SRC}")
print(f"  forward CG  x = {X_CG_FWD:.3f} ft  ({(X_CG_FWD - X_LEMAC) / MAC * 100:.1f}% MAC)")
print(f"  aft CG      x = {X_CG_AFT:.3f} ft  ({(X_CG_AFT - X_LEMAC) / MAC * 100:.1f}% MAC)")

# ------------------------------------------------- 7.1 vertical position
# Gear length is set by ground clearance under the lowest airframe point, which here is the belly fairing, not the fuselage barrel.
CLEARANCE_FAIRING = 1.00        # ft, ASSUMPTION inside Sadraey Table 9.4 item 1
Z_GROUND = Z_FAIRING_BOTTOM - CLEARANCE_FAIRING
H_AXIS = -Z_GROUND              # fuselage axis height above ground
Z_CG = -0.50                    # ft, ASSUMPTION: CG sits just below the axis
H_CG = Z_CG - Z_GROUND

print(f"\n7.1 Vertical position")
print(f"  lowest airframe point (belly fairing)  z = {Z_FAIRING_BOTTOM:.2f} ft")
print(f"  clearance under it (Sadraey Table 9.4) = {CLEARANCE_FAIRING:.2f} ft "
      f"({CLEARANCE_FAIRING * 0.3048:.2f} m, inside the 0.2-1.2 m band)")
print(f"  ground plane   z = {Z_GROUND:.2f} ft   -> fuselage axis {H_AXIS:.2f} ft above ground")
print(f"  CG height above ground  H_cg = {H_CG:.2f} ft")

# ---------------------------------------- 7.2 longitudinal position (tipback)
TIPBACK_MIN = 15.0              # deg, Raymer
x_mg_tipback = X_CG_AFT + H_CG * math.tan(math.radians(TIPBACK_MIN))
X_MG = 21.00                    # adopted, ft -- set by the tipback constraint below
tipback = math.degrees(math.atan((X_MG - X_CG_AFT) / H_CG))
print(f"\n7.2 Longitudinal position")
print(f"  tipback >= {TIPBACK_MIN:.0f} deg requires x_mg >= {x_mg_tipback:.3f} ft")
print(f"  adopted main gear station x_mg = {X_MG:.2f} ft"
      f"  -> tipback angle = {tipback:.1f} deg  "
      f"({'OK' if tipback >= TIPBACK_MIN else 'FAILS'})")

# Nose gear station: forward, in the unpressurised nose bay ahead of the cabin
X_NG = 6.50                     # ft, weight.md 3 arm
B = X_MG - X_NG
M_f, M_a = X_MG - X_CG_FWD, X_MG - X_CG_AFT
N_f, N_a = X_CG_FWD - X_NG, X_CG_AFT - X_NG
print(f"  nose gear station x_ng = {X_NG:.2f} ft  ->  wheelbase B = {B:.3f} ft")
print(f"  M_f/B = {M_f / B:.4f}  (Raymer: < 0.20, 0.15 preferred)  "
      f"{'OK' if M_f / B < 0.20 else 'FAILS'}")
print(f"  M_a/B = {M_a / B:.4f}  (Raymer: > 0.05, 0.08 preferred)  "
      f"{'OK' if M_a / B > 0.05 else 'FAILS'}")

# ------------------------------------------------------ 7.3 tail-strike angle
def strike_angle(x, z):
    return math.degrees(math.atan((z - Z_GROUND) / (x - X_MG))) if x > X_MG else 90.0


(x1, z1), (x2, z2) = AFT_LOWER
samples = [(x1 + (x2 - x1) * t, z1 + (z2 - z1) * t) for t in [i / 20 for i in range(21)]]
alpha_c = min(strike_angle(x, z) for x, z in samples)
x_crit = min(samples, key=lambda p: strike_angle(*p))[0]
print(f"\n7.3 Ground clearance during rotation (Sadraey Fig. 9.x, alpha_C >= alpha_TO)")
print(f"  aft-body lower line runs ({x1:.1f}, {z1:.2f}) -> ({x2:.1f}, {z2:.2f}) ft")
print(f"  fuselage tail-strike angle alpha_C = {alpha_c:.1f} deg, critical station x = {x_crit:.1f} ft")

# The belly fairing aft closure is the real constraint if it stays at full depth
x_f2 = X_FAIRING[1]
z_needed = Z_GROUND + (x_f2 - X_MG) * math.tan(math.radians(12.0))
print(f"  belly fairing ends at x = {x_f2:.2f} ft; to clear a 12 deg rotation its lower")
print(f"  line must have risen to z >= {z_needed:.2f} ft there (vs {Z_FAIRING_BOTTOM:.2f} ft at max depth)")
print(f"  -> required aft-closure rise = {z_needed - Z_FAIRING_BOTTOM:.2f} ft. CONSTRAINT ON THE FAIRING RELOFT.")

# --------------------------------------------------- 7.4 track and overturn
PHI_OT_MIN = 25.0               # deg, Sadraey Eq. (9.18)
y_min = H_CG * math.tan(math.radians(PHI_OT_MIN))
TRACK = 8.00                    # ft, adopted
y_ot = TRACK / 2
phi_ot = math.degrees(math.atan(y_ot / H_CG))
z_tip = WING_ROOT_Z + SEMISPAN * math.tan(math.radians(DIHEDRAL))
roll_clear = math.degrees(math.atan((z_tip - Z_GROUND) / (SEMISPAN - y_ot)))
print(f"\n7.4 Wheel track and lateral ground clearance")
print(f"  Sadraey Eq. (9.18) Phi_ot >= {PHI_OT_MIN:.0f} deg -> half-track >= {y_min:.2f} ft "
      f"(track >= {2 * y_min:.2f} ft)")
print(f"  adopted track T = {TRACK:.2f} ft  ->  Phi_ot = {phi_ot:.1f} deg  "
      f"({'OK' if phi_ot >= PHI_OT_MIN else 'FAILS'})")
print(f"  wing tip at y = {SEMISPAN:.2f} ft sits z = {z_tip:.2f} ft "
      f"({z_tip - Z_GROUND:.2f} ft above ground, {DIHEDRAL:.1f} deg dihedral)")
print(f"  roll angle to wing-tip strike = {roll_clear:.1f} deg")

# --------------------------------------------------------------- 7.5 loads
max_static_main = MTOW * N_a / B
max_static_nose = MTOW * M_f / B
min_static_nose = MTOW * M_a / B
dyn_brake_nose = 10.0 * H_CG * MTOW / (G * B)
nose_design = max_static_nose + dyn_brake_nose
N_MAIN_WHEELS, N_NOSE_WHEELS = 4, 2      # twin wheels per main leg, twin nose
print(f"\n7.5 Gear loads (Raymer Eqs. 11.1-11.4, at MTOW = {MTOW:.0f} lb)")
print(f"  max static main  = W*N_a/B = {max_static_main:8.0f} lb "
      f"({max_static_main / MTOW * 100:.1f}% W)  -> {max_static_main / N_MAIN_WHEELS:.0f} lb/wheel "
      f"({N_MAIN_WHEELS} main wheels)")
print(f"  max static nose  = W*M_f/B = {max_static_nose:8.0f} lb "
      f"({max_static_nose / MTOW * 100:.1f}% W)")
print(f"  min static nose  = W*M_a/B = {min_static_nose:8.0f} lb "
      f"({min_static_nose / MTOW * 100:.1f}% W)")
print(f"  dynamic braking  = 10HW/gB = {dyn_brake_nose:8.0f} lb")
print(f"  NOSE DESIGN LOAD = static+dynamic = {nose_design:.0f} lb "
      f"-> {nose_design / N_NOSE_WHEELS:.0f} lb/wheel ({N_NOSE_WHEELS} nose wheels)")

# ---------------------------------------------------------- 7.6 tyre selection
# Raymer Table 11.2 entries (Type VII and three-part-name) that bracket this aircraft's per-wheel loads.
TIRES = [
    # name,          speed,  max load lb, psi, width, diam, roll radius, rim
    ("18 x 4.4",      "174 kt", 2100,  100, 4.45, 17.90, 7.9, 10.0, 6),
    ("18 x 4.4",      "217 kt", 4350,  225, 4.45, 17.90, 7.9, 10.0, 12),
    ("18 x 4.25-10",  "210 mph", 2300, 100, 4.70, 18.25, 7.9, 10.0, 6),
    ("21 x 7.25-10",  "210 mph", 5150, 135, 7.20, 21.25, 9.0, 10.0, 10),
    ("24 x 5.5",      "174 kt", 11500, 355, 5.75, 24.15, 10.6, 14.0, 16),
]


P_FLOTATION = 120.0     # psi, Raymer Table 11.3, major civil airfield


def contact_area(w, d, rr):
    """Raymer Eq. (11.6): A_p = 2.3 sqrt(w d) (d/2 - R_r), in^2."""
    return 2.3 * math.sqrt(w * d) * (d / 2 - rr)


def pick(load, label):
    """A tyre must carry the load (Table 11.2) AND keep P = W_w/A_p (Eq. 11.5) below the Table 11.3 flotation limit -- the smallest tyre that carries the load is often not acceptable on pavement."""
    print(f"\n  {label}: required {load:.0f} lb/wheel")
    print(f"  {'size':<15}{'max load':>9}{'w in':>7}{'d in':>7}{'Rr in':>7}{'rim':>6}"
          f"{'A_p in2':>9}{'P req':>8}{'load':>7}{'float':>7}")
    best = None
    for t in TIRES:
        name, spd, ml, psi, w, d, rr, rim, ply = t
        Ap = contact_area(w, d, rr)
        p_req = load / Ap
        ok_load, ok_float = ml >= load, p_req <= P_FLOTATION
        mark = ""
        if ok_load and ok_float and best is None:
            best, mark = t, "  <-- selected"
        print(f"  {name:<15}{ml:>9}{w:>7.2f}{d:>7.2f}{rr:>7.1f}{rim:>6.1f}"
              f"{Ap:>9.1f}{p_req:>8.0f}{'OK' if ok_load else 'no':>7}"
              f"{'OK' if ok_float else 'no':>7}{mark}")
    return best


main_tire = pick(max_static_main / N_MAIN_WHEELS, "MAIN wheel (max static)")
nose_tire = pick(nose_design / N_NOSE_WHEELS, "NOSE wheel (static + dynamic)")

# Contact-area / inflation-pressure check, Raymer Eqs. (11.5)/(11.6)
for t, load, lbl in ((main_tire, max_static_main / N_MAIN_WHEELS, "main"),
                     (nose_tire, nose_design / N_NOSE_WHEELS, "nose")):
    name, spd, ml, psi, w, d, rr, rim, ply = t
    Ap = contact_area(w, d, rr)
    p_req = load / Ap
    print(f"\n  {lbl} tyre {name}: A_p = {Ap:.1f} in^2, P = W_w/A_p = {p_req:.0f} psi")
    print(f"    rated {psi} psi; flotation limits (Raymer Table 11.3): "
          f"major civil airfield 120, tarmac/good foundation 70-90, "
          f"{'clears both' if p_req <= 70 else 'civil pavement only'}")

# ------------------------------------------------------- 7.7 brake sizing
KE_brake = 0.5 * (MLW / G) * VS_LAND ** 2               # ft-lb, Raymer Eq. (11.7)
print(f"\n7.7 Brakes (Raymer Eq. 11.7)")
print(f"  landing weight {MLW:.0f} lb, V_stall {VS_LAND:.1f} ft/s ({VS_LAND / 1.68781:.0f} kt)")
print(f"  KE_braking = {KE_brake / 1e6:.3f} x 10^6 ft-lb total")
print(f"             = {KE_brake / 1e6 / N_MAIN_WHEELS:.3f} x 10^6 ft-lb per braked wheel "
      f"({N_MAIN_WHEELS} braked main wheels)")
print(f"  Raymer Fig. 11.8 (GA and small jets) returns a rim diameter of roughly")
print(f"  10-12 in at this energy, consistent with the {main_tire[7]:.0f} in rim of the selected tyre.")

# ------------------------------------------------- 7.8 shock absorber stroke
V_VERT = 10.0                   # ft/s, FAR 25 / Raymer
ETA_OLEO, ETA_TIRE = 0.80, 0.47  # Raymer Table 11.4 (metered orifice / tyre)
N_GEAR = 3.0                    # Raymer Table 11.5, commercial 2.7-3
name, spd, ml, psi, w, d, rr, rim, ply = main_tire
S_T = (d / 2 - rr) / 12.0       # ft, tyre stroke
S = V_VERT ** 2 / (2 * G * ETA_OLEO * N_GEAR) - (ETA_TIRE / ETA_OLEO) * S_T
S_in = S * 12 + 1.0             # + 1 in safety margin, Raymer
print(f"\n7.8 Shock absorber (Raymer Eqs. 11.12, 11.13)")
print(f"  sink speed {V_VERT:.0f} ft/s, N_gear = {N_GEAR:.1f}, eta_oleo = {ETA_OLEO}, "
      f"eta_tyre = {ETA_TIRE}")
print(f"  tyre stroke S_T = d/2 - R_r = {S_T * 12:.2f} in")
print(f"  stroke S = V^2/(2 g eta N) - (eta_T/eta) S_T = {S * 12:.2f} in"
      f"  -> {S_in:.1f} in with the 1 in margin")
S_final = max(S_in, 10.0)
print(f"  adopted stroke = {S_final:.1f} in "
      f"(Raymer: 8 in minimum, 10-12 in desirable)")
print(f"  total oleo length ~ 2.5 x stroke = {2.5 * S_final:.1f} in = {2.5 * S_final / 12:.2f} ft")

P_OLEO = 1800.0                 # psi, Raymer
L_main_oleo = max_static_main / 2
L_nose_oleo = nose_design
for lbl, L in (("main (per leg)", L_main_oleo), ("nose", L_nose_oleo)):
    D = 1.3 * math.sqrt(4 * L / (P_OLEO * math.pi))
    print(f"  {lbl:15s} oleo load {L:7.0f} lb -> external diameter "
          f"1.3*sqrt(4L/(pi P)) = {D:.2f} in")

# ------------------------------------------------------------------ summary
out = dict(x_mg=X_MG, x_ng=X_NG, B=B, track=TRACK, H_cg=H_CG, z_ground=Z_GROUND,
           tipback_deg=tipback, phi_ot_deg=phi_ot, alpha_c_deg=alpha_c,
           roll_clearance_deg=roll_clear,
           Mf_over_B=M_f / B, Ma_over_B=M_a / B,
           max_static_main=max_static_main, max_static_nose=max_static_nose,
           min_static_nose=min_static_nose, dyn_brake_nose=dyn_brake_nose,
           nose_design_load=nose_design,
           main_tire=main_tire[0], nose_tire=nose_tire[0],
           stroke_in=S_final, KE_brake=KE_brake,
           n_main_wheels=N_MAIN_WHEELS, n_nose_wheels=N_NOSE_WHEELS)
json.dump(out, open(os.path.join(HERE, "landing_gear.json"), "w"), indent=2)
print(f"\nwritten: {os.path.join(HERE, 'landing_gear.json')}")
