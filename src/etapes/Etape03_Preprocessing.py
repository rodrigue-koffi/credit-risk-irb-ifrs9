import numpy as np

class Etape03_Preprocessing:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()
        if "Risk" in t.columns and "Defaut" not in t.columns:
            t["Defaut"] = t["Risk"].astype(str).str.lower().map({"good": 0, "bad": 1})
            print("Variable Defaut OK")

  
        t = t.replace([np.inf, -np.inf], np.nan)

        ColonnesNumeriques = t.select_dtypes(include=np.number).columns

       
        t[ColonnesNumeriques] = t[ColonnesNumeriques].fillna(
            t[ColonnesNumeriques].median()
        )

       
        if "Defaut" in t.columns:
            t["Defaut"] = t["Defaut"].astype(int)

        print("Preprocessing OK")

        Contexte["t"] = t
        return Contexte
