import sys
class windChill:
    @staticmethod
    def calculate(t,v):
	    if(t > 50 or (v > 120 or v < 3)):
	    	print(" your values are Not valid  ")
	    	sys.exit()
	    w = 35.74 + 0.6215 + (0.4275*t - 35.75) * pow(v,0.16)
	    print(w)