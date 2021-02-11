import numpy as np
len1=int(input("Enter length of array  "))
print("Enter elements of array  ",end='\n')
array1=[]
for i in range(0,len1):
    array1.append(int(input()))
array1=np.array(array1)
count=0
for i,j in enumerate(array1):
    if j>10:
        array1[i]=array1[i]*10
        count=count+1
print("Count ::",end='\n')
print(count)
print("New Array : ")
print(array1)

