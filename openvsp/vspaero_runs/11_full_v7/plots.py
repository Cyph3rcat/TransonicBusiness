"""Figures for the full_v6 empennage-resizing pass.

Produces:
  v6_sizing.png   tail sizing: NP/SM vs S_HT, and Cn_beta vs S_VT
  v6_cg_sm.png    CG envelope and static margin across the flight envelope
  v6_drag.png     CD0 component buildup and the cruise drag polar
  v6_compare.png  v5 -> v6 before/after summary

Run from this directory after gen_v6.py has produced the variants.
"""
import glob
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import size_tails as st

HERE = os.path.dirname(os.path.abspath(__file__))
MAC, XLEMAC, SREF, BREF = 5.0236, 18.512, 193.678, 41.5324
AR = BREF ** 2 / SREF
S_HT_FINAL, S_VT_FINAL = 34.0, 45.0
# Measured on the rebuilt final configuration, not read off the parametric fit.
# The fit (used to CHOOSE the area) predicts x_np = 20.764; the rebuilt model
# measures 20.604 -- a 1.9 in / 3.2% MAC difference, because the fit was taken
# at S_VT = 59 whereas the final model also shrank the fin, which lowers the
# T-tail and shortens L_HT. The measured value governs everything reported.
XNP_MEASURED = 20.604
XCG_MTOW = 19.749

# Palette: one accent for "chosen", neutral greys for context, red for rejected.
C_MAIN, C_PICK, C_BAD, C_CTX = "#2b6cb0", "#c05621", "#9b2c2c", "#718096"
plt.rcParams.update({"figure.dpi": 130, "font.size": 9,
                     "axes.grid": True, "grid.alpha": 0.25,
                     "axes.spines.top": False, "axes.spines.right": False})


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


def ht_sweep_data():
    out = []
    for d in sorted(glob.glob(os.path.join(HERE, "ht*"))):
        p = os.path.join(d, os.path.basename(d) + ".polar")
        if not os.path.exists(p):
            continue
        c, dd = read_polar(p)
        a = np.deg2rad(dd[:, c["AoA"]])
        cla = np.polyfit(a, dd[:, c["CLtot"]], 1)[0]
        cma = np.polyfit(a, dd[:, c["CMytot"]], 1)[0]
        s = float(os.path.basename(d)[2:])
        s = 62.42 if s < 10 else s
        out.append((s, 19.90 + (-cma / cla) * MAC))
    return np.array(sorted(out))


def vt_sweep_data():
    out = []
    for d in sorted(glob.glob(os.path.join(HERE, "vt*_beta"))):
        p = os.path.join(d, os.path.basename(d) + ".polar")
        if not os.path.exists(p):
            continue
        c, dd = read_polar(p)
        b = np.deg2rad(dd[:, c["Beta"]])
        cmz = dd[:, c["CMztot"]]
        out.append((float(os.path.basename(d)[2:6]),
                    -np.polyfit(b, cmz, 1)[0], abs(cmz[0])))
    return np.array(sorted(out))


def fig_sizing():
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.1))
    # ---- left: NP / SM vs S_HT ----
    d = ht_sweep_data()
    s, xnp = d[:, 0], d[:, 1]
    A, B = np.polyfit(s, xnp, 1)          # xnp = A*s + B
    ss = np.linspace(25, 65, 100)
    xcg = XCG_MTOW                        # solved v6 MTOW CG
    sm = (A * ss + B - xcg) / MAC * 100

    a = ax[0]
    a.axhspan(10, 20, color=C_MAIN, alpha=0.10, zorder=0)
    a.plot(ss, sm, color=C_MAIN, lw=1.8, label="measured fit")
    a.plot(s, (xnp - xcg) / MAC * 100, "o", color=C_MAIN, ms=5,
           label="VSPAERO $\\alpha$-sweeps")
    a.axvline(S_HT_FINAL, color=C_PICK, lw=1.4, ls="--")
    a.plot([S_HT_FINAL], [(XNP_MEASURED - xcg) / MAC * 100], "*",
           color=C_PICK, ms=16, zorder=6,
           label=f"v6 built + measured, {S_HT_FINAL:.0f} ft$^2$")
    a.plot([S_HT_FINAL], [(A * S_HT_FINAL + B - xcg) / MAC * 100], "*",
           color=C_PICK, ms=11, mfc="none", zorder=5, label="   (fit prediction)")
    a.plot([51.68], [(A * 51.68 + B - xcg) / MAC * 100], "s", color=C_BAD, ms=6,
           label="v5 as-scripted, 51.7 ft$^2$")
    a.plot([62.42], [(A * 62.42 + B - xcg) / MAC * 100], "s", color=C_BAD, ms=6,
           mfc="none", label="v5 as-in-file, 62.4 ft$^2$")
    a.text(26, 15, "bizjet target\n10-20% MAC", color=C_MAIN, fontsize=8, va="center")
    a.set_xlabel("horizontal tail area $S_{HT}$  (ft$^2$)")
    a.set_ylabel("static margin at MTOW CG  (% MAC)")
    a.set_title("Tail sizing from the measured neutral point", fontsize=10)
    a.legend(fontsize=7.5, loc="upper left")

    # secondary axis: the volume coefficient the area corresponds to
    def s_to_c(x):
        return x * 19.40 / (SREF * MAC)

    def c_to_s(x):
        return x * SREF * MAC / 19.40
    sec = a.secondary_xaxis("top", functions=(s_to_c, c_to_s))
    sec.set_xlabel("horizontal tail volume coefficient $c_{HT}$", fontsize=8)

    # ---- right: Cn_beta vs S_VT, coloured by solve quality ----
    v = vt_sweep_data()
    b = ax[1]
    good = v[:, 2] < 1e-4
    b.axhspan(0.05, 0.15, color=C_MAIN, alpha=0.10, zorder=0)
    b.axhline(0.06, color=C_BAD, lw=1.1, ls=":", label="stability floor +0.06")
    b.scatter(v[good, 0], v[good, 1], s=55, color=C_MAIN, zorder=4,
              label="well-resolved (|C$_{Mz}|_{\\beta=0}$ < 1e-4)")
    b.scatter(v[~good, 0], v[~good, 1], s=55, facecolors="none",
              edgecolors=C_CTX, zorder=4, label="poorly-resolved solve")
    b.axvline(S_VT_FINAL, color=C_PICK, lw=1.4, ls="--")
    b.plot([S_VT_FINAL], [0.2171], "*", color=C_PICK, ms=15, zorder=5,
           label=f"v6 pick, {S_VT_FINAL:.0f} ft$^2$ ($c_{{VT}}$=0.090)")
    b.set_ylim(0, 0.30)
    b.set_xlabel("vertical tail area $S_{VT}$  (ft$^2$)")
    b.set_ylabel("$C_{n\\beta}$  (1/rad)")
    b.set_title("Directional stability: every size tested is stable", fontsize=10)
    b.legend(fontsize=7.5, loc="lower left")
    r = np.corrcoef(v[:, 2], v[:, 1])[0, 1]
    b.text(0.97, 0.95, f"scatter tracks solve symmetry error\n(r = {r:+.2f}), "
                       f"not fin area", transform=b.transAxes, ha="right",
           va="top", fontsize=7.5, color=C_CTX)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v6_sizing.png"))
    plt.close(fig)
    return A, B


def fig_cg_sm(A, B):
    ht, vt = st.tail_geometry(S_HT_FINAL, S_VT_FINAL)
    w = st.wing_geometry(15.9)
    g, l = st.weight_items(15.9, S_HT_FINAL, S_VT_FINAL, ht, vt)
    crew, pax, bags, fuel = l
    states = [("Empty", []), ("OEW (+crew)", [crew]),
              ("Zero-fuel", [crew, pax, bags]),
              ("Ferry (OEW+fuel)", [crew, fuel]),
              ("MTOW", [crew, pax, bags, fuel])]
    pts = []
    for name, extra in states:
        W, x = st.cg_of(g + extra)
        pts.append((name, W, (x - w["x_lemac"]) / w["mac"] * 100))

    xnp_pct = (XNP_MEASURED - w["x_lemac"]) / w["mac"] * 100
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.1))

    a = ax[0]
    flight = [p for p in pts if p[0] != "Empty"]
    lo = min(p[2] for p in flight)
    hi = max(p[2] for p in flight)
    a.axvspan(lo, hi, color=C_MAIN, alpha=0.12, label=f"flight CG band\n{lo:.1f}-{hi:.1f}% MAC")
    for name, W, pct in pts:
        marker = "o" if name != "Empty" else "x"
        a.plot(pct, W, marker, color=C_MAIN if name != "Empty" else C_CTX, ms=7)
        a.annotate(f" {name}", (pct, W), fontsize=7.5,
                   color=C_MAIN if name != "Empty" else C_CTX)
    a.axvline(xnp_pct, color=C_BAD, lw=1.6)
    a.text(xnp_pct - 0.6, 7600, f"measured NP {xnp_pct:.1f}% MAC",
           rotation=90, color=C_BAD, fontsize=8, ha="right")
    a.set_xlabel("CG position  (% MAC)")
    a.set_ylabel("weight  (lb)")
    a.set_title("CG envelope vs the neutral point", fontsize=10)
    a.legend(fontsize=7.5, loc="lower left")

    b = ax[1]
    pcts = np.linspace(15, 32, 100)
    b.axhspan(10, 20, color=C_MAIN, alpha=0.10, zorder=0)
    b.plot(pcts, xnp_pct - pcts, color=C_MAIN, lw=1.8,
           label="v6 measured (S$_{HT}$=34 ft$^2$)")
    xnp_v5 = (A * 62.42 + B - w["x_lemac"]) / w["mac"] * 100
    b.plot(pcts, xnp_v5 - pcts, color=C_BAD, lw=1.4, ls="--",
           label="v5 as-in-file (S$_{HT}$=62.4 ft$^2$)")
    for name, W, pct in flight:
        b.plot(pct, xnp_pct - pct, "o", color=C_MAIN, ms=6)
        b.annotate(f" {name}", (pct, xnp_pct - pct), fontsize=7.5, color=C_MAIN)
    b.axvspan(lo, hi, color=C_MAIN, alpha=0.12)
    b.set_xlabel("CG position  (% MAC)")
    b.set_ylabel("static margin  (% MAC)")
    b.set_title("Static margin across the flight envelope", fontsize=10)
    b.legend(fontsize=7.5)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v6_cg_sm.png"))
    plt.close(fig)


def fig_drag():
    import drag_buildup as db
    rows = db.read_buildup(db.PD_CSV)
    names, fs = [], []
    for r in rows:
        q, _ = db.Q_RAYMER.get(r["name"], (1.0, ""))
        names.append(r["name"])
        fs.append(r["cf"] * r["ff"] * q * r["swet"])
    fs = np.array(fs)
    cd0c = fs / SREF
    cd0 = cd0c.sum() * 1.03
    c, d = read_polar(db.POLAR)
    cl, cdiw = d[:, c["CLtot"]], d[:, c["CDiw"]]
    m = cl > 0.05
    k = np.polyfit(cl[m] ** 2, cdiw[m], 1)[0]

    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.1))
    a = ax[0]
    order = np.argsort(-cd0c)
    a.barh([names[i] for i in order][::-1], [cd0c[i] * 1e4 for i in order][::-1],
           color=C_MAIN)
    for i, idx in enumerate(order[::-1]):
        a.text(cd0c[idx] * 1e4 + 1.5, i, f"{cd0c[idx]*1e4:.1f}", va="center", fontsize=7.5)
    a.set_xlabel("parasite drag contribution  (counts, $C_{D}\\times10^4$)")
    a.set_title(f"Raymer component buildup: $C_{{D0}}$ = {cd0*1e4:.0f} counts\n"
                f"(FL410 / M0.80, incl. 3% leakage)", fontsize=10)
    a.grid(axis="y", alpha=0)

    b = ax[1]
    cls = np.linspace(0, 0.9, 100)
    cds = cd0 + k * cls ** 2
    b.plot(cds * 1e4, cls, color=C_MAIN, lw=1.8)
    b.set_xlabel("$C_D$  (counts)")
    b.set_ylabel("$C_L$")
    b.set_title("Cruise drag polar (pre-wave-drag)", fontsize=10)
    b2 = b.twiny()
    b2.plot(cls / cds, cls, color=C_PICK, lw=1.6)
    b2.set_xlabel("L/D", color=C_PICK)
    b2.tick_params(axis="x", colors=C_PICK)
    q_dyn = 0.5 * 0.000558 * 774.5 ** 2
    for tag, wfrac in (("MTOW", 1.0), ("end cruise", 0.86)):
        clc = wfrac * db.MTOW / SREF / q_dyn
        b2.plot(clc / (cd0 + k * clc ** 2), clc, "o", color=C_PICK, ms=7)
        b2.annotate(f" {tag}: L/D={clc/(cd0+k*clc**2):.1f}", (clc / (cd0 + k * clc ** 2), clc),
                    fontsize=7.5, color=C_PICK)
    b.set_ylim(0, 0.9)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v6_drag.png"))
    plt.close(fig)


if __name__ == "__main__":
    A, B = fig_sizing()
    print(f"  NP fit: x_np = {A:.6f}*S_HT + {B:.4f} ft")
    fig_cg_sm(A, B)
    fig_drag()
    print("  wrote v6_sizing.png, v6_cg_sm.png, v6_drag.png")
