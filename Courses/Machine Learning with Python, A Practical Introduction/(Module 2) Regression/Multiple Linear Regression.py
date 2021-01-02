# This code is an exercise done at module 2 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the excercise is to teach how to solve a Multiple Linear Regression problem.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv'
df = pd.read_csv(url)
new_df = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

msk = np.random.rand(len(df)) < 0.8
train = new_df[msk]
test = new_df[~msk]

regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
print('Coefficients: ', regr.coef_)
test_x = np.asanyarray(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_prediction = regr.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
print(f"Residual sum of squares: {np.mean((test_y_prediction - test_y)**2) :.2f}")
print(f'Variance score: {regr.score(test_x, test_y) :.2f}')

train_x2 = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
regr.fit(train_x2, train_y)
print("Coefficients: ", regr.coef_)
test_x2 = np.asanyarray(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
test_y_prediction2 = regr.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
print(f"Residual sum of squares: {np.mean((test_y_prediction2 - test_y)**2) :.2f}")
print(f"Variance score: {regr.score(test_x2, test_y) :.2f}")

# print(df.head())
