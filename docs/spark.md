# 配置Spark的CLASSPATH

- cd /usr/local/spark
- cp ./conf/spark-env.sh.templates ./conf/spark-env.sh
- 编辑以上的配置文件，在文件最后面加上如下内容
    - export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)

- export SPARK_HOME=/usr/local/spark
- export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.8-src.zip:$PYTHONPATH
- export PATH=$SPARK_HOME/bin:$SPARK_HOME/python:$PATH
- 编辑.bashrc文件, 添加如下内容
    - export PYSPARK_PYTHON=/bbox/anaconda3/bin/python
- 配置ipython
    - export PYSPARK_DRIVER_PYTHON=ipython
    - pyspark
# Spark WebUI
- ./sbin/start-master.sh
    - 启动master结点

# 运行多任务程序

```python
params = [1,2,3,4,5]
def my_func(val):
    print(val*val)

rdd = sc.parallelize(params)

rdd.foreach(my_func)
```
