import Coupon_NumberBL

# Take the user input how many coupons user want to create distinct coupons
while True:
    N = (input("Enter N for find N distinct coupons : "))
    # check user input is valid or not
    try:
        N = int(N)
    except ValueError:
        print('Please enter the valid number : ', type(N))
        continue
    if N >= 0:
        break
    else:
        print('Please enter positive number. ')

# call our coupons generate function and store all unique coupons into a list
coupons = Coupon_NumberBL.N_coupons(N)

# display the our unique N coupons
print("Your distinct coupons : ", coupons)
