#!/usr/bin/env python
# coding: utf-8
"""Calculate anomalies within a xr.DataArray."""
import xarray as xr
from imktk.dataarray_methods import climatology


def main(dataarray):
    """Return monthly anomalies for dataarray."""
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    anomalies = dataarray.groupby("time.month") - climatology(dataarray)
    return anomalies
