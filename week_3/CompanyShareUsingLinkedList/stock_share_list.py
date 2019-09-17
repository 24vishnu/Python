# *********************************************** USING LINKED LIST********************************************
#
# program for sell, buy, display, and total 
# stock share in the recourd (commercial data processing)
#
# *************************************************************************************************

import stock_share_listBL as ss_obj

# take input from user and check user input is correct or not as required
while True:
    print('Enter')
    print('1. Buy stock')
    print('2. for sell stock')
    print('3. for total stock value ')
    print('4. print Report')
    N = input()
    try:
        N = int(N)
    except ValueError:
        print('please enter valid number : ')
        continue

    # user choice should not be less than 1 and grater than 4
    if 0 < N < 5:
        break
    else:
        print('please choose valid option between (1 to 5) ')

record = ss_obj.obj.readFileData()

# take input from user and check user input is correct or not as required
if N == 1:
    while True:
        amount = input('Enter your amount ')
        try:
            amount = int(amount)
        except ValueError:
            print('please enter valid number : ')
            continue
        break
    symbol = input('Enter name of company ')
    ss_obj.obj.buy_stock(symbol, amount, record)

# take input from user and check user input is correct or not as required
elif N == 2:
    while True:
        amount = input('Enter your amount ')
        try:
            amount = int(amount)
        except ValueError:
            print('please enter valid number : ')
            continue
        break
    symbol = input('Enter name (symbol) of stock ')
    ss_obj.obj.sell_stock(symbol, record)

elif N == 3:
    ss_obj.obj.valueOf(record)

else:
    ss_obj.obj.printRecord(record)
