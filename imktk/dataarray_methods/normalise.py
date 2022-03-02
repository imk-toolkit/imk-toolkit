#!/usr/bin/env python
# coding: utf-8
"""Calculate normalisation within a xr.DataArray."""
import xarray as xr

def standard(arr):
    pass

def t_stats(arr):
    pass

def main(dataarray):
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    return standard(dataarray)
