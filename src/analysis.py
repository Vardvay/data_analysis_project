import pandas as pd
import numpy as np
import time
df = pd.read_csv("data/fitness_data.csv")




def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Запуск: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Завершение: {func.__name__}")
        return result
    return wrapper



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"[TIME] {func.__name__}: {end - start:.5f} sec")

        return result
    return wrapper


def high_strength_generator(df, threshold=30):
    for _, row in df.iterrows():
        if row["strength_gain"] > threshold:
            yield row


def chunk_generator(df, chunk_size=50):
    for i in range(0, len(df), chunk_size):
        yield df.iloc[i:i + chunk_size]




@logger
@timer
def protein_efficiency(df):
    df = df.copy()
    res = df.groupby("program")["protein_synthesis"].mean().sort_values(ascending = False)
    return res


@logger
@timer
def strength_efficiency(df):
    df = df.copy()
    return (df.groupby("program")["strength_gain"].mean().sort_values(ascending=False))


def hormone_efficiency(df):
    df = df.copy()

    df["hormone_score"] = (df["testosterone_change"] - df["cortisol_change"])

    return (df.groupby("program")["hormone_score"].mean().sort_values(ascending=False))


def universal_program(df):
     df = df.copy()

     df["hormone_score"] = (df["testosterone_change"] - df["cortisol_change"])

     df["score"] = (
         df["protein_synthesis_change"] * 0.4 +
         df["strength_gain"] * 0.4 +
         df["hormone_score"] * 0.2
     )

     return (df.groupby("program")["score"].mean().sort_values(ascending=False))

def mps_volume_correlation(df):
     return np.corrcoef(df["volume_sets"],df["protein_synthesis"])[0, 1]


def intensity_comparison(df):
     df = df.copy()
     df["intensity"] = df["volume_sets"].apply(lambda x: "high" if x > 17 else "low")

     return df.groupby("intensity")[
         [
             "strength_gain",
             "protein_synthesis_change",
             "testosterone_change",
             "cortisol_change"
         ]].mean()


print("\nHIGH STRENGTH ATHLETES:\n")

for athlete in high_strength_generator(df):
    print(
        athlete["program"],
        athlete["strength_gain"]
    )


print("\nCHUNKS:\n")

for chunk in chunk_generator(df, 100):
    print(chunk.shape)