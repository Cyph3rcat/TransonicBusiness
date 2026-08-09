"""Schrenk tip-station washout calc (config.md B.1); degenerate by construction -- result depends only on C_L_wing and a0, so it's identical for SC(2)-0412/0414 regardless of sweep/taper/airfoil, and can't discriminate between those candidates."""
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
