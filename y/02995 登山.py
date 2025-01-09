n=int(input())
site=list(map(int,input().split()))
site=[-float('inf')]+site
dp1=[0]*(n+1)#上山中
dp2=[0]*(n+1)#下山中
for i in range(1,n+1):
    for j in range(1,i):
        if site[j]<site[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
for i in range(n,0,-1):
    for j in range(n,i,-1):
        if site[j]<site[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)
#print(dp1,dp2)
dp=[]
for i in range(1,n+1):
    dp.append(dp1[i]+dp2[i]+1)
print(max(dp))