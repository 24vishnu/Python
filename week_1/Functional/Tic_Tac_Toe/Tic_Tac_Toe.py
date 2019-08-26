'''
Desc ­> Write a Program to play a Cross Game or Tic­Tac­Toe Game. Player 1 is
the Computer and the Player 2 is the user. Player 1 take Random Cell that is the
Column and Row.

I/P ­> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’

Logic ­> The User or the Computer can only take the unoccupied cell. The Game
is played till either wins or till draw...

O/P ­> Print the Col and the Cell after every step.
Hint ­> The Hints is provided in the Logic. Use Functions for the Logic...
'''

import sys
import Tic_Toc_ToeBL as ob

# play game till any one not win or draw
# for i in range(9):
i = 0
while(i < 9):
    
	#condition for player one
	if(i%2 == 0):
		print("Enter player1 position (xy) : ")
		x = int(input())
		y = int(input())

		if(ob.check(x,y) == True):
			ob.put_value(x,y,i%2)

			#Check player win or not
			if(ob.check_win('X') == True):
				print("player1 You win :")
				ob.print_game()
				sys.exit()
				
			# print current status of game
			ob.print_game()

		# if given place not free to move
		else:
			print("This place allready filled :")
			i -= 1

	#condition for player 2
	else:
		print("Enter player2 position (xy) : ")
		x = int(input())
		y = int(input())

		#check filling condition
		if(ob.check(x,y) == True):
			ob.put_value(x,y,i%2)

			#check winning condition
			if(ob.check_win('O') == True):
				print("player2 You win :")
				ob.print_game()
				sys.exit()

			ob.print_game()

		# if place is already filled
		else:
			print("This place allready filled :")
			i -= 1
	i += 1
	
# if no one is win drow
print("Draw game")
