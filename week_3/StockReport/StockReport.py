'''
Desc ­> Write a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock.

I/P ­> N number of Stocks, for Each Stock Read In the Share Name, Number of
Share, and Share Price

Logic ­> Calculate the value of each stock and the total value

O/P ­> Print the Stock Report.
'''

import StockReportBL as St_Rep_obj

# Take user input for write number of stock into file
while True:
    N = (input('How many stock you want to read : '))
    #ckeck user input is valid or not
    try:
       N = int(N)
    except ValueError:
       print('Please enter the valid number : ',type(N))
       continue
    if N >= 0:
        break
    else:
        print('Please enter positive number. ')

#Enter stock details and store into a list
for i in range(N):
    St_Rep_obj.writeFile()

#write list data into json file
St_Rep_obj.add_data(N)

#read file and display requred result
print('\nFollowing is stock report : ')
St_Rep_obj.readFile()

