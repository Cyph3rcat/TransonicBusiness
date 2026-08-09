import csv
import glob
import re

rows = []
for f in sorted(glob.glob("history_m0p*.csv")):
    with open(f) as fh:
        r = list(csv.reader(fh))
    header = [h.strip().strip('"') for h in r[0]]
    last = r[-1]
    d = dict(zip(header, last))
    m = re.search(r"m0p(\d+)", f)
    mach = float("0." + m.group(1))
    rows.append((mach, d.get("Inner_Iter"), d.get("CL"), d.get("CD"), d.get("CMz")))
rows.sort()

print(f"{'Mach':>6} {'iters':>6} {'CL':>10} {'CD':>10} {'CMz':>10}")
for mach, it, cl, cd, cmz in rows:
    print(f"{mach:6.2f} {it:>6} {float(cl):10.5f} {float(cd):10.5f} {float(cmz):10.5f}")
