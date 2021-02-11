import numpy as np
len1=int(input("Enter length of array 1 "))
print("Enter elements of array 1 ",end='\n')
array1=[]
for i in range(0,len1):
    array1.append(int(input()))
array1=np.array(array1)
final=np.array([],dtype=int)
for i in range(0,len(array1)):
    if  array1[i]>=5 and array1[i]<=10:
       final=np.append(final,array1[i])
print(final)
