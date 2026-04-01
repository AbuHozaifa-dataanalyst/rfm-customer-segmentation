# rfm_scoring.py

"""
Convert RFM values into scores (1–5).
"""

import pandas as pd


def assign_rfm_scores(rfm):
    """
    Assign quantile-based scores.
    
    Important:
    - Recency is reversed (lower is better)
    """
    
    rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
    rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

    return rfm