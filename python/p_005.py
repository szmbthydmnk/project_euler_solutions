# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

import math

def euler5(n):
    num = 1
    for i in range(1,n):
        num *= i//(math.gcd(i,num))
    return num

print(euler5(20))
