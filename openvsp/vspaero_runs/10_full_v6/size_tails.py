"""Coupled empennage-sizing/CG solve for full_v6: v5 moved the wing 3.1 ft forward for CG (weight.md 3), lengthening both tail arms without re-sizing the tails, leaving c_HT=1.34/c_VT=0.1225 vs Sadraey/Raymer's 1.1/0.09 and doubts.md 23's over-stability (SM=37.7% MAC); solved as a fixed-point loop (tail area -> tail weight -> CG -> wing position -> tail arm -> tail area) in two modes that disagree on purpose -- historical (textbook volume coefficient, no light-jet row so it over-sizes) vs requirement (target SM from the measured dNP/dS_HT sweep). Usage: python size_tails.py [--np A,B]"""
import argparse
import math

# ---------------------------------------------------------------- wing (fixed)
S_W = 193.678          # ft^2, trapezoidal reference (config.md B.2)
B_W = 41.5324          # ft
CR_W, CT_W = 6.9086, 2.4180
SEMISPAN_W = 20.7662
SWEEP25_W = 13.8       # deg, quarter chord (config.md B.1, SU2-derived)

# empennage shape (Raymer 4.3): areas are the free variables; AR/taper held fixed since v5's values already sit inside Raymer Table 4.3 ranges (HT AR 3-5 taper 0.3-0.6; VT AR 0.7-1.2 taper 0.6-1.0)
AR_HT, TAPER_HT, SWEEP25_HT = 4.4706, 0.4783, 20.0
AR_VT, TAPER_VT, SWEEP25_VT = 1.0659, 0.6052, 35.0
X_VT_ROOT, Z_VT_ROOT = 31.6, 2.0       # fin root LE, fixed to the tail cone

# ------------------------------------------------------- weights (weight.md 3)
MTOW = 11660.0
W_E = 0.59 * MTOW
W_FUEL = 0.2634 * MTOW
S_HT_REF, S_VT_REF = 51.68, 59.0       # areas the v5 weight fractions refer to
X_WING_REF = 19.0                      # root LE the v5 group arms were tabulated at

# volume coefficients: Sadraey Table 6.4 jet transport = 1.1/0.09; Raymer Table 6.4 = 1.00/0.09 with a -5% T-tail credit each (Raymer Ch.6: fin end-plate effect, clean air on the horizontal)
CHT_SADRAEY, CVT_SADRAEY = 1.10, 0.090
CHT_RAYMER, CVT_RAYMER = 1.00 * 0.95, 0.090 * 0.95


def panel(area, ar, taper, one_sided):
    """Planform from area/AR/taper (Sadraey Eqs. 6.77-6.80); one_sided=True for a vertical tail (AR=b^2/S over the single surface), False for horizontal (AR over the full span)."""
    b = math.sqrt(ar * area)
    cr = 2.0 * area / (b * (1.0 + taper)) if not one_sided else \
        2.0 * area / (b * (1.0 + taper)) * 1.0
    # For a one-sided surface S = b*cbar = b*cr*(1+lam)/2, giving the same form.
    ct = taper * cr
    mac = (2.0 / 3.0) * cr * (1 + taper + taper ** 2) / (1 + taper)
    # Spanwise station of the MAC, measured from the root.
    span_to_root = b / 2.0 if not one_sided else b
    y_mac = (span_to_root / 3.0) * (1 + 2 * taper) / (1 + taper)
    return dict(S=area, b=b, cr=cr, ct=ct, mac=mac, y_mac=y_mac)


def le_sweep(cr, taper, span_to_root, sweep25):
    """LE sweep from quarter-chord sweep, for a straight-tapered panel."""
    return math.atan(math.tan(math.radians(sweep25))
                     + 0.25 * cr * (1 - taper) / span_to_root)


def wing_geometry(x_root_le):
    p = panel(S_W, B_W ** 2 / S_W, CT_W / CR_W, one_sided=False)
    # Use the exact wing numbers rather than the AR/taper round trip.
    taper = CT_W / CR_W
    mac = (2.0 / 3.0) * CR_W * (1 + taper + taper ** 2) / (1 + taper)
    y_mac = (SEMISPAN_W / 3.0) * (1 + 2 * taper) / (1 + taper)
    x_c4 = x_root_le + 0.25 * CR_W + y_mac * math.tan(math.radians(SWEEP25_W))
    return dict(mac=mac, y_mac=y_mac, x_c4=x_c4, x_lemac=x_c4 - 0.25 * mac)


def tail_geometry(s_ht, s_vt):
    """Tail planforms and positions; the HT rides on the fin tip (T-tail) so shrinking the fin lowers/moves it and shortens L_HT -- that coupling is why this is solved rather than assigned."""
    vt = panel(s_vt, AR_VT, TAPER_VT, one_sided=True)
    vt_le = le_sweep(vt["cr"], TAPER_VT, vt["b"], SWEEP25_VT)
    vt["x_c4"] = X_VT_ROOT + 0.25 * vt["cr"] + vt["y_mac"] * math.tan(math.radians(SWEEP25_VT))
    vt["x_lemac"] = X_VT_ROOT + vt["y_mac"] * math.tan(vt_le)
    vt["x_tip_le"] = X_VT_ROOT + vt["b"] * math.tan(vt_le)
    vt["z_tip"] = Z_VT_ROOT + vt["b"]

    ht = panel(s_ht, AR_HT, TAPER_HT, one_sided=False)
    ht["x_root_le"] = vt["x_tip_le"]
    ht["z"] = vt["z_tip"]
    ht_le = le_sweep(ht["cr"], TAPER_HT, ht["b"] / 2.0, SWEEP25_HT)
    ht["x_c4"] = ht["x_root_le"] + 0.25 * ht["cr"] \
        + ht["y_mac"] * math.tan(math.radians(SWEEP25_HT))
    ht["x_lemac"] = ht["x_root_le"] + ht["y_mac"] * math.tan(ht_le)
    return ht, vt


def weight_items(x_root_le, s_ht, s_vt, ht, vt):
    """Class-I group weights (arms from weights_cg.py) with tail groups scaled by area; caveat: the tail-group fraction covers fin+dorsal together, so scaling by S_VT/S_VT_ref slightly over-scales the constant-area dorsal (~0.01 ft CG effect at MTOW)."""
    dx = x_root_le - X_WING_REF
    groups = [
        ("Wing",                 0.095 * MTOW, 23.62 + dx),
        ("Horizontal tail",      0.009 * MTOW * s_ht / S_HT_REF,
         ht["x_lemac"] + 0.40 * ht["mac"]),
        ("Vertical tail+dorsal", 0.012 * MTOW * s_vt / S_VT_REF,
         vt["x_lemac"] + 0.40 * vt["mac"]),
        ("Fuselage",             0.102 * MTOW, 19.00),
        ("Nacelles+pylons",      0.016 * MTOW, 28.50 + dx),
        ("Nose gear",            0.009 * MTOW,  6.50),
        ("Main gear",            0.035 * MTOW, 24.80 + dx),
        ("Engines installed",    2 * 520 * 1.25, 28.40 + dx),
    ]
    w_fixed = W_E - sum(g[1] for g in groups)
    groups += [("Avionics (nose)",   0.16 * w_fixed,  5.50),
               ("Furnishings",       0.42 * w_fixed, 16.90),
               ("Systems (aft-mid)", 0.42 * w_fixed, 21.50)]
    loading = [("Crew 2x200",   400.0,  7.50),
               ("Pax 6x180",   1080.0, 17.00),
               ("Baggage 6x40", 240.0, 25.00),
               ("Fuel",        W_FUEL, 23.62 + dx)]
    return groups, loading


def cg_of(items):
    w = sum(i[1] for i in items)
    return w, sum(i[1] * i[2] for i in items) / w


def solve(cht, cvt, cg_target_pct=28.0, np_fit=None, sm_target=None, quiet=False,
          fix_wing=None):
    """Fixed-point solve on (wing position, S_HT, S_VT); np_fit/sm_target switch HT sizing from volume-coefficient to static-margin (x_np = A + B*S_HT); fix_wing pins the wing root LE, REQUIRED with np_fit since the measured fit is only valid at the wing position it was run at (CG still moves as tail groups get lighter)."""
    x_w, s_ht, s_vt = (fix_wing or 15.9), S_HT_REF, S_VT_REF
    rows = []
    for it in range(40):
        wing = wing_geometry(x_w)
        ht, vt = tail_geometry(s_ht, s_vt)
        l_ht = ht["x_c4"] - wing["x_c4"]
        l_vt = vt["x_c4"] - wing["x_c4"]

        groups, loading = weight_items(x_w, s_ht, s_vt, ht, vt)
        w_mtow, x_mtow = cg_of(groups + loading)
        pct = (x_mtow - wing["x_lemac"]) / wing["mac"] * 100.0

        rows.append(dict(it=it, x_w=x_w, s_ht=s_ht, s_vt=s_vt, l_ht=l_ht,
                         l_vt=l_vt, cg_pct=pct, x_cg=x_mtow,
                         cht=s_ht * l_ht / (S_W * wing["mac"]),
                         cvt=s_vt * l_vt / (S_W * B_W)))

        # --- next iterate -------------------------------------------------
        s_vt_new = cvt * B_W * S_W / l_vt
        if np_fit is not None and sm_target is not None:
            a, b = np_fit
            # x_np(S_HT) = a + b*S_HT ; want (x_np - x_cg)/mac = sm_target
            s_ht_new = (x_mtow + sm_target * wing["mac"] - a) / b
        else:
            s_ht_new = cht * wing["mac"] * S_W / l_ht
        if fix_wing is not None:
            x_w_new = x_w
        else:
            # move the wing to hold the CG target; d(cg%)/d(x_w) ~ -0.5/MAC per ft since roughly half the weight rides with the wing group
            x_w_new = x_w + (pct - cg_target_pct) / 100.0 * wing["mac"] * 1.9

        if (abs(s_ht_new - s_ht) < 1e-4 and abs(s_vt_new - s_vt) < 1e-4
                and abs(x_w_new - x_w) < 1e-4):
            break
        s_ht, s_vt, x_w = s_ht_new, s_vt_new, x_w_new

    if not quiet:
        print(f"{'it':>3} {'x_wLE':>7} {'S_HT':>7} {'S_VT':>7} {'L_HT':>7} "
              f"{'L_VT':>7} {'c_HT':>6} {'c_VT':>7} {'CG %MAC':>8}")
        for r in rows[:6] + ([rows[-1]] if len(rows) > 6 else []):
            print(f"{r['it']:3d} {r['x_w']:7.3f} {r['s_ht']:7.2f} {r['s_vt']:7.2f} "
                  f"{r['l_ht']:7.3f} {r['l_vt']:7.3f} {r['cht']:6.3f} "
                  f"{r['cvt']:7.4f} {r['cg_pct']:8.2f}")
    return rows[-1], rows


def report_current():
    """Where the model actually is now, for comparison."""
    wing = wing_geometry(15.9)
    # As it sits in full_v5.vsp3 after the GUI edits.
    for tag, s_ht, s_vt in [("v5 as-scripted", 51.68, 59.00),
                            ("v5 as-in-file ", 62.42, 59.00)]:
        ht, vt = tail_geometry(s_ht, s_vt)
        l_ht = ht["x_c4"] - wing["x_c4"]
        l_vt = vt["x_c4"] - wing["x_c4"]
        print(f"  {tag}: S_HT={s_ht:6.2f} L_HT={l_ht:6.2f} c_HT={s_ht * l_ht / (S_W * wing['mac']):6.3f}"
              f"   S_VT={s_vt:5.2f} L_VT={l_vt:6.2f} c_VT={s_vt * l_vt / (S_W * B_W):7.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--np", help="measured NP fit 'A,B' for x_np = A + B*S_HT (ft)")
    ap.add_argument("--sm", type=float, default=0.15, help="target static margin")
    ap.add_argument("--cg", type=float, default=28.0, help="target MTOW CG, %%MAC")
    ap.add_argument("--fix-wing", type=float, default=15.9, dest="fix_wing",
                    help="pin the wing root LE (required with --np)")
    a = ap.parse_args()

    wing = wing_geometry(15.9)
    print(f"Wing: MAC={wing['mac']:.4f} ft  X_LEMAC={wing['x_lemac']:.3f}  "
          f"quarter-MAC={wing['x_c4']:.3f} ft  (wing root LE 15.9)\n")

    print("Current model, volume coefficients recomputed at the TRUE arms:")
    report_current()
    print(f"  targets: Sadraey jet transport c_HT={CHT_SADRAEY} c_VT={CVT_SADRAEY};"
          f"  Raymer +T-tail credit c_HT={CHT_RAYMER:.3f} c_VT={CVT_RAYMER:.4f}\n")

    print("=== Historical sizing (Sadraey Table 6.4, jet transport) ===")
    fin_s, _ = solve(CHT_SADRAEY, CVT_SADRAEY, a.cg)
    print()
    print("=== Historical sizing (Raymer Table 6.4 + T-tail credit) ===")
    fin_r, _ = solve(CHT_RAYMER, CVT_RAYMER, a.cg)

    if a.np:
        A, B = (float(x) for x in a.np.split(","))
        print(f"\n=== Requirement-driven sizing, wing PINNED at {a.fix_wing} ft "
              f"(SM = {a.sm * 100:.0f}% MAC, x_np = {A:.4f} + {B:.5f}*S_HT) ===")
        fin_q, _ = solve(CHT_SADRAEY, CVT_SADRAEY, a.cg, np_fit=(A, B),
                         sm_target=a.sm, fix_wing=a.fix_wing)
        w = wing_geometry(fin_q["x_w"])
        x_np = A + B * fin_q["s_ht"]
        print(f"\n  -> S_HT = {fin_q['s_ht']:.2f} ft^2, c_HT = {fin_q['cht']:.3f}"
              f"   S_VT = {fin_q['s_vt']:.2f} ft^2, c_VT = {fin_q['cvt']:.4f}")
        print(f"  -> CG = {fin_q['x_cg']:.3f} ft ({fin_q['cg_pct']:.1f}% MAC), "
              f"x_np = {x_np:.3f} ft ({(x_np - w['x_lemac']) / w['mac'] * 100:.1f}% MAC)")
        # CG band (weight.md 3) is +/- about the MTOW point; report margin at both ends since aft is the binding limit
        fwd, aft = fin_q["cg_pct"] - 4.4, fin_q["cg_pct"] + 3.7
        for tag, pct in (("fwd", fwd), ("MTOW", fin_q["cg_pct"]), ("aft", aft)):
            sm = (x_np - w["x_lemac"]) / w["mac"] * 100 - pct
            print(f"       SM at {tag:4s} CG ({pct:4.1f}% MAC) = {sm:5.1f}% MAC")


if __name__ == "__main__":
    main()
