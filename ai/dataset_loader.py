import pandas as pd


def load_dataset(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
