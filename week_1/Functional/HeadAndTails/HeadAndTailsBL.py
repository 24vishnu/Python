# ---------------------------------- prg-----------------------------------------------
# HeadsAndTails.py
# date : 26/08/2019
# print the percentage of head and tail in N time of tass


import random


# we create a class name coins
class coins:

    # We create static method because
    # static method does not receive an implicit first argument.
    @staticmethod
    def calculate(N_times):

        # initial we take two variables head and tails and assign default value 0
        head = 0
        tails = 0
        i = 0

        while i < N_times:

            # generate random value between 0 and 1
            toss = random.random()

            # if random value is grater than 0.5 then head else tails
            if toss < 0.5:
                tails += 1
            else:
                head += 1

            i += 1

        # print percentage of get head and tails
        print("Percentage of head is : ", round((head * 100) / N_times, 2))
        print("Percentage of tails is : ", round((tails * 100) / N_times, 2))
