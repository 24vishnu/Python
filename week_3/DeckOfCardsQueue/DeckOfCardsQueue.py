"""
Write a Program DeckOfCards.py , to initialize deck of cards having
suit ("Clubs", "Diamonds", "Hearts", "Spades") &
Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace").
Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
Print the Cards the received by the 4 Players in the sorting order
"""

import DeckOfCardsQueueBL as card_obj

# First user initiate the game
play = card_obj.card_game()

# one user take all playing cards
play.create_cards()

# Now user shuffle cards
play.shuffle_Cards()

# Now distribute these cards
play.disrtibute_and_sort_card()

# put card in a sequence
play.add_card_queue()

# print cards one by one from sequence
play.print_players_cards()
