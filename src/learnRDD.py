from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

filepath = "/home/hadoop/workspace/bigdata/data/README.md"

textFile = spark.read.text("file://"+filepath)
print(textFile.first())
print(textFile.count())
spark.stop()


