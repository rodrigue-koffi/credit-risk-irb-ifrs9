class Etape15_RWA:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        print("\n RWA CALCULATION ")

        if "Capital_IRB" in t.columns:
            t["RWA"] = t["Capital_IRB"] / 0.08
            print("RWA calculés")
            print("RWA moyen:", round(t["RWA"].mean(), 2))
        else:
            print("RWA KO")

        Contexte["t"] = t
        return Contexte