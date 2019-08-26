import SortingFunctionsBL as ob

# f=open("demo.txt",'r')
with open("demo.txt") as f:
	data = f.read()
	ob.sortinLogic(data)
# word = ""
# string = data.strip().strip('.').strip(',')
# list_obj = []
# # print(string)
# for i in range(len(string)):
# 	if(string[i] == ' '):
# 		if(len(word) > 0):
# 			list_obj.append(word)
# 			word = ""
# 	elif((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z')):
# 		word += string[i]
# if(len(word) > 0):
# 	list_obj.append(word)

# print("\n")
# print(ob.insertionSort(list_obj))
f.close()