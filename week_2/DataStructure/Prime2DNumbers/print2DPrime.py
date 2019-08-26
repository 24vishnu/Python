'''
Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0­100,
100­200, and so on. While the second dimension represents the prime numbers in
that range
'''

import print2DPrimeBL as prim_obj

prim_obj.primeIn2D.primeList()

#print prime number in 2 D formate
for i in range(len(prim_obj.prim)):
    print(prim_obj.prim[i])
