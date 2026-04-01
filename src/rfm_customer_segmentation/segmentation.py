# segmentation.py

"""
Business logic for customer segmentation.
"""


def segment_customer(row):
    """
    Assign segment based on RFM scores.
    
    Why:
    - Converts numbers → business meaning
    """
    
    r, f, m = int(row['R_score']), int(row['F_score']), int(row['M_score'])

    if r >= 4 and f >= 4 and m >= 4:
        return 'Champions'
    elif r >= 3 and f >= 3:
        return 'Loyal Customers'
    elif r >= 4 and f <= 2:
        return 'Potential Loyalists'
    elif r <= 2 and f >= 3:
        return 'At Risk'
    elif r <= 2 and f <= 2:
        return 'Lost Customers'
    return 'Others'


def apply_segmentation(rfm):
    """
    Apply segmentation to entire dataframe.
    """
    rfm['Segment'] = rfm.apply(segment_customer, axis=1)
    return rfm