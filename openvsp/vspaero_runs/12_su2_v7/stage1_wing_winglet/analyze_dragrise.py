"""Fits constant-CL drag rise from whatever solved points exist on disk -- deliberately decoupled from dragrise_fixedcl.py's run loop so a killed orchestrator doesn't lose survived SU2 results; reports CD at CL=0.360 (drag-rise curve), CD0 (its climb IS wave drag), e (a fall means the shock distorts the spanwise lift distribution), and fit residual (large = nonlinear flow, don't trust the interpolation). Usage: python3 analyze_dragrise.py"""
import csv
import glob
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_CL = 0.360
AR = 41.5324 ** 2 / 193.678


def read_final(path):
    rows = list(csv.DictReader(open(path)))
    if not rows:
        return None
    k = {c.strip().strip('"'): c for c in rows[0].keys()}
    if "CL" not in k or "CD" not in k:
        return None
    last = rows[-1]
    return float(last[k["CL"]]), float(last[k["CD"]]), float(last[k["CMz"]])


def collect():
    """-> {mach: [(aoa, CL, CD, CMz), ...]}"""
    by_mach = {}
    pats = [
        (os.path.join(HERE, "history_cl_a*_m*.csv"),
         r"history_cl_a(?P<a>[0-9p]+)_m(?P<m>[0-9p]+)\.csv"),
        (os.path.join(HERE, "history_aoa*_m0p80.csv"),
         r"history_aoa(?P<a>[0-9p]+)_m(?P<m>[0-9p]+)\.csv"),
    ]
    for pat, rx in pats:
        for f in glob.glob(pat):
            mo = re.match(rx, os.path.basename(f))
            if not mo:
                continue
            aoa = float(mo.group("a").replace("p", "."))
            mach = float(mo.group("m").replace("p", "."))
            got = read_final(f)
            if got is None:
                continue
            cl, cd, cmz = got
            by_mach.setdefault(mach, []).append((aoa, cl, cd, cmz))
    for m in by_mach:
        by_mach[m].sort()
    return by_mach


def fit_polar(pts):
    n = len(pts)
    x = [cl ** 2 for _, cl, _, _ in pts]
    y = [cd for _, _, cd, _ in pts]
    sx, sy = sum(x), sum(y)
    sxx = sum(v * v for v in x)
    sxy = sum(a * b for a, b in zip(x, y))
    den = n * sxx - sx * sx
    if abs(den) < 1e-20:
        return None
    k = (n * sxy - sx * sy) / den
    cd0 = (sy - k * sx) / n
    resid = max(abs(b - (k * a + cd0)) for a, b in zip(x, y))
    return cd0, k, resid


def main():
    by_mach = collect()
    if not by_mach:
        raise SystemExit("no solved points found")

    rows = []
    for mach in sorted(by_mach):
        pts = by_mach[mach]
        # fit inside a symmetric window around the target CL so every Mach gets a comparable range: M0.80's 3.7deg point sits in shock-separated flow and an asymmetric window made CD0 come out non-monotonic across Mach in the first pass
        usable = [p for p in pts if abs(p[1] - TARGET_CL) <= 0.12]
        if len(usable) < 2:
            usable = pts[:3]
        fit = fit_polar(usable)
        if fit is None:
            continue
        cd0, k, resid = fit
        cls = [p[1] for p in usable]
        rows.append(dict(
            mach=mach, n=len(usable), cd0=cd0, k=k,
            e=(1.0 / (math.pi * k * AR)) if k > 0 else float("nan"),
            cd_at_target=cd0 + k * TARGET_CL ** 2, resid=resid,
            cl_lo=min(cls), cl_hi=max(cls),
            extrapolated=not (min(cls) <= TARGET_CL <= max(cls)),
            points=[dict(aoa=a, cl=cl, cd=cd, cmz=cm) for a, cl, cd, cm in pts],
        ))

    print("raw solved points")
    for mach in sorted(by_mach):
        angles = ", ".join(f"{a:.2f}deg->CL{cl:.4f}/CD{cd*1e4:.1f}"
                           for a, cl, cd, _ in by_mach[mach])
        print(f"  M{mach:.2f}: {angles}")

    print(f"\n=== DRAG RISE AT CONSTANT CL = {TARGET_CL} ===")
    print(f"{'Mach':>6} {'CD(counts)':>11} {'CD0':>8} {'e':>7} "
          f"{'n':>3} {'resid':>8}  note")
    prev = None
    for r in rows:
        note = "EXTRAPOLATED" if r["extrapolated"] else ""
        if prev is not None:
            dcd = (r["cd_at_target"] - prev["cd_at_target"])
            dm = r["mach"] - prev["mach"]
            if dm > 0 and dcd / dm > 0.10:
                note = (note + " " if note else "") + "dCD/dM>0.10"
        print(f"{r['mach']:>6.2f} {r['cd_at_target']*1e4:>11.2f} "
              f"{r['cd0']*1e4:>8.2f} {r['e']:>7.3f} {r['n']:>3} "
              f"{r['resid']*1e4:>7.2f}c  {note}")
        prev = r

    # Drag-divergence Mach, standard slope criterion dCD/dM = 0.10.
    mdd = None
    for a, b in zip(rows, rows[1:]):
        dm = b["mach"] - a["mach"]
        if dm <= 0:
            continue
        s = (b["cd_at_target"] - a["cd_at_target"]) / dm
        if s >= 0.10:
            prev_s = None
            i = rows.index(a)
            if i > 0:
                p = rows[i - 1]
                dmp = a["mach"] - p["mach"]
                if dmp > 0:
                    prev_s = (a["cd_at_target"] - p["cd_at_target"]) / dmp
            if prev_s is not None and prev_s < 0.10 and s > prev_s:
                mdd = a["mach"] + (0.10 - prev_s) / (s - prev_s) * dm
            else:
                mdd = a["mach"]
            break
    print(f"\ndrag-divergence Mach (dCD/dM = 0.10): "
          f"{('%.3f' % mdd) if mdd else 'not reached in this range'}")

    with open(os.path.join(HERE, "dragrise_analysis.json"), "w") as fh:
        json.dump(rows, fh, indent=2)
    print("wrote dragrise_analysis.json")


if __name__ == "__main__":
    main()
