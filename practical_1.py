import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_table("/root/PycharmProjects/DATA_MINING/people.txt",sep=' ')
print(data)
def check_status(val):
    count=0
    for i in val:
        if not i:
            count+=1
    return count
def rule_4():
    fun=lambda x:x.Age<18 and x.agegroup=='child' or x.Age>=18 and x.Age<=65 and x.agegroup=='adult' or x.Age>65 and x.agegroup=='elderly'
    status=data[['Age','agegroup']].apply(fun,axis=1)
    count=check_status(status)
    if count!=0:
        print("Violation : Rule 4 is not satisfied ")
        print(f"{count} records are violated")
    else:
        print("No Violation of rule 4")
    return status

def age_range():
    fun=lambda x: x >=0 and x<=150
    status=data['Age'].apply(fun)
    count=check_status(status)
    if count!=0:
        print("Violation : Age is not in the range of 0 to 150 ")
        print(f"{count} records are violated")
    else:
        print("No Violation of rule 1")
    return status
def age_marriage():
    fun=lambda  x:x.Age>x.yearsmarried
    status=data[['Age','yearsmarried']].apply(fun,axis=1)
    count = check_status(status)
    if count != 0:
        print("Violation : Age is not greater than total married years ")
        print(f"{count} records are violated")
    else:
        print("No Violation of rule 2")
    return status
def status():
    fun=lambda x:x in ['widowed','married','single']
    st=data['status'].apply(fun)
    count=check_status(st)
    if count!=0:
        print("Violation : The status is not single,married or widowed .")
        print(f"{count} records are violated")
    else:
        print("No Violation of rule 3")
    return st


rule_1=age_range()
rule_2=age_marriage()
rule_3=status()
rule4=rule_4()
print(" ---- Rule 1 -----")
print(f" Total Non Violated record : {rule_1.sum()}")
print(f" Total  Violated record : {rule_1.shape[0]-rule_1.sum()}")
print(f" Mean : {rule_1.mean()}")
print(f" Median : {rule_1.median()}")

print(" ---- Rule 2 -----")
print(f" Total Non Violated record : {rule_2.sum()}")
print(f" Total  Violated record : {rule_2.shape[0]-rule_2.sum()}")
print(f" Mean : {rule_2.mean()}")
print(f" Median : {rule_2.median()}")

print(" ---- Rule 3 -----")
print(f" Total Non Violated record : {rule_3.sum()}")
print(f" Total  Violated record : {rule_3.shape[0]-rule_3.sum()}")
print(f" Mean : {rule_3.mean()}")
print(f" Median : {rule_3.median()}")



print(" ---- Rule 4 -----")
print(f" Total Non Violated record : {rule4.sum()}")
print(f" Total  Violated record : {rule4.shape[0]-rule4.sum()}")
print(f" Mean : {rule4.mean()}")
print(f" Median : {rule4.median()}")
overall=pd.DataFrame({'Rule 1':rule_1.astype(int),'Rule 2':rule_2.astype(int),'Rule 3':rule_3.astype(int),'Rule 4':rule4.astype(int)})
mea_=overall.mean()
med=overall.median()
total_no_v=overall.sum()
v=overall.shape[0]-overall.sum()
overall=overall.rename(columns={'Rule 1':'Mean','Rule 2':'Median','Rule 3':'No violated','Rule 4':'Violated'})
overall=overall.drop(range(0,overall.shape[0]))
overall['Mean']=mea_
overall['Median']=med
overall['No violated']=total_no_v
overall['Violated']=v
print(overall)
overall.plot(kind='bar')
plt.show()