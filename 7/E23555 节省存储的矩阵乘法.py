n,m1,m2=map(int,input().split())
matrix1=[[0]*n for i in range(n)]
matrix2=[[0]*n for i in range(n)]
for i in range(m1):
    row,col,num=map(int,input().split())
    matrix1[row][col]= num
for i in range(m2):
    row,col,num=map(int,input().split())
    matrix2[row][col]= num
matrix3=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        sum=0
        for k in range(n):
            sum+=matrix1[i][k]*matrix2[k][j]
        matrix3[i][j]=sum
        if sum!=0:
            print(i,j,sum)