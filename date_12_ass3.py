number=int(input("Enter count "))
names=[]
print("Enter names ")
for i in range(0,number):
    names.append((input()))
dic={}
for x in names:
    if not dic.__contains__(x):
      dic[x]=len(x)
print(dic)