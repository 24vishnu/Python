
# ---------------------------------- prg-----------------------------------------------
# TempretureConverstion.py
# date : 26/08/2019
# Convert the tempreture Celsius to Fahrenheit and Fahrenheit to Celsius



# Tempreturn convertion function
def temperaturConversion(tmp, choice):
	if(choice == 1):
		return (tmp*9/5)+32
	else:
		return (tmp - 32)*(5/9)