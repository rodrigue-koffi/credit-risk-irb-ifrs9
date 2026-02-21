class Etape02_Gouvernance:
    def Executer(self, Contexte):
        t = Contexte["t"].copy()

        # Suppression doublons
        t = t.drop_duplicates()

        # Suppression lignes vides
        t = t.dropna(how="all")

        print("Gouvernance OK - shape:", t.shape)

        Contexte["t"] = t
        return Contexte