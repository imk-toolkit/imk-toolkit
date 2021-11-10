#!/usr/bin/env python
# coding: utf-8
"""Calculate anomalies within a xr.DataArray."""
import xarray as xr


def main(dataarray):
    """Return monthly anomalies for dataarray."""
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    climatology = dataarray.groupby("time.month").mean("time")
    anomalies = dataarray.groupby("time.month") - climatology
    return anomalies
