from sklearn.datasets import *
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from scipy.spatial import  distance_matrix
from scipy.cluster import  hierarchy

data=pd.read_csv('/home/ARTHAKUR/Computer_2/College/LAST_SEM/DM/HTRU_2.csv',header=None)

HR=data.drop(columns=8)
data=pd.DataFrame(scale(HR))
pca=PCA(n_components=2)
data=pca.fit_transform(data)

hier=AgglomerativeClustering(n_clusters=3,linkage='average')
hier.fit(data)

new_labels = hier.labels_
plt.scatter(data[:,0],data[:,1],c = new_labels)
plt.show()

mat = distance_matrix(data,data)

Z = hierarchy.linkage(mat,'average')

dendro=hierarchy.dendrogram(Z)



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
