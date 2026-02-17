# Project Euler - 93 - Arithmetic Expressions
# Solution by Dominik Szombathy 
# Date - 2026.02.17

# Solution: ###

from itertools import combinations, permutations, product
from fractions import Fraction

# Define arithmetic operations safely
def apply_operator(op, x, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        if y == 0:
            return None
        return x / y

# All possible parenthesization structures for 4 numbers
def evaluate_all(nums, ops):
    a, b, c, d = nums
    o1, o2, o3 = ops
    results = set()

    try:
        # ((a o1 b) o2 c) o3 d
        r = apply_operator(o3, apply_operator(o2, apply_operator(o1, a, b), c), d)
        if r is not None:
            results.add(r)

        # (a o1 (b o2 c)) o3 d
        r = apply_operator(o3, apply_operator(o1, a, apply_operator(o2, b, c)), d)
        if r is not None:
            results.add(r)

        # a o1 ((b o2 c) o3 d)
        r = apply_operator(o1, a, apply_operator(o3, apply_operator(o2, b, c), d))
        if r is not None:
            results.add(r)

        # a o1 (b o2 (c o3 d))
        r = apply_operator(o1, a, apply_operator(o2, b, apply_operator(o3, c, d)))
        if r is not None:
            results.add(r)

        # (a o1 b) o2 (c o3 d)
        r = apply_operator(o2, apply_operator(o1, a, b), apply_operator(o3, c, d))
        if r is not None:
            results.add(r)

    except ZeroDivisionError:
        pass

    return results

def consecutive_length(values):
    n = 1
    while n in values:
        n += 1
    return n - 1

def solve():
    ops = ['+', '-', '*', '/']
    best_run = 0
    best_digits = None

    for digits in combinations(range(1, 10), 4):
        results = set()

        for perm in permutations(digits):
            nums = [Fraction(x) for x in perm]

            for opset in product(ops, repeat=3):
                values = evaluate_all(nums, opset)
                for v in values:
                    if v > 0 and v.denominator == 1:
                        results.add(int(v))

        run = consecutive_length(results)

        if run > best_run:
            best_run = run
            best_digits = digits

    return best_digits, best_run

if __name__ == "__main__":
    digits, run = solve()
    print("Best digits:", "".join(map(str, digits)))
    print("Longest run:", run)