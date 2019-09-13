# ---------------------------------- prg-----------------------------------------------
# merge_Sort.py
# date : 26/08/2019
# implement the merge sort algorithm


# Following we define merge sort function this will devide our list into two part
def merge_part(values):
    if len(values) > 1:
        mid = (len(values)) // 2

        l_list = values[:mid]
        r_list = values[mid:]

        merge_part(l_list)
        merge_part(r_list)
        sort_now(values, l_list, r_list)


# this method is use for sort the data and merge
def sort_now(list_object, l_list, r_list):
    i = j = index = 0

    # sort both list data
    while i < len(l_list) and j < len(r_list):
        if l_list[i] < r_list[j]:
            list_object[index] = l_list[i]
            i += 1

        else:
            list_object[index] = r_list[j]
            j += 1
        index += 1

    # add remaining left list data
    while i < len(l_list):
        list_object[index] = l_list[i]
        index += 1
        i += 1

    # add remaining right list data
    while j < len(r_list):
        list_object[index] = r_list[j]
        index += 1
        j += 1
