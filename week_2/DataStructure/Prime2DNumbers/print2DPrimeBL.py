# ---------------------------------- prg-----------------------------------------------
# priem2DPrime.py
# date : 26/08/2019
# print the prime number in two dimension 

import math

prim = []


class primeIn2D:

    # check number is prime or not
    @staticmethod
    def prime(n):
        if n < 2:
            return False

        if n == 2:
            return True

        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

    # prime list in 2D
    @staticmethod
    def primeList():
        p = 0
        num_range = str(p) + ' to '
        p += 100
        num_range += str(p) + '      '

        temp_list = [num_range]

        for i in range(1, 1000):
            if primeIn2D.prime(i):
                temp_list.append(i)

            if i % 100 == 0:
                num_range = str(p) + ' to '
                p += 100
                num_range += str(p) + '    '

                prim.append(temp_list)
                temp_list = [num_range]

        prim.append(temp_list)
