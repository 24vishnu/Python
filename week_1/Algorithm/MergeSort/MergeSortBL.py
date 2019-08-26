#Following we define merge sort function this will devide our list into two part 
def merge_part(ll):
    if(len(ll) > 1):

        mid = (len(ll))//2
        
        l_list = ll[:mid]
        r_list = ll[mid:]
        merge_part(l_list)
        merge_part(r_list)
        sort_now(ll,l_list,r_list)

def sort_now(list_object, l_list, r_list):

		i = j = index = 0

		while(i < len(l_list) and j < len(r_list)):
			if(l_list[i] < r_list[j]):
				list_object[index] = l_list[i]
				i += 1
			else:
				list_object[index] = r_list[j]
				j += 1
			index += 1
		while i < len(l_list):
			list_object[index] = l_list[i]
			index += 1
			i += 1
		while j < len(r_list):
			list_object[index] = r_list[j]
			index += 1
			j += 1
