import sys
import pandas as pd

# To compute mean and standard deviation of a distribution in csv file (with energies)

path = sys.argv[1]
energies = pd.read_csv(path)["energies"]
print(energies)
print("mean :", sum(energies) / len(energies))
print("standard deviation :", energies.std())