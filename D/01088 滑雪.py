r,c=map(int,input().split())
hill=[]
height=[]
for i in range(r):
    row=list(map(int,input().split()))
    hill.append(row)
    for j in range(c):
        height.append((row[j],i,j))
height.sort()
#print(height)
length=[[-float('inf')]*c for j in range(r)]
h0,x0,y0=height[0]
length[x0][y0]=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
out=[0]
for i in range(1,r*c):
    h,x,y=height[i]
    length[x][y]=0
    for j in range(4):
        nx,ny=x+dx[j],y+dy[j]
        if 0<=nx<r and 0<=ny<c:
            if length[nx][ny]>=0 and hill[nx][ny]<hill[x][y]:
                length[x][y]=max(length[x][y],length[nx][ny]+1)
    out.append(length[x][y])
print(max(out)+1)