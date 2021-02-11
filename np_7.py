import numpy as np
import copy
array1=np.array([[1,2,4],[5,6,7],[8,9,10]])
array1=np.transpose(array1)
temp=copy.deepcopy(array1[0])
array1[0]=array1[1]
array1[1]=temp
array1=np.transpose(array1)
print(array1)
