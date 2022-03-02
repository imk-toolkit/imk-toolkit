#!/usr/bin/env python
# coding: utf-8
"""Calculate normalisation within a xr.DataArray."""
import xarray as xr


def standard(arr):
    print("Using standard normalisation")
    pass


def t_stats(arr):
    print("Using t-stats normalisation")
    pass


def main(dataarray, mode):
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    if mode == "standard":
        return standard(dataarray)
    else:
        return t_stats(dataarray)
