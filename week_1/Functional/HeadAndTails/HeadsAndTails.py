"""
I/P ­> The number of times to Flip Coin. Ensure it is positive integer .

Logic ­> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads

O/P ­> Percentage of Head vs Tails
"""

import HeadAndTailsBL as obj

# Take user input
while True:
    number = input("How many time you want to flip the coin \t : ")
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


# call logic function if user input is positive integer
if number > 0:
    obj.coins.calculate(number)
else:
    print('wrong input (input should be positive integer)')