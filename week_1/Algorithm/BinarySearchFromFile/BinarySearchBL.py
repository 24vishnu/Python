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
