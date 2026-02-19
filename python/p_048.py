import numpy as np

modulo = 10**10
Number = 0
for i in range(1, 1001):
    Number += pow(i, i, modulo)
    
print(Number % modulo)

