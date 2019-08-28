# ---------------------------------------------- Commercial data processing program -----------------------------
# StockAccount.py
# Date : 28/08/2019
# update the json file after performing operation like sell, buy
# -----------------------------------------------------------------------------------------------------


import json
import time

class StockAccount:
    #Constructor for initialize the commercial data object or open the file and read
    def __init__(self,accountFile):
        with open(accountFile,'r') as file_obj:
            self.record = json.load(file_obj)

  #=====================================================  
  #print the total values of all share in the record
    def valueOf(self):
        result = 0
        for i in self.record:
            result += i['share'] * i['amount']
        
        print('Over all total values of shares is : $',result,'\n')

#=====================================================
#buy a share with passing share name (symbol) and amount
    def buy(self, amount, symbol):
        present = False
        for i in self.record:
            if symbol not in i.values():
                continue
            i['share'] += 1
            i['time'] = time.ctime()
            Stock_obj.save(self.record,'personal.json')
            present = True
            break
        
        if present == False:

            new_share = {
                'Symbol': symbol,
                'share' : 1,
                'amount': amount,
                'time': time.ctime()
                }

            self.record.append(new_share)
            Stock_obj.save(self.record,'personal.json')
                
#==================================================
#buy a share with passing share name (symbol) and amount
    def sell(self, amount, symbol):
        present = False

        for i in self.record:
            i['time'] = time.ctime()
            if symbol not in i.values():
                continue

            if(i['share'] != 0):
                if(i['share'] == 1):
                    self.record.remove(i)
                    Stock_obj.save(self.record,'personal.json')

                else:
                    i['share'] -= 1
                    i['time'] = time.ctime()
                Stock_obj.save(self.record,'personal.json')
                present = True
                break

            else:
                print('share is out or stock. ')
                i['time'] = time.ctime()
                Stock_obj.save(self.record,'personal.json')
                present = True
                break

        if(present == False):
            print('This itrm not available rigth now, this will be comming soon.')

#============================================================================
#save the record in file after perform operation
    def save(self,data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file)

#============================================================================
#print all record of the file
    def printReport(self):
        for i in self.record:
            for j,k in i.items():
                print(j,'\t',k, end = ' \t ')
            print()
       
Stock_obj = StockAccount('personal.json')