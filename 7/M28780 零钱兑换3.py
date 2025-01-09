n,m=map(int,input().split())
coin=list(map(int,input().split()))
dp=[float('inf')] * (m+1)
dp[0]=0
for _ in coin:
    for i in range(_,m+1):
        dp[i]=min(dp[i],dp[i-_]+1)
if dp[m]!=float('inf'):
    print(dp[m])
else:
    print(-1)