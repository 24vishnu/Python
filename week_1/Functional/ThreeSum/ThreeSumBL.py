# ---------------------------------- prg-----------------------------------------------
# ThreeSum.py
# date : 26/08/2019
# Calcutate the three number whose sum is zero

#calculate number of distinct triplets 
def three_sum(nums):

    nums.sort()
    ll = []

    for i in range(len(nums)-2):

        for j in range(i+1,len(nums)-1,1):

            for k in range(j+1,len(nums),1):

                if(nums[i]+nums[j]+nums[k] == 0):
                    l1 = [nums[i],nums[j],nums[k]]

                    # if numbers are distinct then add in list
                    if(l1 not in ll):
                        ll.append(l1)
    #return list of all distinct triples whose sum is zero
    return ll