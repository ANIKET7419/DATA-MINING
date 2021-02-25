import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('https://raw.githubusercontent.com/edwindj/datacleaning/master/data/dirty_iris.csv')
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


