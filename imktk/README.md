# IMK Toolkit

This toolkit provides post-processing scripts developed by members of the
[Institute of Meteorology and Climate Research (IMK)](https://dev.to/epassaro/keep-your-research-reproducible-with-conda-pack-and-github-actions-339n)
at the Karlsruhe Institute of Technology (KIT). The goal of this module is to
gather together python post-processing scripts for the analysis of netCDF
data.

## Install

Choose one of the following methods to install the package:

1. Install using `pip`
2. Install using `conda`
3. Install straight from this repository using `git clone`

This package supports `Python3` starting with version `3.7`. If you are using
an earlier version of `Python` please consider updating your system.

### `pip`

Releases are automatically uploaded to PyPI. Please execute following command
to install the package.

```
python3 -m pip install imktk
```

### `conda`

Currently the package does no support native installation using `conda`
respectively `conda-forge`. This feature is on the roadmap and you can follow
its process using issue [#34](https://github.com/imk-toolkit/imk-toolkit/issues/34).
The current workaround for `conda` installation is to use the following steps
for any given environment `<env>`.

1. Activate the environment
```bash
conda activate <env>
```
2. Install using `pip`
```bash
python3 -m pip install imktk
```

### `git clone`

It is also possible to install the package natively by cloning the repository.
If you are interested in using this method of installation please follow
these steps

1. Clone repository

```bash
git clone https://github.com/imk-toolkit/imk-toolkit.git
```

2. Enter the `imktk` directory and build Python packages for installation. The
installation files will be saved in `imk-toolkit/dist`

```bash
cd imk-toolkit/imktk && python3 -m build
```

3. Enter the `dist` directory and install packages

```bash
cd dist && pip3 install imktk-<current.version>-py3-none-any.whl
```

Please be aware that the package uses `HDF5` and `netCDF` c-library in the
backend. If you are installing using this method consider setting the
`HDF5_DIR` environment variable with the location of the HDF5 header files.


## Usage

```python
import imktk
import xarray as xr

t = xr.tutorial.open_dataset("rasm").load().Tair
anomaly_free_t = t.imktk.anomalies()
```
## Further reading
If you are interested in the inner workings of the package and details of the implementation please refer to the embedded [README.md](https://github.com/imk-toolkit/imk-toolkit/blob/master/imktk/imktk/README.md).
