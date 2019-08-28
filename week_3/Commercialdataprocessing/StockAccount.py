#program for sell, buy, display, and total stock share in the recourd (commercial data processing)


import StockAccountBL as BL_file_obj

class_name_obj = BL_file_obj.StockAccount('personal.json')

# take input from user and check user input is currect or not as required
while(True):
    N = input('Enter 1. Buy stock \n2. for sell stock\n3. for tatal stock value \n4. print Report\n')
    try:
            N = int(N)
    except ValueError:
        print('please enter valid number : ')
        continue
    # user choice shoud not be less than 1 and grater than 4 
    if N > 0 and N < 5:
        break
    else:
        print('please choose valid option between (1 to 5) ')

# take input from user and check user input is currect or not as required
if N == 1:
    while(True):
        amount = input('Enter your amount ')
        try:
                amount = int(amount)
        except ValueError:
            print('please enter valid number : ')
            continue
        break
    symbol = input('Enter name (symbol) of stock ')   
    class_name_obj.buy(amount,symbol)

# take input from user and check user input is currect or not as required
elif N == 2:
    while(True):
        amount = input('Enter your amount ')
        try:
                amount = int(amount)
        except :
            print('please enter valid number : ')
            continue
        break
    symbol = input('Enter name (symbol) of stock ')   
    class_name_obj.sell(amount,symbol)

elif N == 3:
    class_name_obj.valueOf()

else:
    class_name_obj.printReport()