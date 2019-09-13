"""
Write Binary.java to read an integer as an Input, convert to Binary using toBinary
function and perform the following functions.

i. Swap nibbles and find the new number.
ii. Find the resultant number is the number is a power of 2.

A nibble is a four­bit aggregation, or half an octet. There are two nibbles in a byte.
"""

import BinarySwapNibbleBL as ob

# take decimal value from user
n = int(input("Enter a decimal value : "))

obj = ob.BaseConvertor()

if n > 256:
    print("Please Enter decimal value less than 256 ")
else:
    print("Binary conversion of your number is : ", obj.toBinary(n))
    print("Swap nibble of your binary number is : ", obj.swapNibbles(obj.toBinary(n)))
    print("Decimal value after shaping of your binary number is : ", obj.toDecimal(obj.swapNibbles(obj.toBinary(n))))
