import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import sample
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# Importe data
red_wine_df = pd.read_csv("winequality_red.csv")
white_wine_df = pd.read_csv("winequality_white.csv")

# Add type label
red_wine_df["wine_type"] = "red"
white_wine_df["wine_type"] = "white"

# Concatenate data
df = pd.concat([red_wine_df, white_wine_df], axis=0)

# Check statistical and type of features in the dataframe
print(df.describe(), "\n")

# Check for missing data
n_missing_values = df.isnull().sum()
print(n_missing_values)
print('''No missing data so no need to raplace the missing data\n''')

# Separating predictor and target variables
X = df.drop("wine_type", axis= 1).values
y = df["wine_type"].values

# Binary Classification
categorical_type = preprocessing.LabelEncoder()
categorical_type.fit(["red", "white"])
y = categorical_type.transform(y) 


# Fitting the model for various max depth and criterion
max_depth = range(1, 20)
criterion = ["entropy", "gini"]
entropy =[]
gini = []
for _ in criterion:
    for __ in max_depth:
        winetree = DecisionTreeClassifier(criterion=_, max_depth=__)
        score = cross_val_score(winetree, X, y, cv=5)
        if _ == "entropy":
            entropy.append(score.mean())
        else:
            gini.append(score.mean())


plt.plot(max_depth, entropy, c='red')
plt.plot(max_depth, gini, c='blue')
plt.legend(["entropy", "gini"])
plt.xlabel('Max Depth Value')
plt.ylabel("F1-Score")
plt.show()

print(f"""The criterion that best fits for the dataset is "entropy".
around the 5th depth the accuracy becomes basic constant. To spend less memory a max depth of 5
is already enough to reach a F1-score around 0.985\n""")

# Using train test split method from sklearn
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size= 0.2, random_state = 4)
print(f'Shape of "X" training set: {xtrain.shape} \nShape of "y" training set {ytrain.shape}')
print(f'Shape of "X" test set: {xtest.shape} \nShape of "y" test set {ytest.shape}\n')

# Tree Classifier with entropy criterion and max_depth = 5
winetree = DecisionTreeClassifier(criterion="entropy", max_depth=5)
winetree.fit(xtrain, ytrain)
y_hat = winetree.predict(xtest)
print(f"F1-score: ", metrics.f1_score(ytest, y_hat), "\n")

print("""The F1-score of the first depth is already around 0.95 for both criterion (entropy and gini).
That may means that the type of wine has a strong correlation with one of the features allowing to
classify the wine class logistically with this featuring.
For that is necessary to check the pearson correlation between the wine type and the other features.\n""")

binary_classification_df = df
binary_classification_df["wine_type"].replace("red", 0, inplace=True)
binary_classification_df["wine_type"].replace("white", 1, inplace=True)
print(binary_classification_df.corr(method="pearson"), "\n")
print("""The total sulfur free has a strong correlation with the wine type. Therefore, 
would be iteresting to check how a model would logistically classify the wine given the 
"total sulfur dioxide".\n""")

# Logistic regression
X_standardize = preprocessing.StandardScaler().fit(X).transform(X)
xstrain, xstest, ystrain, ystest = train_test_split(X_standardize, y, test_size=0.2, random_state=4)
print(f'Shape of "X" training set: {xstrain.shape} \nShape of "y" training set {ystrain.shape}')
print(f'Shape of "X" test set: {xstest.shape} \nShape of "y" test set {ystest.shape}\n')

C = [0.01, 0.1, 0.1, 1, 10]
solver = ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]
newton_cg = []
lbfgs = []
liblinear = []
sag = []
saga = []
for _ in solver:    
    for __ in C:
        LR = LogisticRegression(C=__, solver=_).fit(xstrain, ystrain)
        # ys_hat = LR.predict(xstest)
        score = cross_val_score(LR, X, y, cv=5)
        if _ == "newton-cg":
            # newton_cg.append(metrics.f1_score(ystest, ys_hat))
            newton_cg.append(score.mean())
        elif _ == "lbfgs":
            # lbfgs.append(metrics.f1_score(ystest, ys_hat))
            lbfgs.append(score.mean())
        elif _ == "liblinear":
            # liblinear.append(metrics.f1_score(ystest, ys_hat))
            liblinear.append(score.mean())
        elif _ == "sag":
            # sag.append(metrics.f1_score(ystest, ys_hat))
            sag.append(score.mean())
        else:
            # saga.append(metrics.f1_score(ystest, ys_hat))
            saga.append(score.mean())
            
plt.plot(C, newton_cg)
plt.plot(C, lbfgs)
plt.plot(C, liblinear)
plt.plot(C, saga)
plt.plot(C, sag)
plt.legend(["newton-cg", "lbfgs", "liblinear", "sag", "saga"])
plt.xlabel('C-value')
plt.ylabel("F1-Score")
plt.show()

LR = LogisticRegression(C=0.1, solver="liblinear").fit(xstrain, ystrain)
ys_hat = LR.predict(xstest)
print(f"""As expected the wine can be classified with Logistic Regression reaching a F1-score
of {metrics.f1_score(ystest, ys_hat):.3f} for C=0.1 and liblinear solver""")
