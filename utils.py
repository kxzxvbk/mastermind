import os
import pandas as pd


def load_dataset(root_path, split):
    dataset_path = os.path.join(root_path, f'{split}_dataset.parquet')
    df = pd.read_parquet(dataset_path)
    return df.to_dict('records')
