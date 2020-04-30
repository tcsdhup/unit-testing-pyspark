# Unit Testing with PySpark

A minimal unit testing setup with PySpark fixtures.

For CDSW users, you must ensure that the `PYSPARK_PYTHON` environment variable in the CDSW points to the same version of python as the driver (env var `PYSPARK_DRIVER_PYTHON`.)

For instance, you may want to set a project-level environment variable to something like.

pyspark-2.4.5 is not compatible with python3.8, so use version <= 3.7.5

```
PYSPARK_PYTHON=/usr/local/bin/python3.6
```

STEPS:

1. git clone <Repo URL>

2. Create virtualenv venv
>python3 -m venv venv

3. Activate the virtualenv
>source venv/bin/activate

4. Install Dependencies
>pip install -r unit-testing-pyspark/requirements.txt

5. Test the program with python run
>python3 unit-testing-pyspark/wordcount/word_count.py

6. Test the program with spark-submit
>spark-submit unit-testing-pyspark/wordcount/word_count.py

7. Run unit tests
> pytest unit-test-pyspark/
