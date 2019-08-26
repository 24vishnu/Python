
# ---------------------------------- prg-----------------------------------------------
# Vending_machine.py
# date : 26/08/2019
# retrun the minimum number of notes of given money



notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def change(my_money):
    	
	count = 0
	i = 0

	while(my_money > 0):
		
		if(my_money//notes[i] > 0):
			print('Notes of ',notes[i],' : ',my_money//notes[i])
			count += (my_money//notes[i])
			my_money = my_money%notes[i]
		i += 1

	return count