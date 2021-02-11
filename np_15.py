import numpy as np
import copy
array=np.repeat(0,10)
temp=[]
for i in range(0,10):
   temp.append(copy.copy(array))
matrix=np.array(temp,dtype=int)
for i in range(0,10):
    for j in range(0,10):
        if i==0 or j==0 or i==9 or j==9:
            matrix[i][j]=1
print(matrix)
