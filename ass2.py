size=int(input("Enter size"))
li=[]
for i in range(0,size):
    li.append(int(input()))
print("After removing duplicate elements ")
lis_=[]
for i in li:
    if  i not in lis_:
        lis_.append(i)
print(lis_)