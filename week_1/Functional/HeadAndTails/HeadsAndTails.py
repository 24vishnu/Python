'''
I/P ­> The number of times to Flip Coin. Ensure it is positive integer .

Logic ­> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads

O/P ­> Percentage of Head vs Tails
'''

import HeadAndTailsBL as obj

#Take user input
n = int(input("How many time you want to flip the coin \t : "))

# call logic fuunction if user input is positive integer
if(n>0):
    obj.coins.calculate(n)
else:
    print('wrong input (input should be positive integer)')