import sys

day = ['S ','M ','T ','W ','Th','F ','SA']
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
mon_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = []*7
class MyCalender:
    @staticmethod
    def startDay(yy,mm,dd):
        y0 = yy - (14 - mm) // 12
        x = y0 + y0//4 - y0//100 + y0//400
        m0 = mm + 12*((14 - mm)//12) - 2
        d0 = (dd + x + (31*m0)//12 ) % 7
        return d0

    @staticmethod
    def leapYear(yy):
        if (yy % 100 == 0 and not yy%400==0):
            return False
        if(yy%4 == 0):
            return True
        return False
    @staticmethod
    def createCal():
        for i in range(7):
            month.append([])
        for i in range(7):
            month[0].append(day[i])
    @staticmethod
    def updateCale():
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
            # j = 0
            # while(j < 7):
            #     k += 1        
            #     if(k > mon[m-1]):
            #         # month[i].append('  ')
            #         month[i][j] = ' - '
            #     else:
            #         if(k < 10):
            #             month[i].append(' '+str(k))
            #         else:
            #             # month[i].append(k)
            #     j+= 1
            for j in range(7):
                k += 1        
                if(k > mon[m-1]):
                    month[i].append('  ')
                    # month[i][j] = '- '
                else:
                    if(k < 10):
                        month[i].append(' '+str(k))
                    else:
                        month[i].append(k)
                        # month[i][j] = k
    
    @staticmethod
    def displayCale():
        for j in range(7):
            for i in range(7):
                print(month[j][i],end = '  ')
            print()

m = int(input())
y = int(input())
if(m < 1 or m > 12):
    print('You Entered incorrect month : ')
    sys.exit(0)
start = MyCalender.startDay(y,m,1)
if(MyCalender.leapYear(y) == True):
    mon[1] = 29
print('\n\n------------------------------')
print('Python Calender: ',m,y)
print(mon_name[m-1],y)
print('------------------------------\n')
MyCalender.createCal()
MyCalender.updateCale()
MyCalender.displayCale()
