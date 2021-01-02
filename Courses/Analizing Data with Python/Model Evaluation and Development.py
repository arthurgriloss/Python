# This code is an exercise done at module 5 as part of the course (DA0101EN) Analyzing Data with Python by IBM.
# The intention of the module is to teach good practices at data analysis as k-fold cross validation and Ridge Regression
# by passing multiple penalty terms λ and select the one that best fits the model.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import pandas as pd
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns


def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color='r', label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color='b', label=BlueName)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of cars')

    plt.show()
    plt.close()


def PollyPlot(xtrain, xtest, ytrain, ytest, lr, poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    xmax = max([xtrain.values.max(), xtest.values.max()])
    xmin = min([xtrain.values.min(), xtest.values.min()])
    x = np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, ytrain, 'ro', label='Training Data')
    plt.plot(xtest, ytest, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predict Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


def f(order, test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_data, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train)
    x_test_pr = pr.fit_transform(x_test)
    poly = LinearRegression()
    poly.fit(x_train_pr, y_train)
    PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train, y_test, poly, pr)


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
raw_df = pd.read_csv(url)

numeric_df = raw_df._get_numeric_data()
x_data = numeric_df.drop('price', axis=1)
y_data = numeric_df['price']

xtrain, xtest, ytrain, ytest = train_test_split(x_data, y_data, test_size=0.1, random_state=1)
print("number of training samples: ", xtrain.shape[0])
print("number of test samples: ", xtest.shape[0]) 

lm = LinearRegression()
lm.fit(xtrain[['horsepower']], ytrain)
print("Train score: ", lm.score(xtrain[['horsepower']], ytrain))
print("Test score: ", lm.score(xtest[['horsepower']], ytest))

x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x_data, y_data, test_size=0.1, random_state=0)
lm.fit(x_train_1[['horsepower']], y_train_1)
print("Test score: ", lm.score(x_test_1[['horsepower']], y_test_1))

Rcross = cross_val_score(lm, x_data[['horsepower']], y_data, cv=4)
y_hat = cross_val_predict(lm, x_data[['horsepower']], y_data, cv=4)
print(f"The mean of the folds is {Rcross.mean():.2f} and the standard deviation is {Rcross.std():.2f}")

lm.fit(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], ytrain)
y_hat_train = lm.predict(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
y_hat_test = lm.predict(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])

Title = 'Distribution  Plot of  Predicted Value Using Training Data vs Training Data Distribution'
# DistributionPlot(ytrain, y_hat_train, "Actual Values (Train)", "Predicted Values (Train)", Title)
# DistributionPlot(ytest, y_hat_test, "Actual Values (Train)", "Predicted Values (Train)", Title)

xtrain, xtest, ytrain, ytest = train_test_split(x_data, y_data, test_size=0.45, random_state=0)
pf5 = PolynomialFeatures(degree=5)
xtrain_pf5 = pf5.fit_transform(xtrain[['horsepower']])
xtest_pf5 = pf5.fit_transform(xtest[['horsepower']])
poly = LinearRegression()
poly.fit(xtrain_pf5, ytrain)
y_hat = poly.predict(xtest_pf5)
# PollyPlot(xtrain[['horsepower']], xtest[['horsepower']], ytrain, ytest, poly, pf5)
print("Train score: ", poly.score(xtrain_pf5, ytrain))
print("Test score: ", poly.score( xtest_pf5, ytest))

Rsqu_test = []
order = [1, 2, 3, 4]
for n in order:
    pr = PolynomialFeatures(degree=n)
    xtrain_pr = pr.fit_transform(xtrain[['horsepower']])
    xtest_pr = pr.fit_transform(xtest[['horsepower']])
    poly.fit(xtrain_pr, ytrain)
    Rsqu_test.append(poly.score(xtest_pr, ytest))
# plt.plot(order, Rsqu_test)
# plt.xlabel('Order')
# plt.ylabel('R2-score')
# plt.text(3, Rsqu_test[2], 'Maximum R2')
interact(f, order=(0, 6, 1), test_data=(0.05, 0.95, 0.05))

pr1 = PolynomialFeatures(degree=2)
x_train_pr1 = pr1.fit_transform(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
x_test_pr1 = pr1.fit_transform(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
print(x_train_pr1.shape)
print(x_test_pr1.shape)
poly1 = LinearRegression()
poly1.fit(x_train_pr1, ytrain)
Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
y_hat_pr1 = poly1.predict(x_test_pr1)
# DistributionPlot(ytest, y_hat_pr1, "Actual Values (Test)","Predicted Values (Test)",Title)

pr2 = PolynomialFeatures(degree=2)
x_train_pr2 = pr2.fit_transform(xtrain[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr2 = pr2.fit_transform(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
Rsqu_test = []
Rsqu_train = []
Alpha = 10*np.array(range(0, 1000))
for alpha in Alpha:
    RideModel = Ridge(alpha=alpha)
    RideModel.fit(x_train_pr2, ytrain)
    Rsqu_train.append(RideModel.score(x_train_pr2, ytrain))
    Rsqu_test.append(RideModel.score(x_test_pr2, ytest))
# plt.figure(figsize=(12, 10))
# plt.plot(Alpha, Rsqu_train, label='Training Data')
# plt.plot(Alpha, Rsqu_test, 'r', label='Test Data')
# plt.xlabel('Aplha')
# plt.ylabel('R2-score')
# plt.legend()

parameters = [{'alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]}]
RR = Ridge()
Grid1 = GridSearchCV(RR, parameters, cv=4)
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)
BestRR = Grid1.best_estimator_
print("The best R2-score is: ", BestRR.score(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], ytest))

parameters2 = [{'alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000], 'normalize': [True, False]}]
Grid2 = GridSearchCV(RR, parameters2, cv=4)
Grid2.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)
BestRR = Grid2.best_estimator_
print("The best estimator is: ", BestRR)
print("The best R2-score is: ", BestRR.score(xtest[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], ytest))

plt.show()
