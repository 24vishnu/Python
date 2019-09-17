"""
Write a Program DeckOfCards.py , to initialize deck of cards having
suit ("Clubs", "Diamonds", "Hearts", "Spades") &
Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace").
Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
Print the Cards the received by the 4 Players
"""

import DeckOfCardsBL as card_obj

# shuffle our cards first
card_obj.shuffle_Cards()

# Ask to user how many player want to play
# and how many cards need to distribute for each player
N = int(input('Enter players : '))
P = int(input("card for each palyer "))

# check condition number of cards less than  and equle to 52 with respect to player distribution
if N * P <= 52:
    card_obj.distribute(P, N)
else:
    print("Equal distribution is not possible: ")
