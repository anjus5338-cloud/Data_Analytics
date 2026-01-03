import seaborn as sns 
import pandas as pd
import numpy as np

print(sns.get_dataset_names())

penguins = sns.load_dataset('penguins')
print(penguins.head())
x = penguins["species"].value_counts()
print(x)

a = sns.scatterplot(data = penguins, x = "flipper_length_mm", y = "body_mass_g")
print(a)