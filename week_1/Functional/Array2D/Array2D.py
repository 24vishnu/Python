import Array2DBL

# Take the input from user for row of array
n = int (input("Enter N for size "))

# Take the input from user for column of array
m = int (input("Enter M for size "))

'''
we are passing size of row (n) and column (m) in method2D()
this method take the (n*m) vcalues form user and write into the file 
'''
Array2DBL.method2D(n,m)				
