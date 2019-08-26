import orderListBL as ord_ll_obj

#--------------------------------------------------
obj = ord_ll_obj.singleLinkedList()

fileData = obj.readFileData()

print(fileData)
number_list = ord_ll_obj.wordToString(fileData)

for i in range(len(number_list)):
    obj.add_list(number_list[i])

obj.print_List()
print("Enter the element for search in list : ")
item = int(input())
if(obj.searchItem(item) == True):
    print("Your Item is present in list :")
    obj.removeItem(item)
else:
    print("Your Item is not present in list :")
    obj.add_list(item)
obj.print_List()
# print()
obj.writeFile()
# print()
#---------------------------------------------------
