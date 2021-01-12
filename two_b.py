number=None
def _in():
    global number
    number=int(input("Enter a number "))
def print_pattern():
    for i in range(number,0,-1):
        for j in range(number,i-1,-1):
            print(j, end=' ')
        print()
    print()
if __name__=='__main__':
    _in()
    print_pattern()
