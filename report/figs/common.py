"""Shared style, palette and data readers for report figures; nothing is hand-drawn -- each figure reads a solver output file or the same closed-form geometry the OpenVSP scripts use. Palette is a fixed categorical order, never cycled; status colours are reserved for pass/fail marks."""
import os
import re

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.dirname(HERE)
ROOT = os.path.dirname(REPORT)
OUT = os.path.join(REPORT, "figures")
VSP = os.path.join(ROOT, "openvsp", "vspaero_runs")
AF = os.path.join(ROOT, "airfoils")

os.makedirs(OUT, exist_ok=True)

# ----------------------------------------------------------------- palette ---
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
          "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
C1, C2, C3, C4, C5, C6, C7, C8 = SERIES

GOOD = "#0ca30c"
WARNING = "#fab219"
SERIOUS = "#ec835a"
CRITICAL = "#d03b3b"

INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#fcfcfb"

# Sequential blue ramp (single hue, light -> dark) for magnitude encodings.
BLUES = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec",
         "#5598e7", "#3987e5", "#2a78d6", "#256abf", "#1c5cab",
         "#184f95", "#104281", "#0d366b"]


def use_style():
    plt.rcParams.update({
        "figure.dpi": 160,
        "savefig.dpi": 160,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10.5,
        "axes.labelsize": 9.5,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK2,
        "axes.edgecolor": AXIS,
        "axes.linewidth": 0.9,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.frameon": False,
        "legend.fontsize": 8.5,
        "legend.labelcolor": INK2,
        "lines.linewidth": 2.0,
        "lines.markersize": 5.0,
    })


def save(fig, name, tight_rect=None):
    path = os.path.join(OUT, name)
    if tight_rect:
        fig.tight_layout(rect=tight_rect)
    else:
        fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {os.path.relpath(path, ROOT)}")
    return path


def title(ax, main, sub=None):
    """Title plus an optional plain-language subtitle underneath."""
    if sub:
        # Reserve one blank title line per subtitle line so the two never collide.
        ax.set_title(main + "\n" * sub.count("\n") + "\n", loc="left", color=INK)
        ax.text(0, 1.015, sub, transform=ax.transAxes, fontsize=8.6,
                color=INK2, va="bottom", ha="left")
    else:
        ax.set_title(main, loc="left", color=INK)


# ------------------------------------------------------------ file readers ---
def read_polar(path):
    """VSPAERO .polar -> (column-index dict, ndarray of rows)."""
    hdr, rows = None, []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith(("Surface", "Surf-")):
                continue
            if s.startswith("Beta "):
                hdr = s.split()
                continue
            if hdr is not None:
                rows.append([float(x) for x in s.split()])
    return {n: i for i, n in enumerate(hdr)}, np.array(rows)


def polar_col(path, name):
    c, d = read_polar(path)
    return d[:, c[name]]


def read_lod(path):
    """VSPAERO .lod -> (list of per-case section tables, reference dict); a new case is detected when the leading 'Iter' column resets."""
    ref, hdr, blocks, cur = {}, None, [], None
    with open(path) as f:
        for line in f:
            s = line.rstrip("\n")
            if not s.strip() or s.startswith("*"):
                continue
            m = re.match(r"^([A-Za-z_]\w*_)\s+(-?[\d.eE+]+)\s", s)
            if m and hdr is None:
                ref[m.group(1).rstrip("_")] = float(m.group(2))
                continue
            t = s.split()
            if t[0] == "Iter":
                hdr = t
                continue
            if hdr is None or t[0] == "#":
                continue
            try:
                vals = [float(x) for x in t]
            except ValueError:
                continue
            if cur is None or vals[2] < cur[-1][2]:  # TrailVort index restarted
                cur = []
                blocks.append(cur)
            cur.append(vals)
    cols = {n: i for i, n in enumerate(hdr)}
    out = []
    for b in blocks:
        a = np.array(b)
        out.append({n: a[:, i] for n, i in cols.items()})
    return out, ref


def read_wavedrag_area(path):
    """OpenVSP wave-drag CSV -> (x [ft], mean cross-sectional area [ft^2]); averages the per-rotation Slice_Area rows into Whitcomb's equivalent body."""
    rows, start, length, xn = [], None, None, None
    with open(path) as f:
        for line in f:
            k, _, rest = line.partition(",")
            if k not in ("Slice_Area", "Start_X", "Length", "X_Norm"):
                continue
            v = [float(x) for x in rest.strip().split(",")] if rest.strip() else []
            if k == "Slice_Area":
                rows.append(v)
            elif k == "Start_X" and start is None:
                start = v[0]
            elif k == "Length" and length is None:
                length = v[0]
            elif k == "X_Norm" and xn is None:
                xn = v
    a = np.array(rows).mean(axis=0)
    x = start + np.array(xn) * length
    return x, a


# --------------------------------------------------------- full_v7 geometry ---
# Station table copied verbatim from the FUSE list in openvsp/vspaero_runs/11_full_v7/gen_v7.py, so this is the same body OpenVSP lofted and VSPAERO solved.
FUSE_L = 42.2
FUSE_STATIONS = [
    # x,      z,       height, width
    (0.000, -1.9285, 1.18617, 1.15014),
    (5.737, -1.1149, 3.70512, 4.88275),
    (10.852, 0.0000, 6.04571, 5.70454),
    (17.000, 0.0000, 6.10000, 6.10000),
    (23.400, 0.0000, 6.10000, 6.10000),
    (30.500, 0.4769, 4.69600, 4.69600),
    (42.200, 1.7956, 0.60000, 0.60000),
]

# Belly fairing (gen_v7.py, offset by X_FAIRING + wing_dx and z = -2.20).
X_WING_LE = 14.3464           # final_alpha: wing root leading edge
WING_DX = X_WING_LE - 19.0
FAIR_X0, FAIR_L = 16.0 + WING_DX, 17.5
FAIR_STATIONS = [  # x from fairing nose, width, height, z offset
    (0.0, 0.00, 0.00, 0.25),
    (3.5, 5.30, 2.20, 0.05),
    (7.8, 7.00, 2.85, 0.00),
    (13.5, 5.60, 2.40, 0.32),
    (17.5, 0.00, 0.00, 1.20),
]

WING = dict(x_le=X_WING_LE, z=-2.6, semispan=20.7662, cr=6.9086, ct=2.4180,
            sweep25=18.5, dihedral=2.3, twist=-3.0)
WINGLET = dict(span=2.40, sweep25=31.0, cant=70.0, ct=0.95)
NACELLE = dict(x=25.1 + WING_DX, y=6.9, z=1.0, length=7.5,
               stations=[(0.0, 0.0), (0.7, 2.1), (2.8, 2.9), (5.6, 2.6), (7.5, 0.0)])
PYLON = dict(x=24.0 + WING_DX, y=6.9, z=-2.0, span=3.2, cr=3.6, ct=2.4, sweepLE=35.0)
# Final configuration: S_HT = 29.10 ft^2, S_VT = 43.20 ft^2 (size_tails.py).
VT = dict(x_root_le=31.6, z_root=2.0, span=6.7867, cr=4.0293, ct=2.4385, sweep25=35.0)
HT = dict(span=11.4056, cr=3.4529, ct=1.6515, sweep25=20.0)
DORSAL = dict(x=26.5, z=2.60, span=1.5, cr=6.2, ct=1.4, sweepLE=76.0)


def fuselage_outline(n=400):
    """(x, half-width, half-height, centreline z) for the full_v7 body."""
    from scipy.interpolate import PchipInterpolator
    s = np.array(FUSE_STATIONS)
    x = np.linspace(0.0, FUSE_L, n)
    z = PchipInterpolator(s[:, 0], s[:, 1])(x)
    h = PchipInterpolator(s[:, 0], s[:, 2])(x)
    w = PchipInterpolator(s[:, 0], s[:, 3])(x)
    # Round end caps: the nose cap is 1.0 x local radius, the tail cap 0.5.
    return x, w / 2.0, h / 2.0, z


def fairing_outline(n=200):
    from scipy.interpolate import PchipInterpolator
    s = np.array(FAIR_STATIONS)
    xl = np.linspace(0.0, FAIR_L, n)
    w = PchipInterpolator(s[:, 0], s[:, 1])(xl)
    h = PchipInterpolator(s[:, 0], s[:, 2])(xl)
    z = PchipInterpolator(s[:, 0], s[:, 3])(xl) - 2.20
    return FAIR_X0 + xl, w / 2.0, h / 2.0, z


def wing_planform(w=WING):
    """Leading- and trailing-edge x at the root and tip of one panel."""
    tan25 = np.tan(np.radians(w["sweep25"]))
    x_le_tip = w["x_le"] + 0.25 * w["cr"] + w["semispan"] * tan25 - 0.25 * w["ct"]
    return dict(x_le_root=w["x_le"], x_te_root=w["x_le"] + w["cr"],
                x_le_tip=x_le_tip, x_te_tip=x_le_tip + w["ct"],
                y_tip=w["semispan"])


def load_airfoil(name):
    """Selig-format .dat -> (x, y), normalised to unit chord."""
    p = os.path.join(AF, "dat_clean", name)
    if not os.path.exists(p):
        p = os.path.join(AF, "dat", name)
    xy = []
    with open(p) as f:
        for line in f:
            t = line.split()
            if len(t) != 2:
                continue
            try:
                xy.append((float(t[0]), float(t[1])))
            except ValueError:
                continue
    a = np.array(xy)
    return a[:, 0], a[:, 1]
