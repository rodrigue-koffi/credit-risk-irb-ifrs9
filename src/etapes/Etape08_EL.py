class Etape08_EL:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        if {"PD_TTC", "LGD", "EAD"}.issubset(t.columns):
            t["EL"] = t["PD_TTC"] * t["LGD"] * t["EAD"]
            print("Expected Loss OK")
            print("EL moyenne:", t["EL"].mean())
        else:
            print("EL KO")

        Contexte["t"] = t
        return Contexte