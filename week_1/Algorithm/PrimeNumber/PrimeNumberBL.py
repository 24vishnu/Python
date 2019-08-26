'''
# ---------------------------------- prg-----------------------------------------------
# Prime_Number.py
# date : 26/08/2019
# Find given number is prime or not
'''

#method for find prime number
def prime(n):

    #Check base condition 1
    if n < 2 :
	    return False

    #Check base condition 2
    if n == 2:
    	return True

    i = 2
    while (i*i < n):
    	if(n%i == 0):
    		return False
    	i += 1

    return True