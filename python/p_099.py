import numpy as np
import csv

# Lists to store the numbers
a_values = []
b_values = []

# Open the file and read line by line
with open("/Volumes/THYMac/Users/ThyDominik/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0099_base_exp.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # Assume each row has two elements: base and exponent
        a = int(row[0].strip())
        b = int(row[1].strip())
        a_values.append(a)
        b_values.append(b)


MaximalNumber       = 0
MaximalNumberIndex  = 0
for LineIndex in range(0, len(a_values)):
    LineNumber = b_values[LineIndex] * np.log10(a_values[LineIndex])
    if MaximalNumber < LineNumber:
        print("Maximal number \t = ", MaximalNumber, " \t ||| \t New Number \t = ", LineNumber, " Index: ", LineIndex)
        MaximalNumber = LineNumber
        MaximalNumberIndex = LineIndex + 1
        
print(MaximalNumberIndex)