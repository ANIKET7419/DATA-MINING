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
final=[]
for i in array1:
    if not i in array2:
       final.append(i)
array1=np.array(final)
print(" Final Array 1 " ,end='\n')
print(array1)
print(" Final Array 2 ",end='\n')
print(array2)