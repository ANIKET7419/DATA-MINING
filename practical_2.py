import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import practical_2_ruleset as ruleset
data=pd.read_csv('https://raw.githubusercontent.com/edwindj/datacleaning/master/data/dirty_iris.csv')
print(data)
print('i. Calculate the number and percentage of observations that are complete .')

def calculate_number():
    def func(x):
        for i in range(0,x.shape[0]):
            if pd.isna(x[i]):
                return 0
        return 1
    status=data.apply(func,axis=1)
    n=sum(status)
    print(f" Total Number of observation those are complete {n} ")
    print(f" Percentage {(n/data.shape[0])*100}")
calculate_number()
print(" ii. Replace all the special values in data with NA .")
for  j in data.columns:
    for i in range(data.shape[0]):
     if pd.isnull(data.loc[i,j]):
            data.loc[i,j]=None

print(data)
print("iii. ------------------------------------------------>>>>>>>>>>>>>>>>> ")
rule1=ruleset.rule_1(data)
rule2=ruleset.rule_2(data)
rule3=ruleset.rule_3(data)
rule4=ruleset.rule_4(data)
rule5=ruleset.rule_5(data)
print("iv. ----------------------------------------------->>>>>>>>>>>>>>>>> ")
print(" ---- Rule 1 -----")
print(f" Total Non Violated record : {rule1.sum()}")
print(f" Total  Violated record : {rule1.shape[0]-rule1.sum()}")
print(f" Mean : {rule1.mean()}")
print(f" Median : {rule1.median()}")

print(" ---- Rule 2 -----")
print(f" Total Non Violated record : {rule2.sum()}")
print(f" Total  Violated record : {rule2.shape[0]-rule2.sum()}")
print(f" Mean : {rule2.mean()}")
print(f" Median : {rule2.median()}")

print(" ---- Rule 3 -----")
print(f" Total Non Violated record : {rule3.sum()}")
print(f" Total  Violated record : {rule3.shape[0]-rule3.sum()}")
print(f" Mean : {rule3.mean()}")
print(f" Median : {rule3.median()}")



print(" ---- Rule 4 -----")
print(f" Total Non Violated record : {rule4.sum()}")
print(f" Total  Violated record : {rule4.shape[0]-rule4.sum()}")
print(f" Mean : {rule4.mean()}")
print(f" Median : {rule4.median()}")



print(" ---- Rule 5 -----")
print(f" Total Non Violated record : {rule5.sum()}")
print(f" Total  Violated record : {rule5.shape[0]-rule5.sum()}")
print(f" Mean : {rule5.mean()}")
print(f" Median : {rule5.median()}")


overall=pd.DataFrame({'Rule 1':rule1.astype(int),'Rule 2':rule2.astype(int),'Rule 3':rule3.astype(int),'Rule 4':rule4.astype(int),'Rule 5':rule5.astype(int)})
mea_=overall.mean()
med=overall.median()
total_no_v=overall.sum()
v=overall.shape[0]-overall.sum()
overall=overall.drop('Rule 5',axis=1)
overall=overall.rename(columns={'Rule 1':'Mean','Rule 2':'Median','Rule 3':'No violated','Rule 4':'Violated'})
overall=overall.drop(range(0,overall.shape[0]))
overall['Mean']=mea_
overall['Median']=med
overall['No violated']=total_no_v
overall['Violated']=v
print(overall)
overall.plot(kind='bar')
plt.show()

print("v. Find outliers in sepal length using boxplot and boxplot stats ")
d=data['Sepal.Length']
d=d.dropna()
plt.boxplot(d)
plt.show()