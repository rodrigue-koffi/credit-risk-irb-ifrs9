import numpy as np

class Etape03_Preprocessing:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        # Remplacement infinis
        t = t.replace([np.inf, -np.inf], np.nan)

        # Colonnes numériques
        ColonnesNumeriques = t.select_dtypes(include=np.number).columns

        # Imputation médiane
        t[ColonnesNumeriques] = t[ColonnesNumeriques].fillna(
            t[ColonnesNumeriques].median()
        )

        # Typage défaut si présent
        if "Defaut" in t.columns:
            t["Defaut"] = t["Defaut"].astype(int)

        print("Preprocessing OK")

        Contexte["t"] = t
        return Contexte