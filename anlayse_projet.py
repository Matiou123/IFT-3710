import pandas as pd, matplotlib.pyplot as plt, re

chemin = "logs/crystalgfn/local/2026-03-23_16-39-49_153932/eval/samples/turaco_density_projet_Pt.csv"
regex = r"([A-Z][a-z]*)" # Les atomes
regex2 = r"[A-Z][a-z]*([\d*]+)" # Le nombre après les atomes

d = dict() # Fréquence des atomes dans l'échantillon
d2 = dict() # Nombre total d'atomes dans l'échantillion
df = pd.read_csv(chemin)

for i in range(df.shape[0]):
    élément = df['readable'][i].split(';')[2]
    atomes = re.findall(regex, élément)
    nombre_atomes = re.findall(regex2, élément)

    for j, a in enumerate(atomes):
        if a not in d:
            d[a] = 1
            d2[a] = int(nombre_atomes[j])
        else:
            d[a] += 1
            d2[a] += int(nombre_atomes[j])

def plot1():
    pd.Series(d).plot(kind='barh')
    plt.title("La fréquence des atomes dans les éléments générés")
    plt.show()
    plt.savefig("Distribution des éléments.pdf")


def plot2():
    pd.Series(d2).plot(kind='barh')
    plt.title("Le nombre total des atomes qui ont été générés")
    plt.show()
    plt.savefig("Nombre total des atomes.pdf")