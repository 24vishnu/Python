
notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def change(my_money):
	count = 0
	i = 0
	while(my_money > 0):
		count += (my_money//notes[i])
		my_money = my_money%notes[i]
		i += 1
	return count