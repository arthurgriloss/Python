# This code is an exercise done at module 2 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to solve a Simple Linear Regression problem and introduce the traning/test split method to evaluate the model

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv'
df = pd.read_csv(url)
print(df.describe())
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
viz = cdf[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
# viz.hist()
# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='blue')

msk = np.random.rand(len(cdf)) < 0.8
train = cdf[msk]
test = cdf[~msk]
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_predict = regr.predict(test_x)
print(f"Mean absolute error: {np.mean(np.absolute(test_y_predict - test_y)) :.2f}")
print(f"Residual sum of squares (MSE): { np.mean((test_y_predict - test_y)**2 ):.2f}")
print(f"R2-score: {r2_score(test_y, test_y_predict):.2f}")


plt.show()
# print(df.head())
