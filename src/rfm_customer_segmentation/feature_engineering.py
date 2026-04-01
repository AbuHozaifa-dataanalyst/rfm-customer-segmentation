# feature_engineering.py

"""
Creates RFM metrics from cleaned data.
This is the CORE analytical step.
"""

import pandas as pd


def calculate_rfm(df):
    """
    Calculate Recency, Frequency, Monetary.
    
    Why:
    - These are the 3 pillars of customer segmentation
    """
    
    snapshot_date = df['invoice_date'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('customer_id').agg({
        'invoice_date': lambda x: (snapshot_date - x.max()).days,
        'invoice_no': 'nunique',
        'TotalAmount': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']

    return rfm.reset_index()