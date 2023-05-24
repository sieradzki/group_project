import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("affectnet_train.csv", names=["class", "image", "pitch", "yaw", "roll"], index_col=None)

from sklearn.cluster import KMeans
data = pd.DataFrame(df.iloc[:, -3:])

k = 4
kmeans = KMeans(n_clusters = k)
kmeans.fit(data)

data['cluster_label'] = kmeans.labels_

plt.scatter(data['yaw'], data['roll'], c=data['cluster_label'], cmap='viridis')
plt.xlabel('Yaw')
plt.ylabel('Roll')
plt.title('Clusters in Yaw-Roll space')
plt.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Visualize the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['pitch'], data['yaw'], data['roll'], c=data['cluster_label'], cmap='viridis')

ax.set_xlabel('Pitch')
ax.set_ylabel('Yaw')
ax.set_zlabel('Roll')

plt.title('Clusters in 3D space')
plt.show()