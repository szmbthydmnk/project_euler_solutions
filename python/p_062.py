# Cubic Permutations

Numbers     = []
Occurances  = []
for n in range(2, 20000):
    cube = n**3
    sorted_cube = ''.join(sorted(str(cube)))
    if sorted_cube in Numbers:
        index = Numbers.index(sorted_cube)
        Occurances[index] += 1
    else:
        Numbers.append(sorted_cube)
        Occurances.append(1)

indices = []
for i in range(len(Occurances)):
    if Occurances[i] == 5:
        indices.append(i)

for index in indices:
    n = Numbers[index]
    for m in range(2, 20000):
        if ''.join(sorted(str(m**3))) == n:
            print(m**3)
            break
