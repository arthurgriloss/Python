# This code is an exercise done at module 4 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to visualize how K-means clustering method work creating clusters for a random generated data.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

np.random.seed(0)
x, y = make_blobs(n_samples=5000, centers=[[4, 4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
# plt.scatter(x[:, 0], x[:, 1], marker='.')

k_means = KMeans(init='k-means++', n_clusters=4, n_init=12)
k_means.fit(x)
print(k_means.labels_)
print(k_means.cluster_centers_)

fig = plt.figure(figsize=(6, 4))
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means.labels_))))
ax = fig.add_subplot(1, 1, 1)
for k, col in zip(range(len([[4, 4], [-2, -1], [2, -3], [1, 1]])), colors):
    my_members = (k_means.labels_ == k)
    cluster_center = k_means.cluster_centers_[k]
    ax.plot(x[my_members, 0], x[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)
ax.set_title('K-Means')
ax.set_xticks(())
ax.set_yticks(())

k_means3= KMeans(init='k-means++', n_clusters=3, n_init=12)
k_means3.fit(x)
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means3.labels_))))
for k, col in zip(range(len(k_means3.cluster_centers_)), colors):
    my_members = (k_means3.labels_ == k)
    cluster_center = k_means3.cluster_centers_[k]
    ax.plot(x[my_members, 0], x[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)

plt.show()
