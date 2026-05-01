import pandas as pd
import numpy as np
df = pd.read_csv("data/fitness_data.csv")
def protein_efficiency(df):
    df = df.copy()
    res = df.groupby("program")["protein_synthesis"].mean().sort_values(ascending = False)
    return res
print(protein_efficiency(df))