"""
Desc ­> Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
efficiently search a number from a given set of number

I/P ­> read a set of numbers from a file and take user input to search a number

Logic ­> Firstly store the numbers in the Slot. Since there are 10 Numbers divide
each number by 11 and the reminder put in the appropriate slot. Create a Chain
for each Slot to avoid Collision. If a number searched is found then pop it or else
push it. Use Map of Slot Numbers and Ordered LinkedList to solve the problem.
In the Figure Below, you can see number 77/11 reminder is 0 hence sits in the 0
slot while 26/11 remainder is 4 hence sits in slot 4

O/P ­> Save the numbers in a file
"""

import HashingClassBL as hash_obj

obj = hash_obj.Hashing()

# read the data from file
f = open("number.txt", "r")
data = f.read()
f.close()

num = ''

for i in data:
    if i == ' ':
        obj.addData(int(num))
        num = ''
    else:
        num = num + i

for i in range(len(obj.hashList)):
    print(obj.hashList[i])

print('Enter the number to search!  ')
num = int(input())

print(obj.search(num))
f = open("Number.txt", "w")
# f.write('\n\n')

for i in range(len(obj.hashList)):
    for j in range(len(obj.hashList[i])):
        f.write(str(obj.hashList[i][j]))
        f.write(' ')

    f.write('\n')
