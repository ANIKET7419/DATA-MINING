import numpy as np
list_=[]
count=0
temp=[]
for i in range(10,34):
    if count==3:
        list_.append(temp)
        temp=[]
        temp.append(i)
        count=0
    else:
        temp.append(i)
    count+=1
list_.append(temp)
array=np.array(list_)
subarrays=np.split(array,indices_or_sections=4)
print(subarrays)
