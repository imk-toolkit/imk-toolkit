#!/usr/bin/env python
# coding: utf-8
"""Calculate anomalies within a xr.DataArray."""
import xarray as xr
from imktk import cli_argument


def main(dataarray):
    """Return monthly anomalies for dataarray."""
    assert isinstance(dataarray, xr.DataArray), "Input is not an xr.DataArray"
    climatology = dataarray.groupby("time.month").mean("time")
    anomalies = dataarray.groupby("time.month") - climatology
    return anomalies


def _arguments():
    return [
        cli_argument("-i", "--input", help="Inputfile", required=True),
        cli_argument("-o", "--output", help="Outputfile", required=True),
        cli_argument("-v", "--variable", help="Variable", required=True),
    ]


def _cli(args):
    dataset = xr.open_dataset(args.input)
    dataarray = getattr(dataset, args.variable)
    result = main(dataarray)
    result.to_netcdf(args.output)
