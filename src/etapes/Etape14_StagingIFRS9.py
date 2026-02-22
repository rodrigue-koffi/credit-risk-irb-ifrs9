class Etape14_StagingIFRS9:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        print("\n IFRS9 STAGING ")

        if "Defaut" in t.columns:

            # PD de référence
            pd_ref = t["PD_PIT"] if "PD_PIT" in t.columns else t["PD_TTC"]

            t["Stage_IFRS9"] = 1

            # Stage 2 : degradation du risque
            t.loc[pd_ref > 0.10, "Stage_IFRS9"] = 2

            # Stage 3 : default observé
            t.loc[t["Defaut"] == 1, "Stage_IFRS9"] = 3

            print("Staging IFRS9")
            print(t["Stage_IFRS9"].value_counts().sort_index())

        else:
            print("Staging KO")

        Contexte["t"] = t
        return Contexte