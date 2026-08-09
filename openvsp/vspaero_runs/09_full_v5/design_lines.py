"""Design the full_v5 fuselage lines before committing them to the vspscript.

Goals (user brief 2026-08-05):
- nose must taper DOWN to a low tip (Phenom 300 look, not Airbus): tip well
  below the fuselage centerline, top line falling steeply, bottom line nearly flat
- everything C1-tangent at the barrel (no creases), monotone top line aft
- few, well-spaced stations so the OpenVSP skinning spline doesn't ripple
  (v4 used 8 nose stations and the loft oscillated between them)

Prints the station table for the vspscript and writes a profile plot.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

L = 42.2
D = 6.10
R = D / 2.0
L_nc = 10.4          # nose length (fuselage.md 6)
X_te = 23.4          # tail cone start (cabin end)
Z_tip_nose = -1.30   # nose tip droop (v4 was -0.60: too axial, read as Airbus)
Z_tip_tail = 1.75    # tail tip height (v4 used 1.98; lowered to soften upsweep)

# ---- nose: height/width law + droop law, both tangent at the barrel ----
P_H = 0.85           # sine-power exponent: <1 => rounded tip, 0.7 was too blunt
P_Z = 1.6            # droop exponent (>1 => tangent at barrel)

def nose_h(x):
    return D * np.sin(0.5 * np.pi * (x / L_nc) ** P_H)

def nose_zc(x):
    return Z_tip_nose * (1.0 - x / L_nc) ** P_Z

# ---- tail cone: build TOP and BOTTOM lines directly, derive h and zc ----
# top: gentle monotone fall 3.05 -> Z_tip_tail, tangent at the barrel
# bottom: tangent blend over the first 35% of the cone, then CONSTANT slope to
#   the tip (this is what v4's realized stations looked like; a cosine-height
#   law stays too full mid-body and then closes at 25 deg)
L_t = L - X_te
S_BLEND = 0.35

def _f_bottom(s):
    # integral of a slope profile that smoothsteps 0->1 over [0, S_BLEND] then
    # holds 1; normalized so f(1) = 1
    s = np.atleast_1d(s)
    sb = np.clip(s / S_BLEND, 0.0, 1.0)
    # integral of smoothstep(t) = t^3 - t^4/2 evaluated in stretched coords
    I_blend = S_BLEND * (sb ** 3 - 0.5 * sb ** 4)
    I_lin = np.where(s > S_BLEND, s - S_BLEND, 0.0)
    return (I_blend + I_lin) / (S_BLEND * 0.5 + (1.0 - S_BLEND))

def tail_top(x):
    s = (x - X_te) / L_t
    return R - (R - Z_tip_tail) * s ** 1.8

def tail_bot(x):
    s = (x - X_te) / L_t
    return -R + (R + Z_tip_tail) * _f_bottom(s)

def tail_h(x):
    return tail_top(x) - tail_bot(x)

def tail_zc(x):
    return 0.5 * (tail_top(x) + tail_bot(x))

x_n = np.linspace(0, L_nc, 400)
x_t = np.linspace(X_te, L, 400)

# tangency checks at the barrel joints
eps = 1e-4
print("nose  dh/dx at barrel:", (nose_h(L_nc) - nose_h(L_nc - eps)) / eps)
print("nose  dz/dx at barrel:", (nose_zc(L_nc) - nose_zc(L_nc - eps)) / eps)
print("tail  dh/dx at barrel:", (tail_h(X_te + eps) - tail_h(X_te)) / eps)
print("tail  dz/dx at barrel:", (tail_zc(X_te + eps) - tail_zc(X_te)) / eps)

# aft top line must be monotone falling; lower-line upsweep must land 13-15 deg
top_t = tail_zc(x_t) + tail_h(x_t) / 2
bot_t = tail_zc(x_t) - tail_h(x_t) / 2
dtop = np.diff(top_t) / np.diff(x_t)
print("aft top line max slope (must be <= 0):", dtop.max())
m = (x_t[:-1] > 26.5) & (x_t[:-1] < 40.5)
up = np.degrees(np.arctan(np.diff(bot_t) / np.diff(x_t)))
print("mean lower-line upsweep 26.5-40.5 (deg):", up[m].mean())
print("max  lower-line upsweep (deg):", up.max())

# ---- station tables ----
# Iteration history (measured in ripple_metric.py, top-line max |mesh-analytic|):
#   7 nose stations, non-uniform    -> 0.21 ft ripple
#   13 nose stations, non-uniform   -> 0.054 ft
#   36 stations, UNIFORM 1.2 ft     -> 0.127 ft (worse: uniformity is not the
#                                      mechanism, local density is)
# Overshoot scales ~spacing^2, so: <=0.45 ft spacing where the nose is highly
# curved, 0.6-0.8 ft through the tail cap.
xs_nose = [0.0, 0.25, 0.55, 0.9, 1.3, 1.75, 2.2, 2.65, 3.1, 3.55, 4.0, 4.45,
           4.9, 5.4, 5.9, 6.5, 7.2, 8.0, 8.8, 9.6, L_nc]
xs_barrel = [12.0, 14.0, 16.0, 18.0, 20.0, 21.7, X_te]
xs_tail = [24.4, 25.4, 26.4, 27.4, 28.6, 29.8, 31.0, 32.2, 33.4, 34.6, 35.8,
           37.0, 38.2, 39.3, 40.3, 41.1, 41.7, L]

rows = []
for x in xs_nose:
    rows.append((x, float(nose_h(x)), float(nose_zc(x))))
for x in xs_barrel:
    rows.append((x, D, 0.0))
for x in xs_tail:
    rows.append((float(x), float(tail_h(np.array([x]))[0]), float(tail_zc(np.array([x]))[0])))

n = len(rows)
print(f"\n// {n} stations -> paste into build_full_v5.vspscript")
print(f"// InsertXSec count: {n - 5}; ellipse loop 1..{n - 2}; index loop 0..{n - 1}")


def emit(name, vals, fmt):
    body = ", ".join(fmt % v for v in vals)
    print(f"    array<double> {name} = {{ {body} }};")

emit("xloc", [r[0] for r in rows], "%.2f")
emit("dia",  [r[1] for r in rows], "%.3f")
emit("zloc", [r[2] for r in rows], "%.3f")

# ---- plot ----
fig, ax = plt.subplots(figsize=(14, 4))
for xx, h, zc in [(x_n, nose_h(x_n), nose_zc(x_n)), (x_t, tail_h(x_t), tail_zc(x_t))]:
    ax.plot(xx, zc + h / 2, "b-"); ax.plot(xx, zc - h / 2, "b-"); ax.plot(xx, zc, "g--", lw=0.7)
ax.plot([L_nc, X_te], [R, R], "b-"); ax.plot([L_nc, X_te], [-R, -R], "b-")
ax.plot([L_nc, X_te], [0, 0], "g--", lw=0.7)
sta = xs_nose + xs_barrel + xs_tail
for x in sta:
    if x <= L_nc: h, zc = nose_h(x), nose_zc(x)
    elif x <= X_te: h, zc = D, 0.0
    else: h, zc = tail_h(x), tail_zc(x)
    ax.plot([x, x], [zc - h / 2, zc + h / 2], "r-", lw=0.8)
ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.set_title("full_v5 fuselage side profile (red = XSec stations)")
fig.savefig("profile_v5.png", dpi=110, bbox_inches="tight")
print("wrote profile_v5.png")
