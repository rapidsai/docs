In the terminal we can open `ipython` and check that we can import and use RAPIDS libraries like `cudf`.

```ipython
In [1]: import cudf
In [2]: df = cudf.datasets.timeseries()
In [3]: df.head()
Out[3]:
                       id     name         x         y
timestamp
2000-01-01 00:00:00  1020    Kevin  0.091536  0.664482
2000-01-01 00:00:01   974    Frank  0.683788 -0.467281
2000-01-01 00:00:02  1000  Charlie  0.419740 -0.796866
2000-01-01 00:00:03  1019    Edith  0.488411  0.731661
2000-01-01 00:00:04   998    Quinn  0.651381 -0.525398
```

You can also access Jupyter via `<VM ip>:8888` in the browser.
Visit `cudf/10-min.ipynb` and execute the cells to try things out.

When running a Dask cluster you can also visit `<VM ip>:8787` to monitor the Dask cluster status.
