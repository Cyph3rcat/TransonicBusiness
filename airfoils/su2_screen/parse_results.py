import glob
import re

def parse_log(path):
    with open(path, errors="ignore") as f:
        lines = f.readlines()
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith("|") and line.endswith("|") and "Inner_Iter" not in line and "-" not in line[:5]:
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) == 5:
                try:
                    it, rho, rhoe, cl, cd = [float(p) for p in parts]
                    rows.append((it, rho, rhoe, cl, cd))
                except ValueError:
                    continue
    return rows

results = {}
for path in sorted(glob.glob("log_*.txt")):
    tag = path[len("log_"):-len(".txt")]
    rows = parse_log(path)
    if not rows:
        results[tag] = None
        continue
    last10 = rows[-10:]
    final = rows[-1]
    cl_vals = [r[3] for r in last10]
    cd_vals = [r[4] for r in last10]
    cl_drift = max(cl_vals) - min(cl_vals)
    cd_drift = max(cd_vals) - min(cd_vals)
    results[tag] = {
        "n_iters": final[0],
        "rms_rho": final[1],
        "cl": final[3],
        "cd": final[4],
        "cl_drift_last10": cl_drift,
        "cd_drift_last10": cd_drift,
    }

for tag, r in results.items():
    if r is None:
        print(f"{tag}: NO DATA PARSED")
    else:
        ld = r["cl"] / r["cd"] if r["cd"] not in (0, None) and abs(r["cd"]) > 1e-6 else float("nan")
        print(f"{tag:16s} iters={r['n_iters']:.0f} rms_rho={r['rms_rho']:.2f} "
              f"CL={r['cl']:.4f} CD={r['cd']:.5f} L/D={ld:7.2f} "
              f"| drift(last10): dCL={r['cl_drift_last10']:.4f} dCD={r['cd_drift_last10']:.5f}")
