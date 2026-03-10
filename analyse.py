import pandas as pd, matplotlib.pyplot as plt, numpy, re
from gflownet.utils.crystals.constants import ATOMIC_MASS

chemin = "logs/crystalgfn/local/2026-03-06_18-29-54_865552/eval/samples/gfn_samples.csv"


DENSITY_CONVERSION = 10 / 6.022  # constant to convert g/molA3 to g/cm3

def density(total_mass, lattice):
    
    a, b, c, cos_alpha, cos_beta, cos_gamma = (
        lattice[0],
        lattice[1],
        lattice[2],
        numpy.cos(numpy.deg2rad(lattice[3])),
        numpy.cos(numpy.deg2rad(lattice[4])),
        numpy.cos(numpy.deg2rad(lattice[5])),
    )
    
    volume = (a * b * c) * numpy.sqrt(
        1
        - (cos_alpha**2 + cos_beta**2 + cos_gamma**2)
        + (2 * cos_alpha * cos_beta * cos_gamma)
    )

    return (total_mass / volume) * DENSITY_CONVERSION

element_to_mass = {"Pt" : ATOMIC_MASS[78], "Pd": ATOMIC_MASS[46]}

with open(chemin, "rb") as file:
    a = pd.read_csv(file)
    b = list(a["readable"])
    
    densité_éléments = {"Pt2": [], "Pt4" : [], "Pd2" : [], "Pd4" : []}
    
    for i in range(5):
        regex_nombre = r"(\d+\.\d+)"
        
        lattices = list(map(float, re.findall(regex_nombre, b[i])))
        
        regex_elements = r"([A-Z][a-z]?)(\d+)"
        elements = re.findall(regex_elements, b[i])
        
        molecules = elements[0][0]+elements[0][1]

        total_mass = element_to_mass[elements[0][0]] * int(elements[0][1])
        
        densité_éléments[molecules].append(density(total_mass, lattices))

labels = list(densité_éléments.keys())
values = list(densité_éléments.values())

# Imprime les moyennes pour vérifier le graphique
#print(list(map(lambda x : sum(densité_éléments[x])/len(densité_éléments[x]), labels  )))

plt.boxplot(values, label=labels)
plt.xticks([e for e in range(1, len(labels) + 1)], labels)
plt.ylabel("Densité")
plt.title("Distribution des différentes densités selon les molécules")
plt.savefig("densités_turacos_corners.pdf")