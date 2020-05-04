import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope='session')
def spark():
    spark = (
        SparkSession
        .builder
        .master('local')
        .appName('adder')
        .getOrCreate()
    )
    yield spark
    spark.stop()


@pytest.fixture(scope='session')
def spark_context(spark):
    sc = spark.sparkContext
    yield sc
    spark.stop()