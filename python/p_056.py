
SumOfDigits = 0

for a in range(1, 100):
    for b in range(1, 100):
        Number = pow(a, b)
        TempSum = 0
        for s in str(Number):
            TempSum += int(s)
        if TempSum > SumOfDigits:
            SumOfDigits = TempSum
            
print(SumOfDigits)