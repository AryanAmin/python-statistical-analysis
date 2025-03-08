import pandas as pd
import numpy as np

fileName = "load.csv"
filePath = f"data/{fileName}"

# manual data load in python
cols = None
data = []
with open(filePath) as f:
    for line in f.readlines():
        vals = line.replace("\n", "").split(",")

        if cols is None:
            cols = vals
        else:
            data.append([float(x) for x in vals])

# converting to pandas dataframe
d0 = pd.DataFrame(data, columns=cols)
# print(d0.dtypes)
# print(d0.head())


# Using numpy load text to load same data
# skiprows = 1 skip the first row because it is header ('string')
# delimiter is "," in our data file
d1 = np.loadtxt(filePath, skiprows=1, delimiter=",")
# print(d1.dtype)
# print(d1[:5, :])

d2 = np.genfromtxt(filePath, delimiter=",", names=True, dtype=None)
# print(d2.dtype)
# print(d2[:5])

d3 = pd.read_csv(filePath)
print(d3.dtypes)
print(d3.head())
