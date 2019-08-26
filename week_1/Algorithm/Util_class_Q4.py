# class util:
# binary search 
def bnarySerch(ll,num):
	i = 0
	j = len(ll)-1
	while i <= j:
		m = int(i+(j-i)/2)
		if(ll[m] == num):
			return True
		elif ll[m] < num:
			i = m+1
		else:
			j = m-1
	return False
	
#bubble sort 
def bubbleSort(ll):
	for i in range(0,len(ll),1):
		for j in range(0,len(ll)-(i+1),1):
			if(ll[j] > ll[j+1]):
				t = ll[j]
				ll[j] = ll[j+1]
				ll[j+1] = t
	return ll			
	
#insertion sort 
def insertionSort(ll):
	for i in range(1,len(ll),1):
		k = ll[i]
		j = i-1
		while(j >= 0 and k < ll[j]):
			ll[j+1] = ll[j]
			j -= 1
		ll[j+1] = k
	return ll
	
# Day of week of year
def dayOfWeek(yy,mm,dd):
	y0 = yy - (14 - mm) // 12
	x = y0 + y0//4 - y0//100 + y0//400
	m0 = mm + 12*((14 - mm)//12) - 2
	d0 = (dd + x + (31*m0)//12 ) % 7
	return d0-1

# Tempreturn convertion function
def temperaturConversion(tmp, choice):
	if(choice == 1):
		return (tmp*9/5)+32
	else:
		return (tmp - 32)*(5/9)

# calculate monthly salary
def monthlyPayment(P, Y, R):
	n = 12*Y
	r = R/(12*100)
	result = (int)((P*r)/(1 - (1+r)**(-n)))
	print(result)

# mll = [3,6,8,1,0,5,7,2,9]
# mll = ['vis','abc','xyz','pqr','lmn','aaa','abc','bbc','bcb']
# print(bubbleSort(mll))
# print(bnarySerch(mll,18))
# print(insertionSort(mll))
	