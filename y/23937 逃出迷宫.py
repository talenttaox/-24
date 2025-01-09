def dfs(mx,vis,x,y):
    if x==n-1 and y==n-1:
        return True
    dir=[[0,1],[1,0]]
    for i in dir:
        x1=x+i[0]
        y1=y+i[1]
        if 0<=x1<n and 0<=y1<n and not vis[x1][y1] and mx[x1][y1]==0:
            vis[x1][y1]=True
            if dfs(mx,vis,x1,y1):
                return True
    return False

n=int(input())
mx=[list(map(int,input().split())) for i in range(n)]
vis=[[False]*n for i in range(n)]
if mx[0][0]==1:
    print('No')
else:
    vis[0][0]==True
    if dfs(mx,vis,0,0):
        print('Yes')
    else:
        print('No')