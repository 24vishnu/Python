from math import sqrt
import cmath

def roots(a,b,c):
    delta = (b**2 - 4*a*c)
    if(delta > 0):
    	print("There are two root : {0} and {1}".format((-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a)))
    elif(delta == 0):
    	print("Root are equla : {0} and {1}".format((-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a)))
    else:
    	print("Root are imaginary : {0} and {1}".format((-b + cmath.sqrt(delta))/(2*a),(-b - cmath.sqrt(delta))/(2*a)))
