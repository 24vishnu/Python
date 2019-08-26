'''
I/P ­> Year, ensure it is a 4 digit number.

Logic ­> Determine if it is a Leap Year.

O/P ­> Print the year is a Leap Year or not.
'''

import Leap_YearBL as ob

# take input from the user as year 
yy = int(input("Enter Your year : "))

#call method and check given year is leap year or not
ob.isLeap(yy)