import pandas as pd, matplotlib.pyplot as plt, re

# Chemin csv eval
chemin = "logs/crystalgfn/local/2026-04-13_00-36-55_666578/eval/samples/gfn_samples.csv"
titre = "testing.pdf" # Sur-titre du graphique
regex = r"([A-Z][a-z]*)(\d*)" # Le premier groupe sont les atomes et le second sont leur nombre total
fréquences = dict() # Fréquence des atomes dans l'échantillon 
nombre_total_atomes = dict() # Nombre total d'atomes dans l'échantillion
df = pd.read_csv(chemin)


# Calcule les atomes dans les cristaux, leur fréquence dans les et leur nombre total
for i in range(df.shape[0]):
    élément = df['readable'][i].split(';')[2]
    nombre_atomes = re.findall(regex, élément)
    
    for atome, nombre in nombre_atomes:
        n = int(nombre) if nombre != "" else 1
        
        if atome not in fréquences:
            fréquences[atome] = 1
            nombre_total_atomes[atome] = n 
        else:
            fréquences[atome] += 1
            nombre_total_atomes[atome] += n

def plot1(chemin_sauv:str):
    plt.figure()
    pd.Series(fréquences).plot(kind='barh')
    plt.title("La fréquence des atomes dans les éléments générés")
    #plt.show()
    plt.savefig(chemin_sauv)


def plot2(chemin_sauv:str):
    plt.figure()
    pd.Series(nombre_total_atomes).plot(kind='barh')
    plt.title("Le nombre total des atomes qui ont été générés")
    #plt.show()
    plt.savefig(chemin_sauv)


densité = df['energies'].dropna().astype(float)

import numpy as np
 
array_densité = np.array(densité)
print("Stat densité")
print(f"Moyenne : {array_densité.mean()} Écart-type :  {array_densité.std()}")

    
import seaborn as sb

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plt.suptitle("Uniforme")

pd.Series(fréquences).plot(kind='barh', ax=axes[0])
axes[0].set_title("La fréquence des atomes dans les éléments générés")

pd.Series(nombre_total_atomes).plot(kind='barh', ax=axes[1], color= "blue")
axes[1].set_title("Le nombre total des atomes qui ont été générés")

sb.histplot(pd.Series(densité),color="green" ,kde=True, bins=30, ax=axes[2], legend=False)
axes[2].set_xlabel("Densité")
axes[2].set_title("Distribution de la densité")

plt.tight_layout()
plt.savefig(titre)
