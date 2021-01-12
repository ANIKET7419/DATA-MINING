number=int(input("Enter count "))
marks=[]
print("Enter marks ")
for i in range(0,number):
    marks.append(float(input()))
dictionary={}
for x in marks:
    if dictionary.__contains__(x):
        dictionary[x]=dictionary.get(x)+1
    else:
        dictionary[x]=1
print(dictionary)

