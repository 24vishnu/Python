def isLeap(year):
    if(year%100 == 0):
        if(year%400 == 0):
            print("Yes! This is leap year")
        else:
            print("No! This is not leap year")
    elif(year%4 == 0):
        print("Yes! This is leap year")
    else:
        print("No! This is not leap year")