import random
import math
# This class for create a new node when calling there constructor with passing data (item)
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class QueueList:
#This function use to initialize the empty queue
    def __init__(self):
        self.head = None
        self.rear = 0
        return

# Function for push the value in the queue
    def enQueue(self, item):
        self.rear += 1
        if not isinstance(item,LinkedList):
            item = LinkedList(item)                             
        if self.head is None:
            self.head = item
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = item

# Function for remove the item from top
    def deQueue(self):
        if self.rear == 0:
            print('Queue is Empty : ')
        else:
            self.rear -= 1
            data = self.head.data
            self.head = self.head.next
            return data
           

# Function to find the current size  of stack
    def size(self):
        return self.rear
        

# Function to check Stack is empty or not..
    def isEmpty(self):
        return self.rear == 0

#Function for print the value of stack
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
        print()

#==================================================
prim = []
anagram_list = []
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

def primeList():
    for i in range(1,1000):
        if(prime(i) == True):
            prim.append(i)
       
def anagram(a,b):
    x = list(str(a))
    y = list(str(b))
    x.sort()
    y.sort()
    return x == y

primeList()
for i in range(len(prim)):
    for j in range(len(prim)):
        if prim[i] is not prim[j]:
            if(anagram(prim[i],prim[j]) == True):
                if prim[i] not in anagram_list:
                    anagram_list.append(prim[i])
                if prim[j] not in anagram_list:
                    anagram_list.append(prim[j])
        

#==================================================
q = QueueList()
print('Following are the numbers enQueue into queue : ')
for i in anagram_list:
    print(i,end=' ')
    q.enQueue(i)
    # q.display()
print('\n\nFollowing are the numbers deQueue from queue : ')
while q.size() > 0:
    print(q.deQueue(),end=" ")
print()

