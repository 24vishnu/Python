# ----------------------------------------------Distribute cards in 4 palyer-----------------------------
# DeckOfCardsQueue.py
# Date : 31/08/2019
# Shuffle the cards using Random method and then distribute 9 Cards to 4 Players 
# and sort these card then add in queue and Print the Cards the received by the 4 Players
# from queue 
# ---------------------------------------------------------------------------------------------

import random


# +++++++++++++++++++++++++++++++++ Implement Queue using Linked list +++++++++++++++++++++++
# Linked list class to create a node with data or empty (this is use only implement queue)
class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
        return


# ===============================================================
'''
In this class we implement the queue methods using linked list 
'''


class my_Queue:

    # -- constructor for queue
    def __init__(self):
        self.head = None
        self.rear = 0
        self.front = 0

        return

    # --enqueue(item) Method for Add item-----------------------------------
    def enqueue(self, item):

        if not isinstance(item, LinkedList):
            item = LinkedList(item)

        if self.head is None:
            self.head = item

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = item
        self.rear += 1

    # ----- dequeue() method for delete the top Item from queue -----------------------------
    def dequeue(self):

        if self.head is None:
            print('Under flow')
            return

        data = self.head.data
        self.head = self.head.next
        self.rear -= 1
        return data

    # -----isEmpty() method return true is queue is empty else return false ------------
    def isEmpty(self):

        # return self.head == None
        return self.rear == self.front

    # ----size() method Return the number of elements in the queue-------------------
    def size(self):
        return self.rear - self.front


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Following is the main game class here we use only queue methods
class card_game:

    # initial requirement for play game
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.Rank = ["2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:", "Jack:", "Queen:", "King:", "Ace:"]
        self.Rank = ["10", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "Ace:", "Jack:", "Queen:", "King:"]

        # Total cards
        self.cards = []
        # four players
        self.P1 = []
        self.P2 = []
        self.P3 = []
        self.P4 = []

        # Queue object for put in sequence all sorted cards for every player
        self.player1_cards = my_Queue()
        self.player2_cards = my_Queue()
        self.player3_cards = my_Queue()
        self.player4_cards = my_Queue()

    # create_cards() method is used for 52 card every suit have 13 rank
    def create_cards(self):
        for i in self.Rank:
            for j in self.suit:
                self.cards.append(i + j)

    # shuffle_Card() method is shuffel all cards
    def shuffle_Cards(self):
        random.shuffle(self.cards)

    # Sort cards
    def disrtibute_and_sort_card(self):
        count = 0

        while count < 9:
            card = random.choice(self.cards)
            self.P1.append(card)
            self.cards.remove(card)
            card = random.choice(self.cards)
            self.P2.append(card)
            self.cards.remove(card)
            card = random.choice(self.cards)
            self.P3.append(card)
            self.cards.remove(card)
            card = random.choice(self.cards)
            self.P4.append(card)
            self.cards.remove(card)
            count += 1

        self.P1.sort()
        self.P2.sort()
        self.P3.sort()
        self.P4.sort()

    def add_card_queue(self):
        for i in range(len(self.P1)):
            self.player1_cards.enqueue(self.P1[i])
            self.player2_cards.enqueue(self.P2[i])
            self.player3_cards.enqueue(self.P3[i])
            self.player4_cards.enqueue(self.P4[i])

    def print_players_cards(self):
        print('%15s %15s %15s %15s' % ('--------', '--------', "--------", '--------'))
        print('%15s %15s %15s %15s' % ('Player1', 'Player2', "Player3", 'Player4'))
        print('%15s %15s %15s %15s' % ('cards', 'cards', "cards", 'cards'))
        print('%15s %15s %15s %15s\n' % ('--------', '--------', "--------", '--------'))

        while self.player1_cards.size() > 0:
            print('%15s %15s %15s %15s' % (
                self.player1_cards.dequeue(), self.player2_cards.dequeue(), self.player3_cards.dequeue(),
                self.player4_cards.dequeue()))
