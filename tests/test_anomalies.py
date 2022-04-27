"""Test module for anomalies methods."""
import numpy as np
import xarray as xr
from pytest import fixture, mark

from tests import ImktkRequirements, dataarrays_data


# Requirements section ----------------------------------------------
class Requirements(ImktkRequirements):
    def test_some_feature(self, result):
        assert True  # TODO: Assert something has sense

    def test_expected_result(self, result, expected):
        assert True  # TODO: Assert something has sense


# Parametrization section -------------------------------------------
@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestTemperatureAnomalies(Requirements):
    @fixture(scope="class")
    def mock_data(self):
        return dataarrays_data.temperature()

    @fixture(scope="class")
    def expected(self):  # TODO: Create something has sense
        return xr.DataArray(np.random.randn(2, 2, 3))


@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestHumidityAnomalies(Requirements):
    @fixture(scope="class")
    def mock_data(self):
        return dataarrays_data.humidity()

    @fixture(scope="class")
    def expected(self):  # TODO: Create something has sense
        return xr.DataArray(np.random.randn(2, 2, 3))
