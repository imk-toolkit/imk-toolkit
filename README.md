# IMK Toolkit

This toolkit provides [post-processing scripts](/imktk) developed by members of the
[Institute of Meteorology and Climate Research (IMK)](https://dev.to/epassaro/keep-your-research-reproducible-with-conda-pack-and-github-actions-339n)
at the Karlsruhe Institute of Technology (KIT). The goal of this module is to
gather together python post-processing scripts for the analysis of netCDF data
and distribute them easily.

## Usage
Simply import the library using `import imktk`. From then on all scripts are
available using the `imktk` attribute:

```python
import imktk

ds = imktk.tutorial.open_dataset("toy_weather")  # Load example dataset
anomaly_free_tmin = ds.tmin.imktk.anomalies()  # Select dataarray `xr.tmin` and execute anomalies script
```

The following is a list of available scripts:


| Description | Example usage | Link to Script
|--------|--------|-------------|
|Calculate temperature for adiabatic process in air|`ds.tmin.imktk.ad_temp(temp_at_0, press_at_0)`| [here](./imktk/dataarray_methods/ad_temp.py)|
|Calculate monthly anomalies|`ds.tmin.imktk.anomalies()`| [here](./imktk/dataarray_methods/anomalies.py)|
|Calculate monthly climatology|`ds.tmin.imktk.climatology()`| [here](./imktk/dataarray_methods/climatology.py)|
|Interpolation routine for flight track (incl. aircraft and satellites)| `ds.tmin.imktk.flight_track(**dims)` | [here](./imktk/dataarray_methods/flight_track.py) |
|Calculate number density from mixing ratio, temperature and pressure| `ds.tmin.imktk.num_den(temp, press)` | [here](./imktk/dataarray_methods/num_den.py)|
|Calculate saturation vapour pressure over ice for temperatures > 110 K| `ds.tmin.imktk.vapour_pres_ice()` | [here](./imktk/dataarray_methods/vapour_pres_ice.py)|
|Calculate saturation vapour pressure over liquid water for temperatures 123 K < T < 332 K|`ds.tmin.imktk.vapour_pres_liq()` | [here](./imktk/dataarray_methods/vapour_pres_liq.py)|

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
