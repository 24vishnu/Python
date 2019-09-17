# ---------------------------------- prg-----------------------------------------------
# Quadratic.py
# date : 26/08/2019
# Find the root of equation

from math import sqrt
import cmath


# roots method to find root of equation
def roots(a, b, c):
    # calculate delta (b^2 - 4ac)
    delta = (b ** 2 - 4 * a * c)

    # real roots
    if delta > 0:
        print("There are two root : {0} and {1}".format((-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)))
    # Equal roots
    elif delta == 0:
        print("Root are equal : {0} and {1}".format((-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)))
    # imaginary root
    else:
        print("Root are imaginary : {0} and {1}".format((-b + cmath.sqrt(delta)) / (2 * a),
                                                        (-b - cmath.sqrt(delta)) / (2 * a)))
