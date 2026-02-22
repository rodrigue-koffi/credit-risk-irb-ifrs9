class Etape02_Gouvernance:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        # traitement doublons
        t = t.drop_duplicates()

        # Suppression lineNa
        t = t.dropna(how="all")

        print("Gouvernance OK - shape:", t.shape)

        Contexte["t"] = t
        return Contexte