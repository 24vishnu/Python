# ---------------------------------- prg-----------------------------------------------
# Calender.py
# date : 26/08/2019
# Proit the calender of given date


import sys

#name of day list of a week
day = ['S ','M ','T ','W ','Th','F ','SA']

#list of number of days in list
mon = [31,28,31,30,31,30,31,31,30,31,30,31]

#Name oof month
mon_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

month = []*7

class MyCalender:

    #Calculate start day of month
    @staticmethod
    def startDay(yy,mm,dd):

        y0 = yy - (14 - mm) // 12
        x = y0 + y0//4 - y0//100 + y0//400
        m0 = mm + 12*((14 - mm)//12) - 2
        d0 = (dd + x + (31*m0)//12 ) % 7

        return d0

    #check given year is leap year or not
    @staticmethod
    def leapYear(yy):
        if (yy % 100 == 0 and not yy%400==0):
            return False

        if(yy%4 == 0):
            return True

        return False

    #method for create a empty calender
    @staticmethod
    def createCal():
        for i in range(7):
            month.append([])

        for i in range(7):
            month[0].append(day[i])

    #update calender according to given date
    @staticmethod
    def updateCale(start, current_Month):
        k = 0

        for i in range(7):
            if i < start:
                month[1].append('  ')

            else:
                k += 1

                if(k < 10):
                    month[1].append(' '+str(k))

                else:
                    month[1].append(k)

        for i in range(2,7):
            j = 0
            while(j < 7):
                j += 1
                k += 1 

                if(k > mon[current_Month-1]):
                    month[i].append('  ')

                else:
                    if(k < 10):
                        month[i].append(' '+str(k))

                    else:
                        month[i].append(k)

    #Method for display the calender
    @staticmethod
    def displayCale():

        for j in range(7):
            for i in range(7):
                print(month[j][i],end = '  ')

            print()

#make a method of user input and and according to given input we display the calender
def userInput(year, month):
    if(month < 1 or month > 12):
        print('You Entered incorrect month : ')
        sys.exit(0)

    start = MyCalender.startDay(year,month,1)
    if(MyCalender.leapYear(year) == True):
        mon[1] = 29

    print('\n\n------------------------------')
    print('Python Calender: ',month,year)
    print(mon_name[month-1],year)
    print('------------------------------\n')
    print(mon_name[month-1],year)
    MyCalender.createCal()
    MyCalender.updateCale(start,month)
    MyCalender.displayCale()