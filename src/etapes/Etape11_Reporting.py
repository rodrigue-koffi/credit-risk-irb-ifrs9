class Etape11_Reporting:
    def Executer(self, Contexte):
        t = Contexte["t"]

        print("\n===== RAPPORT FINAL =====")

        if "PD_TTC" in t.columns:
            print(f"PD moyenne : {t['PD_TTC'].mean():.4f}")

        if "EL" in t.columns:
            print(f"Expected Loss moyenne : {t['EL'].mean():.2f}")

        if "ECL" in t.columns:
            print(f"ECL IFRS9 moyenne : {t['ECL'].mean():.2f}")

        if "Capital_IRB" in t.columns:
            print(f"Capital IRB moyen : {t['Capital_IRB'].mean():.2f}")

        if "Metrics_PD" in Contexte:
            gini = Contexte["Metrics_PD"]["Gini"]
            print(f"Gini modèle PD : {gini:.3f}")

        print("=========================\n")

        return Contexte