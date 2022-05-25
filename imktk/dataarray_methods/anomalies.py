#!/usr/bin/env python
# coding: utf-8
"""Calculate monthly anomalies within a xr.DataArray."""
import xarray as xr
from climatology import main as climatology


def main(dataarray):
    """Return monthly anomalies for dataarray.

    Arguments
    =========
    dataarray: Climate dataarray with `time` coordinate

    Returns
    =======
    dataarray: Normalized climate dataarray with `time` coordinate on months resolution
    """
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    anomalies = dataarray.groupby("time.month") - climatology(dataarray)
    return anomalies
