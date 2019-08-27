
# ----------------------------------------------Inventry program -----------------------------
# InventryDataManagement.py
# Date : 27/08/2019
# read the json file and display the file containt
#---------------------------------------------------------------------------------------------


import json
import os.path

#Read the JSON file and display data of file
def read_File():

    #open file and read data from file
    with open("inventry.json", 'r') as json_file:
        # load the file data into a variable data
        data = (json.load(json_file))
        return data

        #print all file data line by line
def print_data(data):
    print('\nData of file is following : \n')
    for i in data:
        print(i)

#take the price and weigth value and print total price of stock inventry
def print_toal_price(data):
    for i in data:
        res = 1
        name = ''
        for j,k in i.items():
            if j == 'name':
                name = k
            if j == 'weight' or j == 'price':
                res *= k
        for j,k in i.items():
            print('Total price of ',name,k,' is ',res)
            break