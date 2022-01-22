# imktk

In the following we will describe in detail the goal, inner workings and
functioning properties of the `imktk` module.

## Idea

As in many other scientific fields there are repeating tasks which have to be
done almost everyone. Most often the predecessors already have done the task
in the past. In an ideal world, these scripts are shared and distributed
within the institute in such a way that everyone has access to them.
Unfortunately often the reality is different. Most tasks are solved by
several times by different individuals and mistakes are repeated. Everyone
has its own way to deal with the problem and find a different solution. The
goal of `imktk` is to enable easy distribution of these post-processing
scripts in atmospheric sciences. Further, the module should help achieve a
reproducible research environment and an easily extensible structure.

- Easy distribution of post-processing script
- Common basis for future developments
- Common coding standards for the development of post-processing script

## Solution

There are two location for the scripts to be saved by the scientists. These
are the folders [`dataset_methods`](./dataset_methods) and
[`dataarray_methods`](./dataarray_methods). All scripts adhering to the
structure defined in next section will be saved in these locations. The
`imktk` will then scan these folders (i.e. on `import imktk`) and extend the
`xarray` module with the functionalities defined in the scripts. All scripts
saved in [`dataset_methods`](./dataset_methods) will be added to the
`xarray.Dataset` class and all scripts saved in [`dataarray_methods`]
(./dataarray_methods) will be added to the `xarray.DataArray` class. The
scripts can then be executed using the filename of the script and `imktk`
extension. Let `Tair` be an `xarray.DataArray` for air temperature. The script
[`anomalies.py`](./dataarray_methods/anomalies.py) can be executed on this
data using the command `temp.imktk.anomalies()`. Here an example:

```python
import imktk
import xarray as xr

t = xr.tutorial.open_dataset("rasm").load().Tair
anomaly_free_t = t.imktk.anomalies()
```

## Requirements

There are two premises which `imktk` assumes about the scripts to be loaded.
These are:

1. The script has a `main(..)` function 2. The first argument of the
`main(..)` is either a `xarray.Dataset` (for [`dataset_methods`](./dataset_methods)
scripts) or `xarray.DataArray` (for [`dataarray_methods`](./dataarray_methods)
scripts)

The toolkit needs a common entrypoint for the execution of the script. This
method must be available in each script. Should the function be not
available, loading of the script will not work and silently fail. This is the
`main` function and it will be executed by the script. The first argument of
this function call will be the element on which the method is being called.
This is the cause for the second premise: It must be either a
`xarray.Dataset` for the scripts at [`dataset_methods`](./dataset_methods)
and a `xarray.DataArray` for the scripts saved at [`dataarray_methods`](./dataarray_methods).


## Implementation

The main skeleton of the module is saved in the [`toolkit.py`](./toolkit.py).
It defines the classes and necessary methods to register the
scripts at the `xarray` endpoint.
