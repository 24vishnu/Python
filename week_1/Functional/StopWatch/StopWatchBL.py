import time

def startWatch(ready):
    if(ready == 1):
    	start = time.time()
    	stop = int(input("Enter 1 if you want to stop your timer : "))
    	if(stop == 1):
    		print("your total time is : ",round((time.time()-start)),"Sec")
    else:
        print("You have to enter 1 only. please try again")

