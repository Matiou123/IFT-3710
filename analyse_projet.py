import pandas as pd, matplotlib.pyplot as plt, re

# Chemin csv eval
chemin = "logs/crystalgfn/local/2026-04-01_14-31-31_453580/eval/samples/gfn_samples.csv"
regex = r"([A-Z][a-z]*)(\d*)" # Les atomes
d = dict() # Fréquence des atomes dans l'échantillon
d2 = dict() # Nombre total d'atomes dans l'échantillion
df = pd.read_csv(chemin)


for i in range(df.shape[0]):
    élément = df['readable'][i].split(';')[2]
    #atomes = re.findall(regex, élément)
    nombre_atomes = re.findall(regex, élément)
    
    for atome, nombre in nombre_atomes:
        n = int(nombre) if nombre != "" else 1
        
        if atome not in d:
            d[atome] = 1
            d2[atome] = n
        else:
            d[atome] += 1
            d2[atome] += n

def plot1(chemin_sauv:str):
    plt.figure()
    pd.Series(d).plot(kind='barh')
    plt.title("La fréquence des atomes dans les éléments générés")
    #plt.show()
    plt.savefig(chemin_sauv)


def plot2(chemin_sauv:str):
    plt.figure()
    pd.Series(d2).plot(kind='barh')
    plt.title("Le nombre total des atomes qui ont été générés")
    #plt.show()
    plt.savefig(chemin_sauv)


DENSITY_CONVERSION = 10 / 6.022  # constant to convert g/molA3 to g/cm3
from gflownet.utils.crystals.constants import ATOMIC_MASS, ELEMENT_NAMES
ELEMENT_NAMES_TO_NUMBER = {v : k for k, v in ELEMENT_NAMES.items()}
import numpy as np


regex_lattices = r'\d+\.\d+'
regex_elements = r"([A-Z][a-z]?)(\d+)"
densité = []

for i in range(df.shape[0]):
    t = df["readable"][i].split(';')

    lattices = t[5]
    a, b, c, cos_alpha, cos_beta, cos_gamma = tuple(map(float,(re.findall(regex_lattices, lattices))))
    cos_alpha, cos_beta, cos_gamma = np.cos(np.deg2rad(cos_alpha)), np.cos(np.deg2rad(cos_beta)),  np.cos(np.deg2rad(cos_gamma))
    
    élément = df['readable'][i].split(';')[2]
    atomes = re.findall(regex_elements, élément)
    masse_total = 0
    for atom in atomes:
        masse_atom = ATOMIC_MASS[ELEMENT_NAMES_TO_NUMBER[atom[0]]]
        masse_total += masse_atom * float(atom[1])
        
    arg_racine = (1 
                - cos_alpha**2 - cos_beta**2 - cos_gamma**2 
                + 2 * cos_alpha * cos_beta * cos_gamma)


    volume = (a * b * c) * np.sqrt(arg_racine)


    dens = (masse_total / volume) * DENSITY_CONVERSION

    densité.append(dens)
    
import seaborn as sb, pandas as pd

array_densité = np.array(densité)
print("Stat densité")
print(f"Moyenne : {array_densité.mean()} Écart-type :  {array_densité.std()}")


plot1("Distribution des éléments centre=100, beta=0.01269.pdf")
plot2("Nombre total des atomes centre=100, beta=0.01269.pdf")

plt.figure()
sb.histplot(pd.DataFrame(densité), kde=True)
plt.title("Distribution de la densité centre: 100, beta: 0.01269")
plt.savefig("Distribution densité centre: 100, beta: 0.01269.pdf")
