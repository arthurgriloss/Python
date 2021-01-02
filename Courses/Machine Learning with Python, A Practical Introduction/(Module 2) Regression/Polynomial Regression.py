# This code is an exercise done at module 2 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to transform the features to polinomial features and solve a Linear Regression problem with polinomial features.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv'
df = pd.read_csv(url)
new_df = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

msk = np.random.rand(len(new_df)) < 0.8
train = new_df[msk]
test = new_df[~msk]


poly = PolynomialFeatures(degree=2)
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_x_poly = poly.fit_transform(train_x)
test_x = np.asanyarray(test[['ENGINESIZE']])
test_x_poly = poly.fit_transform(test_x)
train_y = np.asanyarray(train[['CO2EMISSIONS']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
regr.fit(train_x_poly, train_y)
print("Coefficients: ", regr.coef_)
print("Intercept: ", regr.intercept_)
test_y_predict = regr.predict(test_x_poly)
print(f"Mean absolut error: {np.mean(np.absolute(test_y_predict - test_y)) :.2f}")
print(f"Residual sum of squares: {np.mean((test_y_predict - test_y)**2) :.2f}")
print(f"R2-score: {r2_score(test_y_predict, test_y) :.2f}")

poly = PolynomialFeatures(degree=3)
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_x_poly = poly.fit_transform(train_x)
test_x = np.asanyarray(test[['ENGINESIZE']])
test_x_poly = poly.fit_transform(test_x)
train_y = np.asanyarray(train[['CO2EMISSIONS']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
regr.fit(train_x_poly, train_y)
print("Coeficients: ", regr.coef_)
print("Intercept: ", regr.intercept_)
test_y_predict = regr.predict(test_x_poly)
print(f"Mean Absolute Error: {np.mean(np.absolute(test_y_predict - test_y)):.2f}")
print(f'Residual sum of squares: {np.mean((test_y_predict - test_y)**2):.2f}')
print(f"R2-score: {r2_score(test_y_predict, test_y):.2f}")
