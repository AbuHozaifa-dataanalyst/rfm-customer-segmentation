# data_preprocessing.py

"""
Handles raw data loading and cleaning.
This is the FIRST real step in the pipeline.
"""

import pandas as pd
from .utils import (
    convert_to_datetime,
    remove_missing_customer,
    remove_invalid_values,
)


def read_csv_latin1(*args, **kwargs):
    return pd.read_csv(*args, encoding='latin1', **kwargs)


def load_data(file_path):
    """
    Load raw CSV data.
    """
    return read_csv_latin1(file_path)


def clean_data(df):
    """
    Perform full data cleaning pipeline.
    
    Steps:
    1. Rename columns
    2. Convert date
    3. Remove invalid rows
    """
    
    # Standardize column names
    df = df.rename(columns={
        'Customer ID': 'customer_id',
        'Invoice': 'invoice_no',
        'InvoiceDate': 'invoice_date',
        'Quantity': 'quantity',
        'UnitPrice': 'unit_price'
    })

    # Convert date
    df = convert_to_datetime(df, 'invoice_date')

    # Remove bad data
    df = remove_missing_customer(df)
    df = remove_invalid_values(df)

    # Create revenue column
    df['TotalAmount'] = df['quantity'] * df['unit_price']

    return df