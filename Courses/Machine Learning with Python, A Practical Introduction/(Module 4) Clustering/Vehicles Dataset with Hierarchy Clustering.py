# This code is an exercise done at module 4 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to clusters for vehicles according to some features as horsepower, engine size, miles per galon, etc.
# The exercise shows how to apply Hierarchy Clustering with scipy as with sklearn libraries.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler
import pylab
import matplotlib.cm as cm

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%204/data/cars_clus.csv'
raw_df = pd.read_csv(url)

print('Shape before dataset cleaning: ', raw_df.size)
df = raw_df
df[[ 'sales', 'resale', 'type', 'price', 'engine_s',
       'horsepow', 'wheelbas', 'width', 'length', 'curb_wgt', 'fuel_cap',
       'mpg', 'lnsales']] = df[[ 'sales', 'resale', 'type', 'price', 'engine_s',
       'horsepow', 'wheelbas', 'width', 'length', 'curb_wgt', 'fuel_cap',
       'mpg', 'lnsales']].apply(pd.to_numeric, errors='coerce')
df = df.dropna()
df = df.reset_index(drop=True)
print('Shape after dataset cleaning', df.size)

feature_set = df[['engine_s',  'horsepow', 'wheelbas', 'width', 'length', 'curb_wgt', 'fuel_cap', 'mpg']]
x = feature_set.values
min_max_scaler = MinMaxScaler()
feature_mtx = min_max_scaler.fit_transform(x)

# Using scypi
leng = feature_mtx.shape[0]
D = scipy.zeros([leng, leng])
for i in range(leng):
    for j in range(leng):
        D[i, j] = scipy.spatial.distance.euclidean(feature_mtx[i], feature_mtx[j])

Z = hierarchy.linkage(D, 'complete')
max_d = 3
clusters = hierarchy.fcluster(Z, max_d, criterion='distance')
k = 5
clusters = hierarchy.fcluster(Z, k, criterion='maxclust')

# fig = pylab.figure(figsize=(18, 50))

def llf(id):
    return f'[{df["manufact"][id]} {df["model"][id]} {int(float(df["type"][id]))}]'

# dendro = hierarchy.dendrogram(Z, leaf_label_func=llf, leaf_rotation=0, leaf_font_size=12, orientation='right')

# Using sklearn
dist_matrix = distance_matrix(feature_mtx, feature_mtx)
print(dist_matrix)
agglom = AgglomerativeClustering(n_clusters=6, linkage='complete')
agglom.fit(feature_mtx)
df['cluster_'] = agglom.labels_
n_clusters = max(agglom.labels_) + 1
colors = cm.rainbow(np.linspace(0, 1, n_clusters))
cluster_labels = list(range(0, n_clusters))
fig = plt.figure(figsize=(16, 14))
# for color, label in zip(colors, cluster_labels):
    # subset = df[df.cluster_ == label]
    # for i in subset.index:
        # plt.text(subset.horsepow[i], subset.mpg[i],str(subset['model'][i]), rotation=25) 
    # plt.scatter(subset.horsepow, subset.mpg, s= subset.price*10, c=color, label='cluster'+str(label),alpha=0.5)
    # plt.legend()
# plt.title('Clusters')
# plt.xlabel('horsepow')
# plt.ylabel('mpg')

df.groupby(['cluster_','type'])['cluster_'].count()
agg_cars = df.groupby(['cluster_','type'])['horsepow','engine_s','mpg','price'].mean()

for color, label in zip(colors, cluster_labels):
    subset = agg_cars.loc[(label,),]
    for i in subset.index:
        plt.text(subset.loc[i][0]+5, subset.loc[i][2], 'type='+str(int(i)) + ', price='+str(int(subset.loc[i][3]))+'k')
        plt.scatter(subset.horsepow, subset.mpg, s=subset.price*20, c=color, label='cluster'+str(label))
plt.legend()
plt.title('Clusters')
plt.xlabel('horsepow')
plt.ylabel('mpg')

plt.show()
