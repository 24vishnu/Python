# Write static functions to return all permutation of a String using iterative method and
# Recursion method. Check if the arrays returned by two string functions are equal.

import PermutationBL as obj

# take user input
string = input("Enter your string : ")

# call recursive function for get permutaition of input
print('\nfollowing output using recursive method')
obj.call_recursive(string)

# call iterative function for get permutaition of input
print('\n\nfollowing output using iterative method')
print(obj.iterative_permutation(string))
	