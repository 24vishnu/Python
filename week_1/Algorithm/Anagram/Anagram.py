import AnagramBL as ob
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

# ob.isAnagram(str1,str2)
if(ob.isAnagram(str1,str2) == True):
	print("Yes this is anagram")
else:
	print("No this is not anagram")

