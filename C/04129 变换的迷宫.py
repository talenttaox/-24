from collections import deque
def find(maze,r,c):
    for i in range(r):
        for j in range(c):
            if maze[i][j]=='S':
                return (i,j)
    
def bfs(maze,r,c,k):
    x0,y0=find(maze,r,c)          
    a=deque()
    a.append((x0,y0,0,0))
    visited=set()
    visited.add((x0,y0,0))

    while a:
        x,y,mod,step=a.popleft()
        if maze[x][y]=='E':
            return step
        for i in range(4):
            x1=x+dx[i]
            y1=y+dy[i]
            if 0<=x1<r and 0<=y1<c:
                nmod=(mod+1)%k
                if maze[x1][y1]=='#' and nmod!=0:
                        continue
                if (x1,y1,nmod) not in visited:
                    a.append((x1,y1,nmod,step+1))
                    visited.add((x1,y1,nmod))
    return 'Oop!'

t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(t):
    r,c,k=map(int,input().split())
    maze=[]
    for i in range(r):
        maze.append(input())
    print(bfs(maze,r,c,k))