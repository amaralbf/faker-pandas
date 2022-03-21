import pandas as pd

import pandas_faker as pf


def test_simple_df_return_type():
    df = pf.simple_df()
    assert isinstance(df, pd.DataFrame)


def test_simple_df_has_multiple_cols_and_rows():
    df = pf.simple_df()
    rows, cols = df.shape
    assert rows > 1 and cols > 1
