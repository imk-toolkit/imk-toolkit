# -*- coding: utf-8 -*-
"""
Calculate temperature for adiabatic process in air.
"""
import xarray as xr
from imktk import constants as cs


def main(p, T_0, p_0):
    """Calculate temperature for adiabatic process in air.

    Arguments
    =========
    p: xr.DataArray
        pressure
    T_0: float
        Temperature of start condition in K
    p_0: float
        Pressure of start condition

    Returns
    =======
    dataarray: temperature for adiabatic process
    """
    assert isinstance(T_0, float), "Input is not a float"
    assert isinstance(p_0, float), "Input is not a float"
    assert isinstance(p, xr.DataArray), "Input is not a xr.DataArray"

    T_ad = T_0 * (p / p_0) ** ((cs.gamma_air - 1) / cs.gamma_air)
    return T_ad
