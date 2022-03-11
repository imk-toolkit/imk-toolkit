"""Test module for <<your_module>> methods."""
import numpy as np
import xarray as xr
from pytest import fixture, mark

from tests import ImktkRequirements, dataarrays_data, datasets_data


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


# Requirements section ----------------------------------------------
class Requirements_1(ImktkRequirements):
    """Define your method requirements with a clear list of test methods
    that only assert your specific requirements. Use the parametrization
    section bellow to create the input arguments of this functions.

    In addition, there are already built-in fixtures you can use and replace
    when needed:
     - args: Tuple with arguments used to call `<<method_module>>.main`
     - result: Returns <<method_module>>.main(*args, **kwargs)
    """

    def test_some_feature_1(self, result):
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible

    def test_some_feature_2(self, result):
        assert True  # Write your result assert as simple as possible

    def test_some_feature_3(self, result):
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible

    def test_some_feature_4(self, result):
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible


class Requirements_2(ImktkRequirements):
    """You are not forced to write all your requirements in a single class.
    Split your requirements into many classes as you think the definitions
    make sense.
    """

    def test_extra_feature_1(self, result):
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible

    def test_extra_feature_2(self, result):
        assert True  # Write your result assert as simple as possible
        assert True  # Write your result assert as simple as possible


# Parametrization section -------------------------------------------
@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestExample_SimpleDataArray(Requirements_1):
    """Parametrization simple example for testing single requirements.
    In this example, we define the fixture `mock_data` to return the
    first argument of our main method.

    Note that you are required to parametrize the following:
     - mark.parametrize `folder` to "dataarray_methods" for DataArray methods
     - mark.parametrize `module` with the module name coinaining your main
    """

    @fixture(scope="class")
    def mock_data(self):
        return dataarrays_data.some_data_generator()


@mark.parametrize("folder", ["dataset_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestExample_SimpleDataArray(Requirements_1):
    """Parametrization simple example for testing single requirements.
    In this example, we define `mock_data` to return a dataset for our
    method.

    Note that you are required to parametrize the following:
     - mark.parametrize `folder` to "dataset_methods" for Dataset methods
     - mark.parametrize `module` with the module name coinaining your main
    """

    @fixture(scope="class")
    def mock_data(self):
        return datasets_data.some_data_generator()


@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestExample_MultipleArguments(Requirements_1):
    """Parametrization example for testing your requirements.
    In this example, we use the possibility of defining the fixture `args`
    instead of `mock_data` to return more than one possition arguments for
    our main method.

    It also includes a kwargs fixture with named parameters tp additionally
    add to the method call.
    """

    @fixture(scope="class")
    def args(self):
        return (dataarrays_data.some_data_generator(), "a_second_argument")

    @fixture(scope="class")
    def kwargs(self):
        return dict(param_1="a", param_2="b")


@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestExample_MultipleRequirements(Requirements_1, Requirements_2):
    """Parametrization example for testing multiple requirements.
    In this example, we are subclassing from Requirements 1 and 2. This
    means we are going to execute both lists of requirements under the
    following conditions.

    As `Requirements_2` include tests that require of a `expected` input,
    we are required to create and parametrize such fixture.
    """

    @fixture(scope="class")
    def mock_data(self):
        return dataarrays_data.some_data_generator()

    @fixture(scope="class")
    def expected(self, args, kwargs):
        return xr.DataArray()


@mark.parametrize("folder", ["dataarray_methods"], indirect=True)
@mark.parametrize("module", ["anomalies"], indirect=True)
class TestExample_MultiParametrization(Requirements_1):
    """Parametrization example for testing your requirements.
    In this example, we define the fixture `mock_data` requiring additional
    fixtures to provide multiple combinations for our data.

    We have defined `param_1` and `param_2` with a **params** definition.
    As both definitions include a list of 2 elements, this will generate
    the following 2x2 combination: ('a','x') ('a','y') ('b','x') ('b','y')

    Tests at Requirements_1 will be evaluated one time for each one of the
    generated combinations.
    """

    @fixture(scope="class")
    def mock_data(self, param_1, param_2):
        return dataarrays_data.some_data_generator(param_1, param_2)

    @fixture(scope="class", params=["a", "b"])
    def param_1(self, request):
        return request.param

    @fixture(scope="class", params=["x", "y"])
    def param_2(self, request):
        return request.param
