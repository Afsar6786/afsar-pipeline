"""
Example usage of quality_utils
"""

import pandas as pd
from afsar_pipeline import quality_utils as qu

# Sample DataFrame with some issues
data = {
    "Name": ["Afsar", "Basha", "John", "Basha"],
    "Age": [32, None, 28, 40],
    "Role": ["Engineer", "Manager", "Engineer", "CEO"]
}
df = pd.DataFrame(data)

# 1. Check missing values
print("\nMissing Values:\n", qu.check_missing_values(df))

# 2. Check duplicates
print("\nDuplicate Rows Count:", qu.check_duplicates(df))
