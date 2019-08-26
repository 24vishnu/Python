import time
#bubble sort 
def bubbleSort(ll):
	startTime = time.time()
	for i in range(0,len(ll),1):
		for j in range(0,len(ll)-(i+1),1):
			if(ll[j] > ll[j+1]):
				t = ll[j]
				ll[j] = ll[j+1]
				ll[j+1] = t
				
	print('Time : ',round(time.time()-startTime,10))	
	return ll			
def BSortingLogic(data):
	word = ""
	string = data.strip().strip('.').strip(',')
	list_obj = []
	# print(string)
	for i in range(len(string)):
		if(string[i] == ' '):
			if(len(word) > 0):
				list_obj.append(word)
				word = ""
		elif((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z')):
			word += string[i]
	if(len(word) > 0):
		list_obj.append(word)

	print("\n")
	print(bubbleSort(list_obj))