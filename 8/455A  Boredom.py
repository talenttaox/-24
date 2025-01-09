n=int(input())
a=list(map(int,input().split()))
m=100001
lst=[0]*m
for i in a:
    lst[i]+=i
dp=[[0,0] for _ in range(m)]
for i in range(1,m):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1])
    dp[i][1]=dp[i-1][0]+lst[i]
print(max(dp[-1][0],dp[-1][1]))
