# utils.py

"""
Utility functions used across the RFM project.
This file contains reusable helpers to keep code DRY (Don't Repeat Yourself).
"""

import pandas as pd

def read_csv_latin1(*args, **kwargs):
    return pd.read_csv(*args, encoding='latin1', **kwargs)


def convert_to_datetime(df, column):
    """
    Convert a column to datetime format safely.
    
    Why:
    - RFM depends on date calculations
    - Raw data often has incorrect formats
    """
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df


def remove_missing_customer(df):
    """
    Remove rows where customer_id is missing.
    
    Why:
    - Cannot calculate RFM without customer_id
    """
    return df.dropna(subset=['customer_id'])


def remove_invalid_values(df):
    """
    Remove rows with negative quantity or price.
    
    Why:
    - Negative values = returns
    - RFM focuses on actual purchases
    """
    df = df[df['quantity'] > 0]
    df = df[df['unit_price'] > 0]
    return df