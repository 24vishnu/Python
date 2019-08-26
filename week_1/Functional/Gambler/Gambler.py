'''
Desc ­> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.

I/P ­> $Stake, $Goal and Number of times

Logic ­> Play till the gambler is broke or has won

O/P ­> Print Number of Wins and Percentage of Win and Loss.
'''

import GamblerBL as obj

'''
take user input  as Stake, Goal and Number of times player want to play
'''
stake = int(input("how many stake you have : "))
goal = int(input("What is your goal : "))
number = int(input("How many time you want to play : "))

#call play function
obj.play(stake,goal,number)
