# ---------------------------------- prg-----------------------------------------------
# Stack_List.py date :
# 26/08/2019
# Implement the stack using Linked list and perform operation of prime number and anagram numbers and
# print reverse order

import random
import math


# This class for create a new node when calling there constructor with passing data (item)
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class stack_list:
    # This function use to initialize the empty stack
    def __init__(self):
        self.head = None
        self.top = 0
        return

    # Function for push the value in the stack
    def push(self, item):
        self.top += 1

        if not isinstance(item, LinkedList):
            item = LinkedList(item)

        if self.head is None:
            self.head = item
            return

        item.next = self.head
        self.head = item

    # Function for remove the item from top
    def pop(self):
        if self.top == 0:
            print('Stack is Empty : ')

        else:
            self.top -= 1
            self.head = self.head.next

    # return the top value of the stack
    def peek(self):
        if self.top == 0:
            print('Stack is Empty : ')

        else:
            data = self.head.data
            return data

    # Function to find the current size  of stack
    def size(self):
        return self.top

    # Function to check Stack is empty or not..
    def isEmpty(self):
        return self.top == 0

    # Function for print the value of stack
    def display(self):
        temp = self.head
        while temp is not None:
            print('\t', temp.data)
            temp = temp.next
        print()


# ===========================================
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
