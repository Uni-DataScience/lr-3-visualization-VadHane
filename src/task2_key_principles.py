import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Create a scatter plot using Seaborn
    fig, ax = plt.subplots()
    sns.scatterplot(x='x', y='y', data=data, ax=ax)
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot')

    return fig



# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
