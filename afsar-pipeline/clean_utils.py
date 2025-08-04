def trim_strings(df):
    """Trim whitespace from all string columns."""
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
    return df

def standardize_column_names(df):
    """Convert column names to lowercase and snake_case."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df