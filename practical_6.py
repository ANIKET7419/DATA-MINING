from sklearn.datasets import make_circles
from sklearn.datasets import make_blobs
from matplotlib.pyplot import  scatter
from  sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
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

