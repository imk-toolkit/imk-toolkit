# -*- coding: utf-8 -*-
"""
Calculate temperature for adiabatic process in air.
"""
import xarray as xr
import numpy as np


def main(T_0, p_0, p):
    """Calculate temperature for adiabatic process in air.

    Arguments
    =========
    T_0: float
        Temperature of start condition in K
    p_0: float
        Pressure of start condition
    p: xr.DataArray
    
    Returns
    =======
    dataarray: temperature for adiabatic process
    """
    assert isinstance(T_0, float), "Input is not a float"
    assert isinstance(p_0, float), "Input is not a float"
    assert isinstance(p, xr.DataArray), "Input is not a xr.DataArray"

    kappa_air = 1.4

    T_ad = T_0 * (p / p_0) ** ((kappa_air - 1) / kappa_air)
    return T_ad

