"""
Physical constants used by several scripts.

"""
# fmt: off
__all__ = [
    "avogadro",
    "r_gas", "r_g",
    "c_p_air",
    "c_v_air",
    "gamma_air", "adiabatic_index_air"
]
# fmt: on

avogadro = 6.02214076e23  # mol-1
r_g = r_gas = 8.31446261815324  # J mol-1 K-1
c_p_air = 29.19  # J mol-1 K-1 for room conditions
c_v_air = 20.85  # J mol-1 K-1 for room conditions
gamma_air = adiabatic_index_air = c_p_air / c_v_air
