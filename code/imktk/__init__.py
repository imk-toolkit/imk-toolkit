import os
from .toolkit import _add_folder


def main():
    loc, da, ds = location()
    print(f"File location is '{loc}' with folders {da} and {ds} for methods")


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
