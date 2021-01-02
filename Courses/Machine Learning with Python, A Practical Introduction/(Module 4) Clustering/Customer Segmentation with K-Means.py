# This code is an exercise done at module 4 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to create a customer segmentation by clustering them according to some features as education, age, and income.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%204/data/Cust_Segmentation.csv'
raw_df = pd.read_csv(url)
df = raw_df.drop('Address', axis=1)

x = df.values[:, 1:]
x = np.nan_to_num(x)
Clus_dataSet = StandardScaler().fit_transform(x)

k_means = KMeans(init='k-means++', n_clusters=3, n_init=12)
k_means.fit(x)
df['Clus_km'] = k_means.labels_
df.groupby('Clus_km').mean()

area = np.pi * (x[:, 1]**2)
plt.scatter(x[:, 0], x[:, 3], s=area, c=k_means.labels_.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)

fig = plt.figure(figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
plt.cla()
ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')
ax.scatter(x[:, 1], x[:, 0], x[:, 3], c=k_means.labels_.astype(np.float))

plt.show()
