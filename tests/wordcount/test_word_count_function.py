from pytest_spark import spark_context
from wordcount.word_count_function import word_count

def test_word_count_function(spark_context):
    counts = word_count(spark_context.parallelize(list("Hello World")))
    assert counts == [('l', 3), ('o', 2), ('H', 1), ('e', 1), (' ', 1), ('W', 1), ('r', 1), ('d', 1)]
