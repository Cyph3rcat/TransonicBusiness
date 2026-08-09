"""Schrenk's-approximation washout (twist) calc, formalizing the hand calc
already validated in config.md B.1 for the prior (0deg sweep, SC(2)-0410)
design: washout = -1.1deg.

Method (unchanged from the prior hand calc -- reproduced here as a script,
not a new method): at the wingtip (y=s), Schrenk chord = avg(linear-taper
chord, equal-area-elliptical chord). Since the elliptical chord -> 0 at the
tip for ANY straight-tapered planform, Schrenk_chord(tip)/c_actual(tip) = 0.5
identically, giving C_l,actual(tip) = 0.5 * C_L,wing always, independent of
taper/root chord/span. Likewise the ideal-elliptical local *lift* -> 0 at the
tip, giving C_l,ideal(tip) = 0 always. So:
    delta_Cl(tip) = 0 - 0.5*C_L_wing = -0.5*C_L_wing
    delta_alpha = delta_Cl(tip) / a0   (a0 = 2*pi/rad, thin-airfoil default)

IMPORTANT FINDING (flag, not fixed here per project instruction to keep this
method): this single-tip-station formula is mathematically DEGENERATE -- its
result depends only on C_L_wing and a0, not on taper, root/tip chord, sweep,
or airfoil section at all. It will return the exact same washout for SC(2)-
0412 and SC(2)-0414 even though they carry different sweep, because neither
sweep nor airfoil-specific lift-curve slope enters this single-point
evaluation. This is a real methodological gap (the tip is a singular point
where both ratios collapse to fixed values, not just "no explicit sweep
term") -- worth a follow-up (evaluate at y=0.90-0.95s instead of the literal
tip, or add a 3D/sweep-corrected lift-curve slope) if this number needs to
discriminate between candidates in a future pass.
"""
import math


def schrenk_tip_washout(C_L_wing: float, a0: float = 2 * math.pi) -> float:
    """Returns washout (deg, negative = leading-edge-down at tip)."""
    delta_cl_tip = 0.0 - 0.5 * C_L_wing
    delta_alpha_rad = delta_cl_tip / a0
    return math.degrees(delta_alpha_rad)


if __name__ == "__main__":
    C_L_WING = 0.248  # config.md B.2 C_li target

    washout = schrenk_tip_washout(C_L_WING)
    print(f"Schrenk tip-station washout: {washout:.2f} deg")
    print("(identical for SC(2)-0412 and SC(2)-0414 -- see docstring: this")
    print(" single-station method has no taper/sweep/airfoil dependence)")
