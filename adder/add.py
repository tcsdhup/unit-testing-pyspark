import pyspark.sql.functions as F

def add_columnwise(sdf, col1, col2):
    df_with_new_column = sdf.withColumn('sum', F.col(col1) + F.col(col2))
    return df_with_new_column