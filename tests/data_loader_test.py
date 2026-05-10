import pandas as pd
import os

from src.data_loader import DataLoader


def test_load_data():
    path = "test.csv"

    with open(path, "w") as f:
        f.write("a,b\n1,2\n3,4")

    loader = DataLoader(path)
    df = loader.load_data()

    assert len(df) == 2

    os.remove(path)


def test_clean_data():
    path = "test_clean.csv"

    with open(path, "w") as f:
        f.write("a,b\n1,2\n3,\n4,5")

    loader = DataLoader(path)
    loader.load_data()

    df = loader.clean_data()

    assert df.isna().sum().sum() == 0

    os.remove(path)


def test_get_data():
    path = "test_get.csv"

    with open(path, "w") as f:
        f.write("a,b\n1,2")

    loader = DataLoader(path)

    df = loader.get_data()

    assert len(df) == 1

    os.remove(path)


def test_validate_record():
    loader = DataLoader("test.csv")

    record = {
        "program": "A",
        "frequency_per_week": 3,
        "volume_sets": 15,
        "protein_synthesis": 10,
        "strength_gain": 5,
        "testosterone_change": 4,
        "cortisol_change": 2
    }

    loader.validate_record(record)


def test_validate_record_error():
    loader = DataLoader("test.csv")

    record = {
        "program": "A"
    }

    try:
        loader.validate_record(record)
        assert False
    except ValueError:
        assert True


def test_add_record():
    path = "test_add.csv"

    with open(path, "w") as f:
        f.write(
            "program,frequency_per_week,volume_sets,"
            "protein_synthesis,strength_gain,"
            "testosterone_change,cortisol_change\n"
        )

    loader = DataLoader(path)
    loader.load_data()

    record = {
        "program": "A",
        "frequency_per_week": 3,
        "volume_sets": 15,
        "protein_synthesis": 10,
        "strength_gain": 5,
        "testosterone_change": 4,
        "cortisol_change": 2
    }

    df = loader.add_record(record)

    assert len(df) == 1
    assert "id" in df.columns

    os.remove(path)


def test_save_data():
    path = "test_save.csv"

    loader = DataLoader(path)

    loader.df = pd.DataFrame({
        "a": [1, 2]
    })

    loader.save_data()

    assert os.path.exists(path)

    os.remove(path)