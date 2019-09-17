# ---------------------------------- prg-----------------------------------------------
# Queue_List.py
# date : 26/08/2019
# Implement the queue using Linked list and perform operation of prime number and anagram numbers


import random
import math


# This class for create a new node when calling there constructor with passing data (item)
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class QueueList:

    # This function use to initialize the empty queue
    def __init__(self):
        self.head = None
        self.rear = 0
        return

    # Function for push the value in the queue
    def enQueue(self, item):
        self.rear += 1

        if not isinstance(item, LinkedList):
            item = LinkedList(item)

        if self.head is None:
            self.head = item
            return

        temp = self.head
        while temp.next is not None:
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

    # Function for print the value of stack
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

        print()


# ==================================================
prim = []
anagram_list = []


# check number is prime or not
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


# make a list of prime numbers
def primeList():
    for i in range(1, 1000):
        if prime(i):
            prim.append(i)


# check number is anagram or not
def anagram(a, b):
    x = list(str(a))
    y = list(str(b))
    x.sort()
    y.sort()
    return x == y


primeList()

# make a list of anagram numbers
for i in range(len(prim)):
    for j in range(len(prim)):
        if prim[i] is not prim[j]:
            if anagram(prim[i], prim[j]):
                if prim[i] not in anagram_list:
                    anagram_list.append(prim[i])
                if prim[j] not in anagram_list:
                    anagram_list.append(prim[j])

# ==================================================
