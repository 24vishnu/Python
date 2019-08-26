#program is take the data from file and and sort using insertion sort

import SortingFunctionsBL as ob

#Open the file 
# f=open("demo.txt",'r')
with open("demo.txt") as f:

	#read the data
	data = f.read()
	
	#sort the data
	ob.sortinLogic(data)
	
#close the file
f.close()