from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf=conf)

studentMarksData = [
        ["si1", "year1", 62.08, 62.4],
        ["si1", "year2", 75.94, 76.75],
        ["si2", "year1", 68.26, 72.95],
        ["si2", "year2", 85.49, 75.8],
        ["si3", "year1", 75.08, 79.84],
        ["si3", "year2", 54.98, 87.72],
        ["si4", "year1", 50.03, 66.85],
        ["si4", "year2", 71.26, 69.77],
        ["si5", "year1", 52.74, 76.27],
        ["si5", "year2", 50.39, 68.58],
        ["si6", "year1", 74.86, 60.8],
        ["si6", "year2", 58.29, 62.38],
        ["si7", "year1", 63.95, 74.51],
        ["si7", "year2", 66.69, 56.92]
]

studentMarksDataRDD = sc.parallelize(studentMarksData, 4)

print(studentMarksDataRDD.take(5))