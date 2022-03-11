"""Generic fixtures for testing."""
import importlib
import sys

from pytest import fixture

# Session fixtures --------------------------------------------------


# Common class fixtures ---------------------------------------------
@fixture(scope="class", autouse=True)
def method(module, folder):
    importlib.import_module(f"imktk.{folder}.{module}")
    return sys.modules[module].main


@fixture(scope="class", params=[])
def module(request):
    return request.param


@fixture(scope="class", params=[])
def folder(request):
    return request.param

@fixture(scope="class")
def result(method, args, kwargs):
    return method(*args, **kwargs)


@fixture(scope="class")
def args(mock_data):
    return (mock_data,)


@fixture(scope="class")
def kwargs():
    return {}
