'''
Progeam for read the data from file and perfoming bubble sort
'''


import BubbleSortBl as ob

#Open file
with open("demo.txt") as f:
	data = f.read()

    #call bubble sort function
	ob.BSortingLogic(data)

#close file
f.close()
