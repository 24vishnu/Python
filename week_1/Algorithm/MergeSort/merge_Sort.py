#Program for sort the list of data using merge sort and find the time use by sorting algorithm

import time
import MergeSortBL as ob


list_object = [3,5,2,8,23,1,67,9,3,78,19,32,53,83]
# list_object = ['vishnu', 'rahul', 'upender', 'vema', 'vinit', 'amit', 'bhasker']

startTime = time.time()
ob.merge_part(list_object)

print('Time : ',round(time.time()-startTime,10))

print(list_object)