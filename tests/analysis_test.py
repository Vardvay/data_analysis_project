import pandas as pd

from src.analysis import (
    protein_efficiency,
    strength_efficiency,
    hormone_efficiency,
    universal_program,
    mps_volume_correlation,
    intensity_comparison
)

def test_on_real_data():
    df = pd.read_csv("data/fitness_data.csv")

def get_df():
    return pd.DataFrame({
        "program": ["A", "A", "B"],
        "protein_synthesis_change_pct": [10, 20, 30],
        "strength_gain_pct": [5, 10, 15],
        "testosterone_change_pct": [8, 9, 10],
        "cortisol_change_pct": [2, 3, 1],
        "volume_sets": [10, 20, 25]
    })


def test_protein_efficiency():
    df = get_df()

    result = protein_efficiency(df)

    assert result.index[0] == "B"


def test_strength_efficiency():
    df = get_df()

    result = strength_efficiency(df)

    assert result.index[0] == "B"


def test_hormone_efficiency():
    df = get_df()

    result = hormone_efficiency(df)

    assert result.index[0] == "B"


def test_universal_program():
    df = get_df()

    result = universal_program(df)

    assert result.index[0] == "B"


def test_mps_volume_correlation():
    df = get_df()

    result = mps_volume_correlation(df)

    assert isinstance(result, float)


def test_intensity_comparison():
    df = get_df()

    result = intensity_comparison(df)

    assert "high" in result.index
    assert "low" in result.index