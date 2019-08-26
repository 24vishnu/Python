#import math package for use mathematical functions like (square function, root function and other)
import math

'''
Calculate the distance from given points a and b from origin 
using distance formula square root of [(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)]
here x2 and y2 are (0,0) and x1 and y1 are (a ,b) points
'''
def distance(a,b):
    return (round(math.sqrt(a*a + b*b),2))
