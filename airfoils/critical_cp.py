"""Shared isentropic critical-pressure-coefficient formula.

Cp_cr(M) is the pressure coefficient at which local flow first reaches
Mach 1 (sonic), given freestream Mach M. Used by both critical_mach_pg.py
(Prandtl-Glauert extrapolation of a low-speed Cp_min) and
su2_screen/extract_cpmin_crossing.py (real compressible CFD Cp_min) so the
two independent M_crit methods share exactly one copy of this formula --
a typo here would silently corrupt the comparison between them.
"""

GAMMA = 1.4


def cp_critical(M: float) -> float:
    return (2.0 / (GAMMA * M**2)) * (
        ((2 + (GAMMA - 1) * M**2) / (GAMMA + 1)) ** (GAMMA / (GAMMA - 1)) - 1.0
    )
