# ----------------------------------replace prg-----------------------------------------------
# Tic_Toc_Toe.py
# date : 26/08/2019
# play game and find the winning condition and palce the payer choice character in the user given position


import sys

# playing board
arry2D = []

# fill every box of playing board as empty like '-'
for i in range(0, 3):
    arry2D.append([])

for i in range(3):
    for j in range(3):
        arry2D[i].append(j)
        arry2D[i][j] = '-'


# print board status
def print_game():
    for i in range(3):
        for j in range(3):
            print(arry2D[i][j], end=" ")
        print()


# add player choice value in board
def put_value(x, y, ch):
    if ch == 0:
        arry2D[x][y] = 'X'
    else:
        arry2D[x][y] = 'O'


# return false if position is already filled
def check(x, y):
    return arry2D[x][y] == '-'


# ++++++++++++++++++++++++++++++++++++++++++++
# check winning condition
def check_win(ch):
    # // [0 0 0]
    # // [1 1 1]
    # // [2 2 2]

    # Horizontal check
    for i in range(3):

        count = 0

        for j in range(3):

            if arry2D[i][j] == ch:
                count += 1
            else:
                break

        if count == 3:
            return True

    # 	vertical check
    for i in range(3):

        count = 0

        for j in range(3):
            if arry2D[j][i] == ch:
                count += 1
            else:
                break

        if count == 3:
            return True

    # Diagonal 1
    count = 0

    for i in range(3):
        for j in range(3):

            if i == j:

                if arry2D[i][j] == ch:
                    count += 1
                else:
                    break

        if count == 3:
            return True

    # diagonal 2
    count = 0

    for i in range(3):
        for j in range(3):

            if (i + j) == 2:

                if arry2D[i][j] == ch:
                    count += 1
                else:
                    break

        if count == 3:
            return True

    return False
