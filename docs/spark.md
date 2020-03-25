# 配置Spark的CLASSPATH

- cd /usr/local/spark
- cp ./conf/spark-env.sh.templates ./conf/spark-env.sh
- 编辑以上的配置文件，在文件最后面加上如下内容
    - export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)

- export SPARK_HOME=/usr/local/spark
- export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.8-src.zip:$PYTHONPATH
- export PATH=$SPARK_HOME/bin:$SPARK_HOME/python:$PATH

# Spark WebUI
- ./sbin/start-master.sh
    - 启动master结点
