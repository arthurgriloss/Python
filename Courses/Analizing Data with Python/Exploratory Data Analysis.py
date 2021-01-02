# This code is an exercise done at module 3 as part of the course (DA0101EN) Analyzing Data with Python by IBM.
# The intention of the module is to teach how to analyse data by plot visualization, correlation and ANOVA.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(url)

print(df.corr())
print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

# sns.regplot(x='engine-size', y='price', data=df)
print(df[['engine-size', 'price']].corr())
# sns.regplot(x='highway-mpg', y='price', data=df)
print(df[['highway-mpg', 'price']].corr())
# sns.regplot(x='peak-rpm', y='price', data=df)
print(df[['peak-rpm', 'price']].corr())
# sns.regplot(x='stroke', y='price', data=df)
print(df[['stroke', 'price']].corr())
# fig = plt.figure(figsize=(5, 15))
# fig.add_subplot(3, 1, 1)
# sns.boxplot(x='body-style', y='price', data=df)
# fig.add_subplot(3, 1, 2)
# sns.boxplot(x='engine-location', y='price', data=df)
# fig.add_subplot(3, 1, 3)
# sns.boxplot(x='drive-wheels', y='price', data=df)

print(df.describe())
print(df.describe(include=['object']))
drive_wheels_count = df['drive-wheels'].value_counts().to_frame()
drive_wheels_count.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_count.index.name = 'drive-wheels'
print(drive_wheels_count)
engine_loc_count = df['engine-location'].value_counts().to_frame()
engine_loc_count.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_count.index.name = 'engine-location'
print(engine_loc_count)

print(df['drive-wheels'].unique())
df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
print(df_group_one)
df_gptest = df[['drive-wheels', 'body-style', 'price']]
df_gptest = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
print(df_gptest)
group_pivoted = df_gptest.pivot(index='drive-wheels', columns='body-style').fillna(0)
print(group_pivoted)
df_gptest2 = df[['body-style', 'price']]
df_gptest2 = df_gptest2.groupby(['body-style'], as_index=False).mean()
print(df_gptest2)

# plt.pcolor(group_pivoted, cmap='RdBu')
# plt.colorbar()

# fig, ax = plt.subplots()
# im = ax.pcolor(group_pivoted, cmap='RdBu')
# row_labels = group_pivoted.columns.levels[1]
# col_labels = group_pivoted.index
# ax.set_xticks(np.arange(group_pivoted.shape[1]) + 0.5, minor=False)
# ax.set_yticks(np.arange(group_pivoted.shape[0]) + 0.5, minor=False)
# ax.set_xticklabels(row_labels, minor=False)
# ax.set_yticklabels(col_labels, minor=False)
# plt.xticks(rotation=90)
# plt.colorbar(im)

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats. pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

grouped_test2 = df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val)

plt.show()
# print(df.head())
