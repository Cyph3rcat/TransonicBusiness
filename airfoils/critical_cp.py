"""Cp_cr(M): isentropic critical pressure coefficient (local sonic point) -- shared by critical_mach_pg.py and su2_screen/extract_cpmin_crossing.py so the two independent M_crit methods can't silently diverge."""

GAMMA = 1.4


def cp_critical(M: float) -> float:
    return (2.0 / (GAMMA * M**2)) * (
        ((2 + (GAMMA - 1) * M**2) / (GAMMA + 1)) ** (GAMMA / (GAMMA - 1)) - 1.0
    )
