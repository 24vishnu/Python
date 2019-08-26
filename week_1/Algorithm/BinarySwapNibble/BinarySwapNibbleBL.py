class BaseConvertor:
    @staticmethod
    def dcimalToBinary(n):
        ans = ''
        while(n>0):
        	ans =str(n%2)+ans
        	n //= 2
        return ans

    @staticmethod
    def toBinary(n):
        res = [0]*8
        i = 7
        while(n>0):
            	res[i] = n%2
            	n //= 2
            	i -= 1
        ans = ''
        for i in range(8):
        	ans += str(res[i])
        return (ans)

    @staticmethod
    def swapNibbles(binary_value):
    	res = ''
    	res += binary_value[4:len(binary_value)]
    	res += binary_value[0:4]
    	return res

    @staticmethod
    def toDecimal(binary_value):
    	ans = 0
    	for i in range(len(binary_value)):
    		ans += (pow(2,(i))* int(binary_value[(7-i)]))
    	return ans