import numpy as np
import copy
array1 = np.array([[1, 2, 4], [5, 6, 7], [8, 9, 10],[11,22,34],[190,167,45],[3477,457,458]])
def swap(i,j):
    global array1
    array1 = np.transpose(array1)
    temp=copy.deepcopy(array1[i])
    array1[i]=array1[j]
    array1[j]=temp
    array1 = np.transpose(array1)
i=0
j=2
while i<j:
    swap(i,j)
    i+=1
    j-=1
print(array1)