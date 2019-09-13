# ---------------------------------- prg-----------------------------------------------
# Harmonic_number.py
# date : 26/08/2019
# Calculate Nth Harmonic number


def Nth_Number(number):
    # Set initial Nth harmonic value is 0
    res = 0

    for i in range(1, number + 1, 1):
        # calculate 1/i and add previous result
        res += (1 / i)

    # return the calculated result value 
    return res
