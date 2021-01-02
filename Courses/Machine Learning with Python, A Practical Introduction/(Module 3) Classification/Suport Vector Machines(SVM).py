# This code is an exercise done at module 3 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to solve a classification problem with the Support Vector Machines(SVM) method and evaluate
# the model using F1-score.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pylab as pl
from sklearn import preprocessing, svm
import scipy.optimize as opt
from sklearn.metrics import classification_report, confusion_matrix, f1_score
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/cell_samples.csv'
df = pd.read_csv(url)
cell_df  = df

ax = cell_df[cell_df['Class'] == 4][0: 50].plot(kind='scatter', x='Clump', y='UnifSize', color='DarkBlue', label='malignant')
cell_df[cell_df['Class'] == 2][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='Yellow', label='benign', ax=ax)

cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]
cell_df['BareNuc'] = cell_df['BareNuc'].astype("int")

feature_df = cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize',
       'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
X = np.asarray(feature_df)
target_df = cell_df['Class'].astype("int")
Y = np.asarray(target_df)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
print("Train set: ", x_train.shape, y_train.shape)
print("Test set: ", x_test.shape, y_test.shape)

clf = svm.SVC(kernel='rbf')
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)

cnf_matrix = confusion_matrix(y_test, y_predict, labels=[2, 4])
np.set_printoptions(precision=2)
print(classification_report(y_test, y_predict))
plt.figure
plot_confusion_matrix(cnf_matrix, classes=['Benign(2)', 'Malignant(4)'])
print(f1_score(y_test, y_predict, average='weighted'))

clf2 = svm.SVC(kernel='linear')
clf2.fit(x_train, y_train)
y_predict2 = clf2.predict(x_test)
print(f1_score(y_test, y_predict2, average='weighted'))

plt.show()


