# This code is an exercise done at module 4 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to visualize how Density-Based Clustering method work creating clusters for a random generated data
# and show the advantage over K-Means method for data with outliers.

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def createDataPoints(centroidLocation, numSamples, clusterDeviation):
    x, y = make_blobs(n_samples=numSamples, centers=centroidLocation, cluster_std=clusterDeviation)
    x = StandardScaler().fit_transform(x)
    return x, y


x, y = createDataPoints([[4, 3], [2, -1], [-1, 4]], 1500, 0.5)

epsilon = 0.3
minimumSamples = 7
db = DBSCAN(eps=epsilon, min_samples=minimumSamples).fit(x)
labels = db.labels_

core_sample_mask = np.zeros_like(labels, dtype=bool)
core_sample_mask[db.core_sample_indices_]= True
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(n_clusters)
unique_labels = set(labels)


colors =  plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
fig = plt.figure(figsize=(6, 8))
fig.add_subplot(2, 1, 1)
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = 'k'
    class_member_mask = (labels == k)
    xy = x[class_member_mask & core_sample_mask]
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], marker=u'o', alpha=0.5)
    xy = x[class_member_mask & ~core_sample_mask]
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], marker=u'o', alpha=0.5)

k = 3
k_means3 = KMeans(init = "k-means++", n_clusters = k, n_init = 12)
k_means3.fit(x)
fig.add_subplot(2, 1, 2)
for k, col in zip(range(k), colors):
    my_members = (k_means3.labels_ == k)
    plt.scatter(x[my_members, 0], x[my_members, 1],  c=col, marker=u'o', alpha=0.5)

plt.show()
