import numpy as np
array = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(" i. Sort above array by second row ",end='\n')
sorted_array=array[:,np.argsort(array[1])]
print(sorted_array)
print(" ii. Sort above array by second column ",end='\n')
sorted_array=array[np.argsort(array[:,1])]
print(sorted_array)
print("iii. Print max from axis 0 and min from axis 1",end='\n')
print("Axis 0 ",end='\n')
print(np.max(array,axis=0))
print("Axis 1 ",end='\n')
print(array)
print(np.min(array,axis=1))
print("iv. Delete col 2 and insert new Column numpy.array([[10,10,10]]) in its place ",end='\n')
array=np.delete(array,1,axis=1)
array=np.insert(array,1,[10,10,10],axis=1)
print(array)