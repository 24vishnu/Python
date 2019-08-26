# ---------------------------------- prg-----------------------------------------------
# ExtendedPrime2D.py
# date : 26/08/2019
# print the prime nuimber amd anagram number in 2 D


import math

prim = []
ana_G = []
not_ana_G = []

class ExtendePrimeClass:

    #prime method
    @staticmethod
    def prime(n):
        #Base conditions
        if n < 2:
            return False

        if n == 2:
            return True

        for i in range(2,int(math.sqrt(n))):
            if n%i == 0:
                return False

        return True

#creatre a list of prime numbers
    @staticmethod
    def primeList():
        for i in range(1,1000):
            if(ExtendePrimeClass.prime(i) == True):
                prim.append(i)

#create a list of anagram number   
    @staticmethod
    def anagram(a,b):
        x = list(str(a))
        y = list(str(b))
        x.sort()
        y.sort()
        return x == y



ExtendePrimeClass.primeList()

for i in range(len(prim)):
    for j in range(len(prim)):
        if prim[i] is not prim[j]:
            if(ExtendePrimeClass.anagram(prim[i],prim[j]) == True):
                if prim[i] not in ana_G:
                    ana_G.append(prim[i])
                if prim[j] not in ana_G:
                    ana_G.append(prim[j])

for i in range(len(prim)):
    if prim[i] not in ana_G:
        not_ana_G.append(prim[i])
