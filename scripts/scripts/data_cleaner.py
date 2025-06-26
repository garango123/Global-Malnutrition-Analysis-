def clean_data(df):
    """
    Clean the dataset by handling missing values and duplicates.
    """
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill or drop missing values
    df = df.dropna()  # Or you can use fillna if appropriate
    
    print("✅ Data cleaned successfully.")
    return df
