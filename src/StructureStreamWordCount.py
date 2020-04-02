from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split


"""
nc -kl -p 9999
"""

spark = SparkSession.builder.appName("StructuredNetWorkWordCount").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

lines = spark.readStream.format("socket").option("host", "192.168.1.4").option("port", 9999).load()

words = lines.select(explode(split(lines.value, " ")).alias("word"))

wordCounts = words.groupBy("word").count()

query = wordCounts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
