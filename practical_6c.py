from sklearn.datasets import *
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np
n_samples =1500
noisy_circles =make_circles(n_samples=n_samples)
noisy_moons=make_moons(n_samples=n_samples)
blobs = make_blobs(n_samples=n_samples)
no_structures =np.random.rand(n_samples,2),None
datasets=[noisy_circles,noisy_moons,blobs,no_structures]
for i,j in datasets:
  X=StandardScaler().fit_transform(i)
  for num in range(2,5):
    agglomerative = AgglomerativeClustering(n_clusters=num,linkage='single')
    agglomerative1=agglomerative.fit(X)
    l=agglomerative1.labels_
    plt.scatter(X[:,0],X[:,1],c=l,cmap='gist_rainbow')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()