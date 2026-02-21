import numpy as np

class Etape06_LGD:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        # Cas 1 : si recovery existe
        if "Recovery" in t.columns:
            t["LGD"] = 1 - t["Recovery"]

        else:
            # Valeur standard retail (Bâle approx)
            t["LGD"] = 0.45

        # Bornage
        t["LGD"] = np.clip(t["LGD"], 0.05, 0.95)

        print("LGD calculée")

        Contexte["t"] = t
        return Contexte