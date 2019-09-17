# ----------------------------------------------Distribute cards in 4 player-----------------------------
# DeckOfCards.py
# Date : 30/08/2019
# Shuffle the cards using Random method and then distribute 9 Cards to 4 Players 
# and Print the Cards the received by the 4 Players
# ---------------------------------------------------------------------------------------------

import random

suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
Rank = ["2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:", "Jack:", "Queen:", "King:", "Ace:"]
cards = []
Shuffle = []


# create_cards() method is used for 52 card every suit have 13 rank
def create_cards():
    for i in range(13):
        cards.append(Rank[i] + suit[0])
        cards.append(Rank[i] + suit[1])
        cards.append(Rank[i] + suit[2])
        cards.append(Rank[i] + suit[3])


# shuffle_Card() method is shuffle all cards
def shuffle_Cards():
    while len(cards) > 0:
        card = random.choice(cards)
        Shuffle.append(card)
        cards.remove(card)

    # cards = Shuffle


# distribute() method is N equal cards for each player (4)
def distribute(N, p):
    # print('--------\t---------\t---------\t--------')
    # print('Player1 \t player2 \t Player3 \t Player4')
    # print('--------\t---------\t---------\t--------')
    for i in range(1, ((N * p) + 1), 1):
        if i % p == 0:
            print(' \t {}'.format(Shuffle[i - 1]))
        else:
            print(Shuffle[i - 1], end=' \t {}'.format(''))


create_cards()