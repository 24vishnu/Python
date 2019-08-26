# ---------------------------------- prg-----------------------------------------------
# Harmonic_number.py
# date : 26/08/2019
#Calculate Nth Harmonic mumber

def Nth_Number(n):

    #Set initial Nth harmonic value is 0
    res = 0

    for i in range(1,n+1,1):
        #calculate 1/i and add previpous result
        res += (1/i)

    # return the calculated result value 
    return round(res,5)