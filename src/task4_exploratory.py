import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # 1. Descriptive statistics
    print("Descriptive Statistics:")
    print(df.describe())
    print("\n")

    # 2. Outlier detection using boxplot
    print("Outlier Detection (Boxplot):")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.title('Outlier Detection - Boxplot')
    plt.show()

    # 3. Correlation analysis
    print("Correlation Analysis:")
    correlation_matrix = df.corr()
    print(correlation_matrix)
    
    # Visualize the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
