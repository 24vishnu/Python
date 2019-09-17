"""
I/P ­> Take User Name as Input. Ensure UserName has min 3 char
Logic ­> Replace <<UserName>> with the proper name
O/P ­> Print the String with User Nam
"""

import ReplaceStringTemplateBL as ob

# take user input as string name
name = input("Enter Your name : ")

# replace given input string by calling replaceString method
name = ob.replaceString(name)

# print replaced string
print(name)
