# ---------------------------------- prg-----------------------------------------------
# Array2D.py
# date : 26/08/2019
# write into the file in form of 2D array

array_2D = []


def method2D(row, col):
    # we take a empty list name array_2D initially this is empty
    # array_2D = []

    # for loop for create n number or inner list in the empty list
    # append empty list in every row
    for i in range(0, row):
        array_2D.append([])

    """	
        initialise 2D list n row and m column
        in each row we append the m number of elements
        and now initialise with 0 (zero) of every row	
    """

    for i in range(row):
        for j in range(col):
            array_2D[i].append(j)
            array_2D[i][j] = 0

    # Taking the value for every index of each row from user and assign value at particular position
    for i in range(row):
        for j in range(col):
            x = input("Enter value for array ")
            array_2D[i][j] = x
    return save_file()
    """
        we are opening a file and write the all value of 
        arry_2D into the file in form of row and column
    
        If file not exist then create the new file as same name
    """


def save_file():
    result = False
    f = open("File2D_Print.txt", "w")
    for i in range(len(array_2D)):
        for j in range(len(array_2D[i])):
            f.write(str(array_2D[i][j]))
            f.write(' ')
        f.write('\n')
        result = True
    f.close()
    return result
