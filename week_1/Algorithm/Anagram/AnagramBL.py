# ---------------------------------- prg-----------------------------------------------
# Anagram.py
# date : 26/08/2019
# Find two string are anagram or not

def isAnagram(str1,str2):

    li = [0]*26

    #Find the frequency of first string by add one 
    for i in range(len(str1)):
    	li[ord(str1[i])-97] += 1

    #Find the frequency of first string by substract one     
    for i in range(len(str2)):
    	li[ord(str2[i])-97] -= 1

    #check any index of list have any value except 0 (zero)
    for i in range(26):
    	if(li[i] != 0):
    		return False

    return True
    # print('Yes! strings are Anagram')