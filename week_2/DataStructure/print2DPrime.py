import math
prim = []

class primeIn2D:
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
        stre = ''
        p = 0
        stre = str(p)+' to '
        p += 100
        stre +=  str(p)+'    '
          
        temp_list = []
        temp_list.append(stre)
        for i in range(1,1000):
            if(primeIn2D.prime(i) == True):
                temp_list.append(i)
            if i % 100 == 0:
                stre = ''
                stre = str(p)+' to '
                p += 100
                stre +=  str(p)+ '    '

                prim.append(temp_list)
                temp_list = []
                temp_list.append(stre)
        prim.append(temp_list)

primeIn2D.primeList()
for i in range(len(prim)):
    print(prim[i])
