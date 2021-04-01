# NAME - ANIKET , AKRAM KHAN
# ROLLNO - 18/94026 , 18/94047
# TITLE - FAKE NEWS DETECTION
# DATASET SOURCE - https://www.kaggle.com/jruvika/fake-news-detection
# PROBLEM :- WE HAVE DATASET HAVING  DETAILS REGARDING NEWS WHETHER IT IS FAKE OR REAL . OUR MOTIVE IS TO BUILD MODEL ON THIS DATA SET TO PREDICT FURTHER
# NEWS ( REAL OR FAKE )
# There are four attributes Urls , Heading , Body and the Label
# Url - String - Source of the news
# Heading - String - Heading of the news
# Body - String - Actual Content of news
# Label - 0 for Fake and 1 for Real
# No need to normalize















import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data = pd.read_csv('/home/ARTHAKUR/Downloads/data.csv')
data=  data.drop(['URLs'], axis=1)
data = data.dropna()

plt.title('Headline')
plt.hist(encoder.fit_transform(data.iloc[:,0]))
plt.show()

plt.title('Body')
plt.hist(encoder.fit_transform(data.iloc[:,1]))
plt.show()

plt.title('Label')
plt.hist(data.iloc[:,2])
plt.xticks([0,1],['Fake','Real'])
plt.show()

i=0
j=0
for i1 in data['Label']:
    if i1==1:
        i+=1
    else:
        j+=1
plt.show()
plt.pie([i,j],shadow=True,labels=['Real','Fake'],autopct='%1.2f%%')
plt.show()









