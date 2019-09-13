# ---------------------------------- prg-----------------------------------------------
# Prime_factor.py
# date : 26/08/2019
# find the prime factors

import math


# method to check number is prime or not
def prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    root_value = math.sqrt(n)

    for i in range(2, root_value + 1, 1):
        if n % i == 0:
            return False

    return True


# Method for find prime factor
def print_Prime_Factor(n):
    print('Prime factors of your number are following : ')

    for i in range(2, n):
        if n % i == 0 and prime(i) == True:
            print(i, end=', ')

    print()
