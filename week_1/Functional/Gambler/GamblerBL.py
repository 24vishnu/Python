import random

def play(stake,goal,number):
    win = 0
    loss = 0
    flag = False
    i = 0
    while(i < number): 
               
        if(winner() == True):
            stake += 1
            win+=1
        else:
            stake -= 1
            loss += 1
        if(stake == 0):
            break
        if(stake == goal):
            flag = True
            break
        i+=1


    if(flag != True):
        print("Not Achive")
    else:
        print("yes Achive")

    # print("Total number of time win = ",win)
    # print("Total number of time loss = ",loss)
    print("Percentage of win : ",round((win*100)/(win+loss),2))
    print("Percentage of loss : ",round((loss*100)/(win+loss),2))


def winner():
    x = random.randint(0,1)
    # print(x)
    if(x == 0):
        return False
    else:
        return True
