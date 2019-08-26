import DayOfWeekBL as ob
day_list = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
year = int(input("Enter year : "))
month = int(input("Enter month : "))
day = int(input("Enter day : "))
print(day_list[ob.dayOfWeek(year, month, day)])