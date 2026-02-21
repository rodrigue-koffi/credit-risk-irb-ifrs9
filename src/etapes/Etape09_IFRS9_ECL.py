class Etape09_IFRS9_ECL:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        if {"PD_TTC", "LGD", "EAD"}.issubset(t.columns):

            # Approximation PD PIT
            t["PD_PIT"] = t["PD_TTC"] * 1.2  # proxy forward-looking

            # Bornage
            t["PD_PIT"] = t["PD_PIT"].clip(0, 1)

            # ECL
            t["ECL"] = t["PD_PIT"] * t["LGD"] * t["EAD"]

            print("IFRS9 ECL OK")
            print("ECL moyenne:", t["ECL"].mean())

        else:
            print("ECL non calculée - colonnes manquantes")

        Contexte["t"] = t
        return Contexte