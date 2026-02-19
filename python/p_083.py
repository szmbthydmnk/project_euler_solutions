# Path sum: Four ways


Path = "/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0083_matrix.txt"

with open(Path, "r") as f:
    Matrix = [[int(x) for x in line.strip().split(",")] for line in f]

N = len(Matrix)
M = len(Matrix[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
distances = [[float('inf')] * M for _ in range(N)]
distances[0][0] = Matrix[0][0]

visited = [[False] * M for _ in range(N)]

while True:

    min_distance = float('inf')
    x = y = -1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and distances[i][j] < min_distance:
                min_distance = distances[i][j]
                x, y = i, j


    if x == -1:
        break
    
    visited[x][y] = True

    if (x, y) == (N - 1, M - 1):
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            new_distance = distances[x][y] + Matrix[nx][ny]
            if new_distance < distances[nx][ny]:
                distances[nx][ny] = new_distance

print(distances[N - 1][M - 1])
