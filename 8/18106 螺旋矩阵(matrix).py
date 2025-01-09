n=int(input())
matrix=[]
matrix.append([1]*(n+2))
for i in range(n):
    matrix.append([1]+[0]*n+[1])
matrix.append([1]*(n+2))
matrix[1][0]=0
y=t=0
x=1
while t!=n**2:
    if matrix[x+1][y]==0:
        while matrix[x+1][y]==0:
            matrix[x][y]=t
            t+=1
            x+=1
        if t==n**2:
            matrix[x][y]=t
    elif matrix[x-1][y]==0:
        while matrix[x-1][y]==0:
            matrix[x][y]=t
            t+=1
            x-=1
        if t==n**2:
            matrix[x][y]=t
    elif matrix[x][y+1]==0:
        while matrix[x][y+1]==0:
            matrix[x][y]=t
            t+=1
            y+=1
        if t==n**2:
            matrix[x][y]=t
    elif matrix[x][y-1]==0:
        while matrix[x][y-1]==0:
            matrix[x][y]=t
            t+=1
            y-=1
        if t==n**2:
            matrix[x][y]=t
    elif t==n**2:
        break
for i in range(1,n+1):
    print(' '.join(map(str,matrix[i][1:n+1])))
