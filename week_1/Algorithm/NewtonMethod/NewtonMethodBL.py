class newtonSqrt:
    @staticmethod
    def my_Sqrt(n):
    	eps = 1e-15
    	res = n
    	while (abs(res - (n/res)) > eps*res):
    		res = (n/res + res) / 2.0
    	return res
