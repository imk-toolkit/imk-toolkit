# -*- coding: utf-8 -*-

"""
Calculate saturation vapour pressure over liquid water for temperatures 123 K < T < 332 K according to
Murphy & Koop, 2005 https://doi.org/10.1256/qj.04.94.
"""
import xarray as xr
import numpy as np
import warnings


def main(T):
    """Return saturation vapour pressure over liquid water in Pa for given Temperature in K.

    Arguments
    =========
    T: xr.DataArray
        in K

    Returns
    =======
    dataarray: saturation vapour pressure over liquid water in Pa.
    """
    assert isinstance(T, xr.DataArray), "Input is not an xr.DataArray"
    if (T.max(skipna=True) >= 332) | (T.min(skipna=True) <= 123):
        warnings.warn("At least one of the values of T is out of range.")
    p_liq = np.exp(
        54.842763
        - 6763.22 / T
        - 4.21 * np.log(T)
        + 0.000367 * T
        + np.tanh(0.0415 * (T - 218.8)) * (53.878 - 1331.22 / T - 9.44523 * np.log(T) + 0.014025 * T)
    )
    return p_liq
