import sys
class DeQueue:
    #Constructor
    def __init__(self,cap = None):
        if cap != None:
            self.capasity = cap
        else:
            self.capasity = 10
        self.front = 0
        self.rear = 0
        self.queue = [-1]*self.capasity
    #Add Front
    def addFront(self,item):
        if (self.rear - self.front) == self.capasity:
            print('Queue is full')
            return
        temp = self.rear
        while temp > self.front:
            self.queue[temp] = self.queue[temp - 1]
            temp -= 1
        self.queue[temp] = item
        self.rear += 1
    #Add Rear
    def addRear(self,item):
        if (self.rear - self.front) == self.capasity:
            print('Queue is full')
            return
        self.queue[self.rear] = item
        self.rear += 1
    #Remove Front
    def removeFront(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return
        data = self.queue[self.front]
        for i in range(self.front,self.rear):
            self.queue[i] = self.queue[i+1]
        self.rear -= 1
        return data
    # Remove Rear
    def removeRear(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return
        data = self.queue[self.rear-1]
        self.rear -= 1
        return data
    #IsEmpty
    def isEmpty(self):
        return self.front == self.rear
    #size
    def size(self):
        return (self.rear - self.front)
    def display(self):
        for i in range(self.front, self.rear):
            print(self.queue[i],end=' ')

#=================================================
ob = DeQueue()
string1 = input('Enter String to check palindrom : ')
for i in string1:
    ob.addFront(i)
string2 = ''
while ob.size() > 1:
    if ob.removeFront() is not ob.removeRear():
        print(False)
        sys.exit(0)
print(True)
    # string2 = string2 + ob.removeFront()
# print(string1 == string2)
#====================================================


# flag = True
# while(flag):
#     print("1. Add Front\n2. Add back\n3. remove front\n4. remove back")
#     ch = int(input())
#     if(ch == 1):
#         print('Enter Items : ')
#         item = input()
#         ob.addFront(item)
#         ob.display()
#     elif ch == 2:
#         print('Enter Items : ')
#         item = input()
#         ob.addRear(item)
#         ob.display()
#     elif ch == 3:
#         print(ob.removeFront())
#         ob.display()
#     else:
#         print(ob.removeRear())
#         ob.display()
#     print('Yu want to exit : (1/0) : ')
#     rep = int(input())
#     if(rep == 0):
#         flag = False
