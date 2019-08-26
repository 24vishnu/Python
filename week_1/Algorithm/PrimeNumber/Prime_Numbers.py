import PrimeNumberBL as ob

for i in range(1,1000,1):
	if(ob.prime(i) == True):
		print(i,end=" ")
print()