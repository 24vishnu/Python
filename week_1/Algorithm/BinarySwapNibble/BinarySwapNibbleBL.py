# ---------------------------------- prg-----------------------------------------------
# BinarySwapNibble.py
# date : 26/08/2019
# we are convert the decimal to binary and binary to decimal and also swap the nibble bits 


class BaseConvertor:

    # Decimal to binary conversion method
    @staticmethod
    def dcimalToBinary(number):

        binary_value = ''

        while number > 0:
            binary_value = str(number % 2) + binary_value
            number //= 2

        return binary_value

    # This method convert decimal to binary only less the or equal to 8 bit size binary representation
    @staticmethod
    def toBinary(decimal_value):
        binary_value = [0] * 8
        i = 7
        while decimal_value > 0:
            binary_value[i] = decimal_value % 2
            decimal_value //= 2
            i -= 1

        binary_value_result = ''
        for i in range(8):
            binary_value_result += str(binary_value[i])

        return binary_value_result

    # Method for swap nibble
    @staticmethod
    def swapNibbles(binary_value):
        answer = ''
        answer += binary_value[4:len(binary_value)]
        answer += binary_value[0:4]

        return answer

    # method for convert binary to decimal value
    @staticmethod
    def toDecimal(binary_value):
        decimal_value = 0
        for i in range(len(binary_value)):
            decimal_value += (pow(2, i) * int(binary_value[(7 - i)]))

        return decimal_value
