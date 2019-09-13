# ---------------------------------- prg-----------------------------------------------
# Decimal_To_Binary.py
# date : 26/08/2019
# Convert decimal to binary number


def toBinary(decimalNumber):
    binaryNumber = ''

    while decimalNumber > 0:
        binaryNumber = str(decimalNumber % 2) + binaryNumber
        decimalNumber //= 2

    for i in range(len(binaryNumber), 32, 1):
        binaryNumber = '0' + binaryNumber

    return binaryNumber
