t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=[0]+list(map(int,input().split()))
    p=[0]+list(map(int,input().split()))      
    dp=[[0,0] for i in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        if m[i]>k:
            a=i-1
            while a>0:
                if m[i]-m[a]>k:
                    break
                else:
                    a-=1
            dp[i][1]=max(dp[a][1],dp[a][0])+p[i]
        else:
            dp[i][1]=p[i]
    print(max(dp[-1][0],dp[-1][1]))