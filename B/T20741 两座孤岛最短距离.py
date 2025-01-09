from collections import deque
n=int(input())
land=[list(map(int, input())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
queue = deque()

def dfs(x, y, land, n, queue):
    land[x][y]=2
    queue.append((x,y,0))
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and land[nx][ny] == 1:
            dfs(nx,ny,land,n,queue)

def bfs(land,n,queue):
    while queue:
        x,y,length=queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if land[nx][ny]==1:
                    return length
                elif land[nx][ny]==0:
                    land[nx][ny]=2
                    queue.append((nx,ny,length+1))

def output(land,n):
    for i in range(n):
        for j in range(n):
            if land[i][j]==1:
                dfs(i, j, land, n, queue)
                return bfs(land,n,queue)

print(output(land,n))