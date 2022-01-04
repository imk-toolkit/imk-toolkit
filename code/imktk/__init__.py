import os
from .toolkit import _load_from_env

_load_from_env(mode="da")
_load_from_env(mode="ds")


def main():
    loc, da, ds = location()
    print(f"File location is '{loc}' with folders {da} and {ds} for methods")


def location():
    loc = os.path.abspath(__file__)
    directory = os.path.dirname(loc)
    da = os.path.join(directory, "dataarray_methods")
    ds = os.path.join(directory, "dataset_methods")
    return (loc, da, ds)


if __name__ == "__main__":
    main()
