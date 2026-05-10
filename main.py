from src.data_loader import DataLoader
from src.CLI import run_cli
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "fitness_data.csv")

loader = DataLoader(file_path)
df = loader.load_data()

run_cli(df)