# import random
# count = 0
# with open('Number.txt',"w") as file_obj:
#     for i in range(100):
#         count += 1
#         file_obj.write(str(random.randint(1,1001)))
#         if count % 15 == 0:
#             file_obj.write(' \n')
#         else:
#             file_obj.write(' ')

def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
            
                s = l[:i] + l[i+1:]
                p = perm(s)
                for x in p:
                    print(l[i:i+1] , x)
                    r.append(l[i:i+1] + x)
    return r
print(perm('123'))
# perm('123')

# 123     1 23
# 23      2 3
# 3       3 
