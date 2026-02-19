# Project euler 32. problem

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 
# 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity,39 x 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 99 * 99 = 9801 these are only 8 digits, so on the LHS we have at least 5 digits
# 100*100 = 10000 these are 10 digits, so again the LHS has at most 5 digits
# we can reformulate the question from a*b = c to c/a = b, so b has to be the divisor
# of c, meaning it is a whole number. If we search only the divisors it is enough to check up until
# sqrt(c) for it.

import math

def euler32():
    NoPandigital = 0
    for i in range(1, 10**5):
        if HasPandigitalProduct(i) == 1:
            NoPandigital += i

    return NoPandigital

def HasPandigitalProduct(a):
    for count in range(1, math.isqrt(a) + 1):
        if a % count == 0:
            NumberString = str(a) + str(count) + str(a // count)
            if "".join(sorted(NumberString)) == "123456789":
                return 1
    return 0

print(euler32())