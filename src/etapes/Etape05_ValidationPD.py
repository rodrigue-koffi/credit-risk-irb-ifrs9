import numpy as np
from sklearn.metrics import roc_auc_score

class Etape05_ValidationPD:
    def Executer(self, Contexte):
        t = Contexte["t"]

        if "Defaut" not in t.columns or "PD_TTC" not in t.columns:
            print("Validation PD ignorée")
            return Contexte

        y = t["Defaut"]
        pd = t["PD_TTC"]

        # AUC
        auc = roc_auc_score(y, pd)
        gini = 2 * auc - 1

        # KS
        df = t.sort_values("PD_TTC")
        cum_def = np.cumsum(df["Defaut"]) / df["Defaut"].sum()
        cum_nondef = np.cumsum(1 - df["Defaut"]) / (1 - df["Defaut"]).sum()
        ks = np.max(np.abs(cum_def - cum_nondef))

        print(f"AUC: {auc:.3f} | Gini: {gini:.3f} | KS: {ks:.3f}")

        Contexte["Metrics_PD"] = {
            "AUC": auc,
            "Gini": gini,
            "KS": ks
        }

        return Contexte