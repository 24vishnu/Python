# ---------------------------------------------- Stock Report program -----------------------------
# StockReport.py
# Date : 28/08/2019
# Write and read the data of stock into JSON file
# -----------------------------------------------------------------------------------------------------

import json

feeds_data = []


# Method for write the data into JSON file
def writeFile():
    # Take name of stack from user
    stock_name = input('Enter Stock name of ')

    # Take Number of share of stocks and check is it valid number or not
    while True:
        N_stocks = (input('Number of Share : '))
        try:
            N_stocks = int(N_stocks)
        except ValueError:
            print('Please Enter valid number of share : ')
            continue
        if N_stocks >= 0:
            break
        else:
            print('Please enter positive number. ')

    # Take price of one share and check is it valid number or not
    while True:
        stock_price = (input('Enter Share Price '))
        try:
            stock_price = float(stock_price)
        except ValueError:
            print('Please Enter valid price of share : ')
            continue
        if stock_price >= 0:
            break
        else:
            print('Please enter positive number. ')

    # Add detail in the dictionary  
    stock_details = {
        'stock_name': stock_name,
        'stocks': N_stocks,
        'stock_price': stock_price
    }
    # append Dictionary into a list
    feeds_data.append(stock_details)


# write (dump) stock details into json file
def add_data(N):
    write_N_Stocks = N
    if write_N_Stocks > 0:
        with open('personal.json', 'w') as json_file:
            json.dump(feeds_data, json_file, indent=1)
    else:
        print('old data of file will be display : ')


# Read (load) stocks details from JSON file
def readFile():
    with open('personal.json', 'r') as json_file:
        data = (json.load(json_file))
    # Display the required details
    for i in data:
        print('value of one stock of', i.get('stock_name'), ' is :', i.get('stock_price'),
              '\t And total value of stocks are : ', i.get('stocks') * i.get('stock_price'))
