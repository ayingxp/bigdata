from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")

sc = SparkContext(conf=conf)

# pyspark默认读取存储在hdfs的文件(数据)
# 如果需要读取本地的文件,则使用绝对路径: file:///path/to/file
# 当传入的路径为一个文件夹的路径而非具体的文件时，spark会默认把该目录下的所有文件都读取进来

logFile="file:///home/hadoop/bigdata/readme.md"

logData = sc.textFile(logFile, 2).cache()

numAs = logData.filter(lambda line: 'a' in line).count()
numBs = logData.filter(lambda line: 'b' in line).count()

print("Lines with a: %s, Lines with b: %s " % (numAs, numBs))
