n=int(input())
acti=[]
for i in range(n):
    start,end=map(int,input().split())
    acti.append((start+1,end+1))
acti.sort(key=lambda x:x[0])
dp=[0]*62
for i in range(n):
    for j in range(acti[i][1],62):
        dp[j]=max(dp[j],dp[acti[i][0]-1]+1)
print(dp[61])