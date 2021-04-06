import pandas as pd
from mlxtend.preprocessing import  TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules
import requests
file=open('/root/PycharmProjects/DATA_MINING/groceries.csv','w')
data=requests.get('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/groceries.csv')
file.write(data.text)
file.close()
file=open('/root/PycharmProjects/DATA_MINING/groceries.csv','r')
lines=file.readlines()
data=[ [x if x[len(x)-1]!='\n' else x[:len(x)-1]  for x in y.split(',')] for y in lines]
print(data)
encoder=TransactionEncoder()
data=encoder.fit_transform(data)
data=data.astype('int')
print(data)
data=pd.DataFrame(data,columns=encoder.columns_)
print(data)


print(" Minimum support 50 % and confidence 75 % ")
frq_items = apriori(data, min_support=0.50,use_colnames=True)
rules = association_rules(frq_items, metric="confidence", min_threshold=0.75)
print(rules)

print(" Minimum support 60 % and confidence 60 % ")
frq_items = apriori(data, min_support=0.60,use_colnames=True)
rules = association_rules(frq_items, metric="confidence", min_threshold=0.60)
print(rules)