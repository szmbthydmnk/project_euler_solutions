# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy as np

def euler3():
    num     = 600851475143
    sq_num  = int(np.sqrt(num))
    factors = []
    # for loop goes from 3 (num obviuosly not even) to the num bc num could be a prime
    for i in range(3, num):
        if num % i == 0:
            num //= i
            factors.append(i)
            if num == 1:
                break
    return max(factors)

print(euler3())
