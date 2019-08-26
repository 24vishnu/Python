#program to check the sting is palindrom or not using dequeue using linked list

import DequeueBL as Dq_Obj
import sys

ob = Dq_Obj.DeQueue()
string1 = input('Enter String to check palindrom : ')

for i in string1:
    ob.addFront(i)
string2 = ''

while ob.size() > 1:
    if ob.removeFront() is not ob.removeRear():
        print(False)
        sys.exit(0)

print(True)
  