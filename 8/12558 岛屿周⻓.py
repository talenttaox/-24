n,m=map(int,input().split())
area=[]
length=0
for i in range(n):
    area.append([0]+list(map(int,input().split()))+[0])
area=[[0]*(m+2)]+area+[[0]*(m+2)]
row=[0]
for i in range(1,n+1):
    rowland=(area[i].count(1))
    row.append(rowland)
    if rowland!=0:
        length+=2
        for j in range(1,m+1):
            if area[i][j]==1:
                st=j
                break
        for j in range(st,st+rowland):
            length+=2-(area[i+1][j]+area[i-1][j])
    if rowland==0 and row[i-1]!=0:
        break
print(length)