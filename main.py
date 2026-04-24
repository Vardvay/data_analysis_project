from src.data_loader import DataLoader

loader = DataLoader("data/fitness_data.csv")

df = loader.load_data()

new_record = {
    "program": "split",
    "frequency_per_week": 5,
    "volume_sets": 18,
    "protein_synthesis": 40,
    "strength_gain": 25,
    "testosterone_change": 8,
    "cortisol_change": -4
}

loader.add_record(new_record)
loader.save_data()