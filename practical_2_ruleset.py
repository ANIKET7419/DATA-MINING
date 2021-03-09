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
def rule_2(data):
    def fun(x):
        for i in range(0,x.size):

            try:
                float(x[i])
            except Exception as e:
                return False
            if x[i]<0:
                 return False
        return True
    status = data.iloc[:,0:4].apply(fun,axis=1)
    count = check_status(status)
    if count != 0:
        print("Violation : Rule 2 is not satisfied ")
        print(f"{count} records are violated ")
    else:
        print("No Violation of rule 2")
    return status
def rule_3(data):
    def fun(x):
        try:
            float(x[0])
            float(x[1])
        except Exception as e:
            return False

        return  x[0]>=x[1]*2
    status = data[['Petal.Length','Petal.Width']].apply(fun,axis=1)
    count = check_status(status)
    if count != 0:
        print("Violation : Rule 3 is not satisfied ")
        print(f"{count} records are violated ")
    else:
        print("No Violation of rule 3")
    return status
def rule_4(data):
    def fun(x):
        try:
            float(x)
        except Exception as e:
            return False
        return x<=30
    status = data['Sepal.Length'].apply(fun)
    count = check_status(status)
    if count != 0:
        print("Violation : Rule 4 is not satisfied ")
        print(f"{count} records are violated ")
    else:
        print("No Violation of rule 4")
    return status
def rule_5(data):
    def fun(x):
        try:
            float(x[0])
            float(x[1])
            float(x[2])
            float(x[3])
        except Exception as e:
            return False
        return x[0]*x[1]>x[2]*x[3]
    status = data.iloc[:,0:4].apply(fun,axis=1)
    count = check_status(status)
    if count != 0:
        print("Violation : Rule 5 is not satisfied ")
        print(f"{count} records are violated ")
    else:
        print("No Violation of rule 5")
    return status


