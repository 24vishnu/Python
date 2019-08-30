# ----------------------------------------------Company share program using stack-----------------------------
# stock_share_stack.py
# Date : 30/08/2019
# implement STACK using linklist according to requrement for modification in company share and update JSON file
#---------------------------------------------------------------------------------------------

import json
import time

# Linked list class to create a node with data or empty
class LinkedList:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        return

#===============================================================   
'''
In this class we implement the some methods for 
modification in stock data from json file and 
also we implement the stack function using linked list
and perform the all operation only using stack implemented functions   
'''
class stock_function:

    def __init__(self):
        self.head = None
        self.Top = 0

        return


 #----------------------------push(item) Method for Add item-----------------------------------   
    def push(self, item):

        if not isinstance(item,LinkedList):
            item = LinkedList(item) 

        if self.head is None:
            self.head = item

        else:   
            item.next = self.head
            self.head = item

        self.Top += 1

#----------------------------- pop() method for delete the top Item from stack -----------------------------
    def pop(self):

        if self.head == None:# or self.Top == 0:
            print('Under flow')
            return

        self.head = self.head.next
        self.Top -= 1
        
#-----------------------------peek() method for only return the top Item of stack---------------------------
    def peek(self):

        if self.head == None:
            print('Under flow')
            return
        
        return self.head.data 

 #-----------------------------isEmpty() method return true is stack is empty else return false ------------
    def isEmpty(self, ):

        return self.head == None
        # return self.Top == 0

 #-------------------------------size() method Return the number of elements in the stack-------------------
    def size(self):
        return self.Top

 
 #------------------------------- print_list() method is print linked list ---------------------------------
    def print_list(self):

        temp = self.head

        while(temp != None):
            print(temp.data)
            temp = temp.next

 #---- search_stock() method Search object is present stack or not------------------------------------------
    def search_stock(self,stock_name):
        temp = False

        if obj.Top == 0:
            return temp
       
        new_stack = stock_function()

        while(obj.size() > 0):

            item = obj.peek()
            new_stack.push(item)
            obj.pop()

            if item == stock_name:
                temp = True
                break

        while(new_stack.size()>0):
            item = new_stack.peek()
            obj.push(item)
            new_stack.pop()

        return temp
        
        
 
 #----------------------------------delete data(stock) from stack-------------------------------------------
    def delete_stock(self,stock_name):
        
        new_stack = stock_function()

        while(obj.size() > 0):
            item = obj.peek()

            if item == stock_name:
                break

            new_stack.push(item)
            obj.pop()
           
        obj.pop()

        while(new_stack.size()>0):
            item = new_stack.peek()
            obj.push(item)
            new_stack.pop()

 #-----------------------------------sell stock with name --------------------------------------------------
    def sell_stock(self,stock_name,record):

        if obj.search_stock(stock_name) == True:
            obj.delete_stock(stock_name)
            obj.writeFile(record)

 #----buy_stock() method for add stock using there name and price into the stack then json file-------------
    def buy_stock(self,stock_name,amount, record):
        share = int(input('how many share you want to purchase : '))
        record[stock_name] = {
            'share' : share,
            'amount': amount,
            'time'  : time.ctime()
        }
        obj.push(stock_name)
        obj.writeFile(record)

 #------------------------------------printRecord() print all data using stack------------------------------
    def printRecord(self):

        new_stack = stock_function()
        
        while(obj.size() > 0):
            item = obj.peek()
            new_stack.push(item)
            print(item)
            obj.pop()

        while(new_stack.size()>0):
            item = new_stack.peek()
            obj.push(item)
            new_stack.pop()

 #----------------------------------valueOf() method return the total value of stock -----------------------
    def valueOf(self,record):
        value = 0
        stack_temp = stock_function()

        while obj.size() > 0:
            item = obj.peek()
            value += record[item]['share'] * record[item]['amount']
            stack_temp.push(item)
            obj.pop()

        while stack_temp.size() > 0:
            obj.push(stack_temp.peek())
            stack_temp.pop()

        print('Total value of recourd : ',value)
 #----------------------------------readFileData() method read data from json file -------------------------
    def readFileData(self):

        with open('company_stocks.json',"r") as file_obj:
            fileData = json.load(file_obj)

        return fileData
    
 #----------------------------------writeFile() method write data into json file ---------------------------
    def writeFile(self ,record):

        with open('company_stocks.json',"w") as file_obj:

            re_write = {}
            while obj.size() > 0:
                re_write[obj.peek()] = record[obj.peek()]
                obj.pop()

            json.dump(re_write,file_obj,indent = 1)
#----------------------------------------- createStack() method for push the all record into stack-----------
    def createStack(self,file_record):
        for symbol in file_record:
            obj.push(symbol)

obj = stock_function()


