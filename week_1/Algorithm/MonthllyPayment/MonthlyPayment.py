#program to find the monthly payment 

import MonthlyPaymentBL as ob

# take the input as priciple, time in year and rate of interest 
Priciple = int(input("Enter principal : "))
Year = int(input("Enter time (in year) : "))
Rate = int(input("Enter rate interest : "))

ob.monthlyPayment(Priciple,Year,Rate)

