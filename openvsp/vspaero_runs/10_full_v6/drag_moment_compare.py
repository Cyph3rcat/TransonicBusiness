"""v5 -> v6 comparison: parasitic, induced and interference drag, and the
per-component pitching-moment buildup.

"v5" here means **v5-equivalent**: v6's fuselage (closed tail -- v5's actual
file has an open tail that corrupts CMy, doubts.md #26) carrying v5's
DOCUMENTED tail areas (S_HT=51.68, S_VT=59.0 ft^2). This isolates the
tail-resizing effect from the fuselage-closure fix, which is the honest
comparison -- diffing against the corrupted v5.vsp3 directly would mix a data
bug into a sizing result.

Data sources:
  parasitic / interference : {00_baseline,final_alpha}/*_ParasiteBuildUp.csv
                              (Raymer Ch.12 method, drag_buildup.py's Q table)
  induced                  : {00_baseline,final_alpha}/*.polar, Trefftz-plane
                              CDiw vs CL^2 fit
  pitching moment          : component_moment_results.json, leave-one-out
                              buildup (component_moment.py)

Produces: v6_drag_moment_compare.png (2x2)
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import drag_buildup as db

HERE = os.path.dirname(os.path.abspath(__file__))
SREF, BREF = 193.678, 41.5324
AR = BREF ** 2 / SREF

C_V5, C_V6 = "#9b2c2c", "#2b6cb0"
plt.rcParams.update({"figure.dpi": 130, "font.size": 9,
                     "axes.grid": True, "grid.alpha": 0.25,
                     "axes.spines.top": False, "axes.spines.right": False})

CASES = {
    "v5eq": dict(dir="00_baseline", csv="00_baseline_ParasiteBuildUp.csv",
                 label="v5-equivalent (S$_{HT}$=51.7, S$_{VT}$=59.0 ft$^2$)",
                 color=C_V5),
    "v6":   dict(dir="final_alpha", csv="final_alpha_ParasiteBuildUp.csv",
                 label="v6 (S$_{HT}$=34.0, S$_{VT}$=45.0 ft$^2$)",
                 color=C_V6),
}


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


def parasite_and_interference(case):
    rows = db.read_buildup(os.path.join(HERE, case["dir"], case["csv"]))
    out = {}
    for r in rows:
        q, _ = db.Q_RAYMER.get(r["name"], (1.0, ""))
        f_actual = r["cf"] * r["ff"] * q * r["swet"]
        f_noQ = r["cf"] * r["ff"] * 1.0 * r["swet"]
        out[r["name"]] = dict(cd0=f_actual / SREF, cd0_noQ=f_noQ / SREF,
                              interference=(f_actual - f_noQ) / SREF, q=q)
    return out


def induced_k(case):
    polar_name = {"00_baseline": "00_baseline", "final_alpha": "final_alpha"}[case["dir"]]
    c, d = read_polar(os.path.join(HERE, case["dir"], f"{polar_name}.polar"))
    cl, cdiw = d[:, c["CLtot"]], d[:, c["CDiw"]]
    m = cl > 0.05
    k = np.polyfit(cl[m] ** 2, cdiw[m], 1)[0]
    e = 1.0 / (np.pi * AR * k)
    return k, e


def main():
    fig, ax = plt.subplots(2, 2, figsize=(12, 9.5))

    # ---------------------------------------------------------- (0,0) parasitic
    a = ax[0, 0]
    pd_data = {tag: parasite_and_interference(c) for tag, c in CASES.items()}
    comps = [c for c in db.Q_RAYMER if c in pd_data["v6"]]
    comps.sort(key=lambda c: -pd_data["v6"][c]["cd0"])
    y = np.arange(len(comps))
    h = 0.36
    v5_vals = [pd_data["v5eq"][c]["cd0"] * 1e4 for c in comps]
    v6_vals = [pd_data["v6"][c]["cd0"] * 1e4 for c in comps]
    a.barh(y + h / 2, v5_vals, height=h, color=C_V5, label="v5-equivalent")
    a.barh(y - h / 2, v6_vals, height=h, color=C_V6, label="v6")
    for yi, (v5v, v6v) in enumerate(zip(v5_vals, v6_vals)):
        a.text(max(v5v, v6v) + 1, yi + h / 2, f"{v5v:.1f}", va="center", fontsize=7, color=C_V5)
        a.text(max(v5v, v6v) + 1, yi - h / 2, f"{v6v:.1f}", va="center", fontsize=7, color=C_V6)
    a.set_yticks(y, comps)
    tot5 = sum(pd_data["v5eq"][c]["cd0"] for c in comps) * 1.03 * 1e4
    tot6 = sum(pd_data["v6"][c]["cd0"] for c in comps) * 1.03 * 1e4
    a.set_xlabel("parasite drag  $C_{D0}$ (counts)")
    a.set_title(f"Parasitic drag by component\ntotal incl. 3% leakage: "
                f"v5eq {tot5:.0f} $\\to$ v6 {tot6:.0f} counts ({tot6-tot5:+.0f})",
                fontsize=10)
    a.legend(fontsize=8, loc="lower right")

    # ------------------------------------------------------------ (0,1) induced
    b = ax[0, 1]
    cls = np.linspace(0, 0.85, 100)
    for tag, c in CASES.items():
        k, e = induced_k(c)
        b.plot(cls, k * cls ** 2 * 1e4, color=c["color"], lw=2,
               label=f"{tag}: $C_{{Di}}$={k:.4f}$\\cdot C_L^2$, e={e:.3f}")
    b.axvline(0.36, color="grey", lw=1, ls=":")
    b.text(0.365, 5, "~cruise $C_L$", fontsize=7.5, color="grey", rotation=90, va="bottom")
    b.set_xlabel("$C_L$")
    b.set_ylabel("$C_{Di}$  (counts, Trefftz plane)")
    b.set_title("Induced drag: v5-equiv vs v6\n(winglets unchanged; wake e "
                "improves slightly with the lighter tail)", fontsize=10)
    b.legend(fontsize=8, loc="upper left")

    # ------------------------------------------------------- (1,0) interference
    c_ax = ax[1, 0]
    icomps = [c for c in comps if pd_data["v6"][c]["q"] > 1.0]
    y2 = np.arange(len(icomps))
    v5i = [pd_data["v5eq"][c]["interference"] * 1e4 for c in icomps]
    v6i = [pd_data["v6"][c]["interference"] * 1e4 for c in icomps]
    c_ax.barh(y2 + h / 2, v5i, height=h, color=C_V5, label="v5-equivalent")
    c_ax.barh(y2 - h / 2, v6i, height=h, color=C_V6, label="v6")
    for yi, (v5v, v6v, comp) in enumerate(zip(v5i, v6i, icomps)):
        q = pd_data["v6"][comp]["q"]
        c_ax.text(max(v5v, v6v) + 0.15, yi, f"  Q={q:.2f}", va="center", fontsize=7.5, color="#444")
    c_ax.set_yticks(y2, icomps)
    c_ax.set_xlabel("interference-drag increment  $\\Delta C_{D0} = C_f{\\cdot}FF{\\cdot}Swet{\\cdot}(Q-1)$  (counts)")
    c_ax.set_title("Interference drag (Raymer Q-factor increment)\n"
                   "only components with Q>1 shown; Q=1 elsewhere", fontsize=10)
    c_ax.legend(fontsize=8, loc="lower right")

    # -------------------------------------------------------------- (1,1) moment
    d_ax = ax[1, 1]
    with open(os.path.join(HERE, "component_moment_results.json")) as fh:
        mom = json.load(fh)
    mcomps = list(mom["v6"]["components"].keys())
    mcomps.sort(key=lambda c: mom["v6"]["components"][c]["dCMy"])
    y3 = np.arange(len(mcomps))
    v5m = [mom["v5eq"]["components"][c]["dCMy"] for c in mcomps]
    v6m = [mom["v6"]["components"][c]["dCMy"] for c in mcomps]
    d_ax.axvline(0, color="black", lw=0.8)
    d_ax.barh(y3 + h / 2, v5m, height=h, color=C_V5, label="v5-equivalent")
    d_ax.barh(y3 - h / 2, v6m, height=h, color=C_V6, label="v6")
    d_ax.set_yticks(y3, mcomps)
    d_ax.set_xlabel("$\\Delta C_{My}$ contribution  (leave-one-out, $\\alpha$=3.7$\\degree$)")
    d_ax.set_title(f"Pitching-moment buildup by component\n"
                   f"full config: v5eq $C_{{My}}$={mom['v5eq']['full'][2]:+.3f}  "
                   f"$\\to$  v6 $C_{{My}}$={mom['v6']['full'][2]:+.3f}", fontsize=10)
    d_ax.text(0.02, 0.03, "$\\leftarrow$ nose-down (stabilizing)      "
                          "nose-up (destabilizing) $\\rightarrow$",
             transform=d_ax.transAxes, fontsize=7.5, color="#444")
    d_ax.legend(fontsize=8, loc="upper left")

    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v6_drag_moment_compare.png"))
    plt.close(fig)
    print("wrote v6_drag_moment_compare.png")

    # ---- console summary ----
    print(f"\nHorizTail moment contribution: v5eq {mom['v5eq']['components']['HorizTail']['dCMy']:+.4f} "
          f"-> v6 {mom['v6']['components']['HorizTail']['dCMy']:+.4f}  "
          f"(ratio {mom['v6']['components']['HorizTail']['dCMy']/mom['v5eq']['components']['HorizTail']['dCMy']:.2f}, "
          f"area ratio {34.0/51.68:.2f})")


if __name__ == "__main__":
    main()
