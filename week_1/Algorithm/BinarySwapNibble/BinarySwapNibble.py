import BinarySwapNibbleBL as ob
n = int(input("Enter a decimal value : "))
obj = ob.BaseConvertor()

if(n > 256):
	print("Please Enter decimal value less than 256 ")
else:
	print("Binary conversion of your number is : ",obj.toBinary(n))
	print("Swap nibble of your binary number is : ",obj.swapNibbles(obj.toBinary(n)))
	print("Decimal value after swaping of your binary number is : ",obj.toDecimal(obj.swapNibbles(obj.toBinary(n))))
