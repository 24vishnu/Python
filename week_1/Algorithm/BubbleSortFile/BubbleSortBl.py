# ---------------------------------- prg-----------------------------------------------
# sort_str_from_file2.py
# date : 26/08/2019
# sort the data using bubble sort algo and find requred time to sort data


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


# befor sorting we convert string as a list of every word
def BSortingLogic(data):
	    	
	word = ""
	string = data.strip().strip('.').strip(',')
	list_obj = []


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