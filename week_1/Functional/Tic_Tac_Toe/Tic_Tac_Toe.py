import sys
import Tic_Toc_ToeBL as ob

for i in range(9):
	if(i%2 == 0):
		print("Enter player1 position (xy) : ")
		x = int(input())
		y = int(input())
		if(ob.check(x,y) == True):
			ob.put_value(x,y,i%2)
			if(ob.check_win('X') == True):
				print("player1 You win :")
				ob.print_game()
				sys.exit()
				# return
			ob.print_game()
		else:
			print("This place allready filled :")
	else:
		print("Enter player2 position (xy) : ")
		x = int(input())
		y = int(input())
		if(ob.check(x,y) == True):
			ob.put_value(x,y,i%2)
			if(ob.check_win('O') == True):
				print("player2 You win :")
				ob.print_game()
				sys.exit()
				# return
			ob.print_game()
		else:
			print("This place allready filled :")
print("Draw game")
