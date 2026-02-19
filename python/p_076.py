# Counting Summations

Number = 100

ways = [0] * (Number + 1)
ways[0] = 1
for i in range(1, Number):  # i is the current number we are adding
    for j in range(i, Number + 1): # j is the current total we are forming
        ways[j] += ways[j - i] # add the ways we can form j-i to ways we can form j

print(ways[Number])
