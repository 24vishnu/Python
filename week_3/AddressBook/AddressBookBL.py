# ---------------------------------------------- Address book program-----------------------------
# AddressBook.py
# Date : 03/09/2019
# Manage the addrss book file and perform different operation like add new persion in address book,
# delete persion, save file, sort on different parameters
#---------------------------------------------------------------------------------------------


import json

# Address book class here requre all information of any persion
class AddressBook:
    
    def __init__(self):
        #initially all entry are None (or default)
        self.details = {
            'first_name' : None, 
            'last_name' : None, 
            'address' : None, 
            'city' : None, 
            'state' : None, 
            'zip_code' : 0, 
            'phone_number' : 0 
            }

'''
In menu bar class we can perform the different operations like 
create add details for a new person, Edit details of any persion based on first name
delete record of any persion based on first name and we can perform the different sortion operations
like sort all persion based on address, first name, zip code etc.
and at last we have to save the all details of file after performing operations otherwise data will not
save into the file (record)
'''
class MenuBar:

    #Method for add new persoin in the address book
    def add_new_person(self):

        AB = AddressBook()
        
        f_name = input('Enter your first name ')
        l_name = input('Enter your last name ')
        address = input('Enter your Address ')
        city_name = input('Enter your city name ')
        state_name = input('Enter your state ')
        zip_code = int(input('Enter your city zip '))
        mobile_no = int(input('Enter your phone number '))

        AB.details['first_name']  = f_name
        AB.details['last_name']  = l_name
        AB.details['address']  = address
        AB.details['city' ]  = city_name
        AB.details['state' ] = state_name
        AB.details['zip_code']  = zip_code
        AB.details['phone_number']  = mobile_no

        return AB.details

    #Edit the persion details based on persion first name if persion does not 
    # want to edit some details the enter same as previous
    def edit_information(self,name):
        
        for i in book:
            if(i['first_name'] == name):
                    i['address']    =input('Edit your Address ')
                    i['city']       = input('Edit your city name ')
                    i['state']      = input('Edit your state ')
                    i['zip_code']   = int(input('Edit your city zip '))
                    i['phone_number'] = int(input('Edit your phone number '))
                    break
    
    #Delete a persion from the address book
    def delete_person(self,name):
        for i in book:
            if i['first_name'] == name:
                book.remove(i)
    
    #sort the all address book detail based on the address 
    def sort_by_address(self):

        addr = []

        for i in book:
            addr.append(i['address'])

        addr = sorted(addr,key = lambda s : s.casefold())

        print(' %15s %15s %15s %15s %15s %15s %15s' %('First name', 'Last nmae' ,'Address',  'City' ,   'State'  , 'Zip'  ,  'Phone number'))
        print('------------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['address'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' %(j['first_name'],j['last_name'],j['address'],j['city' ],j['state' ],j['zip_code'],j['phone_number'] ))
                    break

    
    #sort the all address book detail based on the first name 
    def sort_by_name(self):
        addr = []

        for i in book:
            addr.append(i['first_name'])

        addr = sorted(addr,key = lambda s : s.lower())
        
        print(' %15s %15s %15s %15s %15s %15s %15s' %('First name', 'Last nmae' ,'Address',  'City' ,   'State'  , 'Zip'  ,  'Phone number'))
        print('--------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['first_name'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' %(j['first_name'],j['last_name'],j['address'],j['city' ],j['state' ],j['zip_code'],j['phone_number'] ))
                    # print(j['first_name']," : ",j['last_name']," : ",j['address']," : ",j['city' ]," : ",j['state' ]," : ",j['zip_code']," : ",j['phone_number'] )
                    break

    #sort the all address book detail based on the zip code 
    def sort_by_zip(self):
        
        addr = []

        for i in book:
            addr.append(i['zip_code'])
        
        addr.sort()

        print(' %15s %15s %15s %15s %15s %15s %15s' %('First name', 'Last nmae' ,'Address',  'City' ,   'State'  , 'Zip'  ,  'Phone number'))
        print('---------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['zip_code'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' %(j['first_name'],j['last_name'],j['address'],j['city' ],j['state' ],j['zip_code'],j['phone_number'] ))
                    break

    # save all persion derails into file
    def save(self,data):

        with open('Address_book.json','w') as AB:
            json.dump(data, AB,indent = 1)


#Read the address book file
def read_File():

    #open file and read data from file
    with open("Address_book.json", 'r') as json_file:
        # load the file data into a variable data
        data = (json.load(json_file))
        return data

book = read_File()
# if __name__ == "__main__":
#     book = read_File()