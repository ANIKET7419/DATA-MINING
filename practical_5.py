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
from sklearn.preprocessing import  StandardScaler
iris=datasets.load_iris()
x=iris.data
y=iris.target
d_c=[]
k_c=[]
n_c=[]


def decision_tree(nskip=True):
    print('----------- Decision Tree --------------')
    tree= DT(criterion='entropy')
    tree.fit(xt,yt)
    pred=tree.predict(xte)
    d_c.append(accuracy_score(yte,pred))
    if nskip:
        print(confusion_matrix(yte, pred))
        pc(tree, xte, yte, display_labels=iris.target_names)
        t.plot_tree(tree, filled=True, impurity=True, feature_names=iris.feature_names, class_names=iris.target_names)
        plt.show()



def naive(nskip=True):
    print('------------ Naive Bayes ---------')
    nb=GaussianNB()
    nb.fit(xt,yt)
    pre=nb.predict(xte)
    n_c.append(accuracy_score(yte,pre))
    if nskip:
        print(confusion_matrix(yte, pre))
        pc(nb, xte, yte, display_labels=iris.target_names)
        plt.show()


def neighbour(nskip=True):
    print('----------- Kth Nearest Neighbour  ----------------')
    k=KNeighborsClassifier(n_neighbors=int(np.sqrt(len(xt))))
    k.fit(xt,yt)
    pre=k.predict(xte)
    k_c.append(accuracy_score(yte,pre))
    if nskip:
        print(confusion_matrix(yte, pre))
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


print("-------------------------------- Random Sub sampling Method ---------------------------------")
d_c.clear()
k_c.clear()
n_c.clear()
k=int(input('Enter k'))
x__t1=[]
for i in range(0,k):
    size=random.random()
    x__t1.append(str(round(size*100,2)))
    xt, xte, yt, yte = train_test_split(x, y, test_size=size, shuffle=True)
    decision_tree()
    naive()
    neighbour()
data=pd.DataFrame({'Decision Tree':d_c,'Naive Bayes':n_c,'KNN':k_c})
data.plot(kind='bar',width=0.2)
x_t1=[i for i in range(0,k)]
plt.xticks(x_t1,x__t1)
plt.show()
print(' Weighted Accuracy of DT ',np.sum(d_c)/len(d_c))
print(' Weighted Accuracy of Naive Bayes  ',np.sum(n_c)/len(n_c))
print(' Weighted Accuracy of KNN  ',np.sum(k_c)/len(k_c))
print()

print('----------------------- CROSS VALIDATION ---------------------- ')
k=int(input('Enter value of k '))
d_c.clear()
k_c.clear()
n_c.clear()
for i in range(0,k):
         t1=x[:i*k]    # training set p1
         te=x[i*k:i*k+k] # testing set
         t2=x[i*k+k:]    # training set p2
         xt=np.append(t1,t2)
         xt.shape=(xt.shape[0]//t1.shape[1],t1.shape[1])
         xte=te
         t1 = y[:i * k]  # training set p1
         te = y[i * k:i * k + k]  # testing set
         t2 = y[i * k + k:]  # training set p2
         yt=np.append(t1,t2)
         yte=te
         if len(xte)!=0 and len(xt)!=0:
            decision_tree(False)
            naive(False)
            neighbour(False)
data = pd.DataFrame({'Decision Tree': d_c, 'Naive Bayes': n_c, 'KNN': k_c})
data.plot(kind='bar', width=0.2)
plt.show()
print(' Weighted Accuracy of DT ', np.sum(d_c) / len(d_c))
print(' Weighted Accuracy of Naive Bayes  ', np.sum(n_c) / len(n_c))
print(' Weighted Accuracy of KNN  ', np.sum(k_c) / len(k_c))
print()

print('After scaling ')

scaler=StandardScaler()
x=scaler.fit_transform(x)
d_c.clear()
k_c.clear()
n_c.clear()
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
