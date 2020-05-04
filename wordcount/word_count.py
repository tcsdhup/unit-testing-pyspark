from pyspark import SparkContext  
from operator import add  
import word_count_function
sc = SparkContext()  
data = sc.parallelize(list("Hello World"))  
#counts = data.map(lambda x: (x, 1)).reduceByKey(add).sortBy(lambda x: x[1], ascending=False).collect()
counts = word_count_function.word_count(data)
for (word, count) in counts:  
    print("{}: {}".format(word, count))  
sc.stop()
