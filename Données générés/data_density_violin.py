import pandas as pd
import seaborn as sb
import matplotlib as plt
import math

path = "turaco_density_projet_PT.csv"

densities = list(filter(lambda x : not math.isnan(x), pd.read_csv(path)["energies"]))
print(densities)

print(sum(densities) / len(densities))

"""
plot = sb.violinplot(densities)
plt.pyplot.show()
"""
