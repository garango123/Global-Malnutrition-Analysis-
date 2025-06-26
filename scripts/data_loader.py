import pandas as pd

def load_data(filepath):
    """
    Load the dataset from the given filepath.
    """
    try:
        data = pd.read_csv(filepath)
        print("✅ Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
