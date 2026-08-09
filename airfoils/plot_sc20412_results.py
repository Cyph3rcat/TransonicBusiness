"""SC(2)-0412 transonic screen: SU2 CFD Mach sweep vs Prandtl-Glauert approximation, plus the 25%-chord sweep each M_crit/M_dd basis implies -- the project adopted the M_dd basis (27.1 deg) over the literal M_crit basis (39.6 deg), see config.md B.5.2."""
import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
SWEEP_DIR = HERE / "su2_screen" / "mach_sweep_sc20412"
GAMMA = 1.4
M_CRUISE = 0.80


def cp_critical(M: np.ndarray) -> np.ndarray:
    """Isentropic critical pressure coefficient (local sonic condition) vs freestream Mach."""
    return (2.0 / (GAMMA * M**2)) * (
        ((2 + (GAMMA - 1) * M**2) / (GAMMA + 1)) ** (GAMMA / (GAMMA - 1)) - 1.0
    )


def load_airfoil_coords(path: Path) -> np.ndarray:
    """Selig-format .dat: first line is a title, rest is 'x y' pairs, TE -> LE -> TE."""
    lines = [l.strip() for l in path.read_text().splitlines() if l.strip()]

    def is_coord_line(line: str) -> bool:
        toks = line.split()
        if len(toks) < 2:
            return False
        try:
            float(toks[0]), float(toks[1])
            return True
        except ValueError:
            return False

    body = lines[1:] if not is_coord_line(lines[0]) else lines
    return np.array([[float(v) for v in l.split()[:2]] for l in body])


def sweep_for_mach(m_ref: float, m_cruise: float = M_CRUISE) -> float:
    """Lambda25 = arccos(M_ref/M_cruise): 25%-chord sweep needed to bring the effective section Mach back down to m_ref at cruise."""
    return np.degrees(np.arccos(min(m_ref / m_cruise, 1.0)))


def main():
    su2 = json.loads((SWEEP_DIR / "results_su2_sweep_sc20412.json").read_text())
    pg = json.loads((HERE / "results_critical_mach_pg.json").read_text())["candidates"]
    adaptive = json.loads((SWEEP_DIR / "adaptive_sweep_results.json").read_text())
    coords = load_airfoil_coords(HERE / "dat_clean" / "sc20412_selig.dat")

    machs = np.array([p["mach"] for p in su2["points"]])
    cds = np.array([p["cd"] for p in su2["points"]])
    cp_mins = np.array([p["cp_min"] for p in su2["points"]])
    m_crit_cfd = su2["M_crit_CFD"]
    m_dd_cfd = su2["M_dd_CFD"]

    pg412 = pg["NASA SC(2)-0412"]
    pg414 = pg["NASA SC(2)-0414"]
    m_crit_pg412 = pg412["M_crit_PG"]
    cpmin0_412 = pg412["Cpmin_0 (incompressible)"]

    print(f"{'M':>8} {'CD':>10} {'Cp_min (CFD)':>14} {'Cp_cr(M)':>10} {'AoA0 (deg)':>11} {'CL':>8}")
    for p, a in zip(su2["points"], adaptive):
        print(f"{p['mach']:8.4f} {p['cd']:10.5f} {p['cp_min']:14.4f} "
              f"{cp_critical(np.array(p['mach'])):10.4f} {a['aoa0']:11.3f} {a['cl']:8.4f}")
    print(f"\nM_crit (CFD, Cp-crossing) = {m_crit_cfd:.4f}   ->  Lambda25 = {sweep_for_mach(m_crit_cfd):.1f} deg")
    print(f"M_dd   (CFD, Cd hockey-stick) = {m_dd_cfd:.4f}   ->  Lambda25 = {sweep_for_mach(m_dd_cfd):.1f} deg  (adopted)")
    print(f"M_crit (PG, SC(2)-0412) = {m_crit_pg412:.4f}   ->  Lambda25 = {sweep_for_mach(m_crit_pg412):.1f} deg")
    print(f"M_crit (PG, SC(2)-0414) = {pg414['M_crit_PG']:.4f}   ->  Lambda25 = {sweep_for_mach(pg414['M_crit_PG']):.1f} deg")

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("NASA SC(2)-0412 -- SU2 CFD Mach Sweep vs Prandtl-Glauert Approximation", fontsize=13)

    ax = axes[0, 0]
    ax.plot(coords[:, 0], coords[:, 1], color="#1f77b4", lw=1.5)
    ax.set_aspect("equal")
    ax.set_title(f"SC(2)-0412 section  (t/c = {pg412['t/c (%)']:.2f}%)")
    ax.set_xlabel("x/c")
    ax.set_ylabel("y/c")
    ax.axhline(0, color="0.85", lw=0.6, zorder=0)

    ax = axes[0, 1]
    m_dense = np.linspace(0.3, 0.85, 400)
    ax.plot(m_dense, cp_critical(m_dense), "k--", lw=1.3, label=r"$Cp_{cr}(M)$ (isentropic, sonic condition)")
    ax.plot(m_dense, cpmin0_412 / np.sqrt(1 - m_dense**2), color="#ff7f0e", lw=1.5,
             label=r"Prandtl-Glauert: $Cp_{min,0}/\sqrt{1-M^2}$")
    ax.plot(machs, cp_mins, "o-", color="#2ca02c", lw=1.5, ms=5, label="SU2 CFD $Cp_{min}(M)$ (actual)")
    ax.axvline(m_crit_cfd, color="#2ca02c", ls=":", lw=1.2)
    ax.axvline(m_crit_pg412, color="#ff7f0e", ls=":", lw=1.2)
    ax.annotate(f"CFD M_crit={m_crit_cfd:.3f}", (m_crit_cfd, ax.get_ylim()[0]),
                 xytext=(4, 6), textcoords="offset points", color="#2ca02c", fontsize=8)
    ax.annotate(f"PG M_crit={m_crit_pg412:.3f}", (m_crit_pg412, ax.get_ylim()[0]),
                 xytext=(4, 18), textcoords="offset points", color="#ff7f0e", fontsize=8)
    ax.set_xlabel("Freestream Mach")
    ax.set_ylabel(r"$C_{p,min}$")
    ax.set_title(r"$M_{crit}$: where $Cp_{min}(M)$ meets $Cp_{cr}(M)$")
    ax.legend(fontsize=8, loc="lower left")
    ax.invert_yaxis()

    ax = axes[1, 0]
    ax.plot(machs, cds * 1e4, "o-", color="#d62728", lw=1.5, ms=5, label="SU2 CFD $C_D(M)$")
    ax.axvline(m_dd_cfd, color="#d62728", ls=":", lw=1.2)
    ax.annotate(f"M_dd={m_dd_cfd:.3f}\n(2 consecutive intervals\nwith dCd/dM >= 0.10)",
                 (m_dd_cfd, ax.get_ylim()[1] if False else max(cds) * 1e4),
                 xytext=(-90, -30), textcoords="offset points", color="#d62728", fontsize=8,
                 arrowprops=dict(arrowstyle="->", color="#d62728", lw=0.8))
    ax.set_xlabel("Freestream Mach")
    ax.set_ylabel(r"$C_D$ (counts)")
    ax.set_title(r"$M_{dd}$: sustained $dC_D/dM \geq 0.10$ (\"Boeing criterion\")")
    ax.legend(fontsize=8)

    ax = axes[1, 1]
    methods = [
        ("PG\nSC(2)-0412", m_crit_pg412, "#ff7f0e"),
        ("PG\nSC(2)-0414", pg414["M_crit_PG"], "#ffbb78"),
        ("CFD\n$M_{crit}$", m_crit_cfd, "#2ca02c"),
        ("CFD\n$M_{dd}$\n(adopted)", m_dd_cfd, "#d62728"),
    ]
    labels = [m[0] for m in methods]
    sweeps = [sweep_for_mach(m[1]) for m in methods]
    colors = [m[2] for m in methods]
    bars = ax.bar(labels, sweeps, color=colors)
    for b, s in zip(bars, sweeps):
        ax.text(b.get_x() + b.get_width() / 2, s + 0.5, f"{s:.1f}°", ha="center", fontsize=9)
    ax.set_ylabel(r"$\Lambda_{25}$ (deg)  $= \arccos(M_{ref}/0.80)$")
    ax.set_title("Implied 25%-chord sweep by method")
    ax.set_ylim(0, max(sweeps) + 6)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = HERE / "sc20412_results.png"
    fig.savefig(out_path, dpi=160)
    print(f"\nSaved figure: {out_path}")
    plt.show()


if __name__ == "__main__":
    main()
