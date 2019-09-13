"""
Desc ­> takes a command­line argument N, asks you to think of a number
between 0 and N­1, where N = 2^n, and always guesses the answer with n
questions.

I/P ­> the Number N and then recursively ask true/false if the number is between
a high and low value

Logic ­> Use Binary Search to find the number

O/P ­> Print the intermediary number and the final answer
"""

import YourNumberBL

# Ask range of user number
N = int(input("Enter max range : "))

# find and print result
YourNumberBL.check(N)
