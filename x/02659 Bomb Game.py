a,b,k=map(int,input().split())
area=[[0]*b for i in range(a)]
n=0
for i in range(k):
    r,s,p,t=map(int,input().split())
    if t==1:
        n+=1
        for i in range(max(0,r-p//2-1),min(a,r+p//2)):
            for j in range(max(0,s-p//2-1),min(b,s+p//2)):
                area[i][j]+=1
    else:
        for i in range(max(0,r-p//2-1),min(a,r+p//2)):
            for j in range(max(0,s-p//2-1),min(b,s+p//2)):
                area[i][j]-=1
num=0
for i in range(a):
    num+=area[i].count(n)
print(num)