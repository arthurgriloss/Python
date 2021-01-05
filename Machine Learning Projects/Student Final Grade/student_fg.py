import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

math_df = pd.read_csv("student-mat.csv", sep=";")
port_df = pd.read_csv("student-por.csv", sep=";")

# Data description
print(math_df.head())
print(math_df.shape)
print(math_df.dtypes)
print(math_df.isnull().sum(), "\n")

print(port_df.head())
print(port_df.shape)
print(port_df.dtypes)
print(port_df.isnull().sum(), "\n")

# Append dataframes
math_df["Subject"] = "MATH"
port_df["Subject"] = "PORT"
df = pd.concat([math_df, port_df], axis=0)
df["GPA"] = (df["G1"].values + df["G2"].values + df["G3"].values) / 3
df.drop(["G1", "G2", "G3"], axis=1, inplace=True)
print(df, "\n")

# Transfor object variables into discrete variables
categorical_type = preprocessing.LabelEncoder()
for column in df.columns:
    if df[column].dtypes == "O":
        df[column] = pd.Categorical(df[column])
        category_list = df[column].unique()
        categorical_type.fit(category_list)
        df[column] = categorical_type.transform(df[column])
print(df.head(), "\n")

# Splitting data    
values = df.values
np.random.RandomState(3).shuffle(values)
X = values[:, :-1]
y = values[:, [-1]]
m = len(values)
xtrain = X[:int(0.6*m)]
ytrain = y[:int(0.6*m)]
xcrossv = X[int(0.6*m) : int(0.8*m)]
ycrossv = y[int(0.6*m) : int(0.8*m)]
xtest = X[int(0.8*m):]
ytest = y[int(0.8*m):]

# Checking for best polynomial degree
for i in range(1, 5):
    poly = preprocessing.PolynomialFeatures(degree=i)
    xtrain_p = poly.fit_transform(xtrain)
    xcrossv_p = poly.fit_transform(xcrossv)
    xtest_p = poly.fit_transform(xtest)
    parameters = [{'alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000], 'normalize': [True, False]}]
    rr = Ridge()
    grid = GridSearchCV(rr, parameters, cv=5).fit(xtrain_p, ytrain)
    bestRR = grid.best_estimator_
    print(f"For polynomial degree = {i}")
    print(f"The best estimator is: {bestRR}")
    print(f"The R2-score from the train set is: {bestRR.score(xtrain_p, ytrain)}")
    print(f"The R2-score from the cross validation is: {bestRR.score(xcrossv_p, ycrossv)}\n")

# Predict score with the best model
poly = preprocessing.PolynomialFeatures(degree=2)
xtrain_p = poly.fit_transform(xtrain)
xcrossv_p = poly.fit_transform(xcrossv)
xtest_p = poly.fit_transform(xtest)
ridge_model = Ridge(alpha=1, normalize=True).fit(xtrain_p, ytrain)
y_hat = ridge_model.predict(xtest_p)
print(f"The MAE is : {np.mean(np.abs(y_hat - ytest)):.2f}")
print(f"The MSE is: {np.mean((y_hat - ytest) ** 2):.2f}")
print(f"The R2-score from the test set is: {ridge_model.score(xtest_p, ytest)}\n")
