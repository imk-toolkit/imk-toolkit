"""Test module for imktk.datarray_methods.climatology methods.
See https://docs.pytest.org/en/7.1.x/ for more information about how to
build your tests following the pytest framework.
"""
import numpy as np
import pandas as pd
import xarray as xr
from pytest import fixture

from imktk.dataarray_methods import climatology


# Module fixtures section -------------------------------------------
@fixture(scope="module")
def dataarray():
    """Fixture that generates a mockup dataset with some climatology
    information.
    """
    return xr.DataArray(
        data=15 + 8 * np.random.randn(2, 2, 30),
        dims=["x", "y", "time"],
        coords=dict(
            lon=(["x", "y"], [[-99.83, -99.32], [-99.79, -99.23]]),
            lat=(["x", "y"], [[42.25, 42.21], [42.63, 42.59]]),
            time=pd.date_range("2014-09-06", periods=30),
            reference_time=pd.Timestamp("2014-09-05"),
        ),
        attrs=dict(
            description="Ambient temperature.",
            units="degC",
        ),
    )


# Tests section -----------------------------------------------------
def test_something_simple(dataarray):
    clima = climatology.main(dataarray)
    assert "time" not in clima.coords
    assert "month" in clima.coords
