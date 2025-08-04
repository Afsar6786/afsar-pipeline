"""
Example: Cleaning a DataFrame using clean_utils
"""

import pandas as pd
from afsar_pipeline import clean_utils

# Create dummy DataFrame
data = {
    "Name": ["Afsar", None, "Basha"],
    "Age": [30, None, 28]
}
df = pd.DataFrame(data)

print("Before cleaning:")
print(df)

# Remove nulls
df_clean = clean_utils.remove_nulls(df)
print("\nAfter removing nulls:")
print(df_clean)

# Rename columns
df_renamed = clean_utils.rename_columns(df_clean, {"Name": "FullName"})
print("\nAfter renaming columns:")
print(df_renamed)