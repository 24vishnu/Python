# ---------------------------------------------- Address book program-----------------------------
# AddressBook.py
# Date : 03/09/2019
# Manage the address book file and perform different operation like add new person in address book,
# delete pension, save file, sort on different parameters
# ---------------------------------------------------------------------------------------------


import json


# Address book class here require all information of any person
class AddressBook:

    def __init__(self):
        # initially all entry are None (or default)
        self.details = {
            'first_name': None,
            'last_name': None,
            'address': None,
            'city': None,
            'state': None,
            'zip_code': 0,
            'phone_number': 0
        }


'''
In menu bar class we can perform the different operations like 
create add details for a new person, Edit details of any person based on first name
delete record of any person based on first name and we can perform the different sortion operations
like sort all person based on address, first name, zip code etc.
and at last we have to save the all details of file after performing operations otherwise data will not
save into the file (record)
'''


class MenuBar:

    # Method for add new person in the address book
    def add_new_person(self):

        # AB = AddressBook()
        details = {}

        f_name = input('Enter your first name ')
        l_name = input('Enter your last name ')
        address = input('Enter your Address ')
        city_name = input('Enter your city name ')
        state_name = input('Enter your state ')
        while True:
            zip_code = input('Enter your city zip ')
            try:
                zip_code = int(zip_code)
            except ValueError:
                print('Please Enter only numbers ')
                continue
            if 100000 < zip_code < 999999:
                break
            else:
                print('zip code should be in 6 digits ')

        while True:
            mobile_no = int(input('Enter your phone number '))
            try:
                mobile_no = int(mobile_no)
            except ValueError:
                print('please enter only numbers : ')
                continue
            if 7000000000 < mobile_no < 9999999999:
                break
            else:
                print('please valid mobile number( mobile number should have 10 digits and first digit should be '
                      'start with 7,8 or 9)')

        details['first_name'] = f_name
        details['last_name'] = l_name
        details['address'] = address
        details['city'] = city_name
        details['state'] = state_name
        details['zip_code'] = zip_code
        details['phone_number'] = mobile_no

        return details

    # Edit the person details based on person first name if person does not
    # want to edit some details the enter same as previous
    def edit_information(self, name):
        flag = True
        for i in book:
            if i['first_name'] == name:
                flag = False
                i['address'] = input('Edit your Address ')
                i['city'] = input('Edit your city name ')
                i['state'] = input('Edit your state ')
                i['zip_code'] = int(input('Edit your city zip '))
                i['phone_number'] = int(input('Edit your phone number '))
                break
        if flag:
            print('this name is not present in the address book')

    # Delete a person from the address book
    def delete_person(self, name):
        flag = True

        for i in book:
            if i['first_name'] == name:
                flag = False
                book.remove(i)

        if flag:
            print('this name is not present in the address book')

    # sort the all address book detail based on the address
    def sort_by_address(self):
        addr = []

        for i in book:
            addr.append(i['address'])

        addr = sorted(addr, key=lambda s: s.casefold())

        print(' %15s %15s %15s %15s %15s %15s %15s' % (
            'First name', 'Last nmae', 'Address', 'City', 'State', 'Zip', 'Phone number'))
        print(
            '------------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['address'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' % (
                        j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                        j['phone_number']))
                    break

    # sort the all address book detail based on the first name
    def sort_by_name(self):
        addr = []

        for i in book:
            addr.append(i['first_name'])

        addr = sorted(addr, key=lambda s: s.lower())

        print(' %15s %15s %15s %15s %15s %15s %15s' % (
            'First name', 'Last nmae', 'Address', 'City', 'State', 'Zip', 'Phone number'))
        print(
            '--------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['first_name'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' % (
                        j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                        j['phone_number']))
                    # print(j['first_name']," : ",j['last_name']," : ",j['address']," : ",j['city' ]," : ",j['state'
                    # ]," : ",j['zip_code']," : ",j['phone_number'] )
                    break

    # sort the all address book detail based on the zip code
    def sort_by_zip(self):

        addr = []

        for i in book:
            addr.append(i['zip_code'])

        addr.sort()

        print(' %15s %15s %15s %15s %15s %15s %15s' % (
            'First name', 'Last nmae', 'Address', 'City', 'State', 'Zip', 'Phone number'))
        print(
            '---------------------------------------------------------------------------------------------------------------------')

        for i in addr:
            for j in book:
                if j['zip_code'] == i:
                    print(' %15s %15s %15s %15s %15s %15d %15d' % (
                        j['first_name'], j['last_name'], j['address'], j['city'], j['state'], j['zip_code'],
                        j['phone_number']))
                    break

    # save all person derails into file
    def save(self, data):

        with open('Address_book.json', 'w') as AB:
            json.dump(data, AB, indent=1)


# Read the address book file
def read_File():
    # open file and read data from file
    with open("Address_book.json", 'r') as json_file:
        # load the file data into a variable data
        data = (json.load(json_file))
        return data


book = read_File()
# if __name__ == "__main__":
#     book = read_File()
