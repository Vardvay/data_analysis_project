import pandas as pd
import sys

from src.CLI import run_cli


def get_df():
    return pd.DataFrame({
        "program": ["A"],
        "protein_synthesis_change_pct": [10],
        "strength_gain_pct": [5],
        "testosterone_change_pct": [8],
        "cortisol_change_pct": [2],
        "volume_sets": [10]
    })


def test_cli_protein():
    sys.argv = ["prog", "protein"]

    run_cli(get_df())


def test_cli_strength():
    sys.argv = ["prog", "strength"]

    run_cli(get_df())


def test_cli_hormones():
    sys.argv = ["prog", "hormones"]

    run_cli(get_df())


def test_cli_universal():
    sys.argv = ["prog", "universal"]

    run_cli(get_df())


def test_cli_corr():
    sys.argv = ["prog", "corr"]

    run_cli(get_df())


def test_cli_intensity():
    sys.argv = ["prog", "intensity"]

    run_cli(get_df())