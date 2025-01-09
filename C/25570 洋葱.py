n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
sumn=[]

s=n//2
for k in range(s):
    a=0
    for i in range(k+1,n-k-1):
        a+=matrix[k][i]+matrix[n-k-1][i]+matrix[i][k]+matrix[i][n-k-1]
    a+=matrix[k][k]+matrix[k][n-1-k]+matrix[n-1-k][k]+matrix[n-1-k][n-1-k]
    sumn.append(a)
if n%2!=0:
    sumn.append(matrix[s][s])
print(max(sumn))