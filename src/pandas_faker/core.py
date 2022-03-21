import numpy as np
import pandas as pd


def simple_df() -> pd.DataFrame:
    columns = 'A B C D'.split()
    n_rows = 5
    data = np.arange(n_rows * len(columns)).reshape(n_rows, len(columns))
    return pd.DataFrame(data=data, columns=columns)
