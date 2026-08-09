"""Scan tail-cone law parameters: h = D*cos(pi/2 * s^Q), zc = Ztip * s^A.
Constraints: top line monotone falling, mean lower upsweep 26.5-40.5 in 13-15 deg,
max lower upsweep reasonable (< ~19 deg)."""
import numpy as np

L, D, X_te, Ztip = 42.2, 6.10, 23.4, 1.98
x = np.linspace(X_te, L, 800)
s = (x - X_te) / (L - X_te)

best = []
for Q in np.arange(1.1, 1.9, 0.05):
    for A in np.arange(1.6, 3.2, 0.1):
        h = D * np.cos(0.5 * np.pi * s ** Q)
        zc = Ztip * s ** A
        top = zc + h / 2
        bot = zc - h / 2
        dtop = np.diff(top) / np.diff(x)
        dbot = np.degrees(np.arctan(np.diff(bot) / np.diff(x)))
        m = (x[:-1] > 26.5) & (x[:-1] < 40.5)
        pre = x[:-1] < 39.0   # exclude the tip-cap region, steep closure there is normal
        mean_up = dbot[m].mean()
        ok = dtop.max() <= 0.005 and 13.0 <= mean_up <= 16.2 and dbot[pre].max() < 19.0
        if ok:
            best.append((abs(mean_up - 14.5) + 0.15 * dbot[pre].max(), Q, A, mean_up, dbot[pre].max(), dtop.max()))
best.sort()
for row in best[:8]:
    print(f"Q={row[1]:.2f} A={row[2]:.1f}  mean_up={row[3]:.2f}  max_up={row[4]:.2f}  max_dtop={row[5]:+.4f}")
if not best:
    print("no combo satisfies all constraints -- relax something")
