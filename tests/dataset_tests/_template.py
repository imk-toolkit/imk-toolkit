"""Test module for <<your_module>> methods.
See https://docs.pytest.org/en/7.1.x/ for more information about how to
build your tests following the pytest framework.
"""
from imktk.dataset_methods import your_module
import xarray as xr
from pytest import fixture, mark


# Module fixtures section -------------------------------------------
@fixture(scope="module", autouse=True)
def module_fixture():
    """Some tests will need generic initialization. In adition you might
    want that such initialization executes only once to speed up testing
    or save computational resources.
    Use autouse=True if you want this fixture to be always executed.
    Add many module fixtures as you need.
    """
    # Write here your initialization for the fixture
    yield True  # Use yield after initialization to return data (or None)
    # Write here your tear down for the fixture


# Tests section -----------------------------------------------------
def test_something_simple(module_fixture):
    assert True  # Write your result assert as simple as possible
    assert True  # Write your result assert as simple as possible
    assert True  # Write your result assert as simple as possible


@mark.parametrize("variable", [1, 2, 3])
def test_with_parametrization(module_fixture, variable):
    assert True  # Write your result assert as simple as possible
    assert True  # Write your result assert as simple as possible
    assert True  # Write your result assert as simple as possible
