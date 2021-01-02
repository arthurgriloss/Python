# This code is an exercise done at module 2 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to solve a Non-Linear Regression problem, in this case a sigmoid funtion model.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/china_gdp.csv'
df = pd.read_csv(url)
plt.figure(figsize=(8, 5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.scatter(x=x_data, y=y_data, color='red')


def sigmoid(x, Beta_1, Beta_2):
    return 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))


x_data = x_data/max(x_data)
y_data = y_data/max(y_data)

msk = np.random.rand(len(df)) < 0.8
train_x = x_data[msk]
test_x = x_data[~msk]
train_y = y_data[msk]
test_y = y_data[~msk]
popt, pcov = curve_fit(sigmoid, train_x, train_y)
test_y_predict = sigmoid(test_x, *popt)
print(f"Mean Absolute Error: {np.mean(np.absolute(test_y_predict - test_y)):.2f}")
print(f"Residual sum of squares: {np.mean((test_y_predict - test_y)**2):.2f}")
print(f"R2-score: {r2_score(test_y, test_y_predict):.2f}")

# plt.show()
