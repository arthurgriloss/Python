# This code is an exercise done at module 1 as part of the course (DA0101EN) Analyzing Data with Python by IBM.
# The intention of the module is to teach how to import, preview and format data.

import pandas as pd
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
df = pd.read_csv(url, header=None)

print(df.head())
print(df.tail(10))

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
         "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
         "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
         "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
print(df.columns)
print(df.head(10))

df_edit = df.replace("?", np.NaN)
df_non_NaN = df.dropna(subset=['price'], axis=0)

print(df_non_NaN.dtypes)
print(df_non_NaN.describe())
print(df_non_NaN.describe(include='all'))
print(df_non_NaN.info())

df.to_csv('automobile.csv', index=False)
