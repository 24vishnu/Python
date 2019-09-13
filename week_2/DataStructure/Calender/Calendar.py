"""
Write a program Calendar.java that takes the month and year as command­line
arguments and prints the Calendar of the month. Store the Calendar in an 2D Array,
the first dimension the week of the month and the second dimension stores the day
of the week.
"""

import CalenderBL as cal_obj

month = int(input('Enter month : '))
year = int(input('Enter year : '))

cal_obj.userInput(year, month)
