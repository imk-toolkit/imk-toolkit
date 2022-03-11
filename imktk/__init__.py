import os
from .toolkit import _add_folder, _load_from_env


def get_version():
    try:
        # try new metadata package
        from importlib import metadata

        return metadata.version("imktk")
    except ImportError:
        # backup routine if Python version <= 3.7
        import pkg_resources

        return pkg_resources.get_distribution("imktk").version


__version__ = get_version()


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
_load_from_env()


if __name__ == "__main__":
    main()
