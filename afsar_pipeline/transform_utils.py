"""
Transform utilities for afsar_pipeline
"""

import pandas as pd

def rename_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
    """
    Renames columns in a DataFrame based on the provided mapping.
    """
    return df.rename(columns=rename_map)

def filter_rows(df: pd.DataFrame, filter_condition) -> pd.DataFrame:
    """
    Filters rows in a DataFrame based on a condition (boolean mask).
    Example: df['age'] > 30
    """
    return df[filter_condition]

def add_calculated_column(df: pd.DataFrame, col_name: str, calc_function) -> pd.DataFrame:
    """
    Adds a calculated column based on a function applied to the DataFrame.
    """
    df[col_name] = df.apply(calc_function, axis=1)
    return df