n,m=map(int,input().split())
building=[]
for i in range(n):
    building.append(list(map(int,input().split())))
num=0
start=0
a=[1]
while a:
    a=[]
    for i in range(n):
        if building[i][0]<start:
            continue
        s=max(start+building[i][1],building[i][0]+1)
        if s<=m:
            a.append(s)
    if a:
        start=min(a)
        num+=1
print(num)