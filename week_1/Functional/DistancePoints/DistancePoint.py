import DistancePointBl as ob\

'''
Take two points say a and b from user 
'''
a = int(input("Enter the first point : "))
b = int(input("Enter the second point : "))

# pass these values (a, b) and call our distance method and get distance from origin (0,0) and print on screen
print(ob.distance(a,b))