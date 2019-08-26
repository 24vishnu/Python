
def prime(n):
    if(n < 2):
        return False
    if(n == 2):
        return True
    for i in range(2,n,1):
        if(n%i == 0):
            return False
    return True
def print_Prime_Factor(n):
    print('Prime factors of your number are following : ')
    for i in range(2,n):
        if(n%i == 0 and prime(i) == True):
            print(i,end=', ')
    print()