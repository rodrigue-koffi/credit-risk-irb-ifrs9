import numpy as np

class Etape13_ReverseStress:
    def Executer(self, Contexte):
        t = Contexte["t"]

        print("\n===== REVERSE STRESS TEST =====")

        if {"LGD", "EAD", "Capital_IRB"}.issubset(t.columns):

            capital_total = t["Capital_IRB"].sum()
            seuil_rupture = capital_total * 1.5  # buffer stress

            pd_scenarios = np.linspace(0.05, 0.6, 30)

            rupture = None

            for pd_stress in pd_scenarios:
                pertes = np.sum(pd_stress * t["LGD"] * t["EAD"])
                if pertes > seuil_rupture:
                    rupture = pd_stress
                    break

            if rupture:
                print(f"Point de rupture estimé : PD moyenne ≈ {rupture:.2f}")
            else:
                print("Aucun point de rupture trouvé dans le range testé")

        else:
            print("Reverse stress impossible - données manquantes")

        print("================================\n")
        return Contexte