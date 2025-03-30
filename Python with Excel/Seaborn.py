import seaborn as sns
penguins=sns.load_dataset('penguins')

print(penguins.head())

print(penguins.tail(20))

print(penguins.shape)

print(penguins.info())

print(penguins.describe()) # it will give results for columns that are quantitative

print(penguins.describe(include="all"))