import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
plt.rcParams['figure.figsize'] = (8, 6)
plt.style.use('ggplot') 
df = pd.read_csv(r"eruptionreadings.csv")
# Creating a sample dataset with 2 clusters
X, y = make_blobs(n_samples=272, n_features=2, centers=2)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1])
# Initializing KMeans
kmeans = KMeans(n_clusters=2)
# Fitting with inputs
kmeans = kmeans.fit(X)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], c="orange")
ax.scatter(C[:, 0], C[:, 1], marker='*', c='green', s=800)
plt.show()
