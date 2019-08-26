# ---------------------------------- prg-----------------------------------------------
# StopWatch.py
# date : 26/08/2019
# Find the total time from starting to stop time 

import time

def startWatch(ready):
    	
    if(ready == 1):
    	start = time.time()
		
		# take user input 1 when user want to stop there stop watch
    	stop = int(input("Enter 1 if you want to stop your timer : "))

		#if user want to stop then print time 
    	if(stop == 1):
    		print("your total time is : ",round((time.time()-start)),"Sec")
    else:
        print("You have to enter 1 only. please try again")

