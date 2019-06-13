# Unit Testing with PySpark

A minimal unit testing setup with PySpark fixtures.

For CDSW users, you must ensure that the `PYSPARK_PYTHON` environment variable in the CDSW points to the same version of python as the driver (env var `PYSPARK_DRIVER_PYTHON`.)

For instance, you may want to set a project-level environment variable to something like.

```
PYSPARK_PYTHON=/usr/local/bin/python3.6
```