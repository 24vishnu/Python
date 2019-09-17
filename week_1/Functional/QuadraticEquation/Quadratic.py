"""
Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula

delta = b*b ­ 4*a*c
Root 1 of x = (­b + sqrt(delta))/(2*a)
Root 2 of x = (­b ­ sqrt(delta))/(2*a)
"""

import QuadraticBL as ob

# Take user input a, b and c
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

# call roots method
ob.roots(a, b, c)
