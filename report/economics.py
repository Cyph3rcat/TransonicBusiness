"""Chapter 11 -- pricing and economics (Raymer Ch.18 modified DAPCA IV); the +20%/-10% modern-design/commercial adjustments apply only to DAPCA-estimated terms, not to purchased engines/avionics, and the calibration against the competitive set is reported rather than folded away with Raymer's "divide GA by 4" folk factor."""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


# ================================================================== inputs
# Airframe, from Chapter 8 (report/class2_weights.py) and Chapter 10.
W_E = 6878.5                 # lb, Class-II empty weight
MTOW = 11660.0               # lb
V_MAX = 459.0                # kt, M0.80 true airspeed at FL410 (Chapter 10)
N_PAX = 6                    # passengers
N_OCC = 8                    # occupants (6 pax + 2 crew), for interior cost
N_ENG_AC = 2                 # engines per aircraft

# Engine, Williams FJ44-3A-24, EASA TCDS IM.E.016 Issue 13 [10].
T_MAX = 2490.0               # lbf, takeoff rating (GROUNDED, TCDS)
M_MAX = 0.80                 # engine maximum Mach number = aircraft M_MO
TIT_R = 2400.0               # deg R turbine inlet temp -- ASSUMPTION, see below
TIT_BAND = (2200.0, 2300.0, 2400.0, 2500.0, 2600.0)
TURBOFAN_UPLIFT = 1.18       # Raymer: raise Eq.(18.8) by 15-20% for a turbofan

# Purchased equipment.
W_UAV = 300.0                # lb, UNINSTALLED avionics (the Ch.15 input, not the 433 lb installed group weight)
AVIONICS_PER_LB = 6000.0     # 2012 $/lb, midpoint of Raymer's $4,000-$8,000
INTERIOR_PER_PAX = 3500.0    # 2012 $, Raymer's jet-transport allowance

# Program.
Q_BASE = 200                 # aircraft in five years -- ASSUMPTION, see below
Q_BAND = (50, 100, 200, 500, 1000)
FTA = 3                      # flight-test aircraft (Raymer: typically 2-6)

# Raymer Ch.18 wrap rates, 2012 dollars per hour.
R_ENG, R_TOOL, R_QC, R_MFG = 115.0, 118.0, 108.0, 98.0

# Adjustment factors (Raymer Ch.18, applied to DAPCA-estimated terms only).
F_MATERIAL = 1.0             # aluminium airframe, consistent with the Ch.15 weight equations
F_MODERN = 1.2               # "adjust for more modern designs"
F_COMMERCIAL = 0.9           # "DAPCA tends to overpredict commercial aircraft"
F_DAPCA = F_MATERIAL * F_MODERN * F_COMMERCIAL

# Escalation. CPI-U annual average 2012 = 229.594 (BLS); the 2026 figure is an extrapolation, not a published annual average.
CPI_2012, CPI_2026 = 229.594, 330.0
ESC = CPI_2026 / CPI_2012

# Operations.
UTIL_BASE = 500.0            # flight hours per year
UTIL_BAND = (300.0, 500.0, 800.0, 1200.0)      # Raymer Table 18.1: 500-2000 for a business jet
MMH_FH = 4.0                 # Raymer Table 18.1: 3-6 for a business jet
MMH_BAND = (3.0, 4.0, 6.0)
FUEL_PRICE = 6.00            # 2026 $/US gal, Jet-A at a US FBO -- ASSUMPTION
FUEL_BAND = (4.0, 6.0, 8.0)
FUEL_DENSITY = 6.7           # lb/gal, Jet-A (the Chapter 10 value)
DEPREC_YEARS_AF = 12         # Raymer's straight-line airframe schedule
RESALE_FRACTION = 0.10
DEPREC_YEARS_ENG = 4         # Raymer's engine schedule -- challenged below
ENGINE_TBO_HR = 4000.0       # h between overhauls -- ASSUMPTION, class-typical
ENGINE_OVERHAUL_FRAC = 0.35  # overhaul cost as a fraction of new engine price
SINGLE_PILOT_FACTOR = 0.55   # PLACEHOLDER -- Eq. (18.10) has no single-pilot form; see the note in §11.6(d)
INVESTMENT_FACTOR = 1.20     # Raymer: 1.1-1.4, cost of money plus profit
INVESTMENT_BAND = (1.1, 1.2, 1.4)

# Design mission, from Chapter 10 (report/performance.py).
R_DESIGN = 1683.0            # nm, cruise-climb range at max payload
FUEL_DESIGN = 3061.5         # lb loaded at max payload / MTOW
RESERVE_FACTOR = 1.06        # the Chapter 2 reserve allowance
CLIMB_DESCENT_HR = 0.50      # h of climb + descent, credited no ground distance
GROUND_AIR_MANOEUVRE_HR = 0.35   # Raymer: 15 min ground + 6 min air
R_TYPICAL = 600.0            # nm, a representative revenue sector

print("=" * 78)
print("Chapter 11  Airplane pricing and economics   (Raymer Ch.18, DAPCA IV)")
print("=" * 78)
print(f"  inputs: W_e = {W_E:,.0f} lb, V_max = {V_MAX:.0f} kt, "
      f"MTOW = {MTOW:,.0f} lb")
print(f"  escalation: CPI {CPI_2012:.1f} (2012) -> {CPI_2026:.1f} (2026), "
      f"factor {ESC:.3f}")


# ==================================================== 11.3 DAPCA IV buildup
def engine_cost_2012(tit=TIT_R):
    """Raymer Eq. (18.8), production cost of one engine, 2012 dollars."""
    c = 3112.0 * (0.043 * T_MAX + 243.25 * M_MAX + 0.969 * tit - 2228.0)
    return c * TURBOFAN_UPLIFT


def dapca(Q, tit=TIT_R, f_dapca=F_DAPCA):
    """Modified DAPCA IV: 2012-dollar cost elements for Q aircraft, plus derived per-aircraft figures."""
    H_E = 4.86 * W_E ** 0.777 * V_MAX ** 0.894 * Q ** 0.163      # Eq. 18.1
    H_T = 5.99 * W_E ** 0.777 * V_MAX ** 0.696 * Q ** 0.263      # Eq. 18.2
    H_M = 7.37 * W_E ** 0.820 * V_MAX ** 0.484 * Q ** 0.641      # Eq. 18.3
    H_Q = 0.133 * H_M                                            # Eq. 18.4 (non-cargo)

    C_D = 91.3 * W_E ** 0.630 * V_MAX ** 1.3                     # Eq. 18.5
    C_F = 2498.0 * W_E ** 0.325 * V_MAX ** 0.822 * FTA ** 1.21   # Eq. 18.6
    C_M = 22.1 * W_E ** 0.921 * V_MAX ** 0.621 * Q ** 0.799      # Eq. 18.7

    labour = H_E * R_ENG + H_T * R_TOOL + H_M * R_MFG + H_Q * R_QC
    dapca_terms = (labour + C_D + C_F + C_M) * f_dapca

    c_eng_unit = engine_cost_2012(tit)
    engines = c_eng_unit * Q * N_ENG_AC                          # Eq. 18.9
    avionics = W_UAV * AVIONICS_PER_LB * Q
    interiors = INTERIOR_PER_PAX * N_PAX * Q                     # Raymer, p.700

    total = dapca_terms + engines + avionics + interiors
    return dict(
        Q=Q, H_E=H_E, H_T=H_T, H_M=H_M, H_Q=H_Q,
        C_eng_hours=H_E * R_ENG, C_tool=H_T * R_TOOL,
        C_mfg=H_M * R_MFG, C_qc=H_Q * R_QC,
        C_devsup=C_D, C_flttest=C_F, C_matl=C_M,
        labour=labour, dapca_terms=dapca_terms,
        c_eng_unit=c_eng_unit, engines=engines,
        avionics=avionics, interiors=interiors,
        total_2012=total, unit_2012=total / Q,
        unit_2026=total / Q * ESC, total_2026=total * ESC)


base = dapca(Q_BASE)

print(f"\n11.3  RDT&E + flyaway, DAPCA IV at Q = {Q_BASE} aircraft in five years")
print(f"  {'element':<34}{'hours':>13}{'2012 $M':>12}{'% of total':>12}")
print("  " + "-" * 71)
rows = [
    ("Engineering (Eq. 18.1)",      base["H_E"], base["C_eng_hours"]),
    ("Tooling (Eq. 18.2)",          base["H_T"], base["C_tool"]),
    ("Manufacturing (Eq. 18.3)",    base["H_M"], base["C_mfg"]),
    ("Quality control (Eq. 18.4)",  base["H_Q"], base["C_qc"]),
    ("Development support (Eq. 18.5)", None,     base["C_devsup"]),
    ("Flight test (Eq. 18.6)",      None,        base["C_flttest"]),
    ("Manufacturing materials (Eq. 18.7)", None, base["C_matl"]),
]
raw_dapca = sum(r[2] for r in rows)
for name, hrs, cost in rows:
    h = f"{hrs:,.0f}" if hrs else "--"
    print(f"  {name:<34}{h:>13}{cost / 1e6:12,.1f}{cost / base['total_2012']:12.1%}")
print(f"  {'subtotal, DAPCA-estimated':<34}{'':>13}{raw_dapca / 1e6:12,.1f}")
print(f"  {'x adjustment ' + f'{F_DAPCA:.2f}' + ' (1.2 modern x 0.9 comml)':<34}"
      f"{'':>13}{base['dapca_terms'] / 1e6:12,.1f}"
      f"{base['dapca_terms'] / base['total_2012']:12.1%}")
print(f"  {'Engines (Eq. 18.8, purchased)':<34}{'':>13}"
      f"{base['engines'] / 1e6:12,.1f}{base['engines'] / base['total_2012']:12.1%}")
print(f"  {'Avionics (purchased)':<34}{'':>13}"
      f"{base['avionics'] / 1e6:12,.1f}{base['avionics'] / base['total_2012']:12.1%}")
print(f"  {'Interiors':<34}{'':>13}"
      f"{base['interiors'] / 1e6:12,.1f}{base['interiors'] / base['total_2012']:12.1%}")
print("  " + "-" * 71)
print(f"  {'PROGRAM TOTAL (2012 $)':<34}{'':>13}{base['total_2012'] / 1e6:12,.1f}"
      f"{1.0:12.1%}")
print(f"  per aircraft, 2012 $ = {base['unit_2012'] / 1e6:.2f} M")
print(f"  per aircraft, 2026 $ = {base['unit_2026'] / 1e6:.2f} M   "
      f"(x{ESC:.3f} CPI)")

# Raymer's own validity check on the avionics allowance.
av_frac = base["avionics"] / base["total_2012"]
print(f"\n  check: avionics is {av_frac:.0%} of flyaway; Raymer's stated range is"
      f" 5-25%  -> {'inside' if 0.05 <= av_frac <= 0.25 else 'OUTSIDE'}")

# ============================== 11.3.2 the turbine inlet temperature problem
print(f"\n11.3.2  Engine cost sensitivity to turbine inlet temperature")
print(f"  TCDS gives INTERTURBINE temperature (877 C = 2,070 R takeoff), which is")
print(f"  measured downstream of the HP turbine and is NOT Eq. (18.8)'s T_ti.")
print(f"  {'TIT (R)':>9}{'2012 $/engine':>16}{'2026 $/engine':>16}"
      f"{'2026 $M/aircraft':>19}{'unit price':>13}")
tit_rows = []
for tit in TIT_BAND:
    ce = engine_cost_2012(tit)
    d = dapca(Q_BASE, tit=tit)
    price = d["unit_2026"] * INVESTMENT_FACTOR
    tit_rows.append(dict(tit=tit, c_eng_2012=ce, c_eng_2026=ce * ESC,
                         unit_2026=d["unit_2026"], price_2026=price))
    print(f"  {tit:9,.0f}{ce:16,.0f}{ce * ESC:16,.0f}"
          f"{d['unit_2026'] / 1e6:19.2f}{price / 1e6:13.2f}")
print(f"  the term 0.969*T_ti supplies "
      f"{0.969 * TIT_R / (0.043 * T_MAX + 243.25 * M_MAX + 0.969 * TIT_R):.0%} "
      f"of the positive terms in Eq. (18.8) -- it is the equation")

# =========================================== 11.3.3 production-quantity sweep
print(f"\n11.3.3  Production quantity (the learning effect is inside the Q exponents)")
print(f"  {'Q':>6}{'program $M (2026)':>20}{'unit cost $M':>15}"
      f"{'price at x1.2 $M':>19}{'vs Q=200':>11}")
q_rows = []
for Q in Q_BAND:
    d = dapca(Q)
    price = d["unit_2026"] * INVESTMENT_FACTOR
    q_rows.append(dict(Q=Q, total_2026=d["total_2026"], unit_2026=d["unit_2026"],
                       price_2026=price))
    print(f"  {Q:6d}{d['total_2026'] / 1e6:20,.0f}{d['unit_2026'] / 1e6:15.2f}"
          f"{price / 1e6:19.2f}{d['unit_2026'] / base['unit_2026'] - 1:11.0%}")

# ==================================================== 11.4 acquisition price
print(f"\n11.4  Acquisition price and the benchmark reconciliation")
price_rows = []
for f in INVESTMENT_BAND:
    price_rows.append(dict(factor=f, price=base["unit_2026"] * f))
    print(f"  investment cost factor {f:.1f}  ->  price = "
          f"{base['unit_2026'] * f / 1e6:6.2f} M (2026 $)")
PRICE = base["unit_2026"] * INVESTMENT_FACTOR

# Approximate list prices carried from the Chapter 1 market survey; ASSUMPTION-grade, not audited.
COMPETITORS = [("HondaJet Elite II", 5.5e6, 11100.0),
               ("Embraer Phenom 300E", 10.5e6, 18387.0),
               ("Cessna Citation CJ4 Gen3", 12.0e6, 17110.0)]
print(f"\n  {'aircraft':<28}{'list price $M':>15}{'MTOW lb':>11}{'$/lb MTOW':>12}")
for name, p, w in COMPETITORS:
    print(f"  {name:<28}{p / 1e6:15.1f}{w:11,.0f}{p / w:12,.0f}")
print(f"  {'THIS DESIGN (DAPCA)':<28}{PRICE / 1e6:15.1f}{MTOW:11,.0f}"
      f"{PRICE / MTOW:12,.0f}")

# Two benchmarks bracket the price: (i) by weight, $/lb MTOW = floor; (ii) by capability, CJ4/Phenom mission parity = ceiling. The design's premise is CJ4 capability at HondaJet weight, so neither alone is the answer.
per_lb = sum(p / w for _, p, w in COMPETITORS) / len(COMPETITORS)
PRICE_BENCH_LOW = per_lb * MTOW
PRICE_BENCH_HIGH = 12.0e6                      # CJ4 Gen3, capability parity
PRICE_MARKET = 0.5 * (PRICE_BENCH_LOW + PRICE_BENCH_HIGH)
CAL_LOW = PRICE / PRICE_BENCH_HIGH
CAL_HIGH = PRICE / PRICE_BENCH_LOW
CALIBRATION = PRICE / PRICE_MARKET
print(f"\n  competitive-set mean = ${per_lb:,.0f} per lb MTOW")
print(f"  benchmark (i)  by weight, ${per_lb:,.0f}/lb x {MTOW:,.0f} lb "
      f"= {PRICE_BENCH_LOW / 1e6:5.2f} M   [floor]")
print(f"  benchmark (ii) by capability, CJ4 parity      "
      f"= {PRICE_BENCH_HIGH / 1e6:5.2f} M   [ceiling]")
print(f"  market-anchored price, midpoint              "
      f"= {PRICE_MARKET / 1e6:5.2f} M")
print(f"  DAPCA price                                  = {PRICE / 1e6:5.2f} M")
print(f"  IMPLIED DAPCA OVERPREDICTION = {CALIBRATION:.2f}x "
      f"(band {CAL_LOW:.2f}x to {CAL_HIGH:.2f}x)")
print(f"  Raymer's own note says GA users divide DAPCA by 4; this study finds")
print(f"  {CALIBRATION:.1f}x for a light jet, so the folk factor is too aggressive here.")

# ======================================================== 11.5 operating cost
print(f"\n11.5  Direct operating cost")

# -- mission timing
burn_design = FUEL_DESIGN / RESERVE_FACTOR                 # lb actually burned
t_cruise = R_DESIGN / V_MAX
t_flight = t_cruise + CLIMB_DESCENT_HR
t_block = t_flight + GROUND_AIR_MANOEUVRE_HR
fuel_per_fh = burn_design / t_flight
V_BLOCK = R_DESIGN / t_block
print(f"  design mission: {R_DESIGN:,.0f} nm, cruise {t_cruise:.2f} h + "
      f"{CLIMB_DESCENT_HR:.2f} h climb/descent = {t_flight:.2f} h flight")
print(f"  block time {t_block:.2f} h, block speed {V_BLOCK:.0f} kt, "
      f"burn {burn_design:,.0f} lb -> {fuel_per_fh:,.0f} lb/h "
      f"({fuel_per_fh / FUEL_DENSITY:.0f} gal/h)")

t_flight_typ = R_TYPICAL / V_MAX + CLIMB_DESCENT_HR
t_block_typ = t_flight_typ + GROUND_AIR_MANOEUVRE_HR
print(f"  typical {R_TYPICAL:,.0f} nm sector: {t_flight_typ:.2f} h flight, "
      f"{t_block_typ:.2f} h block, block speed "
      f"{R_TYPICAL / t_block_typ:.0f} kt")


def crew_cost_block_hr_2012():
    """Raymer Eq. (18.10), two-man crew, 2012 dollars per block hour."""
    return 70.4 * (V_MAX * (MTOW / 1e5)) ** 0.3 + 168.8


def doc(price_2026, util=UTIL_BASE, fuel_price=FUEL_PRICE, mmh=MMH_FH,
        t_fl=None, t_bl=None, two_crew=True, engine_method="overhaul",
        calibration=None):
    """Direct operating cost, $/flight hour, 2026 dollars; `calibration` scales the DAPCA engine price by the same §11.4 factor so the depreciated aircraft is coherent (otherwise it charges $4.2M of engines against a $9.4M aeroplane)."""
    t_fl = t_flight if t_fl is None else t_fl
    t_bl = t_block if t_bl is None else t_bl
    cal = CALIBRATION if calibration is None else calibration
    c_e_2012 = engine_cost_2012() / cal
    c_e_2026 = c_e_2012 * ESC
    cycles_per_yr = util / t_fl

    fuel = (fuel_per_fh / FUEL_DENSITY) * fuel_price

    # Eq. (18.10) is a two-man form. There is no single-pilot form in Raymer.
    crew_2012 = crew_cost_block_hr_2012() * (1.0 if two_crew else SINGLE_PILOT_FACTOR)
    crew = crew_2012 * ESC * (t_bl / t_fl)

    # Maintenance labour: MMH/FH x wrap rate (Raymer: approximated by the manufacturing wrap-rate absent better data).
    m_lab = mmh * R_MFG * ESC

    # Maintenance materials, Eq. (18.12) per flight hour + (18.13) per cycle.
    c_a = price_2026 / ESC - N_ENG_AC * c_e_2012       # airframe less engines
    per_fh = 3.3 * (c_a / 1e6) + 14.2 + (58.0 * (c_e_2012 / 1e6) - 26.1) * N_ENG_AC
    per_cyc = 4.0 * (c_a / 1e6) + 9.3 + (7.5 * (c_e_2012 / 1e6) + 5.6) * N_ENG_AC
    m_mat = (per_fh + per_cyc / t_fl) * ESC

    af_cost = price_2026 - N_ENG_AC * c_e_2026
    dep_af = af_cost * (1.0 - RESALE_FRACTION) / DEPREC_YEARS_AF / util
    if engine_method == "raymer":
        dep_eng = (N_ENG_AC * c_e_2026) / DEPREC_YEARS_ENG / util
    else:   # on-condition overhaul reserve, the way this class is really run
        dep_eng = N_ENG_AC * c_e_2026 * ENGINE_OVERHAUL_FRAC / ENGINE_TBO_HR

    subtotal = fuel + crew + m_lab + m_mat + dep_af + dep_eng
    insurance = 0.02 * subtotal        # Raymer: insurance adds 1-3% to ops cost
    landing = 0.02 * (subtotal + insurance)      # Raymer: fees add about 2%
    total = subtotal + insurance + landing
    return dict(fuel=fuel, crew=crew, maint_labour=m_lab, maint_materials=m_mat,
                deprec_airframe=dep_af, deprec_engine=dep_eng,
                insurance=insurance, landing=landing, total=total,
                cycles_per_yr=cycles_per_yr,
                per_cyc_2012=per_cyc, per_fh_2012=per_fh,
                c_a_2012=c_a, c_e_2026=c_e_2026)


# DOC is built at the market-anchored price, not the DAPCA price (§11.4 showed DAPCA overpredicts what the aeroplane would sell for); engine price is scaled the same way for a coherent depreciated aircraft.
d = doc(PRICE_MARKET)
print(f"\n  built at the market-anchored price of {PRICE_MARKET / 1e6:.2f} M, with the")
print(f"  engine price scaled by the same {CALIBRATION:.2f}x -> "
      f"${d['c_e_2026']:,.0f} each ({N_ENG_AC * d['c_e_2026'] / PRICE_MARKET:.0%} of the aircraft)")
print(f"  utilisation {UTIL_BASE:,.0f} FH/yr, fuel ${FUEL_PRICE:.2f}/gal, "
      f"{MMH_FH:.0f} MMH/FH, two-pilot crew, engines on overhaul reserve")
print(f"  {'element':<30}{'$/FH':>10}{'% of DOC':>11}{'$/yr':>14}")
print("  " + "-" * 65)
for k, label in (("fuel", "Fuel (Jet-A)"),
                 ("crew", "Crew (Eq. 18.10)"),
                 ("maint_labour", "Maintenance labour"),
                 ("maint_materials", "Maintenance materials"),
                 ("deprec_airframe", "Depreciation, airframe"),
                 ("deprec_engine", "Depreciation, engines"),
                 ("insurance", "Insurance"),
                 ("landing", "Landing and handling fees")):
    print(f"  {label:<30}{d[k]:10,.0f}{d[k] / d['total']:11.1%}"
          f"{d[k] * UTIL_BASE:14,.0f}")
print("  " + "-" * 65)
print(f"  {'TOTAL DIRECT OPERATING COST':<30}{d['total']:10,.0f}{1.0:11.1%}"
      f"{d['total'] * UTIL_BASE:14,.0f}")

seat_mile = d["total"] / (V_BLOCK * N_PAX)
seat_mile_occ = d["total"] / (V_BLOCK * N_OCC)
trip = d["total"] * t_flight
print(f"\n  cost per block hour          = ${d['total'] * t_flight / t_block:,.0f}")
print(f"  cost per design-mission trip = ${trip:,.0f} ({R_DESIGN:,.0f} nm)")
print(f"  cost per seat-nautical-mile  = ${seat_mile:.2f} (6 revenue seats)")
print(f"  cost per nautical mile       = ${d['total'] / V_BLOCK:.2f}")

# Raymer's own split, as a check on the buildup.
print(f"\n  check against Raymer's typical commercial split "
      f"(fuel 38 / crew 24 / maint 25 / deprec 12 / ins 1%):")
print(f"    this aircraft: fuel {d['fuel'] / d['total']:.0%}, "
      f"crew {d['crew'] / d['total']:.0%}, "
      f"maint {(d['maint_labour'] + d['maint_materials']) / d['total']:.0%}, "
      f"deprec {(d['deprec_airframe'] + d['deprec_engine']) / d['total']:.0%}, "
      f"ins {d['insurance'] / d['total']:.0%}")
print(f"    a business jet flying {UTIL_BASE:,.0f} h/yr against an airliner's 3,000+ must")
print(f"    show a smaller fuel share and a larger ownership share. It does.")

# The engine depreciation basis is worth challenging explicitly.
d_sl = doc(PRICE_MARKET, engine_method="raymer")
print(f"\n  engine cost basis: Raymer depreciates engines straight-line over "
      f"{DEPREC_YEARS_ENG} years.")
print(f"  At {UTIL_BASE:,.0f} FH/yr that is {DEPREC_YEARS_ENG * UTIL_BASE:,.0f} h, "
      f"well inside a {ENGINE_TBO_HR:,.0f} h overhaul interval, so it")
print(f"  writes off an engine that has not been used up. This study uses an")
print(f"  overhaul reserve instead, which is how the class is actually operated:")
print(f"    straight-line   ${d_sl['deprec_engine']:,.0f}/FH  ->  DOC ${d_sl['total']:,.0f}/FH")
print(f"    overhaul reserve ${d['deprec_engine']:,.0f}/FH  ->  DOC ${d['total']:,.0f}/FH  "
      f"({d['total'] / d_sl['total'] - 1:+.0%})")

# Short sectors are where this class actually operates.
print(f"\n  the same aeroplane on a {R_TYPICAL:,.0f} nm sector "
      f"({t_flight_typ:.2f} h flight, {t_block_typ:.2f} h block):")
d_typ = doc(PRICE_MARKET, t_fl=t_flight_typ, t_bl=t_block_typ)
v_blk_typ = R_TYPICAL / t_block_typ
print(f"    DOC ${d_typ['total']:,.0f}/FH ({d_typ['total'] / d['total'] - 1:+.0%}), "
      f"trip ${d_typ['total'] * t_flight_typ:,.0f}, "
      f"seat-nm ${d_typ['total'] / (v_blk_typ * N_PAX):.2f} "
      f"({d_typ['total'] / (v_blk_typ * N_PAX) / seat_mile - 1:+.0%})")
print(f"    per-hour cost barely moves; per-seat-mile rises, because the fixed")
print(f"    per-cycle charges and the 0.85 h of climb/descent/manoeuvre are")
print(f"    spread over a third of the distance.")

# =================================================== 11.6 sensitivity studies
print(f"\n11.6  Sensitivity")

print(f"\n  (a) utilisation -- the strongest single lever")
print(f"  {'FH/yr':>8}{'$/FH':>10}{'fixed $/FH':>13}{'variable $/FH':>15}"
      f"{'$/seat-nm':>12}")
util_rows = []
for u in UTIL_BAND:
    du = doc(PRICE_MARKET, util=u)
    fixed = du["deprec_airframe"] + du["deprec_engine"] + du["insurance"]
    var = du["total"] - fixed
    util_rows.append(dict(util=u, total=du["total"], fixed=fixed, variable=var,
                          seat_nm=du["total"] / (V_BLOCK * N_PAX)))
    print(f"  {u:8,.0f}{du['total']:10,.0f}{fixed:13,.0f}{var:15,.0f}"
          f"{du['total'] / (V_BLOCK * N_PAX):12.2f}")

print(f"\n  (b) fuel price")
print(f"  {'$/gal':>8}{'fuel $/FH':>12}{'DOC $/FH':>11}{'vs base':>10}")
fuel_rows = []
for f in FUEL_BAND:
    df = doc(PRICE_MARKET, fuel_price=f)
    fuel_rows.append(dict(price=f, fuel=df["fuel"], total=df["total"]))
    print(f"  {f:8.2f}{df['fuel']:12,.0f}{df['total']:11,.0f}"
          f"{df['total'] / d['total'] - 1:10.0%}")

print(f"\n  (c) maintenance man-hours per flight hour (Raymer band 3-6)")
print(f"  {'MMH/FH':>8}{'labour $/FH':>14}{'DOC $/FH':>11}{'vs base':>10}")
mmh_rows = []
for m in MMH_BAND:
    dm = doc(PRICE_MARKET, mmh=m)
    mmh_rows.append(dict(mmh=m, labour=dm["maint_labour"], total=dm["total"]))
    print(f"  {m:8.1f}{dm['maint_labour']:14,.0f}{dm['total']:11,.0f}"
          f"{dm['total'] / d['total'] - 1:10.0%}")

print(f"\n  (d) single-pilot vs two-pilot crewing")
d1 = doc(PRICE_MARKET, two_crew=False)
print(f"    two-pilot     crew ${d['crew']:,.0f}/FH   DOC ${d['total']:,.0f}/FH")
print(f"    single-pilot  crew ${d1['crew']:,.0f}/FH   DOC ${d1['total']:,.0f}/FH"
      f"   ({d1['total'] / d['total'] - 1:+.0%})")
print(f"    annual saving at {UTIL_BASE:,.0f} FH/yr = "
      f"${(d['total'] - d1['total']) * UTIL_BASE:,.0f}")
print(f"    NOTE: the 0.55 single-pilot factor is a PLACEHOLDER. Eq. (18.10) has")
print(f"    no single-pilot form; the ratio of Raymer's two- to three-man forms")
print(f"    is {(70.4 * (V_MAX * (MTOW / 1e5)) ** 0.3 + 168.8) / (94.5 * (V_MAX * (MTOW / 1e5)) ** 0.3 + 237.2):.2f}, "
      f"which is the only internal guide available.")

# ======================================================= 11.6.4 breakeven
print(f"\n11.6.4  Programme breakeven at a market-clearing price")
print(f"  Price is fixed at the market anchor of {PRICE_MARKET / 1e6:.2f} M and the")
print(f"  production quantity is swept. Two cost models are carried, because")
print(f"  Section 11.4 showed they differ by {CALIBRATION:.2f}x and the answer depends on which is right.")
SEGMENT_RATE = 125.0             # aircraft/yr, light-jet segment -- ASSUMPTION


def breakeven(cal):
    for Q in range(10, 20001, 10):
        if PRICE_MARKET * Q >= dapca(Q)["total_2026"] / cal:
            return Q
    return None


q_be_raw = breakeven(1.0)
q_be_cal = breakeven(CALIBRATION)
print(f"  {'Q':>7}{'revenue $M':>13}{'DAPCA cost $M':>16}{'margin':>9}"
      f"{'calibrated cost $M':>21}{'margin':>9}")
be_rows = []
for Q in Q_BAND:
    dQ = dapca(Q)
    rev = PRICE_MARKET * Q
    cost_raw, cost_cal = dQ["total_2026"], dQ["total_2026"] / CALIBRATION
    be_rows.append(dict(Q=Q, revenue=rev, cost_raw=cost_raw, cost_cal=cost_cal,
                        margin_raw=rev - cost_raw, margin_cal=rev - cost_cal))
    print(f"  {Q:7d}{rev / 1e6:13,.0f}{cost_raw / 1e6:16,.0f}"
          f"{(rev - cost_raw) / rev:9.0%}{cost_cal / 1e6:21,.0f}"
          f"{(rev - cost_cal) / rev:9.0%}")
print(f"  breakeven, DAPCA as written = "
      f"{f'{q_be_raw:,d} aircraft' if q_be_raw else 'NEVER (not reached below 20,000)'}")
print(f"  breakeven, calibrated {CALIBRATION:.2f}x    = "
      f"{f'{q_be_cal:,d} aircraft' if q_be_cal else 'not reached below 20,000'}")
if q_be_cal:
    print(f"  For scale: the light-jet segment absorbs of order {SEGMENT_RATE:,.0f} aircraft")
    print(f"  per year in total, so {q_be_cal:,d} units is about "
          f"{q_be_cal / SEGMENT_RATE:.1f} years of the ENTIRE")
    print(f"  segment's demand, or {q_be_cal / 40.0:.0f} years at a plausible 40/yr build rate.")

# =========================== 11.7 the economic cost of the volume shortfall
print(f"\n11.7  The economic consequence of the Chapter 10 volume shortfall")
VOL_CASES = [("As drawn, wing tanks only (42.6 ft3)", 1009.0),
             ("Centre section resolved (53.1 ft3)", 1331.0),
             ("Volume gap closed (65.2 ft3)", 1683.0),
             ("Standard 6-occupant config, gap closed", 1782.0)]
print(f"  {'case':<42}{'range nm':>10}{'$/trip':>11}{'$/seat-nm':>12}{'trips/yr':>10}")
vol_rows = []
for lbl, rng in VOL_CASES:
    t_fl = rng / V_MAX + CLIMB_DESCENT_HR
    t_bl = t_fl + GROUND_AIR_MANOEUVRE_HR
    dv = doc(PRICE_MARKET, t_fl=t_fl, t_bl=t_bl)
    v_blk = rng / t_bl
    seats = N_PAX if "Standard" not in lbl else 4
    trip_cost = dv["total"] * t_fl
    s_nm = dv["total"] / (v_blk * seats)
    trips = UTIL_BASE / t_fl
    vol_rows.append(dict(case=lbl, range_nm=rng, trip=trip_cost, seat_nm=s_nm,
                         trips_per_yr=trips, doc_fh=dv["total"]))
    print(f"  {lbl:<42}{rng:10,.0f}{trip_cost:11,.0f}{s_nm:12.2f}{trips:10,.0f}")
print(f"  the design mission cannot be flown at all in the first two rows; the")
print(f"  1,750 nm sector becomes a tech stop, which adds a landing cycle, a")
print(f"  turnaround and a second departure fee to every long trip.")

# ==================================================================== output
json.dump(dict(
    escalation=ESC, cpi_2012=CPI_2012, cpi_2026=CPI_2026,
    Q_base=Q_BASE, FTA=FTA, f_dapca=F_DAPCA,
    hours=dict(engineering=base["H_E"], tooling=base["H_T"],
               manufacturing=base["H_M"], quality=base["H_Q"]),
    elements_2012=dict(engineering=base["C_eng_hours"], tooling=base["C_tool"],
                       manufacturing=base["C_mfg"], quality=base["C_qc"],
                       dev_support=base["C_devsup"], flight_test=base["C_flttest"],
                       materials=base["C_matl"], engines=base["engines"],
                       avionics=base["avionics"], interiors=base["interiors"]),
    dapca_terms_2012=base["dapca_terms"], total_2012=base["total_2012"],
    unit_2012=base["unit_2012"], unit_2026=base["unit_2026"],
    engine_unit_2012=base["c_eng_unit"], engine_unit_2026=base["c_eng_unit"] * ESC,
    price_dapca_2026=PRICE, price_bench_low=PRICE_BENCH_LOW,
    price_bench_high=PRICE_BENCH_HIGH, price_market=PRICE_MARKET,
    per_lb_mtow=per_lb, calibration=CALIBRATION,
    calibration_band=[CAL_LOW, CAL_HIGH],
    tit_sweep=tit_rows, q_sweep=q_rows, price_sweep=price_rows,
    mission=dict(range_nm=R_DESIGN, t_flight=t_flight, t_block=t_block,
                 block_speed=V_BLOCK, burn_lb=burn_design,
                 fuel_per_fh_lb=fuel_per_fh,
                 fuel_per_fh_gal=fuel_per_fh / FUEL_DENSITY),
    doc=dict(fuel=d["fuel"], crew=d["crew"], maint_labour=d["maint_labour"],
             maint_materials=d["maint_materials"],
             deprec_airframe=d["deprec_airframe"], deprec_engine=d["deprec_engine"],
             insurance=d["insurance"], landing=d["landing"], total=d["total"],
             per_block_hour=d["total"] * t_flight / t_block,
             per_trip=trip, per_seat_nm=seat_mile, per_seat_nm_occ=seat_mile_occ,
             per_nm=d["total"] / V_BLOCK),
    doc_straightline_basis=dict(deprec_engine=d_sl["deprec_engine"],
                                total=d_sl["total"]),
    doc_typical_sector=dict(range_nm=R_TYPICAL, t_flight=t_flight_typ,
                            t_block=t_block_typ, total=d_typ["total"],
                            per_trip=d_typ["total"] * t_flight_typ,
                            per_seat_nm=d_typ["total"] / (v_blk_typ * N_PAX)),
    doc_single_pilot=dict(crew=d1["crew"], total=d1["total"],
                          annual_saving=(d["total"] - d1["total"]) * UTIL_BASE),
    util_sweep=util_rows, fuel_sweep=fuel_rows, mmh_sweep=mmh_rows,
    breakeven_Q_dapca=q_be_raw, breakeven_Q_calibrated=q_be_cal,
    breakeven_rows=be_rows, volume_cases=vol_rows),
    open(os.path.join(HERE, "economics.json"), "w"), indent=2)
print(f"\nwritten: {os.path.join(HERE, 'economics.json')}")
