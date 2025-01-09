dir=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
area=0

def dfs(x,y,matrix):
    global area
    if matrix[x][y]=='.':
        return
    matrix[x][y]='.'
    area+=1
    for i in range(len(dir)):
        dfs(x+dir[i][0],y+dir[i][1],matrix)

k=int(input())
for _ in range(k):
    n,m=map(int,input().split()) 
    matrix = [['.' for _ in range(m+2)] for _ in range(n+2)]
    for i in range(1,n+1):
        matrix[i][1:-1] = input()
    max_area=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j]=='W':
                area=0
                dfs(i,j,matrix)
                max_area=max(max_area,area)
    print(max_area)