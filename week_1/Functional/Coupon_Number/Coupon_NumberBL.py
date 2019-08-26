import random

'''
Following function is create N distinct coupons and 
store all coupons into a list and return that list of coupons
'''
def N_coupons(N):
    distinct_coupons = []
    count = 0

    while(len(distinct_coupons) < N):
        #Generate a random number
        randomNumber = random.randint(1,N)

        #If generated coupon is already exist into list then we not add that coupon into list
        if(randomNumber not in distinct_coupons):
            distinct_coupons.append(randomNumber)

        count += 1
    
    return distinct_coupons