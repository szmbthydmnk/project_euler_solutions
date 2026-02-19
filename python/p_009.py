# problem 009: Pythagorean triplet finding with condition that a + b + c = 1000

import numpy as np

def euler9():
    # a + b + c = 1000
    # a^2 + b^2 = c^2
    # a < b < c
    # it can be solced using 2 paramters m and m>n
    #a = k * (m^2 - n^2)
    #b = k * (2*m*n)
    #c = k* m^2 + k * n^2
    #divisors = [2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500]
    divisors = []
    for i in range(2, int(np.sqrt(1000)) + 1):
        if 1000 % i == 0:
            divisors.append(i)
            divisors.append(1000/i)
    divisors.sort()
    for m in range(2, int(np.sqrt(1000)) + 1):
        for n in range(1,m):
            for k in divisors:
                if ((1000/(2*k)) - (m*m) - (m*n)) == 0:
                    a = k*(m**2 - n**2)
                    b = k*(2*m * n)
                    c = k*(m**2 + n**2)
                    return a*b*c

print(euler9())
