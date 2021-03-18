from sklearn import  datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.metrics import confusion_matrix,accuracy_score
from  sklearn import tree as t
from sklearn.naive_bayes import  GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from sklearn.metrics import plot_confusion_matrix as pc
iris=datasets.load_iris()
x=iris.data
y=iris.target
d_c=[]
k_c=[]
n_c=[]


def decision_tree():
    print('----------- Decision Tree --------------')
    tree= DT(criterion='entropy')
    tree.fit(xt,yt)
    pred=tree.predict(xte)
    print(confusion_matrix(yte,pred))
    d_c.append(accuracy_score(yte,pred))
    t.plot_tree(tree,filled=True,impurity=True,feature_names=iris.feature_names,class_names=iris.target_names)
    pc(tree,xte,yte,display_labels=iris.target_names)
    plt.show()



def naive():
    print('------------ Naive Bayes ---------')
    nb=GaussianNB()
    nb.fit(xt,yt)
    pre=nb.predict(xte)
    print(confusion_matrix(yte,pre))
    n_c.append(accuracy_score(yte,pre))
    pc(nb,xte,yte,display_labels=iris.target_names)
    plt.show()


def neighbour():
    print('----------- Kth Nearest Neighbour  ----------------')
    k=KNeighborsClassifier(n_neighbors=int(np.sqrt(len(x))))
    k.fit(xt,yt)
    pre=k.predict(xte)
    print(confusion_matrix(yte,pre))
    k_c.append(accuracy_score(yte,pre))
    pc(k,xte,yte,display_labels=iris.target_names)
    plt.show()
for i in [0.25,0.33]:
 xt,xte,yt,yte=train_test_split(x,y,test_size=i,shuffle=True)
 decision_tree()
 naive()
 neighbour()

print(d_c,k_c,n_c)
data=pd.DataFrame({'Decision Tree':d_c,'Naive Bayes':n_c,'KNN':k_c})
data.plot(kind='bar',width=0.2)
plt.xticks([0,1],['25%','33%'])
plt.show()


print("-------------------------------- Random Subsampling Method ---------------------------------")
d_c.clear()
k_c.clear()
n_c.clear()
k=int(input('Enter k'))
for i in range(0,k):
    size=random.random()
    xt, xte, yt, yte = train_test_split(x, y, test_size=size, shuffle=True)
    decision_tree()
    naive()
    neighbour()
print(d_c,k_c,n_c)
data=pd.DataFrame({'Decision Tree':d_c,'Naive Bayes':n_c,'KNN':k_c})
data.plot(kind='bar',width=0.2)
plt.xticks([0,1],['25%','33%'])
plt.show()



print('----------------------- CROSS VALIDATION ---------------------- ')
k=int(input('Enter value of k '))
if int(len(x)%k)!=len(x)%k:
    print("Please enter valid value of k ")
else:
    for i in range(0,k):
         t1=x[:i*k]    # training set p1
         te=x[i*k:i*k+k] # testing set
         t2=x[i*k+k:]    # training set p2
         x_temp_tra=t1+t2
         x_temp_tes=te
         t1 = y[:i * k]  # training set p1
         te = y[i * k:i * k + k]  # testing set
         t2 = y[i * k + k:]  # training set p2
         y_temp_tra=t1+t2
         y_temp_tes=te





