# ----------------------------------------------Inventory program -----------------------------
# stock_share_list.py
# Date : 29/08/2019
# implement linked list according to requirement for modification in company share and update JSON file
# ---------------------------------------------------------------------------------------------

import json
import time

'''
Following is the linked list class. we create a node by creating object of this class
node is where data is stored in the linked list.
Along with the data each node also holds a pointer, which is a reference to the next 
node in the list.  
'''


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


# ===============================================================
# In this class we implement the some methods for modification in stock data    
class stock_function:

    # constructor for create initialize empty linked list
    def __init__(self):
        self.head = None
        return

    # add_list method is used for add the item into linked list
    def add_list(self, item):
        if not isinstance(item, LinkedList):
            item = LinkedList(item)

        if self.head is None:
            self.head = item

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            if temp.next is None:
                temp.next = item
        return

    # if in real time share and amount of stock change then we call this method
    def edit_details(self, object_name, record, share, amount):

        if self.head is None:
            print('Database is empty: ')
            return

        else:
            temp = self.head

            while temp is not None and temp.data != object_name:
                temp = temp.next

            if temp is not None:
                record[temp.data]['amount'] = amount
                record[temp.data]['share'] = share
                obj.writeFile(record)
            else:
                print('No data (Recourd) found for : ', object_name)

    # Method for print list data (comany name (symbol))
    def print_list(self):

        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

    # print total value of stocks in record of all company
    def valueOf(self, record):
        temp = self.head
        value = 0

        while temp is not None:
            value += record[temp.data]['share'] * record[temp.data]['amount']
            temp = temp.next

        print('Total value of record : ', value)

    # search given stock name is present or not in record (Database)
    def search_stock(self, stock_name):

        if self.head is None:
            print('Dukan khali h ): ')
            return False

        temp = self.head

        while temp is not None and temp.data != stock_name:
            temp = temp.next

        if temp is None:
            print('Your item is not present in the stock : ')
            return False
        else:
            return True

    # Method for delete item (data) from linked list (we insure data is present in record)
    def delete_item(self, item):
        temp = self.head

        # if data find at head of list
        if temp.data == item:
            self.head = self.head.next
            return

        # find where is data in link list
        while temp.next is not None and temp.next.data != item:
            temp = temp.next

        # store next pointer address
        next_pointer = temp.next.next
        temp.next = None

        # if data is not in last node of linked list
        if next_pointer is not None:
            temp.next = next_pointer

    # sell method is used for delete a stock detail from record
    def sell_stock(self, stock_name, record):
        if obj.search_stock(stock_name):
            obj.delete_item(stock_name)
            obj.writeFile(record)

    # buy method is used for add the new stock detail into the record
    def buy_stock(self, stock_name, amount, record):
        share = int(input('how many share you want to purchase : '))

        # create a new object (dict) and add all detail of share
        record[stock_name] = {
            'share': share,
            'amount': amount,
            'time': time.ctime()
        }

        # add stock name in list
        obj.add_list(stock_name)
        # update the file with new record
        obj.writeFile(record)

    # Print all data of company share
    def printRecord(self, record):
        temp = self.head

        while temp is not None:
            print(temp.data, '\t->\t', record[temp.data])
            temp = temp.next

    # Read the data from json file
    def readFileData(self):

        with open('stock_file.json', "r") as file_obj:
            fileData = json.load(file_obj)

        return fileData

    # take the data from linked list and update the record into json file
    def writeFile(self, record):

        with open('stock_file.json', "w") as file_obj:
            temp = self.head

            reRight = {}

            while temp is not None:
                reRight[temp.data] = record[temp.data]
                temp = temp.next

            # write the data into json file
            json.dump(reRight, file_obj, indent=1)

    # Read the data from json file by calling readFileData() method and create list of data object
    def createList(self):
        file_data = obj.readFileData()

        for i in file_data:
            obj.add_list(i)


obj = stock_function()
obj.createList()
