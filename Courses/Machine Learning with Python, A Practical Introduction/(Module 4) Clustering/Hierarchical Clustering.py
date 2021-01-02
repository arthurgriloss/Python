# This code is an exercise done at module 4 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to visualize how Hierarchical clustering method work creating clusters for a random generated data.

# Some lines of code are commented to avoid several not desired plots or visualization issues.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs

x1, y1 = make_blobs(n_samples=50, centers=[[4, 4], [-2, -1], [1, 1], [10, 4]], cluster_std=0.9)
# plt.scatter(x1[:, 0], x1[:, 1], marker='o')

agglom = AgglomerativeClustering(n_clusters=4, linkage='average')
agglom.fit(x1, y1)

fig = plt.figure(figsize=(6, 4))
x_min, x_max = np.min(x1, axis=0), np.max(x1, axis=0)
x1 = (x1 - x_min)/(x_max - x_min)
for i in range(x1.shape[0]):
    plt.text(x1[i, 0], x1[i, 1], str(y1[i]), color=plt.cm.nipy_spectral(agglom.labels_[i]/10),
    fontdict={'weight': 'bold', 'size': 9})
plt.xticks([])
plt.yticks([])
# plt.scatter(x1[:, 0], x1[:, 1], marker='.')
dist_matrix = distance_matrix(x1, x1)
print(dist_matrix)

Z = hierarchy.linkage(dist_matrix)
# dendro = hierarchy.dendrogram(Z)

Z = hierarchy.linkage(dist_matrix,'average')
hierarchy.dendrogram(Z)

plt.show()
