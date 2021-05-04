import pandas as pd
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.naive_bayes import  GaussianNB
from sklearn.preprocessing import  LabelEncoder

data=pd.read_csv('/home/ARTHAKUR/Computer_2/College/LAST_SEM/DM/Dataset1.csv')
print(" Summary of the data ")
print(data.describe())
for i in  [0,1,2,3,5,6,7]:
    plt.suptitle(' Data Distribution ')
    plt.title(data.columns[i])
    plt.hist(data.iloc[:,i])
    plt.show()



count=(pd.value_counts(data.iloc[:,data.shape[1]-1]))
plt.suptitle('Class Distribution')
plt.pie(count,shadow=True,labels=count.index,autopct='%1.2f%%')
plt.show()


print(" All the attributes are continuous except PresenceOfHDEL and Protein Localization after observing the histogram of the attributes ")


print(data)
# PREPROCESSING

scaler=MinMaxScaler()

for i in [0,1,2,3,5,6,7]:
    data.iloc[:,i]=scaler.fit_transform(pd.DataFrame(data.iloc[:,i]))

encoder=LabelEncoder()
data['PresenceOfHDEL']=encoder.fit_transform(data['PresenceOfHDEL'])
data['Protien Localization']=encoder.fit_transform(data['Protien Localization'])


Y=data.iloc[:,data.shape[1]-1]
X=data.iloc[:,list(range(0,data.shape[1]-1))]
X=X.to_numpy()
Y=Y.to_numpy()
print(X)
print(Y)

# Training AND Testing DATA SPLIT Ratio  80 :20

xt,xte,yt,yte=train_test_split(X,Y,test_size=0.20,shuffle=True)




acc_=[]

# KNN CLASSIFIER
# Rollno 18/94026 9+4+0+2+6 = 21 =  2 + 1 = 3 so k = 3
knn_classifier=KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(xt,yt)
pre=knn_classifier.predict(xte)
acc_.append(accuracy_score(yte,pre))
plot_confusion_matrix(knn_classifier, xte, yte, display_labels=count.index)
plt.show()


# NAIVE BAYES CLASSIFIER
naive=GaussianNB()
naive.fit(xt,yt)
pre=naive.predict(xte)
acc_.append(accuracy_score(yte,pre))
plot_confusion_matrix(naive, xte, yte, display_labels=count.index)
plt.show()

frame=pd.DataFrame({'ACCURACY':acc_},index=[' KNN ',' NAIVE '])
frame.plot(kind='bar',width=0.3)
plt.show()





