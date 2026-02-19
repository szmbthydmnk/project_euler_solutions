# Project Euler 97
# Find the last ten digits of the non-Mersenne prime:
# 28433 × 2^7830457 + 1

def solve():
    MOD = 10**10
    exponent = 7830457
    base = 2
    multiplier = 28433

    result = (multiplier * pow(base, exponent, MOD) + 1) % MOD
    return result

if __name__ == "__main__":
    print("Answer:", solve())
