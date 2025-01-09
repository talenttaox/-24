t,k=map(int,input().split())
mod=10**9+7
n=100001
dp=[0]*100001
dp[0]=1
s=[0]*100001
for i in range(1,100001):
    if i>=k:
        dp[i]=(dp[i-1]+dp[i-k])%mod
    else:
        dp[i]=1
    s[i]=(s[i-1]+dp[i] )%mod

for _ in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%mod)
