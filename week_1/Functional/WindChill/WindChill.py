'''
Write a program WindChill.java that takes two double command­line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab.
Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
the National Weather Service defines the effective temperature (the wind chill) to
be:
		w = 35.74 + 0.6215 + (0.4275*t - 35.75) * pow(v,0.16)
		
Note : the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
'''
import WindChillBL as ob

class windChill:
    	
    #takre user input as t tempreture and v wind speed
	t = float(input("Enter temperature : "))
	v = float(input("Enter wind speed : "))

	#find result by calling calculate method
	ob.windChill.calculate(t,v)