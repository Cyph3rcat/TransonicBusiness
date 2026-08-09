"""Chapter 10 -- performance analysis (Raymer Ch.17 + FAR 25.111/119/121/333/335/337), using the Chapter 9 measured drag polar rather than a historical L/D; flap/gear increments (Raymer Ch.12 typicals) are the softest inputs here."""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ========================================================= atmosphere (ISA)
RHO_SL, T_SL, A_SL = 0.0023769, 518.67, 1116.45      # slug/ft^3, R, ft/s
G = 32.174
TROP = 36089.0


def isa(h):
    """ISA density (slug/ft^3), temperature (R) and speed of sound (ft/s)."""
    if h <= TROP:
        T = T_SL - 0.00356616 * h
        rho = RHO_SL * (T / T_SL) ** 4.2561
    else:
        T = 389.97
        rho = RHO_SL * 0.29707 * math.exp(-(h - TROP) / 20806.0)
    return rho, T, math.sqrt(1.4 * 1716.5 * T)


# ============================================================ the aeroplane
MTOW = 11660.0
MLW = 0.93 * MTOW
W_FUEL = 0.2634 * MTOW
W_E = 6878.5                     # lb, Class-II (report/class2_weights.py)
W_PAYLOAD_MAX = 1320.0           # lb, 6 pax + baggage (crew carried separately)
W_CREW = 400.0
SW, AR, BW = 193.678, 8.9095, 41.5324
CD0_CRUISE = 0.02465             # Chapter 9, incl. 3% leak/protuberance
K_CRUISE = 0.03617               # CDi = K CL^2, VSPAERO Trefftz (e = 0.988)
E_LOWSPEED = 0.80                # ASSUMPTION for flapped/geared configurations
K_LOW = 1.0 / (math.pi * AR * E_LOWSPEED)

# Propulsion -- Williams FJ44-3A-24, EASA TCDS IM.E.016 Issue 13
T_SL_STATIC = 2 * 2490.0         # lbf, takeoff rating, both engines
BPR = 3.3                        # Williams FJ44 family published bypass ratio
LAPSE_EXP = 0.8                  # T/T_SL = (rho/rho_SL)^0.8, Raymer-style
SFC_CRUISE = 0.70                # lb/(lbf.hr) -- see the report's discussion

# High-lift and configuration increments (Raymer Ch.12 typical values)
CLMAX_CLEAN, CLMAX_TO, CLMAX_LAND = 1.40, 1.70, 2.00
DCD0_FLAP_TO, DCD0_FLAP_LAND, DCD0_GEAR = 0.015, 0.065, 0.020
MU_ROLL, MU_BRAKE = 0.03, 0.50   # Raymer Table 17.1, hard runway


def thrust(h, throttle=1.0):
    rho, _, _ = isa(h)
    return throttle * T_SL_STATIC * (rho / RHO_SL) ** LAPSE_EXP


def vstall(W, clmax, h=0.0):
    rho, _, _ = isa(h)
    return math.sqrt(2 * W / (rho * SW * clmax))


print("=" * 78)
print("CHAPTER 10  PERFORMANCE ANALYSIS")
print("=" * 78)
print(f"  drag polar (Ch.9):  CD = {CD0_CRUISE:.5f} + {K_CRUISE:.5f} CL^2  (clean, pre-wave)")
print(f"  engines: 2 x FJ44-3A-24, {T_SL_STATIC:.0f} lbf total SL static, "
      f"lapse (rho/rho_SL)^{LAPSE_EXP}")
print(f"  T/W at MTOW, sea level = {T_SL_STATIC / MTOW:.3f}")

# ===================================================== 10.1 stall speeds
print(f"\n10.1  Stall speeds (sea level, ISA)")
print(f"  {'configuration':<28}{'CLmax':>7}{'W (lb)':>9}{'Vs (kt)':>9}{'1.2Vs':>8}{'1.3Vs':>8}")
for lbl, clmax, W in (("clean, MTOW", CLMAX_CLEAN, MTOW),
                      ("takeoff flaps, MTOW", CLMAX_TO, MTOW),
                      ("landing flaps, MLW", CLMAX_LAND, MLW)):
    v = vstall(W, clmax) / 1.68781
    print(f"  {lbl:<28}{clmax:7.2f}{W:9.0f}{v:9.1f}{1.2 * v:8.1f}{1.3 * v:8.1f}")

# ==================================================== 10.2 takeoff analysis
print(f"\n10.2  Takeoff (Raymer Eqs. 17.102, 17.113-114)")
CL_CLIMB = CLMAX_TO / 1.2 ** 2                       # CL at 1.2 Vstall
T_av = 0.75 * T_SL_STATIC * (5 + BPR) / (4 + BPR)    # Eq. (17.114)
U = 0.01 * CLMAX_TO + 0.02                           # Eq. (17.113) terminology
CD_TO = CD0_CRUISE + DCD0_FLAP_TO + DCD0_GEAR + K_LOW * CL_CLIMB ** 2
D_over_W_oei = CD_TO / CL_CLIMB
gamma_climb = math.asin(max((T_av / 2) / MTOW - D_over_W_oei, 1e-4))   # one engine out
GAMMA_MIN = 0.024                                     # 2-engine, Eq. (17.113)
Gfac = gamma_climb - GAMMA_MIN
h_obs = 35.0
BFL = (0.863 / (1 + 2.3 * Gfac)
       * (MTOW / SW / (RHO_SL * G * CL_CLIMB) + h_obs)
       * (1.0 / (T_av / MTOW - U) + 2.7)
       + 655.0 / math.sqrt(1.0))
print(f"  CL at 1.2 Vstall            = {CL_CLIMB:.3f}")
print(f"  T_av = 0.75 T (5+BPR)/(4+BPR) = {T_av:.0f} lbf  (BPR = {BPR})")
print(f"  U = 0.01 CLmax + 0.02        = {U:.4f}")
print(f"  one-engine-out climb angle   = {math.degrees(gamma_climb):.2f} deg "
      f"(gradient {100 * math.sin(gamma_climb):.2f}%)")
print(f"  G = gamma_climb - gamma_min  = {Gfac:.4f}")
print(f"  BALANCED FIELD LENGTH        = {BFL:.0f} ft   "
      f"(target {'MET' if BFL <= 3500 else 'MISSED'}: 3,500 ft, config.md A.1)")


def ground_roll(W, clmax, cd0, k, mu, v_i, v_f, h=0.0, thr=1.0, cl_ground=0.10):
    """Raymer Eq. (17.102), closed form for constant thrust over the segment."""
    rho, _, _ = isa(h)
    T = thrust(h, thr)
    K_T = T / W - mu
    K_A = (rho / (2 * (W / SW))) * (mu * cl_ground - cd0 - k * cl_ground ** 2)
    return (1.0 / (2 * G * K_A)) * math.log((K_T + K_A * v_f ** 2)
                                            / (K_T + K_A * v_i ** 2))


V_TO = 1.1 * vstall(MTOW, CLMAX_TO)
s_g = ground_roll(MTOW, CLMAX_TO, CD0_CRUISE + DCD0_FLAP_TO + DCD0_GEAR, K_LOW,
                  MU_ROLL, 0.0, V_TO)
print(f"  all-engines ground roll to V_LOF = 1.1 Vs ({V_TO / 1.68781:.0f} kt) = {s_g:.0f} ft")

# ============================================= 10.3 FAR 25 climb gradients
print(f"\n10.3  FAR 25 certification climb gradients (one engine inoperative)")
print(f"  {'segment':<42}{'req':>7}{'achieved':>10}{'':>6}")
cases = [
    # label, CLmax basis, dCD0, gear, N_eng operating, required gradient, speed factor
    ("25.111 1st seg: gear down, TO flaps, OEI", CLMAX_TO, DCD0_FLAP_TO, True, 1, 0.000, 1.2),
    ("25.121(b) 2nd seg: gear up, TO flaps, OEI", CLMAX_TO, DCD0_FLAP_TO, False, 1, 0.024, 1.2),
    ("25.121(c) final seg: clean, OEI", CLMAX_CLEAN, 0.0, False, 1, 0.012, 1.25),
    ("25.121(d) approach: appr flaps, gear up, OEI", 1.85, 0.035, False, 1, 0.021, 1.4),
    ("25.119 landing: landing flaps, gear down, AEO", CLMAX_LAND, DCD0_FLAP_LAND, True, 2, 0.032, 1.3),
]
climb_rows = []
for lbl, clmax, dcd0, gear, neng, req, vfac in cases:
    W = MLW if "landing" in lbl or "approach" in lbl else MTOW
    CL = clmax / vfac ** 2
    cd0 = CD0_CRUISE + dcd0 + (DCD0_GEAR if gear else 0.0)
    CD = cd0 + K_LOW * CL ** 2
    T = thrust(0.0) * neng / 2
    grad = T / W - CD / CL
    ok = grad >= req
    climb_rows.append((lbl, req, grad, ok))
    print(f"  {lbl:<42}{100 * req:6.1f}%{100 * grad:9.2f}%{'  OK' if ok else '  FAIL':>6}")

# ================================================ 10.4 climb and ceilings
print(f"\n10.4  Rate of climb and ceilings (all engines, MTOW)")


V_MO_KEAS, M_MO = 300.0, 0.80    # operating limits (ASSUMPTION, class-typical)


def climb_speed_limit(h):
    """Allowed climb speed (250 KIAS below 10,000 ft, then V_MO EAS, then M_MO); without this cap the optimum sits near V_MO at sea level, a rate of climb no operator would fly."""
    rho, _, a = isa(h)
    v_eas_cap = (250.0 if h < 10000.0 else V_MO_KEAS) * 1.68781
    v_from_eas = v_eas_cap / math.sqrt(rho / RHO_SL)
    return min(v_from_eas, M_MO * a)


def best_roc(W, h, throttle=1.0, cd0=CD0_CRUISE, k=K_CRUISE, neng=2,
             limited=True):
    rho, _, a = isa(h)
    T = thrust(h, throttle) * neng / 2
    v_max = climb_speed_limit(h) if limited else M_MO * a
    best = (-1e9, 0.0)
    v = 150.0
    while v <= v_max:
        CL = 2 * W / (rho * v ** 2 * SW)
        if CL <= CLMAX_CLEAN:
            D = 0.5 * rho * v ** 2 * SW * (cd0 + k * CL ** 2)
            roc = v * (T - D) / W
            if roc > best[0]:
                best = (roc, v)
        v += 2.0
    return best


print(f"  climb schedule: 250 KIAS below 10,000 ft, then {V_MO_KEAS:.0f} KEAS, "
      f"then M{M_MO}")
print(f"  {'altitude':>9}{'ROC (fpm)':>11}{'V (KTAS)':>10}{'M':>7}{'OEI ROC (fpm)':>15}")
for h in (0, 10000, 20000, 30000, 41000, 45000):
    roc, V = best_roc(MTOW, h)
    roc_oei, _ = best_roc(MTOW, h, neng=1)
    _, _, a = isa(h)
    print(f"  {h:9,.0f}{60 * roc:11,.0f}{V / 1.68781:10.0f}{V / a:7.2f}{60 * roc_oei:15,.0f}")


def ceiling(neng, roc_floor_fpm=100.0):
    """Lowest altitude at which best rate of climb falls below the floor."""
    for h in range(0, 70000, 250):
        roc, _ = best_roc(MTOW, h, neng=neng)
        if 60 * roc < roc_floor_fpm:
            return h
    return None


ceil_ae, ceil_oei = ceiling(2), ceiling(1)
ceil_ae_txt = f"{ceil_ae:,.0f} ft" if ceil_ae else "above 70,000 ft (model limit)"
ceil_oei_txt = f"{ceil_oei:,.0f} ft" if ceil_oei else "above 70,000 ft (model limit)"
print(f"  service ceiling (100 fpm, all engines, MTOW) = {ceil_ae_txt}")
print(f"  OEI service ceiling  (100 fpm, MTOW)         = {ceil_oei_txt}")
print(f"  NOTE: the aerodynamic ceiling this model returns is far above the FL450")
print(f"  design ceiling. FL450 is set by cabin pressurisation and certification,")
print(f"  not by thrust -- and the (rho/rho_SL)^{LAPSE_EXP} lapse is optimistic this high,")
print(f"  since it carries no ram-recovery or compressor-limit term. Treat the")
print(f"  figure as 'thrust is not the binding constraint', not as a real ceiling.")

# ================================================= 10.5 cruise and range
print(f"\n10.5  Cruise and range (Breguet, SFC = {SFC_CRUISE} lb/lbf/hr)")


def breguet(W_start, W_end, h, mach=0.80, sfc=SFC_CRUISE):
    """Range in nm at constant altitude and Mach, using the real polar."""
    rho, _, a = isa(h)
    V = mach * a
    n = 200
    R, W = 0.0, W_start
    dW = (W_start - W_end) / n
    for _ in range(n):
        CL = 2 * W / (rho * V ** 2 * SW)
        LD = CL / (CD0_CRUISE + K_CRUISE * CL ** 2)
        R += (V / (sfc / 3600.0)) * LD * dW / W
        W -= dW
    return R / 6076.12                                   # ft -> nm


W_start = MTOW * 0.98 * 0.97                              # after taxi and climb
W_end = W_start - (W_FUEL / 1.06 - MTOW * (1 - 0.98 * 0.97) - W_start * (1 - 0.99 * 0.997))
print(f"  cruise start weight {W_start:.0f} lb, cruise end weight {W_end:.0f} lb")
for h in (41000, 43000, 45000):
    rho, _, a = isa(h)
    V = 0.80 * a
    CL = 2 * W_start / (rho * V ** 2 * SW)
    LD = CL / (CD0_CRUISE + K_CRUISE * CL ** 2)
    print(f"  FL{h // 100}: V = {V / 1.68781:.0f} KTAS, CL = {CL:.3f}, L/D = {LD:.2f},"
          f"  range = {breguet(W_start, W_end, h):.0f} nm")
R_design = breguet(W_start, W_end, 43000)
print(f"  cruise-climb FL410->FL450 approximated at FL430 mean: R = {R_design:.0f} nm")
print(f"  design range requirement 1,750 nm: "
      f"{'MET' if R_design >= 1750 else 'MISSED'}"
      f"   capability target 2,000 nm: {'MET' if R_design >= 2000 else 'MISSED'}")

print(f"\n  SFC sensitivity (the softest input in this chapter):")
print(f"  {'SFC':>6}{'range (nm)':>13}{'vs 1,750 nm req':>18}")
for sfc in (0.60, 0.65, 0.70, 0.75, 0.80):
    r = breguet(W_start, W_end, 43000, sfc=sfc)
    print(f"  {sfc:6.2f}{r:13.0f}{r / 1750 - 1:17.0%}")

# ================================================ 10.6 payload-range diagram
print(f"\n10.6  Payload-range diagram")
OEW = W_E + W_CREW
MAX_FUEL = 488 * 6.7                                       # gal x lb/gal Jet A
print(f"  OEW = {OEW:.0f} lb, max payload = {W_PAYLOAD_MAX:.0f} lb, "
       f"max fuel = {MAX_FUEL:.0f} lb")
pts = []
# A: max payload, fuel to MTOW
f_A = MTOW - OEW - W_PAYLOAD_MAX
# B: max payload AND max fuel (if MTOW allows), else the max-fuel corner
w_B = OEW + W_PAYLOAD_MAX + MAX_FUEL
pl_B = min(W_PAYLOAD_MAX, MTOW - OEW - MAX_FUEL)
# C: zero payload, max fuel (ferry)
for lbl, pl, fuel in (("A  max payload, MTOW", W_PAYLOAD_MAX, f_A),
                      ("B  max fuel at MTOW", max(pl_B, 0.0), MAX_FUEL),
                      ("C  ferry, zero payload", 0.0, MAX_FUEL)):
    W0 = OEW + pl + fuel
    ws = W0 * 0.98 * 0.97
    burn = fuel / 1.06 - W0 * (1 - 0.98 * 0.97) - ws * (1 - 0.99 * 0.997)
    r = breguet(ws, ws - burn, 43000) if burn > 0 else 0.0
    pts.append((lbl, pl, fuel, W0, r))
    print(f"  {lbl:<26} payload {pl:6.0f} lb  fuel {fuel:6.0f} lb  "
          f"TOW {W0:7.0f} lb  range {r:6.0f} nm")

# ==================================================== 10.7 landing analysis
print(f"\n10.7  Landing (Raymer Eq. 17.102 + FAA 1.666 factor)")
V_APP = 1.3 * vstall(MLW, CLMAX_LAND)
V_TD = 1.15 * vstall(MLW, CLMAX_LAND)
cd0_land = CD0_CRUISE + DCD0_FLAP_LAND + DCD0_GEAR
s_air = (50.0 - 0.0) / math.tan(math.radians(3.0))          # 3 deg approach from 50 ft
s_flare = 1.0 * V_TD * 1.0                                   # 1 s flare at touchdown speed
s_free = 3.0 * V_TD                                          # 3 s free roll before brakes
s_brake = ground_roll(MLW, CLMAX_LAND, cd0_land, K_LOW, MU_BRAKE,
                      V_TD, 0.1, thr=0.0)
s_total = s_air + s_flare + s_free + s_brake
print(f"  approach speed 1.3 Vs = {V_APP / 1.68781:.0f} kt, touchdown 1.15 Vs "
      f"= {V_TD / 1.68781:.0f} kt")
print(f"  air distance from 50 ft (3 deg) = {s_air:.0f} ft")
print(f"  flare + 3 s free roll          = {s_flare + s_free:.0f} ft")
print(f"  braking roll (mu = {MU_BRAKE})        = {s_brake:.0f} ft")
print(f"  total landing distance         = {s_total:.0f} ft")
print(f"  FAR field length = 1.666 x total = {1.666 * s_total:.0f} ft")

# ======================================================= 10.8 V-n diagram
print(f"\n10.8  V-n manoeuvre and gust envelope (FAR 25.333-341)")
n_pos = min(max(2.1 + 24000.0 / (MTOW + 10000.0), 2.5), 3.8)
n_neg = -1.0
V_S1 = vstall(MTOW, CLMAX_CLEAN)
V_A = V_S1 * math.sqrt(n_pos)
rho_c, _, a_c = isa(41000)
V_C_alt = 0.80 * a_c * math.sqrt(rho_c / RHO_SL)      # M0.80 at FL410, in EAS
V_C_eas = max(V_C_alt, V_MO_KEAS * 1.68781)           # FAR 25.335: V_C is normally V_MO
V_D_eas = V_C_eas / 0.80
CL_ALPHA = 4.316                                              # /rad, VSPAERO full_v7
mu_g = 2 * (MTOW / SW) / (RHO_SL * 5.0237 * CL_ALPHA * G)
K_g = 0.88 * mu_g / (5.3 + mu_g)
print(f"  n_limit (FAR 25.337) = {n_pos:.2f} ; n_neg = {n_neg:.1f}")
print(f"  V_S1 = {V_S1 / 1.68781:.0f} KEAS, V_A = V_S1 sqrt(n) = {V_A / 1.68781:.0f} KEAS")
print(f"  M0.80 at FL410 is only {V_C_alt / 1.68781:.0f} KEAS; V_C is therefore set by")
print(f"  V_MO at low altitude, {V_MO_KEAS:.0f} KEAS, which is the critical structural case")
print(f"  V_C = {V_C_eas / 1.68781:.0f} KEAS, V_D = V_C/0.8 = {V_D_eas / 1.68781:.0f} KEAS")
print(f"  gust alleviation (FAR 25.341): mu_g = {mu_g:.1f}, K_g = 0.88 mu/(5.3+mu) = {K_g:.3f}")
# n = 1 +/- K_g U_de V a / (498 W/S), with V in KEAS and a in per-radian.
gust_max = 1.0
for Ude, Vref, lbl in ((56.0, V_C_eas, "V_C, 56 fps"), (25.0, V_D_eas, "V_D, 25 fps")):
    dn = K_g * Ude * (Vref / 1.68781) * CL_ALPHA / (498.0 * (MTOW / SW))
    gust_max = max(gust_max, 1 + dn)
    print(f"  gust load at {lbl:<14} n = 1 +/- {dn:.2f}  ->  {1 + dn:.2f} / {1 - dn:.2f}")
gov = "manoeuvre" if n_pos >= gust_max else "gust"
print(f"  governing positive limit: {gov} case, n = {max(n_pos, gust_max):.2f}")

json.dump(dict(BFL=BFL, ground_roll_TO=s_g, landing_total=s_total,
               landing_FAR=1.666 * s_total, V_app_kt=V_APP / 1.68781,
               service_ceiling=ceil_ae, oei_ceiling=ceil_oei,
               range_design=R_design,
               climb=[dict(seg=c[0], req=c[1], achieved=c[2], ok=c[3]) for c in climb_rows],
               payload_range=[dict(point=p[0], payload=p[1], fuel=p[2], TOW=p[3], range=p[4])
                              for p in pts],
               n_pos=n_pos, V_A_kt=V_A / 1.68781, V_C_kt=V_C_eas / 1.68781,
               V_D_kt=V_D_eas / 1.68781),
          open(os.path.join(HERE, "performance.json"), "w"), indent=2)
print(f"\nwritten: {os.path.join(HERE, 'performance.json')}")
