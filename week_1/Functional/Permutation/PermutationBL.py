# # class Permutation:

def call_iterative(string):
    n = len(string)
    list_convert = list(string)
    ricursive_permutation(list_convert, 0, n-1)
    
def printValue(value):
	return ''.join(value)
#=================================================
def iterative_permutation(value):
	list_convert = list(value)
	answer = [list_convert.pop()]
	while(len(list_convert) != 0):
		charcter = list_convert.pop()
		new_list = []
		for w in answer:
			for i in range(len(w)+1):
				new_list.append(w[:i] + charcter + w[i:])
		answer=new_list
	return answer
#=================================================
recursive_list = []
def ricursive_permutation(value,left,rigth):
	if(left == rigth):
		# recursive_list.append(''.join(value))
		print(printValue(value),end=' ')
	else:
		for  i in range(left,rigth+1):
			value[left], value[i] = value[i],value[left]
			ricursive_permutation(value, left+1, rigth)
			value[left],value[i] = value[i],value[left]

#===================================================
