def toBinary(n):
	res = ''
	while(n>0):
		res = str(n%2) + res
		n //= 2
	return res
 