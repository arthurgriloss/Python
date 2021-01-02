# This code is an exercise done at module 3 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to introduce confusion matrix and to teach how to solve a classification problem with the Logistic Regression method.

import pandas as pd
import numpy as np
import pylab as pl
import scipy.optimize as opt
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, log_loss
import itertools


def plot_confusion_matrix (cm, classes, normalize=False, title='Confusion Matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    if normalize:
        cm = cm.astype("float")/ cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max()/2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment='center', color='white' if cm[i, j] > thresh else 'black')
    plt.tight_layout
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')

    
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/ChurnData.csv'
df = pd.read_csv(url)

churn_df = df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip',   'callcard', 'wireless','churn']]
churn_df['churn'] = churn_df['churn'].astype('int')

print(churn_df.columns)
print(churn_df.shape)

X = np.asarray(churn_df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip']])
Y = np.asarray(churn_df['churn'])

X = preprocessing.StandardScaler().fit(X).transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
print("Train set: ", x_train.shape, y_train.shape)
print("Test set: ", x_test.shape, y_test.shape)

LR = LogisticRegression(C=0.01, solver='liblinear').fit(x_train, y_train)
y_predict = LR.predict(x_test)
y_prob = LR.predict_proba(x_test)

cnf_matrix = confusion_matrix(y_test, y_predict, labels=[1, 0])
print(cnf_matrix)
np.set_printoptions(precision=2)
plt.figure
plot_confusion_matrix(cnf_matrix, classes=['churn=1', 'churn=0'], normalize=False, title='Confusion Matrix')
print(classification_report(y_test, y_predict))
print(log_loss(y_test, y_prob))

LR2 = LogisticRegression(C=0.01, solver='sag').fit(x_train, y_train)
y_prob2 = LR2.predict_proba(x_test)
print(f"LogLoss: {log_loss(y_test, y_prob2)}")

plt.show()

