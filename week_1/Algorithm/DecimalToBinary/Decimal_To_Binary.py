'''
Program for conver decimal to binary representation
'''

import DecimalToBinaryBL as ob

#Take decimal number from user
n = int(input("Enter a decimal value : "))

#print binary number of decimal number
print(ob.toBinary(n))