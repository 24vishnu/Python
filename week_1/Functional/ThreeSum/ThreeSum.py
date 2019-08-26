'''
Desc ­> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.

I/P ­> N number of integer, and N integer input array

Logic ­> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0

O/P ­> One Output is number of distinct triplets as well as the second output is to
print the distinct triplets.
'''

import ThreeSumBL as ob 

# list of data to find distinct triples
ll_object = [-1,0,8,-2,2,4,-4,3,-2,-2,7,3,-4,1]

#print all unique tripls by callinif three_sum method
print(ob.three_sum(ll_object))
