"""
Example: Running a basic Spark job using spark_utils
"""

from afsar_pipeline import spark_utils

# Initialize Spark
spark = spark_utils.create_spark_session("ExampleSparkJob")

# Create example DataFrame
data = [("Afsar", 30), ("Basha", 28)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

print("Data in Spark DataFrame:")
df.show()

# Save output
spark_utils.save_dataframe(df, "spark_output.csv")

# Stop Spark
spark.stop()