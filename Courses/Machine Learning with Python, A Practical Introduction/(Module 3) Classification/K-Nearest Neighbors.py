# This code is an exercise done at module 3 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to solve a classification problem with the KNN method.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv'
df = pd.read_csv(url)

print(df['custcat'].value_counts())
# df.hist(column='income', bins=50)

print(df.columns)
X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed',
       'employ', 'retire', 'gender', 'reside']].values
y = df['custcat'].values

x = preprocessing.StandardScaler().fit(X).transform(X.astype('float'))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)

neighbors = KNeighborsClassifier(n_neighbors=4).fit(x_train, y_train)
y_predict = neighbors.predict(x_test)
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neighbors.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, y_predict))

x = preprocessing.StandardScaler().fit(X).transform(X.astype("float"))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
neigh = KNeighborsClassifier(n_neighbors=6).fit(x_train, y_train)
y_predict = neigh.predict(x_test)
print("Accuracy train data: ", metrics.accuracy_score(y_train, neigh.predict(x_train)))
print("Accuracy test data: ", metrics.accuracy_score(y_test, y_predict))

mean_acc = []
std_acc = []
x = preprocessing.StandardScaler().fit(X).transform(X.astype("float"))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
for n in range(1, 11):
    neigh = KNeighborsClassifier(n_neighbors=n).fit(x_train, y_train)
    y_predict = neigh.predict(x_test)
    mean_acc.append(metrics.accuracy_score(y_test, y_predict))
    std_acc.append(np.std(y_test == y_predict)/np.sqrt(y_predict.shape[0]))
mean_acc = np.asanyarray(mean_acc)
std_acc = np.asanyarray(std_acc)
print(mean_acc)
plt.plot(range(1, 11), mean_acc, 'g')
plt.fill_between(range(1, 11), mean_acc - 1 * std_acc, mean_acc + 1 * std_acc, alpha=0.1)
plt.fill_between(range(1, 11), mean_acc - 3 * std_acc, mean_acc + 3 * std_acc, alpha=0.1, color='green')
plt.legend(('Accuracy', '+/- 1*std', '+/- 3*std'))
plt.ylabel('Accuracy')
plt.xlabel('Number of Neighbors')
plt.tight_layout()

plt.show()
