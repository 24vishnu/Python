def Nth_Number(n):
    res = 0
    for i in range(1,n+1,1):
        res += (1/i)
    return round(res,5)