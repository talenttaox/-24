n=int(input())
height=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if height[i]<=height[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))