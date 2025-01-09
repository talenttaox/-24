import sys

sys.setrecursionlimit(300000)
input = sys.stdin.read


def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def dfs(x, y, water_height_value, m, n, h, water_height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_valid(nx, ny, m, n) and h[nx][ny] < water_height_value:
            if water_height[nx][ny] < water_height_value:
                water_height[x][y] = water_height_value
                dfs(nx, ny, water_height_value, m, n, h, water_height)


data = input().split()
idx = 0
k = int(data[idx])
idx += 1
results = []

for _ in range(k):
    m, n = map(int, data[idx:idx + 2])
    idx += 2
    h = []
    for i in range(m):
        h.append(list(map(int, data[idx:idx + n])))
        idx += n
    water_height = [[0] * n for _ in range(m)]

    i, j = map(int, data[idx:idx + 2])
    idx += 2
    i, j = i - 1, j - 1

    p = int(data[idx])
    idx += 1

    for _ in range(p):
        x, y = map(int, data[idx:idx + 2])
        idx += 2
        x, y = x - 1, y - 1
        if h[x][y] <= h[i][j]:
            continue

        dfs(x, y, h[x][y], m, n, h, water_height)

    results.append("Yes" if water_height[i][j] > 0 else "No")

sys.stdout.write("\n".join(results) + "\n")