# problem 012: Find the first triangle number that has 500 hundred divisors.
import numpy as np

def divisors(num):
    divisors = 2
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            divisors += 2
            if i == np.sqrt(num):
                divisors -= 1
    return divisors    #bc the problem counts 1 and the number itself

def euler12(nod):   #number of divisors needed for the problem
    num = 3
    i   = 3        #starting from the first non trivial triangle number
    div = 0
    while div < nod:
        num += i
        i += 1
        div = divisors(num)

    return num

print(euler12(500))
