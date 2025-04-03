import numpy as np

def numeric_vs_categorical(df):
    """Identifies numeric and categorical columns in a DataFrame."""
    
    # Display list of columns
    print("\nList of column names:")
    print(df.columns.tolist())

    # Identify numeric vs. categorical columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    print(f"\nNumeric columns:\n{numeric_columns}")
    print(f"\nCategorical columns:\n{categorical_columns}")

    # Columns that can be used for one-hot encoding
    dummies_columns = df.columns[df.nunique() < 10].tolist()
    print("\nColumns that can be used for one-hot encoding (<10 unique values):")
    print(dummies_columns)

    # List of unique values for columns with less than 50% unique entries
    total_rows = len(df)
    low_unique_columns = [col for col in df.columns if df[col].nunique() / total_rows < 0.5]
    
    print("\nList of Unique values for columns with less than 50% unique entries:")
    print(low_unique_columns)

    # Return results as a dictionary
    return {
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "dummies_columns": dummies_columns,
        "low_unique_columns": low_unique_columns
    }
