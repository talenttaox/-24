n=int(input())
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        dp[i]+=dp[j]
print(dp[-1])