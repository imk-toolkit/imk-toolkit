#!/usr/bin/env python
# coding=utf-8
"""Extensions for Xarray for analysing weather data."""
import functools
import importlib as ilib
import os
import sys
import xarray as xr
import logging

_DA_ENV = "IMKTK_DATAARRAY"
_DS_ENV = "IMKTK_DATASET"
_LOG_LEVEL = "IMKTK_LOGLEVEL"


def _get_log_level_via_env():
    loglevel = os.environ.get(_LOG_LEVEL, "ERROR")
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {loglevel}")
    return numeric_level


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=_get_log_level_via_env())
logger = logging.getLogger(__name__)


@xr.register_dataarray_accessor("imktk")
class _NyxDA(object):
    def __init__(self, data):
        self._data = data

    def _add_methods(self, folder):
        return _add_folder(folder, mode="da")

    def _load_env(self):
        return _load_from_env(mode="da")

    def __repr__(self):
        add_methods = [x for x in dir(self) if not x.startswith("_")]
        return f"IMKTK.Dataarray(scripts: {add_methods})"


@xr.register_dataset_accessor("imktk")
class _NyxDS(object):
    def __init__(self, data):
        self._data = data

    def _add_methods(self, folder):
        return _add_folder(folder, mode="ds")

    def _load_env(self):
        return _load_from_env(mode="ds")

    def __repr__(self):
        add_methods = [x for x in dir(self) if not x.startswith("_")]
        return f"IMKTK.Dataset(scripts: {add_methods})"


def _patch(func, funcname, mode):
    classobject = _NyxDA if mode == "da" else _NyxDS

    @functools.wraps(func)
    def method(accessor, *args, **kwargs):
        return func(accessor._data, *args, **kwargs)

    setattr(classobject, funcname, method)
    return func


def xtend_dataarray(da_folder=None):
    return _add_folder(da_folder, "da")


def xtend_dataset(ds_folder=None):
    return _add_folder(ds_folder, "ds")


def _add_folder(folder, mode=None):
    assert isinstance(mode, str) and mode.lower() in ["ds", "da"], "Can not understand mode {}".format(mode)
    assert os.path.isdir(folder), '"{}" is not a folder'.format(folder)
    mode = mode.lower()
    folder = os.path.realpath(folder)

    pythonfiles = [x[:-3] for x in os.listdir(folder) if x.endswith(".py") and not x.startswith("_")]
    if not pythonfiles:
        logger.warning("Folder %s is empty. No methods added.", folder)
        return None
    sys.path.insert(0, folder)
    for method in pythonfiles:
        try:
            lib = ilib.import_module(method, package="imktk")
            _patch(getattr(lib, "main"), method, mode)
            logger.info("Method: %s added in mode: %s", method, mode)
        except (SystemError, ImportError) as err:
            logger.error("Method: %s not loaded. Because: %s", method, err)
        except AttributeError as err:
            logger.error("Method: %s has no 'main' function (err: %s).", method, err)
    return True


def _load_from_env(mode=None):
    if mode is None:
        _ = [_load_from_env(x) for x in ["da", "ds"]]
        return None
    envvar = _DA_ENV if mode == "da" else _DS_ENV
    env = os.environ.get(envvar, False)
    if not env:
        logger.warning("ENV %s not set. No methods added.", env)
        return None
    folders = env.split(":")
    for folder in folders:
        logger.info("Adding folder %s as %s (ENV: %s)", folder, mode, env)
        _add_folder(folder, mode)
