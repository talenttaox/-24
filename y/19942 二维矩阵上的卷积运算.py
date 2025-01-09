m,n,p,q=map(int,input().split())
matrix1=[]
matrix2=[]
for i in range(m):
    matrix1.append(list(map(int,input().split())))
for i in range(p):
    matrix2.append(list(map(int,input().split())))
for i in range(m+1-p):
    lst=[]
    for j in range(n+1-q):
        sum=0
        for k in range(p):
            line=0
            for l in range(q):
                line+=matrix1[i+k][j+l]*matrix2[k][l]
            sum+=line
        lst.append(sum)
    print(' '.join(map(str,lst)))