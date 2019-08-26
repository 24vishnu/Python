'''
Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Queue using
the Linked List and Print the Anagrams from the Queue. Note no Collection Library
can be used.
'''

import Queue_List_BL as QLL_obj
    

#==================================================
q = QLL_obj.QueueList()

print('Following are the numbers enQueue into queue : ')

for i in QLL_obj.anagram_list:
    print(i,end=' ')
    q.enQueue(i)
    # q.display()

print('\n\nFollowing are the numbers deQueue from queue : ')
while q.size() > 0:
    print(q.deQueue(),end=" ")
    
print()

