# -*- coding: utf-8 -*-

"""
Calculate saturation vapour pressure over ice for temperatures > 110 K according to
Murphy & Koop, 2005 https://doi.org/10.1256/qj.04.94.
"""
import xarray as xr
import numpy as np
import warnings


def main(T):
    """Return saturation vapour pressure over ice in Pa for given Temperature in K.

    Arguments
    =========
    T: xr.DataArray
        in K

    Returns
    =======
    dataarray: saturation vapour pressure over ice in Pa
    """
    assert isinstance(T, xr.DataArray), "Input is not a xr.DataArray"
    if (T.max(skipna=True) > 273.15) | (T.min(skipna=True) <= 110):
        warnings.warn("At least one of the values of T is out of range.")
    p_ice = np.exp(9.550426 - 5723.265 / T + 3.53068 * np.log(T) - 0.00728332 * T)
    return p_ice
