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
            data.loc[i,j]='NA'

print(data)
print("iii. ------------------------------------------------>>>>>>>>>>>>>>>>> ")
rule1=ruleset.rule_1(data)
rule2=ruleset.rule_2(data)
rule3=ruleset.rule_3(data)
rule4=ruleset.rule_4(data)
rule5=ruleset.rule_5(data)


