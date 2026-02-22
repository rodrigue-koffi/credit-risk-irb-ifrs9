import os
import pandas as pd

from src.main.Orchestrateur import Orchestrateur
from src.etapes.Etape01_Test import Etape01_Test
from src.etapes.Etape02_Gouvernance import Etape02_Gouvernance
from src.etapes.Etape03_Preprocessing import Etape03_Preprocessing
from src.etapes.Etape04_PD_TTC import Etape04_PD_TTC
from src.etapes.Etape05_ValidationPD import Etape05_ValidationPD
from src.etapes.Etape06_LGD import Etape06_LGD
from src.etapes.Etape07_EAD import Etape07_EAD
from src.etapes.Etape08_EL import Etape08_EL
from src.etapes.Etape09_IFRS9_ECL import Etape09_IFRS9_ECL
from src.etapes.Etape10_CapitalIRB import Etape10_CapitalIRB
from src.etapes.Etape11_Reporting import Etape11_Reporting
from src.etapes.Etape12_MonteCarlo import Etape12_MonteCarlo
from src.etapes.Etape13_ReverseStress import Etape13_ReverseStress
from src.etapes.Etape14_StagingIFRS9 import Etape14_StagingIFRS9
from src.etapes.Etape15_RWA import Etape15_RWA


#Load
def OpenFile(Path: str) -> pd.DataFrame:
    Extension = os.path.splitext(Path)[1].lower()

    if Extension in (".xlsx", ".xls"):
        return pd.read_excel(Path)
    elif Extension in (".csv", ".txt"):
        return pd.read_csv(Path, sep=None, engine="python")
    else:
        raise ValueError(f"Erreur: {Extension}")



def main():
    Chemin = "data/german_credit_data.xlsx"

    Contexte = {}

    if os.path.exists(Chemin):
        t = OpenFile(Chemin)
        Contexte["t"] = t
        print("Dataset chargé:", t.shape)
    else:
        print("Pas de dataset")
        return

    # Enchainement Pipeline
    Pipeline = Orchestrateur([
        Etape01_Test(),
        Etape02_Gouvernance(),
        Etape03_Preprocessing(),
        Etape04_PD_TTC(),
        Etape05_ValidationPD(),
        Etape06_LGD(),
        Etape07_EAD(),
        Etape08_EL(),
        Etape09_IFRS9_ECL(),
        Etape10_CapitalIRB(),

        # IFRS9 / Bâle
        Etape14_StagingIFRS9(),
        Etape15_RWA(),

        # Simu
        Etape12_MonteCarlo(),

        # Synthe
        Etape11_Reporting(),

        # Conclusion
        Etape13_ReverseStress(),
    ])

    # Exec.
    Pipeline.Executer(Contexte)


# Entry point
if __name__ == "__main__":
    main()