import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import cross_val_score
from  sklearn import tree as t
from sklearn.naive_bayes import  GaussianNB
from sklearn.neighbors import KNeighborsClassifier




data=pd.read_csv('/home/ARTHAKUR/Computer_2/College/heart.csv')
print(" Summary of the data ")
print(data.describe())
count=[0,0,0,0,0]
for i in data['target']:
    count[i]=count[i]+1
plt.title('Class Distribution')
plt.pie(count,shadow=True,labels=['0','1','2','3','4'],autopct='%1.2f%%')
plt.show()

print(' Categorical Attributes are :-> ')
print('Sex\nChest Pain Type\nNumber of major vessels\ntarget\nExercise Induced Angina\nFasting Blood Sugar\n')
print('Continuous Attributes  :-> ')
print('Age\nResting Blood Pressure\nCholestrol\nResting Electrocardiographic Resylt\nMax Heart Rate\n')


print('Preprocessing :--->>> ')
encoder=LabelEncoder()
data['sex']=encoder.fit_transform(data['sex'])
data['Chest Pain Type']=encoder.fit_transform(data['Chest Pain Type'])
print(data)

scaler=MinMaxScaler()
for i in [3,4,6,7,9,10]:
    data.iloc[:,i]=scaler.fit_transform(pd.DataFrame(data.iloc[:,i]))
print(data)



X=data.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11]]
Y=data.iloc[:,12]




print('----------------------- CROSS VALIDATION ---------------------- ')

print('----------- Decision Tree --------------')
tree= DT(criterion='entropy')
d_score=cross_val_score(tree,X,Y,cv=7)
print('------------ Naive Bayes ---------')
nb=GaussianNB()
n_score=cross_val_score(nb,X,Y,cv=7)
print('----------- Kth Nearest Neighbour  ----------------')
k = KNeighborsClassifier(n_neighbors=6)
k_score=cross_val_score(k,X,Y,cv=7)
data = pd.DataFrame({'Decision Tree': d_score, 'Naive Bayes': n_score, 'KNN': k_score})
data.plot(kind='bar', width=0.2)
plt.show()
print(' Weighted Accuracy of DT ', np.sum(d_score) / len(d_score))
print(' Weighted Accuracy of Naive Bayes  ', np.sum(n_score) / len(n_score))
print(' Weighted Accuracy of KNN  ', np.sum(k_score) / len(k_score))
print()
