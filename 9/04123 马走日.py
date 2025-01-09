k = 10
dirx = [-2,-1,1,2, 2, 1,-1,-2]
diry = [ 1, 2,2,1,-1,-2,-2,-1]
ans = 0
 
def dfs(num, x, y):
    if n*m == num:
        global ans
        ans += 1
        return
    for r in range(8):
        s = x + dirx[r]
        t = y + diry[r]
        if matrix[s][t]==False and 0<=s<n and 0<=t<m :
            matrix[s][t]=True
            dfs(num+1, s, t)
            matrix[s][t] = False
 
for _ in range(int(input())):
    n,m,x,y = map(int, input().split())
    matrix = [[False]*k for _ in range(k)]
    ans = 0
    matrix[x][y] = True
    dfs(1, x, y)
    print(ans)