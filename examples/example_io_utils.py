"""
Example: Using io_utils to read and write CSV files
"""

from afsar_pipeline import io_utils

# Read a CSV file
df = io_utils.read_file("sample.csv")
print("First 5 rows:")
print(df.head())

# Save it back
io_utils.write_file(df, "output.csv")
print("File saved as output.csv")