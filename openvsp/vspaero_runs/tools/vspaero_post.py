"""Post-processing for VSPAERO 7.x runs (.polar + .lod). Usage: python vspaero_post.py <basename> [--clmax2d 2.11] [--cltarget 0.34 0.60 1.27] (basename = path prefix, e.g. ..\01_wing_baseline\wing_v6_baseline). Outputs per run: CL/CDi/CDtot/L/D/e table vs alpha, lift-curve fit (CLalpha, alpha0), span-load plot vs elliptical, and a stall-onset estimate where max local cl hits clmax_2d."""
import argparse
import re
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def read_polar(path):
    rows = []
    with open(path) as f:
        for line in f:
            parts = line.split()
            if len(parts) > 10:
                try:
                    rows.append([float(p) for p in parts])
                except ValueError:
                    header = parts  # last non-numeric wide line is the header
    cols = {name: i for i, name in enumerate(header)}
    return np.array(rows), cols


def read_lod(path):
    """Return dict: aoa -> list of strip rows (last iter only), and column names."""
    cases = {}
    aoa = None
    colnames = None
    with open(path) as f:
        for line in f:
            if line.startswith("AoA_"):
                aoa = float(line.split()[1])
                cases.setdefault(round(aoa, 4), [])
                continue
            if line.lstrip().startswith("Iter") and "Yavg" in line:
                colnames = line.split()
                continue
            parts = line.split()
            if colnames is not None and len(parts) >= len(colnames) - 2 and aoa is not None:
                try:
                    vals = [float(p) if p != "inf" else np.inf for p in parts]
                except ValueError:
                    continue
                cases[round(aoa, 4)].append(vals)
    # keep only the max-Iter rows per case
    out = {}
    for a, rows in cases.items():
        arr = np.array(rows)
        if arr.size == 0:
            continue
        last = arr[:, 0] == arr[:, 0].max()
        out[a] = arr[last]
    return out, colnames


def strip_data(arr, cols, bref, cref):
    i_y = cols.index("Yavg")
    i_c = cols.index("Chord")
    i_cl = cols.index("Cl")
    y = arr[:, i_y]
    chord = arr[:, i_c]
    cl = arr[:, i_cl]
    # starboard side only, sorted root->tip
    m = y > 0
    y, chord, cl = y[m], chord[m], cl[m]
    order = np.argsort(y)
    y, chord, cl = y[order], chord[order], cl[order]
    eta = y / (bref / 2.0)
    load = cl * chord / cref
    return eta, chord, cl, load


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("basename")
    ap.add_argument("--clmax2d", type=float, default=2.11)
    ap.add_argument("--cltargets", type=float, nargs="*", default=[0.34, 0.60, 1.27])
    ap.add_argument("--sref", type=float, default=193.678)
    ap.add_argument("--bref", type=float, default=41.5324)
    ap.add_argument("--cref", type=float, default=5.0236)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()

    polar, pc = read_polar(args.basename + ".polar")
    aoa = polar[:, pc["AoA"]]
    CL = polar[:, pc["CLtot"]]
    CDi = polar[:, pc["CDi"]]
    CDtot = polar[:, pc["CDtot"]]
    E = polar[:, pc["E"]]
    Ew = polar[:, pc["Ew"]] if "Ew" in pc else np.full_like(E, np.nan)
    LD = polar[:, pc["L/D"]]

    print(f"=== {args.basename} ===")
    print(f"{'AoA':>6} {'CL':>8} {'CDi':>9} {'CDtot':>9} {'L/D':>7} {'e_surf':>7} {'e_wake':>7}")
    for i in range(len(aoa)):
        print(f"{aoa[i]:6.1f} {CL[i]:8.4f} {CDi[i]:9.5f} {CDtot[i]:9.5f} "
              f"{LD[i]:7.2f} {E[i]:7.3f} {Ew[i]:7.3f}")

    # lift-curve fit over linear range
    fit = np.polyfit(np.radians(aoa), CL, 1)
    cla, cl0 = fit
    a0 = -cl0 / cla
    print(f"\nCL_alpha = {cla:.3f} /rad ({cla*np.pi/180:.4f} /deg), "
          f"alpha_L0 = {np.degrees(a0):.2f} deg")

    lod, cols = read_lod(args.basename + ".lod")
    aoas_lod = sorted(lod.keys())

    # interpolate alpha for each CL target, get load dist at nearest computed alphas
    AR = args.bref**2 / args.sref
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))
    stall_info = []
    # max local cl vs alpha -> stall onset
    maxcl = []
    for a in aoas_lod:
        eta, chord, cl, load = strip_data(lod[a], cols, args.bref, args.cref)
        maxcl.append((a, cl.max(), eta[np.argmax(cl)]))
    maxcl = np.array(maxcl)
    # linear fit of max local cl vs alpha (use upper half of range)
    sel = maxcl[:, 0] >= np.median(maxcl[:, 0])
    p = np.polyfit(maxcl[sel, 0], maxcl[sel, 1], 1)
    a_stall = (args.clmax2d - p[1]) / p[0]
    CL_at_stall = np.interp(a_stall, aoa, CL, right=np.nan)
    if np.isnan(CL_at_stall):  # extrapolate linearly
        CL_at_stall = cla * np.radians(a_stall) + cl0
    eta_stall = np.interp(a_stall, maxcl[:, 0], maxcl[:, 2])
    print(f"\nStall onset (local cl = clmax2d {args.clmax2d}): "
          f"alpha ~ {a_stall:.1f} deg, wing CL ~ {CL_at_stall:.2f}, "
          f"first-stall station eta ~ {eta_stall:.2f}")

    for tgt in args.cltargets:
        a_t = np.interp(tgt, CL, aoa)
        print(f"CL={tgt:.2f}: alpha ~ {a_t:.2f} deg, "
              f"margin to stall-onset alpha: {a_stall - a_t:.1f} deg")

    # plots at three representative alphas: low, cruise-ish, high
    pick = [aoas_lod[1], aoas_lod[len(aoas_lod)//2], aoas_lod[-1]]
    for a in pick:
        eta, chord, cl, load = strip_data(lod[a], cols, args.bref, args.cref)
        CLa = np.interp(a, aoa, CL)
        # elliptical load with same total CL: cl*c/cref = (4*S*CL)/(pi*b*cref) * sqrt(1-eta^2)
        ell = (4 * args.sref * CLa) / (np.pi * args.bref * args.cref) * np.sqrt(np.clip(1 - eta**2, 0, 1))
        axes[0].plot(eta, load, label=f"a={a:.0f} CL={CLa:.2f}")
        axes[0].plot(eta, ell, "--", color=axes[0].lines[-1].get_color(), alpha=0.5)
        axes[1].plot(eta, cl, label=f"a={a:.0f}")
    axes[0].set_xlabel("eta = 2y/b"); axes[0].set_ylabel("cl*c/cref")
    axes[0].set_title("Span load vs elliptical (dashed)")
    axes[0].legend(fontsize=8)
    axes[1].axhline(args.clmax2d, color="r", ls=":", label=f"clmax2d={args.clmax2d}")
    axes[1].set_xlabel("eta"); axes[1].set_ylabel("local cl"); axes[1].set_title("Section cl")
    axes[1].legend(fontsize=8)
    axes[2].plot(CL, CDi, "o-", label="CDi")
    clg = np.linspace(0, max(CL), 50)
    for ee, lab in [(0.9, "e=0.90"), (1.0, "e=1.00")]:
        axes[2].plot(clg, clg**2 / (np.pi * AR * ee), "--", alpha=0.5, label=lab)
    axes[2].set_xlabel("CL"); axes[2].set_ylabel("CDi"); axes[2].set_title(f"Induced polar (AR={AR:.2f})")
    axes[2].legend(fontsize=8)
    fig.suptitle(args.basename.split("\\")[-1] + (" " + args.tag if args.tag else ""))
    fig.tight_layout()
    out = args.basename + "_post.png"
    fig.savefig(out, dpi=110)
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
