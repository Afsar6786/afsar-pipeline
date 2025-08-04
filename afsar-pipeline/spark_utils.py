from pyspark.sql import SparkSession

def get_spark(app_name="PipelineApp"):
    """Get or create a Spark session."""
    return SparkSession.builder.appName(app_name).getOrCreate()

def read_spark_csv(spark, path):
    """Read CSV file into Spark DataFrame."""
    return spark.read.csv(path, header=True, inferSchema=True)