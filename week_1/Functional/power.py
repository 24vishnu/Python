n = int(input("Enter : "))

def myp(n):
	if(n == 0):
		return 1
	return 2 * myp(n-1)
print(myp(n))
