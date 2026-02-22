import numpy as np
from scipy.stats import norm

class Etape10_CapitalIRB:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        if {"PD_TTC", "LGD", "EAD"}.issubset(t.columns):

            PD = t["PD_TTC"].clip(1e-6, 1 - 1e-6)
            LGD = t["LGD"]

            # Correlation simple Bale
            R = 0.12 * (1 - np.exp(-50 * PD)) / (1 - np.exp(-50)) + \
                0.24 * (1 - (1 - np.exp(-50 * PD)) / (1 - np.exp(-50)))

            # Capital unitaire
            K = LGD * norm.cdf(
                (norm.ppf(PD) + np.sqrt(R) * norm.ppf(0.999)) / np.sqrt(1 - R)
            ) - PD * LGD

            t["Capital_IRB"] = K * t["EAD"]

            print("Capital IRB OK")

        else:
            print("Capital IRB KO")

        Contexte["t"] = t
        return Contexte