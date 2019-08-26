
# ---------------------------------- prg-----------------------------------------------
# sort_str_from_file.py
# date : 26/08/2019
# Sort the data using insertion sort algorithm and print time used by algorithm


import time

#insertion sort 
def insertionSort(ll):
    	
	startTime = time.time()

	for i in range(1,len(ll),1):
		k = ll[i]
		j = i-1

		while(j >= 0 and k < ll[j]):
			ll[j+1] = ll[j]
			j -= 1

		ll[j+1] = k

	print('Time : ',round(time.time()-startTime,10))	
	return ll

# conver a string into a list of words
def sortinLogic(data):

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
    print(insertionSort(list_obj))