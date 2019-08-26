'''
To the Util Class add temperaturConversion static function, given the temperature
in fahrenheit as input outputs the temperature in Celsius or viceversa using the
formula
Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
'''

import TempretureConversionBL as ob

choice = int(input("Enter \n1 for Celsius to Fahrenheit \n2 for Fahrenheit to Celsius: "))

if(choice == 1):
	cf = float(input("Enter temperature in Celsius : "))
	print(round(ob.temperaturConversion(cf,choice),2),"°F")

else:
	fc = float(input("Enter temperature in Fahrenheit : "))
	print(round(ob.temperaturConversion(fc,choice),2),"°C")
