import argparse
from src.analysis import (
    protein_efficiency,
    strength_efficiency,
    hormone_efficiency,
    universal_program,
    mps_volume_correlation,
    intensity_comparison
)


def run_cli(df):
    parser = argparse.ArgumentParser(description="Fitness Data Analysis CLI")

    parser.add_argument(
        "command",
        help="Command: protein | strength | hormones | universal | corr | intensity"
    )

    args = parser.parse_args()

    if args.command == "protein":
        print("\nЭффективность по синтезу белка:\n")
        print(protein_efficiency(df))

    elif args.command == "strength":
        print("\nЭффективность по росту силы:\n")
        print(strength_efficiency(df))

    elif args.command == "hormones":
        print("\nГормональная эффективность:\n")
        print(hormone_efficiency(df))

    elif args.command == "universal":
        print("\nУниверсальная программа:\n")
        print(universal_program(df))

    elif args.command == "corr":
        print("\nКорреляция объёма и синтеза белка:\n")
        print(mps_volume_correlation(df))

    elif args.command == "intensity":
        print("\nСравнение интенсивности:\n")
        print(intensity_comparison(df))

    else:
        print("Неизвестная команда")