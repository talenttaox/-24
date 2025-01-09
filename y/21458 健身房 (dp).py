t,n=map(int,input().split())
ex=[[0,0]]
for i in range(n):
    ex.append(list(map(int,input().split())))
dp=[[0]+[-1]*(t) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(0,t+1):
        if dp[i-1][j-ex[i][0]]>=0 and j>=ex[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-ex[i][0]]+ex[i][1])
        else:
            dp[i][j]=dp[i-1][j]
if dp[-1][-1]==-1:
    print(-1)
else:
    print(dp[-1][-1])