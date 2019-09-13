import DistancePointBl as ob

'''
Take two points say a and b from user 
'''
while True:
    point1 = (input("Enter the first point : "))
    # check user input is valid or not
    try:
        point1 = float(point1)
    except ValueError:
        print('Please enter the valid number : ', type(point1))
        continue
    break

while True:
    point2 = (input("Enter the first point : "))
    # check user input is valid or not
    try:
        point2 = float(point2)
    except ValueError:
        print('Please enter the valid number : ', type(point2))
        continue
    break
# pass these values (a, b) and call our distance method and get distance from origin (0,0) and print on screen
print(ob.distance(point1,point2))