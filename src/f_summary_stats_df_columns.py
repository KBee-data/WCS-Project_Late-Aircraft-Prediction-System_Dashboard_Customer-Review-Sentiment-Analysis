import pandas as pd
from IPython.display import display  # import "display" for a formatted output

def generate_summary_table(df):
    """
    Generates a summary table with column names, data types, missing values,
    and descriptive statistics.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to summarize.
        
    Returns:
        pd.DataFrame: A summary DataFrame containing column statistics.
    """
    
    # Create an empty DataFrame to store summary information
    summary_df = pd.DataFrame()
    
    # Add column names
    summary_df['Column Name'] = df.columns
    
    # Add data types
    summary_df['Data Type'] = df.dtypes.values
    
    # Add missing values count
    summary_df['Missing Values'] = df.isnull().sum().values
    
    # Add percentage of missing values
    summary_df['% Missing Values'] = (df.isnull().sum() / len(df) * 100).values

    # Get descriptive statistics and transpose for merging
    stats = df.describe(include='all').T

    # Merge summary table with descriptive statistics
    summary_df = summary_df.merge(stats, left_on='Column Name', right_index=True, how='left')

    return summary_df