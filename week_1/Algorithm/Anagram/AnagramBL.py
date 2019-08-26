def isAnagram(str1,str2):
    li = [0]*26
    for i in range(len(str1)):
    	li[ord(str1[i])-97] += 1

    for i in range(len(str2)):
    	li[ord(str2[i])-97] -= 1

    for i in range(26):
    	if(li[i] != 0):
    		return False
            # print('Not Anagram ')
            # return
    return True
    # print('Yes! strings are Anagram')