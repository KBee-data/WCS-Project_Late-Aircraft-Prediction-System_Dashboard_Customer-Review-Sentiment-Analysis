import pandas as pd
import numpy as np

def percentage_nan_df(df):
    nan_percentage = df.isna().sum() / len(df) * 100
    return nan_percentage