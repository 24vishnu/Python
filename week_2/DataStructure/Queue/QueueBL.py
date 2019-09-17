# ---------------------------------- prg-----------------------------------------------
# Queue.py
# date : 26/08/2019
# print the prime number in two dimension 


class Queue:
    # Constructor
    def __init__(self, cap=None):
        if cap is not None:
            self.capacity = cap
        else:
            self.capacity = 10
        self.front = 0
        self.rear = 0
        self.queue = [-1] * self.capacity

    # Enqueue
    def enQueue(self, item):
        if self.rear == self.capacity:
            print('Queue is full')
            return
        self.queue[self.rear] = item
        self.rear += 1

    # Dequeue
    def deQueue(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return

        data = self.queue[self.front]
        for i in range(self.front, self.rear):
            self.queue[i] = self.queue[i + 1]
        self.rear -= 1
        return data

    # display queue
    def display(self):
        if self.rear == self.front:
            print('Queue is empty :')
            return
        for i in range(self.front, self.rear):
            print(self.queue[i], end=' ')

    # IsEmpty
    def isEmpty(self):
        return self.front == self.rear

    # size
    def size(self):
        return self.rear - self.front

    # program function:
    def remaining_mony(self, currentMoney, total_people):
        q = Queue()

        for i in range(total_people):
            q.enQueue(currentMoney // total_people)

        print("Enter as following instructions: \n1 : withdraw \n2 : Deposit\n\t")
        total_money = currentMoney

        for i in range(total_people):
            print(q.size())

            print(i + 1, " : What you want withdraw or Deposit money : ")
            reply = int(input())

            if reply == 1:
                print('Enter your amount : ')
                amont = int(input())

                if amont > total_money // total_people:
                    print('You have insufficient amount in your account : ')
                    print('Your current amount is : ', q.deQueue())

                else:
                    # q.enQueue(total_money//total_people - amont)
                    currentMoney -= amont
                    print('Your current amount is : ', q.deQueue() - amont)
                    # q.deQueue()
            else:
                print("Enter amount for Deposit : ")
                amont = int(input())
                # q.enQueue(total_money//total_people + amont)
                currentMoney = currentMoney + amont
                print('Your current amount is : ', q.deQueue() + amont)
                # q.deQueue()

        return currentMoney
