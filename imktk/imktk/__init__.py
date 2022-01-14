import os
from importlib import metadata
from .toolkit import _add_folder

__version__ = metadata.version("imktk")


def main():
    loc, da, ds = location()
    print(f"  Library version: {__version__}")
    print(f" Library location: {os.path.dirname(loc)}")
    print(f"Dataarray scripts: {da}")
    print(f"  Dataset scripts: {ds}")


def location():
    loc = os.path.abspath(__file__)
    directory = os.path.dirname(loc)
    da = os.path.join(directory, "dataarray_methods")
    ds = os.path.join(directory, "dataset_methods")
    return (loc, da, ds)


_, da, ds = location()
_add_folder(da, "da")
_add_folder(ds, "ds")


if __name__ == "__main__":
    main()
