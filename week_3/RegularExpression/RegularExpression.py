#**********************************************************************************
#   program replace the name and number from pre store string and print the updated data 
#
#**********************************************************************************

import RegularExpressionBL as RE_obj

# take input as a valid name from user
while(True):

    name = input("Enter your full name : ")

    if(RE_obj.isValidName(name) == True):
        break
    else:
        print("Incurrect name enter valid full name : ")


# take input as a valid mobile number from user
while(True):

    number = input("Enter your mobile Number : ")

    if(RE_obj.isValidNumber(number)):
        break
    else:
        print("Incurrect number enter valid Number : ")

#send the name and mobile number and update the data and print
RE_obj.replace_name_number(name,number)