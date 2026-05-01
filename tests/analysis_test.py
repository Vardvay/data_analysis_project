import pandas as pd
from src.analysis import protein_efficiency

def test_on_real_data():
    df = pd.read_csv("data/fitness_data.csv")
    result = protein_efficiency(df)

    assert not result.empty
    assert isinstance(result, pd.Series)
    assert result.iloc[1] >= result.iloc[0]