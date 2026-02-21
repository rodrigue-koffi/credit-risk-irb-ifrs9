import os
import pandas as pd

# Loader data


def OpenFile(Path: str) -> pd.DataFrame:
    Extension = os.path.splitext(Path)[1].lower()

    if Extension in (".xlsx", ".xls"):
        return pd.read_excel(Path)

    elif Extension in (".csv", ".txt"):
        return pd.read_csv(Path, sep=None, engine="python")

    else:
        raise ValueError(f"Erreur: {Extension}")


# E_P Pipeline
def main():
    Chemin = "data/german_credit_data.xlsx"  # à adapter

    if os.path.exists(Chemin):
        t = OpenFile(Chemin)
        print("Dataset chargé:", t.shape)
    else:
        print("Pas de données dans /data")


if __name__ == "__main__":
    main()