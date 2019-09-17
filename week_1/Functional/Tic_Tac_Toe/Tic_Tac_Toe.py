"""
Desc ­> Write a Program to play a Cross Game or Tic­Tac­Toe Game. Player 1 is
the Computer and the Player 2 is the user. Player 1 take Random Cell that is the
Column and Row.

I/P ­> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’

Logic ­> The User or the Computer can only take the unoccupied cell. The Game
is played till either wins or till draw...

O/P ­> Print the Col and the Cell after every step.
Hint ­> The Hints is provided in the Logic. Use Functions for the Logic...
"""

import sys
import Tic_Toc_ToeBL as ob

# play game till any one not win or draw
# for i in range(9):
map_dict = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
}
i = 0

while i < 9:
    if i % 2 == 0:
        while True:
            position = input("Enter player1 position (1 to 9) : ")
            try:
                position = int(position)
            except ValueError:
                print('Please Enter only numbers ')
                continue
            if 1 <= position < 10:
                break
            else:
                print('Enter only (1 to 9) : ')
        x = map_dict[position][0]
        y = map_dict[position][1]

        if ob.check(x, y):
            ob.put_value(x, y, i % 2)

            # Check player win or not
            if ob.check_win('X'):
                print("player1 You win :")
                ob.print_game()
                sys.exit()

            # print current status of game
            ob.print_game()
        # if given place not free to move
        else:
            print("This place already filled :")
            i -= 1
    else:
        while True:
            position = input("Enter player2 position (1 to 9) : ")
            try:
                position = int(position)
            except ValueError:
                print('Please Enter only numbers ')
                continue
            if 1 <= position < 10:
                break
            else:
                print('Enter only (1 to 9) : ')
        x = map_dict[position][0]
        y = map_dict[position][1]
        if ob.check(x, y):
            ob.put_value(x, y, i % 2)

            # check winning condition
            if ob.check_win('O'):
                print("player2 You win :")
                ob.print_game()
                sys.exit()

            ob.print_game()

        # if place is already filled
        else:
            print("This place already filled :")
            i -= 1
    i += 1
print("Draw game!!")
