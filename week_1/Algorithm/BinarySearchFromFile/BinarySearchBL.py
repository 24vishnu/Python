# ---------------------------------- prg-----------------------------------------------
# bSearch_str_from_file,.py
# date : 26/08/2019
# Find the prime anagram and palindrome number


# binary search algorithm
def bnarySerch(all_values, search_num):
    i = 0
    j = len(all_values) - 1

    while i <= j:
        m = int(i + (j - i) / 2)

        if all_values[m] == search_num:
            return True

        elif all_values[m] < search_num:
            i = m + 1

        else:
            j = m - 1

    return False


# bubble sort algorithm
def bubbleSort(all_values):
    for i in range(0, len(all_values), 1):
        for j in range(0, len(all_values) - (i + 1), 1):

            if all_values[j] > all_values[j + 1]:
                t = all_values[j]
                all_values[j] = all_values[j + 1]
                all_values[j + 1] = t

    return all_values


# insertion sort Algorithm
def insertionSort(all_values):
    for i in range(1, len(all_values), 1):

        k = all_values[i]
        j = i - 1

        while j >= 0 and k < all_values[j]:
            all_values[j + 1] = all_values[j]
            j -= 1

        all_values[j + 1] = k

    return all_values
