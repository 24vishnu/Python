'''
Desc ­> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).

I/P ­> The Harmonic Value N. Ensure N != 0

Logic ­> compute 1/1 + 1/2 + 1/3 + ... + 1/N

O/P ­> Print the Nth Harmonic Value.
'''

import Harmonic_NumberBL as obj

# Take user input N for find Nth Harmonic number
N = int(input("Enter a number : "))

#Call Nth_Number(parameter) and get the result
print(obj.Nth_Number(N))