import numpy as np

class Etape12_MonteCarlo:
    def Executer(self, Contexte):
        t = Contexte["t"]

        print("\n===== MONTE CARLO =====")

        if {"PD_TTC", "LGD", "EAD"}.issubset(t.columns):

            n_sims = 2000
            pertes = []

            PD = t["PD_TTC"].values
            LGD = t["LGD"].values
            EAD = t["EAD"].values

            for _ in range(n_sims):
                defaults = np.random.binomial(1, PD)
                perte = np.sum(defaults * LGD * EAD)
                pertes.append(perte)

            pertes = np.array(pertes)

            Contexte["MonteCarlo"] = {
                "Perte_moyenne": pertes.mean(),
                "VaR_99": np.percentile(pertes, 99),
            }

            print("Monte Carlo terminé")

        else:
            print("Monte Carlo impossible - données manquantes")

        return Contexte