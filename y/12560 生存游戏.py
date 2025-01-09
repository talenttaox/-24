n,m=map(int,input().split())
cell=[]
cell.append([0]*(m+2))
for i in range(n):
    cell.append([0]+list(map(int,input().split()))+[0])
cell.append([0]*(m+2))
cell_end=[[0]*m for i in range(n)]
for i in range(1,n+1):
    for j in range(1,m+1):
        num=cell[i-1][j-1]+cell[i-1][j]+cell[i-1][j+1]+cell[i+1][j-1]+cell[i+1][j]+cell[i+1][j+1]+cell[i][j-1]+cell[i][j+1]
        if num==2 and cell[i][j]==1:
            cell_end[i-1][j-1]=1
        elif num==3:
            cell_end[i-1][j-1]=1
for i in cell_end:
    print(' '.join(map(str,i)))