# Path sum: Three ways

import numpy as np

Path = "/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0082_matrix.txt"
with open(Path, "r") as f:
    Matrix = np.array([[int(x) for x in line.strip().split(",")] for line in f])

N = Matrix.shape[0]
dp = np.zeros_like(Matrix)

# Initialize first column
dp[:, 0] = Matrix[:, 0]

# Dynamic programming: column by column
for j in range(1, N):
    # move right
    dp[:, j] = dp[:, j - 1] + Matrix[:, j]

    # move up
    for i in range(1, N):
        dp[i, j] = min(dp[i, j], dp[i - 1, j] + Matrix[i, j])

    # move down
    for i in range(N - 2, -1, -1):
        dp[i, j] = min(dp[i, j], dp[i + 1, j] + Matrix[i, j])

# The minimal path sum to reach the rightmost column
answer = dp[:, -1].min()
print(answer)