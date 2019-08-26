def three_sum(nums):
    nums.sort()
    ll = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1,1):
            for k in range(j+1,len(nums),1):
                if(nums[i]+nums[j]+nums[k] == 0):
                    l1 = [nums[i],nums[j],nums[k]]
                    if(l1 not in ll):
                        ll.append(l1)
    return ll