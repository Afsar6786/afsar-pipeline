def check_missing_values(df):
    """Return columns with missing value counts."""
    return df.isnull().sum()

def check_duplicates(df):
    """Check if DataFrame has duplicate rows."""
    return df.duplicated().sum()