# This code is an exercise done at module 4 as part of the course (DA0101EN) Analyzing Data with Python by IBM.
# The intention of the module is to teach how develop a model pipeline for a multi-variable linear regression using scaling, polynomial fit
# and regression to predict the price of a car given multiple features and compare with the price predicted by simple linear regression.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(url)

lm = LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
y_predicted = lm.predict(X)
print("Coefficient: ", lm.coef_)
print("Intercept: ", lm.intercept_)

lm1 = LinearRegression()
lm1.fit(df[['engine-size']], df['price'])
price = lm1.intercept_ + lm1.coef_ * df[['engine-size']]
# print(price)

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, Y)
Z = np.asanyarray(Z)
price = lm.intercept_ + np.matmul(Z, lm.coef_.T)
# print(price)

# fig = plt.figure(figsize=(12, 5))
# fig.add_subplot(1, 2, 1)
# sns.regplot(x='highway-mpg', y='price', data=df)
# fig.add_subplot(1, 2, 2)
# sns.regplot(x='peak-rpm', y='price', data=df)

#fig = plt.figure(figsize=(12, 10))
# sns.residplot(df['highway-mpg'], df['price'])

# ax1 = sns.distplot(df['price'], hist=False, color='r', label="Actual Value")
# sns.distplot(price, hist=False, color='b', label="Fitted Values", ax=ax1)


def PlotPolly(model, independent_variable, dependent_variable):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')


x = df['highway-mpg']
y = df['price']
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
# PlotPolly(p, x, y)

f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
# PlotPolly(p1, x, y)

Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(Z, y)
y_predict = pipe.predict(Z)

X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
Y_predict = lm.predict(X)
print("R2-score: ", lm.score(X, Y))
print("MSE: ", mean_squared_error(Y, Y_predict))

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, Y)
Y_predict_multfit = lm.predict(Z)
print("R2-score: ", lm.score(Z, Y))
print("MSE: ", mean_squared_error(Y, Y_predict_multfit))

print('The R-square value is: ', r2_score(Y, p(X)))
print('MSE: ', mean_squared_error(Y, p(X)))

plt.show()
