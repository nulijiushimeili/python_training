from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

# pyspark test
# RDD
# Python怎么反应这么慢,如果数据量不是特别大的话,还是pandas吧

# 创建sparkconf 对象
conf = SparkConf().setAppName("Test Spark").setMaster("local")
# 创建sparkcontext对象
sc = SparkContext(conf=conf)
# 加载文件
file = sc.textFile("D:\mycode1\program\python_training\spark\emp.txt")
# 将文件的内容切分,转换成Tuple形势
map_rdd = file.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))
# 对相同key的tuple进行reduce操作
word_count = map_rdd.reduceByKey(lambda k, v: k + v)
word_count.foreach(print)

# spark DataFrame
spark = SparkSession \
    .builder \
    .appName("spark dataframe") \
    .master("local") \
    .getOrCreate()

# 读取json文件
df = spark.read.json("D:\mycode1\program\python_training\spark\parse.json")
df.show()

# 等到地老天荒呀... , 参考资料见官网
# http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes
