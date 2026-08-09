"""Class-I weight buildup + CG for full_v5: Roskam group-weight fractions (ASSUMPTION grade) anchored to W_E=0.59*MTOW (weight.md 2.5), engine dry weight TCDS-grounded (FJ44-3A-24 520 lb), MAC=5.024 ft / x_LEMAC=21.61 from the wing planform (cr 6.9086, ct 2.418, semispan 20.766, LE sweep tan 0.2996, root LE x=19.0)."""
MTOW = 11660.0
WE_FRAC = 0.59
W_E = WE_FRAC * MTOW
W_FUEL = 0.2634 * MTOW        # weight.md 2.4
MAC = 5.024
# DX shifts the wing-riding group (wing/fuel/gear/nacelles/engines) aft to put MTOW CG at 28% MAC (root LE 19.0 gave -2% MAC; solving W-balance gives 15.9)
DX = -3.1
X_LEMAC = 21.61 + DX

# ---- empty-weight groups: (name, weight lb, x ft, basis) ----
groups = [
    ("Wing",              0.095 * MTOW, 23.62 + DX, "40% MAC (Raymer CG rule)"),
    ("Horizontal tail",   0.009 * MTOW, 41.00, "40% HT MAC"),
    ("Vertical tail+dorsal", 0.012 * MTOW, 37.60, "40% VT MAC (grown 59 ft2 fin)"),
    ("Fuselage",          0.102 * MTOW, 19.00, "45% fuselage length"),
    ("Nacelles+pylons",   0.016 * MTOW, 28.50 + DX, "45% nacelle length"),
    ("Nose gear",         0.009 * MTOW,  6.50, "bay in the nose cone"),
    ("Main gear",         0.035 * MTOW, 24.80 + DX, "aft of rear spar, retracts into fairing"),
    ("Engines installed", 2 * 520 * 1.25, 28.40 + DX, "FJ44-3A-24 dry 520 (TCDS) x1.25 install"),
]
w_sum = sum(g[1] for g in groups)
w_fixed = W_E - w_sum
# fixed equipment split (ASSUMPTION): avionics nose / furnishings cabin / systems aft-mid
fixed = [
    ("Avionics (nose bay)",       0.16 * w_fixed,  5.50),
    ("Furnishings (cabin)",       0.42 * w_fixed, 16.90),
    ("Systems (ECS/hyd/el, aft)", 0.42 * w_fixed, 21.50),
]
empty = groups + [(n, w, x, "fixed-equipment split") for n, w, x in fixed]

def cg(items):
    W = sum(w for _, w, *_ in items)
    return W, sum(w * i[2] for i in (items) for w in [i[1]]) / W

print(f"{'group':28s} {'W (lb)':>8s} {'x (ft)':>7s}   basis")
for n, w, x, b in empty:
    print(f"{n:28s} {w:8.0f} {x:7.2f}   {b}")
W_e, x_e = cg([(n, w, x) for n, w, x, b in empty])
print(f"{'EMPTY':28s} {W_e:8.0f} {x_e:7.2f}   ({(x_e - X_LEMAC) / MAC * 100:.1f}% MAC)")

# ---- loading items ----
crew  = ("Crew 2x200",            400.0,  7.50)
pax   = ("Pax 6x180",            1080.0, 17.00)
bags  = ("Baggage 6x40",          240.0, 25.00)
fuel  = ("Fuel (wing box)",     W_FUEL, 23.62 + DX)

states = {
    "Empty":                     [],
    "OEW (empty+crew)":          [crew],
    "OEW + fuel (ferry)":        [crew, fuel],
    "Zero-fuel (crew+payload)":  [crew, pax, bags],
    "MTOW (all)":                [crew, pax, bags, fuel],
}
print()
xs = {}
for name, extra in states.items():
    items = [(n, w, x) for n, w, x, b in empty] + list(extra)
    W, x = cg(items)
    xs[name] = x
    print(f"{name:28s} W={W:7.0f} lb   Xcg={x:6.2f} ft   {(x - X_LEMAC) / MAC * 100:5.1f}% MAC")

lo, hi = min(xs.values()), max(xs.values())
print(f"\nCG range: {lo:.2f} to {hi:.2f} ft  ({(lo - X_LEMAC) / MAC * 100:.1f}% to {(hi - X_LEMAC) / MAC * 100:.1f}% MAC, {(hi - lo) / MAC * 100:.1f}% MAC wide)")
print(f"Quarter-MAC (old placeholder Xcg): {X_LEMAC + 0.25 * MAC:.2f} ft")
