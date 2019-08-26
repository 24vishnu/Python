import sys
import Tic_Toc_ToeBL as ob
arry2D = [] 								

for i in range(0,3):						
	arry2D.append([])						
for i in range(3):							
	for j in range(3):
		arry2D[i].append(j)					
		arry2D[i][j] = '-'					

def print_game():
	for i in range(3):						
		for j in range(3):
			print(arry2D[i][j],end=" ")
		print()
# print_game()
def put_value(x,y,ch):
	if(ch == 0):
		arry2D[x][y] = 'X'
	else:
		arry2D[x][y] = 'O'
def check(x,y):
	return arry2D[x][y]=='-'


# ++++++++++++++++++++++++++++++++++++++++++++
def check_win(ch):
	# // [0 0 0]
	# // [1 1 1]
	# // [2 2 2]
# Horizontal check
	for i in range(3):
		count = 0
		for j in range(3):
			if(arry2D[i][j] == ch):
				count+=1
			else:
				break
		if(count == 3):
			return True
# 	vertical check
	for i in range(3):		
		count = 0
		for j in range(3):
			if(arry2D[j][i] == ch):
				count+=1
			else:
				break
		if(count == 3):
			return True
# Diagonal 1
	count = 0
	for i in range(3):
		for j in range(3):
			if(i == j):
				if(arry2D[i][j] == ch):
					count+=1
				else:
					break
		if(count == 3):
			return True

# daigonal 2
	count = 0
	for i in range(3):
		for j in range(3):
			if((i+j) == 2):
				# print(i+j)
				if(arry2D[i][j] == ch):
					count+=1
				else:
					break
		if(count == 3):
			return True
	return False
# # ++++++++++++++++++++++++++++++++++++++++++++



# for i in range(9):
# 	if(i%2 == 0):
# 		print("Enter player1 position (xy) : ")
# 		x = int(input())
# 		y = int(input())
# 		if(ob.check(x,y) == True):
# 			ob.put_value(x,y,i%2)
# 			if(ob.check_win('X') == True):
# 				print("player1 You win :")
# 				ob.print_game()
# 				sys.exit()
# 				# return
# 			ob.print_game()
# 		else:
# 			print("This place allready filled :")
# 	else:
# 		print("Enter player2 position (xy) : ")
# 		x = int(input())
# 		y = int(input())
# 		if(ob.check(x,y) == True):
# 			ob.put_value(x,y,i%2)
# 			if(ob.check_win('O') == True):
# 				print("player2 You win :")
# 				ob.print_game()
# 				sys.exit()
# 				# return
# 			ob.print_game()
# 		else:
# 			print("This place allready filled :")
# print("Draw game")
