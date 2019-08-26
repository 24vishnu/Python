# ---------------------------------- prg-----------------------------------------------
# Gambler.py
# date : 26/08/2019
# play and find player is achive there goal before N+1 stack (iteration)


import random

def play(stake,goal,number):
    '''
    initially we take the variable win loss and flag and assigne defalt value 
    '''
    win = 0
    loss = 0
    flag = False
    i = 0

    while(i < number): 

        # if player win the add winning price into the stake else substract               
        if(winner() == True):
            stake += 1
            win+=1
        else:
            stake -= 1
            loss += 1

        # if player loss all there money then he/she can'nt play more
        if(stake <= 0):
            break
        
        # if player achive there goal then flag assigne True and break
        if(stake == goal):
            flag = True
            break
        i+=1
        
    # if flag True print achive otherwise print not achive there goal
    if(flag != True):
        print("Not Achive")
    else:
        print("yes Achive")

    # print percentage of there result of loss and win 
    print("Percentage of win : ",round((win*100)/(win+loss),2))
    print("Percentage of loss : ",round((loss*100)/(win+loss),2))

# this is winner function we take random value for win and loss of player
def winner():

    # random.randInt(start, end) 
    #generate random value between start and end values
    x = random.randint(0,1)

    if(x == 0):
        return False
    else:
        return True
