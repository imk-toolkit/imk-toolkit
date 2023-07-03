#!/usr/bin/env python
# coding: utf-8
"""
Interpolate between scattered datapoints on a map.
"""
import xarray as xr
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator


def main(dataarray, lons, lats, values, name='Interpolation', long_name=None, mode='linear'):
    """Interpolate between scattered datapoints on a map.

    Arguments
    =========
    dataarray: Dataarray representing the map to be used for interpolation
    lons: List of longitude values for the scattered datapoints
    lats: List of latitude values for the scattered datapoints
    values: List of actual values for the scattered datapoints
    name: Short name for datapoints
    long_name: Long name for datapoints
    mode: Interpolation method (either 'linear' or 'nearest')

    Returns
    =======
    dataarray: Interpolated values for scattered datapoints
    """
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    # check if lons,lats are in dataarray available, eliminate in v2 (warning)
    # check if lons,lats,values are of same length
    # check if lons,lats,values are lists, eliminate in v2
    # check if modes are either linear or nearest
    # check if dataarray has ndim=2, eliminate in v2
    X, Y = np.meshgrid(dataarray.lon, dataarray.lat)
    if mode.lower() in ("linear", "lin", "l"):
        interp = LinearNDInterpolator(list(zip(lons,lats)), values)
    elif mode.lower() in ("neighbour", "nearest", "near", "n"):
        interp = NearestNDInterpolator(list(zip(lons,lats)), values)
    else:
        msg = f"Expected mode 'linear' or 'nearest', got {mode}"
        raise ValueError(msg)
    Z = interp(X, Y)

    result = dataarray.copy()
    result.attrs = dict()
    result.name = name
    if long_name is None:
        long_name = name
    result.attrs['long_name'] = long_name
    result[:, :] = Z

    return result

