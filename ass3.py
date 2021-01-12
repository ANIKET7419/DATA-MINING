size=int(input("Enter size"))
li=[]
for i in range(0,size):
    li.append(int(input()))
print("Reversed list : -> ")
lis_=[]
for i in range(len(li)-1,-1,-1):
        lis_.append(li[i])
print(lis_)