def dfs(x,y,num):
    global max_num,best_path
    if x==n-1 and y==m-1:
        if num>max_num:
            max_num=num
            best_path=path[:]
        return
    visited[x][y]=True
    for i in range(4):
        x1=x+dx[i]
        y1=y+dy[i]
        if 0<=x1<n and 0<=y1<m and (not visited[x1][y1]):
            num1=num+matrix[x1][y1]
            path.append((x1,y1))
            dfs(x1,y1,num1)
            path.pop()
    visited[x][y]=False



n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
visited=[[False for i in range(m)] for j in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
max_num=-float('inf')
best_path=[]
path=[(0,0)]
dfs(0,0,matrix[0][0])
for x,y in best_path:
    print(x+1,y+1)