import pandas as pd
import numpy as np
df = pd.read_csv("data/fitness_data.csv")
def protein_efficiency(df):
    df = df.copy()
    res = df.groupby("program")["protein_synthesis"].mean().sort_values(ascending = False)
    return res


def strength_efficiency(df):
    df = df.copy()
    return (
        df.groupby("program")["strength_gain_pct"]
        .mean()
        .sort_values(ascending=False)
    )


def hormone_efficiency(df):
    df = df.copy()

    df["hormone_score"] = (
        df["testosterone_change_pct"] - df["cortisol_change_pct"]
    )

    return (
        df.groupby("program")["hormone_score"]
        .mean()
        .sort_values(ascending=False)
    )


def universal_program(df):
     df = df.copy()

     df["hormone_score"] = (
         df["testosterone_change_pct"] - df["cortisol_change_pct"])

     df["score"] = (
         df["protein_synthesis_change_pct"] * 0.4 +
         df["strength_gain_pct"] * 0.4 +
         df["hormone_score"] * 0.2
     )

     return (df.groupby("program")["score"].mean().sort_values(ascending=False))

def mps_volume_correlation(df):
     return np.corrcoef(df["volume_sets"],df["protein_synthesis_change_pct"])[0, 1]


def intensity_comparison(df):
     df = df.copy()
     df["intensity"] = df["volume_sets"].apply(lambda x: "high" if x > 17 else "low")

     return df.groupby("intensity")[
         [
             "strength_gain_pct",
             "protein_synthesis_change_pct",
             "testosterone_change_pct",
             "cortisol_change_pct"
         ]].mean()