def check(N):
    i = 0
    j = N-1
    while(i <= j):
    	m = i+(j-i)//2
    	print("Is this your number : ", m)
    	reply1 = int(input("Enter your answer if Yes then 1 else 0 : "))
    	if(reply1 == 1):
    		print("Ab to thik h mil gaya na tumhara soch huaa number")
    		return
    	else:
    		reply2 = int(input("If your number is grater than then Enter 1 else 0 : "))
    		if(reply2 == 1):
    			i = m+1
    		else:
    			j = m-1
    print("You are lier your number is not in this range")  