from pyspark.sql import SparkSession
# spark_session = (SparkSession.builder.master('local[*]')
# .config("spark.executor.memory","4g")
# .config("spark.executor.cores","2")
# .config("spark.files.maxPartitionBytes","134217728")
# .appName('finance_complaint').getOrCreate())


# spark_session = SparkSession.builder.master('local[*]').appName('finance_complaint') \
#     .config("spark.executor.instances", "2") \
#     .config("spark.executor.memory", "12g") \
#     .config("spark.driver.memory", "12g") \
#     .config("spark.executor.memoryOverhead", "12g") \
#     .getOrCreate()

spark_session = SparkSession.builder \
    .appName("finance_complaint") \
    .master("local") \
    .getOrCreate()
