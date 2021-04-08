from sklearn.tree import DecisionTreeClassifier as DT
from  sklearn import tree as t
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv('paper_csv.csv')
x=data.iloc[:,0:data.shape[1]-1]
y=data.iloc[:,data.shape[1]-1]
x=x.to_numpy()
y=y.to_numpy()
print(x)
print(y)
tree= DT(criterion='entropy')
tree.fit(x,y)
t.plot_tree(tree,filled=True, impurity=True, feature_names=['A','B'], class_names=['+','-'])
plt.show()