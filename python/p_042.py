from sympy import isprime
import numpy as np
from itertools import permutations
import csv 

def TriangleNumberN(N):
    return 0.5 * N * (N + 1)

def Word2Number(Word):
    return sum([ord(char) - 96 for char in Word.lower()])

TriangleNumbers = []
for i in range(1, 14*26):
    TriangleNumbers.append(TriangleNumberN(i))

TriangleNumbersInFile = 0
with open("Data/0042_words.txt", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        for word in row:
            if Word2Number(word) in TriangleNumbers:
                TriangleNumbersInFile += 1

print(TriangleNumbersInFile)
            


    