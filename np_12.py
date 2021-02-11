import numpy as np
len1=int(input("Enter length of array 1 "))
len2=int(input("Enter length of array 2 "))
print("Enter elements of array 1 ",end='\n')
array1=[]
array2=[]
for i in range(0,len1):
    array1.append(int(input()))
print("Enter element of array 2 ",end='\n')
for i in range(0,len2):
    array2.append(int(input()))
array1=np.array(array1)
array2=np.array(array2)
final=np.array([],dtype=int)
for i in range(0,min(len(array1),len(array2))):
    if  array1[i]==array2[i]:
       final=np.append(final,i)
print(final)