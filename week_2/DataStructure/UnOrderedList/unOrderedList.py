import UnOrderedListBL as UOL_obj
#--------------------------------------------------
ll_fun_obj = UOL_obj.listFunctions()

fileData = str(UOL_obj.listFunctions().readFileData())

print(fileData)

word_list = UOL_obj.wordToString(fileData)
for i in range(len(word_list)):
    ll_fun_obj.add_list(word_list[i])
ll_fun_obj.print_List()

print("\nEnter the element for search in list : ")
item = input()
if(ll_fun_obj.searchItem(item) == True):
    print("Your Item is present in list :")
    ll_fun_obj.removeItem(item)
else:
    print("Your Item is not present in list :")
    ll_fun_obj.add_list(item)
ll_fun_obj.print_List()
print()
ll_fun_obj.writeFile()
print()