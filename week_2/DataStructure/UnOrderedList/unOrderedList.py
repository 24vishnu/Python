"""
Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file

I/P ­> Read from file the list of Words and take user input to search a Text

Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
Object. Each node object must hold at least two pieces of information. One ref to
the data field and second the ref to the next node object.

O/P ­> The List of Words to a File
"""

import UnOrderedListBL as UOL_obj

# --------------------------------------------------
ll_fun_obj = UOL_obj.listFunctions()

fileData = str(UOL_obj.listFunctions().readFileData())

print(fileData)

# ADD the data into linked list word by word
word_list = UOL_obj.wordToString(fileData)
for i in range(len(word_list)):
    ll_fun_obj.add_list(word_list[i])

# print linked list
ll_fun_obj.print_List()

# take the input form user to search the word
print("\nEnter the element for search in list : ")
item = input()

# If word present then delete the word
if ll_fun_obj.searchItem(item):
    print("Your Item is present in list :")
    ll_fun_obj.removeItem(item)

# Else word not presernt then add the word into file and list
else:
    print("Your Item is not present in list :")
    ll_fun_obj.add_list(item)

ll_fun_obj.print_List()
print()
ll_fun_obj.writeFile()
print()
