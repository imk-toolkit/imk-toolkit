"""Module for tests initialization and common class requirements."""
import xarray as xr


class ImktkRequirements:
    def test_first_argument(self, folder, args):
        if folder == "dataarray_methods":
            assert isinstance(args[0], xr.DataArray)
        if folder == "dataset_methods":
            assert isinstance(args[0], xr.Dataset)
