#!/usr/bin/env python
# coding: utf-8
"""
Interpolation routine for flight track (incl. aircraft and satellites)

This script helps calculating interpolations along aircraft and satellite tracks.

Usage:

    ```python
    import imktk

    da = imktk.tutorial.open_dataset("flight")
    dims = dict(lat = [1.1,2.4], lon = [.21,.35])
    da.imktk.flight_track(**dims)
    ```
"""
import xarray as xr


def main(dataarray, name="flight", method="linear", interpolate_na=None, **dims):
    """Interpolation routine for flight track (incl. aircraft and satellites)

    This script helps calculating interpolations along aircraft and satellite tracks.

    Arguments
    =========
    dataarray: xr.DataArray to be mapped on the flight tracks
    name: Name of flight
    method: Interpolation method to be used
    dims: Dictionary of coord and list of values
    interpolate_na: Options for interpolation of nan values

    Inerpolation options are described here: https://docs.xarray.dev/en/stable/generated/xarray.DataArray.interpolate_na.html

    Returns
    =======
    result: xr.DataArray of interpolated values to flight track
    """
    # check if first argument is a dataarray
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"

    # check if dims dictionary fits to the dataarray, based on ...
    msg = f"Some dim keys of {dims.keys()} not found in {list(dataarray.coords)}"
    # ... all keys are valid coordinate dimensions
    assert all([x in dataarray.coords for x in dims.keys()]), msg
    # ... flight tracks are lists
    assert all([isinstance(x, list) for x in dims.values()]), "Dimension values are not lists"
    # ... all flight tracks are the same length
    lengths = [len(x) for x in dims.values()]
    assert all([x == lengths[0] for x in lengths]), "Not all dims are of same length"

    if interpolate_na is not None:
        assert isinstance(interpolate_na, dict), "Interpolate options are not given as a dict"
        dataarray = dataarray.interpolate_na(**interpolate_na)

    criteria = {k: xr.DataArray(v, dims=name) for k, v in dims.items()}

    return dataarray.interp(**criteria, method=method)
