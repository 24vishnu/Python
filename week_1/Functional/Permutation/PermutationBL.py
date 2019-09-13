# ---------------------------------- prg-----------------------------------------------
# Permutation.py
# date : 26/08/2019
# Find permutation of given string


# this method call the recursive function with pass input value and stating 0 and end length of input value(string)
def call_recursive(string):
    n = len(string)
    list_convert = list(string)
    recursive_permutation(list_convert, 0, n - 1)


# join method is use for join all character and make a string and return
def printValue(value):
    return ''.join(value)


# =================================================\
# this method is perform iterative operation
def iterative_permutation(value):
    # convert all siring value as character list
    list_convert = list(value)

    # assign all permuted value in answer list by using pop method of list
    answer = [list_convert.pop()]

    while len(list_convert) != 0:
        character = list_convert.pop()
        new_list = []

        for w in answer:
            for i in range(len(w) + 1):
                new_list.append(w[:i] + character + w[i:])

        answer = new_list
    return answer


# =================================================
# this method is perform recursive function call operation

# Empty list to store all permuted values
# recursive_list = []

def recursive_permutation(value, left, right):
    if left == right:
        # recursive_list.append(''.join(value))
        print(printValue(value), end=' ')
    else:
        for i in range(left, right + 1):
            value[left], value[i] = value[i], value[left]
            recursive_permutation(value, left + 1, right)
            value[left], value[i] = value[i], value[left]

# ===================================================
