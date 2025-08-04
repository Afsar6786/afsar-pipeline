import pandas as pd
import os

def read_file(path):
    """Auto-detect file type and read into Pandas."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(path)
    elif ext == ".parquet":
        return pd.read_parquet(path)
    elif ext == ".json":
        return pd.read_json(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def save_csv(df, path):
    """Save Pandas DataFrame to CSV."""
    df.to_csv(path, index=False)