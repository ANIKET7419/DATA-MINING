
string=input("Enter String ")
if( len(string)==0):
    exit(100)

char =string[0]
result=None
if char=='a'  or char=='e' or char=='i'or char=='o'or char=='u':
    result=string+'hay'
else :
    result=string[1:]+char+'ay'
print("Result is ",result)