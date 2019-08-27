
# ----------------------------------------------Regula Expression program -----------------------------
# RegularExpression.py
# Date : 27/08/2019
# validate name and mobile number and repalce the name mobile number using regex methods and displce updated string
# -----------------------------------------------------------------------------------------------------


import re
import datetime

#method to check name is valid or not
def isValidName(name):
    full_name = name.split()
    if len(full_name) == 2 and name.replace(" ", "").isalpha():
        return True
    return False

#check mobile number is valid or not
def isValidNumber(number): 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(number) 

#Following method is use perform the repalce database string name, full name, mobile number and current date
def replace_name_number(name,number):
    string = 'Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-­xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.'
    full_name = name.split()
    string = re.sub(r'­xxxxxxxxxx',number,string)
    string = re.sub(r'<<name>>',full_name[0],string)    
    string = re.sub(r'<<full name>>',name,string)
    string = re.sub(r'01/01/2016',str(datetime.datetime.now().date()),string)

    print(string)