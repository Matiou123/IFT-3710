import pandas as pd

d1 = pd.read_csv("crystals/gull.csv")
d2 = pd.read_csv("projet/train.csv")

d2.drop(columns= "Eform", inplace=True)

d = d1.combine_first(d2)
d.rename(columns={d.columns[0] : " "}, inplace=True)
d.to_csv("projet/données_train.csv", index=False)
