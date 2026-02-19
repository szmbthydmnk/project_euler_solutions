n = 999
import math as m

# print(m.ceil(m.log10(n + 1)))



NumberOfNumbers = 0
for n in range(1, 25):
    for a in range(1, 10):

        Number = pow(a, n)

        if len(str(Number)) == n:

            NumberOfNumbers += 1
            print(Number)


print(NumberOfNumbers)