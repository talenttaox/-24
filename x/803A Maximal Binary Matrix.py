n,k=map(int,input().split())
matrix=[[0]*n for i in range(n)]
if k>n**2:
    print(-1)
else:
    for i in range(n):
        s=i
        if k<=1:
            break
        for j in range(i,n):
            if k<=1:
                break
            elif i==j:
                matrix[i][j]=1
                k-=1
            else:
                matrix[i][j]=matrix[j][i]=1
                k-=2
    if k==1:
        matrix[s][s]=1
    for i in matrix:
        print(' '.join(map(str,i)))