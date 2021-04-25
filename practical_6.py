from sklearn.datasets import make_circles
from sklearn.datasets import make_blobs
from matplotlib.pyplot import  scatter
from  sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import numpy as np
from sklearn.metrics import silhouette_score



data=pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
data.dropna(inplace=True)
data=data.to_numpy()
kmean = KMeans(n_clusters=3)
kmean.fit(data[:,1:3])
lab=kmean.labels_
centroids=kmean.cluster_centers_

scatter(data[:,1],data[:,2],cmap='jet',c=lab,edgecolors='black')
scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()





data=pd.read_csv('/home/ARTHAKUR/Computer_2/College/LAST_SEM/DM/HTRU_2.csv',header=None)


HR=data.drop(columns=8)
data=pd.DataFrame(scale(HR))
pca=PCA(n_components=2)
data=pca.fit_transform(data)



e=[]
for i in np.arange(2,10):
  clusters=KMeans(n_clusters=i)
  clusters.fit(data)
  e.append(clusters.inertia_)
plt.plot(np.arange(2,10),e)
plt.xlabel("Clusters")
plt.ylabel("Squared sum of Error")
plt.show()

score=[]
for i in np.arange(2,10):
    clusters=KMeans(n_clusters=i)
    clusters.fit(data)
    score.append(silhouette_score(data,clusters.labels_))
plt.plot(np.arange(2,10),score)
plt.xlabel("Clusters")
plt.ylabel("Silhouette score")
plt.show()




n_samples=2000
data=make_circles(n_samples)
data=data[0]
scaler=StandardScaler()
data=scaler.fit_transform(data)
scatter(data[:,0],data[:,1])
plt.show()
kmean=KMeans(n_clusters=3)
kmean=kmean.fit(data)
lab=kmean.labels_
centroids=kmean.cluster_centers_
scatter(data[:,0],data[:,1],cmap='jet',c=lab,edgecolors='black')
scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()


n_samples=2000
data=make_blobs(n_samples)
data=data[0]
data=scaler.fit_transform(data)
scatter(data[:,0],data[:,1])
plt.show()
kmean=KMeans(n_clusters=3)
kmean=kmean.fit(data)
lab=kmean.labels_
centroids=kmean.cluster_centers_
scatter(data[:,0],data[:,1],cmap='jet',c=lab,edgecolors='black')
scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()




n_samples=2000
data=make_moons(n_samples)
data=data[0]
data=scaler.fit_transform(data)
scatter(data[:,0],data[:,1])
plt.show()
kmean=KMeans(n_clusters=3)
kmean=kmean.fit(data)
lab=kmean.labels_
centroids=kmean.cluster_centers_
scatter(data[:,0],data[:,1],cmap='jet',c=lab,edgecolors='black')
scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()

