import pandas as pd

import pandas_faker as pf


def test_simple_df_return_type():
    df = pf.simple_df()
    assert isinstance(df, pd.DataFrame)
