""" Data Generation for tutorials and examples

This module provides artifical data for tutorials.
Each example data is provided via a function e.g. `_xarray_toy_weather_data`.
These functions are collected using the `_TUTORIAL_DATA` variable.
There the `key` is being defined by which the data can be called.
Finally, the method `open_dataset` actually delivers the data.

All functions have the same argument and parameter space for easy interoberability.
The current argument and parameter space is as follows:

```python
def function_name(seed):
    pass
```
"""
import numpy as np
import xarray as xr
import pandas as pd


def _xarray_toy_weather_data(seed=None):
    """Generate toy weather data.

    Generate toy weather data using the method defined in
    https://xarray.pydata.org/en/stable/examples/weather-data.html#Toy-weather-data

    Arguments
    =========
    seed: Seed value for random number generation

    Returns
    =======
    dataset: Generated dataset
    """
    if seed:
        np.random.seed(seed)
    times = pd.date_range("2000-01-01", "2001-12-31", name="time")
    annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

    base = 10 + 15 * annual_cycle.reshape(-1, 1)
    tmin_values = base + 3 * np.random.randn(annual_cycle.size, 3)
    tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 3)

    dataset = xr.Dataset(
        {
            "tmin": (("time", "location"), tmin_values),
            "tmax": (("time", "location"), tmax_values),
        },
        {"time": times, "location": ["IA", "IN", "IL"]},
    )

    return dataset


# Dictionary for mapping keywords to each function providin example data
_TUTORIAL_DATA = {
    "toy_weather": _xarray_toy_weather_data,
    "xarray": _xarray_toy_weather_data,
}


def open_dataset(keyword, seed=None):
    """Provides example data based on keyword.


    Arguments
    =========
    keyword: Keyword which identifies which method to use for data generation
    seed: Seed value for random number generation

    Returns
    =======
    dataset: Generated dataset
    """
    try:
        return _TUTORIAL_DATA[keyword](seed)
    except KeyError:
        msg = f"Could not find {keyword} in tutorial data"
        raise KeyError(msg)
