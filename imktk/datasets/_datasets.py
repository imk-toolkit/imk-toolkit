__all__ = ["get"]

import os
import xarray as xr

DATA_FOLDER = os.path.dirname(__file__)
KEYWORDS = {
    "era5": "netcdf/era5.reanalysis.2020.nc",
}


def get(keyword):
    if keyword not in KEYWORDS.keys():
        msg = f"Could not find '{keyword}' in example data keyword list: {list(KEYWORDS.keys())}."
        raise KeyError(msg)
    path = os.path.join(DATA_FOLDER, KEYWORDS[keyword])
    if not os.path.exists(path):
        msg = f"Provided path {path} does not exist."
        raise FileNotFoundError(msg)
    data = xr.open_dataset(path)
    return data
