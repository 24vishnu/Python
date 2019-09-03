'''
Create Object Oriented Analysis and Design of a simple Address Book Problem .
'''

import AddressBookBL as A_book_obj

menu = A_book_obj.MenuBar()

#Perform the user choice operations
while True:
    print('Enter your choice : ')
    print('1.   Add New Person : ')
    print('2.   Delete person : ')
    print('3.   Sort by address : ')
    print('4.   sort by first name : ')
    print('5.   sort by zip : ')
    print('6.   Edit Details : ')
    print('7.   save : ')
    print('8.   Exit : ')
    #Enter user choice
    choice = int(input())

    #check user choice and perform there required functionality
    if choice == 1:
        A_book_obj.book.append(menu.add_new_person())

    elif choice == 2:
        name = input('Enter your first name for delete record from address book : ')
        menu.delete_person(name)

    elif choice == 3:
        menu.sort_by_address()

    elif choice == 4:
        menu.sort_by_name()

    elif choice == 5:
        menu.sort_by_zip()

    elif choice == 6:
        name = input('Enter first name for edit informatin : ')
        menu.edit_information(name)

    elif choice == 7:
        menu.save(A_book_obj.book)

    elif choice == 8:
        break

    else:
        print('\n******************** Please Enter correct following choice **************************\n')
