import numpy as np

# Path sum: Two Ways

Path = "/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0081_matrix.txt"
File = open(Path, "r")
Matrix = []
for line in File:
    Matrix.append([int(x) for x in line.split(",")])
File.close()

N = 80
dp = [0] * N

# Initialize a result matrix to store the minimum path sums
result = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            result[i][j] = Matrix[i][j]
        elif i == 0:
            result[i][j] = result[i][j-1] + Matrix[i][j]
        elif j == 0:
            result[i][j] = result[i-1][j] + Matrix[i][j]
        else:
            result[i][j] = Matrix[i][j] + min(result[i-1][j], result[i][j-1])

print(result[N-1][N-1])

import matplotlib.pyplot as plt

# Backtrack to find the path taken
path = []
i, j = N-1, N-1
while i > 0 or j > 0:
    path.append((i, j))
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    else:
        if result[i-1][j] < result[i][j-1]:
            i -= 1
        else:
            j -= 1
path.append((0, 0))
path = path[::-1]

# Plot the result matrix
plt.imshow(result, cmap='viridis')
plt.colorbar()

# Overlay the path
path_y, path_x = zip(*path)
plt.plot(path_x, path_y, color='red', linewidth=2)

plt.title("Minimum Path Sum and Path")
plt.show()

