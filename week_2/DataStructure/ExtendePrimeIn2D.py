import math
prim = []
ana_G = []
not_G = []
class ExtendePrimeIn2D:
    @staticmethod
    def prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2,int(math.sqrt(n))):
            if n%i == 0:
                return False
        return True

    @staticmethod
    def primeList():
        for i in range(1,1000):
            if(ExtendePrimeIn2D.prime(i) == True):
                prim.append(i)
           
    @staticmethod
    def anagram(a,b):
        x = list(str(a))
        y = list(str(b))
        x.sort()
        y.sort()
        return x == y



ExtendePrimeIn2D.primeList()
for i in range(len(prim)):
    for j in range(len(prim)):
        if prim[i] is not prim[j]:
            if(ExtendePrimeIn2D.anagram(prim[i],prim[j]) == True):
                if prim[i] not in ana_G:
                    ana_G.append(prim[i])
                if prim[j] not in ana_G:
                    ana_G.append(prim[j])

for i in range(len(prim)):
    if prim[i] not in ana_G:
        not_G.append(prim[i])

jbnf = []
jbnf.append(ana_G)
jbnf.append(not_G)
print(jbnf)
# print('Anagram List : ',ana_G)
# print('Other numbers : ',not_G)

# for i in range(len(prim)):
# print(prim)
