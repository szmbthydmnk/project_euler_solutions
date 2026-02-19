#problem 23:

#Abundant number: the sum of the divisors of the number is greater than the number.

def euler23():
    from Functions import Divisors, IsAbundant
    Limit = 28123

    AbundantNumbers = []
    for i in range(1, Limit):
        if IsAbundant(i) == True:
            AbundantNumbers.append(i)
    temp_mtx = []
    for i in range(0, len(AbundantNumbers)-1):
        for j in range(i,  len(AbundantNumbers)-1):
            temp_mtx.append(AbundantNumbers[i] + AbundantNumbers[j])

    SumOfAll = sum(i for i in range(1, Limit))

    SumOfAbundants = 0
    for i in list(set(temp_mtx)):
        if i < Limit:
            SumOfAbundants += i
            
    return SumOfAll - SumOfAbundants
print(euler23())
