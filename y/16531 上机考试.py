m,n=map(int,input().split())
stu=[]
for i in range(m):
    stu.append(list(map(int,input().split())))
test=[[0]*n for i in range(m)]
num=[]
tot=0
each=[]
for i in range(n*m):
    a=list(map(int,input().split()))
    each.append(a)
    num.append(sum(a))
for i in range(m):
    for j in range(n):
        test[i][j]=each[stu[i][j]]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visited=set()
for x in range(m):
    for y in range(n):
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<m and 0<=ny<n:
                if test[x][y]==test[nx][ny]:
                    tot+=1
                    visited.add((x,y))
                    break
#print(visited)
#print(test)         
num.sort(reverse=True)
maxs=0.4*m*n
ex=0
nums=0
while True:
    if ex+nums>maxs:
        break
    ex+=nums
    nums=0
    numt=num[0]
    nums=num.count(numt)
    num=num[nums:]
print(tot,ex)
