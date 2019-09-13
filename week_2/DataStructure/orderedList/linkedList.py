"""
Desc ­> Read .a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position

I/P ­> Read from file the list of Numbers and take user input for a new number

Logic ­> Create a Ordered Linked List having Numbers in ascending order.

O/P ­> The List of Numbers to a File.
"""

import orderListBL as ord_ll_obj

# --------------------------------------------------
obj = ord_ll_obj.singleLinkedList()

# take the file data into a string
fileData = obj.readFileData()

print(fileData)
# convert all sting into a list of number
number_list = ord_ll_obj.wordToString(fileData)

# Convert list into linked list
for i in range(len(number_list)):
    obj.add_list(number_list[i])

obj.print_List()

# take user input to search a number into list
print("Enter the element for search in list : ")
item = int(input())

# if number is present the delete that number
if obj.searchItem(item):
    print("Your Item is present in list :")
    obj.removeItem(item)

# If not present then add into list and update file
else:
    print("Your Item is not present in list :")
    obj.add_list(item)

obj.print_List()
# print()
obj.writeFile()
# print()
# ---------------------------------------------------
