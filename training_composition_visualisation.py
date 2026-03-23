import pandas as pd

path_train = "train.csv"
path_table = "Periodic Table of Elements.csv"

# Converts name of a molecule to an array with its elements used
def convert_to_elements_used(name):
	if name == "":
		return []
	i = 0

	while (not name[i].isnumeric()):
		i += 1

	first = name[:i]

	while (i < len(name) and name[i].isnumeric()):
		i += 1

	return [first] + convert_to_elements_used(name[i:])

formulae = pd.read_csv(path_train)["Formulae"]
print(formulae)
elem_frequencies = {}

print("start")
for formula in formulae:
	for elem in convert_to_elements_used(formula):
		if elem in elem_frequencies.keys():
			elem_frequencies[elem] += 1
		else:
			elem_frequencies[elem] = 1

elem_frequencies = list(elem_frequencies.items())
elem_frequencies.sort(reverse = True, key = lambda x : x[1])
print(elem_frequencies)


"""
numbers_atom = pd.read_csv(path_table)
print(numbers_atom)


print(numbers_atom[numbers_atom["Symbol"] == "N"]["AtomicNumber"])
clean_freq = map(lambda x : ("Symbol : " + x[0], "Atomic number : " + numbers_atom[numbers_atom["Symbol"] == x[0]]["AtomicNumber"]), elem_frequencies)
print(list(clean_freq))
"""