import torch, pandas as pd, numpy as np, re, os

from gflownet.utils.crystals.constants import ELEMENT_NAMES, ATOMIC_MASS
DENSITY_CONVERSION = 10 / 6.022  # constant to convert g/molA3 to g/cm3
ELEMENT_NUMBERS = {v: k for k, v in ELEMENT_NAMES.items()}

def masse_totale(formule: str) -> float:
    """ Calcule la masse totale de `formule`et la renvoit """
    
    masse_totale = 0
    
    # ([A-Z][a-z]*) : Une majuscule suivie de 0 ou plusieurs minuscules
    # (\d*)         : Zéro ou plusieurs chiffres
    pattern = r"([A-Z][a-z]*)(\d*)"

    matches = re.findall(pattern, formule)

    for atome, compte in matches:
        atome_int = ELEMENT_NUMBERS[atome]
        masse_atome = ATOMIC_MASS[atome_int]
        if not compte:
            compte = 1 # re.findall renvoit une chaîne vide pour les atomes uniques
        masse_totale += masse_atome * int(compte)

    return masse_totale

def calcule_density_df(chemin_in:str, chemin_out:str) -> None:
    """Rajoute la colonne de densité dans le DataFrame provenant de `chemin_in` et l'enregistre dans `chemin_out` """

    df = pd.read_csv(chemin_in)

    # On ajoute une nouvelle colonne qui est initialiment la masse_totale de la formule
    df['density'] = df['Formulae'].apply(masse_totale) 


    # Calcule de densité provenant de gflownet/proxy/crystals/density.py
    for i in range(df.shape[0]):
        row = df.iloc[i]
        a, b, c, cos_alpha, cos_beta, cos_gamma = (
            row['a'],
            row['b'],
            row['c'],
            torch.cos(torch.deg2rad(torch.tensor(row['alpha']))),
            torch.cos(torch.deg2rad(torch.tensor(row['beta']))),
            torch.cos(torch.deg2rad(torch.tensor(row['gamma']))),
        )
        volume = (a * b * c) * torch.sqrt(
            1
            - (cos_alpha.pow(2) + cos_beta.pow(2) + cos_gamma.pow(2))
            + (2 * cos_alpha * cos_beta * cos_gamma)
        ).item()

        df.at[i, 'density'] = (df.at[i, 'density'] / volume) * DENSITY_CONVERSION


    dossier = os.path.dirname(chemin_out)
    if not os.path.exists(dossier):
        os.makedirs(dossier, exist_ok=True)

    df.columns.values[0] = '' 
    df.to_csv(chemin_out, index=False)

chemin_in = "data_/eform/train.csv"
chemin_out = "data_/eform_density/train.csv"

calcule_density_df(chemin_in, chemin_out)