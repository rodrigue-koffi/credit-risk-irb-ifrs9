class Orchestrateur:
    def __init__(self, ListeEtapes):
        self.ListeEtapes = ListeEtapes

    def Executer(self, Contexte: dict):
        for Etape in self.ListeEtapes:
            Contexte = Etape.Executer(Contexte)
        return Contexte