def check_status(val):
    count=0
    for i in val:
        if not i:
            count+=1
    return count

def rule_1(data):
    fun=lambda x:x=='setosa' or x=='versicolor' or x=='virginica'
    status=data['Species'].apply(fun)
    count=check_status(status)
    if count!=0:
        print("Violation : Rule 1 is not satisfied ")
        print(f"{count} records are violated")
    else:
        print("No Violation of rule 1")
    return status
import pandas as pd
def rule_2(data):

    fun = lambda x:x
    status = data.iloc[:,0:4].apply(fun,axis=1)
    count = check_status(status)
    exit(100)
    if count != 0:
        print("Violation : Rule 2 is not satisfied ")
        print(f"{count} records are violated ")
    else:
        print("No Violation of rule 2")
    return status