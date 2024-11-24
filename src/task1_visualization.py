import matplotlib.pyplot as plt
import numpy as np
import collections
from collections import Counter


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    
    # Count the occurrences of each category
    count = Counter(data)
    
    # Separate the categories and their counts
    categories = list(count.keys())
    counts = list(count.values())
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(categories, counts)
    
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title('Category Distribution')
    
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
