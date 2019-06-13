import pytest
import os
import pandas as pd
import numpy as np

from numpy.testing import assert_array_equal
from pyspark.sql import SparkSession, DataFrame

from adder.add import add_columnwise


ROOT_DIR = os.getcwd()

@pytest.fixture
def input_df(spark):
    pdf = pd.DataFrame({
        'a': [0,  1, 2],
        'b': [1, -1, 3]
    })
    
    df = spark.createDataFrame(pdf)
    return df
    

class TestAddColumnwise:
    def test_returns_dataframe(self, input_df):
        """Return type should be DataFrame."""
        out_df = add_columnwise(input_df, 'a', 'b')
        assert isinstance(out_df, DataFrame)
        
    def test_returns_same_number_of_rows(self, input_df):
        """Summing colums should not change number of rows."""
        out_df = add_columnwise(input_df, 'a', 'b')
        assert out_df.count() == input_df.count()
        
    def test_adds_a_new_column(self, input_df):
        """
        Adding two columns should append a new column to the input
        dataframe.
        """
        out_df = add_columnwise(input_df, 'a', 'b')
        assert len(out_df.columns) == len(input_df.columns) + 1
    
    def test_sum_works_for_integers(self, spark, input_df):
        """
        Adding column a of integers to column b of integers works
        as expected.
        """
        out_df = add_columnwise(input_df, 'a', 'b')
        out_array = out_df.toPandas()['sum'].values
        expected_array = np.array([1, 0, 5])
        assert_array_equal(out_array, expected_array)