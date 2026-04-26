import pandas as pd

def handle_missing_values(df):
    """
    Handles missing values in the dataframe:
    - Numerical: filled with median
    - Industry: filled with 'Unknown'
    - Company Size: filled with mode
    """
    # Numerical columns
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # Industry column
    if 'Industry' in df.columns:
        df['Industry'] = df['Industry'].fillna('Unknown')
        
    # Company Size column
    if 'Company Size' in df.columns:
        mode_val = df['Company Size'].mode()
        if not mode_val.empty:
            df['Company Size'] = df['Company Size'].fillna(mode_val[0])
            
    return df

def clean_text_data(df):
    """
    Cleans text data: lowercase and strip spaces for all string columns.
    """
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.lower().str.strip()
    return df

def preprocess_data(df):
    """
    Main preprocessing function.
    """
    df = handle_missing_values(df)
    df = clean_text_data(df)
    return df
