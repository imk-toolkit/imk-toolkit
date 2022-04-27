#!/usr/bin/env python
# coding: utf-8
"""
This module provides a normalization method for imktk.
"""
import xarray as xr


def main(dataarray):
    """One line documentation for data processing.

    Arguments
    =========
    dataarray: Climate dataarray

    Returns
    =======
    dataarray: Normalized climate dataarray
    """
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"

    # add data processing code here

    return dataarray
