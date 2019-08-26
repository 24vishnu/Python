import random

class coins:	
	@staticmethod
	def calculate(n):
		head = 0
		tails = 0
		i = 0
		while(i < n):
			toss = random.random()
			if toss < 0.5 :
				tails += 1
			else:
				head += 1
			i += 1
		print("Persentage of head is : ",round((head*100)/n , 2))
		print("Persentage of tails is : ",round((tails*100)/n , 2))