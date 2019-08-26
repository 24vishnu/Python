import Coupon_NumberBL

# Take the user input how many coupons user want to create distinct coupons
N = int(input("Enter N for find N distinct coupons : "))

# call our coupons generate function and store all unique coupons into a list
coupons = Coupon_NumberBL.N_coupons(N)

#display the our unique N coupons
print("Your distinct coupons : ",coupons)