# IMK Toolkit
Collection of methods developed by IMK

## Usage

```python
import imktk
import xarray as xr

t = xr.tutorial.open_dataset("rasm").load().Tair
anomaly_free_t = t.imktk.anomalies()
```
