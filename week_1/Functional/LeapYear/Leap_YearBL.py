# ---------------------------------- prg-----------------------------------------------
# Leap_Year.py
# date : 26/08/2019
# find given year is leap or not


def isLeap(year):
    # if year is fully divide by 400 then it is leap year
    # and if it is divided by 4 but not 100 then it also leap year
    # otherwise not leap year
    if year % 100 == 0:

        if year % 400 == 0:
            return True
        else:
            return False

    elif year % 4 == 0:
        return True
    else:
        return False
