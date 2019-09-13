# ---------------------------------- prg-----------------------------------------------
# My_Number.py
# date : 26/08/2019
# find a number using binary search


def check(N):
    i = 0
    j = N - 1

    while i <= j:

        # take a middle number
        m = i + (j - i) // 2

        # Ask the user is this his number
        print("Is this your number : ", m)
        reply1 = int(input("Enter your answer if Yes then 1 else 0 : "))

        if reply1 == 1:
            print("Ab to thik h mil gaya na tumhara soch huaa number")
            return

        # if no then ask number is grater than or less then
        else:
            reply2 = int(input("If your number is grater than then Enter 1 else 0 : "))
            if reply2 == 1:
                i = m + 1

            else:
                j = m - 1

    print("You are liar your number is not in this range")
