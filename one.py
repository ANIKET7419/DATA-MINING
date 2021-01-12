
def in_():
    global  number
    number =int(input("Enter a number "))
def sum_():
    global number
    sum=0
    while number>0:
        t=number%10
        number=number//10
        sum+=t
    print(sum)
if __name__=='__main__':
    in_()
    sum_()