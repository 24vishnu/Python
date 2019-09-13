import Array2DBL

# Take the input from user for row of array
while True:
    row = (input('Enter size of row : '))
    # check user input is valid or not
    try:
        row = int(row)
    except ValueError:
        print('Please enter the valid number : ', type(row))
        continue
    if row >= 0:
        break
    else:
        print('Please enter positive number. ')

# Take the input from user for column of array
while True:
    column = (input('Enter size of column : '))
    # check user input is valid or not
    try:
        column = int(column)
    except ValueError:
        print('Please enter the valid number : ', type(column))
        continue
    if column >= 0:
        break
    else:
        print('Please enter positive number. ')

'''
we are passing size of row (n) and column (m) in method2D()
this method take the (n*m) values form user and write into the file 
'''
if Array2DBL.method2D(row, column):
    print("data saved in file")
else:
    print("data not saved in file")
