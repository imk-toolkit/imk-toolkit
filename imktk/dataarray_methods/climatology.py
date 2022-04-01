#!/usr/bin/env python
# coding: utf-8
"""Calculate monthly climatology within a xr.DataArray."""
import xarray as xr


def main(dataarray):
    """Return monthly climatology for dataarray."""
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    return dataarray.groupby("time.month").mean("time")
