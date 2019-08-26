# calculate monthly salary
def monthlyPayment(P, Y, R):
	n = 12*Y
	r = R/(12*100)
	result = (int)((P*r)/(1 - (1+r)**(-n)))
	print(result)
