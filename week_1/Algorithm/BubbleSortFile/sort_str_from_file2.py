"""
Program for read the data from file and performing bubble sort
"""

import BubbleSortBl as ob

# read file and take data into string
data = ob.read_file()

# convert file data into list of words
list_data = ob.convert_words_list(data)

# call bubble sort function
print(ob.bubbleSort(list_data))
