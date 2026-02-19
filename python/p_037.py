import time
start_time = time.time()
from sympy import isprime

NumberOfPrimes  = 0
Number          = 10

SumOfTruncatedPrimes = 0

while NumberOfPrimes < 11:
    if isprime(Number):
        Number_String = str(Number)
        NumberLength = len(Number_String)

        Left_Prime = 1
        Right_Prime = 1
        for i in range(NumberLength - 1):
            Truncated_Number_Right = int(Number_String[(i + 1)::])     
            Truncated_Number_Left = int(Number_String[:(NumberLength - (i+1)):])
            if isprime(Truncated_Number_Left) == False:
                Left_Prime = 0
            if isprime(Truncated_Number_Right) == False:
                Right_Prime = 0

        if (Right_Prime + Left_Prime) == 2:
            NumberOfPrimes += 1
            print(NumberOfPrimes, Number)
            SumOfTruncatedPrimes += Number

    Number += 1

print(SumOfTruncatedPrimes)
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")
        