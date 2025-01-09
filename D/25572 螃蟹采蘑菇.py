from collections import deque
def bfs(sx1,sy1,dsx,dsy):
    queue=deque()
    queue.append((sx1,sy1))
    visited=set()
    visited.add((sx1,sy1))
    while queue:
        x1,y1=queue.popleft()
        if maze[x1][y1]==9 or maze[x1+dsx][y1+dsy]==9:
            return 'yes'
        for i in range(4):
            nx1,ny1=x1+dx[i],y1+dy[i]
            if 0<=nx1<n and 0<=ny1<n and 0<=nx1+dsx<n and 0<=ny1+dsy<n and ((nx1,ny1) not in visited):
                if maze[nx1][ny1]!=1 and maze[nx1+dsx][ny1+dsy]!=1:
                    queue.append((nx1,ny1))
                    visited.add((nx1,ny1))
    return 'no'

n=int(input())
maze=[]
start=[]
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        if row[j]==5:
            start.append((i,j))
    maze.append(row)
#print(start)
sx1,sy1=start[0]
sx2,sy2=start[1]
dsx,dsy=sx2-sx1,sy2-sy1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
print(bfs(sx1,sy1,dsx,dsy))