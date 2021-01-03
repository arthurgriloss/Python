# This code is an exercise done at module 2 as part of the course (DA0101EN) Analyzing Data with Python by IBM.
# The intention of the module is to teach data wrangling and data feature by cleaning undesired data, normalizing data, and creating new features for futher analysis.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib as plt
from matplotlib import pyplot

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(url, names=headers)


df.replace('?', np.nan, inplace=True)
missing_data = df.isnull()
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

avg_norm_loss = df['normalized-losses'].astype("float").mean(axis=0)
df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)
avg_bore = df['bore'].astype("float").mean(axis=0)
df['bore'].replace(np.nan, avg_bore, inplace=True)
avg_stroke = df['stroke'].astype("float").mean(axis=0)
df['stroke'].replace(np.nan, avg_stroke, inplace=True)
avg_horsepower = df['horsepower'].astype("float").mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peakrpm = df['peak-rpm'].astype("float").mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())
df['num-of-doors'].replace(np.nan, 'four', inplace=True)

df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.dtypes)
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print(df.dtypes)

df['city-L/100km'] = 235/df["city-mpg"]
df['highway-mpg'] = 235/df['highway-mpg']
df.rename(columns={'"highway-mpg"': '"highway-L/100km"'}, inplace=True)

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()
print(df[["length", "width", "height"]].head())

df["horsepower"] = df["horsepower"].astype("int", copy=True)
# pyplot.hist(df["horsepower"])
# pyplot.show()

bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
print(df[['horsepower', 'horsepower-binned']].head(20))
print(df['horsepower-binned'].value_counts())

# pyplot.bar(group_names, df['horsepower-binned'].value_counts())
# pyplot.show()

dummy_variable1 = pd.get_dummies(df['fuel-type'])
dummy_variable1.rename(columns={'gas': 'fuel-type-gas', 'diesel': 'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_variable1], axis=1)
df.drop('fuel-type', axis=1, inplace=True)

dummy_variable2 = pd.get_dummies(df['aspiration'])
dummy_variable2.rename(columns={'std': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
df = pd.concat([df, dummy_variable2], axis=1)
df.drop('aspiration', axis=1, inplace=True)

df.to_csv('clean_df.csv')

print(df.tail(20))
