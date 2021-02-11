import numpy as np
import copy
array1 = np.array([[1, 2, 4], [5, 6, 7], [8, 9, 10],[11,22,34],[190,167,45],[3477,457,458]])
def swap(i,j):
    temp=copy.deepcopy(array1[i])
    array1[i]=array1[j]
    array1[j]=temp
i=0
j=5
while i<j:
    swap(i,j)
    i+=1
    j-=1
print(array1)