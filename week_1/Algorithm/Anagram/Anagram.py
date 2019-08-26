'''
Desc ­> One string is an anagram of another if the second is simply a
rearrangement of the first. For example, 'heart' and 'earth' are anagrams...

I/P ­> Take 2 Strings as Input such abcd and dcba and Check for Anagrams

O/P ­> The Two Strings are Anagram or not....
'''

import AnagramBL as ob

# take two string from user 
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

#call the function and check these are anagram or not
if(ob.isAnagram(str1,str2) == True):
	print("Yes this is anagram")
else:
	print("No this is not anagram")

