"""
Desc ­> Computes the prime factorization of N using brute force.
I/P ­> Number to find the prime factors
Logic ­> Traverse till i*i <= N instead of i <= N for efficiency .
O/P ­> Print the prime factors of number N.
"""

import PrimeFactorsBL as ob

# take a number from user
n = int(input("Enter a number : "))

# call method for print prime factor
ob.print_Prime_Factor(n)
