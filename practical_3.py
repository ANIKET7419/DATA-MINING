import pandas as pd
from sklearn.preprocessing import StandardScaler
st=StandardScaler()
def check(data):
    if data.mean()!=0:
        return False
    else:
        if data.std()==1:
            return True
        else:
            return False
print(' Wine DataSet ')
data=pd.read_csv('https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv')
for i in range(0,data.shape[1]):
    status = check(data.iloc[:,i])
    if not status:
        temp=st.fit_transform(pd.DataFrame(data.iloc[:,i]))
        data.iloc[:,i]=temp
print("After Standardization ")
print(data)
print(' Iris DataSet ')
data=pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')
data.dropna(axis=0,inplace=True)
for i in range(0,data.shape[1]-1):
    status = check(data.iloc[:,i])
    if not status:
        temp=st.fit_transform(pd.DataFrame(data.iloc[:,i]))
        data.iloc[:,i]=temp
print("After Standardization ")
print(data)



