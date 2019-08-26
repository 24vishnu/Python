# ---------------------------------- prg-----------------------------------------------
# WindChill.py
# date : 26/08/2019
# Find the chill ness of wind 

import sys

class windChill:

    @staticmethod
    def calculate(t,v):

		#if tempreture and wind speed are not setisfied with question requirement then exit the program
	    if(t > 50 or (v > 120 or v < 3)):
	    	print(" your values are Not valid  ")
	    	sys.exit()

		#calulate result using formula given in question
	    w = 35.74 + 0.6215 + (0.4275*t - 35.75) * pow(v,0.16)

		#print result
	    print(w)