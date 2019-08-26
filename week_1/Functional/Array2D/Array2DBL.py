def method2D(n,m):
    # we take a empty list name array_2D initially this is empty
	array_2D = [] 								
    
	# for loop for create n number or inner list in the empty list
	# append empty list in every row
	for i in range(0,n):						
		array_2D.append([])						

	'''
	initialise 2D list n row and m column
	in each row we appent the m number of elements
	and now intialise with 0 (zero) of every row	
	'''
	for i in range(n):							
		for j in range(m):
			array_2D[i].append(j)					
			array_2D[i][j] = 0				

	#Taking the value for every index of each row from user and assign value at perticular position
	for i in range(n):
		for j in range(m):
		    x = input("Enter value for array ")	
		    array_2D[i][j] =  x		

	'''
	we are open a file and write the all value of 
	arry_2D into the file in form of row and column

	If file not exist then create the new file as same name
	'''
	f = open("File2D_Print.txt", "w")				
	for i in range(n):
		for j in range(m):
			f.write(str(array_2D[i][j]))			
			f.write(' ')						
		f.write('\n')
	#close the file						
	f.close()		