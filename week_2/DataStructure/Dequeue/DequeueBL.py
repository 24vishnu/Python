# ---------------------------------- prg-----------------------------------------------
# Dequeue.py
# date : 26/08/2019
# Implement the Dequeue using linked list


class DeQueue:

    # Constructor
    def __init__(self, cap=None):
        if cap is not None:
            self.capacity = cap

        else:
            self.capacity = 10

        self.front = 0
        self.rear = 0
        self.queue = [-1] * self.capacity

    # Add Front
    def addFront(self, item):
        if (self.rear - self.front) == self.capacity:
            print('Queue is full')
            return

        temp = self.rear
        while temp > self.front:
            self.queue[temp] = self.queue[temp - 1]
            temp -= 1

        self.queue[temp] = item
        self.rear += 1

    # Add Rear
    def addRear(self, item):
        if (self.rear - self.front) == self.capacity:
            print('Queue is full')
            return

        self.queue[self.rear] = item
        self.rear += 1

    # Remove Front
    def removeFront(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return

        data = self.queue[self.front]
        for i in range(self.front, self.rear):
            self.queue[i] = self.queue[i + 1]

        self.rear -= 1
        return data

    # Remove Rear
    def removeRear(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return

        data = self.queue[self.rear - 1]
        self.rear -= 1
        return data

    # IsEmpty
    def isEmpty(self):
        return self.front == self.rear

    # size
    def size(self):
        return self.rear - self.front

    # print the queue
    def display(self):
        for i in range(self.front, self.rear):
            print(self.queue[i], end=' ')
