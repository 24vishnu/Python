'''
Desc ­> Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.

I/P ­> Panel to add People to Queue to Deposit or Withdraw Money and dequeue

Logic ­> Write a Queue Class to enqueue and dequeue people to either deposit
or withdraw money and maintain the cash balance

O/P ­> True or False to Show Arithmetic Expression is balanced or not.
'''

import QueueBL

print('How many people in queue : ')
quSize = int(input())

qu = QueueBL.Queue(quSize)

print('Hi.. Manager what is the total money today in bank : ')
bankBalance = int(input())

remaningCase = qu.remaining_mony(bankBalance,quSize)
print('now remaining money in the bank is : ',remaningCase)

