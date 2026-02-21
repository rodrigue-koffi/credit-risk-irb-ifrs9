import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class Etape04_PD_TTC:
    def __init__(self):
        self.Modele = None
        self.Scaler = StandardScaler()

    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        if "Defaut" not in t.columns:
            print(" PD non calculée")
            return Contexte

        # Variables num
        Variables = t.select_dtypes(include=np.number).columns.tolist()
        Variables = [v for v in Variables if v != "Defaut"]

        X = t[Variables]
        y = t["Defaut"]

        # Scaling
        X_scaled = self.Scaler.fit_transform(X)

        # Modèle logistiq
        self.Modele = LogisticRegression(max_iter=1000)
        self.Modele.fit(X_scaled, y)

        # Prob défaut
        t["PD_TTC"] = self.Modele.predict_proba(X_scaled)[:, 1]

        print("PD TTC calculée")

        Contexte["t"] = t
        Contexte["Modele_PD"] = self.Modele
        return Contexte