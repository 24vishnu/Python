# ---------------------------------- prg-----------------------------------------------
# Anagram_Palindrom_prime.py
# date : 26/08/2019
# Find the prime anagram and palindrome number


# Check number is prime or not
def prime(num):
    try:
        num = int(num)
    except ValueError:
        return False

    if num < 2:
        return False
    if num == 2:
        return True
    i = 2
    while i * i < num:
        if num % i == 0:
            return False
        i += 1
    return True


# Check two numbers are anagram or not
def anagram(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    return ''.join(sorted(s1)) == ''.join(sorted(s2))


"""
    li = [0] * 10

    for i in range(len(s2)):
        if int(s2[i]) == 0:
            return False
        li[int(s2[i])] += 1

    for i in range(len(s1)):
        if int(s1[i]) == 0:
            return False
        li[int(s1[i])] -= 1

    flag = True

    for i in range(1, 10, 1):
        if li[i] != 0:
            flag = False
            break

    return flag
"""


# check number is palindrome or not
def palind(num):
    s1 = str(num)
    return ''.join(reversed(s1)) == s1


"""
    s2 = ""

    for i in range(len(s1)):
        s2 = s1[i] + s2

    if s1 == s2:
        return True
    return False
"""

prime_numbers = []
anagram_numbers = []
palindrom_Numbers = []
anagram_and_palindrom = []

# make a list of prime numbers and another list of palindrome numbers
for i in range(1, 1000, 1):

    if prime(i):
        prime_numbers.append(i)
        if palind(i):
            palindrom_Numbers.append(i)

# make a list of anagram and palindrome numbers
for i in range(len(palindrom_Numbers)):
    for j in range(i, len(prime_numbers), 1):
        if palindrom_Numbers[i] != prime_numbers[j]:

            if anagram(palindrom_Numbers[i], prime_numbers[j]):

                if palindrom_Numbers[i] not in anagram_and_palindrom:
                    anagram_and_palindrom.append(palindrom_Numbers[i])

                if prime_numbers[j] not in anagram_and_palindrom:
                    anagram_and_palindrom.append(prime_numbers[j])

# make a list of anagram numbers
for i in range(len(prime_numbers)):
    for j in range(i, len(prime_numbers), 1):
        if prime_numbers[i] != prime_numbers[j]:

            if anagram(prime_numbers[i], prime_numbers[j]):

                if prime_numbers[i] not in anagram_numbers:
                    anagram_numbers.append(prime_numbers[i])

                if prime_numbers[j] not in anagram_numbers:
                    anagram_numbers.append(prime_numbers[j])
