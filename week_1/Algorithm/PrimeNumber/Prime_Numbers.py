# program to print all prime number from  1 to  1000

import PrimeNumberBL as ob

for i in range(1,1000,1):
	if(ob.prime(i) == True):
		print(i,end=" ")

print()