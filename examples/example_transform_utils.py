"""
Example usage of transform_utils
"""

import pandas as pd
from afsar_pipeline import transform_utils as tu

# Sample DataFrame
data = {
    "Name": ["Afsar", "Basha", "John"],
    "Age": [32, 40, 28],
    "Salary": [50000, 60000, 45000]
}
df = pd.DataFrame(data)

# 1. Rename columns
df = tu.rename_columns(df, {"Name": "FullName", "Salary": "AnnualSalary"})
print("\nRenamed Columns:\n", df)

# 2. Filter rows (Age > 30)
df_filtered = tu.filter_rows(df, df["Age"] > 30)
print("\nFiltered Rows:\n", df_filtered)

# 3. Add a calculated column (Bonus = Salary * 0.10)
df_with_bonus = tu.add_calculated_column(df, "Bonus", lambda row: row["AnnualSalary"] * 0.10)
print("\nWith Bonus Column:\n", df_with_bonus)