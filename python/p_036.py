MaxNumber = 1000000

def is_symmetric(Number):
    Number_string = str(Number)
    return list(str(Number)) == list(reversed(Number_string))

Sum = 0
for N in range(MaxNumber + 1):
    if is_symmetric(N):
        if bin(N)[2:] == (bin(N)[2:])[::-1]:
            Sum += N

print(Sum)