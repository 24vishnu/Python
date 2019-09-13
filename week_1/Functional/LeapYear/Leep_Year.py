"""
I/P ­> Year, ensure it is a 4 digit number.

Logic ­> Determine if it is a Leap Year.

O/P ­> Print the year is a Leap Year or not.
"""

import Leap_YearBL as ob

# take input from the user as year
while True:
    year = input("Enter Your year : ")
    # check user input is valid or not
    try:
        year = int(year)
    except ValueError:
        print('Please enter the valid year : ', type(year))
        continue
    if year >= 0:
        break
    else:
        print('Please enter positive number. ')


# call method and check given year is leap year or not
if ob.isLeap(year):
    print("Yes! This is leap year")
else:
    print("No! This is not leap year")
