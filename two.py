number=None
def _in():
    global number
    number=int(input("Enter a number "))
def print_pattern():
    for i in range(1,number+1):
        for j in range(1,number+2-i):
            print(j, end=' ')
        print()
    print()
if __name__=='__main__':
    _in()
    print_pattern()
