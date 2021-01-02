# This code is an exercise done at module 3 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to teach how to format categorical features to binary/discrete values and 
# how to solve a classification problem with the decision tree method.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from io import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
df = pd.read_csv(url)
print(df.shape)

X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
Y = df['Drug'].values

categorical_sex = preprocessing.LabelEncoder()
categorical_sex.fit(['F', 'M'])
X[:, 1] = categorical_sex.transform(X[:, 1])
categorical_BP = preprocessing.LabelEncoder()
categorical_BP.fit(['LOW', 'NORMAL', 'HIGH'])
X[:, 2] = categorical_BP.transform(X[:, 2])
categorical_Chol = preprocessing.LabelEncoder()
categorical_Chol.fit(['NORMAL', 'HIGH'])
X[:, 3] = categorical_Chol.transform(X[:, 3])

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=3)
print(f'Shape of X training set: {x_train.shape} \nShape of Y training set {y_train.shape}')
print(f'Shape of X test set: {x_test.shape} \nShape of Y test set {y_test.shape}')

drugtree = DecisionTreeClassifier(criterion='entropy', max_depth=4)
drugtree.fit(x_train, y_train)
y_predict = drugtree.predict(x_test)
print("Decision Tree accuracy score: ", metrics.accuracy_score(y_test, y_predict))

dot_data = StringIO()
filename = "drugtree.png"
featureNames = df.columns[0:5]
targetNames = df['Drug'].unique().tolist()
out = tree.export_graphviz(drugtree, feature_names=featureNames, out_file=dot_data, class_names=np.unique(y_train),
                           filled=True, special_characters=True, rotate=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img, interpolation='nearest')
