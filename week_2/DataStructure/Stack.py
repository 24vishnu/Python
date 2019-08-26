import sys
class Stack:
#1 Constructor
    def __init__(self):
        self.capacity = 10
        self.top = -1
        self.mystack = [-1]*10
#2 push element in stack on top
    def push(self,item):
        if self.top == self.capacity:
            print("Over flow : ")
        self.mystack[self.top] = item
        self.top += 1
#3 delete top element from stack
    def pop(self):
        if self.top == -1:
            print("stack is Empty :")
            return
        self.top -= 1
#4 return top element from stack
    def peek(self):
        if(self.top == -1):
            print('Stack Empty : ')
            return -1
        return self.mystack[self.top-1]       
#5 return size of stack
    def size(self):
        return self.top + 1
#6 check stack is empty or not
    def isEmpty(self):
        return self.top == -1
#7 perform opoeration 
    def checkExpre(self, AE):
        st = Stack()
        for i in AE:
            if i is '(':
                st.push(i)
            elif i is ')':
                if st.isEmpty() is True and st.peek() != '(':
                    print(False)
                    sys.exit(0)
                st.pop()
        return st.isEmpty()

expression = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)' #input()
st = Stack()
print(st.checkExpre(expression))

# for i in expression:
#     if i is '(':
#         st.push(i)
#     elif i is ')':
#         if st.peek() != '(' and st.isEmpty() is True:
#             print(False)
#             sys.exit(0)
#         st.pop()
# print(st.isEmpty())
    