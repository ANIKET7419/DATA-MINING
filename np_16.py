import numpy as np
import copy
array=np.repeat(0,5)
temp=[]
for i in range(0,5):
   temp.append(copy.copy(array))
matrix=np.array(temp,dtype=int)
for i in range(0,5):
        matrix[i][i]=i+1
print(matrix)
