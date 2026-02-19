# Diophantine Equation
# Problem 66

import tqdm
import matplotlib.pyplot as plt

def is_square(n):
    root = int(n**0.5)
    return root * root == n

def minimal_solution_x(D):
    m = 0
    d = 1
    a0 = a = int(D**0.5)
    num1, num = 1, a
    den1, den = 0, 1

    if a * a == D:
        return None  # No solution if D is a perfect square

    while num * num - D * den * den != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d

        num2, num1 = num1, num
        den2, den1 = den1, den
        num = a * num1 + num2
        den = a * den1 + den2

    return num

max_x = 0
result_D = 0
for D in tqdm.tqdm(range(2, 1001)):
    if is_square(D):
        continue
    x = minimal_solution_x(D)
    if x and x > max_x:
        max_x = x
        result_D = D

print(result_D)