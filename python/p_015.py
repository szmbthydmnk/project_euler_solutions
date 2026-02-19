# problem 015: on a 20 by 20 grid how many routes exist if one can only go down and right

# So this is just the pascal triangle. Every element of the triangle can be calculated
# as n choose k, where n is the row in the triangle and k is the kth term from left to right

import math

def euler15(N):
    ans = math.factorial(2*N)/(math.factorial(N) ** 2)
    return int(ans)
print(euler15(20))
