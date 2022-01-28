#!/usr/bin/env python
# coding: utf-8
"""
Calculate number density from mixing ratio, temperature and pressure within a xr.DataArray.
Usage:
    xr.DataArray.nd(temperature, pressure)

    temperature:   in K
    pressure:      in Pa
        either as vector in case of pressure levels or as matrix in case of model levels

    return value: number density in m-3

author: Stefan Versick (KIT)
"""
import xarray as xr
import numpy as np


def main(dataarray, temp, press):
    """Return number density for dataarray."""
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    assert isinstance(temp, xr.DataArray), "Temperature is not an xr.DataArray"
    assert isinstance(press, xr.DataArray), "Pressure is not an xr.DataArray"
    assert dataarray.shape == temp.shape, "Input and Temperature are not of the same shape"
    avogadro = 6.02214076e23  # mol-1
    r_gas = 8.31446261815324  # J mol-1 K-1
    if press.ndim == 1:  # data on fixed pressure grid
        press_mdim = np.array(int(dataarray.size / press.size) * [press.values]).reshape(dataarray.shape)
    else:  # data on model levels
        press_mdim = press
    assert dataarray.shape == press_mdim.shape, "Input and Pressure are not of the same shape"
    var_nd = avogadro * press_mdim / (r_gas * temp) * dataarray
    return var_nd
