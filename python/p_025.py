# problem 25:

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits.
import math

def FibonacciSequence(a0, a1, N):
    Seq = []
    Seq.append(1)
    Seq.append(1)

    if a0 == 0 and a1 == 0:
        for i in range(3, N):
            Seq.append(Seq[-1] + Seq[-2])

        return Seq
    elif N == 0:
        print(' Start from at least 3 pls')
    else:
        return a0 + a1

def HowManyDigits(Num):
    return (int(math.log10(abs(Num)) + 1))

def euler25():

    a0  = 1
    a1  = 1
    Fibonacci = FibonacciSequence(a0, a1, N = 1)

    N   = 2

    while HowManyDigits(Fibonacci) != 1000:
        N += 1
        Fibonacci = FibonacciSequence(a0, a1, N)
        a0 = a1
        a1 = Fibonacci

    return N

print(euler25())
