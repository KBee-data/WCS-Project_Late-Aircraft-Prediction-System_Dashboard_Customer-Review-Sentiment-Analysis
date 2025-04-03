import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_column_uniqueness(df):
    """
    Analyzes the uniqueness of each column and prints unique values if they appear in less than 50% of rows.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    total_rows = len(df)
    
    for col in df.columns:
        unique_count = df[col].nunique()
        if unique_count < total_rows * 0.5:
            unique_values = list(df[col].unique())
            print(f"{col} : {unique_values}")


def detect_and_visualize_outliers(df):
    """
    Detects outliers in numeric columns using the IQR method, displays a heatmap of missing values,
    and visualizes numeric data distributions and correlations.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    """
    numeric_columns = df.select_dtypes(include=[np.number]).columns

    if numeric_columns.empty:
        print("\n!!! No numeric columns detected. Skipping outlier analysis and visualizations.")
        return

    # Function to detect outliers using IQR
    def detect_outliers(col):
        q1 = col.quantile(0.25)
        q3 = col.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = col[(col < lower_bound) | (col > upper_bound)]
        return outliers

    # Count outliers for each numeric column
    print("\nDetecting outliers for numeric columns:")
    outliers_count = {col: len(detect_outliers(df[col])) for col in numeric_columns}
    total_rows = len(df)

    # Create a DataFrame with outlier information
    outliers_df = pd.DataFrame(outliers_count, index=['Number of values'])
    outliers_df.loc['% of values'] = (outliers_df.loc['Number of values'] / total_rows) * 100

    print("\nOutliers Summary:")
    print(outliers_df)

    # HEATMAP OF MISSING VALUES
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Heatmap of Missing Values')
    plt.show()

    # DISTRIBUTION PLOTS FOR NUMERIC COLUMNS
    num_numeric_cols = len(numeric_columns)
    cols_per_row = 3
    num_rows = (num_numeric_cols + cols_per_row - 1) // cols_per_row  # Calculate required rows

    fig, axes = plt.subplots(num_rows, cols_per_row, figsize=(12, 3 * num_rows))
    axes = axes.flatten()

    for i, col in enumerate(numeric_columns):
        sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

    # BOXPLOTS FOR OUTLIERS
    fig, axes = plt.subplots(num_rows, cols_per_row, figsize=(12, 1.5 * num_rows))
    axes = axes.flatten()

    for i, col in enumerate(numeric_columns):
        sns.boxplot(x=df[col], ax=axes[i])
        axes[i].set_title(f'Boxplot of {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

    # PAIRPLOT (if sufficient numeric columns)
    if len(numeric_columns) > 1:
        print("\nPairplot Visualization:")
        sns.pairplot(df[numeric_columns])
        plt.show()

    # HEATMAP CORRELATION MATRIX
    corr_matrix = df[numeric_columns].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.1f', linewidths=.5, mask=mask, cbar_kws={"shrink": .8})
    plt.title('Heatmap Correlation Matrix')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.show()
