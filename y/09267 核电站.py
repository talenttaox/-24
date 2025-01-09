n,m=map(int,input().split())
dp=[0 for i in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    if i <m:
        dp[i]=2*dp[i-1]
    elif i==m:
        dp[i]=2*dp[i-1]-1
    else:
        dp[i]=2*dp[i-1]-dp[i-m-1]
print(dp[-1])