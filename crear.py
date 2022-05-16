import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("Prueba").getOrCreate()

#df = spark.read.csv("filosofos\air_traffic_data.csv")


