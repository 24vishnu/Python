import TempretureConversionBL as ob

choice = int(input("Enter \n1 for Celsius to Fahrenheit \n2 for Fahrenheit to Celsius: "))
if(choice == 1):
	cf = float(input("Enter temperature in Celsius : "))
	print(round(ob.temperaturConversion(cf,choice),2),"°F")

else:
	fc = float(input("Enter temperature in Fahrenheit : "))
	print(round(ob.temperaturConversion(fc,choice),2),"°C")
