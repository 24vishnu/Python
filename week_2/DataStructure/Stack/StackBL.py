# ---------------------------------- prg-----------------------------------------------
# Stack.py
# date : 26/08/2019
# check parenthesis is balance or not and implement all stack functionality


import sys


def checkExpre(arithmetic_expression):
    for i in arithmetic_expression:

        if i is '(':
            st.push(i)

        elif i is ')':

            if st.isEmpty() or st.peek() != '(':
                return False

            st.pop()

    return st.isEmpty()


class Stack:
    # 1 Constructor
    def __init__(self):
        self.capacity = 10
        self.top = 0
        self.mystack = [-1] * 10

    # 2 push element in stack on top
    def push(self, item):
        if self.top == self.capacity:
            print("Over flow : ")
            return
        self.mystack[self.top] = item
        self.top += 1

    # 3 delete top element from stack
    def pop(self):
        if self.top == -1:
            print("stack is Empty :")
            return
        self.top -= 1

    # 4 return top element from stack
    def peek(self):
        if self.top == -1:
            print('Stack Empty : ')
            return -1
        return self.mystack[self.top - 1]

    # 5 return size of stack
    def size(self):
        return self.top

    # 6 check stack is empty or not
    def isEmpty(self):
        return self.top == 0

    # 7 display method
    def display(self):
        for i in range(self.top):
            print(self.mystack[i], end=' ')


st = Stack()
