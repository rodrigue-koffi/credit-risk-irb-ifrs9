class Etape07_EAD:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        # Cas 1 : si montant crédit existe
        if "Credit amount" in t.columns:
            t["EAD"] = t["Credit amount"]

        # Cas 2 : fallback générique
        else:
            t["EAD"] = 10000  # exposition moyenne fictive

        print("EAD calculée")

        Contexte["t"] = t
        return Contexte