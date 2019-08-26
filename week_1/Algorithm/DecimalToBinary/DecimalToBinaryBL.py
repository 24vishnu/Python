# ---------------------------------- prg-----------------------------------------------
# Decimal_To_Binary.py
# date : 26/08/2019
# Convert decimal to binary number

def toBinary(n):
    	
	res = ''

	while(n>0):
		res = str(n%2) + res
		n //= 2
	
	#return binary number as a string
	return res
 