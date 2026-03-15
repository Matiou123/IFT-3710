import pandas as pd 
import matplotlib.pyplot as plt

pd_centered_file = "turaco_density_center_Pd.csv"
pt_centered_file = "turaco_density_center_Pt.csv"
test_file = "turaco_density_1.csv"
TYPES = ["Pt2", "Pt4", "Pd2", "Pd4"]

# Gets count for amount of crystals using listed types from a CSV file.
def get_compositions(file):
	compositions = list(pd.read_csv(file)["readable"].apply(lambda x : x.split(";")[2].strip()))
	return tuple(compositions.count(x) for x in TYPES)

# Shows horizontal bar plot of a distribution 
def plot_distribution(dists, names, colors):
	fig = plt.figure()
	fig.canvas.manager.set_window_title("Distribution of molecule composition based on density trained")

	ax = fig.add_subplot()
	ax.set_title("Distribution of molecule composition based on density trained")
	l = len(dists)

	for i in range(4):
		ax.barh(names, [dists[j][i] for j in range(l)], 0.8, 
			left = [sum(dists[j][:i]) for j in range(l)],
			color = colors[i],
			label = TYPES[i])

	ax.set_xlim(0, 1000)
	ax.legend()
	plt.show()
	return
	
test_a = get_compositions(test_file)
pd_centered = get_compositions(pd_centered_file)
pt_centered = get_compositions(pt_centered_file)

plot_distribution([test_a, pd_centered, pt_centered], 
				  ["Test", "Pd-trained", "Pt-trained"],
				  ["xkcd:blue", "xkcd:light blue", "xkcd:salmon", "xkcd:red"])

