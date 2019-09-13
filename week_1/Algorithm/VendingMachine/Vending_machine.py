"""
Desc ­> There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
returned by Vending Machine. Write a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change

I/P ­> read the Change in Rs to be returned by the Vending Machine

Logic ­> Use Recursion and check for largest value of the Note to return change
to get to minimum number of Notes.

O/P ­> Two Outputs ­ one the number of minimum Note needed to give the
change and second list of Rs Notes that would given in the Change
"""

import VendingMachineBL as ob

my_money = int(input("How many you have : "))

print('Total changes(Notes) are :', ob.change(my_money))
