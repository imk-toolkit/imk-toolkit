# IMK Toolkit

This toolkit provides [post-processing scripts](/imktk) developed by members of the
[Institute of Meteorology and Climate Research (IMK)](https://dev.to/epassaro/keep-your-research-reproducible-with-conda-pack-and-github-actions-339n)
at the Karlsruhe Institute of Technology (KIT). The goal of this module is to
gather together python post-processing scripts for the analysis of netCDF data
and distribute them easily.

> User provided scripts can be imported using the environmental variables `IMKTK_DATAARRAY` and `IMKTK_DATASET`.

## Usage

```python
import imktk

ds = imktk.tutorial.open_dataset("toy_weather")
anomaly_free_tmin = ds.tmin.imktk.anomalies()
```

For user provided scripts please set up the appropriate environmental variables:

| Supported variables | Description |
|---|---|
|`IMKTK_DATAARRAY`| Path to `xr.DataArray` scripts |
|`IMKTK_DATASET`| Path to `xr.Dataset` scripts |
|`IMKTK_LOGLEVEL`| Print debugging information: `DEBUG`, `INFO`, `WARNING`, `ERROR` |

Environmental variables can be set using `export` command

```bash
export IMKTK_DATAARRAY=/path/to/scripts
```

## Getting Started

The easiest method to test the module is to use an interactive session with docker.
In this environment you will have a Python 3 environment with all necessary dependencies already installed.

```bash
docker run -it imktk/imktk:latest bash
```

> For the brave: You can test the latest release candidate by changing `latest` to `testing`

## Install

Choose one of the following methods to install the package:

1. Install using `pip`
2. Install using `conda`
3. Install using `git clone`

> This package supports only Python 3 with version `>=3.7`. If you are using
> an earlier version of Python please consider updating.

### `pip`

Releases are automatically uploaded to PyPI. Please execute following command
to install the package.

```bash
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

1. Install build dependencies

    ```bash
    python3 -m pip install build
    ```

2. Clone repository

    ```bash
    git clone https://github.com/imk-toolkit/imk-toolkit.git
    ```

3. Generate the Python packages

    ```bash
    python3 -m build  # or `make build`
    ```

4. Install packages

    ```bash
    pip3 install dist/imktk-<current.version>-py3-none-any.whl  # or `make install`
    ```

> Please be aware that this package uses `HDF5` and `netCDF` c-libraries in the
> backend. If you are installing using `git clone` the `HDF5_DIR` environment
> variable with the location of the HDF5 header files needs to be set.

## Further reading

If you are interested in the inner workings of the package and details of the
implementation please refer to the embedded [README.md](/imktk/README.md).
