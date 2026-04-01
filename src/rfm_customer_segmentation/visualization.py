# visualization.py

"""
Visualization functions for business insights.
"""

import matplotlib.pyplot as plt


def plot_segment_distribution(rfm):
    """
    Plot number of customers per segment.
    """
    rfm['Segment'].value_counts().plot(kind='bar')
    plt.title('Customer Segment Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_revenue_by_segment(rfm):
    """
    Plot revenue contribution by segment.
    """
    rfm.groupby('Segment')['Monetary'].sum().plot(kind='bar')
    plt.title('Revenue by Segment')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()