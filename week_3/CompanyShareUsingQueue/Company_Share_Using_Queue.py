import Company_Share_Using_QueueBL as que_share_obj

# record = que_share_obj.obj.readFileData()
# que_share_obj.obj.createStack(record)
flag = True
while True:

    if flag:
        flag = False
        record = que_share_obj.obj.readFileData()
        que_share_obj.obj.createQueue(record)

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

    # record = obj.readFileData()
    # obj.createStack(record)

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
        que_share_obj.obj.buy_stock(symbol, amount, record)

    # take input from user and check user input is currect or not as required
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
        que_share_obj.obj.sell_stock(symbol, record)

    elif N == 3:
        que_share_obj.obj.valueOf(record)

    else:
        que_share_obj.obj.printRecord(record)

    again = input('please Enter 1 for again perform : ')
    try:
        again = int(again)
        if again != 1:
            que_share_obj.obj.writeFile(record)
            break
    except ValueError:
        que_share_obj.obj.writeFile(record)
        break
