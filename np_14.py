import numpy as np
len1=int(input("Enter length of array 1 "))
print("Enter elements of array 1 ",end='\n')
array1=[]
for i in range(0,len1):
    array1.append(int(input()))
array1=np.array(array1)
print("Minimum",end='\n')
print(np.min(array1))
print("Maximum",end='\n')
print(np.max(array1))
print("Mean")
print(np.mean(array1))
print("Median")
print(np.median(array1))
print("SD")
print(np.std(array1))
array1=np.sort(array1)
print("5th per..")
index=0.05*len(array1)
if int(index)==index:
    print(array1[index])
else:
    print(array1[int(index)])
print("95th per..")
index=0.95*len(array1)
if int(index)==index:
    print(array1[index])
else:
    print(array1[int(index)])
map={}
for i in array1:
    if map.__contains__(i):
        map[i]=map[i]+1
    else:
        map[i]=1
unique=[]
for i,j in map.items():
   if j==1:
       unique.append(i)
print("Unique Values :")
print(unique)
print("Count of unique values :")
print(len(unique))
m=0
most_fre=[]
for i,j in map.items():
    if j>m:
        m=j
for i,j in map.items():
    if j==m:
        most_fre.append(i)
print("Most Frequent Data ... ")
print(most_fre)





