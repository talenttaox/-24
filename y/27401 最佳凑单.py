n,t=map(int,input().split())
value=list(map(int,input().split()))
tot=sum(value)
dp=[[-float('inf')]*(tot+1) for i in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    for j in range(tot+1):
        if value[i-1]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-value[i-1]]+value[i-1])
        else:
            dp[i][j]=dp[i-1][j]
if tot<t:
    print('0')
else:
    for i in range(t,tot+1):
        if dp[n][i]>0:
            print(dp[n][i])
            break
