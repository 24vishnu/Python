import BinarySearchBL as ob

with open("demo.txt") as f:
	data = f.read()
word = ""
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
f.close()