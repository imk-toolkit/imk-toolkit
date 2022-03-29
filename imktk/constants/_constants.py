"""
Physical constants used by several scripts.

This file allows for import and registration of all custom constants
in `_custom_defined.py`. Without this boilerplate code the auto_completion would
not know about the constants defined in the module.

Since `scipy` is already providing a bunch of
[constants](https://docs.scipy.org/doc/scipy/reference/constants.html) it is
not necessary to duplicate work. This constant module will first check if a
constant is defined in `_custom_defined.py`. If it is **not** defined there,
it will check scipy.constants` and finally throw an error if not found.
"""
from scipy import constants as _cons
from . import _custom_defined as _cd

__all__ = _cd.__all__ + _cons.__all__


def __getattr__(name):
    if name in _cd.__all__:
        return getattr(_cd, name)
    elif name in _cons.__all__:
        return getattr(_cons, name)
    else:
        raise AttributeError(f"Attribute {name} not found.")
