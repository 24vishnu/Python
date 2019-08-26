'''
Desc ­> Read in a list of words from File. Then prompt the user to enter a word to
search the list. The program reports if the search word is found in the list.

I/P ­> read in the list words comma separated from a File and then enter the word
to be searched

Logic ­> Use Arrays to sort the word list and then do the binary search

O/P ­> Print the result if the word is found or not
'''

import BinarySearchBL as ob

#open the file using constaxt maneger (with)
with open("demo.txt") as f:
	#read the all data from file 
	data = f.read()

word = ""

#Skip the space start and end soace and comma and full stop sign
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

sorted_list = ob.bubbleSort(list_obj)
print(sorted_list)

search_word = input("Enter the word for search in the list : ")

print(ob.bnarySerch(sorted_list, search_word))

#close the fileS
f.close()