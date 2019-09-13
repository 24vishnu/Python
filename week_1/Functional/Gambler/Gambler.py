"""
Desc ­> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.

I/P ­> $Stake, $Goal and Number of times

Logic ­> Play till the gambler is broke or has won

O/P ­> Print Number of Wins and Percentage of Win and Loss.
"""

import GamblerBL as obj

'''
take user input  as Stake, Goal and Number of times player want to play
'''

while True:
    stake = (input('Enter the stack : '))
    # check user input is valid or not
    try:
        stake = int(stake)
    except ValueError:
        print('Please enter the valid number : ', type(stake))
        continue
    if stake >= 0:
        break
    else:
        print('Please enter positive number. ')

while True:
    goal = (input('what is your goal : '))
    # check user input is valid or not
    try:
        goal = int(goal)
    except ValueError:
        print('Please enter the valid number : ', type(goal))
        continue
    if goal >= 0:
        break
    else:
        print('Please enter positive number. ')


while True:
    number = input("How many time you want to play : ")
    # check user input is valid or not
    try:
        number = int(number)
    except ValueError:
        print('Please enter the valid number : ', type(number))
        continue
    if number >= 0:
        break
    else:
        print('Please enter positive number. ')

# call play function
obj.play(stake, goal, number)
